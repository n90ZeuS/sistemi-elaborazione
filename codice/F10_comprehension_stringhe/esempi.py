# F10 — Comprehension e stringhe
# Esempi per la lezione frontale 10
# List/dict/set comprehension, metodi stringa, slicing, f-string avanzate

# =============================================================================
# 1. List comprehension — sintassi base
# =============================================================================
print("--- 1. List comprehension base ---")

# Sintassi: [espressione for variabile in iterabile]
quadrati: list[int] = [x ** 2 for x in range(1, 11)]
assert quadrati == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(f"  Quadrati 1-10: {quadrati}")

# Equivalente con ciclo for
quadrati_loop: list[int] = []
for x in range(1, 11):
    quadrati_loop.append(x ** 2)
assert quadrati == quadrati_loop

# Trasformazione di tipo
temperature_str: list[str] = ["36.5", "37.2", "38.1", "36.8", "37.0"]
temperature_float: list[float] = [float(t) for t in temperature_str]
assert temperature_float == [36.5, 37.2, 38.1, 36.8, 37.0]
print(f"  Temperature: {temperature_float}")


# =============================================================================
# 2. List comprehension con filtro (clausola if)
# =============================================================================
print("\n--- 2. Comprehension con filtro ---")

# Sintassi: [espressione for variabile in iterabile if condizione]
numeri: list[int] = list(range(1, 21))

pari: list[int] = [n for n in numeri if n % 2 == 0]
assert pari == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(f"  Pari 1-20: {pari}")

