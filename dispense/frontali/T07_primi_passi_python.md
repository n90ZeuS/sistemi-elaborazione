# Lezione 7 — Primi passi in Python

## Introduzione

Oggi scriviamo il nostro primo codice Python. Dopo cinque lezioni di fondamenti e una di ponte, avete tutti gli strumenti concettuali per capire non solo *come* si programma, ma *perché* le cose funzionano in un certo modo. Quando vedrete che Python usa `=` per l'assegnamento, saprete che dietro c'è un'operazione che modifica un riferimento in memoria. Quando vedrete che `0.1 + 0.2` non è esattamente `0.3`, saprete perché.

Cominciamo.

---

## Il primo programma

Per tradizione inaugurata nel 1978 da Brian Kernighan e Dennis Ritchie nel libro *"The C Programming Language"*, il primo programma in un nuovo linguaggio stampa il messaggio "Hello, World!":

```python
print("Hello, World!")
```

Una sola riga, ma c'è molto da osservare:

- `print` è una **funzione** built-in di Python. Le funzioni si chiamano mettendo gli argomenti tra parentesi.
- `"Hello, World!"` è una **stringa**: una sequenza di caratteri racchiusa tra virgolette (doppie `"` o singole `'`, in Python sono equivalenti).
- Non c'è punto e virgola alla fine della riga. In Python, ogni istruzione occupa una riga (salvo eccezioni esplicite). Questo riduce il "rumore visivo" del codice.

### L'indentazione come sintassi

In molti linguaggi (C, Java, JavaScript), i blocchi di codice sono delimitati da parentesi graffe `{}`. L'indentazione è opzionale e puramente estetica. In Python, **l'indentazione È la sintassi**: il livello di indentazione determina quali istruzioni appartengono a quale blocco.

```python
if temperatura > 30:
    print("Fa caldo!")      # questo è dentro l'if
    print("Accendi il ventilatore")  # anche questo
print("Fine del programma")  # questo è fuori dall'if
```

Questa è una scelta deliberata di Guido van Rossum: forza tutti a scrivere codice leggibile. Non esiste codice Python "funzionante ma illeggibile per l'indentazione" — se l'indentazione è sbagliata, il programma non funziona.

La convenzione è usare **4 spazi** per livello di indentazione (mai tabulazioni, per evitare ambiguità).

### I commenti

I commenti iniziano con `#` e vengono ignorati dall'interprete:

```python
# Questo è un commento su una riga intera
temperatura: float = 23.5  # Commento a fine riga
```

I commenti servono per spiegare il **perché**, non il **cosa**. Il codice stesso deve essere abbastanza chiaro da spiegare cosa fa. Un buon commento spiega l'intenzione, il ragionamento, o avverte di una trappola:

```python
# MALE: commento inutile, ripete il codice
i = i + 1  # incrementa i di 1

# BENE: commento che spiega il perché
i = i + 1  # salta l'intestazione del CSV (la prima riga non contiene dati)
```

---

## Variabili e assegnamento

### Il modello mentale giusto

In molti corsi introduttivi, le variabili vengono presentate come "scatole che contengono valori". Questo modello è sbagliato in Python e porta a fraintendimenti.

In Python, una variabile è un **nome (etichetta) che punta a un oggetto in memoria**. L'operatore `=` non "mette un valore in una scatola" — **attacca un'etichetta a un oggetto**.

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
print(x is y)  # True: sono lo stesso oggetto!
```

Questo modello diventerà cruciale quando parleremo di liste e mutabilità — per ora, tenetelo a mente.

### Assegnamento

L'operatore `=` è l'assegnamento. **Non è l'uguaglianza matematica** (per quella, Python usa `==`).

```python
contatore: int = 0          # assegnamento: contatore punta a 0
contatore = contatore + 1   # riassegnamento: contatore ora punta a 1
# In matematica "x = x + 1" è assurdo; in programmazione è normalissimo.
```

Esistono anche gli **operatori di assegnamento composto**:

```python
contatore += 1   # equivale a contatore = contatore + 1
totale -= 10     # equivale a totale = totale - 10
prodotto *= 2    # equivale a prodotto = prodotto * 2
```

### Assegnamento multiplo e unpacking

Python permette assegnamenti eleganti:

```python
# Assegnamento multiplo
a: int = b: int = c: int = 0  # tutti puntano a 0

