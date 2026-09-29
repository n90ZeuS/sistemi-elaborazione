# T12 — Dizionari, set e mutabilità
# Esempi per la lezione frontale 12

# ============================================================
# 1. CREAZIONE DI DIZIONARI
# ============================================================

# Creazione letterale
studente: dict[str, str | int] = {
    "nome": "Marco",
    "cognome": "Rossi",
    "matricola": 12345,
    "corso": "Informatica",
}
print("=== Creazione dizionari ===")
print(f"Studente: {studente}")

# Creazione con dict()
voti: dict[str, int] = dict(matematica=28, fisica=30, chimica=25)
print(f"Voti: {voti}")

# Creazione da lista di coppie
coppie: list[tuple[str, int]] = [("a", 1), ("b", 2), ("c", 3)]
da_coppie: dict[str, int] = dict(coppie)
assert da_coppie == {"a": 1, "b": 2, "c": 3}
print(f"Da coppie: {da_coppie}")

# ============================================================
# 2. ACCESSO AI VALORI: [], .get(), .setdefault()
# ============================================================
print("\n=== Accesso ai valori ===")

# Accesso con []
nome: str = studente["nome"]
assert nome == "Marco"
print(f"Nome (con []): {nome}")

# Accesso con .get() — ritorna None se la chiave non esiste
email: str | None = studente.get("email")
assert email is None
print(f"Email (con .get()): {email}")

# .get() con valore predefinito
email_default: str = studente.get("email", "non disponibile")
assert email_default == "non disponibile"
print(f"Email (con default): {email_default}")

# .setdefault() — inserisce la chiave se non esiste e ritorna il valore
anno: int = studente.setdefault("anno", 2024)
assert anno == 2024
assert studente["anno"] == 2024
print(f"Anno (con .setdefault()): {anno}")
print(f"Studente aggiornato: {studente}")

# ============================================================
# 3. MODIFICA E .update()
# ============================================================
print("\n=== Modifica e .update() ===")

voti["matematica"] = 30  # modifica valore esistente
voti["biologia"] = 27    # aggiunge nuova coppia
print(f"Voti dopo modifica: {voti}")

# .update() con un altro dizionario
nuovi_voti: dict[str, int] = {"inglese": 29, "matematica": 30}
voti.update(nuovi_voti)
assert voti["inglese"] == 29
print(f"Voti dopo .update(): {voti}")

# ============================================================
# 4. ITERAZIONE: .keys(), .values(), .items()
# ============================================================
print("\n=== Iterazione ===")

print("Chiavi (materie):")
materie: list[str] = list(voti.keys())
for materia in voti.keys():
    print(f"  - {materia}")

print("Valori (voti):")
lista_voti: list[int] = list(voti.values())
for voto in voti.values():
    print(f"  - {voto}")

print("Coppie (materia, voto):")
for materia, voto in voti.items():
    print(f"  {materia}: {voto}")

# ============================================================
# 5. DICT COMPREHENSION
# ============================================================
print("\n=== Dict comprehension ===")

# Quadrati dei numeri da 1 a 5
quadrati: dict[int, int] = {n: n**2 for n in range(1, 6)}
assert quadrati == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(f"Quadrati: {quadrati}")

# Filtrare voti >= 28
voti_alti: dict[str, int] = {m: v for m, v in voti.items() if v >= 28}
print(f"Voti alti (>=28): {voti_alti}")

# Invertire chiavi e valori
originale: dict[str, int] = {"a": 1, "b": 2, "c": 3}
invertito: dict[int, str] = {v: k for k, v in originale.items()}
assert invertito == {1: "a", 2: "b", 3: "c"}
print(f"Invertito: {invertito}")

# ============================================================
# 6. ESEMPIO: REGISTRO STUDENTI
# ============================================================
print("\n=== Registro studenti ===")

