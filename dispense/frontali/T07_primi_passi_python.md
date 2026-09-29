# Lezione 7 — Primi passi in Python

## Introduzione

Nella lezione precedente (T06) abbiamo visto come si passa da un problema a un algoritmo e da un algoritmo a un programma, e che cosa fa l'interprete Python. Oggi scriviamo il primo codice Python: il programma "Hello, World!", le regole di indentazione e i commenti, le variabili e i tipi di dato fondamentali (`int`, `float`, `str`, `bool`, `None`).

---

## Il primo programma

Per una tradizione resa popolare nel 1978 da Brian Kernighan e Dennis Ritchie con il libro *"The C Programming Language"*, il primo programma in un nuovo linguaggio stampa il messaggio "Hello, World!":

```python
print("Hello, World!")
```

In questa riga ci sono già tre elementi da notare:

- `print` è una **funzione** built-in di Python. Le funzioni si chiamano mettendo gli argomenti tra parentesi.
- `"Hello, World!"` è una **stringa**: una sequenza di caratteri racchiusa tra virgolette (doppie `"` o singole `'`, in Python sono equivalenti).
- Non c'è punto e virgola alla fine della riga. In Python, di norma, ogni istruzione occupa una riga e la fine della riga chiude l'istruzione.

### L'indentazione come sintassi

In molti linguaggi (C, Java, JavaScript), i blocchi di codice sono delimitati da parentesi graffe `{}` e l'indentazione serve solo alla leggibilità. In Python **l'indentazione fa parte della sintassi**: il livello di indentazione determina quali istruzioni appartengono a quale blocco.

```python
temperatura: float = 32.0
if temperatura > 30:
    print("Fa caldo!")      # questo è dentro l'if
    print("Accendi il ventilatore")  # anche questo
print("Fine del programma")  # questo è fuori dall'if
```

È una scelta di Guido van Rossum, l'autore di Python: obbliga a scrivere il codice con un'indentazione ordinata. Un'indentazione incoerente produce un errore (`IndentationError`); un'istruzione indentata al livello sbagliato può invece finire nel blocco sbagliato, e il programma fa una cosa diversa da quella voluta. L'`if` verrà spiegato nella prossima lezione (T08).

La convenzione (PEP 8) è usare **4 spazi** per livello di indentazione, senza tabulazioni: mescolare spazi e tabulazioni nello stesso blocco produce un errore. VS Code inserisce 4 spazi quando si preme il tasto Tab in un file Python.

### I commenti

I commenti iniziano con `#` e vengono ignorati dall'interprete:

```python
# Questo è un commento su una riga intera
temperatura: float = 23.5  # Commento a fine riga
```

Un commento utile spiega il **perché** di un'istruzione: l'intenzione, il ragionamento o un caso particolare. Che cosa fa l'istruzione si dovrebbe capire dal codice stesso, con nomi scelti bene:

```python
# MALE: commento inutile, ripete il codice
i = i + 1  # incrementa i di 1

# BENE: commento che spiega il perché
i = i + 1  # salta l'intestazione del CSV (la prima riga non contiene dati)
```

---

## Variabili e assegnamento

### Variabili come nomi

In molti corsi introduttivi le variabili vengono presentate come "scatole che contengono valori". Per Python questo modello è impreciso e porta a fraintendimenti.

In Python una variabile è un **nome (etichetta) che si riferisce a un oggetto in memoria**. L'operatore `=` collega il nome a sinistra all'oggetto ottenuto valutando l'espressione a destra: **attacca un'etichetta a un oggetto**.

```python
x: int = 42
```

Qui succede questo: Python crea un oggetto intero con valore 42 in memoria, e attacca l'etichetta `x` a quell'oggetto. Se poi scrivete:

```python
y: int = x
```

Non viene creata una copia: `y` diventa un'altra etichetta attaccata **allo stesso oggetto**. Sia `x` che `y` puntano al medesimo 42.

```python
x: int = 42
y: int = x
print(x is y)  # True: sono lo stesso oggetto
```

