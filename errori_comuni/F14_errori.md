# Errori comuni — F14: Funzioni avanzate e moduli

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione F14.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

---

### Errore 1: Tentare di scrivere una lambda su più righe

**Codice errato:**
```python
trasforma = lambda x:
    if x > 0:
        return x * 2
    else:
        return -x
```

**Cosa succede:**
```
SyntaxError: expected an indented block after 'lambda' on line 1
```

**Perché è sbagliato:** Le funzioni lambda in Python sono limitate a una singola espressione. Non possono contenere blocchi `if/else` su più righe, cicli, `return` espliciti o istruzioni multiple. Sono pensate per operazioni semplici e concise.

**Codice corretto:**
```python
# Opzione 1: lambda con espressione condizionale (su una riga)
trasforma = lambda x: x * 2 if x > 0 else -x

# Opzione 2: funzione normale (preferibile per logica complessa)
def trasforma(x):
    if x > 0:
        return x * 2
    else:
        return -x
```

**Regola da ricordare:** Le lambda ammettono una sola espressione: se serve logica complessa, usa una funzione definita con `def`.

---

### Errore 2: `from modulo import *` inquina il namespace

**Codice errato:**
```python
from math import *
from statistics import *

# Entrambi i moduli definiscono funzioni con nomi comuni
# Lo studente non sa più quale funzione sta usando
risultato = log(10)     # è math.log? O un'altra log?
media = mean([1, 2, 3]) # questo funziona, ma da dove viene?
```

**Cosa succede:**
```
Nessun errore immediato, ma rischio di conflitti tra nomi e codice difficile da leggere.
```
Se due moduli definiscono una funzione con lo stesso nome, l'ultimo `import *` sovrascrive il precedente senza avviso.

**Perché è sbagliato:** `from modulo import *` importa tutti i nomi del modulo nel namespace corrente, rendendo impossibile capire da dove proviene ogni funzione. Se due moduli esportano lo stesso nome, il secondo sovrascrive il primo silenziosamente, causando bug difficili da trovare.

**Codice corretto:**
```python
# Opzione 1: importa il modulo e usa il prefisso
import math
import statistics

risultato = math.log(10)
media = statistics.mean([1, 2, 3])

# Opzione 2: importa solo le funzioni che servono
from math import log, sqrt
from statistics import mean, stdev
```

**Regola da ricordare:** Non usare mai `from modulo import *`: importa il modulo intero oppure solo i nomi specifici che ti servono.

---

### Errore 3: Late binding nelle closure (variabile catturata per riferimento)

**Codice errato:**
```python
funzioni = []
for i in range(5):
    funzioni.append(lambda: i)

# Lo studente si aspetta [0, 1, 2, 3, 4]
risultati = [f() for f in funzioni]
print(risultati)
```

**Cosa succede:**
```
[4, 4, 4, 4, 4]
```
Tutte le funzioni restituiscono 4 invece dei valori da 0 a 4.

**Perché è sbagliato:** Le lambda catturano la variabile `i` per riferimento, non per valore. Quando le lambda vengono eseguite (dopo la fine del ciclo), `i` ha il valore finale `4` per tutte. Questo comportamento si chiama *late binding*: il valore di `i` viene letto solo al momento della chiamata.

**Codice corretto:**
```python
funzioni = []
for i in range(5):
    funzioni.append(lambda i=i: i)  # i=i "congela" il valore corrente

risultati = [f() for f in funzioni]
print(risultati)  # [0, 1, 2, 3, 4]
```

**Regola da ricordare:** Quando crei una lambda in un ciclo, usa `lambda x=x:` per catturare il valore corrente della variabile, non il riferimento.

---

### Errore 4: Confondere `map()` con il suo risultato

**Codice errato:**
```python
numeri = [1, 2, 3, 4, 5]
quadrati = map(lambda x: x**2, numeri)

print(quadrati)
print(len(quadrati))
```

