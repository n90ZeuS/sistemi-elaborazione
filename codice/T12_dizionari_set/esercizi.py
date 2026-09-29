# T12 — Dizionari, set e mutabilità
# Esercizi per la lezione frontale 12

# ============================================================
# ESERCIZIO 1: Analisi di frequenza
# Dato un testo, calcolare la frequenza di ogni carattere (esclusi spazi).
# ============================================================
print("=== Esercizio 1: Analisi di frequenza ===")


def analisi_frequenza(testo: str) -> dict[str, int]:
    """Conta la frequenza di ogni carattere nel testo, escludendo gli spazi."""
    frequenze: dict[str, int] = {}
    for carattere in testo.lower():
        if carattere != " ":
            frequenze[carattere] = frequenze.get(carattere, 0) + 1
    return frequenze


def frequenza_relativa(frequenze: dict[str, int]) -> dict[str, float]:
    """Calcola la frequenza relativa (proporzione) di ogni carattere."""
    totale: int = sum(frequenze.values())
    return {car: conteggio / totale for car, conteggio in frequenze.items()}


# Test
testo_test: str = "abracadabra"
freq: dict[str, int] = analisi_frequenza(testo_test)
assert freq["a"] == 5
assert freq["b"] == 2
assert freq["r"] == 2
assert freq["c"] == 1
assert freq["d"] == 1
print(f"Frequenze di '{testo_test}': {freq}")

freq_rel: dict[str, float] = frequenza_relativa(freq)
assert abs(freq_rel["a"] - 5 / 11) < 1e-9
print(f"Frequenze relative: { {k: f'{v:.3f}' for k, v in freq_rel.items()} }")

# Test con frase più lunga
frase: str = "il gatto sul tetto"
freq_frase: dict[str, int] = analisi_frequenza(frase)
assert freq_frase["t"] == 5
assert freq_frase["l"] == 2
assert " " not in freq_frase  # gli spazi devono essere esclusi
print(f"Frequenze di '{frase}': {freq_frase}")

print("Esercizio 1 superato!\n")

# ============================================================
# ESERCIZIO 2: Indice invertito
# Dato un insieme di documenti (lista di stringhe), creare un indice
# invertito: per ogni parola, la lista degli indici dei documenti
# in cui appare.
# ============================================================
print("=== Esercizio 2: Indice invertito ===")


def crea_indice_invertito(documenti: list[str]) -> dict[str, list[int]]:
    """
    Crea un indice invertito: per ogni parola (minuscola),
    restituisce la lista ordinata degli indici dei documenti che la contengono.
    """
    indice: dict[str, set[int]] = {}
    for i, doc in enumerate(documenti):
        parole: list[str] = doc.lower().split()
        for parola in parole:
            if parola not in indice:
                indice[parola] = set()
            indice[parola].add(i)
    # Convertiamo i set in liste ordinate
    return {parola: sorted(docs) for parola, docs in indice.items()}


def cerca(indice: dict[str, list[int]], parola: str) -> list[int]:
    """Cerca una parola nell'indice invertito."""
    return indice.get(parola.lower(), [])


# Test
documenti: list[str] = [
    "Il gatto mangia il pesce",       # doc 0
    "Il cane corre nel parco",         # doc 1
    "Il gatto e il cane sono amici",   # doc 2
    "Il pesce nuota nel mare",         # doc 3
]

indice: dict[str, list[int]] = crea_indice_invertito(documenti)
assert cerca(indice, "gatto") == [0, 2]
assert cerca(indice, "pesce") == [0, 3]
assert cerca(indice, "cane") == [1, 2]
assert cerca(indice, "il") == [0, 1, 2, 3]
assert cerca(indice, "dinosauro") == []

print(f"Documenti con 'gatto': {cerca(indice, 'gatto')}")
print(f"Documenti con 'pesce': {cerca(indice, 'pesce')}")
print(f"Documenti con 'cane': {cerca(indice, 'cane')}")
print(f"Documenti con 'dinosauro': {cerca(indice, 'dinosauro')}")

print("Esercizio 2 superato!\n")

# ============================================================
# ESERCIZIO 3: Contatore di elementi unici
# Implementare funzioni per trovare elementi unici, duplicati
# e contare le occorrenze in una collezione.
# ============================================================
print("=== Esercizio 3: Contatore di elementi unici ===")


def elementi_unici(lista: list[int]) -> set[int]:
    """Restituisce gli elementi che appaiono esattamente una volta."""
    conteggio: dict[int, int] = {}
    for elem in lista:
        conteggio[elem] = conteggio.get(elem, 0) + 1
    return {elem for elem, count in conteggio.items() if count == 1}


def elementi_duplicati(lista: list[int]) -> set[int]:
    """Restituisce gli elementi che appaiono più di una volta."""
    conteggio: dict[int, int] = {}
    for elem in lista:
        conteggio[elem] = conteggio.get(elem, 0) + 1
    return {elem for elem, count in conteggio.items() if count > 1}


def elemento_piu_frequente(lista: list[int]) -> tuple[int, int]:
    """Restituisce l'elemento più frequente e il suo conteggio."""
    conteggio: dict[int, int] = {}
    for elem in lista:
        conteggio[elem] = conteggio.get(elem, 0) + 1
    elemento_max: int = max(conteggio, key=lambda k: conteggio[k])
    return elemento_max, conteggio[elemento_max]


# Test
dati: list[int] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