# Filtrare e trasformare contemporaneamente
# Quadrati dei numeri dispari
quadrati_dispari: list[int] = [n ** 2 for n in numeri if n % 2 != 0]
assert quadrati_dispari == [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
print(f"  Quadrati dispari: {quadrati_dispari}")

# Filtrare voti sufficienti
voti: list[int] = [28, 15, 22, 30, 17, 25, 10, 19, 30, 24]
sufficienti: list[int] = [v for v in voti if v >= 18]
assert sufficienti == [28, 22, 30, 25, 19, 30, 24]
print(f"  Voti sufficienti: {sufficienti}")

# Espressione condizionale nella parte espressione (if-else)
# Attenzione: il if-else va PRIMA del for, il filtro DOPO
etichette: list[str] = ["OK" if v >= 18 else "KO" for v in voti]
assert etichette == ["OK", "KO", "OK", "OK", "KO", "OK", "KO", "OK", "OK", "OK"]
print(f"  Etichette: {etichette}")


# =============================================================================
# 3. Dict e set comprehension
# =============================================================================
print("\n--- 3. Dict e set comprehension ---")

# Dict comprehension: {chiave: valore for ...}
nomi: list[str] = ["Alice", "Bob", "Carla", "Davide"]
lunghezze: dict[str, int] = {nome: len(nome) for nome in nomi}
assert lunghezze == {"Alice": 5, "Bob": 3, "Carla": 5, "Davide": 6}
print(f"  Lunghezze nomi: {lunghezze}")

# Invertire un dizionario
originale: dict[str, int] = {"a": 1, "b": 2, "c": 3}
invertito: dict[int, str] = {v: k for k, v in originale.items()}
assert invertito == {1: "a", 2: "b", 3: "c"}
print(f"  Invertito: {invertito}")

# Set comprehension: {espressione for ...}
parole: list[str] = ["ciao", "hello", "CIAO", "Hello", "arrivederci"]
parole_uniche_lower: set[str] = {p.lower() for p in parole}
assert parole_uniche_lower == {"ciao", "hello", "arrivederci"}
print(f"  Parole uniche (lower): {sorted(parole_uniche_lower)}")

# Cifre presenti in un numero
numero_grande: int = 112233445566
cifre_presenti: set[str] = {c for c in str(numero_grande)}
assert cifre_presenti == {"1", "2", "3", "4", "5", "6"}
print(f"  Cifre in {numero_grande}: {sorted(cifre_presenti)}")


# =============================================================================
# 4. Comprehension annidate
# =============================================================================
print("\n--- 4. Comprehension annidate ---")

# Matrice 3x4 con comprehension
matrice: list[list[int]] = [[i * 4 + j + 1 for j in range(4)] for i in range(3)]
assert matrice == [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(f"  Matrice 3x4:")
for riga in matrice:
    print(f"    {riga}")

# Appiattire una matrice (flatten)
piatta: list[int] = [elem for riga in matrice for elem in riga]
assert piatta == list(range(1, 13))
print(f"  Appiattita: {piatta}")

# Tutte le coppie (i, j) con i < j
coppie: list[tuple[int, int]] = [(i, j) for i in range(4) for j in range(i + 1, 4)]
assert len(coppie) == 6
print(f"  Coppie (i,j) con i<j, range(4): {coppie}")


# =============================================================================
# 5. Metodi delle stringhe
# =============================================================================
print("\n--- 5. Metodi delle stringhe ---")

testo: str = "  Python e' un linguaggio fantastico!  "

# upper, lower, title, capitalize
assert testo.strip().upper() == "PYTHON E' UN LINGUAGGIO FANTASTICO!"
assert testo.strip().lower() == "python e' un linguaggio fantastico!"
assert testo.strip().title() == "Python E' Un Linguaggio Fantastico!"
print(f"  Originale: '{testo}'")
print(f"  strip():   '{testo.strip()}'")
print(f"  upper():   '{testo.strip().upper()}'")
print(f"  lower():   '{testo.strip().lower()}'")

# split e join
frase: str = "uno due tre quattro cinque"
parole_lista: list[str] = frase.split()
assert parole_lista == ["uno", "due", "tre", "quattro", "cinque"]
print(f"\n  split(): {parole_lista}")

ricomposta: str = " - ".join(parole_lista)
assert ricomposta == "uno - due - tre - quattro - cinque"
print(f"  join(' - '): '{ricomposta}'")

# split con separatore specifico
csv_riga: str = "Alice,28,Informatica,Bologna"
campi: list[str] = csv_riga.split(",")
assert campi == ["Alice", "28", "Informatica", "Bologna"]
print(f"\n  CSV: '{csv_riga}'")
print(f"  split(','): {campi}")

# replace
frase_nuova: str = frase.replace("tre", "3")
assert frase_nuova == "uno due 3 quattro cinque"
print(f"\n  replace('tre', '3'): '{frase_nuova}'")

# find e index
pos: int = frase.find("tre")
assert pos == 8
pos_non_trovato: int = frase.find("sei")
assert pos_non_trovato == -1  # find restituisce -1 se non trova
print(f"\n  find('tre'): {pos}")
print(f"  find('sei'): {pos_non_trovato}")

# startswith e endswith
nome_file: str = "relazione_finale.pdf"
assert nome_file.startswith("relazione")
assert nome_file.endswith(".pdf")
assert not nome_file.endswith(".docx")
print(f"\n  '{nome_file}'.endswith('.pdf'): {nome_file.endswith('.pdf')}")

# Metodi di verifica
assert "42".isdigit()
assert "ciao".isalpha()
assert "ciao42".isalnum()
assert "   ".isspace()
print(f"  '42'.isdigit() = {('42').isdigit()}")
print(f"  'ciao'.isalpha() = {'ciao'.isalpha()}")


# =============================================================================
# 6. Slicing delle stringhe
# =============================================================================
print("\n--- 6. String slicing ---")

s: str = "Programmazione"

# s[start:stop:step] — stop escluso
assert s[0:6] == "Progra"
assert s[:6] == "Progra"        # start default = 0
assert s[6:] == "mmazione"      # stop default = fine
assert s[-6:] == "azione"       # Indici negativi
assert s[::2] == "Pormain"      # Ogni 2 caratteri
assert s[::-1] == "enoizammargorP"  # Stringa invertita

print(f"  s = '{s}'")
print(f"  s[0:6]   = '{s[0:6]}'")
print(f"  s[6:]    = '{s[6:]}'")
print(f"  s[-6:]   = '{s[-6:]}'")
print(f"  s[::2]   = '{s[::2]}'")
print(f"  s[::-1]  = '{s[::-1]}'")

# Verificare se una stringa e' un palindromo
def is_palindromo(testo: str) -> bool:
    """Verifica se una stringa e' un palindromo (ignorando maiuscole e spazi)."""
    pulita: str = testo.lower().replace(" ", "")
    return pulita == pulita[::-1]

assert is_palindromo("anna") is True
assert is_palindromo("i topi non avevano nipoti") is True
assert is_palindromo("python") is False
print(f"\n  'anna' palindromo? {is_palindromo('anna')}")
print(f"  'i topi non avevano nipoti' palindromo? {is_palindromo('i topi non avevano nipoti')}")


# =============================================================================
# 7. f-string avanzate
# =============================================================================
print("\n--- 7. f-string avanzate ---")

# Debug con = (Python 3.8+)
x: int = 42
y: float = 3.14
print(f"  {x = }")      # Stampa 'x = 42'
print(f"  {y = :.1f}")  # Stampa 'y = 3.1'

# Formattazione di tabelle
studenti: list[tuple[str, int, float]] = [
    ("Alice", 28, 98.5),
    ("Bob", 22, 75.3),
    ("Carla", 30, 100.0),
    ("Davide", 25, 88.7),
]

print(f"\n  {'Nome':<12}{'Voto':>6}{'Percentile':>12}")
print(f"  {'-' * 30}")
for nome_s, voto_s, perc in studenti:
    print(f"  {nome_s:<12}{voto_s:>6}{perc:>11.1f}%")

# Numeri con formattazione speciale
grande: int = 1_500_000
piccolo: float = 0.00034567
print(f"\n  Separatore migliaia: {grande:,}")
print(f"  Notazione scientifica: {piccolo:.3e}")
print(f"  Binario: {255:b}")
print(f"  Esadecimale: {255:x}")
print(f"  Ottale: {255:o}")


print("\nTutti gli assert passati — esempi F10 completati con successo!")
