# Autovalutazione — T17: NumPy e Pandas

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(a + b)
print(a * b)
print(a ** 2)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
[11 22 33 44]
[ 10  40  90 160]
[ 1  4  9 16]
```

**Spiegazione:** A differenza delle liste Python, le operazioni sugli array NumPy sono **elemento per elemento** (element-wise):
- `a + b` somma ogni elemento di `a` con l'elemento corrispondente di `b`.
- `a * b` moltiplica elemento per elemento.
- `a ** 2` eleva al quadrato ogni elemento.
Questo e' molto diverso dal comportamento delle liste, dove `+` concatena e `*` ripete.
</details>

---

### Esercizio 2

```python
import numpy as np

matrice = np.array([[1, 2, 3],
                    [4, 5, 6]])

print(matrice + 10)
print()
print(matrice * np.array([1, 0, 1]))
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
[[11 12 13]
 [14 15 16]]

[[1 0 3]
 [4 0 6]]
```

**Spiegazione:** Questo e' il **broadcasting** di NumPy:
- `matrice + 10`: lo scalare `10` viene "espanso" per essere sommato a ogni elemento della matrice.
- `matrice * np.array([1, 0, 1])`: l'array `[1, 0, 1]` ha 3 elementi come le colonne della matrice. Viene moltiplicato per ogni riga. La seconda colonna viene azzerata (moltiplicata per 0).
Il broadcasting permette operazioni tra array di forme diverse, seguendo regole precise.
</details>

---

### Esercizio 3

```python
import pandas as pd

dati = {"nome": ["Alice", "Bob", "Carla"],
        "voto": [28, 24, 30],
        "corso": ["Stat", "Info", "Stat"]}
df = pd.DataFrame(dati)

print(df[df["voto"] >= 27])
print()
print(df["nome"].values)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
    nome  voto corso
0  Alice    28  Stat
2  Carla    30  Stat

['Alice' 'Bob' 'Carla']
```

**Spiegazione:**
- `df["voto"] >= 27` crea una Serie booleana: `[True, False, True]`. Usata come filtro su `df`, restituisce solo le righe dove la condizione e' vera (Alice e Carla).
- `df["nome"].values` restituisce i valori della colonna "nome" come array NumPy. Notate che gli indici originali (0 e 2) vengono mantenuti nel DataFrame filtrato.
</details>

---

### Esercizio 4

```python
import numpy as np

a = np.array([1, 2, 3])
b = a
b[0] = 99
print(a)

c = a.copy()
c[1] = 88
print(a)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
[99  2  3]
[99  2  3]
```

**Spiegazione:** Come per le liste, `b = a` crea un **alias**: `a` e `b` puntano allo stesso array. Modificare `b[0]` modifica anche `a`. Invece `c = a.copy()` crea una **copia indipendente**: modificare `c[1]` non influenza `a`. Questo comportamento e' identico a quello visto con le liste Python.
</details>

---

## Trova l'errore

### Esercizio 5

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5])
c = a + b
print(c)
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `ValueError: operands could not be broadcast together with shapes (3,) (2,)`

**Problema:** Il broadcasting di NumPy ha regole precise. Due array possono essere sommati solo se le loro dimensioni sono compatibili. Un array di 3 elementi e uno di 2 elementi non sono compatibili: non c'e' modo di "allinearli" elemento per elemento.

**Correzione (dipende dall'intento):**
```python
import numpy as np

# Opzione 1: assicurarsi che abbiano la stessa lunghezza
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # [5 7 9]

# Opzione 2: usare il padding se serve
a = np.array([1, 2, 3])
b = np.array([4, 5, 0])  # aggiungiamo uno 0
print(a + b)  # [5 7 3]
```

**Lezione:** Prima di fare operazioni tra array, verificate le forme con `.shape`. Le regole del broadcasting richiedono che le dimensioni siano uguali o che una delle due sia 1.
</details>

---

### Esercizio 6

```python
import pandas as pd

df = pd.DataFrame({
    "nome": ["Alice", "Bob", "Carla"],
    "voto": [28, 24, 30]
})

# Vogliamo il voto di Bob
print(df["Bob"])
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `KeyError: 'Bob'`

**Problema:** `df["Bob"]` cerca una **colonna** chiamata "Bob", non una riga. In Pandas, `df[...]` con una stringa accede alle colonne, non alle righe.

**Correzione:**
```python
import pandas as pd

df = pd.DataFrame({
    "nome": ["Alice", "Bob", "Carla"],
    "voto": [28, 24, 30]
})

# Metodo 1: filtrare con condizione booleana
print(df[df["nome"] == "Bob"])
#   nome  voto
# 1  Bob    24

# Metodo 2: usare .loc con un indice personalizzato
df_indicizzato = df.set_index("nome")
print(df_indicizzato.loc["Bob"])
# voto    24
# Name: Bob, dtype: int64
```

**Lezione:** In Pandas, `df["..."]` seleziona **colonne**. Per selezionare **righe**, usate `df.loc[...]` (per etichette) o `df.iloc[...]` (per posizione numerica), oppure filtrate con condizioni booleane.
</details>

---

### Esercizio 7

```python
import numpy as np

interi = np.array([1, 2, 3])
risultato = np.array([1, 2, 3]) / 2
print(risultato)
print(risultato.dtype)

misto = np.array([1, 2, "tre"])
print(misto)
print(misto.dtype)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
[0.5 1.  1.5]
float64
['1' '2' 'tre']
<U21
```

