# Autovalutazione — T12: Dizionari e Insiemi

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
voti = {"Alice": 28, "Bob": 30, "Carla": 25}
print(voti.get("Diana", "non trovato"))
print(voti.get("Alice", 0))
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
non trovato
28
```

**Spiegazione:** Il metodo `.get(chiave, valore_default)` restituisce il valore associato alla chiave se questa esiste nel dizionario, altrimenti restituisce il valore di default. `"Diana"` non esiste, quindi viene restituito `"non trovato"`. `"Alice"` esiste con valore `28`, quindi viene restituito `28` (il default `0` viene ignorato).
</details>

---

### Esercizio 2

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)
print(A & B)
print(A - B)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
{1, 2, 3, 4, 5, 6}
{3, 4}
{1, 2}
```

**Spiegazione:**
- `A | B` calcola l'**unione**: tutti gli elementi presenti in almeno uno dei due insiemi.
- `A & B` calcola l'**intersezione**: solo gli elementi presenti in entrambi.
- `A - B` calcola la **differenza**: gli elementi di `A` che non sono in `B`.
</details>

---

### Esercizio 3

```python
d1 = {"x": [1, 2, 3]}
d2 = d1
d2["x"].append(4)
print(d1["x"])
print(d1 is d2)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
[1, 2, 3, 4]
True
```

**Spiegazione:** L'assegnamento `d2 = d1` **non** crea una copia del dizionario: `d1` e `d2` sono due nomi che puntano allo **stesso oggetto** in memoria (aliasing). Modificare la lista tramite `d2["x"]` modifica lo stesso oggetto visibile anche tramite `d1["x"]`. L'operatore `is` conferma che si tratta dello stesso identico oggetto.
</details>

---

### Esercizio 4

```python
parole = "ciao come ciao stai ciao".split()
contatore = {}
for p in parole:
    contatore[p] = contatore.get(p, 0) + 1
print(contatore)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
{'ciao': 3, 'come': 1, 'stai': 1}
```

