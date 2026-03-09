# Lezione Frontale 12 — Dizionari, set e mutabilità

## Introduzione

Finora abbiamo lavorato con sequenze: liste e tuple, strutture che contengono elementi disposti in un ordine preciso e accessibili tramite un indice numerico. Ma molti problemi reali non si modellano bene con un indice intero. Pensate a un anagrafe: volete cercare una persona per codice fiscale, non per "posizione 347 nella lista". Oppure a un sondaggio: volete sapere quante volte ogni risposta è stata data, non scorrere tutte le risposte una per una.

Python offre due strutture dati fondamentali per questi scenari: i **dizionari** (`dict`), che associano chiavi a valori, e i **set** (`set`), che rappresentano insiemi di elementi unici. Entrambi condividono un meccanismo interno — la *hash table* — che garantisce operazioni estremamente veloci.

In questa lezione vedremo anche un tema trasversale che riguarda tutte le strutture dati: la distinzione tra oggetti **mutabili** e **immutabili**, una distinzione che ha conseguenze concrete su come scrivete il codice e su quali errori potete incontrare.

---

## Dizionari

### Cos'è un dizionario

Un dizionario è una collezione di **coppie chiave-valore**. Ogni chiave è associata a esattamente un valore; data la chiave, il dizionario restituisce il valore corrispondente in tempo (quasi) costante.

```python
# Dizionario con type hints
studente: dict[str, str] = {
    "nome": "Anna",
    "cognome": "Rossi",
    "matricola": "SM00123",
    "corso": "Scienze Statistiche"
}

print(studente["nome"])       # Anna
print(studente["matricola"])  # SM00123
```

La sintassi è `{chiave: valore, chiave: valore, ...}`. Le chiavi sono stringhe (ma possono essere qualsiasi tipo immutabile — vedremo tra poco perché), e i valori possono essere di qualsiasi tipo.

### Creare dizionari

Ci sono diversi modi per creare un dizionario:

```python
# Letterale (il più comune)
voti: dict[str, int] = {"analisi": 28, "informatica": 30, "statistica": 27}

# Dizionario vuoto
rubrica: dict[str, str] = {}

# Con la funzione dict() e argomenti con nome
configurazione: dict[str, int] = dict(larghezza=800, altezza=600, dpi=150)

# Da una lista di tuple (chiave, valore)
coppie: list[tuple[str, int]] = [("a", 1), ("b", 2), ("c", 3)]
da_coppie: dict[str, int] = dict(coppie)
```

### Accesso, modifica, aggiunta e rimozione

```python
voti: dict[str, int] = {"analisi": 28, "informatica": 30}

# Accesso
print(voti["analisi"])  # 28

# Modifica di un valore esistente
voti["analisi"] = 29

# Aggiunta di una nuova coppia
voti["statistica"] = 27

# Rimozione
del voti["informatica"]

print(voti)  # {"analisi": 29, "statistica": 27}
```

Attenzione: accedere a una chiave che non esiste solleva un `KeyError`:

```python
print(voti["algebra"])  # KeyError: 'algebra'
```

Per evitare l'errore, potete verificare prima l'esistenza della chiave:

```python
if "algebra" in voti:
    print(voti["algebra"])
else:
    print("Esame non trovato")
```

### Perché O(1)? Hash table sotto il cofano

L'accesso a un elemento di una lista per indice è O(1) — basta un'operazione. Ma cercare un valore in una lista (ad esempio con `in`) richiede di scorrerla tutta: O(n). Con un dizionario, anche la **ricerca per chiave** è O(1). Come è possibile?

Il segreto è la **hash table** (tabella hash). Quando inserite una coppia `chiave: valore`, Python calcola un numero intero dalla chiave tramite una funzione detta *hash*. Questo numero determina direttamente la posizione in memoria dove viene salvato il valore. Quando cercate la chiave, Python ricalcola l'hash e va direttamente alla posizione giusta, senza scorrere nulla.

