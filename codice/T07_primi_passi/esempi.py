# T07 — Primi passi in Python
# Esempi per la lezione T07
# Variabili, tipi, type hints, casting, f-string
#
# Le righe che iniziano con assert controllano un risultato: se la condizione
# è falsa il programma si ferma con AssertionError. Se il file arriva in fondo,
# tutti i controlli sono passati.

# =============================================================================
# 1. Creazione di variabili con type hints
# =============================================================================
# In Python, una variabile è un'etichetta che punta a un oggetto in memoria.
# I type hints indicano il tipo atteso (ma non sono vincolanti a runtime).

nome: str = "Alice"
eta: int = 23
altezza: float = 1.68
studente: bool = True
voto_esame: None = None  # Nessun voto ancora assegnato

assert nome == "Alice"
assert eta == 23
assert altezza == 1.68
assert studente is True
assert voto_esame is None

print("--- 1. Variabili con type hints ---")
print(f"nome = {nome}, eta = {eta}, altezza = {altezza}")
print(f"studente = {studente}, voto_esame = {voto_esame}")


# =============================================================================
# 2. La funzione type() — verificare il tipo di un oggetto
# =============================================================================
print("\n--- 2. Funzione type() ---")

print(f"type(nome)       = {type(nome)}")        # <class 'str'>
print(f"type(eta)        = {type(eta)}")         # <class 'int'>
print(f"type(altezza)    = {type(altezza)}")     # <class 'float'>
print(f"type(studente)   = {type(studente)}")    # <class 'bool'>
print(f"type(voto_esame) = {type(voto_esame)}")  # <class 'NoneType'>

assert type(nome) is str
assert type(eta) is int
assert type(altezza) is float
assert type(studente) is bool
assert type(voto_esame) is type(None)

# isinstance(oggetto, tipo) risponde True se l'oggetto è di quel tipo
assert isinstance(nome, str)
assert isinstance(eta, int)
assert isinstance(altezza, float)
assert isinstance(studente, bool)

# bool è un sottotipo di int: True vale 1, False vale 0
assert isinstance(True, int)
print(f"\nbool è sottotipo di int: isinstance(True, int) = {isinstance(True, int)}")
print(f"True + True = {True + True}")  # 2


# =============================================================================
# 3. Casting — conversione esplicita tra tipi
# =============================================================================
print("\n--- 3. Casting ---")

# Da stringa a intero
eta_stringa: str = "25"
eta_intero: int = int(eta_stringa)
assert eta_intero == 25
assert type(eta_intero) is int
print(f"int('25')   = {eta_intero} (tipo: {type(eta_intero).__name__})")

# Da stringa a float
pi_stringa: str = "3.14"
pi_float: float = float(pi_stringa)
assert pi_float == 3.14
print(f"float('3.14') = {pi_float} (tipo: {type(pi_float).__name__})")

# Da intero a float
numero_intero: int = 7
numero_float: float = float(numero_intero)
assert numero_float == 7.0
print(f"float(7)    = {numero_float} (tipo: {type(numero_float).__name__})")

# Da float a intero: int() tronca la parte decimale, non arrotonda
valore: float = 9.87
valore_troncato: int = int(valore)
assert valore_troncato == 9  # non 10
print(f"int(9.87)   = {valore_troncato} (troncamento)")

# Da numero a stringa
prezzo: float = 19.99
prezzo_str: str = str(prezzo)
assert prezzo_str == "19.99"
assert type(prezzo_str) is str
print(f"str(19.99)  = '{prezzo_str}' (tipo: {type(prezzo_str).__name__})")

# Conversioni booleane
assert bool(0) is False
assert bool(1) is True
assert bool("") is False
assert bool("ciao") is True
assert bool(0.0) is False
assert bool(42) is True
assert bool(None) is False
print("\nbool() restituisce False per 0, 0.0, '' (stringa vuota) e None")
print("Per tutti gli altri valori visti oggi restituisce True")


# =============================================================================
# 4. f-string — formattazione
# =============================================================================
# A lezione abbiamo visto {valore:.1f} (una cifra decimale). Qui ci sono
# anche altri formati, da usare come riferimento: allineamento, percentuali,
# separatore delle migliaia.
print("\n--- 4. f-string ---")