unici: set[int] = elementi_unici(dati)
assert unici == {4, 9, 2, 6}
print(f"Elementi unici: {sorted(unici)}")

duplicati: set[int] = elementi_duplicati(dati)
assert duplicati == {1, 3, 5}
print(f"Elementi duplicati: {sorted(duplicati)}")

top, conteggio_top = elemento_piu_frequente(dati)
assert top == 5
assert conteggio_top == 3
print(f"Più frequente: {top} (appare {conteggio_top} volte)")

print("Esercizio 3 superato!\n")

# ============================================================
# ESERCIZIO 4: Group by
# Implementare un'operazione di raggruppamento simile a SQL GROUP BY.
# ============================================================
print("=== Esercizio 4: Group by ===")


def group_by(
    records: list[dict[str, str | int | float]],
    chiave: str
) -> dict[str | int | float, list[dict[str, str | int | float]]]:
    """
    Raggruppa una lista di dizionari in base al valore di una chiave.
    Simile a SQL GROUP BY.
    """
    gruppi: dict[str | int | float, list[dict[str, str | int | float]]] = {}
    for record in records:
        valore = record[chiave]
        if valore not in gruppi:
            gruppi[valore] = []
        gruppi[valore].append(record)
    return gruppi


def group_by_aggregate(
    records: list[dict[str, str | int | float]],
    chiave_gruppo: str,
    chiave_valore: str,
) -> dict[str | int | float, dict[str, float]]:
    """
    Raggruppa e calcola statistiche aggregate (somma, media, conteggio)
    per un campo numerico.
    """
    gruppi: dict[str | int | float, list[float]] = {}
    for record in records:
        gruppo = record[chiave_gruppo]
        valore: float = float(record[chiave_valore])
        if gruppo not in gruppi:
            gruppi[gruppo] = []
        gruppi[gruppo].append(valore)

    risultato: dict[str | int | float, dict[str, float]] = {}
    for gruppo, valori in gruppi.items():
        risultato[gruppo] = {
            "conteggio": float(len(valori)),
            "somma": sum(valori),
            "media": sum(valori) / len(valori),
            "minimo": min(valori),
            "massimo": max(valori),
        }
    return risultato


# Test
studenti: list[dict[str, str | int | float]] = [
    {"nome": "Marco", "corso": "Informatica", "voto": 28},
    {"nome": "Laura", "corso": "Matematica", "voto": 30},
    {"nome": "Giulia", "corso": "Informatica", "voto": 30},
    {"nome": "Paolo", "corso": "Matematica", "voto": 25},
    {"nome": "Anna", "corso": "Informatica", "voto": 27},
    {"nome": "Luca", "corso": "Fisica", "voto": 29},
]

# Test group_by
per_corso = group_by(studenti, "corso")
assert len(per_corso["Informatica"]) == 3
assert len(per_corso["Matematica"]) == 2
assert len(per_corso["Fisica"]) == 1
print("Studenti per corso:")
for corso, lista_stud in per_corso.items():
    nomi: list[str] = [s["nome"] for s in lista_stud]
    print(f"  {corso}: {nomi}")

# Test group_by_aggregate
stats_corso = group_by_aggregate(studenti, "corso", "voto")
assert stats_corso["Informatica"]["conteggio"] == 3.0
assert abs(stats_corso["Informatica"]["media"] - 85 / 3) < 1e-9
assert stats_corso["Matematica"]["media"] == 27.5
print("\nStatistiche per corso:")
for corso, stats in stats_corso.items():
    print(f"  {corso}: media={stats['media']:.1f}, "
          f"min={stats['minimo']:.0f}, max={stats['massimo']:.0f}")

print("Esercizio 4 superato!\n")

# ============================================================
# ESERCIZIO BONUS: Operazioni su set per analisi dati
# ============================================================
print("=== Bonus: Operazioni su set per analisi dati ===")


def studenti_in_comune(
    corso_a: set[str], corso_b: set[str]
) -> set[str]:
    """Studenti iscritti a entrambi i corsi."""
    return corso_a & corso_b


def studenti_esclusivi(
    corso_a: set[str], corso_b: set[str]
) -> set[str]:
    """Studenti iscritti solo al corso A e non al corso B."""
    return corso_a - corso_b


def tutti_gli_studenti(*corsi: set[str]) -> set[str]:
    """Unione di tutti gli studenti da più corsi."""
    risultato: set[str] = set()
    for corso in corsi:
        risultato = risultato | corso
    return risultato


# Test
python_corso: set[str] = {"Marco", "Laura", "Giulia", "Anna"}
java_corso: set[str] = {"Marco", "Paolo", "Giulia", "Luca"}
cpp_corso: set[str] = {"Anna", "Luca", "Sara"}

in_comune: set[str] = studenti_in_comune(python_corso, java_corso)
assert in_comune == {"Marco", "Giulia"}
print(f"Python ∩ Java: {sorted(in_comune)}")

solo_python: set[str] = studenti_esclusivi(python_corso, java_corso)
assert solo_python == {"Laura", "Anna"}
print(f"Solo Python: {sorted(solo_python)}")

tutti: set[str] = tutti_gli_studenti(python_corso, java_corso, cpp_corso)
assert tutti == {"Marco", "Laura", "Giulia", "Anna", "Paolo", "Luca", "Sara"}
print(f"Tutti gli studenti: {sorted(tutti)}")

print("Bonus superato!\n")
print("=== Tutti gli esercizi T12 completati! ===")
