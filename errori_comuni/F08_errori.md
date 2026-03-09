# Errori comuni — F08: Operatori, I/O e condizionali

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione F08.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

---

### Errore 1: Confondere divisione vera (`/`) e divisione intera (`//`)

**Codice errato:**
```python
# Lo studente vuole calcolare la media di 3 voti
media = (28 + 30 + 25) // 3
print(media)  # Output: 27
```

**Cosa succede:**
```
27
```

Il risultato è 27 invece di 27.666..., perché `//` tronca la parte decimale.

**Perché è sbagliato:** L'operatore `//` esegue la divisione intera, cioè restituisce solo la parte intera del risultato, scartando i decimali. Per ottenere il risultato completo (con la parte decimale), bisogna usare `/`. Per calcoli statistici come la media, quasi sempre serve la divisione vera `/`.

**Codice corretto:**
```python
media = (28 + 30 + 25) / 3
print(media)  # Output: 27.666666666666668
```

**Regola da ricordare:** Usa `/` per la divisione con decimali (la più comune) e `//` solo quando vuoi esplicitamente scartare la parte decimale.

---

### Errore 2: Usare `and`/`or` con valori non booleani senza capire il risultato

**Codice errato:**
```python
# Lo studente vuole verificare se x è 5 oppure 10
x = 7
if x == 5 or 10:
    print("x è 5 oppure 10")
```

**Cosa succede:**
```
x è 5 oppure 10
```

Il messaggio viene stampato anche se `x` vale 7, perché la condizione è sempre vera.

**Perché è sbagliato:** L'espressione `x == 5 or 10` non significa "x è uguale a 5 oppure a 10". Python la interpreta come `(x == 5) or (10)`, cioè: "x è uguale a 5, oppure il valore 10". Siccome il numero `10` è considerato "vero" (ogni numero diverso da 0 è vero in Python), la condizione complessiva è sempre vera.

**Codice corretto:**
```python
x = 7
if x == 5 or x == 10:
    print("x è 5 oppure 10")

# Alternativa più elegante:
if x in (5, 10):
    print("x è 5 oppure 10")
```

**Regola da ricordare:** Dopo `or` e `and` serve sempre una condizione completa — scrivi `x == 5 or x == 10`, mai `x == 5 or 10`.

---

### Errore 3: Dimenticare che `input()` restituisce sempre una stringa

**Codice errato:**
```python
eta = input("Quanti anni hai? ")
anno_nascita = 2026 - eta
print(f"Sei nato nel {anno_nascita}")
```

**Cosa succede:**
```
TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

**Perché è sbagliato:** La funzione `input()` restituisce sempre una stringa, anche se l'utente digita un numero. Quando lo studente scrive `20`, Python lo memorizza come la stringa `"20"`, non come il numero `20`. Non è possibile sottrarre una stringa da un intero: bisogna prima convertire il risultato di `input()` in un numero con `int()` o `float()`.

**Codice corretto:**
```python
eta = int(input("Quanti anni hai? "))
anno_nascita = 2026 - eta
print(f"Sei nato nel {anno_nascita}")
```

**Regola da ricordare:** `input()` restituisce sempre una stringa: se ti serve un numero, usa `int(input(...))` o `float(input(...))`.

---

### Errore 4: Usare `=` invece di `==` nella condizione di un `if`

**Codice errato:**
```python
risposta = input("Vuoi continuare? (s/n) ")
if risposta = "s":
    print("Continuiamo!")
```

**Cosa succede:**
```
SyntaxError: invalid syntax
```

**Perché è sbagliato:** All'interno di una condizione `if` bisogna usare l'operatore di confronto `==` (doppio uguale), non l'operatore di assegnamento `=` (uguale singolo). Python non permette l'assegnamento dentro un `if` e segnala un errore di sintassi. È uno degli errori più comuni per chi inizia a programmare.

**Codice corretto:**
```python
risposta = input("Vuoi continuare? (s/n) ")
if risposta == "s":
    print("Continuiamo!")
```

**Regola da ricordare:** Nelle condizioni `if`, `while` e simili si usa sempre `==` per confrontare, mai `=`.

---

### Errore 5: Indentazione sbagliata in `if`/`elif`/`else`

**Codice errato:**
```python
voto = 28
if voto >= 30:
    print("Ottimo!")
    elif voto >= 24:
    print("Buono")
else:
    print("Sufficiente")
```

**Cosa succede:**
```
IndentationError: unexpected indent
```

**Perché è sbagliato:** Le parole chiave `if`, `elif` e `else` devono trovarsi tutte allo stesso livello di indentazione. Nel codice errato, `elif` è indentato come se fosse dentro il blocco `if`, ma deve essere allineato con `if` ed `else`. Solo le istruzioni all'interno di ciascun blocco vanno indentate.

**Codice corretto:**
```python
voto = 28
if voto >= 30:
    print("Ottimo!")
elif voto >= 24:
    print("Buono")
else:
    print("Sufficiente")
```

**Regola da ricordare:** `if`, `elif` e `else` devono essere allineati alla stessa colonna; solo il codice dentro ciascun blocco va indentato di un livello.

---

### Errore 6: Confronto tra tipi diversi che non dà errore ma produce risultati inattesi

**Codice errato:**
```python
eta = input("Quanti anni hai? ")  # L'utente digita 18
if eta > 17:
    print("Maggiorenne")
else:
    print("Minorenne")
```

**Cosa succede:**
```
TypeError: '>' not supported between instances of 'str' and 'int'
```

**Perché è sbagliato:** Siccome `input()` restituisce una stringa, `eta` contiene la stringa `"18"`, non il numero `18`. Python 3 non permette confronti diretti tra stringhe e numeri interi con `>`, `<` e simili, e genera un `TypeError`. Lo studente deve prima convertire il valore in un intero con `int()`.

**Codice corretto:**
```python
eta = int(input("Quanti anni hai? "))
if eta > 17:
    print("Maggiorenne")
else:
    print("Minorenne")
```

**Regola da ricordare:** Prima di confrontare un valore numerico, assicurati che sia effettivamente un numero e non una stringa — converti sempre il risultato di `input()`.
