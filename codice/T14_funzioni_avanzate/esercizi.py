# F14 — Funzioni avanzate, moduli
# Esercizi per la lezione frontale 14

import time
import statistics
from typing import Callable, TypeVar

T = TypeVar("T")
R = TypeVar("R")

# ============================================================
# ESERCIZIO 1: Implementare map e filter personalizzati
# ============================================================
print("=== Esercizio 1: map e filter personalizzati ===")


def mia_map(
    funzione: Callable[[T], R],
    iterabile: list[T]
) -> list[R]:
    """
    Implementazione personalizzata di map().
    Applica la funzione a ogni elemento e restituisce una nuova lista.
    """
    risultato: list[R] = []
    for elemento in iterabile:
        risultato.append(funzione(elemento))
    return risultato


def mia_filter(
    predicato: Callable[[T], bool],
    iterabile: list[T]
) -> list[T]:
    """
    Implementazione personalizzata di filter().
    Restituisce gli elementi per cui il predicato è True.
    """
    risultato: list[T] = []
    for elemento in iterabile:
        if predicato(elemento):
            risultato.append(elemento)
    return risultato


def mia_reduce(
    funzione: Callable[[T, T], T],
    iterabile: list[T],
    iniziale: T | None = None
) -> T:
    """
    Implementazione personalizzata di reduce().
    Applica la funzione cumulativamente agli elementi.
    """
    it = iter(iterabile)
    if iniziale is not None:
        accumulatore: T = iniziale
    else:
        accumulatore = next(it)
    for elemento in it:
        accumulatore = funzione(accumulatore, elemento)
    return accumulatore


# Test mia_map
numeri: list[int] = [1, 2, 3, 4, 5]
quadrati: list[int] = mia_map(lambda x: x ** 2, numeri)
assert quadrati == [1, 4, 9, 16, 25]
assert quadrati == list(map(lambda x: x ** 2, numeri))
print(f"mia_map(x², {numeri}) = {quadrati}")

stringhe: list[str] = mia_map(str, numeri)
assert stringhe == ["1", "2", "3", "4", "5"]
print(f"mia_map(str, {numeri}) = {stringhe}")

# Test mia_filter
pari: list[int] = mia_filter(lambda x: x % 2 == 0, numeri)
assert pari == [2, 4]
assert pari == list(filter(lambda x: x % 2 == 0, numeri))
print(f"mia_filter(pari, {numeri}) = {pari}")

positivi: list[int] = mia_filter(lambda x: x > 0, [-3, -1, 0, 2, 5])
assert positivi == [2, 5]
print(f"mia_filter(positivi, [-3,-1,0,2,5]) = {positivi}")

# Test mia_reduce
somma: int = mia_reduce(lambda a, b: a + b, numeri)
assert somma == 15
print(f"mia_reduce(+, {numeri}) = {somma}")

prodotto: int = mia_reduce(lambda a, b: a * b, numeri, 1)
assert prodotto == 120
print(f"mia_reduce(*, {numeri}) = {prodotto}")

# Combinazione: somma dei quadrati dei pari
risultato: int = mia_reduce(
    lambda a, b: a + b,
    mia_map(lambda x: x ** 2, mia_filter(lambda x: x % 2 == 0, range(1, 11))),
    0
)
assert risultato == 4 + 16 + 36 + 64 + 100  # = 220
print(f"Somma dei quadrati dei pari (1-10): {risultato}")

print("Esercizio 1 superato!\n")

# ============================================================
# ESERCIZIO 2: Decoratore per timing
# Creare un decoratore che misura e registra i tempi di esecuzione.
# ============================================================
print("=== Esercizio 2: Decoratore timing avanzato ===")

# Registro globale dei tempi (per scopi didattici)
registro_tempi: dict[str, list[float]] = {}


def cronometra(func: Callable) -> Callable:
    """
    Decoratore che misura il tempo di esecuzione e lo registra
    nel registro globale.
    """
    def wrapper(*args, **kwargs):
        inizio: float = time.perf_counter()
        risultato = func(*args, **kwargs)
        fine: float = time.perf_counter()
        durata: float = fine - inizio
        nome: str = func.__name__
        if nome not in registro_tempi:
            registro_tempi[nome] = []
        registro_tempi[nome].append(durata)
        return risultato
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


def conta_chiamate(func: Callable) -> Callable:
    """Decoratore che conta il numero di chiamate a una funzione."""
    contatore: list[int] = [0]

    def wrapper(*args, **kwargs):
        contatore[0] += 1
        risultato = func(*args, **kwargs)
        return risultato

    wrapper.__name__ = func.__name__
    wrapper.chiamate = lambda: contatore[0]  # type: ignore
    return wrapper


@cronometra
def somma_lenta(n: int) -> int:
    """Somma i primi n numeri (versione iterativa)."""
    totale: int = 0
    for i in range(n + 1):
        totale += i
    return totale


@cronometra
def somma_veloce(n: int) -> int:
    """Somma i primi n numeri (formula di Gauss)."""
    return n * (n + 1) // 2


