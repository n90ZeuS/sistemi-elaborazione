# Autovalutazione — T07: Primi passi in Python

Per ogni esercizio scrivete la risposta prima di aprire la soluzione, poi verificatela eseguendo il codice.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
x = 10
y = x
x = 20
print(y)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
10
```

**Spiegazione:** `y = x` non copia nulla: attacca l'etichetta `y` allo stesso oggetto `10` a cui punta `x`. Poi `x = 20` sposta l'etichetta `x` su un nuovo oggetto `20`; `y` resta attaccata a `10`. Riassegnare `x` non cambia l'oggetto a cui punta `y`.
</details>

---

### Esercizio 2

```python
a = "5"
b = 3
print(type(a))
print(type(b))
print(int(a) + b)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
<class 'str'>
<class 'int'>
8
```

**Spiegazione:** La variabile `a` contiene la **stringa** `"5"` (notare le virgolette), mentre `b` contiene l'**intero** `3`. La funzione `type()` mostra il tipo dell'oggetto a cui punta ciascuna variabile. Con `int(a)` convertiamo la stringa `"5"` nell'intero `5`, e poi sommiamo `5 + 3 = 8`.
</details>

---

### Esercizio 3

```python
nome = "Alice"
eta = 22
media = 27.5
print(f"{nome} ha {eta} anni e media {media:.1f}")
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
Alice ha 22 anni e media 27.5
```

**Spiegazione:** Le f-string (stringhe precedute da `f`) permettono di inserire variabili direttamente nel testo usando le parentesi graffe `{}`. Il formato `:.1f` indica di mostrare il numero float con **1 cifra decimale**. `27.5` ha già una sola cifra decimale, quindi il risultato resta `27.5`.
</details>

---

### Esercizio 4

```python
x = 7
x = x + 1
print(x)
print(type(x))
x = float(x)
print(x)
print(type(x))
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
8
<class 'int'>
8.0
<class 'float'>
```

**Spiegazione:** Inizialmente `x` vale `7` (intero). Con `x = x + 1` diventa `8`, sempre intero. Poi `float(x)` converte l'intero `8` nel numero decimale `8.0`. Notare che Python stampa `8.0` (con il punto decimale) per i float, mentre stampa `8` (senza punto) per gli interi.
</details>

---

## Trova l'errore

### Esercizio 5

Il codice seguente dovrebbe convertire in intero un prezzo scritto come stringa, ma genera un errore. Quale?

```python
prezzo = "3.14"
prezzo_intero = int(prezzo)
print(prezzo_intero)
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `ValueError: invalid literal for int() with base 10: '3.14'`

**Problema:** `int()` accetta solo stringhe che rappresentano un intero, come `"3"` o `"-12"`. La stringa `"3.14"` contiene un punto decimale, quindi non è un intero valido. (Con un numero, invece, `int(3.14)` funziona e restituisce `3`.)

**Soluzione:**
```python
prezzo = "3.14"
prezzo_intero = int(float(prezzo))  # prima float, poi int
print(prezzo_intero)  # stampa 3
```

Si deve prima convertire a `float` e poi a `int`. Il passaggio intermedio `float("3.14")` produce `3.14`, e `int(3.14)` tronca a `3`.
</details>

---

### Esercizio 6

Questo codice dovrebbe stampare un saluto, ma genera un errore. Quale?

```python
nome = Alice
print("Ciao, " + nome)
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `NameError: name 'Alice' is not defined`

Nelle versioni recenti di Python il messaggio può proseguire con un suggerimento, per esempio `Did you mean: 'slice'?`: Python propone un nome esistente simile, che qui non c'entra.

**Problema:** Mancano le virgolette attorno ad `Alice`. Senza virgolette, Python pensa che `Alice` sia il nome di una variabile (che non esiste).

**Soluzione:**
```python
nome = "Alice"
print("Ciao, " + nome)
```

Il testo va racchiuso tra virgolette, singole `'...'` o doppie `"..."`.
</details>

---

### Esercizio 7

Il codice dovrebbe calcolare il BMI (peso diviso altezza al quadrato), ma stampa un valore sbagliato. Perché?

```python
peso = 75
altezza = 1.80
bmi = peso / altezza * altezza
print(f"BMI: {bmi:.1f}")
```

<details>
<summary>Mostra la risposta</summary>

**Output prodotto:** `BMI: 75.0`

**Problema:** La formula del BMI è `peso / altezza ** 2`, cioè `peso / (altezza * altezza)`. `/` e `*` hanno la stessa precedenza e senza parentesi vengono eseguiti da sinistra a destra: prima `75 / 1.80 = 41.67`, poi `41.67 * 1.80 = 75.0`. Il risultato è di nuovo il peso.

**Soluzione:**
```python
peso = 75
altezza = 1.80
bmi = peso / (altezza * altezza)  # oppure: peso / altezza ** 2
print(f"BMI: {bmi:.1f}")  # stampa BMI: 23.1
```
</details>

---

## Completa il codice

### Esercizio 8

Completate la f-string in modo che il programma stampi la riga indicata.

```python
nome: str = "Luca"
matricola: int = 12345
media: float = 26.7
print(f"______________________________________")
# deve stampare: Studente: Luca (mat. 12345) — Media: 26.70
```

<details>
<summary>Mostra la risposta</summary>

```python
print(f"Studente: {nome} (mat. {matricola}) — Media: {media:.2f}")
```

**Spiegazione:** Ogni variabile va tra graffe `{}`. Il formato `:.2f` mostra `media` con 2 cifre decimali, quindi `26.7` diventa `26.70`. Con `:.1f` si otterrebbe `26.7`.
</details>

---

### Esercizio 9

Completate il programma che converte una temperatura da Fahrenheit a Celsius con la formula C = (F - 32) × 5/9 e la stampa con 1 cifra decimale.

```python
temp_f: float = 98.6
temp_c: float = _______________________
print(f"{temp_f}°F = {________}°C")
# deve stampare: 98.6°F = 37.0°C
```

<details>
<summary>Mostra la risposta</summary>

```python
temp_f: float = 98.6
temp_c: float = (temp_f - 32) * 5 / 9
print(f"{temp_f}°F = {temp_c:.1f}°C")
```

**Spiegazione:** Le parentesi attorno a `temp_f - 32` servono perché la moltiplicazione viene eseguita prima della sottrazione: senza parentesi `temp_f - 32 * 5 / 9` vale `98.6 - 17.78 = 80.82`. Il formato `:.1f` mostra `temp_c` con una cifra decimale: `37.0`.
</details>