**Spiegazione:** Per ogni parola, `.get(p, 0)` restituisce il conteggio attuale (o `0` se la parola non e' ancora nel dizionario), poi aggiunge 1. Questo e' un pattern molto comune per contare le frequenze. La parola `"ciao"` appare 3 volte, `"come"` e `"stai"` una volta ciascuna.
</details>

---

## Trova l'errore

### Esercizio 5

```python
studente = {"nome": "Luca", "eta": 20}
print(studente["matricola"])
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `KeyError: 'matricola'`

**Problema:** Accedere a una chiave inesistente con `[]` causa un `KeyError`.

**Correzione:**
```python
studente = {"nome": "Luca", "eta": 20}
# Usare .get() con un valore di default
print(studente.get("matricola", "non disponibile"))
```

**Lezione:** Quando non siete sicuri che una chiave esista, usate `.get()` con un valore di default, oppure controllate prima con `if "matricola" in studente:`.
</details>

---

### Esercizio 6

```python
# Vogliamo creare un insieme di liste
gruppi = {[1, 2], [3, 4], [5, 6]}
print(gruppi)
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `TypeError: unhashable type: 'list'`

**Problema:** Gli insiemi (`set`) possono contenere solo elementi **hashable** (immutabili). Le liste sono mutabili e quindi non possono essere inserite in un insieme.

**Correzione:**
```python
# Usare tuple al posto delle liste
gruppi = {(1, 2), (3, 4), (5, 6)}
print(gruppi)
```

**Lezione:** Se avete bisogno di sequenze come elementi di un insieme (o come chiavi di un dizionario), usate le **tuple**, che sono immutabili e quindi hashable.
</details>

---

### Esercizio 7

```python
config_default = {"tema": "chiaro", "lingua": "it", "opzioni": [1, 2]}
config_utente = config_default  # "copia" per l'utente
config_utente["tema"] = "scuro"
config_utente["opzioni"].append(3)

print("Default:", config_default)
print("Utente:", config_utente)
```

<details>
<summary>Mostra la risposta</summary>

**Problema:** Entrambi i `print` mostrano le stesse modifiche, perche' `config_utente` e `config_default` puntano allo stesso dizionario (aliasing).

**Output indesiderato:**
```
Default: {'tema': 'scuro', 'lingua': 'it', 'opzioni': [1, 2, 3]}
Utente: {'tema': 'scuro', 'lingua': 'it', 'opzioni': [1, 2, 3]}
```

**Correzione:**
```python
import copy
config_default = {"tema": "chiaro", "lingua": "it", "opzioni": [1, 2]}
# Usare copy.deepcopy per creare una copia indipendente
config_utente = copy.deepcopy(config_default)
config_utente["tema"] = "scuro"
config_utente["opzioni"].append(3)

print("Default:", config_default)
# Output: Default: {'tema': 'chiaro', 'lingua': 'it', 'opzioni': [1, 2]}
print("Utente:", config_utente)
# Output: Utente: {'tema': 'scuro', 'lingua': 'it', 'opzioni': [1, 2, 3]}
```

**Lezione:** Per copiare un dizionario che contiene oggetti mutabili (come liste), usate `copy.deepcopy()`. Il semplice `dict.copy()` crea solo una copia superficiale.
</details>

---

## Completa il codice

### Esercizio 8

Completa la funzione che conta la frequenza di ogni parola in una frase.

```python
def conta_frequenze(frase):
    """Restituisce un dizionario con la frequenza di ogni parola."""
    parole = frase.lower().split()
    frequenze = {}
    for parola in parole:
        # --- COMPLETA QUI ---
        pass
        # --------------------
    return frequenze

# Test
risultato = conta_frequenze("il gatto e il cane e il pesce")
print(risultato)
# Output atteso: {'il': 3, 'gatto': 1, 'e': 2, 'cane': 1, 'pesce': 1}
```

<details>
<summary>Mostra la soluzione</summary>

```python
def conta_frequenze(frase):
    """Restituisce un dizionario con la frequenza di ogni parola."""
    parole = frase.lower().split()
    frequenze = {}
    for parola in parole:
        frequenze[parola] = frequenze.get(parola, 0) + 1
    return frequenze

risultato = conta_frequenze("il gatto e il cane e il pesce")
print(risultato)
# Output: {'il': 3, 'gatto': 1, 'e': 2, 'cane': 1, 'pesce': 1}
```

**Spiegazione:** Usiamo il pattern `.get(parola, 0) + 1` per incrementare il contatore. Se la parola non esiste ancora nel dizionario, `.get()` restituisce `0`, e aggiungiamo `1`. Se esiste gia', restituisce il valore attuale e aggiungiamo `1`.
</details>

---

### Esercizio 9

Completa la funzione che trova gli studenti iscritti a entrambi i corsi.

```python
def studenti_in_comune(corso_A, corso_B):
    """
    Riceve due liste di nomi di studenti.
    Restituisce un insieme con i nomi presenti in entrambi i corsi.
    """
    # --- COMPLETA QUI ---
    pass
    # --------------------

# Test
statistica = ["Alice", "Bob", "Carla", "Diana"]
informatica = ["Bob", "Eva", "Carla", "Franco"]
print(studenti_in_comune(statistica, informatica))
# Output atteso: {'Bob', 'Carla'}
```

<details>
<summary>Mostra la soluzione</summary>

```python
def studenti_in_comune(corso_A, corso_B):
    """
    Riceve due liste di nomi di studenti.
    Restituisce un insieme con i nomi presenti in entrambi i corsi.
    """
    insieme_A = set(corso_A)
    insieme_B = set(corso_B)
    return insieme_A & insieme_B

statistica = ["Alice", "Bob", "Carla", "Diana"]
informatica = ["Bob", "Eva", "Carla", "Franco"]
print(studenti_in_comune(statistica, informatica))
# Output: {'Bob', 'Carla'}
```

**Spiegazione:** Convertiamo le due liste in insiemi con `set()`, poi usiamo l'operatore `&` per calcolare l'intersezione, cioe' gli elementi presenti in entrambi. In alternativa si poteva usare `insieme_A.intersection(insieme_B)`.
</details>