nome_studente: str = "Marco"
media_voti: float = 27.3456
esami_superati: int = 12

# Formattazione base
messaggio: str = f"{nome_studente} ha superato {esami_superati} esami"
print(messaggio)
assert "Marco" in messaggio
assert "12" in messaggio

# Formattazione numerica: cifre decimali
media_formattata: str = f"Media: {media_voti:.2f}"
print(media_formattata)
assert media_formattata == "Media: 27.35"  # :.2f arrotonda 27.3456 a 27.35

# Allineamento: :<20 allinea a sinistra in 20 caratteri, :>5 a destra in 5
print(f"{'Esame':<20}{'Voto':>5}")
print(f"{'Analisi I':<20}{28:>5}")
print(f"{'Programmazione':<20}{30:>5}")
print(f"{'Fisica':<20}{25:>5}")

# Espressioni dentro le f-string
a: int = 10
b: int = 3
print(f"\n{a} + {b} = {a + b}")
print(f"{a} / {b} = {a / b:.4f}")
print(f"{a} * {b} = {a * b}")

# Percentuali: :.1% moltiplica per 100 e aggiunge il simbolo %
superati: int = 18
totali: int = 25
percentuale: float = superati / totali
print(f"\nEsami superati: {percentuale:.1%}")  # 72.0%
assert f"{percentuale:.1%}" == "72.0%"

# Separatore delle migliaia: :, (usa la virgola, come nella notazione inglese)
popolazione: int = 1_380_000_000
print(f"Popolazione: {popolazione:,}")  # 1,380,000,000


# =============================================================================
# 5. Assegnamento come etichetta → oggetto
# =============================================================================
print("\n--- 5. Assegnamento come etichetta → oggetto ---")

# y = x attacca l'etichetta y allo stesso oggetto di x: nessuna copia
x: int = 42
y: int = x
assert x is y  # stesso oggetto in memoria
print(f"x = {x}, y = {y}, x is y = {x is y}")

# Anticipazione (le liste si vedono in T11): con una lista, che si può
# modificare, l'effetto della condivisione si vede
lista_a: list[int] = [1, 2, 3]
lista_b: list[int] = lista_a  # lista_b è un alias di lista_a, non una copia
lista_b.append(4)
assert lista_a == [1, 2, 3, 4]  # anche lista_a è cambiata
print(f"lista_a = {lista_a}")
print(f"lista_b = {lista_b}")
print(f"lista_a is lista_b = {lista_a is lista_b}")

# Per creare una copia indipendente:
lista_c: list[int] = lista_a.copy()
lista_c.append(5)
assert lista_a == [1, 2, 3, 4]  # lista_a non cambia
assert lista_c == [1, 2, 3, 4, 5]
print("\nDopo lista_c = lista_a.copy() e lista_c.append(5):")
print(f"lista_a = {lista_a}")
print(f"lista_c = {lista_c}")
print(f"lista_a is lista_c = {lista_a is lista_c}")

# id() restituisce un numero che identifica l'oggetto (in CPython è il suo
# indirizzo in memoria); i valori cambiano a ogni esecuzione
print(f"\nid(lista_a) = {id(lista_a)}")
print(f"id(lista_b) = {id(lista_b)} (uguale a lista_a)")
print(f"id(lista_c) = {id(lista_c)} (diverso)")


# =============================================================================
# 6. Assegnamento multiplo e scambio
# =============================================================================
print("\n--- 6. Assegnamento multiplo ---")

# Assegnamento multiplo (unpacking): il primo valore va al primo nome, ecc.
primo, secondo, terzo = 1, 2.0, "tre"
assert primo == 1 and secondo == 2.0 and terzo == "tre"
print(f"primo = {primo}, secondo = {secondo}, terzo = {terzo}")

# Scambio di due variabili senza variabile temporanea
# (x e y sono già state dichiarate int nella sezione 5)
x = 10
y = 20
x, y = y, x
assert x == 20 and y == 10
print(f"Dopo lo scambio: x = {x}, y = {y}")

# Stesso valore a più nomi: tutti e tre puntano all'oggetto 0
maschi = femmine = totale = 0
assert maschi == 0 and femmine == 0 and totale == 0
print(f"maschi = femmine = totale = {maschi}")


print("\nTutti gli assert sono passati: esempi T07 completati.")
