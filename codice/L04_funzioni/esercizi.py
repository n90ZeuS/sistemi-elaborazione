# L04 — Funzioni e modularita'
# Esercizi per il laboratorio 04
#
# Esercizi pratici su funzioni, ricorsione, decoratori, composizione e ricerca.
# Ogni esercizio include assert per verificare la correttezza.

from typing import Callable, Any
import math

# ============================================================================
# ESERCIZIO 1: Fattoriale e Fibonacci ricorsivi
# ============================================================================

def fattoriale_ricorsivo(n: int) -> int:
    """
    Calcola n! con la ricorsione.
    Caso base: 0! = 1, 1! = 1
    Passo ricorsivo: n! = n * (n-1)!
    """
    if n < 0:
        raise ValueError("Il fattoriale non e' definito per numeri negativi")
    if n <= 1:
        return 1
    return n * fattoriale_ricorsivo(n - 1)


def fattoriale_iterativo(n: int) -> int:
    """Calcola n! con un ciclo (versione iterativa per confronto)."""
    if n < 0:
        raise ValueError("Il fattoriale non e' definito per numeri negativi")
    risultato: int = 1
    for i in range(2, n + 1):
        risultato *= i
    return risultato


def fibonacci_ricorsivo(n: int) -> int:
    """
    Calcola l'n-esimo numero di Fibonacci con la ricorsione.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    ATTENZIONE: questa versione ha complessita' esponenziale O(2^n).
    """
    if n < 0:
        raise ValueError("Fibonacci non definito per indici negativi")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_ricorsivo(n - 1) + fibonacci_ricorsivo(n - 2)


def fibonacci_iterativo(n: int) -> int:
    """
    Calcola l'n-esimo numero di Fibonacci iterativamente.
    Complessita' O(n) - molto piu' efficiente della versione ricorsiva.
    """
    if n < 0:
        raise ValueError("Fibonacci non definito per indici negativi")
    if n <= 1:
        return n

    precedente: int = 0
    corrente: int = 1
    for _ in range(2, n + 1):
        precedente, corrente = corrente, precedente + corrente
    return corrente


# --- Test fattoriale ---
assert fattoriale_ricorsivo(0) == 1
assert fattoriale_ricorsivo(1) == 1
assert fattoriale_ricorsivo(5) == 120
assert fattoriale_ricorsivo(10) == 3628800

# Verifica che le due versioni diano lo stesso risultato
for k in range(15):
    assert fattoriale_ricorsivo(k) == fattoriale_iterativo(k)

# --- Test Fibonacci ---
fib_attesi: list[int] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
for i, atteso in enumerate(fib_attesi):
    assert fibonacci_ricorsivo(i) == atteso, f"F({i}) dovrebbe essere {atteso}"
    assert fibonacci_iterativo(i) == atteso

# Verifica proprieta': F(n)^2 - F(n-1)*F(n+1) = (-1)^(n-1) (identita' di Cassini)
for k in range(1, 10):
    fn: int = fibonacci_iterativo(k)
    fn_meno_1: int = fibonacci_iterativo(k - 1)
    fn_piu_1: int = fibonacci_iterativo(k + 1)
    assert fn * fn - fn_meno_1 * fn_piu_1 == (-1) ** (k - 1)
print("Esercizio 1 (Fattoriale e Fibonacci): SUPERATO")


# ============================================================================
# ESERCIZIO 2: Decoratore di memoizzazione
# ============================================================================

def memoize(funzione: Callable) -> Callable:
    """
    Decoratore che implementa la memoizzazione (caching dei risultati).
    Salva il risultato di ogni chiamata in un dizionario.
    Se la funzione viene chiamata di nuovo con gli stessi argomenti,
    restituisce il risultato salvato senza ricalcolare.
    """
    cache: dict[tuple, Any] = {}

    def wrapper(*args: Any) -> Any:
        chiave: tuple = args
        if chiave not in cache:
            cache[chiave] = funzione(*args)
        return cache[chiave]

    # Aggiungiamo un attributo per poter ispezionare la cache nei test
    wrapper.cache = cache  # type: ignore
    wrapper.__name__ = funzione.__name__
    return wrapper


