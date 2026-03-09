# L01 — Ambiente, variabili, condizionali
# Esercizi per il laboratorio 01
#
# Esercizi pratici su variabili, tipi, casting, operatori e condizionali.
# Ogni esercizio include assert per verificare la correttezza.

# ============================================================================
# ESERCIZIO 1: Conversione di temperature
# ============================================================================
# Scrivi funzioni per convertire tra Celsius, Fahrenheit e Kelvin.

def celsius_to_fahrenheit(celsius: float) -> float:
    """Converte gradi Celsius in Fahrenheit: F = C * 9/5 + 32."""
    fahrenheit: float = celsius * 9.0 / 5.0 + 32.0
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converte gradi Fahrenheit in Celsius: C = (F - 32) * 5/9."""
    celsius: float = (fahrenheit - 32.0) * 5.0 / 9.0
    return celsius


def celsius_to_kelvin(celsius: float) -> float:
    """Converte gradi Celsius in Kelvin: K = C + 273.15."""
    kelvin: float = celsius + 273.15
    return kelvin


def kelvin_to_celsius(kelvin: float) -> float:
    """Converte gradi Kelvin in Celsius: C = K - 273.15."""
    celsius: float = kelvin - 273.15
    return celsius


# --- Test conversioni ---
assert abs(celsius_to_fahrenheit(0.0) - 32.0) < 1e-9, "0°C deve essere 32°F"
assert abs(celsius_to_fahrenheit(100.0) - 212.0) < 1e-9, "100°C deve essere 212°F"
assert abs(fahrenheit_to_celsius(32.0) - 0.0) < 1e-9, "32°F deve essere 0°C"
assert abs(fahrenheit_to_celsius(212.0) - 100.0) < 1e-9, "212°F deve essere 100°C"
assert abs(celsius_to_kelvin(0.0) - 273.15) < 1e-9, "0°C deve essere 273.15K"
assert abs(kelvin_to_celsius(273.15) - 0.0) < 1e-9, "273.15K deve essere 0°C"

# Verifica che le conversioni siano inverse l'una dell'altra
temp_originale: float = 37.5
assert abs(fahrenheit_to_celsius(celsius_to_fahrenheit(temp_originale)) - temp_originale) < 1e-9
assert abs(kelvin_to_celsius(celsius_to_kelvin(temp_originale)) - temp_originale) < 1e-9
print("Esercizio 1 (Conversione temperature): SUPERATO")


# ============================================================================
# ESERCIZIO 2: Calcolo dell'interesse composto
# ============================================================================
# Formula: A = P * (1 + r/n)^(n*t)
# P = capitale iniziale, r = tasso annuo, n = composizioni/anno, t = anni

def interesse_composto(
    capitale: float,
    tasso_annuo: float,
    composizioni_anno: int,
    anni: int
) -> float:
    """
    Calcola il montante con interesse composto.

    Parametri:
        capitale: il capitale iniziale (P)
        tasso_annuo: il tasso di interesse annuo come decimale (es. 0.05 per 5%)
        composizioni_anno: numero di volte che l'interesse viene composto per anno (n)
        anni: durata dell'investimento in anni (t)

    Ritorna:
        Il montante finale (A)
    """
    montante: float = capitale * (1 + tasso_annuo / composizioni_anno) ** (composizioni_anno * anni)
    return round(montante, 2)


def interesse_guadagnato(
    capitale: float,
    tasso_annuo: float,
    composizioni_anno: int,
    anni: int
) -> float:
    """Calcola solo l'interesse guadagnato (montante - capitale)."""
    guadagno: float = interesse_composto(capitale, tasso_annuo, composizioni_anno, anni) - capitale
    return round(guadagno, 2)


# --- Test interesse composto ---
# 1000 EUR al 5% annuo, composto annualmente, per 10 anni
montante_1: float = interesse_composto(1000.0, 0.05, 1, 10)
assert montante_1 == 1628.89, f"Atteso 1628.89, ottenuto {montante_1}"