@conta_chiamate
def fibonacci(n: int) -> int:
    """Calcola l'n-esimo numero di Fibonacci (iterativo)."""
    if n <= 1:
        return n
    a: int = 0
    b: int = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Test timing
n_test: int = 100_000
ris_lenta: int = somma_lenta(n_test)
ris_veloce: int = somma_veloce(n_test)
assert ris_lenta == ris_veloce
print(f"Somma lenta({n_test}) = {ris_lenta}")
print(f"Somma veloce({n_test}) = {ris_veloce}")

# Eseguiamo più volte per avere statistiche
for _ in range(5):
    somma_lenta(n_test)
    somma_veloce(n_test)

for nome, tempi in registro_tempi.items():
    media_t: float = sum(tempi) / len(tempi)
    print(f"  {nome}: media={media_t:.6f}s ({len(tempi)} chiamate)")

# Test conta_chiamate
for i in range(10):
    fibonacci(i)
assert fibonacci.chiamate() == 10
print(f"\nfibonacci chiamata {fibonacci.chiamate()} volte")
print(f"fibonacci(9) = {fibonacci(9)}")
assert fibonacci.chiamate() == 11  # una chiamata in più

print("Esercizio 2 superato!\n")

# ============================================================
# ESERCIZIO 3: Confronto con modulo statistics
# Implementare funzioni statistiche e confrontare con statistics.
# ============================================================
print("=== Esercizio 3: Confronto con modulo statistics ===")


def mia_media(valori: list[float]) -> float:
    """Calcola la media aritmetica."""
    return sum(valori) / len(valori)


def mia_varianza(valori: list[float]) -> float:
    """Calcola la varianza campionaria (n-1)."""
    m: float = mia_media(valori)
    return sum((x - m) ** 2 for x in valori) / (len(valori) - 1)


def mia_deviazione_standard(valori: list[float]) -> float:
    """Calcola la deviazione standard campionaria."""
    return mia_varianza(valori) ** 0.5


def mia_mediana(valori: list[float]) -> float:
    """Calcola la mediana."""
    ordinati: list[float] = sorted(valori)
    n: int = len(ordinati)
    mid: int = n // 2
    if n % 2 == 1:
        return ordinati[mid]
    return (ordinati[mid - 1] + ordinati[mid]) / 2


def mia_correlazione(x: list[float], y: list[float]) -> float:
    """
    Calcola il coefficiente di correlazione di Pearson tra due liste.
    """
    n: int = len(x)
    media_x: float = mia_media(x)
    media_y: float = mia_media(y)
    numeratore: float = sum((xi - media_x) * (yi - media_y) for xi, yi in zip(x, y))
    den_x: float = sum((xi - media_x) ** 2 for xi in x) ** 0.5
    den_y: float = sum((yi - media_y) ** 2 for yi in y) ** 0.5
    if den_x == 0 or den_y == 0:
        return 0.0
    return numeratore / (den_x * den_y)


# Dati di test
dati: list[float] = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]

# Confronto con statistics
tolleranza: float = 1e-9

mia_m: float = mia_media(dati)
lib_m: float = statistics.mean(dati)
assert abs(mia_m - lib_m) < tolleranza
print(f"Media:     mia={mia_m:.6f}  lib={lib_m:.6f}  OK")

mia_v: float = mia_varianza(dati)
lib_v: float = statistics.variance(dati)
assert abs(mia_v - lib_v) < tolleranza
print(f"Varianza:  mia={mia_v:.6f}  lib={lib_v:.6f}  OK")

mia_ds: float = mia_deviazione_standard(dati)
lib_ds: float = statistics.stdev(dati)
assert abs(mia_ds - lib_ds) < tolleranza
print(f"Dev.std:   mia={mia_ds:.6f}  lib={lib_ds:.6f}  OK")

mia_med: float = mia_mediana(dati)
lib_med: float = statistics.median(dati)
assert abs(mia_med - lib_med) < tolleranza
print(f"Mediana:   mia={mia_med:.6f}  lib={lib_med:.6f}  OK")

# Test correlazione
ore_studio: list[float] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
voti: list[float] = [18.0, 20.0, 22.0, 24.0, 26.0, 27.0, 29.0, 30.0]
corr: float = mia_correlazione(ore_studio, voti)
assert corr > 0.99  # correlazione quasi perfetta
print(f"\nCorrelazione ore_studio vs voti: {corr:.4f}")

# Correlazione negativa
temperature: list[float] = [30.0, 25.0, 20.0, 15.0, 10.0]
vendite_cappotti: list[float] = [10.0, 20.0, 35.0, 50.0, 70.0]
corr_neg: float = mia_correlazione(temperature, vendite_cappotti)
assert corr_neg < -0.95  # correlazione negativa forte
print(f"Correlazione temperatura vs vendite_cappotti: {corr_neg:.4f}")

print("\nEsercizio 3 superato!")
print("\n=== Tutti gli esercizi F14 completati! ===")
