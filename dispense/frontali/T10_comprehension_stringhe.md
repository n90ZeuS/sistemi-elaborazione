# Lezione 10 — Stringhe

## Introduzione

Finora le stringhe sono servite soprattutto per stampare messaggi. In questa lezione le trattiamo come una struttura dati: una stringa è una sequenza di caratteri, quindi si può accedere a un singolo carattere con un indice, estrarne una parte con lo slicing e scorrerla con un ciclo `for`.

Vediamo poi i metodi principali delle stringhe, che servono per pulire e controllare dati testuali: togliere spazi, cambiare maiuscole e minuscole, cercare e sostituire parti di testo. Chiudiamo con i due formati che usiamo per stampare i numeri e con alcuni esercizi.

All'inizio della lezione vediamo le soluzioni del laboratorio 1.

---

## Stringhe come sequenze

### Indici e immutabilità

Una stringa è una **sequenza immutabile di caratteri**. Sequenza significa che ogni carattere ha una posizione (indice), a partire da 0. Immutabile significa che una stringa, una volta creata, non si può modificare: ogni operazione che sembra modificarla ne crea una nuova.

```python
testo: str = "Statistica"

print(testo[0])        # S
print(testo[-1])       # a    (gli indici negativi contano dalla fine)
print(len(testo))      # 10
print("ist" in testo)  # True
```

Modificare un carattere dà errore:

```python
testo[0] = "s"  # TypeError: 'str' object does not support item assignment
```

Per ottenere una stringa diversa bisogna crearne una nuova:

```python
testo_minuscolo: str = "s" + testo[1:]
print(testo_minuscolo)  # statistica
```

### Slicing

`testo[inizio:fine:passo]` prende i caratteri da `inizio` a `fine` escluso, come in `range()`. Se manca l'inizio si parte da 0, se manca la fine si arriva in fondo.

```python
testo: str = "Statistica"

print(testo[0:4])    # Stat      (da 0 a 3: il 4 è escluso)
print(testo[4:])     # istica    (da 4 alla fine)
print(testo[:4])     # Stat      (dall'inizio a 3)
print(testo[-3:])    # ica       (gli ultimi tre)
print(testo[::2])    # Saitc     (un carattere sì e uno no)
print(testo[::-1])   # acitsitatS
```

### Scorrere una stringa

Una stringa si scorre con `for` come una sequenza: a ogni giro la variabile vale un carattere. Se serve anche la posizione, si scorrono gli indici con `range(len(...))`.

```python
parola: str = "zucca"

for carattere in parola:
    print(carattere, end=" ")    # z u c c a
print()

for i in range(len(parola)):
    print(i, parola[i])          # 0 z, 1 u, 2 c, ...
```

---

## Metodi delle stringhe

Ogni metodo delle stringhe **restituisce una nuova stringa** (o un altro valore) e lascia invariata l'originale.

### `strip()`, `lstrip()`, `rstrip()` — rimozione spazi

```python
dato: str = "  42.5  \n"
pulito: str = dato.strip()
print(repr(pulito))  # '42.5'

# strip() rimuove spazi, tab, newline da entrambi i lati
# lstrip() solo a sinistra, rstrip() solo a destra
```

Nella pulizia di dati importati da file, `strip()` e quasi sempre il primo metodo da chiamare.

### `replace()` — sostituzione

```python
testo: str = "valore: N/A"
pulito: str = testo.replace("N/A", "0")
print(pulito)  # 'valore: 0'

# Sostituisce TUTTE le occorrenze
dati: str = "1,2,,4,,6"
dati_puliti: str = dati.replace(",,", ",0,")
print(dati_puliti)  # '1,2,0,4,0,6'
```

### `count()` — contare

```python
testo: str = "statistica"
print(testo.count("t"))     # 3
print(testo.count("ti"))    # 2
print(testo.count("x"))     # 0
```

### `find()` e `index()` — ricerca

```python
testo: str = "La media campionaria"

# find() restituisce la posizione, o -1 se non trovato
pos: int = testo.find("media")
print(pos)  # 3

pos_assente: int = testo.find("varianza")
print(pos_assente)  # -1

# index() fa lo stesso, ma lancia ValueError se non trovato
# pos: int = testo.index("varianza")  # ValueError!
```

### `startswith()` e `endswith()` — prefisso e suffisso

```python
nome_file: str = "dati_2024.csv"

print(nome_file.startswith("dati"))  # True
print(nome_file.endswith(".csv"))    # True
print(nome_file.endswith(".xlsx"))   # False
```

Utile per filtrare nomi di file, controllare formati, validare input.

### `upper()`, `lower()`, `title()`, `capitalize()` — maiuscole e minuscole

