# Errori comuni — F13: Funzioni: fondamenti

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione F13.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

---

### Errore 1: Argomento default mutabile `def f(x=[])`

**Codice errato:**
```python
def aggiungi_elemento(elemento, lista=[]):
    lista.append(elemento)
    return lista

print(aggiungi_elemento(1))
print(aggiungi_elemento(2))
print(aggiungi_elemento(3))
```

**Cosa succede:**
```
[1]
[1, 2]
[1, 2, 3]
```
Lo studente si aspettava tre liste separate `[1]`, `[2]`, `[3]`.

**Perché è sbagliato:** La lista `[]` usata come valore default viene creata una sola volta, al momento della definizione della funzione. Ogni chiamata successiva lavora sulla stessa lista, che accumula tutti gli elementi. Questo è uno dei tranelli più insidiosi di Python.

**Codice corretto:**
```python
def aggiungi_elemento(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista

print(aggiungi_elemento(1))  # [1]
print(aggiungi_elemento(2))  # [2]
print(aggiungi_elemento(3))  # [3]
```

**Regola da ricordare:** Non usare mai oggetti mutabili (`[]`, `{}`, `set()`) come valori default dei parametri: usa `None` e crea l'oggetto dentro la funzione.

---

### Errore 2: Variabile locale che nasconde (shadow) una variabile globale

**Codice errato:**
```python
contatore = 10

def incrementa():
    contatore = contatore + 1  # sembra che usi la variabile globale
    return contatore

print(incrementa())
```

**Cosa succede:**
```
UnboundLocalError: cannot access local variable 'contatore' where it is not associated with a value
```

**Perché è sbagliato:** Quando Python vede un assegnamento a `contatore` dentro la funzione, tratta `contatore` come variabile locale. Ma a destra di `=` si cerca di leggere `contatore` prima che le sia stato assegnato un valore locale, causando l'errore. La variabile globale è "nascosta" da quella locale.

**Codice corretto:**
```python
contatore = 10

def incrementa(valore):
    return valore + 1

contatore = incrementa(contatore)
print(contatore)  # 11
```

**Regola da ricordare:** Non modificare variabili globali dentro le funzioni: passa il valore come argomento e restituisci il risultato.

---

### Errore 3: Dimenticare l'istruzione `return`

**Codice errato:**
```python
def calcola_media(voti):
    media = sum(voti) / len(voti)
    # manca il return!

risultato = calcola_media([28, 30, 25, 27])
print(f"La media è: {risultato}")
```

**Cosa succede:**
```
La media è: None
```
Nessun errore, ma il risultato è `None` invece del valore calcolato.

**Perché è sbagliato:** Se una funzione non contiene un'istruzione `return`, Python restituisce automaticamente `None`. Il calcolo viene eseguito correttamente, ma il risultato viene perso perché non viene restituito al chiamante.

**Codice corretto:**
```python
def calcola_media(voti):
    media = sum(voti) / len(voti)
    return media

risultato = calcola_media([28, 30, 25, 27])
print(f"La media è: {risultato}")  # La media è: 27.5
```

**Regola da ricordare:** Se la funzione deve produrre un risultato, aggiungi sempre `return valore` alla fine: senza `return`, la funzione restituisce `None`.

---

### Errore 4: Credere che i type hints impongano il tipo

**Codice errato:**
```python
def somma(a: int, b: int) -> int:
    return a + b

# Lo studente pensa che questo dia errore
risultato = somma("ciao", "mondo")
print(risultato)
```

**Cosa succede:**
```
ciaomondo
```
Nessun errore: Python esegue la concatenazione di stringhe senza protestare.

**Perché è sbagliato:** I type hints in Python sono solo annotazioni informative: servono come documentazione e per strumenti di analisi statica (come `mypy`), ma Python non li controlla a runtime. Si possono passare argomenti di qualsiasi tipo e Python non genererà errori basandosi sui type hints.

**Codice corretto:**
```python
def somma(a: int, b: int) -> int:
    """Somma due numeri interi."""
    return a + b

# I type hints documentano l'uso previsto, ma tocca a noi rispettarli
risultato = somma(3, 5)
print(risultato)  # 8

# Per un controllo esplicito:
def somma_sicura(a: int, b: int) -> int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("I parametri devono essere numerici")
    return a + b
```

**Regola da ricordare:** I type hints sono solo suggerimenti per il programmatore e gli strumenti di analisi: Python non li verifica durante l'esecuzione.

---

### Errore 5: Numero di argomenti sbagliato nella chiamata

**Codice errato:**
```python
def calcola_bmi(peso, altezza):
    return peso / (altezza ** 2)

# Chiamata con un solo argomento
risultato = calcola_bmi(75)
```

**Cosa succede:**
```
TypeError: calcola_bmi() missing 1 required positional argument: 'altezza'
```

**Perché è sbagliato:** La funzione `calcola_bmi` richiede esattamente due argomenti posizionali (`peso` e `altezza`). Passarne uno solo o tre causa un `TypeError`. Python è rigoroso: il numero di argomenti nella chiamata deve corrispondere alla definizione.

**Codice corretto:**
```python
def calcola_bmi(peso, altezza):
    return peso / (altezza ** 2)

risultato = calcola_bmi(75, 1.80)
print(f"BMI: {risultato:.1f}")  # BMI: 23.1
```

**Regola da ricordare:** Controlla sempre la definizione della funzione per passare esattamente il numero e il tipo di argomenti richiesti.

---

### Errore 6: Confondere `print()` e `return`

**Codice errato:**
```python
def quadrato(n):
    print(n ** 2)  # stampa il risultato, ma non lo restituisce

# Lo studente prova a usare il risultato
risultato = quadrato(5)
doppio = risultato * 2
```

**Cosa succede:**
```
25
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```
Il `25` viene stampato, ma `risultato` è `None` e non si può moltiplicare.

**Perché è sbagliato:** `print()` mostra un valore sullo schermo ma non lo restituisce alla funzione chiamante. La funzione `quadrato` stampa `25` ma restituisce `None` (perché non ha `return`). Quando si prova a fare `None * 2`, Python solleva un errore.

**Codice corretto:**
```python
def quadrato(n):
    return n ** 2  # restituisce il risultato

risultato = quadrato(5)
print(risultato)    # 25
doppio = risultato * 2
print(doppio)       # 50
```

**Regola da ricordare:** `print()` mostra un valore a schermo, `return` lo restituisce al chiamante: per riutilizzare il risultato di una funzione serve `return`.

---
