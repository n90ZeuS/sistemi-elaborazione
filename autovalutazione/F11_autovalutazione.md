# Autovalutazione — F11: Indici, Slicing, Copie e Tuple

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
frutti = ["mela", "banana", "ciliegia", "dattero", "fico"]
print(frutti[-1])
print(frutti[-2])
print(frutti[1])
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
fico
dattero
banana
```

**Spiegazione:** Gli **indici negativi** contano dalla fine della lista: `-1` e l'ultimo elemento, `-2` il penultimo, e cosi via. Quindi `frutti[-1]` e `"fico"`, `frutti[-2]` e `"dattero"`. L'indice positivo `1` accede al secondo elemento (si conta da `0`): `"banana"`.
</details>

---

### Esercizio 2

```python
numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeri[2:5])
print(numeri[:3])
print(numeri[7:])
print(numeri[::2])
print(numeri[1:8:3])
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
[2, 3, 4]
[0, 1, 2]
[7, 8, 9]
[0, 2, 4, 6, 8]
[1, 4, 7]
```

**Spiegazione:** Lo slicing ha la sintassi `lista[start:stop:step]`, dove `stop` e sempre **escluso**.
- `[2:5]` → elementi agli indici 2, 3, 4.
- `[:3]` → dall'inizio fino all'indice 2 (3 escluso).
- `[7:]` → dall'indice 7 fino alla fine.
- `[::2]` → dall'inizio alla fine, con passo 2 (un elemento si e uno no).
- `[1:8:3]` → indici 1, 4, 7 (da 1 a 7, con passo 3).
</details>

---

### Esercizio 3

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
print(a is b)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
[1, 2, 3, 4]
[1, 2, 3, 4]
True
```

**Spiegazione:** `b = a` **non crea una copia** della lista. Crea un **alias**: `a` e `b` sono due nomi per lo **stesso oggetto** in memoria. Modificare la lista tramite `b` la modifica anche tramite `a`, perche e la stessa lista. L'operatore `is` conferma che sono lo stesso identico oggetto (`True`).
</details>

---

### Esercizio 4

```python
coordinate = (10, 20)
x, y = coordinate
print(f"x={x}, y={y}")

studente = ("Luca", "Informatica", 27.5)
nome, corso, media = studente
print(f"{nome} — {corso} — media: {media}")
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
x=10, y=20
Luca — Informatica — media: 27.5
```

**Spiegazione:** Il **tuple unpacking** permette di assegnare ogni elemento di una tupla a una variabile separata in un'unica istruzione. Il numero di variabili a sinistra deve corrispondere al numero di elementi nella tupla. E un modo compatto e leggibile per estrarre valori da strutture dati.
</details>

---

## Trova l'errore

### Esercizio 5

Il programmatore pensa di lavorare su una copia della lista, ma modifica l'originale.

```python
originale = [1, 2, 3, 4, 5]
copia = originale
copia.append(6)
print(f"Originale: {originale}")
print(f"Copia: {copia}")
```

<details>
<summary>Mostra la risposta</summary>

**Output prodotto:**
```
Originale: [1, 2, 3, 4, 5, 6]
Copia: [1, 2, 3, 4, 5, 6]
```

**Problema:** `copia = originale` non crea una copia! Crea solo un secondo nome (alias) per la stessa lista. Ogni modifica a `copia` si riflette su `originale` e viceversa.

**Soluzione:**
```python
originale = [1, 2, 3, 4, 5]
copia = originale[:]         # slicing crea una NUOVA lista (shallow copy)
# oppure: copia = list(originale)
# oppure: copia = originale.copy()
copia.append(6)
print(f"Originale: {originale}")  # [1, 2, 3, 4, 5]
print(f"Copia: {copia}")          # [1, 2, 3, 4, 5, 6]
```

Per creare una vera copia, usare lo slicing `[:]`, `list()` o il metodo `.copy()`.
</details>

---

### Esercizio 6

Il codice dovrebbe ordinare e stampare la lista, ma il risultato e inatteso.

```python
numeri = [5, 2, 8, 1, 9]
ordinati = numeri.sort()
print(ordinati)
```

<details>
<summary>Mostra la risposta</summary>

**Output prodotto:**
```
None
```

**Problema:** Il metodo `sort()` ordina la lista **in-place** (cioe modifica la lista originale) e restituisce `None`. Quindi `ordinati` contiene `None`, non la lista ordinata. Intanto, `numeri` e stato ordinato ma nessuno lo stampa.

