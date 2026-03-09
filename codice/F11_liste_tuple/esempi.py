# F11 — Liste e tuple
# Esempi per la lezione frontale 11
# Creazione, indicizzazione, slicing, metodi, copia shallow/deep, tuple, unpacking

# =============================================================================
# 1. Creazione e indicizzazione
# =============================================================================
print("--- 1. Creazione e indicizzazione ---")

# Creazione di liste
vuota: list[int] = []
numeri: list[int] = [10, 20, 30, 40, 50]
mista: list[int | str | float | bool] = [1, "due", 3.0, True]

# Indicizzazione 0-based
assert numeri[0] == 10   # Primo elemento
assert numeri[2] == 30   # Terzo elemento
assert numeri[4] == 50   # Ultimo elemento
assert numeri[-1] == 50  # Ultimo (indice negativo)
assert numeri[-2] == 40  # Penultimo

print(f"  numeri = {numeri}")
print(f"  numeri[0]  = {numeri[0]}  (primo)")
print(f"  numeri[-1] = {numeri[-1]} (ultimo)")
print(f"  numeri[-2] = {numeri[-2]} (penultimo)")

# Modifica di un elemento (le liste sono mutabili)
numeri[2] = 99
assert numeri == [10, 20, 99, 40, 50]
numeri[2] = 30  # Ripristiniamo
print(f"\n  Dopo numeri[2] = 99: {[10, 20, 99, 40, 50]}")


# =============================================================================
# 2. Slicing delle liste
# =============================================================================
print("\n--- 2. Slicing ---")

lettere: list[str] = ["a", "b", "c", "d", "e", "f", "g"]

# lista[start:stop] — da start a stop-1
assert lettere[1:4] == ["b", "c", "d"]
assert lettere[:3] == ["a", "b", "c"]       # Dall'inizio
assert lettere[4:] == ["e", "f", "g"]       # Fino alla fine
assert lettere[-3:] == ["e", "f", "g"]      # Ultimi 3
assert lettere[::2] == ["a", "c", "e", "g"]  # Ogni 2
assert lettere[::-1] == ["g", "f", "e", "d", "c", "b", "a"]  # Invertita

print(f"  lettere = {lettere}")
print(f"  lettere[1:4]  = {lettere[1:4]}")
print(f"  lettere[:3]   = {lettere[:3]}")
print(f"  lettere[4:]   = {lettere[4:]}")
print(f"  lettere[::2]  = {lettere[::2]}")
print(f"  lettere[::-1] = {lettere[::-1]}")

# Assegnamento a una slice (modifica multipla)
dati: list[int] = [1, 2, 3, 4, 5]
dati[1:3] = [20, 30]  # Sostituisce gli elementi nelle posizioni 1 e 2
assert dati == [1, 20, 30, 4, 5]
print(f"\n  Dopo dati[1:3] = [20, 30]: {dati}")

# Lo slice crea una copia superficiale
copia_slice: list[str] = lettere[:]
assert copia_slice == lettere
assert copia_slice is not lettere
print(f"  lettere[:] crea una copia: {copia_slice is not lettere}")


# =============================================================================
# 3. Metodi delle liste
# =============================================================================
print("\n--- 3. Metodi delle liste ---")

frutti: list[str] = ["mela", "banana", "arancia"]

# append: aggiunge alla fine
frutti.append("uva")
assert frutti == ["mela", "banana", "arancia", "uva"]
print(f"  Dopo append('uva'): {frutti}")

# insert: inserisce in una posizione specifica
frutti.insert(1, "pera")
assert frutti == ["mela", "pera", "banana", "arancia", "uva"]
print(f"  Dopo insert(1, 'pera'): {frutti}")

# extend: aggiunge piu' elementi (da un iterabile)
frutti.extend(["kiwi", "mango"])
assert frutti[-2:] == ["kiwi", "mango"]
print(f"  Dopo extend(['kiwi', 'mango']): {frutti}")

# remove: rimuove la prima occorrenza di un valore
frutti.remove("banana")
assert "banana" not in frutti
print(f"  Dopo remove('banana'): {frutti}")

# pop: rimuove e restituisce un elemento (default: ultimo)
ultimo: str = frutti.pop()
assert ultimo == "mango"
print(f"  pop() ha rimosso: '{ultimo}', lista: {frutti}")

secondo: str = frutti.pop(1)
assert secondo == "pera"
print(f"  pop(1) ha rimosso: '{secondo}', lista: {frutti}")

# sort: ordina in-place
numeri_disordinati: list[int] = [42, 7, 15, 3, 28, 11]
numeri_disordinati.sort()
assert numeri_disordinati == [3, 7, 11, 15, 28, 42]
print(f"\n  sort(): {numeri_disordinati}")

