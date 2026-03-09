# Strutture Dati a Confronto

Scheda di riferimento rapido: Lista vs Tupla vs Dizionario vs Set.

---

## Tabella di confronto generale

| Caratteristica       | Lista `list`         | Tupla `tuple`        | Dizionario `dict`          | Set `set`              |
|----------------------|----------------------|----------------------|----------------------------|------------------------|
| **Sintassi**         | `[1, 2, 3]`         | `(1, 2, 3)`         | `{"a": 1, "b": 2}`        | `{1, 2, 3}`           |
| **Vuota**            | `[]` o `list()`     | `()` o `tuple()`    | `{}` o `dict()`            | `set()`  (NON `{}`)   |
| **Mutabile?**        | Si                   | No                   | Si                         | Si                     |
| **Ordinata?**        | Si (per indice)      | Si (per indice)      | Si (ordine inserimento 3.7+)| No                    |
| **Duplicati?**       | Si                   | Si                   | Chiavi uniche              | No                     |
| **Indicizzabile?**   | Si `l[0]`            | Si `t[0]`            | Per chiave `d["a"]`        | No                     |
| **Slicing?**         | Si `l[1:3]`          | Si `t[1:3]`          | No                         | No                     |
| **Hashable?**        | No                   | Si (se contenuto lo e')| No                       | No                     |
| **Uso tipico**       | Collezione modificabile | Dati fissi, chiavi dict | Associazioni chiave-valore | Elementi unici, insiemi |

---

## Complessita' temporale (Big-O) delle operazioni principali

| Operazione            | Lista          | Tupla          | Dizionario     | Set            |
|-----------------------|----------------|----------------|----------------|----------------|
| **Accesso per indice**| O(1)           | O(1)           | --             | --             |
| **Accesso per chiave**| --             | --             | O(1) medio     | --             |
| **Ricerca (`in`)**    | O(n)           | O(n)           | O(1) medio     | O(1) medio     |
| **Inserimento**       | O(1) append, O(n) insert | --     | O(1) medio     | O(1) medio     |
| **Cancellazione**     | O(n)           | --             | O(1) medio     | O(1) medio     |
| **Iterazione**        | O(n)           | O(n)           | O(n)           | O(n)           |
| **len()**             | O(1)           | O(1)           | O(1)           | O(1)           |

> **Nota:** "medio" indica il caso medio; nel caso peggiore (collisioni hash) puo' essere O(n).

---

## Operazioni principali per struttura

### Lista

```python
frutti = ["mela", "banana", "ciliegia"]

frutti.append("arancia")        # aggiunge in fondo
frutti.insert(1, "kiwi")        # inserisce alla posizione 1
frutti.remove("banana")         # rimuove per valore
ultimo = frutti.pop()           # rimuove e restituisce l'ultimo
frutti.sort()                   # ordina in-place
frutti.reverse()                # inverte in-place
copia = frutti.copy()           # copia superficiale
indice = frutti.index("mela")  # trova indice del valore
quante = frutti.count("mela")  # conta occorrenze
frutti.extend(["uva", "pera"]) # aggiunge piu' elementi
```

### Tupla

```python
coordinate = (45.07, 7.69)

x, y = coordinate               # unpacking
primo = coordinate[0]            # accesso per indice
sotto = coordinate[0:1]          # slicing -> (45.07,)
indice = coordinate.index(7.69)  # trova indice
quante = coordinate.count(7.69)  # conta occorrenze
lunghezza = len(coordinate)      # numero di elementi

# Tupla con un solo elemento: serve la virgola!
singola = (42,)
```

### Dizionario

```python
studente = {"nome": "Luca", "eta": 20, "media": 27.5}

studente["corso"] = "Statistica"    # aggiunge/modifica
nome = studente["nome"]             # accesso (KeyError se assente)
nome = studente.get("nome", "?")    # accesso sicuro con default
del studente["eta"]                 # cancella chiave
eta = studente.pop("eta", None)     # rimuove e restituisce

chiavi = studente.keys()            # vista sulle chiavi
valori = studente.values()          # vista sui valori
coppie = studente.items()           # vista (chiave, valore)

studente.update({"media": 28})      # aggiorna da altro dict
esiste = "nome" in studente         # True - cerca tra le CHIAVI
```

### Set

```python
numeri = {1, 2, 3, 4, 5}
pari = {2, 4, 6, 8}

numeri.add(6)                       # aggiunge un elemento
numeri.discard(99)                  # rimuove (nessun errore se assente)
numeri.remove(1)                    # rimuove (KeyError se assente)

# Operazioni insiemistiche
unione       = numeri | pari        # oppure numeri.union(pari)
intersezione = numeri & pari        # oppure numeri.intersection(pari)
differenza   = numeri - pari        # oppure numeri.difference(pari)
simmetrica   = numeri ^ pari        # oppure numeri.symmetric_difference(pari)

sottoinsieme = {2, 4} <= pari      # True - sottoinsieme
```

---

## Quando usare quale? Guida decisionale

```
Ho bisogno di una collezione di elementi...

1. Gli elementi devono essere associati a delle chiavi?
   --> Si: usa un DIZIONARIO

2. Gli elementi devono essere tutti unici? (senza duplicati)
   --> Si: usa un SET

3. La collezione deve poter cambiare dopo la creazione?
   --> Si: usa una LISTA
   --> No: usa una TUPLA

Casi particolari:
- Devo usarlo come chiave di un dizionario?   --> TUPLA
- Devo fare molte ricerche "x in collezione"?  --> SET o DIZIONARIO
- Devo mantenere l'ordine di inserimento?      --> LISTA o DIZIONARIO
- Rappresento un record con campi fissi?       --> TUPLA (o namedtuple)
- Devo fare operazioni insiemistiche?          --> SET
```

---

## Conversioni tra tipi

```python
# Lista <-> Tupla
lista = [1, 2, 3]
tupla = tuple(lista)        # (1, 2, 3)
lista = list(tupla)         # [1, 2, 3]

# Lista/Tupla -> Set (rimuove duplicati)
lista = [1, 2, 2, 3, 3]
insieme = set(lista)        # {1, 2, 3}
lista_unica = list(set(lista))  # [1, 2, 3] (ordine non garantito)

# Set -> Lista (per ordinare)
ordinata = sorted(insieme)  # [1, 2, 3] restituisce una lista

# Dizionario -> Lista
chiavi = list(studente.keys())      # ["nome", "corso", ...]
valori = list(studente.values())    # ["Luca", "Statistica", ...]
coppie = list(studente.items())     # [("nome","Luca"), ...]

# Lista di coppie -> Dizionario
coppie = [("a", 1), ("b", 2)]
diz = dict(coppie)                  # {"a": 1, "b": 2}

# Due liste -> Dizionario (con zip)
chiavi = ["nome", "eta"]
valori = ["Luca", 20]
diz = dict(zip(chiavi, valori))     # {"nome": "Luca", "eta": 20}

# Stringa -> Lista di caratteri
caratteri = list("ciao")           # ["c", "i", "a", "o"]

# Lista di stringhe -> Stringa
parole = ["buon", "giorno"]
frase = " ".join(parole)           # "buon giorno"
```

---

## Riepilogo visivo

```
Lista   [a, b, c, d]     Ordinata, mutabile, duplicati ok
Tupla   (a, b, c, d)     Ordinata, immutabile, duplicati ok
Dict    {k1:v1, k2:v2}   Chiave->Valore, mutabile, chiavi uniche
Set     {a, b, c, d}     Non ordinata, mutabile, elementi unici
```
