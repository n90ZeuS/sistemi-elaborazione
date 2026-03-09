# Autovalutazione — F08: Operatori, Confronti e Condizionali

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 + 1)
print(10 // 3, 10 % 3)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
14
20
9
3 1
```

**Spiegazione:** Python segue le normali regole di precedenza matematica: `*` prima di `+`, quindi `3 * 4 = 12`, poi `2 + 12 = 14`. Le parentesi forzano l'ordine: `(2 + 3) = 5`, poi `5 * 4 = 20`. L'esponente `**` ha precedenza su `+`: `2 ** 3 = 8`, poi `8 + 1 = 9`. Infine, `//` è la divisione intera (`10 // 3 = 3`) e `%` il resto (`10 % 3 = 1`).
</details>

---

### Esercizio 2

```python
x = 0
y = 5

if x != 0 and y / x > 2:
    print("Condizione vera")
else:
    print("Condizione falsa")
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
Condizione falsa
```

**Spiegazione:** Questo esempio mostra il **short-circuit** (valutazione a corto circuito). Con l'operatore `and`, se la prima condizione e falsa, Python **non valuta** la seconda. Dato che `x != 0` e `False` (perche `x` vale `0`), Python salta `y / x > 2` senza calcolarla. Senza short-circuit, `y / x` causerebbe un `ZeroDivisionError`!
</details>

---

### Esercizio 3

```python
a = 5
print(1 < a < 10)
print(1 < a < 3)
print(a == 5.0)
print(a is 5.0)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
True
False
True
False
```

**Spiegazione:** Python supporta i **confronti concatenati**: `1 < a < 10` equivale a `1 < a and a < 10`, cioe `True`. Per `1 < a < 3`: `1 < 5` e `True` ma `5 < 3` e `False`, quindi il risultato e `False`. L'operatore `==` confronta i **valori** (`5` e `5.0` hanno lo stesso valore), mentre `is` confronta l'**identita** dell'oggetto in memoria (`5` intero e `5.0` float sono oggetti diversi).
</details>

---

### Esercizio 4

```python
voto = 28

if voto >= 28:
    if voto == 30:
        print("Eccellente")
    else:
        print("Ottimo")
elif voto >= 24:
    print("Buono")
elif voto >= 18:
    print("Sufficiente")
else:
    print("Insufficiente")
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
Ottimo
```

**Spiegazione:** Si parte dall'alto: `28 >= 28` e `True`, quindi si entra nel primo blocco `if`. All'interno, si controlla `voto == 30`: siccome `28 != 30`, si esegue l'`else` interno, stampando `"Ottimo"`. I blocchi `elif` successivi non vengono nemmeno controllati perche il primo `if` era gia stato soddisfatto.
</details>

---

## Trova l'errore

### Esercizio 5

Il codice dovrebbe controllare se un numero e pari, ma non funziona. Perche?

```python
n = 10
if n % 2 = 0:
    print("Pari")
else:
    print("Dispari")
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `SyntaxError: invalid syntax`

**Problema:** Nella condizione, `=` e l'operatore di **assegnamento**, non di **confronto**. Per confrontare due valori si usa `==`.

**Soluzione:**
```python
n = 10
if n % 2 == 0:   # == (doppio uguale) per il confronto
    print("Pari")
else:
    print("Dispari")
```

Ricorda: `=` assegna, `==` confronta.
</details>

---

### Esercizio 6

Il codice dovrebbe controllare se l'utente ha inserito un numero positivo, ma non funziona come previsto.

```python
eta = input("Inserisci la tua età: ")  # l'utente digita 25
if eta > 0:
    print("Età valida")
else:
    print("Età non valida")
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `TypeError: '>' not supported between instances of 'str' and 'int'`

**Problema:** La funzione `input()` restituisce **sempre una stringa**, anche se l'utente digita un numero. Quindi `eta` contiene `"25"` (stringa), e Python non puo confrontare una stringa con un intero.

**Soluzione:**
```python
eta = int(input("Inserisci la tua età: "))  # converto subito a int
if eta > 0:
    print("Età valida")
else:
    print("Età non valida")
```

Bisogna convertire esplicitamente il risultato di `input()` con `int()` o `float()`.
</details>

---

### Esercizio 7

Il programmatore vuole controllare se `x` vale 1 oppure 2, ma il codice non si comporta come previsto.

```python
x = 5
if x == 1 or 2:
    print("x è 1 oppure 2")
else:
    print("x è qualcos'altro")
```

<details>
<summary>Mostra la risposta</summary>

**Output (inatteso):** `x è 1 oppure 2`

**Problema:** `x == 1 or 2` non significa "x uguale a 1 oppure a 2". Python lo interpreta come `(x == 1) or (2)`. Siccome `x == 1` e `False`, Python valuta `2`, che e un valore **truthy** (diverso da zero), quindi la condizione e `True`.

**Soluzione:**
```python
x = 5
if x == 1 or x == 2:       # confronto esplicito per ciascun valore
    print("x è 1 oppure 2")
else:
    print("x è qualcos'altro")

# Alternativa elegante:
if x in (1, 2):
    print("x è 1 oppure 2")
```
</details>

---

## Completa il codice

### Esercizio 8

Completa la funzione che classifica un voto universitario italiano.

```python
def classifica_voto(voto):
    """Classifica un voto universitario (18-30).

    - voto < 18       → "Insufficiente"
    - 18 <= voto < 24 → "Sufficiente"
    - 24 <= voto < 27 → "Buono"
    - 27 <= voto < 30 → "Ottimo"
    - voto == 30       → "Eccellente"

    Esempio: classifica_voto(25) deve restituire "Buono"
    """
    if _______________:
        return "Insufficiente"
    elif _______________:
        return "Sufficiente"
    elif _______________:
        return "Buono"
    elif _______________:
        return "Ottimo"
    else:
        return _______________
```

<details>
<summary>Mostra la risposta</summary>

```python
def classifica_voto(voto):
    """Classifica un voto universitario (18-30)."""
    if voto < 18:
        return "Insufficiente"
    elif voto < 24:
        return "Sufficiente"
    elif voto < 27:
        return "Buono"
    elif voto < 30:
        return "Ottimo"
    else:
        return "Eccellente"
```

**Spiegazione:** Siccome usiamo `elif`, ogni condizione viene controllata solo se le precedenti sono false. Se arriviamo a `voto < 24`, sappiamo gia che `voto >= 18` (altrimenti saremmo entrati nel primo `if`). Quindi non serve scrivere `18 <= voto < 24`, basta `voto < 24`. Questa tecnica semplifica molto il codice.
</details>

---

### Esercizio 9

Completa la funzione che determina se un anno e bisestile.

```python
def è_bisestile(anno):
    """Un anno è bisestile se:
    - è divisibile per 4 E non divisibile per 100
    - OPPURE è divisibile per 400

    Esempio: è_bisestile(2024) → True, è_bisestile(1900) → False
    """
    return _________________________________________
```

<details>
<summary>Mostra la risposta</summary>

```python
def è_bisestile(anno):
    """Determina se un anno è bisestile."""
    return (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0)
```

**Spiegazione:** Traduciamo le regole direttamente in codice. L'operatore `%` (modulo) restituisce il resto della divisione: se `anno % 4 == 0`, l'anno e divisibile per 4. Le parentesi raggruppano le due condizioni collegate da `or`. Ad esempio: 2024 e divisibile per 4 e non per 100, quindi e bisestile. 1900 e divisibile per 4 e per 100 ma non per 400, quindi **non** e bisestile.
</details>
