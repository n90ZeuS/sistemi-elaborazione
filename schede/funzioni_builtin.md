# Funzioni Built-in di Python

Scheda di riferimento rapido con le funzioni predefinite piu' usate, organizzate per categoria.

---

## Conversione di tipo

| Funzione | Firma | Descrizione | Esempio | Risultato |
|----------|-------|-------------|---------|-----------|
| `int()` | `int(x)` `int(s, base)` | Converte a intero | `int("42")` | `42` |
| `float()` | `float(x)` | Converte a numero decimale | `float("3.14")` | `3.14` |
| `str()` | `str(x)` | Converte a stringa | `str(42)` | `"42"` |
| `bool()` | `bool(x)` | Converte a booleano | `bool(0)` | `False` |
| `list()` | `list(iterabile)` | Converte a lista | `list("abc")` | `["a","b","c"]` |
| `tuple()` | `tuple(iterabile)` | Converte a tupla | `tuple([1,2])` | `(1, 2)` |
| `dict()` | `dict(coppie)` | Crea un dizionario | `dict(a=1, b=2)` | `{"a":1,"b":2}` |
| `set()` | `set(iterabile)` | Converte a set (rimuove duplicati) | `set([1,1,2])` | `{1, 2}` |

### Valori "falsy" in Python (bool restituisce False)

```python
bool(0)       # False     (zero numerico)
bool(0.0)     # False
bool("")      # False     (stringa vuota)
bool([])      # False     (lista vuota)
bool({})      # False     (dict vuoto)
bool(None)    # False
bool(set())   # False

# Tutto il resto e' True
bool(1)       # True
bool(-1)      # True
bool("ciao")  # True
bool([0])     # True  (lista NON vuota, anche se contiene 0)
```

---

## Matematica

| Funzione | Firma | Descrizione | Esempio | Risultato |
|----------|-------|-------------|---------|-----------|
| `abs()` | `abs(x)` | Valore assoluto | `abs(-5)` | `5` |
| `round()` | `round(x[, n])` | Arrotonda a n decimali | `round(3.14159, 2)` | `3.14` |
| `sum()` | `sum(iterabile[, start])` | Somma degli elementi | `sum([1, 2, 3])` | `6` |
| `min()` | `min(iterabile)` `min(a, b, ...)` | Valore minimo | `min(3, 1, 4)` | `1` |
| `max()` | `max(iterabile)` `max(a, b, ...)` | Valore massimo | `max(3, 1, 4)` | `4` |
| `pow()` | `pow(base, exp[, mod])` | Potenza (come `**`) | `pow(2, 10)` | `1024` |
| `divmod()` | `divmod(a, b)` | Quoziente e resto | `divmod(17, 5)` | `(3, 2)` |

### Dettagli su round()

```python
round(2.5)      # 2   (!) Python usa "banker's rounding" (arrotonda al pari)
round(3.5)      # 4
round(2.75, 1)  # 2.8
round(1234, -2) # 1200  (arrotonda alle centinaia)
```

### min() e max() con chiave personalizzata

```python
nomi = ["Luca", "Anna", "Gianfranco"]
min(nomi, key=len)    # "Luca"  (il piu' corto)
max(nomi, key=len)    # "Gianfranco"  (il piu' lungo)

studenti = [("Luca", 28), ("Anna", 30), ("Marco", 25)]
max(studenti, key=lambda s: s[1])   # ("Anna", 30)
```

---

## Iterazione

| Funzione | Firma | Descrizione | Esempio | Risultato |
|----------|-------|-------------|---------|-----------|
| `range()` | `range(stop)` `range(start, stop[, step])` | Genera sequenza di interi | `list(range(5))` | `[0,1,2,3,4]` |
| `enumerate()` | `enumerate(iter[, start])` | Aggiunge indice a ogni elemento | `list(enumerate("ab"))` | `[(0,"a"),(1,"b")]` |
| `zip()` | `zip(iter1, iter2, ...)` | Unisce iterabili in parallelo | `list(zip("ab",[1,2]))` | `[("a",1),("b",2)]` |
| `map()` | `map(func, iterabile)` | Applica funzione a ogni elemento | `list(map(int, ["1","2"]))` | `[1, 2]` |
| `filter()` | `filter(func, iterabile)` | Filtra elementi (func restituisce True) | `list(filter(str.isdigit, ["a","1"]))` | `["1"]` |
| `sorted()` | `sorted(iter[, key, reverse])` | Restituisce lista ordinata (nuova) | `sorted([3,1,2])` | `[1, 2, 3]` |
| `reversed()` | `reversed(sequenza)` | Restituisce iteratore invertito | `list(reversed([1,2,3]))` | `[3, 2, 1]` |

### sorted() in dettaglio

```python
# Ordine crescente (default)
sorted([3, 1, 4, 1, 5])             # [1, 1, 3, 4, 5]

# Ordine decrescente
sorted([3, 1, 4, 1, 5], reverse=True)  # [5, 4, 3, 1, 1]

# Ordina per criterio personalizzato
parole = ["banana", "mela", "ciliegia"]
sorted(parole, key=len)               # ["mela", "banana", "ciliegia"]

# Ordina dizionari per un campo
studenti = [{"nome": "Luca", "voto": 28}, {"nome": "Anna", "voto": 30}]
sorted(studenti, key=lambda s: s["voto"], reverse=True)
# [{"nome": "Anna", "voto": 30}, {"nome": "Luca", "voto": 28}]
```

