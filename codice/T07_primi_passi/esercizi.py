# F07 — Primi passi in Python
# Esercizi per la lezione frontale 7
# Conversioni, calcoli base, formattazione

# =============================================================================
# Esercizio 1: Conversione di temperatura
# Convertire gradi Celsius in Fahrenheit e viceversa.
# Formula: F = C * 9/5 + 32
# =============================================================================
print("--- Esercizio 1: Conversione di temperatura ---")


def celsius_to_fahrenheit(celsius: float) -> float:
    """Converte gradi Celsius in Fahrenheit."""
    fahrenheit: float = celsius * 9 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converte gradi Fahrenheit in Celsius."""
    celsius: float = (fahrenheit - 32) * 5 / 9
    return celsius


# Test di verifica
assert celsius_to_fahrenheit(0.0) == 32.0, "0°C deve essere 32°F"
assert celsius_to_fahrenheit(100.0) == 212.0, "100°C deve essere 212°F"
assert celsius_to_fahrenheit(-40.0) == -40.0, "-40°C deve essere -40°F"

assert fahrenheit_to_celsius(32.0) == 0.0
assert fahrenheit_to_celsius(212.0) == 100.0
assert fahrenheit_to_celsius(-40.0) == -40.0

# Andata e ritorno: la conversione deve essere reversibile
temp_originale: float = 36.6
temp_convertita: float = fahrenheit_to_celsius(celsius_to_fahrenheit(temp_originale))
assert abs(temp_convertita - temp_originale) < 1e-10, "La conversione deve essere reversibile"

print(f"  0°C = {celsius_to_fahrenheit(0.0):.1f}°F")
print(f"  100°C = {celsius_to_fahrenheit(100.0):.1f}°F")
print(f"  36.6°C = {celsius_to_fahrenheit(36.6):.1f}°F")
print(f"  98.6°F = {fahrenheit_to_celsius(98.6):.1f}°C")
print("  Esercizio 1 superato!\n")


# =============================================================================
# Esercizio 2: Calcolo dell'area di figure geometriche
# Calcolare area e perimetro di rettangolo, cerchio e triangolo.
# =============================================================================
print("--- Esercizio 2: Area di figure geometriche ---")

import math


def area_rettangolo(base: float, altezza: float) -> float:
    """Calcola l'area di un rettangolo."""
    area: float = base * altezza
    return area


def perimetro_rettangolo(base: float, altezza: float) -> float:
    """Calcola il perimetro di un rettangolo."""
    perimetro: float = 2 * (base + altezza)
    return perimetro


def area_cerchio(raggio: float) -> float:
    """Calcola l'area di un cerchio."""
    area: float = math.pi * raggio ** 2
    return area


def circonferenza_cerchio(raggio: float) -> float:
    """Calcola la circonferenza di un cerchio."""
    circ: float = 2 * math.pi * raggio
    return circ


def area_triangolo(base: float, altezza: float) -> float:
    """Calcola l'area di un triangolo."""
    area: float = base * altezza / 2
    return area


# Test rettangolo
assert area_rettangolo(5.0, 3.0) == 15.0
assert perimetro_rettangolo(5.0, 3.0) == 16.0

# Test cerchio (con tolleranza per confronti con float)
assert abs(area_cerchio(1.0) - math.pi) < 1e-10
assert abs(area_cerchio(10.0) - 314.159265) < 1e-3
assert abs(circonferenza_cerchio(1.0) - 2 * math.pi) < 1e-10

# Test triangolo
assert area_triangolo(6.0, 4.0) == 12.0
assert area_triangolo(10.0, 5.0) == 25.0

# Stampa formattata dei risultati
base_r: float = 8.5
alt_r: float = 4.2
print(f"  Rettangolo {base_r} x {alt_r}:")
print(f"    Area = {area_rettangolo(base_r, alt_r):.2f}")
print(f"    Perimetro = {perimetro_rettangolo(base_r, alt_r):.2f}")

raggio: float = 5.0
print(f"  Cerchio raggio = {raggio}:")
print(f"    Area = {area_cerchio(raggio):.2f}")
print(f"    Circonferenza = {circonferenza_cerchio(raggio):.2f}")