registro: dict[int, dict[str, str | list[int]]] = {
    12345: {"nome": "Marco Rossi", "voti": [28, 30, 25]},
    12346: {"nome": "Laura Bianchi", "voti": [30, 30, 29]},
    12347: {"nome": "Giulia Verdi", "voti": [24, 26, 22]},
}

for matricola, dati in registro.items():
    nome_studente: str = dati["nome"]
    voti_studente: list[int] = dati["voti"]
    media: float = sum(voti_studente) / len(voti_studente)
    print(f"  {matricola} - {nome_studente}: media = {media:.1f}")

# ============================================================
# 7. ESEMPIO: CONTATORE DI PAROLE
# ============================================================
print("\n=== Contatore di parole ===")

testo: str = "il gatto e il cane e il topo e il gatto"
parole: list[str] = testo.split()

# Metodo 1: manuale
conteggio_manuale: dict[str, int] = {}
for parola in parole:
    conteggio_manuale[parola] = conteggio_manuale.get(parola, 0) + 1

assert conteggio_manuale["il"] == 4
assert conteggio_manuale["gatto"] == 2
assert conteggio_manuale["e"] == 3
print(f"Conteggio manuale: {conteggio_manuale}")

# Metodo 2: con .setdefault()
conteggio_setdefault: dict[str, int] = {}
for parola in parole:
    conteggio_setdefault.setdefault(parola, 0)
    conteggio_setdefault[parola] += 1

assert conteggio_setdefault == conteggio_manuale
print(f"Conteggio setdefault: {conteggio_setdefault}")

# ============================================================
# 8. SET — CREAZIONE E OPERAZIONI BASE
# ============================================================
print("\n=== Set ===")

# Creazione
numeri_pari: set[int] = {2, 4, 6, 8, 10}
numeri_dispari: set[int] = {1, 3, 5, 7, 9}
primi: set[int] = {2, 3, 5, 7}
print(f"Pari: {sorted(numeri_pari)}")
print(f"Dispari: {sorted(numeri_dispari)}")
print(f"Primi: {sorted(primi)}")

# Da lista (rimuove duplicati)
lista_con_duplicati: list[int] = [1, 2, 2, 3, 3, 3, 4]
unici: set[int] = set(lista_con_duplicati)
assert len(unici) == 4
print(f"Unici da lista: {sorted(unici)}")

# Set vuoto — ATTENZIONE: {} crea un dict, non un set!
set_vuoto: set[int] = set()
assert isinstance(set_vuoto, set)

# ============================================================
# 9. SET — add, remove, discard
# ============================================================
print("\n=== Set: add, remove, discard ===")

frutta: set[str] = {"mela", "pera", "banana"}
frutta.add("arancia")
assert "arancia" in frutta
print(f"Dopo add('arancia'): {sorted(frutta)}")

frutta.remove("pera")  # KeyError se non esiste
assert "pera" not in frutta
print(f"Dopo remove('pera'): {sorted(frutta)}")

frutta.discard("kiwi")  # Nessun errore se non esiste
print(f"Dopo discard('kiwi'): {sorted(frutta)}")

# ============================================================
# 10. SET — OPERAZIONI INSIEMISTICHE
# ============================================================
print("\n=== Operazioni insiemistiche ===")

A: set[int] = {1, 2, 3, 4, 5}
B: set[int] = {4, 5, 6, 7, 8}

# Unione
unione: set[int] = A | B  # oppure A.union(B)
assert unione == {1, 2, 3, 4, 5, 6, 7, 8}
print(f"A | B (unione): {sorted(unione)}")

# Intersezione
intersezione: set[int] = A & B  # oppure A.intersection(B)
assert intersezione == {4, 5}
print(f"A & B (intersezione): {sorted(intersezione)}")

# Differenza
differenza: set[int] = A - B  # oppure A.difference(B)
assert differenza == {1, 2, 3}
print(f"A - B (differenza): {sorted(differenza)}")

