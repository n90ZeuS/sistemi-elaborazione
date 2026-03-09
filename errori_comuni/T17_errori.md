# Errori comuni — T17: NumPy, Pandas e visualizzazione

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione T17.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

---

### Errore 1: Shape mismatch nelle operazioni tra array NumPy

**Codice errato:**
```python
import numpy as np

voti = np.array([28, 30, 25, 27])       # shape (4,)
pesi = np.array([0.3, 0.3, 0.4])        # shape (3,)

media_pesata = np.sum(voti * pesi)
```

**Cosa succede:**
```
ValueError: operands could not be broadcast together with shapes (4,) (3,)
```

**Perché è sbagliato:** Le operazioni elemento per elemento tra array NumPy richiedono che gli array abbiano dimensioni compatibili. Un array di 4 elementi non può essere moltiplicato per uno di 3 elementi: NumPy non sa come allinearli. Bisogna assicurarsi che gli array abbiano la stessa shape.

**Codice corretto:**
```python
import numpy as np

voti = np.array([28, 30, 25, 27])             # shape (4,)
pesi = np.array([0.2, 0.3, 0.2, 0.3])        # shape (4,) — stesso numero di elementi

media_pesata = np.sum(voti * pesi)
print(f"Media pesata: {media_pesata}")  # Media pesata: 27.6

# Verifica sempre le dimensioni:
print(voti.shape, pesi.shape)  # (4,) (4,)
```

**Regola da ricordare:** Prima di fare operazioni tra array NumPy, controlla che le shape siano compatibili con `.shape`: devono avere le stesse dimensioni o essere compatibili con il broadcasting.

---

### Errore 2: Confondere accesso a colonne e righe in un DataFrame Pandas

**Codice errato:**
```python
import pandas as pd

df = pd.DataFrame({
    "nome": ["Luca", "Anna", "Marco"],
    "voto": [28, 30, 25],
    "lode": [False, True, False]
})

# Lo studente prova ad accedere a una riga con la sintassi delle colonne
prima_riga = df["Luca"]
```

**Cosa succede:**
```
KeyError: 'Luca'
```

**Perché è sbagliato:** `df["nome_colonna"]` accede a una colonna del DataFrame, non a una riga. Per accedere alle righe bisogna usare `.loc[]` (per etichetta) o `.iloc[]` (per posizione numerica). "Luca" è un valore contenuto nella colonna "nome", non è un'etichetta di riga né un nome di colonna.

**Codice corretto:**
```python
import pandas as pd

df = pd.DataFrame({
    "nome": ["Luca", "Anna", "Marco"],
    "voto": [28, 30, 25],
    "lode": [False, True, False]
})

# Accesso a una colonna
colonna_voti = df["voto"]

# Accesso a una riga per posizione (indice numerico)
prima_riga = df.iloc[0]

# Accesso a righe con una condizione
riga_luca = df[df["nome"] == "Luca"]
print(riga_luca)
```

**Regola da ricordare:** Usa `df["colonna"]` per le colonne, `df.iloc[indice]` per le righe per posizione e `df.loc[etichetta]` per le righe per etichetta.

---

### Errore 3: Promozione di tipo inattesa (dtype promotion) in NumPy

**Codice errato:**
```python
import numpy as np

voti = np.array([28, 30, 25, 27])
print(voti.dtype)  # int64

# Lo studente aggiunge un valore mancante
voti_con_mancante = np.append(voti, np.nan)
print(voti_con_mancante)
print(voti_con_mancante.dtype)
```

**Cosa succede:**
```
int64
[28. 30. 25. 27. nan]
float64
```
L'array è diventato di tipo `float64` senza preavviso. I valori `28` sono diventati `28.0`.

**Perché è sbagliato:** `np.nan` è un valore float speciale che non esiste nel tipo intero. Quando si aggiunge `nan` a un array di interi, NumPy promuove automaticamente tutto l'array a `float64` per poter contenere il `nan`. Questo può causare problemi in calcoli successivi che si aspettano numeri interi.

**Codice corretto:**
```python
import numpy as np
import pandas as pd

# Opzione 1: usare un array float fin dall'inizio se ci sono dati mancanti
voti = np.array([28, 30, 25, 27], dtype=float)
voti_con_mancante = np.append(voti, np.nan)

# Opzione 2: usare Pandas che gestisce meglio i dati mancanti
voti_series = pd.array([28, 30, 25, 27, pd.NA], dtype=pd.Int64Dtype())
print(voti_series)  # [28, 30, 25, 27, <NA>] — mantiene il tipo intero
```

**Regola da ricordare:** `np.nan` è un float: inserirlo in un array di interi ne cambia il tipo automaticamente; se prevedi valori mancanti, usa `float` oppure Pandas con `pd.Int64Dtype()`.

---

### Errore 4: Il grafico non viene mostrato (manca `plt.show()`)

**Codice errato:**
```python
import matplotlib.pyplot as plt

voti = [28, 30, 25, 27, 22, 30, 26]
plt.hist(voti, bins=5)
plt.title("Distribuzione dei voti")
plt.xlabel("Voto")
plt.ylabel("Frequenza")
# manca plt.show()
```

