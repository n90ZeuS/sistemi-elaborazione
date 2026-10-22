# L01 — Ambiente, variabili, condizionali
# Esercizi per il laboratorio 01
#
# Esercizi 1-4: soluzioni della traccia (Parte 5 e Sfida di slide e dispensa).
# Esercizi 5-7: esercizi aggiuntivi per chi ha finito.
#
# Nella traccia ogni programma legge i dati con input(); qui i dati sono
# scritti nel codice, cosi' il file si esegue tutto in una volta.
# La riga con input() e' riportata in commento: per provarla, toglietele
# il # e commentate la riga sotto. Cambiate i valori e rilanciate per
# provare casi diversi. Accanto a ogni risultato c'e' il valore atteso.

# ============================================================================
# ESERCIZIO 1 (base): conversione di temperatura — temperatura.py
# ============================================================================
# Convertire una temperatura da Celsius a Fahrenheit: F = C * 9/5 + 32
# Stampare il risultato con una cifra decimale.
# In piu': conversione in Kelvin (K = C + 273.15) e ritorno a Celsius.
print("--- Esercizio 1: Conversione di temperatura ---")

# celsius: float = float(input("Temperatura in Celsius: "))
celsius: float = 25.0

fahrenheit: float = celsius * 9 / 5 + 32
print(f"  {celsius:.1f}°C = {fahrenheit:.1f}°F")   # atteso: 25.0°C = 77.0°F

kelvin: float = celsius + 273.15
print(f"  {celsius:.1f}°C = {kelvin:.2f} K")       # atteso: 25.0°C = 298.15 K

# Riconvertendo all'indietro si deve tornare al valore di partenza
celsius_da_fahrenheit: float = (fahrenheit - 32) * 5 / 9
celsius_da_kelvin: float = kelvin - 273.15
print(f"  Da °F a °C: {celsius_da_fahrenheit:.1f}")   # atteso: 25.0
print(f"  Da K a °C:  {celsius_da_kelvin:.1f}")       # atteso: 25.0
# Altri casi da provare: 0 -> 32.0°F, 100 -> 212.0°F, 37.5 -> 99.5°F
print()


# ============================================================================
# ESERCIZIO 2 (intermedio): calcolo IMC con classificazione — imc.py
# ============================================================================
# IMC = peso (kg) / altezza (m) ** 2
# Fasce OMS:
#   IMC < 18.5         -> "Sottopeso"
#   18.5 <= IMC < 25   -> "Normopeso"
#   25 <= IMC < 30     -> "Sovrappeso"
#   IMC >= 30          -> "Obesita"
# Validazione: peso e altezza positivi, altezza non oltre 2.50 m.
print("--- Esercizio 2: Calcolo IMC ---")

# peso_kg: float = float(input("Peso (kg): "))
# altezza_m: float = float(input("Altezza (m): "))
peso_kg: float = 72.0
altezza_m: float = 1.75

if peso_kg <= 0 or altezza_m <= 0:
    print("  Errore: peso e altezza devono essere positivi")
elif altezza_m > 2.50:
    print("  Errore: l'altezza non puo' superare 2.50 m")
else:
    imc: float = peso_kg / altezza_m ** 2

    classificazione: str
    if imc < 18.5:
        classificazione = "Sottopeso"
    elif imc < 25.0:
        classificazione = "Normopeso"
    elif imc < 30.0:
        classificazione = "Sovrappeso"
    else:
        classificazione = "Obesita"

    print(f"  IMC: {imc:.1f} — {classificazione}")  # atteso: IMC: 23.5 — Normopeso
# Altri casi da provare:
#   80 kg, 1.80 m -> 24.7 Normopeso
#   50 kg, 1.80 m -> 15.4 Sottopeso
#   95 kg, 1.75 m -> 31.0 Obesita
#   70 kg, 0 m    -> errore valori non positivi
#   70 kg, 2.60 m -> errore altezza
print()


# ============================================================================
# ESERCIZIO 3 (avanzato): simulazione bancomat — bancomat.py
# ============================================================================
# Saldo iniziale 1000.00 EUR, costante nel codice.
# Menu: D = deposito, P = prelievo, S = saldo (maiuscole o minuscole).
# Errori da gestire: operazione non riconosciuta, importo negativo o zero,
# prelievo superiore al saldo.
print("--- Esercizio 3: Simulazione bancomat ---")