# Differenza simmetrica
diff_simm: set[int] = A ^ B  # oppure A.symmetric_difference(B)
assert diff_simm == {1, 2, 3, 6, 7, 8}
print(f"A ^ B (diff. simmetrica): {sorted(diff_simm)}")

# Sottinsieme e sovrainsieme
C: set[int] = {1, 2, 3}
assert C.issubset(A)
assert A.issuperset(C)
print(f"{sorted(C)} è sottinsieme di {sorted(A)}: {C.issubset(A)}")

# ============================================================
# 11. FROZENSET
# ============================================================
print("\n=== Frozenset ===")

# frozenset è un set immutabile — può essere usato come chiave di dict
immutabile: frozenset[int] = frozenset([1, 2, 3])
print(f"Frozenset: {immutabile}")

# Può essere usato come chiave di un dizionario
gruppi: dict[frozenset[str], str] = {
    frozenset(["Marco", "Laura"]): "Gruppo A",
    frozenset(["Giulia", "Paolo"]): "Gruppo B",
}
chiave: frozenset[str] = frozenset(["Laura", "Marco"])  # ordine non conta
assert gruppi[chiave] == "Gruppo A"
print(f"Gruppo per Marco e Laura: {gruppi[chiave]}")

# ============================================================
# 12. MUTABILITÀ vs IMMUTABILITÀ
# ============================================================
print("\n=== Mutabilità vs Immutabilità ===")

# Tipi immutabili: int, float, str, tuple, frozenset
# Tipi mutabili: list, dict, set

# Le stringhe sono immutabili
s: str = "ciao"
s2: str = s.upper()  # crea una NUOVA stringa
assert s == "ciao"    # l'originale non cambia
assert s2 == "CIAO"
print(f"Stringa originale: {s}, nuova: {s2}")

# Le liste sono mutabili
lista_a: list[int] = [1, 2, 3]
lista_a.append(4)  # modifica IN PLACE
assert lista_a == [1, 2, 3, 4]
print(f"Lista dopo append: {lista_a}")

# ============================================================
# 13. ALIASING vs COPYING
# ============================================================
print("\n=== Aliasing vs Copying ===")

# Aliasing — due nomi per lo stesso oggetto
originale_lista: list[int] = [1, 2, 3]
alias: list[int] = originale_lista  # NON è una copia!
alias.append(4)
assert originale_lista == [1, 2, 3, 4]  # anche l'originale è cambiato!
print(f"Originale dopo modifica alias: {originale_lista}")

# Copia superficiale (shallow copy)
lista_x: list[int] = [1, 2, 3]
copia_x: list[int] = lista_x.copy()  # oppure list(lista_x) o lista_x[:]
copia_x.append(4)
assert lista_x == [1, 2, 3]  # l'originale NON cambia
assert copia_x == [1, 2, 3, 4]
print(f"Originale dopo modifica copia: {lista_x}")
print(f"Copia: {copia_x}")

# Copia di dizionari
dict_orig: dict[str, int] = {"a": 1, "b": 2}
dict_copia: dict[str, int] = dict_orig.copy()
dict_copia["c"] = 3
assert "c" not in dict_orig
print(f"Dict originale: {dict_orig}")
print(f"Dict copia: {dict_copia}")

# Attenzione: shallow copy con oggetti mutabili annidati
import copy

lista_nested: list[list[int]] = [[1, 2], [3, 4]]
shallow: list[list[int]] = lista_nested.copy()
deep: list[list[int]] = copy.deepcopy(lista_nested)

shallow[0].append(99)
assert lista_nested[0] == [1, 2, 99]  # shallow copy condivide gli oggetti interni!
assert deep[0] == [1, 2]              # deep copy è completamente indipendente
print(f"Originale dopo modifica shallow: {lista_nested}")
print(f"Deep copy (indipendente): {deep}")

print("\n=== Fine esempi T12 ===")
