# T08 — Operatori, I/O e condizionali
# Esercizi per la lezione frontale 8
# Calcolatrice, classificatore voti, anno bisestile, discriminante
#
# Ogni esercizio parte da dati scritti nel codice: cambiate i valori
# e rilanciate il programma per provare casi diversi.
# Accanto a ogni risultato trovate, in commento, il valore atteso.

# =============================================================================
# Esercizio 1: Calcolatrice
# Dati due numeri e un'operazione, stampare il risultato.
# Gestire la divisione per zero e le operazioni non riconosciute.
# =============================================================================
print("--- Esercizio 1: Calcolatrice ---")

a: float = 10
b: float = 3
operazione: str = "//"

if operazione == "+":
    print(f"  {a} + {b} = {a + b}")
elif operazione == "-":
    print(f"  {a} - {b} = {a - b}")
elif operazione == "*":
    print(f"  {a} * {b} = {a * b}")
elif operazione == "**":
    print(f"  {a} ** {b} = {a ** b}")
elif operazione == "/" or operazione == "//" or operazione == "%":
    # Le tre divisioni hanno lo stesso problema: b non puo' essere zero
    if b == 0:
        print("  Errore: divisione per zero")
    elif operazione == "/":
        print(f"  {a} / {b} = {a / b:.4f}")
    elif operazione == "//":
        print(f"  {a} // {b} = {a // b}")
    else:
        print(f"  {a} % {b} = {a % b}")
else:
    print(f"  Errore: operazione '{operazione}' non riconosciuta")
# atteso: 10 // 3 = 3
# Altri casi da provare:
#   "/"  -> 3.3333     "%" -> 1     "**" -> 1000
#   b = 0 con "/"      -> Errore: divisione per zero
#   "§"                -> Errore: operazione '§' non riconosciuta
print()


# =============================================================================
# Esercizio 2: Classificatore di voti
# Classificare un voto in trentesimi (sistema universitario italiano).
# =============================================================================
print("--- Esercizio 2: Classificatore di voti ---")

voto: int = 24

giudizio: str
if voto < 0 or voto > 30:
    giudizio = "Non valido"
elif voto < 18:
    giudizio = "Insufficiente"
elif voto < 22:
    giudizio = "Sufficiente"
elif voto < 26:
    giudizio = "Discreto"
elif voto < 29:
    giudizio = "Buono"
else:
    giudizio = "Ottimo"

promosso: bool = voto >= 18 and voto <= 30

print(f"  Voto {voto}: {giudizio}")   # atteso: Discreto
print(f"  Promosso? {promosso}")      # atteso: True
# Altri casi da provare:
#   30 -> Ottimo   28 -> Buono   19 -> Sufficiente
#   10 -> Insufficiente, promosso False
#   31 -> Non valido, promosso False
print()


# =============================================================================
# Esercizio 3: Verifica anno bisestile
# Un anno e' bisestile se:
#   - divisibile per 4 E
#   - (NON divisibile per 100 OPPURE divisibile per 400)
# =============================================================================
print("--- Esercizio 3: Anno bisestile ---")

anno: int = 1900

bisestile: bool = (anno % 4 == 0) and (anno % 100 != 0 or anno % 400 == 0)

if bisestile:
    print(f"  {anno} e' bisestile: febbraio ha 29 giorni")
else:
    print(f"  {anno} non e' bisestile: febbraio ha 28 giorni")
# atteso: 1900 non e' bisestile (divisibile per 100 ma non per 400)
# Altri casi da provare:
#   2000 -> bisestile (divisibile per 400)
#   2024 -> bisestile (divisibile per 4, non per 100)
#   2023 -> non bisestile
#   2100 -> non bisestile
print()


# =============================================================================
# Esercizio 4: Discriminante dell'equazione quadratica
# Data ax^2 + bx + c = 0, calcolare il discriminante e le soluzioni.
# Delta = b^2 - 4ac
# La radice quadrata si calcola con ** 0.5
# =============================================================================
print("--- Esercizio 4: Discriminante equazione quadratica ---")

coeff_a: float = 1
coeff_b: float = -5
coeff_c: float = 6

print(f"  Equazione: {coeff_a}x^2 + {coeff_b}x + {coeff_c} = 0")

if coeff_a == 0:
    # Non e' un'equazione di secondo grado
    if coeff_b == 0:
        print("  Equazione degenere: nessuna incognita")
    else:
        x: float = -coeff_c / coeff_b
        print(f"  Equazione lineare: x = {x}")
else:
    delta: float = coeff_b ** 2 - 4 * coeff_a * coeff_c
    print(f"  Delta = {delta}")

    if delta > 0:
        x1: float = (-coeff_b + delta ** 0.5) / (2 * coeff_a)
        x2: float = (-coeff_b - delta ** 0.5) / (2 * coeff_a)
        print(f"  Due soluzioni reali distinte: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x1 = -coeff_b / (2 * coeff_a)
        print(f"  Due soluzioni reali coincidenti: x = {x1}")
    else:
        parte_reale: float = -coeff_b / (2 * coeff_a)
        parte_immaginaria: float = (-delta) ** 0.5 / (2 * coeff_a)
        print(f"  Soluzioni complesse coniugate: {parte_reale} ± {parte_immaginaria}i")
# atteso: Delta = 1, x1 = 3.0, x2 = 2.0
# Altri casi da provare:
#   1, -4, 4  -> Delta = 0, x = 2.0
#   1, 0, 1   -> Delta = -4, soluzioni -0.0 ± 1.0i (-0.0 e 0.0 sono lo stesso numero)
#   2, -7, 3  -> Delta = 25, x1 = 3.0, x2 = 0.5
#   0, 2, -6  -> lineare, x = 3.0
print()


print("Fine degli esercizi T08")
