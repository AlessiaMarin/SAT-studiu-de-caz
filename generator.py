import random
import math


def calculate_max_unique_clauses(max_literal):
    return 2 ** max_literal - 1


def generate_clause(max_literal):
    num_literals = random.randint(1, max_literal - 1)
    clause = set()
    while len(clause) < num_literals:
        literal = random.randint(1, max_literal)
        if random.choice([True, False]):
            literal *= -1
        if literal not in clause and -literal not in clause:
            clause.add(literal)
    return tuple(sorted(clause))


def generate_clauses(num_clauses, max_literal):
    unique_clauses = set()
    while len(unique_clauses) < num_clauses:
        clause = generate_clause(max_literal)
        unique_clauses.add(clause)
    return [list(clause) for clause in unique_clauses]


num_clauses = int(input("Introduceti numarul de clauze: "))
max_literal = int(input("Introduceti valoarea maxima a literalului: "))

max_unique_clauses = calculate_max_unique_clauses(max_literal)

if num_clauses > max_unique_clauses:
    print(
        f"Eroare: Ati cerut {num_clauses} clauze, dar doar {max_unique_clauses} clauze unice sunt posibile cu valoarea maxima de literal={max_literal}.")
    print("Reduceti numarul de clauze sau cresteti valoarea maxima a literalului ")
else:
    clauses = generate_clauses(num_clauses, max_literal)

    with open("clauses.txt", "w") as file:
        for clause in clauses:
            file.write(" ".join(map(str, sorted(clause))) + "\n")

    print("\nClauzele generate au fost scrise in clauses.txt")
