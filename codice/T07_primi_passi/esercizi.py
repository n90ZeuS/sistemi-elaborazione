# T07 — Primi passi in Python
# Esercizi per la lezione T07, con soluzione
# Variabili con type hints, operazioni aritmetiche, conversioni, f-string
#
# Gli esercizi usano solo ciò che è stato visto finora: variabili, tipi,
# operazioni aritmetiche (+ - * / **), conversioni di tipo e f-string.
# Condizioni (if) e input da tastiera arrivano in T08, i cicli in T09.
#
# Per ogni esercizio: leggete la consegna, scrivete la vostra versione in un
# file a parte e confrontate il risultato con i valori indicati in "Controllo".
#
# Le righe assert controllano il risultato: se la condizione è falsa il
# programma si ferma con AssertionError. Per confrontare numeri float si
# confronta il testo formattato (per esempio f"{x:.1f}" == "97.9"), perché
# due calcoli sui float possono differire nell'ultima cifra (0.1 + 0.2 != 0.3).
#
# import math rende disponibili math.pi e math.sqrt (radice quadrata).

import math

# =============================================================================
# Esercizio 1: conversione di temperatura
# Consegna: data una temperatura in gradi Celsius, calcolate i gradi
# Fahrenheit con F = C * 9 / 5 + 32. Poi, data una temperatura in Fahrenheit,
# calcolate i gradi Celsius con C = (F - 32) * 5 / 9.
# Stampate i risultati con una cifra decimale.
# Controllo: 25.0 °C = 77.0 °F; 36.6 °C = 97.9 °F; 98.6 °F = 37.0 °C;
#            -40.0 °C = -40.0 °F.
# =============================================================================
print("--- Esercizio 1: conversione di temperatura ---")

celsius: float = 25.0
fahrenheit: float = celsius * 9 / 5 + 32
print(f"  {celsius}°C = {fahrenheit:.1f}°F")
assert fahrenheit == 77.0

celsius_corporea: float = 36.6
fahrenheit_corporea: float = celsius_corporea * 9 / 5 + 32
print(f"  {celsius_corporea}°C = {fahrenheit_corporea:.1f}°F")
assert f"{fahrenheit_corporea:.1f}" == "97.9"

temp_f: float = 98.6
temp_c: float = (temp_f - 32) * 5 / 9
print(f"  {temp_f}°F = {temp_c:.1f}°C")
assert f"{temp_c:.1f}" == "37.0"

# -40 è l'unica temperatura uguale nelle due scale
celsius_uguale: float = -40.0
fahrenheit_uguale: float = celsius_uguale * 9 / 5 + 32
print(f"  {celsius_uguale}°C = {fahrenheit_uguale:.1f}°F")
assert fahrenheit_uguale == -40.0
print()


# =============================================================================
# Esercizio 2: area e perimetro di figure geometriche
# Consegna: calcolate
#   - area e perimetro di un rettangolo di base 8.5 e altezza 4.2;
#   - area e circonferenza di un cerchio di raggio 5.0 (usate math.pi,
#     che vale 3.141592653589793, dopo la riga import math in cima al file);
#   - area di un triangolo di base 6.0 e altezza 4.0.
# Stampate i risultati con due cifre decimali.
# Controllo: rettangolo area 35.70, perimetro 25.40; cerchio area 78.54,
#            circonferenza 31.42; triangolo area 12.00.
# =============================================================================
print("--- Esercizio 2: area e perimetro ---")

base_rettangolo: float = 8.5
altezza_rettangolo: float = 4.2
area_rettangolo: float = base_rettangolo * altezza_rettangolo
perimetro_rettangolo: float = 2 * (base_rettangolo + altezza_rettangolo)
print(f"  Rettangolo {base_rettangolo} x {altezza_rettangolo}:")
print(f"    area = {area_rettangolo:.2f}, perimetro = {perimetro_rettangolo:.2f}")
assert f"{area_rettangolo:.2f}" == "35.70"
assert f"{perimetro_rettangolo:.2f}" == "25.40"

raggio: float = 5.0
area_cerchio: float = math.pi * raggio ** 2
circonferenza: float = 2 * math.pi * raggio
print(f"  Cerchio di raggio {raggio}:")
print(f"    area = {area_cerchio:.2f}, circonferenza = {circonferenza:.2f}")
assert f"{area_cerchio:.2f}" == "78.54"
assert f"{circonferenza:.2f}" == "31.42"

base_triangolo: float = 6.0
altezza_triangolo: float = 4.0
area_triangolo: float = base_triangolo * altezza_triangolo / 2
print(f"  Triangolo {base_triangolo} x {altezza_triangolo}:")
print(f"    area = {area_triangolo:.2f}")
assert area_triangolo == 12.0
print()