# sort con reverse
numeri_disordinati.sort(reverse=True)
assert numeri_disordinati == [42, 28, 15, 11, 7, 3]
print(f"  sort(reverse=True): {numeri_disordinati}")

# sort con chiave personalizzata
parole: list[str] = ["banana", "mela", "uva", "arancia", "kiwi"]
parole.sort(key=len)  # Ordina per lunghezza
assert parole == ["uva", "mela", "kiwi", "banana", "arancia"]
print(f"  sort(key=len): {parole}")

# sorted() restituisce una NUOVA lista (non modifica l'originale)
originale: list[int] = [5, 2, 8, 1, 9]
ordinata: list[int] = sorted(originale)
assert originale == [5, 2, 8, 1, 9]  # Non modificata!
assert ordinata == [1, 2, 5, 8, 9]
print(f"\n  sorted() non modifica l'originale: {originale} → {ordinata}")

# reverse: inverte in-place
numeri_seq: list[int] = [1, 2, 3, 4, 5]
numeri_seq.reverse()
assert numeri_seq == [5, 4, 3, 2, 1]
print(f"  reverse(): {numeri_seq}")

# Altre operazioni utili
numeri_test: list[int] = [10, 20, 30, 20, 40, 20]
assert numeri_test.count(20) == 3
assert numeri_test.index(30) == 2
assert len(numeri_test) == 6
print(f"\n  {numeri_test}.count(20) = {numeri_test.count(20)}")
print(f"  {numeri_test}.index(30) = {numeri_test.index(30)}")


# =============================================================================
# 4. Copia shallow vs deep
# =============================================================================
print("\n--- 4. Shallow copy vs deep copy ---")

import copy

# ALIAS — stessa lista in memoria
originale_2d: list[list[int]] = [[1, 2], [3, 4], [5, 6]]
alias: list[list[int]] = originale_2d
assert alias is originale_2d  # Stesso oggetto!

# SHALLOW COPY — nuova lista, ma gli elementi interni sono condivisi
shallow: list[list[int]] = originale_2d.copy()  # equivale a originale_2d[:]
assert shallow is not originale_2d      # Lista esterna diversa
assert shallow[0] is originale_2d[0]    # Ma le sotto-liste sono le stesse!

# Modificare una sotto-lista nella copia shallow modifica anche l'originale
shallow[0][0] = 999
assert originale_2d[0][0] == 999  # Modificato anche l'originale!
originale_2d[0][0] = 1  # Ripristiniamo

print(f"  Originale: {originale_2d}")
print(f"  Shallow copy condivide le sotto-liste: {shallow[0] is originale_2d[0]}")

# DEEP COPY — copia completamente indipendente
deep: list[list[int]] = copy.deepcopy(originale_2d)
assert deep is not originale_2d
assert deep[0] is not originale_2d[0]  # Anche le sotto-liste sono diverse!

deep[0][0] = 888
assert originale_2d[0][0] == 1  # L'originale NON e' modificato

print(f"  Deep copy indipendente: modifica deep[0][0]=888, originale[0][0]={originale_2d[0][0]}")

# Riepilogo visivo
print(f"\n  Riepilogo:")
print(f"    alias = originale     → alias is originale: True")
print(f"    shallow = orig.copy() → shallow is orig: False, shallow[0] is orig[0]: True")
print(f"    deep = deepcopy(orig) → deep is orig: False, deep[0] is orig[0]: False")


# =============================================================================
# 5. Tuple — sequenze immutabili
# =============================================================================
print("\n--- 5. Tuple ---")

# Creazione
punto: tuple[float, float] = (3.0, 4.0)
singolo: tuple[int] = (42,)  # La virgola e' necessaria per tuple con un elemento!
vuota_t: tuple[()] = ()

assert type(punto) is tuple
assert type(singolo) is tuple
assert len(singolo) == 1

# Indicizzazione (come le liste)
assert punto[0] == 3.0
assert punto[1] == 4.0
assert punto[-1] == 4.0

# Le tuple sono IMMUTABILI — non si possono modificare
try:
    punto[0] = 5.0  # type: ignore
    assert False, "Doveva lanciare TypeError"
except TypeError as e:
    print(f"  punto[0] = 5.0 → TypeError: {e}")

# Le tuple possono contenere oggetti mutabili (ma la tuple stessa non cambia)
strano: tuple[int, list[int]] = (1, [2, 3])
strano[1].append(4)  # La lista interna e' mutabile!
assert strano == (1, [2, 3, 4])
print(f"  Tuple con lista interna: {strano}")