```python
# Potete vedere l'hash di un oggetto con la funzione built-in hash()
print(hash("analisi"))    # Un intero (es. 2837465918273...)
print(hash(42))           # 42
print(hash((1, 2, 3)))    # Un intero calcolato dalla tupla
```

Questo meccanismo ha una conseguenza fondamentale: le **chiavi devono essere immutabili** (hashable). Se una chiave potesse cambiare dopo l'inserimento, il suo hash cambierebbe e il dizionario non saprebbe più dove trovare il valore. Per questo le stringhe, i numeri e le tuple funzionano come chiavi, ma le liste e i set no:

```python
# OK: chiavi immutabili
d: dict[str, int] = {"ciao": 1}
d2: dict[int, str] = {42: "risposta"}
d3: dict[tuple[int, int], str] = {(0, 0): "origine"}

# ERRORE: le liste non sono hashable
# d4: dict[list[int], str] = {[1, 2]: "errore"}  # TypeError: unhashable type: 'list'
```

### Dizionari ordinati per inserimento

Da Python 3.7 in poi, i dizionari mantengono l'**ordine di inserimento**. Se aggiungete prima "analisi" e poi "statistica", iterando sul dizionario li otterrete in quell'ordine. Nelle versioni precedenti di Python l'ordine non era garantito — un dettaglio storico che potreste trovare in materiale più datato.

```python
ordine: dict[str, int] = {}
ordine["terzo"] = 3
ordine["primo"] = 1
ordine["secondo"] = 2

for chiave in ordine:
    print(chiave)
# Output: terzo, primo, secondo (ordine di inserimento, NON alfabetico)
```

---

## Metodi principali dei dizionari

### `get()`: accesso con valore di default

Il metodo `get()` è l'alternativa sicura all'accesso con parentesi quadre. Se la chiave non esiste, invece di sollevare un `KeyError`, restituisce un valore di default (per default `None`):

```python
voti: dict[str, int] = {"analisi": 28, "statistica": 27}

# Con le parentesi quadre: errore se la chiave manca
# print(voti["algebra"])  # KeyError!

# Con get(): restituisce None se la chiave manca
risultato: int | None = voti.get("algebra")
print(risultato)  # None

# Con get() e un default esplicito
risultato_default: int = voti.get("algebra", 0)
print(risultato_default)  # 0
```

Questo metodo è particolarmente utile nei conteggi e negli accumuli:

```python
conteggi: dict[str, int] = {}
parole: list[str] = ["casa", "albero", "casa", "gatto", "albero", "casa"]

for parola in parole:
    conteggi[parola] = conteggi.get(parola, 0) + 1

print(conteggi)  # {"casa": 3, "albero": 2, "gatto": 1}
```

### `keys()`, `values()`, `items()`

Questi tre metodi restituiscono **viste** (view) sul dizionario: oggetti che riflettono dinamicamente il contenuto del dizionario.

```python
esame: dict[str, int | str] = {"nome": "Statistica", "cfu": 9, "anno": 1}

# Le chiavi
print(list(esame.keys()))    # ["nome", "cfu", "anno"]

# I valori
print(list(esame.values()))  # ["Statistica", 9, 1]

# Le coppie (chiave, valore) come tuple
print(list(esame.items()))   # [("nome", "Statistica"), ("cfu", 9), ("anno", 1)]
```

Il modo più pythonic per iterare su un dizionario è con `items()`:

```python
voti: dict[str, int] = {"analisi": 28, "statistica": 27, "informatica": 30}

for esame, voto in voti.items():
    if voto >= 28:
        print(f"{esame}: ottimo ({voto})")
```

### `update()`: unire dizionari

Il metodo `update()` aggiunge (o sovrascrive) coppie chiave-valore da un altro dizionario:

```python
base: dict[str, int] = {"analisi": 28, "statistica": 27}
nuovi: dict[str, int] = {"informatica": 30, "analisi": 29}  # analisi viene aggiornato

base.update(nuovi)
print(base)  # {"analisi": 29, "statistica": 27, "informatica": 30}
```

