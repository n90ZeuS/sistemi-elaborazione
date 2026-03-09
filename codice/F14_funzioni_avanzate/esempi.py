# F14 — Funzioni avanzate, moduli
# Esempi per la lezione frontale 14

import time
import math
import random
import statistics
from collections import Counter, defaultdict
from typing import Callable, TypeVar

T = TypeVar("T")
R = TypeVar("R")

# ============================================================
# 1. FUNZIONI COME OGGETTI DI PRIMA CLASSE
# ============================================================
print("=== Funzioni come oggetti di prima classe ===")


def quadrato(x: float) -> float:
    """Restituisce il quadrato di x."""
    return x ** 2


def cubo(x: float) -> float:
    """Restituisce il cubo di x."""
    return x ** 3


# Le funzioni sono oggetti: possiamo assegnarle a variabili
operazione: Callable[[float], float] = quadrato
assert operazione(5) == 25
print(f"operazione(5) = {operazione(5)}")

operazione = cubo
assert operazione(5) == 125
print(f"operazione(5) = {operazione(5)}")

# Le funzioni possono stare in una lista
operazioni: list[Callable[[float], float]] = [quadrato, cubo, abs]
for op in operazioni:
    print(f"  {op.__name__}(3) = {op(3)}")

# Le funzioni possono stare in un dizionario
calcolatrice: dict[str, Callable[[float, float], float]] = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}
assert calcolatrice["+"](10, 3) == 13
assert calcolatrice["*"](4, 5) == 20
print(f"10 + 3 = {calcolatrice['+'](10, 3)}")
print(f"4 * 5 = {calcolatrice['*'](4, 5)}")

# ============================================================
# 2. FUNZIONI DI ORDINE SUPERIORE
# ============================================================
print("\n=== Funzioni di ordine superiore ===")


def applica(funzione: Callable[[float], float], valore: float) -> float:
    """Applica una funzione a un valore."""
    return funzione(valore)


assert applica(quadrato, 4) == 16
assert applica(math.sqrt, 16) == 4.0
print(f"applica(quadrato, 4) = {applica(quadrato, 4)}")
print(f"applica(sqrt, 16) = {applica(math.sqrt, 16)}")


def applica_a_lista(
    funzione: Callable[[float], float],
    valori: list[float]
) -> list[float]:
    """Applica una funzione a ogni elemento di una lista."""
    return [funzione(v) for v in valori]


numeri: list[float] = [1.0, 4.0, 9.0, 16.0, 25.0]
radici: list[float] = applica_a_lista(math.sqrt, numeri)
assert radici == [1.0, 2.0, 3.0, 4.0, 5.0]
print(f"Radici quadrate: {radici}")

# ============================================================
# 3. LAMBDA
# ============================================================
print("\n=== Lambda ===")

# Lambda: funzioni anonime per espressioni semplici
doppio: Callable[[float], float] = lambda x: x * 2
assert doppio(5) == 10
print(f"doppio(5) = {doppio(5)}")

# Lambda con più parametri
somma: Callable[[float, float], float] = lambda a, b: a + b
assert somma(3, 4) == 7

# Lambda utile negli argomenti
numeri_int: list[int] = [-5, -2, 0, 3, 7, -1, 4]
ordinati_per_valore_assoluto: list[int] = sorted(numeri_int, key=lambda x: abs(x))
assert ordinati_per_valore_assoluto == [0, -1, -2, 3, 4, -5, 7]
print(f"Ordinati per |x|: {ordinati_per_valore_assoluto}")

# ============================================================
# 4. map(), filter(), sorted() con key
# ============================================================
print("\n=== map, filter, sorted ===")

# map — applica una funzione a ogni elemento
valori: list[int] = [1, 2, 3, 4, 5]
quadrati: list[int] = list(map(lambda x: x**2, valori))
assert quadrati == [1, 4, 9, 16, 25]
print(f"map(x²): {quadrati}")

# filter — filtra gli elementi che soddisfano una condizione
pari: list[int] = list(filter(lambda x: x % 2 == 0, range(1, 11)))
assert pari == [2, 4, 6, 8, 10]
print(f"filter(pari): {pari}")

# sorted con key
studenti: list[dict[str, str | float]] = [
    {"nome": "Marco", "media": 27.5},
    {"nome": "Laura", "media": 29.0},
    {"nome": "Giulia", "media": 28.3},
    {"nome": "Paolo", "media": 25.0},
]

# Ordina per media (crescente)
per_media: list[dict[str, str | float]] = sorted(
    studenti, key=lambda s: s["media"]
)
print("Ordinati per media:")
for s in per_media:
    print(f"  {s['nome']}: {s['media']}")

# Ordina per media (decrescente)
top: list[dict[str, str | float]] = sorted(
    studenti, key=lambda s: s["media"], reverse=True
)
assert top[0]["nome"] == "Laura"
print(f"Migliore studente: {top[0]['nome']} ({top[0]['media']})")

# Combinazione di map e filter
# Trova i quadrati dei numeri pari da 1 a 10
quadrati_pari: list[int] = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(1, 11))))
assert quadrati_pari == [4, 16, 36, 64, 100]
print(f"Quadrati dei pari: {quadrati_pari}")

# ============================================================
# 5. CLOSURES
# ============================================================
print("\n=== Closures ===")


