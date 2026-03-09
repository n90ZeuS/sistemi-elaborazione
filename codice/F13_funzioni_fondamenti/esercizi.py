# F13 — Funzioni: fondamenti
# Esercizi per la lezione frontale 13

import math

# ============================================================
# ESERCIZIO 1: Varianza campionaria
# Implementare la varianza campionaria (divisore n-1).
# ============================================================
print("=== Esercizio 1: Varianza campionaria ===")


def media(valori: list[float]) -> float:
    """Calcola la media aritmetica."""
    if not valori:
        raise ValueError("La lista non può essere vuota")
    return sum(valori) / len(valori)


def varianza_campionaria(valori: list[float]) -> float:
    """
    Calcola la varianza campionaria (con divisore n-1).
    Formula: s² = Σ(xi - x̄)² / (n - 1)
    """
    if len(valori) < 2:
        raise ValueError("Servono almeno 2 valori per la varianza campionaria")
    m: float = media(valori)
    somma_scarti_quadrati: float = sum((x - m) ** 2 for x in valori)
    return somma_scarti_quadrati / (len(valori) - 1)


# Test
dati_1: list[float] = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
var_1: float = varianza_campionaria(dati_1)
# Media = 5.0, varianza campionaria = 4.571428...
assert abs(media(dati_1) - 5.0) < 1e-9
assert abs(var_1 - 32 / 7) < 1e-9
print(f"Dati: {dati_1}")
print(f"Media: {media(dati_1)}")
print(f"Varianza campionaria: {var_1:.4f}")

# Test con dati uniformi (varianza = 0)
dati_uniformi: list[float] = [5.0, 5.0, 5.0, 5.0]
assert varianza_campionaria(dati_uniformi) == 0.0
print(f"Varianza di {dati_uniformi}: {varianza_campionaria(dati_uniformi)}")

print("Esercizio 1 superato!\n")

# ============================================================
# ESERCIZIO 2: Deviazione standard campionaria
# Implementare la deviazione standard campionaria.
# ============================================================
print("=== Esercizio 2: Deviazione standard ===")


def deviazione_standard(valori: list[float]) -> float:
    """
    Calcola la deviazione standard campionaria.
    Formula: s = √(varianza_campionaria)
    """
    return math.sqrt(varianza_campionaria(valori))


# Test
dati_2: list[float] = [10.0, 12.0, 23.0, 23.0, 16.0, 23.0, 21.0, 16.0]
ds: float = deviazione_standard(dati_2)
media_2: float = media(dati_2)
assert abs(media_2 - 18.0) < 1e-9
print(f"Dati: {dati_2}")
print(f"Media: {media_2}")
print(f"Deviazione standard: {ds:.4f}")

# Verifica: ~68% dei dati entro 1 deviazione standard dalla media
dentro_1ds: int = sum(1 for x in dati_2 if abs(x - media_2) <= ds)
percentuale: float = dentro_1ds / len(dati_2) * 100
print(f"Dati entro 1 DS dalla media: {dentro_1ds}/{len(dati_2)} ({percentuale:.0f}%)")

print("Esercizio 2 superato!\n")

# ============================================================
# ESERCIZIO 3: Mediana
# Implementare il calcolo della mediana.
# ============================================================
print("=== Esercizio 3: Mediana ===")


def mediana(valori: list[float]) -> float:
    """
    Calcola la mediana di una lista di valori.
    Se il numero di valori è dispari, restituisce il valore centrale.
    Se è pari, restituisce la media dei due valori centrali.
    """
    if not valori:
        raise ValueError("La lista non può essere vuota")
    ordinati: list[float] = sorted(valori)
    n: int = len(ordinati)
    indice_medio: int = n // 2
    if n % 2 == 1:
        return ordinati[indice_medio]
    else:
        return (ordinati[indice_medio - 1] + ordinati[indice_medio]) / 2


# Test con numero dispari di elementi
dati_dispari: list[float] = [3.0, 1.0, 4.0, 1.0, 5.0]
med_dispari: float = mediana(dati_dispari)
assert med_dispari == 3.0  # ordinati: [1, 1, 3, 4, 5] → mediana = 3
print(f"Mediana di {dati_dispari}: {med_dispari}")

# Test con numero pari di elementi
dati_pari: list[float] = [1.0, 2.0, 3.0, 4.0]
med_pari: float = mediana(dati_pari)
assert med_pari == 2.5  # media di 2 e 3
print(f"Mediana di {dati_pari}: {med_pari}")

# Test con un solo elemento
assert mediana([42.0]) == 42.0

# Test con dati non ordinati
dati_test: list[float] = [7.0, 1.0, 3.0, 5.0, 9.0, 2.0, 8.0]
assert mediana(dati_test) == 5.0  # ordinati: [1,2,3,5,7,8,9]
print(f"Mediana di {dati_test}: {mediana(dati_test)}")

print("Esercizio 3 superato!\n")

# ============================================================
# ESERCIZIO 4: Moda
# Implementare il calcolo della moda (il valore più frequente).
# ============================================================
print("=== Esercizio 4: Moda ===")