**Cosa succede:**
```
(nessun output visibile — il grafico non appare)
In uno script Python (.py) eseguito dal terminale, la finestra del grafico
non si apre e non si vede nulla.
```

**Perché è sbagliato:** In uno script Python eseguito da terminale, `matplotlib` accumula le istruzioni di disegno ma non mostra il grafico finché non si chiama `plt.show()`. Senza questa chiamata il grafico viene costruito in memoria ma non viene mai visualizzato. (Nota: in Jupyter Notebook con `%matplotlib inline` il grafico appare automaticamente, ma è buona pratica includere comunque `plt.show()`.)

**Codice corretto:**
```python
import matplotlib.pyplot as plt

voti = [28, 30, 25, 27, 22, 30, 26]
plt.hist(voti, bins=5)
plt.title("Distribuzione dei voti")
plt.xlabel("Voto")
plt.ylabel("Frequenza")
plt.show()  # mostra il grafico

# Per salvare il grafico su file:
# plt.savefig("distribuzione_voti.png", dpi=150)  # prima di plt.show()
```

**Regola da ricordare:** Chiama sempre `plt.show()` alla fine delle istruzioni di disegno per visualizzare il grafico, soprattutto negli script eseguiti da terminale.

---

### Errore 5: Usare `and`/`or` di Python invece di `&`/`|` con array e DataFrame

**Codice errato:**
```python
import pandas as pd

df = pd.DataFrame({
    "nome": ["Luca", "Anna", "Marco", "Sara"],
    "voto": [28, 30, 25, 30],
    "lode": [False, True, False, True]
})

# Lo studente filtra con 'and' di Python
bravi = df[df["voto"] >= 28 and df["lode"] == True]
```

**Cosa succede:**
```
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(),
a.item(), a.any() or a.all().
```

**Perché è sbagliato:** `and` e `or` sono operatori logici di Python che funzionano su singoli valori booleani. Quando si lavora con colonne Pandas o array NumPy, ogni confronto produce una Serie di valori booleani (uno per ogni riga). Python non sa come ridurre una serie intera a un singolo `True`/`False`. Bisogna usare gli operatori elemento per elemento `&` (and) e `|` (or), racchiudendo ogni condizione tra parentesi.

**Codice corretto:**
```python
import pandas as pd

df = pd.DataFrame({
    "nome": ["Luca", "Anna", "Marco", "Sara"],
    "voto": [28, 30, 25, 30],
    "lode": [False, True, False, True]
})

# Usa & invece di 'and', con parentesi obbligatorie
bravi = df[(df["voto"] >= 28) & (df["lode"] == True)]
print(bravi)
#   nome  voto  lode
# 1  Anna    30  True
# 3  Sara    30  True

# Per 'or' usa |
sufficienti = df[(df["voto"] >= 28) | (df["lode"] == True)]
```

**Regola da ricordare:** Con Pandas e NumPy usa `&` al posto di `and` e `|` al posto di `or`, mettendo ogni condizione tra parentesi tonde.

---

### Errore 6: Index non resettato dopo un filtro in Pandas

**Codice errato:**
```python
import pandas as pd

df = pd.DataFrame({
    "nome": ["Luca", "Anna", "Marco", "Sara", "Giulia"],
    "voto": [28, 30, 25, 30, 22]
})

# Filtra solo chi ha voto >= 28
bravi = df[df["voto"] >= 28]
print(bravi)
print()

# Lo studente prova ad accedere per posizione
for i in range(len(bravi)):
    print(bravi.iloc[i]["nome"])  # funziona, ma...

# ...poi prova con .loc usando la posizione
print(bravi.loc[2])  # pensando di prendere il "terzo" studente
```

**Cosa succede:**
```
   nome  voto
0  Luca    28
1  Anna    30
3  Sara    30

Luca
Anna
Sara
KeyError: 2
```
L'indice 2 (Marco) è stato rimosso dal filtro, ma gli indici originali 0, 1, 3 sono rimasti.

**Perché è sbagliato:** Quando si filtra un DataFrame, il risultato mantiene gli indici originali. Il DataFrame filtrato ha indici `[0, 1, 3]`, non `[0, 1, 2]`. Usare `.loc[2]` cerca l'indice con etichetta `2`, che non esiste nel DataFrame filtrato.

**Codice corretto:**
```python
import pandas as pd

df = pd.DataFrame({
    "nome": ["Luca", "Anna", "Marco", "Sara", "Giulia"],
    "voto": [28, 30, 25, 30, 22]
})

bravi = df[df["voto"] >= 28].reset_index(drop=True)
print(bravi)
#    nome  voto
# 0  Luca    28
# 1  Anna    30
# 2  Sara    30

# Ora gli indici sono 0, 1, 2 e l'accesso è prevedibile
print(bravi.loc[2])  # Sara, voto 30
```

**Regola da ricordare:** Dopo un filtro su un DataFrame, usa `.reset_index(drop=True)` per riallineare gli indici da 0 ed evitare `KeyError` con `.loc[]`.

---
