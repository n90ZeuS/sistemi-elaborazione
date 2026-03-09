# F08 — Operatori, I/O e condizionali
# Esempi per la lezione frontale 8
# Operatori aritmetici, confronto, logici, condizionali, operatore ternario

# =============================================================================
# 1. Operatori aritmetici
# =============================================================================
print("--- 1. Operatori aritmetici ---")

a: int = 17
b: int = 5

somma: int = a + b
differenza: int = a - b
prodotto: int = a * b
divisione: float = a / b          # Divisione reale (sempre float)
divisione_intera: int = a // b    # Divisione intera (troncamento verso -inf)
resto: int = a % b                # Modulo (resto della divisione)
potenza: int = a ** b             # Elevamento a potenza

assert somma == 22
assert differenza == 12
assert prodotto == 85
assert divisione == 3.4
assert divisione_intera == 3
assert resto == 2
assert potenza == 1419857

print(f"  a = {a}, b = {b}")
print(f"  a + b  = {somma}")
print(f"  a - b  = {differenza}")
print(f"  a * b  = {prodotto}")
print(f"  a / b  = {divisione}   (divisione reale, sempre float)")
print(f"  a // b = {divisione_intera}     (divisione intera)")
print(f"  a % b  = {resto}     (modulo)")
print(f"  a ** b = {potenza} (potenza)")

# Attenzione alla divisione intera con numeri negativi
assert -17 // 5 == -4   # Tronca verso -infinito, NON verso zero!
assert -17 % 5 == 3     # Il resto segue la regola: a == (a // b) * b + (a % b)
print(f"\n  -17 // 5 = {-17 // 5}  (tronca verso -inf)")
print(f"  -17 % 5  = {-17 % 5}   (coerente: -17 == -4 * 5 + 3)")

# Operatori di assegnamento composto
contatore: int = 0
contatore += 10   # equivale a contatore = contatore + 10
assert contatore == 10
contatore -= 3
assert contatore == 7
contatore *= 2
assert contatore == 14
contatore //= 3
assert contatore == 4
contatore **= 2
assert contatore == 16
print(f"\n  Operatori composti: contatore finale = {contatore}")


# =============================================================================
# 2. Operatori di confronto
# =============================================================================
print("\n--- 2. Operatori di confronto ---")

x: int = 10
y: int = 20

assert (x == y) is False
assert (x != y) is True
assert (x < y) is True
assert (x > y) is False
assert (x <= y) is True
assert (x >= y) is False

print(f"  x = {x}, y = {y}")
print(f"  x == y → {x == y}")
print(f"  x != y → {x != y}")
print(f"  x <  y → {x < y}")
print(f"  x >  y → {x > y}")

# Confronto a catena (peculiarita' di Python)
voto: int = 25
assert (18 <= voto <= 30) is True
print(f"\n  voto = {voto}: 18 <= voto <= 30 → {18 <= voto <= 30}")

# == confronta il valore, 'is' confronta l'identita' (oggetto in memoria)
lista1: list[int] = [1, 2, 3]
lista2: list[int] = [1, 2, 3]
assert lista1 == lista2       # Stesso valore
assert lista1 is not lista2   # Oggetti diversi in memoria
print(f"\n  [1,2,3] == [1,2,3] → {lista1 == lista2}")
print(f"  [1,2,3] is [1,2,3] → {lista1 is lista2}")


# =============================================================================
# 3. Operatori logici e short-circuit
# =============================================================================
print("\n--- 3. Operatori logici e short-circuit ---")

p: bool = True
q: bool = False

assert (p and q) is False
assert (p or q) is True
assert (not p) is False

print(f"  p = {p}, q = {q}")
print(f"  p and q → {p and q}")
print(f"  p or  q → {p or q}")
print(f"  not p   → {not p}")

# Tavola di verita' completa
print("\n  Tavola di verita':")
print(f"  {'A':<6}{'B':<6}{'A and B':<10}{'A or B':<10}{'not A':<8}")
for a_val in [True, False]:
    for b_val in [True, False]:
        print(f"  {str(a_val):<6}{str(b_val):<6}{str(a_val and b_val):<10}"
              f"{str(a_val or b_val):<10}{str(not a_val):<8}")