Da Python 3.9+ esiste anche l'operatore `|` per unire dizionari:

```python
unione: dict[str, int] = base | nuovi  # nuovo dizionario, senza modificare base
```

### `pop()`: rimuovere e restituire

Il metodo `pop()` rimuove una chiave e restituisce il valore corrispondente. Come `get()`, accetta un default per evitare errori:

```python
voti: dict[str, int] = {"analisi": 28, "statistica": 27, "informatica": 30}

rimosso: int = voti.pop("informatica")
print(rimosso)  # 30
print(voti)     # {"analisi": 28, "statistica": 27}

# Con default, se la chiave non esiste
assente: int = voti.pop("algebra", -1)
print(assente)  # -1
```

---

## `defaultdict` e `Counter` dal modulo `collections`

La libreria standard di Python include il modulo `collections`, che offre varianti specializzate dei contenitori built-in. Due sono particolarmente utili.

### `defaultdict`: dizionario con valore di default automatico

Abbiamo visto il pattern `conteggi.get(parola, 0) + 1` per contare occorrenze. Con `defaultdict`, il codice diventa più pulito: se accedete a una chiave che non esiste, il dizionario la crea automaticamente con un valore di default.

```python
from collections import defaultdict

# Il tipo passato come argomento determina il default
# int() -> 0, list() -> [], str() -> ""
conteggi: defaultdict[str, int] = defaultdict(int)

parole: list[str] = ["casa", "albero", "casa", "gatto", "albero", "casa"]
for parola in parole:
    conteggi[parola] += 1  # Se la chiave non esiste, parte da 0

print(dict(conteggi))  # {"casa": 3, "albero": 2, "gatto": 1}
```

Un altro uso comune è raggruppare elementi:

```python
from collections import defaultdict

studenti: list[tuple[str, str]] = [
    ("Rossi", "Statistica"),
    ("Bianchi", "Analisi"),
    ("Verdi", "Statistica"),
    ("Neri", "Analisi"),
    ("Gialli", "Informatica"),
]

per_corso: defaultdict[str, list[str]] = defaultdict(list)
for cognome, corso in studenti:
    per_corso[corso].append(cognome)

print(dict(per_corso))
# {"Statistica": ["Rossi", "Verdi"], "Analisi": ["Bianchi", "Neri"], "Informatica": ["Gialli"]}
```

### `Counter`: contare occorrenze

`Counter` è una sottoclasse di `dict` specializzata nel conteggio. Fa automaticamente quello che abbiamo fatto a mano con `get()` o `defaultdict`:

```python
from collections import Counter

parole: list[str] = ["casa", "albero", "casa", "gatto", "albero", "casa"]
conteggio: Counter[str] = Counter(parole)

print(conteggio)              # Counter({"casa": 3, "albero": 2, "gatto": 1})
print(conteggio["casa"])      # 3
print(conteggio["drago"])     # 0 (non solleva errore!)
print(conteggio.most_common(2))  # [("casa", 3), ("albero", 2)]
```

Un esempio statistico: contare le frequenze di un campione.

```python
from collections import Counter

risposte: list[str] = [
    "molto", "poco", "abbastanza", "molto", "molto",
    "poco", "abbastanza", "molto", "per_niente", "poco"
]
frequenze: Counter[str] = Counter(risposte)

totale: int = sum(frequenze.values())
for risposta, conteggio in frequenze.most_common():
    percentuale: float = conteggio / totale * 100
    print(f"{risposta:>12}: {conteggio:>2} ({percentuale:.1f}%)")
```

Output:

```
       molto:  4 (40.0%)
        poco:  3 (30.0%)
  abbastanza:  2 (20.0%)
  per_niente:  1 (10.0%)
```

---

## Set

### Cos'è un set

