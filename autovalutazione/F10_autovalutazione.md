# Autovalutazione — F10: Comprehension, Stringhe e Metodi

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
numeri = [1, 2, 3, 4, 5, 6, 7, 8]
pari = [n for n in numeri if n % 2 == 0]
print(pari)
doppi = [n * 2 for n in numeri if n < 5]
print(doppi)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
[2, 4, 6, 8]
[2, 4, 6, 8]
```

**Spiegazione:** La prima list comprehension filtra solo gli elementi pari dalla lista: il risultato e `[2, 4, 6, 8]`. La seconda seleziona gli elementi minori di 5 (`1, 2, 3, 4`) e li moltiplica per 2 (`2, 4, 6, 8`). Notare che i risultati sono uguali per coincidenza, ma i meccanismi sono diversi: la prima filtra, la seconda trasforma e filtra.
</details>

---

### Esercizio 2

```python
frase = "Ciao Mondo"
print(frase.lower())
print(frase.upper())
print(frase.replace("Mondo", "Python"))
print(frase)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
ciao mondo
CIAO MONDO
Ciao Python
Ciao Mondo
```

**Spiegazione:** I metodi delle stringhe (`lower()`, `upper()`, `replace()`) restituiscono una **nuova stringa** e non modificano l'originale. Le stringhe in Python sono **immutabili**: non possono essere cambiate dopo la creazione. L'ultima riga lo dimostra: `frase` e ancora `"Ciao Mondo"` nonostante le operazioni precedenti.
</details>

---

### Esercizio 3

```python
dati = "rosso,verde,blu,giallo"
colori = dati.split(",")
print(colori)
print(len(colori))
risultato = " - ".join(colori)
print(risultato)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
['rosso', 'verde', 'blu', 'giallo']
4
rosso - verde - blu - giallo
```

**Spiegazione:** `split(",")` divide la stringa in una lista usando la virgola come separatore. `len()` conta gli elementi della lista (4 colori). `" - ".join(colori)` fa l'operazione inversa: unisce gli elementi della lista in un'unica stringa, inserendo `" - "` tra un elemento e l'altro.
</details>

---

### Esercizio 4

```python
parole = ["ciao", "mondo", "python", "è", "bello"]
lunghe = [p.upper() for p in parole if len(p) > 3]
print(lunghe)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
['CIAO', 'MONDO', 'PYTHON', 'BELLO']
```

**Spiegazione:** La comprehension ha tre parti: (1) trasformazione `p.upper()`, (2) iterazione `for p in parole`, (3) filtro `if len(p) > 3`. Prima si filtrano le parole con piu di 3 caratteri (si esclude `"è"` che ha 1 carattere), poi si trasformano in maiuscolo. L'ordine di lettura e: "per ogni `p` in `parole`, **se** la lunghezza e maggiore di 3, prendi `p.upper()`".
</details>

---

## Trova l'errore

### Esercizio 5

Il codice dovrebbe mettere in maiuscolo la prima lettera di una stringa, ma genera un errore.

```python
nome = "alice"
nome[0] = "A"
print(nome)
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `TypeError: 'str' object does not support item assignment`

**Problema:** Le stringhe sono **immutabili** in Python: non si possono modificare i singoli caratteri. L'operazione `nome[0] = "A"` tenta di cambiare il primo carattere, ma Python non lo permette.

**Soluzione:**
```python
nome = "alice"
nome = "A" + nome[1:]     # creiamo una NUOVA stringa
print(nome)                # stampa: Alice

# Oppure, più semplice:
nome = "alice"
nome = nome.capitalize()   # metodo che capitalizza la prima lettera
print(nome)                # stampa: Alice
```

Con le stringhe, si crea sempre una **nuova** stringa invece di modificare quella esistente.
</details>

---

### Esercizio 6

Il codice dovrebbe separare nome e cognome, ma il risultato e sbagliato.