# Short-circuit evaluation
# 'and' restituisce il primo valore falsy, oppure l'ultimo se tutti truthy
# 'or'  restituisce il primo valore truthy, oppure l'ultimo se tutti falsy
assert (0 and 5) == 0          # 0 e' falsy, si ferma subito
assert (3 and 5) == 5          # 3 e' truthy, valuta e restituisce 5
assert (0 or 5) == 5           # 0 e' falsy, prosegue e restituisce 5
assert ("" or "default") == "default"  # Utile per valori di default!

print(f"\n  Short-circuit:")
print(f"  0 and 5        → {0 and 5}")
print(f"  3 and 5        → {3 and 5}")
print(f"  0 or 5         → {0 or 5}")
print(f"  '' or 'default' → {'' or 'default'}")


# =============================================================================
# 4. Condizionali: if / elif / else
# =============================================================================
print("\n--- 4. Condizionali ---")


def classifica_voto(voto: int) -> str:
    """Classifica un voto universitario in una categoria."""
    if voto < 18:
        giudizio: str = "Insufficiente"
    elif voto < 22:
        giudizio = "Sufficiente"
    elif voto < 26:
        giudizio = "Discreto"
    elif voto < 29:
        giudizio = "Buono"
    elif voto == 30:
        giudizio = "Ottimo"
    else:
        giudizio = "Molto buono"
    return giudizio


assert classifica_voto(15) == "Insufficiente"
assert classifica_voto(18) == "Sufficiente"
assert classifica_voto(24) == "Discreto"
assert classifica_voto(27) == "Buono"
assert classifica_voto(29) == "Molto buono"
assert classifica_voto(30) == "Ottimo"

voti_test: list[int] = [15, 18, 22, 26, 29, 30]
for v in voti_test:
    print(f"  Voto {v:>2} → {classifica_voto(v)}")


# =============================================================================
# 5. Operatore ternario (espressione condizionale)
# =============================================================================
print("\n--- 5. Operatore ternario ---")

# Sintassi: valore_se_vero if condizione else valore_se_falso
eta_studente: int = 20
stato: str = "maggiorenne" if eta_studente >= 18 else "minorenne"
assert stato == "maggiorenne"
print(f"  Eta' {eta_studente}: {stato}")

# Utile per assegnamenti concisi
temperatura: float = -5.0
stato_acqua: str = "ghiaccio" if temperatura <= 0 else "liquida"
assert stato_acqua == "ghiaccio"
print(f"  Temperatura {temperatura}°C: acqua {stato_acqua}")

# Equivalente con if/else classico (piu' lungo ma piu' leggibile per casi complessi)
numero: int = 42
parita: str = "pari" if numero % 2 == 0 else "dispari"
assert parita == "pari"
print(f"  {numero} e' {parita}")

# Ternario annidato (sconsigliato: poco leggibile!)
x_val: int = 0
segno: str = "positivo" if x_val > 0 else ("negativo" if x_val < 0 else "zero")
assert segno == "zero"
print(f"  {x_val} e' {segno}")


# =============================================================================
# 6. Esempio integrato: simulazione di input con variabili
# =============================================================================
print("\n--- 6. Esempio integrato: parsificazione dati ---")

# Simuliamo l'input di un utente (senza usare input())
input_simulato: str = "  42.5  "

# Pulizia e conversione
valore_pulito: str = input_simulato.strip()
valore_numerico: float = float(valore_pulito)
valore_intero: int = int(valore_numerico)

assert valore_pulito == "42.5"
assert valore_numerico == 42.5
assert valore_intero == 42

print(f"  Input grezzo:    '{input_simulato}'")
print(f"  Dopo strip():    '{valore_pulito}'")
print(f"  Come float:      {valore_numerico}")
print(f"  Come int (troncato): {valore_intero}")


print("\nTutti gli assert passati — esempi F08 completati con successo!")
