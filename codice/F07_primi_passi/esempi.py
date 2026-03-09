# F07 — Primi passi in Python
# Esempi per la lezione frontale 7
# Variabili, tipi, type hints, casting, f-string

# =============================================================================
# 1. Creazione di variabili con type hints
# =============================================================================
# In Python, una variabile e' un'etichetta che punta a un oggetto in memoria.
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

# isinstance() e' spesso preferibile a type() per i controlli
assert isinstance(nome, str)
assert isinstance(eta, int)
assert isinstance(altezza, float)
assert isinstance(studente, bool)

# Nota: bool e' una sottoclasse di int in Python
assert isinstance(True, int)
print(f"\nbool e' sottoclasse di int: isinstance(True, int) = {isinstance(True, int)}")


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

# Da float a intero (troncamento, NON arrotondamento)
valore: float = 9.87
valore_troncato: int = int(valore)
assert valore_troncato == 9  # Tronca, non arrotonda!
print(f"int(9.87)   = {valore_troncato} (troncamento!)")

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
assert bool(None) is False
assert bool([]) is False
assert bool([1]) is True
print("\nValori 'falsy': 0, '', None, [], {}, set(), 0.0")
print("Tutto il resto e' 'truthy'")


# =============================================================================
# 4. f-string — formattazione avanzata
# =============================================================================
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
assert media_formattata == "Media: 27.35"  # Arrotondamento!

# Allineamento e padding
print(f"{'Esame':<20}{'Voto':>5}")
print(f"{'Analisi I':<20}{28:>5}")
print(f"{'Programmazione':<20}{30:>5}")
print(f"{'Fisica':<20}{25:>5}")

# Espressioni dentro le f-string
a: int = 10
b: int = 3
print(f"\n{a} + {b} = {a + b}")
print(f"{a} / {b} = {a / b:.4f}")
print(f"{a} e' pari? {a % 2 == 0}")

# Percentuali
superati: int = 18
totali: int = 25
percentuale: float = superati / totali
print(f"\nEsami superati: {percentuale:.1%}")  # 72.0%
assert f"{percentuale:.1%}" == "72.0%"

# Separatore delle migliaia
popolazione: int = 1_380_000_000
print(f"Popolazione: {popolazione:,}")  # 1,380,000,000


# =============================================================================
# 5. Assegnamento come etichetta → oggetto
# =============================================================================
print("\n--- 5. Assegnamento come etichetta → oggetto ---")

# Due variabili possono puntare allo stesso oggetto
x: int = 42
y: int = x
assert x is y  # Stesso oggetto in memoria (per interi piccoli, Python li "interna")
print(f"x = {x}, y = {y}, x is y = {x is y}")

# Con liste, la condivisione e' evidente
lista_a: list[int] = [1, 2, 3]
lista_b: list[int] = lista_a  # lista_b e' un ALIAS, non una copia!
lista_b.append(4)
assert lista_a == [1, 2, 3, 4]  # Anche lista_a e' cambiata!
print(f"lista_a = {lista_a}")
print(f"lista_b = {lista_b}")
print(f"lista_a is lista_b = {lista_a is lista_b}")

# Per creare una copia indipendente:
lista_c: list[int] = lista_a.copy()
lista_c.append(5)
assert lista_a == [1, 2, 3, 4]  # lista_a NON cambia
assert lista_c == [1, 2, 3, 4, 5]
print(f"\nDopo lista_c = lista_a.copy() e lista_c.append(5):")
print(f"lista_a = {lista_a}")
print(f"lista_c = {lista_c}")
print(f"lista_a is lista_c = {lista_a is lista_c}")

# La funzione id() mostra l'indirizzo in memoria
print(f"\nid(lista_a) = {id(lista_a)}")
print(f"id(lista_b) = {id(lista_b)} (uguale!)")
print(f"id(lista_c) = {id(lista_c)} (diverso!)")


# =============================================================================
# 6. Assegnamento multiplo e scambio
# =============================================================================
print("\n--- 6. Assegnamento multiplo ---")

# Assegnamento multiplo
a, b, c = 1, 2.0, "tre"
assert a == 1 and b == 2.0 and c == "tre"
print(f"a = {a}, b = {b}, c = {c}")

# Scambio elegante di due variabili (senza variabile temporanea)
x: int = 10
y: int = 20
x, y = y, x
assert x == 20 and y == 10
print(f"Dopo scambio: x = {x}, y = {y}")

# Assegnamento ripetuto
a = b = c = 0
assert a == 0 and b == 0 and c == 0
print(f"a = b = c = {a}")


print("\n✓ Tutti gli assert passati — esempi F07 completati con successo!")