Un `set` è una collezione **non ordinata** di elementi **unici**. Se i dizionari sono come un'anagrafe (cerchi per chiave, ottieni un valore), i set sono come un registro di presenze: ti interessa solo sapere se un elemento c'è o non c'è.

```python
# Creare un set
numeri: set[int] = {1, 2, 3, 4, 5}
print(numeri)  # {1, 2, 3, 4, 5} (l'ordine può variare)

# I duplicati vengono eliminati automaticamente
con_duplicati: set[int] = {1, 2, 2, 3, 3, 3}
print(con_duplicati)  # {1, 2, 3}

# Set vuoto: ATTENZIONE, {} crea un dizionario vuoto!
vuoto: set[int] = set()  # Corretto
# vuoto2 = {}  # Questo è un dict, non un set!

# Creare un set da una lista (utile per rimuovere duplicati)
lista: list[str] = ["roma", "milano", "roma", "napoli", "milano"]
citta_uniche: set[str] = set(lista)
print(citta_uniche)  # {"roma", "milano", "napoli"}
```

Come i dizionari, i set usano internamente una hash table. Questo significa che il test di appartenenza (`in`) è O(1), non O(n) come nelle liste:

```python
grandi_numeri: set[int] = set(range(1_000_000))

# Questo è O(1) — praticamente istantaneo
print(999_999 in grandi_numeri)  # True

# Con una lista, sarebbe O(n) — molto più lento
# grandi_lista: list[int] = list(range(1_000_000))
# print(999_999 in grandi_lista)  # True, ma lento!
```

### Operazioni sugli insiemi

I set supportano le classiche operazioni insiemistiche della matematica. Se avete studiato insiemi a scuola, la notazione vi sarà familiare:

```python
a: set[int] = {1, 2, 3, 4, 5}
b: set[int] = {4, 5, 6, 7, 8}

# Unione: elementi presenti in A o in B (o in entrambi)
print(a | b)   # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersezione: elementi presenti in A e in B
print(a & b)   # {4, 5}

# Differenza: elementi in A ma non in B
print(a - b)   # {1, 2, 3}

# Differenza simmetrica: elementi in A o in B, ma non in entrambi
print(a ^ b)   # {1, 2, 3, 6, 7, 8}

# Sottoinsieme: A è contenuto in B?
piccolo: set[int] = {4, 5}
print(piccolo <= b)   # True (piccolo è sottoinsieme di b)
print(piccolo <= a)   # True (piccolo è sottoinsieme anche di a)
print(a <= b)          # False
```

Ogni operatore ha anche una versione con nome di metodo (`union()`, `intersection()`, `difference()`, `symmetric_difference()`, `issubset()`), ma gli operatori sono più concisi e leggibili.

### Un esempio: confrontare risposte a un sondaggio

```python
domanda_1: set[str] = {"Rossi", "Bianchi", "Verdi", "Neri", "Gialli"}
domanda_2: set[str] = {"Bianchi", "Neri", "Viola", "Rosa"}

# Chi ha risposto a entrambe?
entrambe: set[str] = domanda_1 & domanda_2
print(f"Hanno risposto a entrambe: {entrambe}")  # {"Bianchi", "Neri"}

# Chi ha risposto solo alla prima?
solo_prima: set[str] = domanda_1 - domanda_2
print(f"Solo alla prima: {solo_prima}")  # {"Rossi", "Verdi", "Gialli"}

# Chi ha risposto ad almeno una?
almeno_una: set[str] = domanda_1 | domanda_2
print(f"Almeno una: {almeno_una}")
```

### Aggiungere e rimuovere elementi

```python
colori: set[str] = {"rosso", "verde", "blu"}

colori.add("giallo")       # Aggiunge un elemento
colori.discard("verde")    # Rimuove un elemento (nessun errore se assente)
colori.remove("rosso")     # Rimuove un elemento (KeyError se assente)

print(colori)  # {"blu", "giallo"}
```

---

## `frozenset`: il set immutabile