L'operatore `is` restituisce `True` quando due nomi si riferiscono allo stesso oggetto. Questo modello servirà quando parleremo di liste e mutabilità.

### Assegnamento

L'operatore `=` è l'assegnamento. **Non è l'uguaglianza matematica** (per quella, Python usa `==`).

```python
contatore: int = 0          # assegnamento: contatore punta a 0
contatore = contatore + 1   # riassegnamento: contatore ora punta a 1
# In matematica "x = x + 1" non ha soluzione; qui significa:
# calcola contatore + 1 e collega il nome contatore al risultato.
```

Esistono anche gli **operatori di assegnamento composto**:

```python
totale: int = 100
prodotto: int = 3
contatore += 1   # equivale a contatore = contatore + 1
totale -= 10     # equivale a totale = totale - 10
prodotto *= 2    # equivale a prodotto = prodotto * 2
```

### Assegnamento multiplo e unpacking

Python permette di assegnare più nomi in una sola istruzione:

```python
# Assegnamento multiplo: tre nomi collegati allo stesso oggetto 0
a = b = c = 0

# Unpacking: a ogni nome a sinistra va il valore corrispondente a destra
a, b, c = 1, 2, 3  # a=1, b=2, c=3

# Scambio di variabili: in altri linguaggi serve una variabile temporanea
a, b = b, a  # ora a=2, b=1
```

In queste forme non si possono scrivere i type hints (`a: int = b: int = 0` è un `SyntaxError`); se servono, si annotano i nomi in righe separate.

### Naming conventions (PEP 8)

**PEP 8** è la guida di stile ufficiale di Python. Per i nomi, le regole sono:

- **Variabili e funzioni:** `snake_case` (lettere minuscole separate da underscore)
  ```python
  media_voti: float = 27.5
  numero_studenti: int = 120
  ```
- **Costanti:** `UPPER_SNAKE_CASE`
  ```python
  SOGLIA_SUFFICIENZA: int = 18
  PI_GRECO: float = 3.14159265
  ```
- **Classi:** `PascalCase` (lo vedremo più avanti)
  ```python
  class StudenteUniversitario:
      pass
  ```

Oltre allo stile, conta il significato: **i nomi devono descrivere il contenuto**. Il nome di una variabile è una forma di documentazione:

```python
# MALE: cosa significano x, y, z?
x: float = sum(z) / len(z)

# BENE: il codice si spiega da solo
media_voti: float = sum(lista_voti) / len(lista_voti)
```

Evitate nomi di una sola lettera (tranne `i`, `j`, `k` per gli indici di ciclo e `n` per le dimensioni, dove la convenzione matematica è chiara). Evitate `l` (elle minuscola), `O` (o maiuscola) e `I` (i maiuscola) perché si confondono con i numeri 1 e 0.

---

## Tipi di dato fondamentali

### Python è tipizzato dinamicamente

In Python, il **tipo appartiene all'oggetto, non alla variabile**. Una variabile può puntare a oggetti di tipo diverso nel tempo:

```python
x = 42        # x punta a un int
x = "ciao"    # ora x punta a una str (è consentito)
```

Questo è diverso da linguaggi come C o Java, dove ogni variabile ha un tipo fisso dichiarato. La tipizzazione dinamica rende Python flessibile, ma alcuni errori di tipo emergono solo durante l'esecuzione. Per rendere esplicito il tipo atteso useremo i **type hints**.

### Type hints: il nostro approccio