```python
testo: str = "statistica Descrittiva"

print(testo.upper())       # 'STATISTICA DESCRITTIVA'
print(testo.lower())       # 'statistica descrittiva'
print(testo.title())       # 'Statistica Descrittiva'
print(testo.capitalize())  # 'Statistica descrittiva'
```

La conversione a `lower()` e fondamentale per confronti case-insensitive:

```python
risposta: str = "Si"
if risposta.lower() == "si":
    print("Confermato")
```

### `isdigit()`, `isalpha()`, `isalnum()` — test sul contenuto

```python
print("42".isdigit())      # True
print("3.14".isdigit())    # False (il punto non e una cifra)
print("abc".isalpha())     # True
print("abc123".isalnum())  # True
print("abc 123".isalnum()) # False (lo spazio non e alfanumerico)
```

Questi metodi sono utili per validare l'input dell'utente prima di convertirlo.

---

## Formattare i numeri

Dopo i due punti dentro le graffe di una f-string si può indicare come stampare un numero. In questo corso servono due formati:

- `.Nf`: N cifre decimali;
- `.N%`: percentuale con N decimali (il valore viene moltiplicato per 100).

```python
media: float = 27.4567
print(f"Media: {media:.2f}")     # Media: 27.46
print(f"Media: {media:.1f}")     # Media: 27.5

quota: float = 0.0325
print(f"Quota: {quota:.1%}")     # Quota: 3.2%
print(f"Quota: {quota:.0%}")     # Quota: 3%
```

Il formato cambia solo la stampa: la variabile mantiene tutte le sue cifre.

---

## Esercizi in aula

### Esercizio 1 — Contare

Data `frase = "la statistica è una scienza"`, contate le lettere `a` con un ciclo `for`. Poi controllate il risultato con `count()`.

```python
frase: str = "la statistica è una scienza"

conta: int = 0
for carattere in frase:
    if carattere == "a":
        conta += 1

print(conta)               # 5
print(frase.count("a"))    # 5
```

### Esercizio 2 — Estensione

Dato `nome_file = "vendite_2026.csv"`, stampate il nome senza estensione e l'estensione. Usate `find(".")` e lo slicing. Se il punto manca, stampate un messaggio.

```python
nome_file: str = "vendite_2026.csv"

punto: int = nome_file.find(".")
if punto == -1:
    print("Il file non ha estensione")
else:
    print(nome_file[:punto])       # vendite_2026
    print(nome_file[punto + 1:])   # csv
```

### Esercizio 3 — Nome e iniziali

Dato `dato = "  mARIO rossi  "`, stampate `Mario Rossi` e le iniziali `M.R.`.

```python
dato: str = "  mARIO rossi  "

nome: str = dato.strip().title()
spazio: int = nome.find(" ")

print(nome)                                   # Mario Rossi
print(f"{nome[0]}.{nome[spazio + 1]}.")      # M.R.
```

### Esercizio 4 — CAP

Chiedete un CAP con `input()`. È valido se ha 5 caratteri, tutti cifre. Il CAP si tiene come stringa: come numero, `00184` perderebbe gli zeri iniziali.

```python
cap: str = input("CAP: ")

if len(cap) == 5 and cap.isdigit():
    print("CAP valido")
else:
    print("CAP non valido")
```

---

## Domande di verifica

1. Cosa stampa `"Statistica"[2:5]`? E `"Statistica"[-3:]`?

2. Cosa significa che le stringhe sono immutabili? Cosa succede con `testo.upper()` se non assegnate il risultato a una variabile?

3. Che differenza c'è tra `find()` e `index()` quando la sottostringa non c'è?

4. Perché un CAP va tenuto come stringa e non come numero?

5. Cosa stampa `f"{0.1573:.1%}"`?

---

## Esercizi

1. Chiedete all'utente un nome di file e stampate se finisce con `.csv` o con `.txt`.

2. Chiedete una parola e stampatela al contrario, una volta con lo slicing e una volta con un ciclo `for` che costruisce la stringa rovesciata carattere per carattere.

3. Chiedete una frase e stampate quante cifre e quanti spazi contiene, usando `isdigit()` e un ciclo.

4. Chiedete una data nel formato `gg/mm/aaaa` (per esempio `27/10/2026`). Controllate che abbia 10 caratteri, che le barre siano in posizione 2 e 5 e che gli altri caratteri siano cifre; poi stampate giorno, mese e anno con lo slicing.

---

## Riepilogo

1. Una stringa è una sequenza di caratteri: si usano indici, slicing, `len()`, `in` e il ciclo `for`.

2. Le stringhe sono immutabili: ogni metodo (`strip()`, `replace()`, `upper()`, ...) restituisce una stringa nuova.

3. Per stampare i numeri servono due formati: `.2f` per i decimali e `.1%` per le percentuali.

Nella prossima lezione vediamo le **liste e le tuple**. Con le liste arrivano anche le list comprehension e i metodi `split()` e `join()`, che collegano stringhe e liste.
