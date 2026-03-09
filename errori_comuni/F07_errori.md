# Errori comuni — F07: Primi passi in Python

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione F07.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

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

**Perché è sbagliato:** Python usa l'indentazione (gli spazi a inizio riga) per definire la struttura del codice. Se una riga è indentata senza motivo (cioè senza un `if`, `for`, `def` o simile che la precede), Python non sa come interpretarla e segnala un errore. A differenza di altri linguaggi, in Python gli spazi a inizio riga non sono solo estetici: hanno un significato preciso.

**Codice corretto:**
```python
nome = "Mario"
print(nome)
```

**Regola da ricordare:** In Python, non indentare mai una riga a meno che non faccia parte di un blocco (dopo `if`, `for`, `while`, `def`, ecc.).

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
SyntaxError: invalid syntax
```

**Perché è sbagliato:** L'operatore `=` serve per assegnare un valore a una variabile, non per confrontare due valori. Per verificare se due valori sono uguali si usa `==` (doppio uguale). È un errore molto comune perché in matematica usiamo un solo `=` per l'uguaglianza.

**Codice corretto:**
```python
voto = 30
if voto == 30:
    print("Complimenti!")
```

**Regola da ricordare:** Un solo `=` assegna, due `==` confrontano: sono due operazioni completamente diverse.

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

**Perché è sbagliato:** La funzione `int()` può convertire in intero solo stringhe che contengono effettivamente un numero (come `"42"` o `"7"`). Se la stringa contiene lettere o altri caratteri non numerici, Python non sa come trasformarla in un numero e genera un errore. Lo stesso vale per `float()` con stringhe non numeriche.

**Codice corretto:**
```python
# Convertire una stringa che contiene un numero
numero = int("42")
print(numero)  # 42

# Convertire un numero decimale in stringa
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

**Perché è sbagliato:** In Python, il testo (le stringhe) deve essere racchiuso tra virgolette, singole (`'...'`) o doppie (`"..."`). Senza virgolette, Python interpreta `Ciao` come un nome di variabile e non trova nessuna variabile con quel nome. Il testo scritto senza virgolette non viene riconosciuto come stringa.

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
SyntaxError: invalid syntax
```

**Perché è sbagliato:** I nomi delle variabili in Python devono rispettare regole precise: non possono iniziare con un numero e non possono contenere spazi. `1_voto` inizia con un numero, `media voti` contiene uno spazio. Python li considera sintassi non valida e non riesce a interpretare la riga.

**Codice corretto:**
```python
voto_1 = 28
media_voti = 25.5
```

**Regola da ricordare:** I nomi di variabile devono iniziare con una lettera o underscore, e non possono contenere spazi — usa l'underscore `_` per separare le parole.

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

**Perché è sbagliato:** In Python 3, `print` è una funzione e, come tutte le funzioni, richiede le parentesi per essere chiamata. Scrivere `print "Ciao"` era la sintassi di Python 2, ormai non più utilizzato. Molti tutorial vecchi o esempi trovati online usano ancora la vecchia sintassi.

**Codice corretto:**
```python
print("Ciao mondo")
```

**Regola da ricordare:** `print()` è una funzione: il contenuto da stampare va sempre tra parentesi tonde.

---

### Errore 7: Errore nell'uso delle f-string

**Codice errato:**
```python
nome = "Giulia"
eta = 20
# Errore 1: dimenticare la f prima delle virgolette
print("{nome} ha {eta} anni")

# Errore 2: dimenticare le graffe
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
