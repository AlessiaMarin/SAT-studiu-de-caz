import time
from collections import Counter


def read_clauses():
    try:
        with open("clauses.txt", "r") as file:
            clauses = [list(map(int, line.strip().split())) for line in file.readlines()]
        return clauses
    except FileNotFoundError:
        print("Eroare: 'clauses.txt' nu a fost gasit.")
        return []


def print_clauses(clauses, title="Clauze"):
    print(f"\n{title}:")
    for i, clause in enumerate(clauses, 1):
        print(f"{i:>2}: {' ∨ '.join(map(str, clause))}")


def resolve(clause1, clause2):
    resolved = None
    for literal in clause1:
        if -literal in clause2:
            resolvent = set(clause1).union(set(clause2))
            resolvent.discard(literal)
            resolvent.discard(-literal)
            if any(lit in resolvent and -lit in resolvent for lit in resolvent):
                return None
            if resolved is not None:
                return None
            resolved = resolvent
    return list(resolved) if resolved is not None else None


def resolution(clauses):
    new_clauses = set(map(lambda c: tuple(sorted(c)), clauses))
    while True:
        pairs = [(c1, c2) for i, c1 in enumerate(clauses) for c2 in clauses[i + 1:]]
        added_new_resolvents = False
        for c1, c2 in pairs:
            resolvent = resolve(c1, c2)
            if resolvent is None:
                continue
            if not resolvent:
                return "NESATISFIABIL"
            sorted_resolvent = tuple(sorted(resolvent))
            if sorted_resolvent not in new_clauses:
                new_clauses.add(sorted_resolvent)
                clauses.append(resolvent)
                added_new_resolvents = True
        if not added_new_resolvents:
            break
    return "SATISFIABIL"


def unit_propagation(clauses):
    clauses = [list(c) for c in clauses]  # Make a copy
    while True:
        unit_clauses = [c[0] for c in clauses if len(c) == 1]
        if not unit_clauses:
            break
        unit = unit_clauses[0]
        new_clauses = []
        for clause in clauses:
            if unit in clause:
                continue
            if -unit in clause:
                new_clause = [lit for lit in clause if lit != -unit]
                if not new_clause:
                    return [[]]
                new_clauses.append(new_clause)
            else:
                new_clauses.append(clause)
        clauses = new_clauses
    return clauses


def pure_literal_elimination(clauses):
    literals = [lit for clause in clauses for lit in clause]
    counter = Counter(literals)
    pure_literals = [lit for lit in counter if -lit not in counter]
    return [c for c in clauses if not any(lit in c for lit in pure_literals)]


def dp_algorithm(clauses):

    while True:
        prev_clause_count = len(clauses)
        clauses = unit_propagation(clauses)
        if any(len(c) == 0 for c in clauses):
            return "NESATISFIABIL"
        if not clauses:
            return "SATISFIABIL"

        clauses = pure_literal_elimination(clauses)
        if not clauses:
            return "SATISFIABIL"
        if len(clauses) == prev_clause_count:
            break
    return resolution(clauses)


def select_literal(clauses):
    literal_counts = Counter(lit for clause in clauses for lit in clause)
    return max(literal_counts, key=literal_counts.get)


def split(clauses, literal):
    def assign(clauses, value):
        return [
            [lit for lit in clause if lit != -value]
            for clause in clauses
            if value not in clause
        ]

    if dpll_algorithm(assign(clauses, literal)) == "SATISFIABIL":
        return "SATISFIABIL"
    return dpll_algorithm(assign(clauses, -literal))

def dpll_algorithm(clauses):
    clauses = unit_propagation(clauses)
    if any(len(clause) == 0 for clause in clauses):
        return "NESATISFIABIL"
    if not clauses:
        return "SATISFIABIL"

    clauses = pure_literal_elimination(clauses)
    if not clauses:
        return "SATISFIABIL"

    literal = select_literal(clauses)
    return split(clauses, literal)


def measure_time(func, *args):
    start = time.time_ns()
    result = func(*args)
    end = time.time_ns()
    return result, (end - start) / 1_000_000_000


def main():
    print("Alegeti o metoda:")
    print("1. Rezolutie")
    print("2. DP")
    print("3. DPLL")
    try:
        choice = int(input("Optiunea (1/2/3): "))
        clauses = read_clauses()
        if not clauses:
            return
        result = None
        elapsed_time = 0
        if choice == 1:
            result, elapsed_time = measure_time(resolution, clauses)
        elif choice == 2:
            result, elapsed_time = measure_time(dp_algorithm, clauses)
        elif choice == 3:
            result, elapsed_time = measure_time(dpll_algorithm, clauses)
        else:
            print("Optiune invalida.")
            return
        print("\nRezultat:", result)
        print(f"Timp de executie: {elapsed_time:.10f} s")
    except ValueError:
        print("Introduceti un numar valid.")


if __name__ == "__main__":
    main()
