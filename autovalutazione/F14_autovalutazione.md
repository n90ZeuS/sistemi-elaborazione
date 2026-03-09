# Autovalutazione — F14: Lambda, Map/Filter e Closure

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
numeri = [1, 2, 3, 4, 5]
doppi = list(map(lambda x: x * 2, numeri))
print(doppi)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
[2, 4, 6, 8, 10]
```

**Spiegazione:** `map()` applica una funzione a ogni elemento di un iterabile. Qui la funzione lambda `lambda x: x * 2` raddoppia ogni numero. `map()` restituisce un iteratore, quindi usiamo `list()` per ottenere una lista. Il risultato e' ogni elemento della lista originale moltiplicato per 2.
</details>

---

### Esercizio 2

```python
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pari = list(filter(lambda x: x % 2 == 0, numeri))
print(pari)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
[2, 4, 6, 8, 10]
```

**Spiegazione:** `filter()` mantiene solo gli elementi per cui la funzione restituisce `True`. La lambda `lambda x: x % 2 == 0` verifica se un numero e' pari (resto della divisione per 2 uguale a 0). Vengono quindi mantenuti solo i numeri pari.
</details>

---

### Esercizio 3

```python
def crea_moltiplicatori():
    moltiplicatori = []
    for i in range(1, 4):
        moltiplicatori.append(lambda x: x * i)
    return moltiplicatori

funzioni = crea_moltiplicatori()
print(funzioni[0](10))
print(funzioni[1](10))
print(funzioni[2](10))
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
30
30
30
```

**Spiegazione:** Questo e' un errore classico chiamato **late binding** nelle closure. Tutte e tre le lambda catturano la **stessa variabile** `i`, non il suo valore al momento della creazione. Quando le funzioni vengono chiamate, il ciclo `for` e' gia' terminato e `i` vale `3`. Quindi tutte e tre calcolano `10 * 3 = 30`. Per catturare il valore corrente si usa un argomento di default: `lambda x, i=i: x * i`.
</details>

---

### Esercizio 4

```python
nomi = ["alice", "Bob", "CARLA", "diana"]
ordinati = sorted(nomi, key=lambda s: s.lower())
print(ordinati)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
['alice', 'Bob', 'CARLA', 'diana']
```

**Spiegazione:** `sorted()` ordina gli elementi usando la funzione `key` per determinare l'ordine. La lambda converte ogni stringa in minuscolo **solo per il confronto**, senza modificare gli elementi originali. L'ordine alfabetico (ignorando maiuscole/minuscole) e': alice, Bob, CARLA, diana. Gli elementi nella lista risultante mantengono le lettere originali.
</details>

---

## Trova l'errore

### Esercizio 5

```python
# Vogliamo una lambda che calcola il BMI
calcola_bmi = lambda peso, altezza:
    peso / (altezza ** 2)

print(calcola_bmi(70, 1.75))
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `SyntaxError: invalid syntax`

**Problema:** Le lambda in Python devono essere scritte su **una sola riga**. Non si puo' andare a capo dopo i `:`.

**Correzione:**
```python
# Lambda su una sola riga
calcola_bmi = lambda peso, altezza: peso / (altezza ** 2)

print(calcola_bmi(70, 1.75))  # 22.857142857142858
```

**Alternativa (consigliata per funzioni con un nome):**
```python
def calcola_bmi(peso, altezza):
    """Calcola l'indice di massa corporea."""
    return peso / (altezza ** 2)

print(calcola_bmi(70, 1.75))  # 22.857142857142858
```

**Lezione:** Le lambda sono pensate per funzioni semplici e brevi. Se una funzione ha bisogno di piu' righe o merita un nome descrittivo, usate `def`.
</details>

---

### Esercizio 6

```python
def crea_incrementatori():
    funzioni = []
    for n in range(5):
        funzioni.append(lambda x: x + n)
    return funzioni

inc = crea_incrementatori()
print(inc[0](100))  # Ci aspettiamo 100
print(inc[3](100))  # Ci aspettiamo 103
```

<details>
<summary>Mostra la risposta</summary>

**Output indesiderato:**
```
104
104
```

**Problema:** Late binding delle closure. Tutte le lambda catturano la variabile `n`, che alla fine del ciclo vale `4`. Quindi tutte le funzioni calcolano `x + 4`.

