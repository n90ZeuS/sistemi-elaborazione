# T11 — Liste e tuple
# Esercizi per la lezione frontale 11
# Rimozione duplicati, merge liste ordinate, record studenti, media mobile

# =============================================================================
# Esercizio 1: Rimuovi duplicati preservando l'ordine
# Data una lista, restituire una nuova lista senza duplicati
# mantenendo l'ordine di prima apparizione.
# =============================================================================
print("--- Esercizio 1: Rimuovi duplicati (ordine preservato) ---")


def rimuovi_duplicati(lista: list[int]) -> list[int]:
    """
    Rimuove i duplicati da una lista preservando l'ordine di prima apparizione.
    Usa un set per tenere traccia degli elementi gia' visti (O(n)).
    """
    visti: set[int] = set()
    risultato: list[int] = []
    for elem in lista:
        if elem not in visti:
            visti.add(elem)
            risultato.append(elem)
    return risultato


# Test base
assert rimuovi_duplicati([1, 2, 3, 2, 1, 4, 3, 5]) == [1, 2, 3, 4, 5]
assert rimuovi_duplicati([]) == []
assert rimuovi_duplicati([1, 1, 1, 1]) == [1]
assert rimuovi_duplicati([1, 2, 3]) == [1, 2, 3]  # Nessun duplicato

# Test ordine preservato
assert rimuovi_duplicati([5, 3, 5, 1, 3, 2, 1]) == [5, 3, 1, 2]

# Confronto con set() (che NON preserva l'ordine di inserimento garantito)
originale: list[int] = [4, 2, 7, 2, 4, 1, 7, 3]
senza_dup: list[int] = rimuovi_duplicati(originale)
assert len(senza_dup) == len(set(originale))
assert senza_dup == [4, 2, 7, 1, 3]

print(f"  Originale:     {originale}")
print(f"  Senza duplicati: {senza_dup}")

# Test con dati realistici: codici studenti con duplicati
codici: list[int] = [1001, 1003, 1001, 1005, 1003, 1007, 1005, 1009]
codici_unici: list[int] = rimuovi_duplicati(codici)
assert codici_unici == [1001, 1003, 1005, 1007, 1009]
print(f"  Codici: {codici}")
print(f"  Unici:  {codici_unici}")
print("  Esercizio 1 superato!\n")


# =============================================================================
# Esercizio 2: Merge di due liste ordinate
# Date due liste ordinate, produrne una terza ordinata (come merge sort).
# =============================================================================
print("--- Esercizio 2: Merge liste ordinate ---")


def merge_ordinate(lista_a: list[int], lista_b: list[int]) -> list[int]:
    """
    Unisce due liste gia' ordinate in una singola lista ordinata.
    Algoritmo: due puntatori, complessita' O(n + m).
    """
    risultato: list[int] = []
    i: int = 0  # Indice per lista_a
    j: int = 0  # Indice per lista_b

    # Confrontiamo elemento per elemento
    while i < len(lista_a) and j < len(lista_b):
        if lista_a[i] <= lista_b[j]:
            risultato.append(lista_a[i])
            i += 1
        else:
            risultato.append(lista_b[j])
            j += 1

    # Aggiungiamo gli eventuali elementi rimanenti
    risultato.extend(lista_a[i:])
    risultato.extend(lista_b[j:])

    return risultato