# =============================================================================
# Esercizio 3: indice di massa corporea (BMI)
# Consegna: dati peso in kg e altezza in metri, calcolate
# BMI = peso / altezza ** 2 e stampatelo con una cifra decimale.
# Controllo: peso 70.0, altezza 1.75 -> BMI 22.9;
#            peso 95.0, altezza 1.70 -> BMI 32.9.
# (Stabilire la categoria, per esempio "sottopeso" se BMI < 18.5, richiede
# l'istruzione if: lo faremo in T08.)
# =============================================================================
print("--- Esercizio 3: BMI ---")

peso_kg: float = 70.0
altezza_m: float = 1.75
bmi: float = peso_kg / altezza_m ** 2  # ** ha la precedenza su /
print(f"  Peso {peso_kg} kg, altezza {altezza_m:.2f} m -> BMI {bmi:.1f}")
assert f"{bmi:.1f}" == "22.9"

peso_2: float = 95.0
altezza_2: float = 1.70
bmi_2: float = peso_2 / altezza_2 ** 2
print(f"  Peso {peso_2} kg, altezza {altezza_2:.2f} m -> BMI {bmi_2:.1f}")
assert f"{bmi_2:.1f}" == "32.9"
print()


# =============================================================================
# Esercizio 4: media di tre voti
# Consegna: dati tre voti interi, calcolate la media aritmetica e stampatela
# con due cifre decimali. Stampate anche il tipo della somma e della media.
# Controllo: voti 28, 30, 25 -> somma 83 (int), media 27.67 (float).
# =============================================================================
print("--- Esercizio 4: media di tre voti ---")

voto_1: int = 28
voto_2: int = 30
voto_3: int = 25
somma_voti: int = voto_1 + voto_2 + voto_3
media: float = somma_voti / 3  # / restituisce sempre un float
print(f"  Voti: {voto_1}, {voto_2}, {voto_3}")
print(f"  Somma = {somma_voti}, tipo {type(somma_voti)}")
print(f"  Media = {media:.2f}, tipo {type(media)}")
assert somma_voti == 83
assert f"{media:.2f}" == "27.67"
# Errore frequente: voto_1 + voto_2 + voto_3 / 3 divide per 3 solo voto_3
print()


# =============================================================================
# Esercizio 5: conversione di valuta
# Consegna: dato un importo in euro e il tasso di cambio (quanti dollari vale
# 1 euro), calcolate l'importo in dollari. Poi riconvertite il risultato in
# euro dividendo per lo stesso tasso. Usate nomi di variabile significativi.
# Controllo: 250.00 EUR con tasso 1.08 -> 270.00 USD -> 250.00 EUR.
# =============================================================================
print("--- Esercizio 5: conversione di valuta ---")

importo_euro: float = 250.0
tasso_eur_usd: float = 1.08
importo_dollari: float = importo_euro * tasso_eur_usd
importo_euro_ritorno: float = importo_dollari / tasso_eur_usd
print(f"  {importo_euro:.2f} EUR = {importo_dollari:.2f} USD (tasso {tasso_eur_usd})")
print(f"  {importo_dollari:.2f} USD = {importo_euro_ritorno:.2f} EUR")
assert f"{importo_dollari:.2f}" == "270.00"
assert f"{importo_euro_ritorno:.2f}" == "250.00"
print()


# =============================================================================
# Esercizio 6 (avanzato): distanza euclidea
# Consegna: dati i punti (x1, y1) e (x2, y2), calcolate la distanza
# d = radice quadrata di ((x2 - x1)**2 + (y2 - y1)**2) con math.sqrt.
# Stampatela con quattro cifre decimali.
# Controllo: (1, 2) e (4, 6) -> 5.0000 (triangolo rettangolo 3, 4, 5);
#            (0, 0) e (1, 1) -> 1.4142.
# =============================================================================
print("--- Esercizio 6: distanza euclidea ---")

x1: float = 1.0
y1: float = 2.0
x2: float = 4.0
y2: float = 6.0
distanza: float = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"  Distanza tra ({x1}, {y1}) e ({x2}, {y2}) = {distanza:.4f}")
assert distanza == 5.0

# In alternativa, la radice quadrata è l'elevamento alla potenza 0.5
diagonale: float = (1.0 ** 2 + 1.0 ** 2) ** 0.5
print(f"  Distanza tra (0.0, 0.0) e (1.0, 1.0) = {diagonale:.4f}")
assert f"{diagonale:.4f}" == "1.4142"
print()


print("Tutti i controlli sono passati: esercizi T07 completati.")