**Cosa succede:**
```
<map object at 0x7f8b8c0d5e80>
TypeError: object of type 'map' has no len()
```

**Perché è sbagliato:** `map()` restituisce un oggetto *map* (un iteratore), non una lista. Gli iteratori sono "pigri": calcolano i valori solo quando richiesti. Non si può stampare direttamente il contenuto, calcolarne la lunghezza, o indicizzarli come una lista.

**Codice corretto:**
```python
numeri = [1, 2, 3, 4, 5]
quadrati = list(map(lambda x: x**2, numeri))

print(quadrati)       # [1, 4, 9, 16, 25]
print(len(quadrati))  # 5

# Alternativa più leggibile con list comprehension:
quadrati = [x**2 for x in numeri]
```

**Regola da ricordare:** `map()` restituisce un iteratore, non una lista: avvolgilo con `list()` se ti servono tutti i risultati subito.

---

### Errore 5: Import circolare tra moduli

**Codice errato:**
```python
# --- file: modulo_a.py ---
from modulo_b import funzione_b

def funzione_a():
    return "A"

# --- file: modulo_b.py ---
from modulo_a import funzione_a

def funzione_b():
    return funzione_a() + "B"
```

**Cosa succede:**
```
ImportError: cannot import name 'funzione_a' from partially initialized module 'modulo_a'
(most likely due to a circular import)
```

**Perché è sbagliato:** `modulo_a` importa `modulo_b`, che a sua volta importa `modulo_a`. Python entra in un ciclo: quando `modulo_b` cerca di importare `funzione_a`, `modulo_a` non ha ancora finito di caricarsi, quindi `funzione_a` non è ancora stata definita.

**Codice corretto:**
```python
# Soluzione 1: ristrutturare il codice per eliminare la dipendenza circolare
# Mettere le funzioni condivise in un terzo modulo

# --- file: funzioni_comuni.py ---
def funzione_a():
    return "A"

# --- file: modulo_b.py ---
from funzioni_comuni import funzione_a

def funzione_b():
    return funzione_a() + "B"

# Soluzione 2: importare dentro la funzione (import locale)
# --- file: modulo_b.py ---
def funzione_b():
    from modulo_a import funzione_a  # import ritardato
    return funzione_a() + "B"
```

**Regola da ricordare:** Se due moduli si importano a vicenda, ristruttura il codice estraendo le funzioni condivise in un terzo modulo.

---

### Errore 6: Usare `sorted()` con una funzione `key` sbagliata

**Codice errato:**
```python
studenti = [
    {"nome": "Luca", "voto": 28},
    {"nome": "Anna", "voto": 30},
    {"nome": "Marco", "voto": 25},
]

# Lo studente chiama la funzione invece di passarla
ordinati = sorted(studenti, key=lambda s: s["voto"]())
```

**Cosa succede:**
```
TypeError: 'int' object is not callable
```

**Perché è sbagliato:** `s["voto"]` restituisce già un intero (es. `28`). Aggiungere `()` dopo significa cercare di chiamare quel numero come se fosse una funzione. Il parametro `key` vuole una funzione che estrae il valore da usare per il confronto, non il risultato di una chiamata.

**Codice corretto:**
```python
studenti = [
    {"nome": "Luca", "voto": 28},
    {"nome": "Anna", "voto": 30},
    {"nome": "Marco", "voto": 25},
]

# La lambda accede al valore senza chiamarlo
ordinati = sorted(studenti, key=lambda s: s["voto"])
print(ordinati)
# [{'nome': 'Marco', 'voto': 25}, {'nome': 'Luca', 'voto': 28}, {'nome': 'Anna', 'voto': 30}]

# Per ordine decrescente:
ordinati_desc = sorted(studenti, key=lambda s: s["voto"], reverse=True)
```

**Regola da ricordare:** Il parametro `key` di `sorted()` richiede una funzione che restituisce il criterio di ordinamento: non aggiungere `()` al valore estratto.

---
