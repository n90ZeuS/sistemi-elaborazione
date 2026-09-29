# Errori comuni — T07: Primi passi in Python

Errori frequenti sugli argomenti della lezione T07. Per ogni errore: il codice sbagliato, il messaggio di Python (verificato con Python 3.13), la spiegazione e la correzione.

---

### Errore 1: IndentationError — indentazione inaspettata

**Codice errato:**
```python
nome = "Mario"
  print(nome)
```

**Cosa succede:**
```
IndentationError: unexpected indent
```

**Perché è sbagliato:** Python usa l'indentazione (gli spazi a inizio riga) per definire la struttura del codice. Una riga può essere indentata solo se fa parte di un blocco, cioè se segue un'istruzione che termina con `:` come `if` (che vedremo in T08). Qui `print(nome)` è indentata senza un blocco che la contenga, quindi Python segnala l'errore. In Python gli spazi a inizio riga fanno parte della sintassi.

**Codice corretto:**
```python
nome = "Mario"
print(nome)
```

**Regola da ricordare:** Si indenta una riga solo quando fa parte di un blocco (dopo `if`, e più avanti `for`, `while`, `def`). Le istruzioni del programma principale partono dalla colonna 1.

---

### Errore 2: Usare `=` al posto di `==` per confrontare

**Codice errato:**
```python
voto = 30
if voto = 30:
    print("Complimenti!")
```

**Cosa succede:**
```
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

**Perché è sbagliato:** L'operatore `=` assegna un valore a una variabile, non confronta due valori. Per verificare se due valori sono uguali si usa `==` (doppio uguale). L'errore è frequente perché in matematica si usa un solo `=` per l'uguaglianza. L'istruzione `if` la vediamo in T08; il messaggio di Python suggerisce già la correzione (`:=` è un operatore diverso, che in questo corso non useremo).

**Codice corretto:**
```python
voto = 30
if voto == 30:
    print("Complimenti!")
```

**Regola da ricordare:** Un solo `=` assegna, due `==` confrontano.

---

### Errore 3: Tipo sbagliato nel casting — passare una stringa non numerica a `int()`

**Codice errato:**
```python
numero = int("ciao")
```

**Cosa succede:**
```
ValueError: invalid literal for int() with base 10: 'ciao'
```

**Perché è sbagliato:** La funzione `int()` può convertire in intero solo stringhe che contengono un numero intero (come `"42"` o `"-7"`). Se la stringa contiene lettere, o anche un punto decimale come `"3.14"`, Python genera un `ValueError`. Lo stesso vale per `float()` con stringhe non numeriche: `float("ciao")` dà `ValueError: could not convert string to float: 'ciao'`.

**Codice corretto:**
```python
# Convertire una stringa che contiene un numero
numero = int("42")
print(numero)  # 42

# Convertire in float una stringa che contiene un numero decimale
valore = float("3.14")
print(valore)  # 3.14
```

**Regola da ricordare:** `int()` e `float()` possono convertire solo stringhe che rappresentano numeri validi, altrimenti si ottiene un `ValueError`.

---

### Errore 4: Virgolette mancanti attorno a una stringa

**Codice errato:**
```python
messaggio = Ciao a tutti
print(messaggio)
```

**Cosa succede:**
```
SyntaxError: invalid syntax
```

(Con Python 3.14 il messaggio è `SyntaxError: invalid syntax. Did you mean 'and'?`: il suggerimento non è pertinente.)

**Perché è sbagliato:** Il testo (le stringhe) va racchiuso tra virgolette, singole (`'...'`) o doppie (`"..."`). Senza virgolette Python legge `Ciao`, `a` e `tutti` come tre nomi di variabile scritti uno dopo l'altro, che non formano un'istruzione valida: per questo l'errore è di sintassi. Con una sola parola, per esempio `messaggio = Ciao`, la sintassi è valida ma Python cerca una variabile di nome `Ciao` e dà `NameError: name 'Ciao' is not defined`.

**Codice corretto:**
```python
messaggio = "Ciao a tutti"
print(messaggio)
```

**Regola da ricordare:** Ogni testo letterale in Python deve essere racchiuso tra virgolette (singole o doppie), altrimenti Python lo interpreta come un nome di variabile.

---

### Errore 5: Nome di variabile non valido

**Codice errato:**
```python
1_voto = 28
media voti = 25.5
```

**Cosa succede:**
```
SyntaxError: invalid decimal literal
```

Python si ferma al primo errore, sulla riga `1_voto = 28`. Corretta quella, la riga `media voti = 25.5` dà `SyntaxError: invalid syntax`.

**Perché è sbagliato:** I nomi delle variabili non possono iniziare con una cifra e non possono contenere spazi. `1_voto` inizia con una cifra, quindi Python prova a leggerlo come numero (`1_000` è un numero valido) e non ci riesce. `media voti` contiene uno spazio, quindi sono due nomi separati.

**Codice corretto:**
```python
voto_1 = 28
media_voti = 25.5
```

**Regola da ricordare:** I nomi di variabile iniziano con una lettera o con `_` e non contengono spazi; per separare le parole si usa `_` (`media_voti`).

---

### Errore 6: `print` senza parentesi

**Codice errato:**
```python
print "Ciao mondo"
```

**Cosa succede:**
```
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

**Perché è sbagliato:** In Python 3, `print` è una funzione e, come tutte le funzioni, richiede le parentesi per essere chiamata. Scrivere `print "Ciao"` era la sintassi di Python 2, non più supportato dal 2020. Molti tutorial ed esempi online usano ancora questa sintassi.

**Codice corretto:**
```python
print("Ciao mondo")
```

**Regola da ricordare:** `print()` è una funzione: il contenuto da stampare va sempre tra parentesi tonde.

---

### Errore 7: f-string senza `f` o senza graffe

**Codice errato:**
```python
nome = "Giulia"
eta = 20
# Manca la f prima delle virgolette
print("{nome} ha {eta} anni")

# Mancano le graffe
print(f"nome ha eta anni")
```

**Cosa succede:**
```
{nome} ha {eta} anni
nome ha eta anni
```

Non c'è un messaggio di errore, ma l'output non è quello atteso.

**Perché è sbagliato:** Le f-string richiedono due elementi: la lettera `f` prima delle virgolette e le parentesi graffe `{}` attorno alle variabili. Senza la `f`, le graffe vengono stampate letteralmente come testo. Senza le graffe, i nomi delle variabili vengono stampati come testo normale e non vengono sostituiti con i loro valori.

**Codice corretto:**
```python
nome = "Giulia"
eta = 20
print(f"{nome} ha {eta} anni")
# Output: Giulia ha 20 anni
```

**Regola da ricordare:** Per inserire variabili in una stringa, servono sia la `f` prima delle virgolette sia le graffe `{}` attorno a ogni variabile.
