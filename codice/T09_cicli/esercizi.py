# F09 — Cicli
# Esercizi per la lezione frontale 9
# Fattoriale, somma pari, numeri primi, tavola pitagorica, FizzBuzz, indovina il numero

# =============================================================================
# Esercizio 1: Fattoriale
# Calcolare n! sia con un ciclo for sia ricorsivamente.
# =============================================================================
print("--- Esercizio 1: Fattoriale ---")


def fattoriale_iterativo(n: int) -> int:
    """Calcola n! con un ciclo for (pattern accumulatore)."""
    if n < 0:
        raise ValueError("Il fattoriale non e' definito per numeri negativi")
    risultato: int = 1
    for i in range(2, n + 1):
        risultato *= i
    return risultato


def fattoriale_ricorsivo(n: int) -> int:
    """Calcola n! ricorsivamente (caso base: 0! = 1)."""
    if n < 0:
        raise ValueError("Il fattoriale non e' definito per numeri negativi")
    if n <= 1:
        return 1
    return n * fattoriale_ricorsivo(n - 1)


# Test
assert fattoriale_iterativo(0) == 1
assert fattoriale_iterativo(1) == 1
assert fattoriale_iterativo(5) == 120
assert fattoriale_iterativo(10) == 3628800

assert fattoriale_ricorsivo(0) == 1
assert fattoriale_ricorsivo(5) == 120
assert fattoriale_ricorsivo(10) == 3628800

# Verifica che le due versioni diano lo stesso risultato
for n in range(15):
    assert fattoriale_iterativo(n) == fattoriale_ricorsivo(n)

print(f"  5!  = {fattoriale_iterativo(5)}")
print(f"  10! = {fattoriale_iterativo(10)}")
print(f"  15! = {fattoriale_iterativo(15)}")
print("  Esercizio 1 superato!\n")


# =============================================================================
# Esercizio 2: Somma dei numeri pari
# Somma di tutti i numeri pari in un intervallo [a, b].
# =============================================================================
print("--- Esercizio 2: Somma dei numeri pari ---")


def somma_pari(a: int, b: int) -> int:
    """Somma tutti i numeri pari nell'intervallo [a, b] inclusi."""
    totale: int = 0
    for n in range(a, b + 1):
        if n % 2 == 0:
            totale += n
    return totale


def somma_pari_formula(a: int, b: int) -> int:
    """Somma dei pari con formula chiusa (per verifica)."""
    # Il primo pari >= a
    primo: int = a if a % 2 == 0 else a + 1
    # L'ultimo pari <= b
    ultimo: int = b if b % 2 == 0 else b - 1
    if primo > ultimo:
        return 0
    # Numero di pari nell'intervallo
    n_pari: int = (ultimo - primo) // 2 + 1
    # Formula della somma aritmetica
    return n_pari * (primo + ultimo) // 2


# Test
assert somma_pari(1, 10) == 2 + 4 + 6 + 8 + 10  # = 30
assert somma_pari(1, 10) == 30
assert somma_pari(1, 1) == 0    # Nessun pari
assert somma_pari(2, 2) == 2    # Un solo pari
assert somma_pari(1, 100) == 2550

# Verifica con formula
for a_test, b_test in [(1, 10), (5, 50), (1, 100), (3, 3), (0, 0)]:
    assert somma_pari(a_test, b_test) == somma_pari_formula(a_test, b_test)

print(f"  Somma pari [1, 10]  = {somma_pari(1, 10)}")
print(f"  Somma pari [1, 100] = {somma_pari(1, 100)}")
print("  Esercizio 2 superato!\n")


# =============================================================================
# Esercizio 3: Verifica numeri primi
# Determinare se un numero e' primo e trovare i primi N numeri primi.
# =============================================================================
print("--- Esercizio 3: Numeri primi ---")


