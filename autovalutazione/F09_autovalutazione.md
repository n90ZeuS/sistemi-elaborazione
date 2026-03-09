# Autovalutazione — F09: Cicli, Range e Pattern Accumulatore

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
for i in range(1, 5):
    print(i, end=" ")
print()
for i in range(0, 10, 2):
    print(i, end=" ")
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
1 2 3 4
0 2 4 6 8
```

**Spiegazione:** `range(1, 5)` genera i numeri da `1` a `4` inclusi: il valore **stop** (5) e sempre **escluso**. Con `range(0, 10, 2)` il terzo argomento e il **passo** (step): si parte da 0 e si avanza di 2 in 2, fermandosi prima di 10. Il parametro `end=" "` in `print` sostituisce l'andare a capo con uno spazio.
</details>

---

### Esercizio 2

```python
totale = 0
for n in range(1, 6):
    totale = totale + n
    print(f"n={n}, totale={totale}")
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
n=1, totale=1
n=2, totale=3
n=3, totale=6
n=4, totale=10
n=5, totale=15
```

**Spiegazione:** Questo e il **pattern accumulatore**: si inizializza una variabile (`totale = 0`) prima del ciclo e la si aggiorna a ogni iterazione. A ogni passo, `totale` accumula la somma dei numeri visti finora: 1, 1+2=3, 3+3=6, 6+4=10, 10+5=15.
</details>

---

### Esercizio 3

```python
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(f"({i},{j})", end=" ")
    print()
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
(0,1) (0,2)
(1,0) (1,2)
(2,0) (2,1)
```

**Spiegazione:** Abbiamo due cicli annidati. `continue` **salta** il resto dell'iterazione corrente (del ciclo piu interno) e passa alla successiva. Quando `i == j` (cioe sulla "diagonale"), la coppia non viene stampata. Per `i=0`: si salta `j=0`, si stampano `(0,1)` e `(0,2)`. E cosi via per le altre righe.
</details>

---

### Esercizio 4

```python
numeri = [10, 25, 3, 47, 8, 12]
for n in numeri:
    if n > 30:
        print(f"Trovato: {n}")
        break
else:
    print("Nessun numero maggiore di 30")
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
Trovato: 47
```

**Spiegazione:** Il ciclo scorre la lista e, quando trova `47 > 30`, stampa il messaggio e interrompe il ciclo con `break`. Il blocco `else` di un `for` viene eseguito **solo** se il ciclo termina normalmente (senza `break`). Siccome qui `break` viene eseguito, l'`else` viene saltato.
</details>

---

## Trova l'errore

### Esercizio 5

Il codice dovrebbe stampare i numeri da 1 a 10, ma ne stampa uno in meno. Perche?

```python
for i in range(1, 10):
    print(i)
```

<details>
<summary>Mostra la risposta</summary>

**Output prodotto:** numeri da 1 a **9** (manca il 10).

**Problema:** In `range(1, 10)` il valore di stop `10` e **escluso**. Questo e l'errore **off-by-one**, uno dei piu comuni in programmazione.

**Soluzione:**
```python
for i in range(1, 11):   # 11 escluso → ultimo valore è 10
    print(i)
```

Regola pratica: se vuoi arrivare fino a `n` incluso, usa `range(start, n + 1)`.
</details>

---

### Esercizio 6

Il codice dovrebbe contare alla rovescia da 5 a 1, ma va in loop infinito. Perche?

```python
n = 5
while n > 0:
    print(n)
```

<details>
<summary>Mostra la risposta</summary>

**Problema:** La variabile `n` non viene mai modificata all'interno del ciclo. Siccome `n` resta sempre `5`, la condizione `n > 0` e sempre `True`, creando un **ciclo infinito**.

**Soluzione:**
```python
n = 5
while n > 0:
    print(n)
    n = n - 1    # oppure: n -= 1
```

Con i cicli `while`, bisogna **sempre** assicurarsi che la condizione possa diventare `False` a un certo punto, altrimenti il programma non termina mai.
</details>

---

### Esercizio 7

Il codice dovrebbe calcolare la somma dei numeri da 1 a 5, ma il risultato e sbagliato.

```python
for i in range(1, 6):
    totale = 0
    totale = totale + i