Come esiste la tupla (immutabile) accanto alla lista (mutabile), esiste il `frozenset` accanto al `set`. Un `frozenset` supporta tutte le operazioni insiemistiche ma non può essere modificato dopo la creazione.

```python
fisso: frozenset[int] = frozenset([1, 2, 3, 4])

print(3 in fisso)    # True
print(fisso | {5})   # frozenset({1, 2, 3, 4, 5}) — crea un nuovo frozenset

# fisso.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'
```

Il vantaggio pratico: essendo immutabile, un `frozenset` è **hashable**. Potete usarlo come chiave di un dizionario o come elemento di un altro set:

```python
# Un set di set non è possibile
# errore: set[set[int]] = {{1, 2}, {3, 4}}  # TypeError: unhashable type: 'set'

# Ma un set di frozenset sì
insiemi: set[frozenset[int]] = {frozenset([1, 2]), frozenset([3, 4])}
print(insiemi)
```

---

## Mutabilità vs immutabilità

### Il concetto

Alcuni oggetti in Python possono essere modificati dopo la creazione: sono **mutabili**. Altri, una volta creati, non possono cambiare: sono **immutabili**.

| Tipo          | Mutabile? |
|---------------|-----------|
| `int`         | No        |
| `float`       | No        |
| `str`         | No        |
| `bool`        | No        |
| `tuple`       | No        |
| `frozenset`   | No        |
| `list`        | Si        |
| `dict`        | Si        |
| `set`         | Si        |

### Cosa significa in pratica

Con i tipi immutabili, ogni "modifica" crea in realtà un **nuovo oggetto**:

```python
a: str = "ciao"
b: str = a        # b punta allo stesso oggetto di a
a = a + " mondo"  # a ora punta a un NUOVO oggetto "ciao mondo"
print(b)          # "ciao" — b non è cambiato
```

Con i tipi mutabili, la modifica avviene **in place** — sullo stesso oggetto:

```python
lista_a: list[int] = [1, 2, 3]
lista_b: list[int] = lista_a   # lista_b punta allo STESSO oggetto
lista_a.append(4)               # Modifica l'oggetto
print(lista_b)                  # [1, 2, 3, 4] — anche lista_b è cambiato!
```

Questo è un punto cruciale e una fonte di errori molto comuni. Quando assegnate una lista a un'altra variabile, non state creando una copia: state creando un **alias**, un secondo nome per lo stesso oggetto. Potete verificarlo con `id()`, che restituisce l'identificativo univoco dell'oggetto in memoria:

```python
lista_a: list[int] = [1, 2, 3]
lista_b: list[int] = lista_a
print(id(lista_a) == id(lista_b))  # True — stesso oggetto!

# Per creare una vera copia
lista_c: list[int] = lista_a.copy()       # Copia superficiale
lista_d: list[int] = list(lista_a)        # Altra sintassi per la copia
lista_e: list[int] = lista_a[:]           # Ancora un altro modo
print(id(lista_a) == id(lista_c))  # False — oggetti diversi
```

### Side effect nelle funzioni

La mutabilità ha conseguenze importanti quando passate oggetti a una funzione. In Python, gli argomenti sono passati **per riferimento all'oggetto**: la funzione riceve un riferimento allo stesso oggetto, non una copia.

Con oggetti immutabili, questo non è un problema:

```python
def aggiungi_dieci(n: int) -> int:
    n = n + 10  # Crea un nuovo intero, non modifica l'originale
    return n

valore: int = 5
risultato: int = aggiungi_dieci(valore)
print(valore)     # 5 — non è cambiato
print(risultato)  # 15
```

Con oggetti mutabili, la funzione può modificare l'oggetto originale, causando un **side effect** (effetto collaterale):

```python
def aggiungi_elemento(lista: list[int], elemento: int) -> None:
    lista.append(elemento)  # Modifica la lista originale!

numeri: list[int] = [1, 2, 3]
aggiungi_elemento(numeri, 4)
print(numeri)  # [1, 2, 3, 4] — la lista è stata modificata!
```

