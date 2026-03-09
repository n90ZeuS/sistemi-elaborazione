# Autovalutazione — F07: Variabili, Tipi e Stringhe

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

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

**Spiegazione:** Quando scriviamo `y = x`, Python copia il **valore** di `x` (cioè `10`) e lo assegna a `y`. Da quel momento, `y` è un'etichetta indipendente che punta al valore `10`. Modificare `x` successivamente non ha alcun effetto su `y`.
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

**Spiegazione:** La variabile `a` contiene la **stringa** `"5"` (notare le virgolette), mentre `b` contiene l'**intero** `3`. La funzione `type()` ci mostra il tipo di ciascuna variabile. Con `int(a)` convertiamo la stringa `"5"` nell'intero `5`, e poi sommiamo `5 + 3 = 8`.
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

**Spiegazione:** Le f-string (stringhe precedute da `f`) permettono di inserire variabili direttamente nel testo usando le parentesi graffe `{}`. Il formato `:.1f` indica di mostrare il numero float con **1 cifra decimale**. Siccome `27.5` ha già una sola cifra decimale, il risultato resta `27.5`.
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

Il seguente codice dovrebbe convertire l'input utente in un numero intero, ma genera un errore. Quale?

```python
prezzo = "3.14"
prezzo_intero = int(prezzo)
print(prezzo_intero)
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `ValueError: invalid literal for int() with base 10: '3.14'`

**Problema:** `int()` non riesce a convertire direttamente una stringa che contiene un numero decimale. La stringa `"3.14"` non rappresenta un intero valido.

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

**Problema:** Mancano le virgolette attorno ad `Alice`. Senza virgolette, Python pensa che `Alice` sia il nome di una variabile (che non esiste).

**Soluzione:**
```python
nome = "Alice"
print("Ciao, " + nome)
```

Le stringhe di testo devono **sempre** essere racchiuse tra virgolette (singole `'...'` o doppie `"..."`).
</details>

---

### Esercizio 7

Il codice dovrebbe stampare il risultato, ma produce un valore inatteso.

```python
peso = 75
altezza = 1.80
bmi = peso / altezza * altezza
print(f"BMI: {bmi:.1f}")
```

<details>
<summary>Mostra la risposta</summary>

**Output prodotto:** `BMI: 75.0`

**Problema:** La formula del BMI è `peso / altezza**2`, cioè `peso / (altezza * altezza)`. Senza parentesi, Python esegue da sinistra a destra: prima `75 / 1.80 = 41.67`, poi `41.67 * 1.80 = 75.0`. Il risultato torna al peso originale!

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

Completa la funzione che restituisce una stringa formattata con le informazioni di uno studente.

```python
def scheda_studente(nome, matricola, media):
    """Restituisce una stringa con le info dello studente.

    Esempio: scheda_studente("Luca", 12345, 26.7)
    deve restituire: "Studente: Luca (mat. 12345) — Media: 26.70"
    """
    return _______________________________________________
```

<details>
<summary>Mostra la risposta</summary>

```python
def scheda_studente(nome, matricola, media):
    """Restituisce una stringa con le info dello studente."""
    return f"Studente: {nome} (mat. {matricola}) — Media: {media:.2f}"
```

**Spiegazione:** Usiamo una f-string per comporre la stringa. Il formato `:.2f` formatta `media` con esattamente **2 cifre decimali**. Quindi `26.7` diventa `26.70`.
</details>

---

### Esercizio 9

Completa la funzione che converte una temperatura da Fahrenheit a Celsius, restituendo un float arrotondato a 1 decimale.

```python
def fahrenheit_a_celsius(temp_f):
    """Converte Fahrenheit in Celsius.

    Formula: C = (F - 32) * 5/9
    Esempio: fahrenheit_a_celsius(98.6) deve restituire 37.0
    """
    temp_c = _______________________
    return round(_______, ___)
```

<details>
<summary>Mostra la risposta</summary>

```python
def fahrenheit_a_celsius(temp_f):
    """Converte Fahrenheit in Celsius."""
    temp_c = (temp_f - 32) * 5 / 9
    return round(temp_c, 1)
```

**Spiegazione:** Applichiamo la formula `(F - 32) * 5/9`. Le parentesi attorno a `temp_f - 32` sono fondamentali per la precedenza degli operatori. La funzione `round(valore, 1)` arrotonda a **1 cifra decimale**.
</details>