saldo: float = 1000.00

print("  === BANCOMAT ===")
print(f"  Saldo attuale: {saldo:,.2f} EUR")

# operazione: str = input("Operazione (D=Deposito, P=Prelievo, S=Saldo): ").upper()
operazione: str = "p".upper()

if operazione == "S":
    print(f"  Saldo disponibile: {saldo:,.2f} EUR")
elif operazione == "D" or operazione == "P":
    # importo: float = float(input("Importo: "))
    importo: float = 250.0

    if importo <= 0:
        print("  Errore: l'importo deve essere positivo")
    elif operazione == "D":
        saldo = saldo + importo
        print(f"  Deposito di {importo:,.2f} EUR effettuato.")
        print(f"  Nuovo saldo: {saldo:,.2f} EUR")
    elif importo > saldo:
        print(f"  Errore: saldo insufficiente ({saldo:,.2f} EUR disponibili)")
    else:
        saldo = saldo - importo
        print(f"  Prelievo di {importo:,.2f} EUR effettuato.")
        print(f"  Nuovo saldo: {saldo:,.2f} EUR")
else:
    print(f"  Errore: operazione '{operazione}' non riconosciuta")
# atteso: Prelievo di 250.00 EUR effettuato. Nuovo saldo: 750.00 EUR
# Altri casi da provare:
#   "d", 500   -> Nuovo saldo: 1,500.00 EUR
#   "P", 2000  -> saldo insufficiente
#   "P", -10   -> importo non positivo
#   "X"        -> operazione non riconosciuta
print()


# ============================================================================
# ESERCIZIO 4 (sfida): convertitore e classificatore — sfida_temperatura.py
# ============================================================================
# Convertire Celsius in Fahrenheit e classificare la percezione:
#   C <= -10        -> Gelido
#   -10 < C <= 5    -> Freddo
#   5 < C <= 18     -> Mite
#   18 < C <= 30    -> Caldo
#   C > 30          -> Torrido
# Sotto lo zero assoluto (-273.15) stampare un errore e non proseguire.
print("--- Esercizio 4: Sfida temperatura ---")

ZERO_ASSOLUTO: float = -273.15

# temperatura_c: float = float(input("Temperatura in Celsius: "))
temperatura_c: float = 22.0

if temperatura_c < ZERO_ASSOLUTO:
    print(f"  Errore: {temperatura_c}°C e' sotto lo zero assoluto ({ZERO_ASSOLUTO}°C)")
else:
    temperatura_f: float = temperatura_c * 9 / 5 + 32

    percezione: str
    if temperatura_c <= -10:
        percezione = "Gelido"
    elif temperatura_c <= 5:
        percezione = "Freddo"
    elif temperatura_c <= 18:
        percezione = "Mite"
    elif temperatura_c <= 30:
        percezione = "Caldo"
    else:
        percezione = "Torrido"

    print("  === REPORT TEMPERATURA ===")
    print(f"  Celsius:       {temperatura_c:.1f}°C")   # atteso: 22.0°C
    print(f"  Fahrenheit:    {temperatura_f:.1f}°F")   # atteso: 71.6°F
    print(f"  Percezione:    {percezione}")            # atteso: Caldo
# Altri casi da provare:
#   -15 -> Gelido   0 -> Freddo   18 -> Mite (18 e' incluso in Mite)
#   35  -> Torrido  -300 -> errore zero assoluto
print()


# ============================================================================
# ESERCIZI AGGIUNTIVI
# ============================================================================

# ============================================================================
# ESERCIZIO 5: calcolo dell'interesse composto
# ============================================================================
# Formula: A = P * (1 + r/n) ** (n*t)
# P = capitale iniziale, r = tasso annuo, n = composizioni/anno, t = anni
print("--- Esercizio 5: Interesse composto ---")

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
# ESERCIZIO 6: classificazione di un triangolo per lati
# ============================================================================
# Dato un triangolo con lati a, b, c:
# - Non valido: un lato non positivo, oppure un lato >= somma degli altri due
# - Equilatero: tutti i lati uguali
# - Isoscele: esattamente due lati uguali
# - Scaleno: tutti i lati diversi
print("--- Esercizio 6: Classificazione triangolo ---")

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
# ESERCIZIO 7: calcolatore di tasse semplificato (a scaglioni)
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
print("--- Esercizio 7: IRPEF a scaglioni ---")

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