Questo può essere intenzionale (e a volte è utile), ma spesso è una fonte di bug. Per evitare side effect indesiderati, lavorate su una copia:

```python
def ordina_senza_modificare(lista: list[int]) -> list[int]:
    copia: list[int] = lista.copy()
    copia.sort()
    return copia

originale: list[int] = [3, 1, 4, 1, 5]
ordinata: list[int] = ordina_senza_modificare(originale)
print(originale)  # [3, 1, 4, 1, 5] — intatta
print(ordinata)   # [1, 1, 3, 4, 5]
```

### Chiavi di dizionario e mutabilità

Ora potete capire perché le chiavi dei dizionari devono essere immutabili. Se una chiave fosse una lista e la modificaste dopo averla usata come chiave, il suo hash cambierebbe. Il dizionario avrebbe salvato il valore in una posizione basata sull'hash originale, ma non lo troverebbe più perché l'hash è cambiato. Python previene questo problema alla radice: gli oggetti mutabili non hanno un metodo `__hash__` e non possono essere usati come chiavi.

```python
# Questo principio si applica anche ai set
# (un set è essenzialmente un dizionario senza valori)
valido: set[tuple[int, int]] = {(1, 2), (3, 4)}     # OK: tuple immutabili
# invalido: set[list[int]] = {[1, 2], [3, 4]}        # TypeError
```

---

## Scegliere la struttura dati giusta

Con quattro strutture dati a disposizione, come scegliere? Ecco una guida pratica:

| Serve...                                   | Struttura | Esempio                              |
|--------------------------------------------|-----------|--------------------------------------|
| Una sequenza ordinata e modificabile       | `list`    | Voti da aggiornare                   |
| Una sequenza ordinata e fissa              | `tuple`   | Coordinate (x, y)                    |
| Un'associazione chiave-valore              | `dict`    | Studente per matricola               |
| Un insieme di elementi unici              | `set`     | Codici fiscali presenti              |

Alcune regole pratiche:

- **Dovete cercare per chiave?** Usate un `dict`.
- **Vi interessano solo presenze/unicità?** Usate un `set`.
- **L'ordine conta e dovete modificare?** Usate una `list`.
- **L'ordine conta ma i dati sono fissi?** Usate una `tuple`.
- **Dovete contare occorrenze?** Usate `Counter`.
- **Dovete raggruppare per categoria?** Usate `defaultdict(list)`.

Un esempio che combina tutto:

```python
from collections import Counter

# Dati: lista di voti per un esame (con possibili ripetizioni di studenti)
registrazioni: list[tuple[str, int]] = [
    ("Rossi", 28), ("Bianchi", 25), ("Rossi", 30),  # Rossi ha rifatto l'esame
    ("Verdi", 22), ("Bianchi", 27), ("Neri", 30),
]

# Teniamo solo l'ultimo voto per ogni studente (dict: chiave -> ultimo valore)
ultimi_voti: dict[str, int] = {}
for studente, voto in registrazioni:
    ultimi_voti[studente] = voto

print(ultimi_voti)  # {"Rossi": 30, "Bianchi": 27, "Verdi": 22, "Neri": 30}

# Chi ha preso 30? (set: ci interessa solo l'unicità)
trenta: set[str] = {s for s, v in ultimi_voti.items() if v == 30}
print(trenta)  # {"Rossi", "Neri"}

# Distribuzione dei voti (Counter)
distribuzione: Counter[int] = Counter(ultimi_voti.values())
print(distribuzione)  # Counter({30: 2, 27: 1, 22: 1})
```

---

## Cenni sulla complessità: O(1) vs O(n)

### L'idea di Big O

Quando diciamo che un'operazione è **O(1)** (si legge "O di uno" o "ordine costante"), intendiamo che il tempo necessario non dipende dalla dimensione dei dati. Che il dizionario contenga 10 o 10 milioni di elementi, cercare una chiave richiede (circa) lo stesso tempo.