# Fibonacci con memoizzazione: ora e' efficiente anche in forma ricorsiva!
@memoize
def fibonacci_memo(n: int) -> int:
    """Fibonacci ricorsivo con memoizzazione - complessita' O(n)."""
    if n < 0:
        raise ValueError("Fibonacci non definito per indici negativi")
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


# Decoratore contatore di chiamate (utile per verificare la memoizzazione)
def conta_chiamate(funzione: Callable) -> Callable:
    """Decoratore che conta il numero di volte che una funzione viene chiamata."""
    contatore: list[int] = [0]  # lista per mutabilita' nella closure

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        contatore[0] += 1
        return funzione(*args, **kwargs)

    wrapper.contatore = contatore  # type: ignore
    wrapper.__name__ = funzione.__name__
    return wrapper


# --- Test memoizzazione ---
# Fibonacci memoizzato puo' calcolare valori grandi senza problemi
assert fibonacci_memo(50) == 12586269025
assert fibonacci_memo(100) == 354224848179261915075

# La cache deve contenere i risultati calcolati
assert 50 in fibonacci_memo.cache.values() or fibonacci_memo.cache[(50,)] == 12586269025  # type: ignore

# Test decoratore conta_chiamate
@conta_chiamate
def quadrato(x: int) -> int:
    return x * x

_ = quadrato(5)
_ = quadrato(10)
_ = quadrato(15)
assert quadrato.contatore[0] == 3  # type: ignore
print("Esercizio 2 (Memoizzazione): SUPERATO")


# ============================================================================
# ESERCIZIO 3: Toolkit statistico
# ============================================================================

def media(dati: list[float]) -> float:
    """Calcola la media aritmetica."""
    if not dati:
        raise ValueError("Lista vuota")
    return sum(dati) / len(dati)


def mediana(dati: list[float]) -> float:
    """
    Calcola la mediana (valore centrale).
    Per liste di lunghezza pari, restituisce la media dei due valori centrali.
    """
    if not dati:
        raise ValueError("Lista vuota")
    ordinati: list[float] = sorted(dati)
    n: int = len(ordinati)
    centro: int = n // 2

    if n % 2 == 1:
        # Lunghezza dispari: il valore centrale
        return ordinati[centro]
    else:
        # Lunghezza pari: media dei due valori centrali
        return (ordinati[centro - 1] + ordinati[centro]) / 2.0


def moda(dati: list[float]) -> list[float]:
    """
    Calcola la moda (valori piu' frequenti).
    Puo' restituire piu' valori se ci sono piu' mode.
    """
    if not dati:
        raise ValueError("Lista vuota")

    frequenze: dict[float, int] = {}
    for valore in dati:
        frequenze[valore] = frequenze.get(valore, 0) + 1

    max_freq: int = max(frequenze.values())
    # Se tutti i valori hanno la stessa frequenza e appaiono una sola volta,
    # non c'e' una moda significativa; restituiamo comunque tutti
    mode: list[float] = sorted([v for v, f in frequenze.items() if f == max_freq])
    return mode


def varianza(dati: list[float], campione: bool = True) -> float:
    """
    Calcola la varianza.
    campione=True: varianza campionaria (divisione per n-1)
    campione=False: varianza della popolazione (divisione per n)
    """
    if not dati:
        raise ValueError("Lista vuota")
    n: int = len(dati)
    if campione and n < 2:
        raise ValueError("Servono almeno 2 valori per la varianza campionaria")

    m: float = media(dati)
    somma_scarti_quadrati: float = sum((x - m) ** 2 for x in dati)
    divisore: int = (n - 1) if campione else n
    return somma_scarti_quadrati / divisore


def deviazione_standard(dati: list[float], campione: bool = True) -> float:
    """Calcola la deviazione standard (radice quadrata della varianza)."""
    return math.sqrt(varianza(dati, campione))