def crea_moltiplicatore(fattore: float) -> Callable[[float], float]:
    """Crea una funzione che moltiplica per un fattore fisso."""
    def moltiplica(x: float) -> float:
        return x * fattore  # 'fattore' viene "catturato" dalla closure
    return moltiplica


doppio_fn: Callable[[float], float] = crea_moltiplicatore(2)
triplo_fn: Callable[[float], float] = crea_moltiplicatore(3)

assert doppio_fn(5) == 10
assert triplo_fn(5) == 15
print(f"doppio(5) = {doppio_fn(5)}")
print(f"triplo(5) = {triplo_fn(5)}")


def crea_contatore(inizio: int = 0) -> Callable[[], int]:
    """Crea un contatore che si incrementa ad ogni chiamata."""
    conteggio: list[int] = [inizio]  # lista per poter modificare nella closure

    def incrementa() -> int:
        conteggio[0] += 1
        return conteggio[0]
    return incrementa


conta: Callable[[], int] = crea_contatore(0)
assert conta() == 1
assert conta() == 2
assert conta() == 3
print(f"Contatore: {conta()}, {conta()}, {conta()}")

# ============================================================
# 6. DECORATORI (base)
# ============================================================
print("\n=== Decoratori ===")


def log_chiamata(func: Callable) -> Callable:
    """Decoratore che stampa quando una funzione viene chiamata."""
    def wrapper(*args, **kwargs):
        print(f"  [LOG] Chiamata a {func.__name__} con args={args}")
        risultato = func(*args, **kwargs)
        print(f"  [LOG] {func.__name__} ha restituito {risultato}")
        return risultato
    wrapper.__name__ = func.__name__
    return wrapper


@log_chiamata
def fattoriale(n: int) -> int:
    """Calcola il fattoriale di n."""
    if n <= 1:
        return 1
    risultato: int = 1
    for i in range(2, n + 1):
        risultato *= i
    return risultato


# La decorazione equivale a: fattoriale = log_chiamata(fattoriale)
risultato_fatt: int = fattoriale(5)
assert risultato_fatt == 120

# ============================================================
# 7. DECORATORE PER MISURARE IL TEMPO
# ============================================================
print("\n=== Decoratore timing ===")


def misura_tempo(func: Callable) -> Callable:
    """Decoratore che misura il tempo di esecuzione."""
    def wrapper(*args, **kwargs):
        inizio: float = time.perf_counter()
        risultato = func(*args, **kwargs)
        fine: float = time.perf_counter()
        durata: float = fine - inizio
        print(f"  {func.__name__} eseguita in {durata:.6f} secondi")
        return risultato
    wrapper.__name__ = func.__name__
    return wrapper


@misura_tempo
def somma_grande(n: int) -> int:
    """Somma i primi n numeri."""
    return sum(range(n + 1))


risultato_somma: int = somma_grande(1_000_000)
assert risultato_somma == 500_000_500_000

# ============================================================
# 8. MODULI E IMPORT
# ============================================================
print("\n=== Moduli e standard library ===")

# math — funzioni matematiche
print(f"pi = {math.pi}")
print(f"e = {math.e}")
print(f"sqrt(2) = {math.sqrt(2):.6f}")
print(f"log(e) = {math.log(math.e):.6f}")
print(f"sin(pi/2) = {math.sin(math.pi / 2):.6f}")

# random — numeri casuali (con seed per riproducibilità)
random.seed(42)
numeri_casuali: list[int] = [random.randint(1, 100) for _ in range(5)]
print(f"\nNumeri casuali (seed 42): {numeri_casuali}")

campione: list[int] = random.sample(range(1, 91), 5)  # 5 numeri unici da 1 a 90
print(f"Campione casuale: {campione}")

# statistics — funzioni statistiche
dati: list[float] = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
print(f"\nstatistics.mean: {statistics.mean(dati)}")
print(f"statistics.median: {statistics.median(dati)}")
print(f"statistics.stdev: {statistics.stdev(dati):.4f}")
print(f"statistics.variance: {statistics.variance(dati):.4f}")

# collections — strutture dati utili
print("\ncollections.Counter:")
parole: list[str] = "il gatto e il cane e il topo".split()
contatore: Counter[str] = Counter(parole)
print(f"  Conteggio: {dict(contatore)}")
print(f"  Più comuni: {contatore.most_common(2)}")

print("\ncollections.defaultdict:")
raggruppamento: defaultdict[str, list[str]] = defaultdict(list)
studenti_dati: list[tuple[str, str]] = [
    ("Informatica", "Marco"),
    ("Matematica", "Laura"),
    ("Informatica", "Giulia"),
    ("Matematica", "Paolo"),
]
for corso, nome in studenti_dati:
    raggruppamento[corso].append(nome)
print(f"  Raggruppamento: {dict(raggruppamento)}")

# ============================================================
# 9. __name__ == "__main__"
# ============================================================
print("\n=== __name__ == '__main__' ===")
print(f"Il valore di __name__ in questo file è: {__name__!r}")
# Quando eseguiamo direttamente questo file, __name__ è '__main__'.
# Quando viene importato da un altro modulo, __name__ è il nome del modulo.

if __name__ == "__main__":
    print("Questo codice viene eseguito solo se il file è lanciato direttamente.")

print("\n=== Fine esempi F14 ===")