print("  Esercizio 2 superato!\n")


# =============================================================================
# Esercizio 3: Calcolo del BMI (Indice di Massa Corporea)
# BMI = peso_kg / altezza_m^2
# Classificazione:
#   < 18.5  → Sottopeso
#   18.5-24.9 → Normopeso
#   25.0-29.9 → Sovrappeso
#   >= 30.0   → Obesita'
# =============================================================================
print("--- Esercizio 3: Calcolo del BMI ---")


def calcola_bmi(peso_kg: float, altezza_m: float) -> float:
    """Calcola l'indice di massa corporea."""
    bmi: float = peso_kg / (altezza_m ** 2)
    return round(bmi, 1)


def classifica_bmi(bmi: float) -> str:
    """Restituisce la classificazione del BMI come stringa."""
    if bmi < 18.5:
        categoria: str = "Sottopeso"
    elif bmi < 25.0:
        categoria = "Normopeso"
    elif bmi < 30.0:
        categoria = "Sovrappeso"
    else:
        categoria = "Obesita'"
    return categoria


def report_bmi(peso_kg: float, altezza_m: float) -> str:
    """Genera un report completo del BMI."""
    bmi: float = calcola_bmi(peso_kg, altezza_m)
    categoria: str = classifica_bmi(bmi)
    report: str = f"Peso: {peso_kg} kg, Altezza: {altezza_m} m → BMI: {bmi} ({categoria})"
    return report


# Test BMI
assert calcola_bmi(70.0, 1.75) == 22.9
assert calcola_bmi(50.0, 1.70) == 17.3
assert calcola_bmi(95.0, 1.70) == 32.9

# Test classificazione
assert classifica_bmi(17.0) == "Sottopeso"
assert classifica_bmi(22.0) == "Normopeso"
assert classifica_bmi(27.5) == "Sovrappeso"
assert classifica_bmi(35.0) == "Obesita'"

# Test casi limite
assert classifica_bmi(18.5) == "Normopeso"
assert classifica_bmi(25.0) == "Sovrappeso"
assert classifica_bmi(30.0) == "Obesita'"

# Stampa report per diversi soggetti
soggetti: list[tuple[str, float, float]] = [
    ("Anna", 55.0, 1.65),
    ("Marco", 80.0, 1.80),
    ("Giulia", 48.0, 1.70),
    ("Luca", 105.0, 1.78),
]

for nome, peso, altezza in soggetti:
    bmi_val: float = calcola_bmi(peso, altezza)
    cat: str = classifica_bmi(bmi_val)
    print(f"  {nome:>8}: peso={peso:.0f}kg, h={altezza:.2f}m → BMI={bmi_val:.1f} ({cat})")

print("  Esercizio 3 superato!\n")


# =============================================================================
# Esercizio 4 (Bonus): Statistiche base di un dataset
# Calcolare media, minimo e massimo di una lista di voti.
# =============================================================================
print("--- Esercizio 4 (Bonus): Statistiche base ---")


def media_voti(voti: list[float]) -> float:
    """Calcola la media aritmetica di una lista di voti."""
    somma: float = sum(voti)
    n: int = len(voti)
    risultato: float = somma / n
    return round(risultato, 2)


def report_statistico(voti: list[float]) -> str:
    """Genera un report statistico di base per una lista di voti."""
    n: int = len(voti)
    med: float = media_voti(voti)
    minimo: float = min(voti)
    massimo: float = max(voti)
    report: str = (
        f"n={n}, media={med:.2f}, min={minimo:.1f}, max={massimo:.1f}"
    )
    return report


# Dati di test: voti di un esame
voti_esame: list[float] = [28.0, 30.0, 25.0, 18.0, 27.0, 30.0, 22.0, 26.0]

assert media_voti(voti_esame) == 25.75
assert min(voti_esame) == 18.0
assert max(voti_esame) == 30.0

# Voti con un solo elemento
assert media_voti([30.0]) == 30.0

print(f"  Voti: {voti_esame}")
print(f"  {report_statistico(voti_esame)}")
print("  Esercizio 4 superato!\n")


print("Tutti gli esercizi F07 completati con successo!")