def sommario_statistico(dati: list[float]) -> dict[str, float]:
    """Genera un sommario statistico completo dei dati."""
    return {
        "n": float(len(dati)),
        "media": round(media(dati), 4),
        "mediana": round(mediana(dati), 4),
        "varianza": round(varianza(dati), 4),
        "dev_std": round(deviazione_standard(dati), 4),
        "minimo": min(dati),
        "massimo": max(dati),
    }


# --- Test toolkit statistico ---
dati_test: list[float] = [4, 8, 6, 5, 3, 7, 9, 1, 2, 10]

assert media(dati_test) == 5.5
assert mediana(dati_test) == 5.5  # valori centrali 5 e 6, media = 5.5
assert mediana([1, 3, 5]) == 3.0   # valore centrale

# Moda
assert moda([1, 2, 2, 3, 3, 3, 4]) == [3]
assert moda([1, 1, 2, 2, 3]) == [1, 2]  # bimodale

# Varianza e deviazione standard (verifica con valori noti)
dati_semplici: list[float] = [2, 4, 4, 4, 5, 5, 7, 9]
media_semplici: float = media(dati_semplici)
assert media_semplici == 5.0

# Varianza della popolazione: sum((x - 5)^2) / 8 = 32/8 = 4.0
var_pop: float = varianza(dati_semplici, campione=False)
assert abs(var_pop - 4.0) < 1e-9

# Varianza campionaria: 32/7 ≈ 4.5714
var_camp: float = varianza(dati_semplici, campione=True)
assert abs(var_camp - 32.0 / 7.0) < 1e-9

# Deviazione standard della popolazione = 2.0
assert abs(deviazione_standard(dati_semplici, campione=False) - 2.0) < 1e-9

# Test sommario
sommario: dict[str, float] = sommario_statistico(dati_semplici)
assert sommario["media"] == 5.0
assert sommario["n"] == 8.0
print("Esercizio 3 (Toolkit statistico): SUPERATO")


# ============================================================================
# ESERCIZIO 4: Composizione di funzioni
# ============================================================================

def componi(f: Callable[[float], float], g: Callable[[float], float]) -> Callable[[float], float]:
    """
    Composizione di due funzioni: (f o g)(x) = f(g(x)).
    Prima si applica g, poi f al risultato.
    """
    def composta(x: float) -> float:
        return f(g(x))
    return composta


def componi_n(*funzioni: Callable[[float], float]) -> Callable[[float], float]:
    """
    Composizione di n funzioni: (f1 o f2 o ... o fn)(x).
    Le funzioni vengono applicate da destra a sinistra:
    prima fn, poi fn-1, ..., infine f1.
    """
    def composta(x: float) -> float:
        risultato: float = x
        # Applica le funzioni da destra a sinistra
        for func in reversed(funzioni):
            risultato = func(risultato)
        return risultato
    return composta


def applica_pipeline(valore: float, *funzioni: Callable[[float], float]) -> float:
    """
    Applica una pipeline di funzioni da sinistra a destra.
    A differenza della composizione matematica, qui le funzioni vengono
    applicate nell'ordine in cui sono elencate.
    """
    risultato: float = valore
    for func in funzioni:
        risultato = func(risultato)
    return risultato


# --- Test composizione ---
# Funzioni di test
def raddoppia(x: float) -> float:
    return x * 2

def incrementa(x: float) -> float:
    return x + 1

def quadrato_f(x: float) -> float:
    return x * x

# f o g: raddoppia(incrementa(3)) = raddoppia(4) = 8
f_composta: Callable[[float], float] = componi(raddoppia, incrementa)
assert f_composta(3) == 8

# g o f: incrementa(raddoppia(3)) = incrementa(6) = 7
g_composta: Callable[[float], float] = componi(incrementa, raddoppia)
assert g_composta(3) == 7

# Composizione di 3 funzioni: quadrato(raddoppia(incrementa(2)))
# = quadrato(raddoppia(3)) = quadrato(6) = 36
tripla: Callable[[float], float] = componi_n(quadrato_f, raddoppia, incrementa)
assert tripla(2) == 36

