# T09 — Cicli
# Esercizi per la lezione frontale 9
# Fattoriale, somma pari, numeri primi, tavola pitagorica, FizzBuzz, indovina il numero
#
# Ogni esercizio parte da dati scritti nel codice: cambiate i valori
# e rilanciate il programma per provare casi diversi.
# Accanto a ogni risultato trovate, in commento, il valore atteso.

# =============================================================================
# Esercizio 1: Fattoriale
# Calcolare n! = 1 * 2 * ... * n sia con for sia con while (pattern accumulatore).
# Per definizione 0! = 1.
# =============================================================================
print("--- Esercizio 1: Fattoriale ---")

n: int = 10

if n < 0:
    print("  Errore: il fattoriale non e' definito per numeri negativi")
else:
    # Versione con for
    fattoriale_for: int = 1
    for i in range(2, n + 1):
        fattoriale_for *= i

    # Versione con while: stesso risultato, contatore gestito a mano
    fattoriale_while: int = 1
    k: int = 2
    while k <= n:
        fattoriale_while *= k
        k += 1

    print(f"  {n}! con for   = {fattoriale_for}")    # atteso: 3628800
    print(f"  {n}! con while = {fattoriale_while}")  # atteso: 3628800
# Altri casi da provare: 0 -> 1, 5 -> 120, 15 -> 1307674368000
print()


# =============================================================================
# Esercizio 2: Somma dei numeri pari
# Somma di tutti i numeri pari nell'intervallo [inizio, fine].
# =============================================================================
print("--- Esercizio 2: Somma dei numeri pari ---")

inizio: int = 1
fine: int = 100

# Versione 1: scorro tutti i numeri e tengo solo i pari (pattern filtro)
somma: int = 0
for numero in range(inizio, fine + 1):
    if numero % 2 == 0:
        somma += numero

# Versione 2: parto dal primo pari e salto di 2 in 2
primo_pari: int = inizio
if primo_pari % 2 != 0:
    primo_pari += 1
somma_passo: int = 0
for numero in range(primo_pari, fine + 1, 2):
    somma_passo += numero

print(f"  Somma pari in [{inizio}, {fine}]: {somma}")     # atteso: 2550
print(f"  Con range a passo 2:        {somma_passo}")      # atteso: 2550
# Altri casi da provare: [1, 10] -> 30, [1, 1] -> 0, [2, 2] -> 2
print()


# =============================================================================
# Esercizio 3: Numeri primi
# 3a) Stabilire se un numero e' primo (pattern ricerca: trovato + break).
# 3b) Trovare tutti i primi fino a un limite (cicli annidati).
# =============================================================================
print("--- Esercizio 3: Numeri primi ---")

# 3a) Un numero e' primo se e' >= 2 e non ha divisori tra 2 e la sua radice
candidato: int = 97

primo: bool = candidato >= 2
d: int = 2
while d * d <= candidato:
    if candidato % d == 0:
        primo = False
        break               # trovato un divisore: inutile continuare
    d += 1

print(f"  {candidato} e' primo? {primo}")  # atteso: True
# Altri casi da provare: 0, 1 -> False   2, 17 -> True   18, 100 -> False

# 3b) Stesso controllo, ripetuto per ogni numero fino al limite
limite: int = 50
primi: list[int] = []
for numero in range(2, limite + 1):
    e_primo: bool = True
    divisore: int = 2
    while divisore * divisore <= numero:
        if numero % divisore == 0:
            e_primo = False
            break
        divisore += 1
    if e_primo:
        primi.append(numero)

print(f"  Primi fino a {limite}: {primi}")
# atteso: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print(f"  Quanti sono: {len(primi)}")  # atteso: 15 (con limite 100: 25)
print()


# =============================================================================
# Esercizio 4: Tavola pitagorica
# Stampare la tavola pitagorica N x N con intestazione (cicli annidati).
# =============================================================================
print("--- Esercizio 4: Tavola pitagorica ---")

lato: int = 7

# Intestazione
print("    ", end="")
for colonna in range(1, lato + 1):
    print(f"{colonna:>4}", end="")
print()
print("    " + "-" * (4 * lato))

# Righe
for riga in range(1, lato + 1):
    print(f"  {riga:>2}|", end="")
    for colonna in range(1, lato + 1):
        print(f"{riga * colonna:>4}", end="")
    print()
# atteso: l'ultima riga termina con 49 (7 * 7)
print()


# =============================================================================
# Esercizio 5: FizzBuzz
# Per i numeri da 1 a N:
#   - multiplo di 3 e 5 → "FizzBuzz"
#   - multiplo di 3     → "Fizz"
#   - multiplo di 5     → "Buzz"
#   - altrimenti        → il numero stesso
# Contare anche quante volte compare ciascuna parola (pattern contatore).
# =============================================================================
print("--- Esercizio 5: FizzBuzz ---")

limite_fb: int = 15
n_fizz: int = 0
n_buzz: int = 0
n_fizzbuzz: int = 0

for i in range(1, limite_fb + 1):
    if i % 15 == 0:  # multiplo di 3 E di 5: va controllato per primo
        print("FizzBuzz", end=" ")
        n_fizzbuzz += 1
    elif i % 3 == 0:
        print("Fizz", end=" ")
        n_fizz += 1
    elif i % 5 == 0:
        print("Buzz", end=" ")
        n_buzz += 1
    else:
        print(i, end=" ")
print()

print(f"  Fizz={n_fizz}, Buzz={n_buzz}, FizzBuzz={n_fizzbuzz}")
# atteso: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
#         Fizz=4, Buzz=2, FizzBuzz=1
# Con limite_fb = 100: Fizz=27, Buzz=14, FizzBuzz=6
print()


# =============================================================================
# Esercizio 6: Simulazione "Indovina il numero"
# Il programma indovina un numero segreto con la ricerca binaria:
# prova sempre il valore a meta' dell'intervallo e scarta la meta' sbagliata.
# =============================================================================
print("--- Esercizio 6: Indovina il numero (simulazione) ---")

segreto: int = 73
basso: int = 1
alto: int = 100

tentativi: list[int] = []
while basso <= alto:
    tentativo: int = (basso + alto) // 2
    tentativi.append(tentativo)

    if tentativo == segreto:
        break
    elif tentativo < segreto:
        basso = tentativo + 1
    else:
        alto = tentativo - 1

print(f"  Numero segreto: {segreto}, intervallo [1, 100]")
print(f"  Tentativi: {tentativi}")             # atteso: [50, 75, 62, 68, 71, 73]
print(f"  Indovinato in {len(tentativi)} tentativi")  # atteso: 6
# Con [1, 100] non servono mai piu' di 7 tentativi (2^7 = 128 > 100).
# Provate segreto = 1 o segreto = 100 e alto = 1000.
print()


print("Fine degli esercizi T09")