Quando diciamo che un'operazione è **O(n)** (si legge "O di enne" o "ordine lineare"), intendiamo che il tempo cresce proporzionalmente al numero di elementi. Cercare un valore in una lista di 10 elementi richiede al massimo 10 confronti; in una lista di 10 milioni, al massimo 10 milioni di confronti.

La notazione Big O è un modo per descrivere **come scala** un algoritmo, ignorando i dettagli (costanti, termini minori). Non dice quanto tempo esatto ci vuole, ma come il tempo cresce al crescere dell'input.

### Tabella riassuntiva

| Operazione                    | `list`       | `dict`/`set` |
|-------------------------------|-------------|-------------|
| Accesso per indice            | O(1)        | —           |
| Accesso per chiave            | —           | O(1)        |
| Ricerca (`in`)                | O(n)        | O(1)        |
| Aggiunta in fondo             | O(1)*       | O(1)        |
| Inserimento in mezzo          | O(n)        | —           |
| Rimozione per valore          | O(n)        | O(1)        |

(*O(1) ammortizzato — quasi sempre costante, occasionalmente richiede un riallocamento.)

### Un esempio concreto

Supponiamo di avere un elenco di 100.000 codici fiscali e di dover verificare se un dato codice è presente. La scelta della struttura dati fa una differenza enorme:

```python
import time

# Preparazione dei dati
codici_lista: list[str] = [f"CF{i:06d}" for i in range(100_000)]
codici_set: set[str] = set(codici_lista)

# Ricerca in una lista: O(n)
inizio: float = time.time()
for _ in range(1000):
    _ = "CF099999" in codici_lista
tempo_lista: float = time.time() - inizio

# Ricerca in un set: O(1)
inizio = time.time()
for _ in range(1000):
    _ = "CF099999" in codici_set
tempo_set: float = time.time() - inizio

print(f"Lista: {tempo_lista:.4f}s")  # Es. 1.2345s
print(f"Set:   {tempo_set:.4f}s")    # Es. 0.0002s
```

La differenza è di diversi ordini di grandezza. Questo è il motivo per cui scegliere la struttura dati giusta non è un dettaglio: è una decisione progettuale fondamentale.

### Quando O(n) va bene

Non serve sempre O(1). Se la vostra lista ha 20 elementi, la differenza tra O(1) e O(n) è trascurabile. Big O diventa importante quando i dati crescono: centinaia, migliaia, milioni di elementi. Come regola pratica: se dovete fare ricerche ripetute su una collezione che cresce, preferite `dict` o `set`.

---

## Domande di verifica

1. **Qual è la differenza fondamentale tra una lista e un dizionario?** In quali situazioni preferireste un dizionario?

2. **Perché le chiavi di un dizionario devono essere immutabili?** Cosa succede se provate a usare una lista come chiave?

3. **Qual è la differenza tra `voti["algebra"]` e `voti.get("algebra")`?** Quando conviene usare `get()`?

4. **Spiegate la differenza tra `set` e `frozenset`.** In quale situazione è indispensabile usare un `frozenset`?

5. **Cosa stampa il seguente codice e perché?**
   ```python
   a: list[int] = [1, 2, 3]
   b: list[int] = a
   b.append(4)
   print(a)
   ```

6. **Cosa si intende per "side effect" di una funzione?** Fate un esempio con una lista passata come argomento.

7. **Qual è la complessità dell'operatore `in` per una lista? E per un set?** Perché sono diverse?

8. **Date due set A e B, che differenza c'è tra `A - B` e `A ^ B`?**

---

## Esercizi

### Base

1. Create un dizionario che rappresenta un'anagrafe semplificata: ogni chiave è un codice fiscale (stringa) e ogni valore è un dizionario con "nome", "cognome" e "eta". Inserite almeno tre persone, poi stampate nome e cognome di ciascuna iterando con `items()`.