### map() e filter() -- alternative alle comprehension

```python
# map: applica una funzione a ogni elemento
voti_str = ["28", "30", "25"]
voti_int = list(map(int, voti_str))      # [28, 30, 25]
# Equivalente: [int(v) for v in voti_str]

# filter: mantiene solo gli elementi che soddisfano la condizione
numeri = [1, -2, 3, -4, 5]
positivi = list(filter(lambda x: x > 0, numeri))  # [1, 3, 5]
# Equivalente: [x for x in numeri if x > 0]
```

---

## Input/Output

| Funzione | Firma | Descrizione | Esempio | Tipo restituito |
|----------|-------|-------------|---------|-----------------|
| `print()` | `print(*args, sep=" ", end="\n")` | Stampa a schermo | `print("ciao", "mondo")` | `None` |
| `input()` | `input(prompt)` | Legge stringa da tastiera | `nome = input("Nome: ")` | `str` |
| `open()` | `open(file, mode, encoding)` | Apre un file | `open("dati.csv", "r", encoding="utf-8")` | file object |

### print() -- parametri utili

```python
print("a", "b", "c")                # a b c
print("a", "b", "c", sep=", ")      # a, b, c
print("a", "b", "c", sep="")        # abc
print("caricamento", end="...")      # caricamento... (senza andare a capo)
print("ciao", file=open("out.txt","w"))  # scrive su file

# Stampare una tabella allineata
for nome, voto in [("Luca", 28), ("Anna", 30)]:
    print(f"{nome:<10} {voto:>5}")
# Luca           28
# Anna           30
```

### input() -- ricordare che restituisce sempre str!

```python
eta = input("Quanti anni hai? ")     # eta e' una STRINGA
eta = int(eta)                       # ora e' un intero

# In una riga
eta = int(input("Quanti anni hai? "))
```

---

## Ispezione

| Funzione | Firma | Descrizione | Esempio | Risultato |
|----------|-------|-------------|---------|-----------|
| `type()` | `type(x)` | Restituisce il tipo dell'oggetto | `type(42)` | `<class 'int'>` |
| `isinstance()` | `isinstance(x, tipo)` | Verifica se x e' di quel tipo | `isinstance(42, int)` | `True` |
| `len()` | `len(x)` | Numero di elementi / lunghezza | `len([1,2,3])` | `3` |
| `id()` | `id(x)` | Identita' univoca dell'oggetto | `id(42)` | intero (indirizzo) |
| `dir()` | `dir(x)` | Lista di attributi e metodi | `dir("")` | lista di stringhe |
| `help()` | `help(x)` | Documentazione interattiva | `help(print)` | mostra la doc |

### type() vs isinstance()

```python
# type() controlla il tipo esatto
type(42) == int           # True
type(True) == int         # True (!)  bool e' sottotipo di int

# isinstance() gestisce l'ereditarieta'
isinstance(42, int)       # True
isinstance(True, int)     # True
isinstance(42, (int, float))  # True (controlla piu' tipi)
```

---

## Logica

| Funzione | Firma | Descrizione | Esempio | Risultato |
|----------|-------|-------------|---------|-----------|
| `any()` | `any(iterabile)` | True se almeno un elemento e' vero | `any([False, True, False])` | `True` |
| `all()` | `all(iterabile)` | True se tutti gli elementi sono veri | `all([True, True, False])` | `False` |
| `callable()` | `callable(x)` | Verifica se x e' chiamabile (funzione) | `callable(print)` | `True` |
| `hasattr()` | `hasattr(obj, name)` | Verifica se obj ha l'attributo name | `hasattr("abc", "upper")` | `True` |

### any() e all() -- molto utili in statistica

```python
voti = [28, 30, 15, 25, 22]

# Almeno un insufficiente?
any(v < 18 for v in voti)          # True

# Tutti sufficienti?
all(v >= 18 for v in voti)         # False

# Almeno un 30?
any(v == 30 for v in voti)         # True

# Tutte le risposte compilate?
risposte = ["si", "", "no", "si"]
all(risposte)                      # False ("" e' falsy)
```

---

## Altre funzioni utili

| Funzione | Firma | Descrizione | Esempio | Risultato |
|----------|-------|-------------|---------|-----------|
| `chr()` | `chr(n)` | Numero Unicode -> carattere | `chr(65)` | `"A"` |
| `ord()` | `ord(c)` | Carattere -> numero Unicode | `ord("A")` | `65` |
| `bin()` | `bin(n)` | Intero -> stringa binaria | `bin(10)` | `"0b1010"` |
| `hex()` | `hex(n)` | Intero -> stringa esadecimale | `hex(255)` | `"0xff"` |
| `repr()` | `repr(x)` | Rappresentazione "per programmatori" | `repr("ciao\n")` | `"'ciao\\n'"` |
| `format()` | `format(val, spec)` | Formattazione singolo valore | `format(3.14, ".1f")` | `"3.1"` |
| `hash()` | `hash(x)` | Valore hash (solo per immutabili) | `hash("abc")` | intero |

---

## Riepilogo: le 10 funzioni da sapere assolutamente

```python
print()      # Stampa a schermo
input()      # Legge dall'utente (restituisce str!)
len()        # Lunghezza / numero di elementi
type()       # Che tipo e'?
int()        # Converti a intero
float()      # Converti a decimale
str()        # Converti a stringa
range()      # Genera sequenza di numeri
sorted()     # Ordina (restituisce nuova lista)
enumerate()  # Indice + valore in un ciclo for
```
