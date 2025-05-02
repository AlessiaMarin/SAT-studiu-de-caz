# SAT - Studiu de caz

Sunt prezente 3 fișiere `.py`:

- un generator de clauze,
- un program care conține algoritmi pentru rezolvarea satisfiabilității: rezoluție, DP și DPLL,
- și un generator automat de mulțimi de clauze, care va reține atât mulțimile de clauze folosite, cât și timpul și rezultatul fiecărei metode.

## Cum testez programele în PyCharm?

### Metoda 1 – Copiere cod sursă
- Se poate copia codul din fiecare fișier într-un fișier nou de același tip (`.py`, `.csv`, `.txt`), apăsând pe fișierul dorit și apoi pe **"Copy raw file"**.
- După ce s-au creat toate fișierele în același folder, se pot rula programele.

### Metoda 2 – Salvare directă
- Se pot salva direct, apăsând pe fișierul dorit și apoi pe **"Download raw file"**.
- După ce au fost salvate toate fișierele într-un folder, se apasă pe **File > Open** în PyCharm și se selectează folderul cu codul necesar.

---

## Cum folosesc codul?

- **`generator.py`** – Este un generator de clauze. Acesta generează o mulțime de clauze, pe care o salvează în `clauses.txt`. Literalii din clauze sunt ordonați crescător și sunt sub formă de numere întregi (ex: `-5 -4 2 3`), unde numerele negative înseamnă negarea literalului.

  Se va introduce:
  - numărul de clauze,
  - valoarea maximă a unui literal.

  **Obs:** Valoarea maximă a unui literal reprezintă numărul de literali pozitivi cu care se va lucra. De exemplu, dacă se introduce 5, literalii vor fi: `1, 2, 3, 4, 5` și negările lor. Numărul de literali dintr-o clauză va fi ales aleatoriu.

- **`SatSolver.py`** – Citește mulțimea de clauze din `clauses.txt` și verifică dacă este satisfiabilă. Utilizatorul introduce `1`, `2` sau `3`, în funcție de metoda dorită: rezoluție, DP sau DPLL.

  Se va afișa:
  - rezultatul (SATISFIABIL / NESATISFIABIL),
  - timpul de execuție al algoritmului ales (în secunde).

- **`automatedSat.py`** – Generează mai multe mulțimi de clauze, le rezolvă, apoi scrie în fișier:
  - numărul de clauze,
  - timpul de execuție pentru cei trei algoritmi,
  - valoarea maximă a literalului,
  - rezultatul pentru fiecare algoritm.

---
Fișierele .txt conțin mulțimile de clauze pe care le-am folosit pentru a studia cei trei algoritmi.