def moda(valori: list[float]) -> list[float]:
    """
    Calcola la moda (valori più frequenti) di una lista.
    Restituisce una lista ordinata perché ci possono essere più mode.
    """
    if not valori:
        raise ValueError("La lista non può essere vuota")
    conteggio: dict[float, int] = {}
    for v in valori:
        conteggio[v] = conteggio.get(v, 0) + 1
    max_freq: int = max(conteggio.values())
    mode: list[float] = sorted(
        [v for v, freq in conteggio.items() if freq == max_freq]
    )
    return mode


# Test moda singola
dati_moda: list[float] = [1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0]
m: list[float] = moda(dati_moda)
assert m == [3.0]
print(f"Moda di {dati_moda}: {m}")

# Test moda multipla (bimodale)
dati_bimodali: list[float] = [1.0, 1.0, 2.0, 3.0, 3.0]
m_bi: list[float] = moda(dati_bimodali)
assert m_bi == [1.0, 3.0]
print(f"Moda di {dati_bimodali}: {m_bi}")

# Test tutti uguali
dati_tutti_uguali: list[float] = [5.0, 5.0, 5.0]
assert moda(dati_tutti_uguali) == [5.0]

# Test tutti diversi (tutti sono moda)
dati_tutti_diversi: list[float] = [1.0, 2.0, 3.0]
assert moda(dati_tutti_diversi) == [1.0, 2.0, 3.0]
print(f"Moda di {dati_tutti_diversi}: {moda(dati_tutti_diversi)}")

print("Esercizio 4 superato!\n")

# ============================================================
# ESERCIZIO 5: Funzioni min/max personalizzate con key
# Implementare versioni personalizzate di min e max.
# ============================================================
print("=== Esercizio 5: Min/Max personalizzati ===")

from typing import Callable, TypeVar

T = TypeVar("T")


def mio_min(
    valori: list[float],
    chiave: Callable[[float], float] | None = None
) -> float:
    """
    Trova il minimo di una lista.
    Se chiave è specificata, il confronto usa chiave(elemento).
    """
    if not valori:
        raise ValueError("La lista non può essere vuota")
    minimo: float = valori[0]
    for v in valori[1:]:
        val_confronto: float = chiave(v) if chiave else v
        val_min: float = chiave(minimo) if chiave else minimo
        if val_confronto < val_min:
            minimo = v
    return minimo


def mio_max(
    valori: list[float],
    chiave: Callable[[float], float] | None = None
) -> float:
    """
    Trova il massimo di una lista.
    Se chiave è specificata, il confronto usa chiave(elemento).
    """
    if not valori:
        raise ValueError("La lista non può essere vuota")
    massimo: float = valori[0]
    for v in valori[1:]:
        val_confronto: float = chiave(v) if chiave else v
        val_max: float = chiave(massimo) if chiave else massimo
        if val_confronto > val_max:
            massimo = v
    return massimo


# Test base
numeri: list[float] = [3.0, 1.0, 4.0, 1.0, 5.0, 9.0, 2.0, 6.0]
assert mio_min(numeri) == 1.0
assert mio_max(numeri) == 9.0
print(f"Min di {numeri}: {mio_min(numeri)}")
print(f"Max di {numeri}: {mio_max(numeri)}")

# Test con chiave — valore più vicino a 5
vicino_a_5: float = mio_min(numeri, chiave=lambda x: abs(x - 5.0))
assert vicino_a_5 == 5.0
print(f"Più vicino a 5: {vicino_a_5}")

# Test con chiave — valore più lontano da 5
lontano_da_5: float = mio_max(numeri, chiave=lambda x: abs(x - 5.0))
assert lontano_da_5 == 1.0
print(f"Più lontano da 5: {lontano_da_5}")

# Test con valori negativi
neg: list[float] = [-3.0, -1.0, -4.0, -1.0, -5.0]
assert mio_min(neg) == -5.0
assert mio_max(neg) == -1.0

print("Esercizio 5 superato!\n")

# ============================================================
# ESERCIZIO 6: Riepilogo statistico completo
# Combinare tutte le funzioni in un riepilogo.
# ============================================================
print("=== Esercizio 6: Riepilogo statistico completo ===")


def riepilogo_statistico(
    valori: list[float],
) -> dict[str, float | list[float]]:
    """Produce un riepilogo statistico completo di una lista di valori."""
    return {
        "n": float(len(valori)),
        "media": media(valori),
        "mediana": mediana(valori),
        "moda": moda(valori),
        "varianza": varianza_campionaria(valori),
        "dev_standard": deviazione_standard(valori),
        "minimo": mio_min(valori),
        "massimo": mio_max(valori),
        "range": mio_max(valori) - mio_min(valori),
    }


# Test con dati di esempio: voti di un esame
voti_esame: list[float] = [
    18.0, 22.0, 25.0, 25.0, 27.0, 28.0, 28.0, 28.0, 30.0, 30.0
]

riep: dict[str, float | list[float]] = riepilogo_statistico(voti_esame)
assert riep["n"] == 10.0
assert riep["minimo"] == 18.0
assert riep["massimo"] == 30.0
assert riep["range"] == 12.0

print(f"Voti: {voti_esame}")
print(f"{'Statistica':<20} {'Valore':>10}")
print("-" * 32)
for chiave, valore in riep.items():
    if isinstance(valore, list):
        print(f"{chiave:<20} {str(valore):>10}")
    else:
        print(f"{chiave:<20} {valore:>10.4f}")

print("\nEsercizio 6 superato!")
print("\n=== Tutti gli esercizi F13 completati! ===")