# 1000 EUR al 5% annuo, composto mensilmente, per 10 anni
montante_2: float = interesse_composto(1000.0, 0.05, 12, 10)
assert montante_2 == 1647.01, f"Atteso 1647.01, ottenuto {montante_2}"

# Interesse guadagnato
guadagno: float = interesse_guadagnato(1000.0, 0.05, 12, 10)
assert guadagno == 647.01, f"Atteso 647.01, ottenuto {guadagno}"

# Con tasso zero il montante deve essere uguale al capitale
assert interesse_composto(5000.0, 0.0, 12, 5) == 5000.0
print("Esercizio 2 (Interesse composto): SUPERATO")


# ============================================================================
# ESERCIZIO 3: Classificazione di un triangolo per lati
# ============================================================================
# Dato un triangolo con lati a, b, c:
# - Equilatero: tutti i lati uguali
# - Isoscele: esattamente due lati uguali
# - Scaleno: tutti i lati diversi
# - Non valido: la somma di due lati qualsiasi deve essere > del terzo

def classifica_triangolo(a: float, b: float, c: float) -> str:
    """
    Classifica un triangolo in base ai suoi lati.

    Ritorna una stringa: 'equilatero', 'isoscele', 'scaleno', oppure
    'non valido' se i lati non formano un triangolo.
    """
    # Verifica che i lati siano positivi
    if a <= 0 or b <= 0 or c <= 0:
        return "non valido"

    # Disuguaglianza triangolare: ogni lato deve essere minore della somma degli altri due
    if a + b <= c or a + c <= b or b + c <= a:
        return "non valido"

    # Classificazione
    if a == b == c:
        return "equilatero"
    elif a == b or b == c or a == c:
        return "isoscele"
    else:
        return "scaleno"


# --- Test classificazione triangolo ---
assert classifica_triangolo(3, 3, 3) == "equilatero"
assert classifica_triangolo(5, 5, 3) == "isoscele"
assert classifica_triangolo(3, 4, 5) == "scaleno"
assert classifica_triangolo(1, 1, 3) == "non valido"    # viola disuguaglianza
assert classifica_triangolo(0, 4, 5) == "non valido"    # lato zero
assert classifica_triangolo(-1, 2, 3) == "non valido"   # lato negativo
assert classifica_triangolo(5, 3, 5) == "isoscele"      # lati non consecutivi uguali
print("Esercizio 3 (Classificazione triangolo): SUPERATO")


# ============================================================================
# ESERCIZIO 4: Calcolatore BMI con categorie
# ============================================================================
# BMI = peso (kg) / altezza (m)^2
# Categorie OMS:
#   BMI < 18.5       -> "sottopeso"
#   18.5 <= BMI < 25  -> "normopeso"
#   25 <= BMI < 30    -> "sovrappeso"
#   BMI >= 30         -> "obesità"

def calcola_bmi(peso_kg: float, altezza_m: float) -> float:
    """Calcola il BMI dato peso in kg e altezza in metri."""
    if altezza_m <= 0 or peso_kg <= 0:
        raise ValueError("Peso e altezza devono essere positivi")
    bmi: float = peso_kg / (altezza_m ** 2)
    return round(bmi, 1)


def categoria_bmi(bmi: float) -> str:
    """Restituisce la categoria OMS corrispondente al BMI."""
    if bmi < 18.5:
        return "sottopeso"
    elif bmi < 25.0:
        return "normopeso"
    elif bmi < 30.0:
        return "sovrappeso"
    else:
        return "obesità"


def report_bmi(peso_kg: float, altezza_m: float) -> dict[str, object]:
    """
    Genera un report completo del BMI.

    Ritorna un dizionario con: peso, altezza, bmi, categoria.
    """
    bmi: float = calcola_bmi(peso_kg, altezza_m)
    cat: str = categoria_bmi(bmi)
    report: dict[str, object] = {
        "peso_kg": peso_kg,
        "altezza_m": altezza_m,
        "bmi": bmi,
        "categoria": cat,
    }
    return report