# Operazioni sulle tuple (come le liste, tranne quelle che modificano)
numeri_t: tuple[int, ...] = (5, 3, 8, 1, 5, 3, 5)
assert numeri_t.count(5) == 3
assert numeri_t.index(8) == 2
assert len(numeri_t) == 7
assert max(numeri_t) == 8
assert min(numeri_t) == 1
assert sum(numeri_t) == 30
assert sorted(numeri_t) == [1, 3, 3, 5, 5, 5, 8]  # sorted restituisce una lista!

print(f"\n  numeri_t = {numeri_t}")
print(f"  count(5) = {numeri_t.count(5)}")
print(f"  sorted() = {sorted(numeri_t)} (restituisce lista!)")


# =============================================================================
# 6. Tuple unpacking
# =============================================================================
print("\n--- 6. Tuple unpacking ---")

# Unpacking base
coordinate: tuple[float, float, float] = (1.5, 2.7, 3.9)
x, y, z = coordinate
assert x == 1.5 and y == 2.7 and z == 3.9
print(f"  x, y, z = {coordinate} → x={x}, y={y}, z={z}")

# Unpacking con * (raccolta dei rimanenti)
primi: list[int] = [10, 20, 30, 40, 50]
primo, secondo_el, *resto = primi
assert primo == 10
assert secondo_el == 20
assert resto == [30, 40, 50]
print(f"  primo, secondo, *resto = {primi}")
print(f"    primo={primo}, secondo={secondo_el}, resto={resto}")

# * al centro
primo_v, *mezzo, ultimo_v = primi
assert primo_v == 10
assert mezzo == [20, 30, 40]
assert ultimo_v == 50
print(f"  primo, *mezzo, ultimo = {primi}")
print(f"    primo={primo_v}, mezzo={mezzo}, ultimo={ultimo_v}")

# Unpacking nella funzione: restituire piu' valori
def min_max_media(valori: list[float]) -> tuple[float, float, float]:
    """Restituisce minimo, massimo e media di una lista."""
    minimo: float = min(valori)
    massimo: float = max(valori)
    media: float = sum(valori) / len(valori)
    return minimo, massimo, media  # Restituisce una tupla


voti: list[float] = [28.0, 22.0, 30.0, 19.0, 25.0, 27.0]
vmin, vmax, vmedia = min_max_media(voti)  # Unpacking del risultato
assert vmin == 19.0
assert vmax == 30.0
assert abs(vmedia - 25.1667) < 0.001
print(f"\n  Voti: {voti}")
print(f"  min={vmin}, max={vmax}, media={vmedia:.2f}")

# Scambio di variabili (usa tuple unpacking sotto il cofano)
a: int = 10
b: int = 20
a, b = b, a
assert a == 20 and b == 10
print(f"\n  Scambio: a=10, b=20 → a={a}, b={b}")


# =============================================================================
# 7. Named tuple (cenni)
# =============================================================================
print("\n--- 7. Named tuple ---")

from collections import namedtuple

# Definizione di un tipo named tuple
Studente = namedtuple("Studente", ["nome", "matricola", "media"])

# Creazione di istanze
s1: Studente = Studente("Alice", "0001234", 28.5)
s2: Studente = Studente(nome="Bob", matricola="0001235", media=25.0)

# Accesso per nome (piu' leggibile) o per indice
assert s1.nome == "Alice"
assert s1[0] == "Alice"      # Anche per indice (e' una tupla)
assert s1.media == 28.5

# Le named tuple sono immutabili
try:
    s1.nome = "Anna"  # type: ignore
    assert False
except AttributeError as e:
    print(f"  s1.nome = 'Anna' → AttributeError: {e}")

# _replace crea una NUOVA named tuple
s1_aggiornato: Studente = s1._replace(media=29.0)
assert s1.media == 28.5       # Originale invariato
assert s1_aggiornato.media == 29.0
print(f"  s1 = {s1}")
print(f"  s1._replace(media=29.0) = {s1_aggiornato}")

# Conversione a dizionario
assert s1._asdict() == {"nome": "Alice", "matricola": "0001234", "media": 28.5}
print(f"  s1._asdict() = {s1._asdict()}")

# Lista di studenti
classe: list[Studente] = [
    Studente("Alice", "001", 28.5),
    Studente("Bob", "002", 25.0),
    Studente("Carla", "003", 30.0),
    Studente("Davide", "004", 22.5),
]

# Ordinare per media
per_media: list[Studente] = sorted(classe, key=lambda s: s.media, reverse=True)
print(f"\n  Classifica per media:")
for pos, stud in enumerate(per_media, start=1):
    print(f"    {pos}. {stud.nome} — media: {stud.media}")


print("\nTutti gli assert passati — esempi F11 completati con successo!")