**Correzione:**
```python
def crea_incrementatori():
    funzioni = []
    for n in range(5):
        # n=n cattura il valore corrente come default
        funzioni.append(lambda x, n=n: x + n)
    return funzioni

inc = crea_incrementatori()
print(inc[0](100))  # 100
print(inc[3](100))  # 103
```

**Lezione:** Quando create lambda in un ciclo, usate il trucco `n=n` nel parametro di default per "congelare" il valore della variabile al momento della creazione.
</details>

---

### Esercizio 7

```python
from math import *

print(sqrt(16))
print(log(1))

# Piu' tardi nel codice...
sqrt = "radice quadrata"
print(sqrt(25))
```

<details>
<summary>Mostra la risposta</summary>

**Output prima dell'errore:**
```
4.0
0.0
```
**Poi errore:** `TypeError: 'str' object is not callable`

**Problema:** `from math import *` importa tutte le funzioni di `math` nel namespace corrente. Successivamente, il nome `sqrt` viene sovrascritto con una stringa. Quando si tenta di chiamare `sqrt(25)`, Python prova a "chiamare" la stringa `"radice quadrata"`, causando l'errore.

**Correzione:**
```python
import math

print(math.sqrt(16))   # 4.0
print(math.log(1))     # 0.0

sqrt = "radice quadrata"  # Non sovrascrive math.sqrt
print(math.sqrt(25))      # 5.0
```

**Lezione:** Evitate `from modulo import *` perche' inquina il namespace e rende possibili sovrascritture accidentali. Preferite `import math` e usate `math.sqrt()`.
</details>

---

## Completa il codice

### Esercizio 8

Completa il codice per trasformare una lista di temperature da Celsius a Fahrenheit usando `map` e una `lambda`.

```python
temperature_celsius = [0, 20, 37, 100]

# --- COMPLETA: usa map e lambda per convertire ---
# Formula: F = C * 9/5 + 32
temperature_fahrenheit = ???

print(temperature_fahrenheit)
# Output atteso: [32.0, 68.0, 98.6, 212.0]
```

<details>
<summary>Mostra la soluzione</summary>

```python
temperature_celsius = [0, 20, 37, 100]

temperature_fahrenheit = list(map(lambda c: c * 9/5 + 32, temperature_celsius))

print(temperature_fahrenheit)
# Output: [32.0, 68.0, 98.6, 212.0]
```

**Spiegazione:** La lambda `lambda c: c * 9/5 + 32` applica la formula di conversione a ogni temperatura. `map()` applica questa lambda a ogni elemento della lista, e `list()` converte il risultato in una lista.
</details>

---

### Esercizio 9

Completa la funzione che filtra gli studenti con un voto sopra la soglia.

```python
def studenti_sopra_soglia(registro, soglia):
    """
    Riceve un dizionario {nome: voto} e una soglia.
    Restituisce la lista dei nomi degli studenti con voto >= soglia,
    ordinata alfabeticamente.
    """
    # --- COMPLETA: usa filter e/o lambda ---
    pass

# Test
voti = {"Alice": 28, "Bob": 18, "Carla": 30, "Diana": 24, "Eva": 15}
print(studenti_sopra_soglia(voti, 25))
# Output atteso: ['Alice', 'Carla']
print(studenti_sopra_soglia(voti, 18))
# Output atteso: ['Alice', 'Bob', 'Carla', 'Diana']
```

<details>
<summary>Mostra la soluzione</summary>

```python
def studenti_sopra_soglia(registro, soglia):
    """
    Riceve un dizionario {nome: voto} e una soglia.
    Restituisce la lista dei nomi degli studenti con voto >= soglia,
    ordinata alfabeticamente.
    """
    filtrati = filter(lambda nome: registro[nome] >= soglia, registro)
    return sorted(filtrati)

voti = {"Alice": 28, "Bob": 18, "Carla": 30, "Diana": 24, "Eva": 15}
print(studenti_sopra_soglia(voti, 25))
# Output: ['Alice', 'Carla']
print(studenti_sopra_soglia(voti, 18))
# Output: ['Alice', 'Bob', 'Carla', 'Diana']
```

**Spiegazione:** `filter()` itera sulle chiavi del dizionario (i nomi) e mantiene solo quelli per cui `registro[nome] >= soglia` e' `True`. Poi `sorted()` ordina i nomi rimanenti in ordine alfabetico. Si poteva scrivere anche con una list comprehension: `sorted([nome for nome, voto in registro.items() if voto >= soglia])`.
</details>