2. Data la lista `["mela", "banana", "mela", "arancia", "banana", "mela", "kiwi"]`, usate un `set` per ottenere i frutti unici e un `Counter` per contare quante volte appare ciascun frutto.

3. Date due liste di studenti iscritti a due corsi diversi, usate i set per trovare: (a) gli studenti iscritti a entrambi i corsi, (b) gli studenti iscritti solo al primo corso, (c) tutti gli studenti (senza duplicati).

### Intermedio

4. Scrivete una funzione `frequenze_relative(dati: list[str]) -> dict[str, float]` che, data una lista di risposte a un sondaggio, restituisca un dizionario con la frequenza relativa di ciascuna risposta (conteggio / totale). Usate `Counter`.

5. Scrivete una funzione `inverti_dizionario(d: dict[str, int]) -> dict[int, list[str]]` che, dato un dizionario, crei un nuovo dizionario dove i valori originali diventano chiavi e le chiavi originali diventano liste di valori. Ad esempio, `{"a": 1, "b": 2, "c": 1}` diventa `{1: ["a", "c"], 2: ["b"]}`. Usate `defaultdict`.

6. Scrivete una funzione `rimuovi_duplicati_mantieni_ordine(lista: list[int]) -> list[int]` che rimuova i duplicati da una lista mantenendo l'ordine della prima occorrenza. (Suggerimento: usate un set come "registro delle presenze".)

### Avanzato

7. Scrivete una funzione `analisi_testo(testo: str) -> dict[str, int | float | list[str]]` che, dato un testo, restituisca un dizionario con: il numero di parole (`"n_parole"`), il numero di parole uniche (`"n_uniche"`), la parola piu frequente (`"piu_frequente"`), le parole che compaiono una sola volta (`"hapax"`). Usate `Counter` e operazioni sui set.

   ```python
   testo: str = "il gatto e il cane e il topo e il gatto"
   risultato: dict[str, int | float | list[str]] = analisi_testo(testo)
   # {"n_parole": 10, "n_uniche": 5, "piu_frequente": "il",
   #  "hapax": ["cane", "topo"]}  (l'ordine degli hapax può variare)
   ```

8. Scrivete una funzione `trova_anagrammi(parole: list[str]) -> list[set[str]]` che, data una lista di parole, raggruppi quelle che sono anagrammi l'una dell'altra. (Suggerimento: due parole sono anagrammi se hanno le stesse lettere con le stesse frequenze. Usate `tuple(sorted(parola))` come chiave di un dizionario.)

   ```python
   parole: list[str] = ["roma", "mora", "amor", "cane", "acne", "sole"]
   print(trova_anagrammi(parole))
   # [{"roma", "mora", "amor"}, {"cane", "acne"}, {"sole"}]
   ```

---

## Osservazioni finali

Dizionari e set completano la vostra cassetta degli attrezzi per le strutture dati. Con liste, tuple, dizionari e set avete tutto il necessario per rappresentare la maggior parte dei dati che incontrerete in statistica e nella programmazione quotidiana.

Il tema della mutabilità non riguarda solo i dizionari: attraversa tutta la programmazione Python. Il fatto che `b = a` su una lista crei un alias e non una copia e un dettaglio che puo causare bug sottili e difficili da trovare. La regola pratica: quando passate un oggetto mutabile a una funzione e non volete che venga modificato, passate una copia.

La notazione Big O, per quanto introdotta qui in modo informale, e uno strumento concettuale potente. Non serve conoscere la matematica formale dietro alla complessita: basta ricordare che O(1) significa "tempo costante, indipendente dalla dimensione" e O(n) significa "tempo proporzionale alla dimensione". Questa intuizione vi guidera nella scelta della struttura dati giusta e, piu avanti, nella scrittura di codice efficiente.

Nella prossima lezione vedremo le **funzioni in profondita**: scope delle variabili, funzioni come oggetti e le funzioni `lambda`.
