# Autovalutazione — F13: Funzioni — Scope, Return e Buone Pratiche

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
x = 10

def modifica():
    x = 20
    print("Dentro:", x)

modifica()
print("Fuori:", x)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
Dentro: 20
Fuori: 10
```

**Spiegazione:** Quando assegniamo `x = 20` dentro la funzione, Python crea una variabile **locale** che esiste solo all'interno di `modifica()`. La variabile globale `x` rimane invariata a `10`. Questo e' il principio dello **scope**: le variabili definite dentro una funzione sono locali e non modificano quelle esterne con lo stesso nome.
</details>

---

### Esercizio 2

```python
def aggiungi_elemento(valore, lista=[]):
    lista.append(valore)
    return lista

print(aggiungi_elemento(1))
print(aggiungi_elemento(2))
print(aggiungi_elemento(3))
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
[1]
[1, 2]
[1, 2, 3]
```

**Spiegazione:** Questo e' uno dei tranelli piu' famosi di Python! Il valore di default `[]` viene creato **una sola volta**, quando la funzione viene definita, non ad ogni chiamata. Quindi tutte le chiamate senza argomento `lista` condividono la **stessa lista**. Gli elementi si accumulano tra una chiamata e l'altra. Questo e' il problema dei **default mutabili**.
</details>

---

### Esercizio 3

```python
def calcola_doppio(n):
    risultato = n * 2

valore = calcola_doppio(5)
print(valore)
print(type(valore))
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
None
<class 'NoneType'>
```

**Spiegazione:** La funzione `calcola_doppio` calcola `n * 2` e lo assegna a `risultato`, ma **non ha un'istruzione `return`**. In Python, una funzione senza `return` esplicito restituisce automaticamente `None`. Il fatto che il calcolo sia corretto non basta: bisogna restituire il valore con `return risultato`.
</details>

---

### Esercizio 4

```python
contatore = 0

def incrementa():
    global contatore
    contatore += 1

incrementa()
incrementa()
incrementa()
print(contatore)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
3
```

**Spiegazione:** La parola chiave `global` dice a Python che `contatore` dentro la funzione si riferisce alla variabile globale, non a una nuova variabile locale. Senza `global`, la riga `contatore += 1` causerebbe un `UnboundLocalError`, perche' Python interpreterebbe `contatore` come variabile locale non ancora definita. Con `global`, la modifica si riflette sulla variabile esterna. Nota: l'uso di `global` e' generalmente **sconsigliato** perche' rende il codice difficile da seguire.
</details>

---

## Trova l'errore

### Esercizio 5

```python
def registra_studente(nome, corsi=[]):
    corsi.append(nome)
    return corsi

gruppo_a = registra_studente("Statistica")
gruppo_b = registra_studente("Informatica")
print("Gruppo A:", gruppo_a)
print("Gruppo B:", gruppo_b)
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** Entrambi i gruppi mostrano `['Statistica', 'Informatica']` invece di essere liste separate.

**Problema:** Il default mutabile `[]` viene condiviso tra tutte le chiamate. `gruppo_a` e `gruppo_b` puntano alla stessa lista.

**Correzione:**
```python
def registra_studente(nome, corsi=None):
    if corsi is None:
        corsi = []
    corsi.append(nome)
    return corsi

gruppo_a = registra_studente("Statistica")
gruppo_b = registra_studente("Informatica")
print("Gruppo A:", gruppo_a)  # ['Statistica']
print("Gruppo B:", gruppo_b)  # ['Informatica']
```

**Lezione:** Non usate mai oggetti mutabili (liste, dizionari, insiemi) come valori di default. Usate `None` e create l'oggetto dentro la funzione.
</details>

---

### Esercizio 6

```python
x = 100

def mostra():
    print(x)
    x = 200

mostra()
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `UnboundLocalError: cannot access local variable 'x' where it is not associated with a value`

**Problema:** Python analizza l'intera funzione **prima** di eseguirla. Vede che `x = 200` esiste, quindi considera `x` come variabile locale. Ma il `print(x)` avviene **prima** dell'assegnamento, quando `x` locale non ha ancora un valore. Questo si chiama **shadowing** della variabile globale.

**Correzione (opzione 1 — leggere solo la globale):**
```python
x = 100

def mostra():
    print(x)  # Legge la variabile globale

mostra()  # Stampa: 100
```

**Correzione (opzione 2 — se serve modificare):**
```python
x = 100

def mostra():
    global x
    print(x)
    x = 200