# --- Test BMI ---
assert calcola_bmi(70, 1.75) == 22.9
assert categoria_bmi(17.0) == "sottopeso"
assert categoria_bmi(22.0) == "normopeso"
assert categoria_bmi(27.5) == "sovrappeso"
assert categoria_bmi(35.0) == "obesità"

# Test ai confini delle categorie
assert categoria_bmi(18.5) == "normopeso"
assert categoria_bmi(25.0) == "sovrappeso"
assert categoria_bmi(30.0) == "obesità"

# Test report completo
report: dict[str, object] = report_bmi(80, 1.80)
assert report["categoria"] == "normopeso"
assert report["bmi"] == 24.7

# Test errore per valori non validi
errore_catturato: bool = False
try:
    calcola_bmi(70, 0)
except ValueError:
    errore_catturato = True
assert errore_catturato, "Dovrebbe sollevare ValueError per altezza zero"
print("Esercizio 4 (BMI): SUPERATO")


# ============================================================================
# ESERCIZIO 5: Calcolatore di tasse semplificato (a scaglioni)
# ============================================================================
# Sistema a scaglioni IRPEF semplificato:
#   Fino a 15.000      -> 23%
#   15.001 - 28.000    -> 25%
#   28.001 - 50.000    -> 35%
#   Oltre 50.000       -> 43%
#
# Ogni scaglione si applica SOLO alla parte di reddito che rientra in quello scaglione.

def calcola_irpef(reddito: float) -> float:
    """
    Calcola l'IRPEF con il sistema a scaglioni progressivi.

    Il calcolo e' progressivo: ogni aliquota si applica solo alla porzione
    di reddito che ricade nello scaglione corrispondente.
    """
    if reddito <= 0:
        return 0.0

    # Definizione degli scaglioni: (limite superiore, aliquota)
    scaglioni: list[tuple[float, float]] = [
        (15_000.0, 0.23),
        (28_000.0, 0.25),
        (50_000.0, 0.35),
        (float('inf'), 0.43),
    ]

    tassa_totale: float = 0.0
    limite_precedente: float = 0.0

    for limite, aliquota in scaglioni:
        if reddito <= limite_precedente:
            break
        # La porzione tassabile in questo scaglione
        porzione: float = min(reddito, limite) - limite_precedente
        tassa_totale += porzione * aliquota
        limite_precedente = limite

    return round(tassa_totale, 2)


def aliquota_effettiva(reddito: float) -> float:
    """Calcola l'aliquota effettiva (tassa / reddito) in percentuale."""
    if reddito <= 0:
        return 0.0
    tassa: float = calcola_irpef(reddito)
    return round(tassa / reddito * 100, 2)


# --- Test IRPEF ---
# Reddito interamente nel primo scaglione
assert calcola_irpef(10_000) == 2_300.0, f"Atteso 2300, ottenuto {calcola_irpef(10_000)}"

# Reddito esattamente al limite del primo scaglione
assert calcola_irpef(15_000) == 3_450.0

# Reddito che copre due scaglioni: 15000*0.23 + 5000*0.25 = 3450 + 1250 = 4700
assert calcola_irpef(20_000) == 4_700.0

# Reddito che copre tre scaglioni: 3450 + 3250 + 2000*0.35 = 3450 + 3250 + 700 = 7400
assert calcola_irpef(30_000) == 7_400.0

# Reddito che copre tutti e quattro gli scaglioni:
# 15000*0.23 + 13000*0.25 + 22000*0.35 + 10000*0.43
# = 3450 + 3250 + 7700 + 4300 = 18700
assert calcola_irpef(60_000) == 18_700.0

# Reddito zero o negativo
assert calcola_irpef(0) == 0.0
assert calcola_irpef(-1000) == 0.0

# Aliquota effettiva
assert aliquota_effettiva(15_000) == 23.0
assert aliquota_effettiva(60_000) == 31.17  # 18700/60000*100
print("Esercizio 5 (IRPEF): SUPERATO")


# ============================================================================
print("\n" + "=" * 60)
print("TUTTI GLI ESERCIZI DEL LABORATORIO 01 SUPERATI!")
print("=" * 60)