```python
dati = "Rossi;Marco;25"
parti = dati.split(",")
print(f"Cognome: {parti[0]}, Nome: {parti[1]}")
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `IndexError: list index out of range`

**Problema:** La stringa usa il punto e virgola `;` come separatore, ma `split(",")` cerca la virgola `,`. Siccome non ci sono virgole, `split` restituisce una lista con un solo elemento: `["Rossi;Marco;25"]`. Tentare di accedere a `parti[1]` causa un `IndexError`.

**Soluzione:**
```python
dati = "Rossi;Marco;25"
parti = dati.split(";")    # separatore corretto: punto e virgola
print(f"Cognome: {parti[0]}, Nome: {parti[1]}")
# stampa: Cognome: Rossi, Nome: Marco
```

Bisogna sempre verificare quale carattere viene usato come separatore nei dati.
</details>

---

### Esercizio 7

Il codice dovrebbe creare una lista di quadrati dei numeri pari, ma ha un errore di sintassi.

```python
numeri = [1, 2, 3, 4, 5, 6]
quadrati = [n ** 2 for n in numeri if n % 2 == 0 if n > 3]
print(quadrati)
```

<details>
<summary>Mostra la risposta</summary>

**Output:** `[16, 36]`

**Nota:** In realta questo codice **funziona** in Python (piu `if` consecutivi sono equivalenti a `and`), ma e molto poco leggibile e fonte comune di confusione.

**Versione consigliata (piu chiara):**
```python
numeri = [1, 2, 3, 4, 5, 6]
quadrati = [n ** 2 for n in numeri if n % 2 == 0 and n > 3]
print(quadrati)  # stampa: [16, 36]
```

Usare `and` per combinare piu condizioni rende il codice piu leggibile. I numeri che soddisfano entrambe le condizioni (pari **e** maggiori di 3) sono `4` e `6`, i cui quadrati sono `16` e `36`.
</details>

---

## Completa il codice

### Esercizio 8

Completa la funzione che restituisce le parole piu lunghe di `n` caratteri da una frase.

```python
def parole_lunghe(frase, n):
    """Restituisce la lista delle parole più lunghe di n caratteri.

    Esempio: parole_lunghe("il gatto dorme sul divano", 3)
    deve restituire ["gatto", "dorme", "divano"]
    """
    parole = frase.____________
    return [_________ for p in _________ if ___________]
```

<details>
<summary>Mostra la risposta</summary>

```python
def parole_lunghe(frase, n):
    """Restituisce la lista delle parole più lunghe di n caratteri."""
    parole = frase.split()
    return [p for p in parole if len(p) > n]
```

**Spiegazione:** `split()` senza argomenti divide la stringa per spazi bianchi (spazi, tab, a capo). La comprehension scorre ogni parola `p` e la include nel risultato solo se la sua lunghezza supera `n`. Nota: `split()` senza argomenti gestisce anche spazi multipli, a differenza di `split(" ")`.
</details>

---

### Esercizio 9

Completa la funzione che pulisce e normalizza un testo.

```python
def normalizza_testo(testo):
    """Pulisce un testo: minuscolo, senza spazi extra, senza punteggiatura finale.

    Esempio: normalizza_testo("  Ciao, MONDO!  ")
    deve restituire "ciao, mondo!"

    Esempio: normalizza_testo("  PYTHON   è   BELLO  ")
    deve restituire "python è bello"
    """
    testo = testo.____________     # rimuove spazi iniziali e finali
    testo = testo.____________     # converte in minuscolo
    parole = testo.____________    # divide in parole
    return _________________________  # riunisce con un singolo spazio
```

<details>
<summary>Mostra la risposta</summary>

```python
def normalizza_testo(testo):
    """Pulisce un testo: minuscolo, senza spazi extra."""
    testo = testo.strip()
    testo = testo.lower()
    parole = testo.split()
    return " ".join(parole)
```

**Spiegazione:** La pipeline di pulizia funziona cosi: (1) `strip()` rimuove gli spazi bianchi all'inizio e alla fine; (2) `lower()` converte tutto in minuscolo; (3) `split()` divide per spazi (gestendo anche spazi multipli); (4) `" ".join(parole)` ricompone il testo con un solo spazio tra le parole, eliminando cosi gli spazi extra interni.
</details>

---

### Esercizio 10

Completa la funzione che conta le vocali in una stringa.

```python
def conta_vocali(testo):
    """Conta il numero di vocali (a, e, i, o, u) nel testo.

    Esempio: conta_vocali("Ciao Mondo") deve restituire 4
    """
    vocali = "aeiou"
    testo_lower = testo.__________
    return ____([_____________ for c in testo_lower if ______________])
```

<details>
<summary>Mostra la risposta</summary>

```python
def conta_vocali(testo):
    """Conta il numero di vocali (a, e, i, o, u) nel testo."""
    vocali = "aeiou"
    testo_lower = testo.lower()
    return len([c for c in testo_lower if c in vocali])
```

**Spiegazione:** Prima convertiamo il testo in minuscolo per non doverci preoccupare delle maiuscole. La comprehension `[c for c in testo_lower if c in vocali]` costruisce una lista con solo i caratteri che sono vocali. Infine, `len()` conta quanti elementi ha questa lista. In `"ciao mondo"` le vocali sono `i, a, o, o` = 4.
</details>