**Soluzione:**
```python
# Opzione 1: usare sort() e poi la lista originale
numeri = [5, 2, 8, 1, 9]
numeri.sort()
print(numeri)              # [1, 2, 5, 8, 9]

# Opzione 2: usare sorted() che restituisce una NUOVA lista
numeri = [5, 2, 8, 1, 9]
ordinati = sorted(numeri)
print(ordinati)            # [1, 2, 5, 8, 9]
print(numeri)              # [5, 2, 8, 1, 9] — non modificata
```

`sort()` modifica e restituisce `None`; `sorted()` non modifica e restituisce la nuova lista.
</details>

---

### Esercizio 7

Il codice dovrebbe accedere all'ultimo elemento, ma causa un errore.

```python
voti = [28, 30, 25]
ultimo = voti[3]
print(ultimo)
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `IndexError: list index out of range`

**Problema:** La lista ha 3 elementi, con indici `0`, `1`, `2`. L'indice `3` non esiste. Questo e un classico errore "off-by-one": con 3 elementi, l'ultimo indice valido e `2` (cioe `len(voti) - 1`).

**Soluzione:**
```python
voti = [28, 30, 25]
ultimo = voti[2]    # indice esplicito
# oppure, più robusto:
ultimo = voti[-1]   # indice negativo: sempre l'ultimo elemento
print(ultimo)       # stampa: 25
```

Usare `voti[-1]` e il modo piu sicuro e pythonico per accedere all'ultimo elemento, perche funziona indipendentemente dalla lunghezza della lista.
</details>

---

## Completa il codice

### Esercizio 8

Completa la funzione che inverte una lista usando lo slicing.

```python
def inverti_lista(lista):
    """Restituisce una NUOVA lista con gli elementi in ordine inverso.

    Esempio: inverti_lista([1, 2, 3, 4, 5]) → [5, 4, 3, 2, 1]
    Non deve modificare la lista originale.
    """
    return lista[_______]
```

<details>
<summary>Mostra la risposta</summary>

```python
def inverti_lista(lista):
    """Restituisce una nuova lista con gli elementi in ordine inverso."""
    return lista[::-1]
```

**Spiegazione:** Lo slicing `[::-1]` significa "dall'inizio alla fine, con passo -1", cioe percorrendo la lista al contrario. Questo crea una **nuova** lista (non modifica l'originale). E uno degli idiomi piu usati in Python. Ricorda la sintassi completa: `lista[start:stop:step]` — quando `start` e `stop` sono omessi, si intende tutta la lista.
</details>

---

### Esercizio 9

Completa la funzione che usa il tuple unpacking per elaborare dati di studenti.

```python
def migliore_studente(studenti):
    """Riceve una lista di tuple (nome, media) e restituisce il nome
    dello studente con la media più alta.

    Esempio: migliore_studente([("Alice", 28.5), ("Bob", 26.0), ("Carol", 29.3)])
    deve restituire "Carol"
    """
    miglior_nome = ________
    miglior_media = ________

    for ________, ________ in studenti:
        if media ______ miglior_media:
            miglior_nome = ________
            miglior_media = ________

    return miglior_nome
```

<details>
<summary>Mostra la risposta</summary>

```python
def migliore_studente(studenti):
    """Restituisce il nome dello studente con la media più alta."""
    miglior_nome = ""
    miglior_media = -1

    for nome, media in studenti:
        if media > miglior_media:
            miglior_nome = nome
            miglior_media = media

    return miglior_nome
```

**Spiegazione:** Inizializziamo `miglior_media` a `-1` (un valore che qualsiasi media reale superera). Nel ciclo `for`, il **tuple unpacking** `nome, media` estrae automaticamente i due valori da ogni tupla. A ogni iterazione, se la media corrente e maggiore della migliore trovata finora, aggiorniamo sia il nome che la media. Questo e il **pattern accumulatore** applicato alla ricerca del massimo.
</details>

---

### Esercizio 10

Completa la funzione che estrae una sotto-lista e ne crea una copia indipendente.

```python
def estrai_centrali(lista):
    """Restituisce una COPIA degli elementi centrali (esclude il primo e l'ultimo).
    La copia deve essere indipendente dalla lista originale.

    Esempio: estrai_centrali([10, 20, 30, 40, 50]) → [20, 30, 40]
    """
    return _________________
```

<details>
<summary>Mostra la risposta</summary>

```python
def estrai_centrali(lista):
    """Restituisce una copia degli elementi centrali."""
    return lista[1:-1]
```

**Spiegazione:** Lo slicing `[1:-1]` prende gli elementi dall'indice `1` (secondo elemento) fino all'indice `-1` escluso (cioe esclude l'ultimo). Lo slicing crea sempre una **nuova** lista, quindi il risultato e gia una copia indipendente dall'originale. Modificare la lista restituita non influenzera la lista originale.
</details>