# In realtà, la forma più pythonica è:
a, b, c = 1, 2, 3  # unpacking: a=1, b=2, c=3

# Scambio di variabili (in altri linguaggi serve una variabile temporanea!)
a, b = b, a  # Python lo fa in un passo
```

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

La regola più importante: **i nomi devono essere significativi**. Il nome di una variabile è una forma di documentazione:

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
x = "ciao"    # ora x punta a una str (perfettamente legale)
```

Questo è diverso da linguaggi come C o Java, dove ogni variabile ha un tipo fisso dichiarato. La tipizzazione dinamica rende Python flessibile, ma può nascondere errori. Per questo useremo i **type hints**.

### Type hints: il nostro approccio

I type hints sono annotazioni **volontarie** che dichiarano il tipo atteso. Non cambiano il comportamento del programma, ma:
- Rendono il codice **più leggibile** (capisco subito cosa contiene ogni variabile)
- Permettono agli strumenti (**mypy**) di verificare la coerenza prima dell'esecuzione
- Forzano a **pensare ai tipi**, una disciplina mentale preziosa

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

Li useremo **sempre**, fin da questa lezione. Non sono un fardello — sono una buona abitudine che vi renderà programmatori migliori.

### I tipi fondamentali

#### `int` — Numeri interi

```python
eta: int = 25
popolazione: int = 59_000_000  # underscore come separatore delle migliaia (ignorato)
temperatura: int = -5
```

Come visto nella lezione sulla rappresentazione dei dati, gli interi Python hanno **precisione arbitraria**: nessun overflow, nessun limite di dimensione.

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

Sono numeri IEEE 754 a double precision (64 bit, ~15-16 cifre significative). Ricordate: `0.1 + 0.2 != 0.3`.

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

`True` e `False` (con la maiuscola!). Un fatto curioso: `bool` è un sottotipo di `int`. `True` vale `1` e `False` vale `0`:

```python
print(True + True)   # 2
print(True * 10)     # 10
print(False + 5)     # 5
```

Perché? Retrocompatibilità e praticità: permette di contare gli elementi veri in una sequenza con `sum()`.

#### `NoneType` — L'assenza di valore

```python
risultato: None = None
```

`None` rappresenta l'assenza di valore. Non è zero, non è la stringa vuota, non è `False` — è "niente". Le funzioni che non restituiscono esplicitamente un valore restituiscono `None`.

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
y: int = int(3.99)             # 3 (tronca, non arrotonda!)

# Conversione a bool
print(bool(0))       # False
print(bool(42))      # True (qualsiasi numero diverso da 0)
print(bool(""))      # False (stringa vuota)
print(bool("ciao"))  # True (qualsiasi stringa non vuota)
```

### Tutto è un oggetto

In Python, tutto è un oggetto — anche i numeri:

```python
print((42).bit_length())      # 6 (servono 6 bit per rappresentare 42)
print((-7).bit_length())      # 3
print("ciao".upper())         # "CIAO"
print([1, 2, 3].append(4))    # None (modifica la lista in-place)
```

Questo significa che ogni valore ha **attributi** e **metodi** — funzioni associate all'oggetto che operano su di esso. La notazione col punto (`oggetto.metodo()`) è fondamentale in Python.

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
   print(c is d)    # ?  (Sorpresa! Perché?)
   ```
   Ricercate il concetto di "integer caching" in Python per spiegare il risultato.

---

## Osservazioni finali

Oggi avete scritto il vostro primo codice Python. Può sembrare poco — variabili, tipi, assegnamenti — ma le fondamenta sono cruciali. Due concetti di questa lezione vi accompagneranno per tutto il corso e oltre:

1. **Le variabili sono etichette, non scatole.** Questo modello mentale diventerà essenziale quando lavorerete con liste e dizionari: capire che `b = a` non copia ma crea un alias vi risparmierà ore di debugging.

2. **I type hints come disciplina.** Annotare i tipi non è burocrazia — è pensare con chiarezza a cosa entra e cosa esce, a cosa contiene ogni variabile. È la differenza tra "funziona, non so perché" e "funziona, e so perché".

Nella prossima lezione aggiungeremo gli operatori, l'input/output e le strutture condizionali — e i vostri programmi inizieranno a prendere decisioni.