print(f"Somma: {totale}")
```

<details>
<summary>Mostra la risposta</summary>

**Output prodotto:** `Somma: 5`

**Problema:** L'inizializzazione `totale = 0` e **dentro** il ciclo: a ogni iterazione, `totale` viene azzerato prima di sommare `i`. Alla fine, `totale` contiene solo l'ultimo valore (`5`).

**Soluzione:**
```python
totale = 0                 # inizializzazione FUORI dal ciclo
for i in range(1, 6):
    totale = totale + i
print(f"Somma: {totale}")  # stampa: Somma: 15
```

Nel pattern accumulatore, l'inizializzazione deve stare **prima** del ciclo, non dentro.
</details>

---

## Completa il codice

### Esercizio 8

Completa la funzione che calcola la somma dei numeri **pari** in un intervallo.

```python
def somma_pari(inizio, fine):
    """Somma i numeri pari da inizio a fine (inclusi).

    Esempio: somma_pari(1, 10) deve restituire 30
    (perché 2 + 4 + 6 + 8 + 10 = 30)
    """
    totale = ___
    for n in range(inizio, _________):
        if _____________:
            totale = _______________
    return totale
```

<details>
<summary>Mostra la risposta</summary>

```python
def somma_pari(inizio, fine):
    """Somma i numeri pari da inizio a fine (inclusi)."""
    totale = 0
    for n in range(inizio, fine + 1):
        if n % 2 == 0:
            totale = totale + n
    return totale
```

**Spiegazione:** Inizializziamo `totale` a `0` (elemento neutro della somma). Usiamo `fine + 1` nel range perche vogliamo includere `fine`. A ogni iterazione, controlliamo se `n` e pari con `n % 2 == 0` (il resto della divisione per 2 e zero). Se si, lo aggiungiamo al totale.
</details>

---

### Esercizio 9

Completa la funzione che trova il primo multiplo di `k` in una lista.

```python
def primo_multiplo(numeri, k):
    """Restituisce il primo multiplo di k nella lista, oppure None.

    Esempio: primo_multiplo([3, 7, 12, 5, 9], 4) → 12
    Esempio: primo_multiplo([3, 7, 5], 4) → None
    """
    for n in ___________:
        if _______________:
            return ___
    return ________
```

<details>
<summary>Mostra la risposta</summary>

```python
def primo_multiplo(numeri, k):
    """Restituisce il primo multiplo di k nella lista, oppure None."""
    for n in numeri:
        if n % k == 0:
            return n
    return None
```

**Spiegazione:** Scorriamo la lista con un `for`. Appena troviamo un numero divisibile per `k` (cioe `n % k == 0`), lo restituiamo subito con `return` (che interrompe anche il ciclo). Se il ciclo finisce senza trovare nulla, restituiamo `None`, il valore speciale di Python che indica "nessun risultato".
</details>

---

### Esercizio 10

Completa la funzione che conta quante volte un carattere appare in una stringa.

```python
def conta_carattere(testo, carattere):
    """Conta le occorrenze di un carattere nel testo.

    Esempio: conta_carattere("banana", "a") deve restituire 3
    """
    contatore = ___
    for c in ________:
        if ___________:
            contatore _________
    return contatore
```

<details>
<summary>Mostra la risposta</summary>

```python
def conta_carattere(testo, carattere):
    """Conta le occorrenze di un carattere nel testo."""
    contatore = 0
    for c in testo:
        if c == carattere:
            contatore += 1
    return contatore
```

**Spiegazione:** Questo e un altro esempio di pattern accumulatore, questa volta per **contare**. Inizializziamo il contatore a `0`. Scorriamo ogni carattere `c` della stringa `testo` (le stringhe in Python sono iterabili). Se `c` corrisponde al carattere cercato, incrementiamo il contatore. Nota: `contatore += 1` e una scorciatoia per `contatore = contatore + 1`.
</details>
