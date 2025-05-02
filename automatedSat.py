import csv
import time
from generator import generate_clauses
from SatSolver import resolution, dp_algorithm, dpll_algorithm

def run_generator_and_solver(num_sets, num_clauses, max_literal):
    output_file = "results.csv"
    methods = [
        ("Rezolutie", resolution),
        ("DP", dp_algorithm),
        ("DPLL", dpll_algorithm),
    ]

    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Set", "Metodă", "Timp (ms)", "Rezultat"])

        for set_index in range(1, num_sets + 1):
            print(f"Se generează setul {set_index}...")
            clauses = generate_clauses(num_clauses, max_literal)
            print(f"Multimea de clauze {set_index} a fost generata cu {len(clauses)} clauze.")

            for method_name, method in methods:
                start_time = time.time_ns()
                result = method(clauses)
                elapsed_time = (time.time_ns() - start_time) / 1_000_000

                writer.writerow([set_index, method_name, elapsed_time, result])
                print(f"Metodă: {method_name}, Timp: {elapsed_time:.10f} s, Rezultat: {result}")

    print(f"Rezultatele au fost scrise în fișierul {output_file}")

if __name__ == "__main__":
    try:
        num_sets = int(input("Introduceți numărul de multimi de clauze de generat: "))
        num_clauses = int(input("Introduceți numărul de clauze: "))
        max_literal = int(input("Introduceți valoarea maximă a unui literal: "))
        run_generator_and_solver(num_sets, num_clauses, max_literal)
    except ValueError:
        print("Optiune invalidă. Vă rugăm să introduceți numere valide.")