**Problema illustrato (dtype promotion):**
- La divisione `/` converte automaticamente gli interi in float: il risultato e' `float64` anche se gli input erano interi.
- Quando un array contiene tipi misti (numeri e stringhe), NumPy converte **tutto** al tipo piu' generale. `1` e `2` diventano le stringhe `'1'` e `'2'`. Il dtype `<U21` significa "stringa Unicode fino a 21 caratteri".

**Attenzione:** Con l'array misto, operazioni numeriche come `misto + 1` causerebbero un errore, perche' non si puo' sommare 1 a una stringa. Assicuratevi che i vostri array contengano dati omogenei.
</details>

---

## Completa il codice

### Esercizio 8

Completa la funzione che usa NumPy per calcolare statistiche base di un dataset.

```python
import numpy as np

def statistiche_array(dati):
    """Calcola statistiche descrittive di un array numerico.

    Args:
        dati: lista o array di numeri.

    Returns:
        Dizionario con media, mediana, deviazione standard, minimo e massimo.
    """
    arr = np.array(dati)

    # --- COMPLETA: calcola le statistiche usando funzioni NumPy ---
    return {
        "media": ???,
        "mediana": ???,
        "dev_std": ???,
        "minimo": ???,
        "massimo": ???
    }

# Test
risultato = statistiche_array([4, 8, 15, 16, 23, 42])
for chiave, valore in risultato.items():
    print(f"{chiave}: {valore:.2f}")
# Output atteso:
# media: 18.00
# mediana: 15.50
# dev_std: 12.66
# minimo: 4.00
# massimo: 42.00
```

<details>
<summary>Mostra la soluzione</summary>

```python
import numpy as np

def statistiche_array(dati):
    """Calcola statistiche descrittive di un array numerico.

    Args:
        dati: lista o array di numeri.

    Returns:
        Dizionario con media, mediana, deviazione standard, minimo e massimo.
    """
    arr = np.array(dati)

    return {
        "media": np.mean(arr),
        "mediana": np.median(arr),
        "dev_std": np.std(arr),
        "minimo": np.min(arr),
        "massimo": np.max(arr)
    }

risultato = statistiche_array([4, 8, 15, 16, 23, 42])
for chiave, valore in risultato.items():
    print(f"{chiave}: {valore:.2f}")
```

**Spiegazione:** NumPy fornisce funzioni ottimizzate per le statistiche:
- `np.mean()` calcola la media aritmetica.
- `np.median()` calcola la mediana (valore centrale).
- `np.std()` calcola la deviazione standard (popolazione, non campionaria).
- `np.min()` e `np.max()` trovano il minimo e il massimo.
Queste funzioni sono molto piu' veloci dei corrispondenti Python puro su grandi dataset.
</details>

---

### Esercizio 9

Completa la funzione che crea un DataFrame e risponde a una domanda sui dati.

```python
import pandas as pd

def analisi_esami(nomi, voti, corsi):
    """Crea un DataFrame e calcola la media per corso.

    Args:
        nomi: lista di nomi studenti.
        voti: lista di voti.
        corsi: lista di nomi dei corsi.

    Returns:
        Serie Pandas con la media dei voti per ogni corso.
    """
    # --- COMPLETA: crea il DataFrame ---

    # --- COMPLETA: calcola la media raggruppando per corso ---

# Test
nomi = ["Alice", "Bob", "Carla", "Diana", "Eva", "Franco"]
voti = [28, 24, 30, 22, 27, 25]
corsi = ["Stat", "Info", "Stat", "Info", "Stat", "Info"]

risultato = analisi_esami(nomi, voti, corsi)
print(risultato)
# Output atteso:
# corso
# Info    23.666667
# Stat    28.333333
# Name: voto, dtype: float64
```

<details>
<summary>Mostra la soluzione</summary>

```python
import pandas as pd

def analisi_esami(nomi, voti, corsi):
    """Crea un DataFrame e calcola la media per corso.

    Args:
        nomi: lista di nomi studenti.
        voti: lista di voti.
        corsi: lista di nomi dei corsi.

    Returns:
        Serie Pandas con la media dei voti per ogni corso.
    """
    df = pd.DataFrame({
        "nome": nomi,
        "voto": voti,
        "corso": corsi
    })

    medie_per_corso = df.groupby("corso")["voto"].mean()
    return medie_per_corso

nomi = ["Alice", "Bob", "Carla", "Diana", "Eva", "Franco"]
voti = [28, 24, 30, 22, 27, 25]
corsi = ["Stat", "Info", "Stat", "Info", "Stat", "Info"]

risultato = analisi_esami(nomi, voti, corsi)
print(risultato)
```

**Spiegazione:**
1. `pd.DataFrame({...})` crea una tabella a partire da un dizionario dove ogni chiave diventa il nome di una colonna.
2. `df.groupby("corso")` raggruppa le righe per valore della colonna "corso".
3. `["voto"].mean()` seleziona la colonna "voto" e calcola la media per ogni gruppo.
Il risultato e' una Serie Pandas indicizzata per corso. `groupby` e' uno degli strumenti piu' potenti di Pandas per l'analisi dei dati.
</details>