# Pipeline (ordine opposto): incrementa, raddoppia, quadrato
# incrementa(2) = 3, raddoppia(3) = 6, quadrato(6) = 36
assert applica_pipeline(2, incrementa, raddoppia, quadrato_f) == 36

# Pipeline con ordine diverso: raddoppia(2) = 4, incrementa(4) = 5, quadrato(5) = 25
assert applica_pipeline(2, raddoppia, incrementa, quadrato_f) == 25
print("Esercizio 4 (Composizione funzioni): SUPERATO")


# ============================================================================
# ESERCIZIO 5: Ricerca binaria
# ============================================================================

def ricerca_binaria(lista: list[float], obiettivo: float) -> int:
    """
    Ricerca binaria iterativa in una lista ordinata.
    Restituisce l'indice dell'elemento cercato, oppure -1 se non trovato.

    Complessita': O(log n)

    Prerequisito: la lista deve essere ordinata in ordine crescente.
    """
    sinistra: int = 0
    destra: int = len(lista) - 1

    while sinistra <= destra:
        centro: int = (sinistra + destra) // 2

        if lista[centro] == obiettivo:
            return centro
        elif lista[centro] < obiettivo:
            # L'obiettivo e' nella meta' destra
            sinistra = centro + 1
        else:
            # L'obiettivo e' nella meta' sinistra
            destra = centro - 1

    return -1  # Non trovato


def ricerca_binaria_ricorsiva(
    lista: list[float], obiettivo: float, sinistra: int = 0, destra: int = -1
) -> int:
    """
    Ricerca binaria ricorsiva in una lista ordinata.
    Restituisce l'indice dell'elemento, oppure -1 se non trovato.
    """
    # Inizializzazione: destra = -1 come valore sentinella
    if destra == -1:
        destra = len(lista) - 1

    # Caso base: intervallo vuoto
    if sinistra > destra:
        return -1

    centro: int = (sinistra + destra) // 2

    if lista[centro] == obiettivo:
        return centro
    elif lista[centro] < obiettivo:
        return ricerca_binaria_ricorsiva(lista, obiettivo, centro + 1, destra)
    else:
        return ricerca_binaria_ricorsiva(lista, obiettivo, sinistra, centro - 1)


def ricerca_inserimento(lista: list[float], valore: float) -> int:
    """
    Trova la posizione in cui un valore dovrebbe essere inserito
    per mantenere la lista ordinata.
    """
    sinistra: int = 0
    destra: int = len(lista)

    while sinistra < destra:
        centro: int = (sinistra + destra) // 2
        if lista[centro] < valore:
            sinistra = centro + 1
        else:
            destra = centro

    return sinistra


# --- Test ricerca binaria ---
lista_ord: list[float] = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Cerca elementi presenti
assert ricerca_binaria(lista_ord, 7) == 3
assert ricerca_binaria(lista_ord, 1) == 0    # primo elemento
assert ricerca_binaria(lista_ord, 19) == 9   # ultimo elemento
assert ricerca_binaria(lista_ord, 11) == 5

# Cerca elemento assente
assert ricerca_binaria(lista_ord, 4) == -1
assert ricerca_binaria(lista_ord, 20) == -1

# Lista vuota
assert ricerca_binaria([], 5) == -1

# Verifica versione ricorsiva (stessi risultati)
for val in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 20]:
    assert ricerca_binaria(lista_ord, val) == ricerca_binaria_ricorsiva(lista_ord, val)

# Test posizione di inserimento
assert ricerca_inserimento([1, 3, 5, 7], 4) == 2   # tra 3 e 5
assert ricerca_inserimento([1, 3, 5, 7], 0) == 0   # prima di tutto
assert ricerca_inserimento([1, 3, 5, 7], 8) == 4   # dopo tutto
assert ricerca_inserimento([1, 3, 5, 7], 3) == 1   # esiste gia'
print("Esercizio 5 (Ricerca binaria): SUPERATO")


# ============================================================================
print("\n" + "=" * 60)
print("TUTTI GLI ESERCIZI DEL LABORATORIO 04 SUPERATI!")
print("=" * 60)