mostra()  # Stampa: 100, poi x diventa 200
```

**Lezione:** Se una variabile viene assegnata in qualsiasi punto della funzione, Python la considera locale nell'intera funzione.
</details>

---

### Esercizio 7

```python
def media(numeri):
    """Calcola la media di una lista di numeri."""
    somma = sum(numeri)
    n = len(numeri)
    media = somma / n

risultato = media([10, 20, 30])
print(f"La media e': {risultato}")
```

<details>
<summary>Mostra la risposta</summary>

**Output indesiderato:**
```
La media e': None
```

**Problema:** La funzione calcola correttamente la media ma **dimentica il `return`**. Senza `return`, la funzione restituisce `None`.

**Correzione:**
```python
def media(numeri):
    """Calcola la media di una lista di numeri."""
    somma = sum(numeri)
    n = len(numeri)
    return somma / n

risultato = media([10, 20, 30])
print(f"La media e': {risultato}")
# Output: La media e': 20.0
```

**Lezione:** Controllate sempre che le vostre funzioni abbiano un `return` esplicito se devono restituire un valore. Il `return` implicito (`None`) e' una fonte comune di bug.
</details>

---

## Completa il codice

### Esercizio 8

Completa la funzione con una docstring appropriata, gestione corretta dei default e un `return` esplicito.

```python
def statistiche_base(dati):
    # --- COMPLETA: aggiungi una docstring ---

    if not dati:
        # --- COMPLETA: cosa restituire se la lista e' vuota? ---
        pass

    media = sum(dati) / len(dati)
    minimo = min(dati)
    massimo = max(dati)

    # --- COMPLETA: restituisci i tre valori come dizionario ---
    pass

# Test
print(statistiche_base([4, 8, 15, 16, 23, 42]))
# Output atteso: {'media': 18.0, 'minimo': 4, 'massimo': 42}
print(statistiche_base([]))
# Output atteso: None
```

<details>
<summary>Mostra la soluzione</summary>

```python
def statistiche_base(dati):
    """Calcola media, minimo e massimo di una lista di numeri.

    Args:
        dati: lista di numeri.

    Returns:
        Dizionario con chiavi 'media', 'minimo', 'massimo',
        oppure None se la lista e' vuota.
    """
    if not dati:
        return None

    media = sum(dati) / len(dati)
    minimo = min(dati)
    massimo = max(dati)

    return {"media": media, "minimo": minimo, "massimo": massimo}

print(statistiche_base([4, 8, 15, 16, 23, 42]))
# Output: {'media': 18.0, 'minimo': 4, 'massimo': 42}
print(statistiche_base([]))
# Output: None
```

**Spiegazione:** La docstring descrive cosa fa la funzione, i parametri e il valore restituito. Il `return None` nel caso di lista vuota e' esplicito per chiarezza. Il dizionario finale raccoglie i tre risultati con chiavi descrittive.
</details>

---

### Esercizio 9

Completa la funzione evitando il problema del default mutabile.

```python
def aggiungi_voto(studente, voto, registro=???):
    """Aggiunge un voto al registro dello studente.

    Args:
        studente: nome dello studente.
        voto: voto da aggiungere.
        registro: dizionario dei voti (opzionale).

    Returns:
        Il registro aggiornato.
    """
    # --- COMPLETA: gestisci il default in modo sicuro ---

    if studente not in registro:
        registro[studente] = []
    registro[studente].append(voto)
    return registro

# Test
r1 = aggiungi_voto("Alice", 28)
r2 = aggiungi_voto("Bob", 30)
print(r1)  # {'Alice': [28]}
print(r2)  # {'Bob': [30]}  (NON deve contenere Alice!)
```

<details>
<summary>Mostra la soluzione</summary>

```python
def aggiungi_voto(studente, voto, registro=None):
    """Aggiunge un voto al registro dello studente.

    Args:
        studente: nome dello studente.
        voto: voto da aggiungere.
        registro: dizionario dei voti (opzionale).

    Returns:
        Il registro aggiornato.
    """
    if registro is None:
        registro = {}

    if studente not in registro:
        registro[studente] = []
    registro[studente].append(voto)
    return registro

r1 = aggiungi_voto("Alice", 28)
r2 = aggiungi_voto("Bob", 30)
print(r1)  # {'Alice': [28]}
print(r2)  # {'Bob': [30]}
```

**Spiegazione:** Usiamo `None` come valore di default e creiamo un nuovo dizionario `{}` dentro la funzione ad ogni chiamata. In questo modo ogni chiamata senza argomento `registro` ottiene un dizionario indipendente. Il confronto `is None` e' preferibile a `== None` perche' e' piu' efficiente e idiomatico.
</details>