def is_primo(n: int) -> bool:
    """Verifica se n e' un numero primo."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Basta controllare i divisori dispari fino a sqrt(n)
    d: int = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def primi_n_numeri(n: int) -> list[int]:
    """Restituisce i primi n numeri primi."""
    primi: list[int] = []
    candidato: int = 2
    while len(primi) < n:
        if is_primo(candidato):
            primi.append(candidato)
        candidato += 1
    return primi


def primi_fino_a(limite: int) -> list[int]:
    """Restituisce tutti i numeri primi fino a 'limite' incluso."""
    primi: list[int] = []
    for n in range(2, limite + 1):
        if is_primo(n):
            primi.append(n)
    return primi


# Test is_primo
assert is_primo(0) is False
assert is_primo(1) is False
assert is_primo(2) is True
assert is_primo(3) is True
assert is_primo(4) is False
assert is_primo(17) is True
assert is_primo(18) is False
assert is_primo(97) is True
assert is_primo(100) is False

# Test primi_n_numeri
primi_10: list[int] = primi_n_numeri(10)
assert primi_10 == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Test primi_fino_a
assert primi_fino_a(20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert len(primi_fino_a(100)) == 25  # Ci sono 25 primi sotto 100

print(f"  Primi 10 numeri primi: {primi_10}")
print(f"  Primi fino a 50: {primi_fino_a(50)}")
print(f"  Quanti primi < 100: {len(primi_fino_a(100))}")
print("  Esercizio 3 superato!\n")


# =============================================================================
# Esercizio 4: Tavola pitagorica
# Generare la tavola pitagorica NxN come matrice (lista di liste).
# =============================================================================
print("--- Esercizio 4: Tavola pitagorica ---")


def tavola_pitagorica(n: int) -> list[list[int]]:
    """Genera la tavola pitagorica NxN (da 1 a n)."""
    tavola: list[list[int]] = []
    for i in range(1, n + 1):
        riga: list[int] = []
        for j in range(1, n + 1):
            riga.append(i * j)
        tavola.append(riga)
    return tavola


def stampa_tavola(tavola: list[list[int]]) -> None:
    """Stampa la tavola pitagorica in formato tabellare."""
    n: int = len(tavola)
    # Intestazione
    print("    ", end="")
    for j in range(1, n + 1):
        print(f"{j:>4}", end="")
    print()
    print("    " + "-" * (4 * n))
    # Righe
    for i, riga in enumerate(tavola, start=1):
        print(f"  {i:>2}|", end="")
        for val in riga:
            print(f"{val:>4}", end="")
        print()


# Test
tavola_3: list[list[int]] = tavola_pitagorica(3)
assert tavola_3 == [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9],
]

tavola_5: list[list[int]] = tavola_pitagorica(5)
assert tavola_5[0] == [1, 2, 3, 4, 5]
assert tavola_5[4] == [5, 10, 15, 20, 25]
assert tavola_5[2][3] == 12  # 3 * 4

stampa_tavola(tavola_pitagorica(7))
print("  Esercizio 4 superato!\n")


# =============================================================================
# Esercizio 5: FizzBuzz
# Per i numeri da 1 a N:
#   - multiplo di 3 e 5 → "FizzBuzz"
#   - multiplo di 3     → "Fizz"
#   - multiplo di 5     → "Buzz"
#   - altrimenti        → il numero stesso (come stringa)
# =============================================================================
print("--- Esercizio 5: FizzBuzz ---")


def fizzbuzz(n: int) -> list[str]:
    """Genera la sequenza FizzBuzz da 1 a n."""
    risultato: list[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:  # Multiplo di 3 E 5
            risultato.append("FizzBuzz")
        elif i % 3 == 0:
            risultato.append("Fizz")
        elif i % 5 == 0:
            risultato.append("Buzz")
        else:
            risultato.append(str(i))
    return risultato


# Test
fb_15: list[str] = fizzbuzz(15)
assert fb_15[0] == "1"
assert fb_15[2] == "Fizz"       # 3
assert fb_15[4] == "Buzz"       # 5
assert fb_15[5] == "Fizz"       # 6
assert fb_15[9] == "Buzz"       # 10
assert fb_15[14] == "FizzBuzz"  # 15

# Contiamo i vari tipi
fb_100: list[str] = fizzbuzz(100)
n_fizz: int = sum(1 for x in fb_100 if x == "Fizz")
n_buzz: int = sum(1 for x in fb_100 if x == "Buzz")
n_fizzbuzz: int = sum(1 for x in fb_100 if x == "FizzBuzz")
n_numeri: int = sum(1 for x in fb_100 if x not in ("Fizz", "Buzz", "FizzBuzz"))

assert n_fizz + n_buzz + n_fizzbuzz + n_numeri == 100
assert n_fizzbuzz == 6   # 15, 30, 45, 60, 75, 90
assert n_fizz == 27      # Multipli di 3 non di 5: 33 - 6 = 27
assert n_buzz == 14       # Multipli di 5 non di 3: 20 - 6 = 14

print(f"  FizzBuzz(15): {fb_15}")
print(f"  Su 100: Fizz={n_fizz}, Buzz={n_buzz}, FizzBuzz={n_fizzbuzz}, numeri={n_numeri}")
print("  Esercizio 5 superato!\n")


# =============================================================================
# Esercizio 6: Simulazione "Indovina il numero"
# Simula un gioco in cui un algoritmo cerca di indovinare un numero
# usando la ricerca binaria (senza input dell'utente).
# =============================================================================
print("--- Esercizio 6: Indovina il numero (simulazione) ---")


def indovina_numero(
    segreto: int, minimo: int, massimo: int
) -> tuple[int, list[int]]:
    """
    Simula il gioco 'indovina il numero' con ricerca binaria.
    Restituisce (numero di tentativi, lista dei tentativi).
    """
    tentativi: list[int] = []
    basso: int = minimo
    alto: int = massimo

    while basso <= alto:
        tentativo: int = (basso + alto) // 2
        tentativi.append(tentativo)

        if tentativo == segreto:
            break
        elif tentativo < segreto:
            basso = tentativo + 1
        else:
            alto = tentativo - 1

    return len(tentativi), tentativi


# Test: il numero segreto e' 73, intervallo [1, 100]
n_tentativi, lista_tentativi = indovina_numero(73, 1, 100)
assert lista_tentativi[-1] == 73  # L'ultimo tentativo deve essere corretto
assert n_tentativi <= 7           # log2(100) ≈ 7, mai piu' di 7 tentativi

# Test: caso estremo — indovinare 1 nell'intervallo [1, 1000]
n2, t2 = indovina_numero(1, 1, 1000)
assert t2[-1] == 1
assert n2 <= 10  # log2(1000) ≈ 10

# Test: caso medio
n3, t3 = indovina_numero(500, 1, 1000)
assert t3[-1] == 500

# Simulazione con output dettagliato
segreto_test: int = 73
n_tent, tentativi_test = indovina_numero(segreto_test, 1, 100)
print(f"  Numero segreto: {segreto_test}")
print(f"  Intervallo: [1, 100]")
print(f"  Tentativi: {tentativi_test}")
print(f"  Indovinato in {n_tent} tentativi")

# Statistiche: quanti tentativi servono mediamente per [1, 100]?
totale_tentativi: int = 0
max_tentativi: int = 0
for numero in range(1, 101):
    n_t, _ = indovina_numero(numero, 1, 100)
    totale_tentativi += n_t
    if n_t > max_tentativi:
        max_tentativi = n_t

media_tentativi: float = totale_tentativi / 100
assert max_tentativi <= 7
print(f"\n  Statistiche su [1, 100]:")
print(f"    Media tentativi: {media_tentativi:.2f}")
print(f"    Max tentativi:   {max_tentativi}")
print("  Esercizio 6 superato!\n")


print("Tutti gli esercizi F09 completati con successo!")