# Test base
assert merge_ordinate([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
assert merge_ordinate([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert merge_ordinate([], [1, 2, 3]) == [1, 2, 3]
assert merge_ordinate([1, 2, 3], []) == [1, 2, 3]
assert merge_ordinate([], []) == []

# Test con duplicati
assert merge_ordinate([1, 3, 3, 5], [2, 3, 4]) == [1, 2, 3, 3, 3, 4, 5]

# Test con liste di lunghezza molto diversa
assert merge_ordinate([1], [2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]

# Verifica che il risultato sia effettivamente ordinato
a: list[int] = [2, 5, 11, 23, 45]
b: list[int] = [1, 8, 12, 30, 50, 55]
merged: list[int] = merge_ordinate(a, b)
assert merged == sorted(a + b)  # Deve coincidere con il sort nativo
for k in range(len(merged) - 1):
    assert merged[k] <= merged[k + 1], "Il risultato deve essere ordinato"

print(f"  Lista A: {a}")
print(f"  Lista B: {b}")
print(f"  Merge:   {merged}")
print("  Esercizio 2 superato!\n")


# =============================================================================
# Esercizio 3: Record studenti con tuple
# Gestire un registro studenti usando liste di tuple (nome, matricola, voti).
# =============================================================================
print("--- Esercizio 3: Record studenti con tuple ---")

from collections import namedtuple

# Definiamo il tipo Studente come named tuple
Studente = namedtuple("Studente", ["nome", "matricola", "voti"])

# Database degli studenti
studenti: list[Studente] = [
    Studente("Alice Rossi", "MAT001", (28, 30, 25, 27, 30)),
    Studente("Bob Bianchi", "MAT002", (22, 18, 20, 24, 19)),
    Studente("Carla Verdi", "MAT003", (30, 30, 28, 30, 29)),
    Studente("Davide Neri", "MAT004", (18, 20, 15, 22, 19)),
    Studente("Elena Gialli", "MAT005", (25, 27, 26, 28, 24)),
]


def media_studente(studente: Studente) -> float:
    """Calcola la media dei voti di uno studente."""
    return round(sum(studente.voti) / len(studente.voti), 2)


def trova_per_matricola(
    registro: list[Studente], matricola: str
) -> Studente | None:
    """Cerca uno studente per matricola."""
    for s in registro:
        if s.matricola == matricola:
            return s
    return None


def classifica_studenti(
    registro: list[Studente],
) -> list[tuple[str, float]]:
    """Restituisce la classifica degli studenti per media (decrescente)."""
    classifiche: list[tuple[str, float]] = [
        (s.nome, media_studente(s)) for s in registro
    ]
    classifiche.sort(key=lambda coppia: coppia[1], reverse=True)
    return classifiche


def studenti_sopra_media(
    registro: list[Studente], soglia: float
) -> list[str]:
    """Restituisce i nomi degli studenti con media >= soglia."""
    return [s.nome for s in registro if media_studente(s) >= soglia]


# Test media
assert media_studente(studenti[0]) == 28.0   # Alice: (28+30+25+27+30)/5 = 28
assert media_studente(studenti[1]) == 20.6   # Bob: (22+18+20+24+19)/5 = 20.6

# Test ricerca
alice: Studente | None = trova_per_matricola(studenti, "MAT001")
assert alice is not None
assert alice.nome == "Alice Rossi"
assert trova_per_matricola(studenti, "MAT999") is None

# Test classifica
classifica: list[tuple[str, float]] = classifica_studenti(studenti)
assert classifica[0][0] == "Carla Verdi"  # Media piu' alta
assert classifica[0][1] == 29.4

# Test filtro
bravi: list[str] = studenti_sopra_media(studenti, 25.0)
assert "Alice Rossi" in bravi
assert "Carla Verdi" in bravi
assert "Elena Gialli" in bravi
assert "Bob Bianchi" not in bravi

# Stampa risultati
print(f"  {'Nome':<18}{'Matricola':<12}{'Media':>6}{'Voti'}")
print(f"  {'-' * 60}")
for s in studenti:
    med: float = media_studente(s)
    print(f"  {s.nome:<18}{s.matricola:<12}{med:>6.2f}  {list(s.voti)}")

print(f"\n  Classifica:")
for pos, (nome, media) in enumerate(classifica, start=1):
    print(f"    {pos}. {nome:<18} media: {media:.2f}")

print(f"\n  Studenti con media >= 25: {bravi}")
print("  Esercizio 3 superato!\n")


# =============================================================================
# Esercizio 4: Media mobile (running average)
# Calcolare la media mobile di una serie di dati con finestra di dimensione k.
# =============================================================================
print("--- Esercizio 4: Media mobile (running average) ---")


def media_mobile(dati: list[float], finestra: int) -> list[float]:
    """
    Calcola la media mobile di una serie di dati.
    Per ogni posizione i (da finestra-1 in poi), la media mobile e'
    la media degli ultimi 'finestra' valori: dati[i-finestra+1 : i+1].
    Restituisce una lista di medie, piu' corta di len(dati) - finestra + 1.
    """
    if finestra <= 0:
        raise ValueError("La finestra deve essere positiva")
    if finestra > len(dati):
        return []

    medie: list[float] = []
    for i in range(finestra - 1, len(dati)):
        sottoinsieme: list[float] = dati[i - finestra + 1: i + 1]
        media: float = sum(sottoinsieme) / finestra
        medie.append(round(media, 2))
    return medie


def media_mobile_cumulativa(dati: list[float]) -> list[float]:
    """
    Calcola la media cumulativa: ad ogni punto, la media di tutti
    i dati visti fino a quel momento.
    """
    medie: list[float] = []
    somma: float = 0.0
    for i, valore in enumerate(dati):
        somma += valore
        medie.append(round(somma / (i + 1), 2))
    return medie


# Test media mobile con finestra 3
dati_test: list[float] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
mm3: list[float] = media_mobile(dati_test, 3)
# Finestra 3: [1,2,3]=2.0, [2,3,4]=3.0, [3,4,5]=4.0, [4,5,6]=5.0, [5,6,7]=6.0
assert mm3 == [2.0, 3.0, 4.0, 5.0, 6.0]
assert len(mm3) == len(dati_test) - 3 + 1

# Test con finestra 1 (nessun smoothing)
mm1: list[float] = media_mobile(dati_test, 1)
assert mm1 == dati_test

# Test con finestra uguale alla lunghezza dei dati
mm_tutto: list[float] = media_mobile(dati_test, len(dati_test))
assert mm_tutto == [4.0]  # Media di tutti

# Test finestra troppo grande
assert media_mobile([1.0, 2.0], 5) == []

# Test media cumulativa
mc: list[float] = media_mobile_cumulativa([10.0, 20.0, 30.0, 40.0])
assert mc == [10.0, 15.0, 20.0, 25.0]

# Esempio realistico: temperature giornaliere (una settimana)
temperature: list[float] = [
    15.2, 16.1, 14.8, 17.3, 18.5, 16.9, 15.7,
    14.2, 13.8, 16.4, 17.8, 19.1, 18.3, 17.5,
]

mm_3giorni: list[float] = media_mobile(temperature, 3)
mm_5giorni: list[float] = media_mobile(temperature, 5)

print(f"  Temperature giornaliere: {temperature}")
print(f"  Media mobile (3 giorni): {mm_3giorni}")
print(f"  Media mobile (5 giorni): {mm_5giorni}")

# Verifica che la media mobile "liscia" i dati
# La varianza della media mobile deve essere minore di quella dei dati originali
def varianza(dati: list[float]) -> float:
    """Calcola la varianza di una lista di numeri."""
    n: int = len(dati)
    med: float = sum(dati) / n
    return sum((x - med) ** 2 for x in dati) / n

var_originale: float = varianza(temperature)
var_mm3: float = varianza(mm_3giorni)
var_mm5: float = varianza(mm_5giorni)

assert var_mm3 < var_originale  # La media mobile riduce la varianza
assert var_mm5 < var_mm3        # Finestra piu' grande = piu' smoothing

print(f"\n  Varianza originale: {var_originale:.4f}")
print(f"  Varianza MM(3):    {var_mm3:.4f}")
print(f"  Varianza MM(5):    {var_mm5:.4f}")
print(f"  (la media mobile riduce la varianza, finestra piu' grande = piu' liscia)")
print("  Esercizio 4 superato!\n")


print("Tutti gli esercizi T11 completati con successo!")
