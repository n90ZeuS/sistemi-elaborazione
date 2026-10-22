# L01 — Ambiente, variabili, condizionali
# Esercizi per il laboratorio 01
#
# Esercizi pratici su variabili, tipi, operatori e condizionali.
# Ogni esercizio parte da dati scritti nel codice: cambiate i valori
# e rilanciate il programma per provare casi diversi.
# Accanto a ogni risultato trovate, in commento, il valore atteso.

# ============================================================================
# ESERCIZIO 1: Conversione di temperature
# ============================================================================
# Convertire una temperatura tra Celsius, Fahrenheit e Kelvin.
#   F = C * 9/5 + 32
#   C = (F - 32) * 5/9
#   K = C + 273.15
print("--- Esercizio 1: Conversione temperature ---")

celsius: float = 37.5

fahrenheit: float = celsius * 9 / 5 + 32
kelvin: float = celsius + 273.15

# Riconvertendo all'indietro si deve tornare al valore di partenza
celsius_da_fahrenheit: float = (fahrenheit - 32) * 5 / 9
celsius_da_kelvin: float = kelvin - 273.15

print(f"  {celsius:.2f} °C = {fahrenheit:.2f} °F")   # atteso: 99.50 °F
print(f"  {celsius:.2f} °C = {kelvin:.2f} K")        # atteso: 310.65 K
print(f"  Da °F a °C: {celsius_da_fahrenheit:.2f}")   # atteso: 37.50
print(f"  Da K a °C:  {celsius_da_kelvin:.2f}")       # atteso: 37.50
print()


# ============================================================================
# ESERCIZIO 2: Calcolo dell'interesse composto
# ============================================================================
# Formula: A = P * (1 + r/n) ** (n*t)
# P = capitale iniziale, r = tasso annuo, n = composizioni/anno, t = anni
print("--- Esercizio 2: Interesse composto ---")

capitale: float = 1000.0
tasso_annuo: float = 0.05        # 5% scritto come decimale
composizioni_anno: int = 12      # composizione mensile
anni: int = 10

montante: float = capitale * (1 + tasso_annuo / composizioni_anno) ** (composizioni_anno * anni)
interesse: float = montante - capitale

print(f"  Capitale iniziale: {capitale:,.2f} EUR")
print(f"  Montante finale:   {montante:,.2f} EUR")   # atteso: 1,647.01 EUR
print(f"  Interesse:         {interesse:,.2f} EUR")  # atteso: 647.01 EUR
# Provate composizioni_anno = 1: il montante atteso diventa 1,628.89 EUR
print()


# ============================================================================
# ESERCIZIO 3: Classificazione di un triangolo per lati
# ============================================================================
# Dato un triangolo con lati a, b, c:
# - Non valido: un lato non positivo, oppure un lato >= somma degli altri due
# - Equilatero: tutti i lati uguali
# - Isoscele: esattamente due lati uguali
# - Scaleno: tutti i lati diversi
print("--- Esercizio 3: Classificazione triangolo ---")

a: float = 5.0
b: float = 3.0
c: float = 5.0

tipo: str
if a <= 0 or b <= 0 or c <= 0:
    tipo = "non valido"
elif a + b <= c or a + c <= b or b + c <= a:
    # Disuguaglianza triangolare violata
    tipo = "non valido"
elif a == b and b == c:
    tipo = "equilatero"
elif a == b or b == c or a == c:
    tipo = "isoscele"
else:
    tipo = "scaleno"

print(f"  Lati {a}, {b}, {c}: {tipo}")  # atteso: isoscele
# Altri casi da provare:
#   3, 3, 3  -> equilatero
#   3, 4, 5  -> scaleno
#   1, 1, 3  -> non valido (disuguaglianza triangolare)
#   0, 4, 5  -> non valido (lato zero)
print()


# ============================================================================
# ESERCIZIO 4: Calcolatore BMI con categorie
# ============================================================================
# BMI = peso (kg) / altezza (m) ** 2
# Categorie OMS:
#   BMI < 18.5        -> "sottopeso"
#   18.5 <= BMI < 25  -> "normopeso"
#   25 <= BMI < 30    -> "sovrappeso"
#   BMI >= 30         -> "obesità"
print("--- Esercizio 4: BMI ---")

peso_kg: float = 80.0
altezza_m: float = 1.80

if peso_kg <= 0 or altezza_m <= 0:
    print("  Errore: peso e altezza devono essere positivi")
else:
    bmi: float = peso_kg / altezza_m ** 2

    categoria: str
    if bmi < 18.5:
        categoria = "sottopeso"
    elif bmi < 25.0:
        categoria = "normopeso"
    elif bmi < 30.0:
        categoria = "sovrappeso"
    else:
        categoria = "obesità"

    print(f"  Peso {peso_kg} kg, altezza {altezza_m} m")
    print(f"  BMI: {bmi:.1f} — {categoria}")  # atteso: 24.7 — normopeso
# Altri casi da provare:
#   70 kg, 1.75 m -> 22.9 normopeso
#   50 kg, 1.80 m -> 15.4 sottopeso
#   70 kg, 0 m    -> messaggio di errore
print()


# ============================================================================
# ESERCIZIO 5: Calcolatore di tasse semplificato (a scaglioni)
# ============================================================================
# Sistema a scaglioni IRPEF semplificato:
#   Fino a 15.000      -> 23%
#   15.001 - 28.000    -> 25%
#   28.001 - 50.000    -> 35%
#   Oltre 50.000       -> 43%
#
# Ogni aliquota si applica SOLO alla parte di reddito che rientra nel suo
# scaglione. Le tasse sugli scaglioni pieni si calcolano una volta sola:
#   primo scaglione pieno:   15000 * 0.23 = 3450
#   secondo scaglione pieno: 13000 * 0.25 = 3250
#   terzo scaglione pieno:   22000 * 0.35 = 7700
print("--- Esercizio 5: IRPEF a scaglioni ---")

reddito: float = 60_000.0

tassa: float
if reddito <= 0:
    tassa = 0.0
elif reddito <= 15_000:
    tassa = reddito * 0.23
elif reddito <= 28_000:
    tassa = 3450 + (reddito - 15_000) * 0.25
elif reddito <= 50_000:
    tassa = 3450 + 3250 + (reddito - 28_000) * 0.35
else:
    tassa = 3450 + 3250 + 7700 + (reddito - 50_000) * 0.43

print(f"  Reddito: {reddito:,.2f} EUR")
print(f"  IRPEF:   {tassa:,.2f} EUR")  # atteso: 18,700.00 EUR

if reddito > 0:
    aliquota_effettiva: float = tassa / reddito * 100
    print(f"  Aliquota effettiva: {aliquota_effettiva:.2f}%")  # atteso: 31.17%
# Altri casi da provare:
#   10000 -> 2,300.00   15000 -> 3,450.00 (23.00%)
#   20000 -> 4,700.00   30000 -> 7,400.00
#   0     -> 0.00 (nessuna aliquota effettiva)
print()


# ============================================================================
print("=" * 60)
print("Fine degli esercizi del laboratorio 01")
print("=" * 60)