I type hints sono annotazioni **facoltative** che dichiarano il tipo atteso. L'interprete non le controlla: `eta: int = "venti"` viene eseguito senza errori. Le annotazioni però:
- rendono il codice **più leggibile** (si vede subito che cosa contiene ogni variabile);
- permettono a strumenti come **mypy** (o all'editor) di segnalare incoerenze prima dell'esecuzione;
- obbligano a **decidere il tipo** di ogni variabile mentre si scrive il codice.

```python
# Senza type hints (funziona, ma meno chiaro):
eta = 25
nome = "Mario"
media = 27.5

# Con type hints (il nostro standard):
eta: int = 25
nome: str = "Mario"
media: float = 27.5
iscritto: bool = True
```

In questo corso li useremo **sempre**, a partire da questa lezione.

### I tipi fondamentali

#### `int` — Numeri interi

```python
eta: int = 25
popolazione: int = 59_000_000  # underscore come separatore delle migliaia (ignorato)
temperatura: int = -5
```

Gli interi Python hanno **precisione arbitraria**: non vanno in overflow e la loro dimensione è limitata solo dalla memoria disponibile. In C o Java, invece, un intero occupa un numero fisso di bit (ad esempio 32 o 64) e ha quindi un valore massimo; ne parleremo nella lezione sulla rappresentazione dei dati (T05).

```python
grande: int = 2 ** 100  # funziona perfettamente
print(grande)  # 1267650600228229401496703205376
```

#### `float` — Numeri in virgola mobile

```python
altezza: float = 1.75
pi: float = 3.14159265358979
temperatura: float = -2.5
notazione_scientifica: float = 6.022e23  # 6.022 × 10²³
```

Sono numeri IEEE 754 a doppia precisione (64 bit, circa 15-16 cifre decimali significative). Molti numeri decimali, come 0.1, non hanno una rappresentazione esatta in binario, quindi i calcoli possono avere piccoli errori di arrotondamento:

```python
print(0.1 + 0.2)         # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False
```

Il motivo verrà spiegato nella lezione sulla rappresentazione dei dati (T05).

#### `str` — Stringhe

```python
nome: str = "Anna"
cognome: str = 'Rossi'     # virgolette singole equivalenti
messaggio: str = "Ciao, mondo!"
multilinea: str = """Questa stringa
occupa più righe"""
```

Le stringhe sono sequenze **immutabili** di caratteri Unicode. Le approfondiremo in una lezione dedicata.

#### `bool` — Booleani

```python
iscritto: bool = True
esame_superato: bool = False
```

`True` e `False` si scrivono con l'iniziale maiuscola. `bool` è un sottotipo di `int`: `True` vale `1` e `False` vale `0`:

```python
print(True + True)   # 2
print(True * 10)     # 10
print(False + 5)     # 5
```

Il motivo è storico: il tipo `bool` è stato aggiunto in Python 2.3, quando si usavano già 1 e 0 come valori di verità, e doveva restare compatibile con quel codice. In pratica permette di contare i valori veri di una sequenza con `sum()`: `sum([True, False, True])` vale 2.

#### `NoneType` — L'assenza di valore

```python
risultato: None = None
```

`None` rappresenta l'assenza di valore. È diverso da zero, dalla stringa vuota e da `False`: è l'unico valore del tipo `NoneType`. Le funzioni che non restituiscono esplicitamente un valore restituiscono `None`.

### La funzione `type()`

Per verificare il tipo di un oggetto:

```python
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("ciao"))     # <class 'str'>
print(type(True))       # <class 'bool'>
print(type(None))       # <class 'NoneType'>
```

### Conversioni di tipo (casting)

```python
# Da stringa a numero
eta: int = int("25")           # 25
altezza: float = float("1.75") # 1.75

# Da numero a stringa
testo: str = str(42)           # "42"

# Da int a float e viceversa
x: float = float(42)           # 42.0
y: int = int(3.99)             # 3 (tronca verso lo zero, non arrotonda)

# Conversione a bool
print(bool(0))       # False
print(bool(42))      # True (qualsiasi numero diverso da 0)
print(bool(""))      # False (stringa vuota)
print(bool("ciao"))  # True (qualsiasi stringa non vuota)
```

### Tutto è un oggetto

In Python ogni valore è un oggetto, anche i numeri:

```python
print((42).bit_length())      # 6 (servono 6 bit per rappresentare 42)
print((-7).bit_length())      # 3
print("ciao".upper())         # CIAO
print([1, 2, 3].append(4))    # None (append modifica la lista e restituisce None)
```

Ogni valore ha quindi **attributi** e **metodi**, cioè funzioni associate all'oggetto che operano su di esso. Si chiamano con la notazione col punto (`oggetto.metodo()`), che useremo in tutto il corso.

---

## Domande di verifica

1. **Perché in Python l'indentazione non è opzionale?** Qual è il vantaggio di questa scelta progettuale?

2. **Qual è la differenza tra il modello "variabile come scatola" e il modello "variabile come etichetta"?** Quale è corretto in Python?

3. **Cosa sono i type hints?** Cambiano il comportamento del programma?

4. **Perché `bool` è un sottotipo di `int` in Python?** Cosa significa in pratica?

5. **Qual è la differenza tra `=` e `==` in Python?**

6. **Cosa restituisce `int(3.99)`?** Perché non restituisce 4?

7. **Perché è importante dare nomi significativi alle variabili?** Fate un esempio di nome cattivo e del suo equivalente buono.

8. **Cosa significa "tutto è un oggetto" in Python?** Fate un esempio con un numero intero.

---

## Esercizi

### Base

1. Scrivete un programma che dichiara le seguenti variabili con type hints e stampa il loro tipo:
   ```python
   nome: str = "il vostro nome"
   eta: int = # la vostra età
   altezza: float = # la vostra altezza in metri
   studente: bool = True
   ```

2. Scrivete un programma che calcola l'area di un rettangolo:
   ```python
   base: float = 5.0
   altezza: float = 3.0
   area: float = ...  # completate
   print(f"L'area del rettangolo è {area}")
   ```

3. Cosa stampa il seguente codice? Provate a prevederlo prima di eseguirlo:
   ```python
   a: int = 10
   b: int = a
   a = 20
   print(b)
   ```

### Intermedio

4. Scrivete un programma che converte una temperatura da Celsius a Fahrenheit (formula: F = C × 9/5 + 32). Usate type hints e f-string per l'output formattato:
   ```python
   celsius: float = 25.0
   # ... completate
   print(f"{celsius}°C = {fahrenheit:.1f}°F")
   ```

5. Scrivete un programma che, dato un importo in euro e un tasso di cambio, calcola l'equivalente in un'altra valuta. Usate nomi di variabili significativi.

6. Esplorate il tipo `bool` come sottotipo di `int`:
   ```python
   # Cosa stampano queste espressioni? Perché?
   print(True + True + True)
   print(True * 100)
   print(False - 1)
   print(type(True + 1))
   ```

### Avanzato

7. Scrivete un programma che calcola la **distanza euclidea** tra due punti nel piano:
   ```python
   import math

   x1: float = 1.0
   y1: float = 2.0
   x2: float = 4.0
   y2: float = 6.0

   distanza: float = ...  # formula: √((x2-x1)² + (y2-y1)²)
   print(f"Distanza: {distanza:.4f}")
   ```

8. Investigate il comportamento dell'operatore `is` vs `==`:
   ```python
   a: int = 256
   b: int = 256
   print(a == b)   # ?
   print(a is b)    # ?

   c: int = 257
   d: int = 257
   print(c == d)   # ?
   print(c is d)    # ?
   ```
   Eseguite il codice una volta nella shell interattiva (una riga alla volta) e una volta come script (`python3 file.py`): i risultati di `c is d` possono essere diversi. Cercate il concetto di "integer caching" in CPython per spiegare il risultato.

---

## Osservazioni finali

Oggi abbiamo visto il primo programma, le variabili, i tipi fondamentali e le conversioni. Due concetti torneranno per tutto il corso:

1. **Le variabili sono nomi che si riferiscono a oggetti.** Con liste e dizionari questo modello sarà necessario: `b = a` non copia l'oggetto, ma crea un secondo nome (alias) per lo stesso oggetto.

2. **I type hints.** Annotare i tipi obbliga a stabilire che cosa contiene ogni variabile e rende il codice verificabile con strumenti come mypy.

Nella prossima lezione (T08) vedremo gli operatori, l'input/output e le strutture condizionali, con cui un programma può scegliere quali istruzioni eseguire in base ai dati.
