# Lezione Frontale 17 — NumPy, Pandas e visualizzazione

## Introduzione: perché servono nuovi strumenti

Nelle lezioni precedenti abbiamo imparato a programmare in Python: variabili, funzioni, cicli, classi, file, gestione degli errori. Sappiamo scrivere codice corretto e leggibile. Ma c'è un problema che finora abbiamo ignorato: Python, nella sua forma base, è *lento* per il calcolo numerico, e *scomodo* per l'analisi dei dati.

Provate a immaginare di avere un milione di osservazioni e dover calcolare la media, la deviazione standard, filtrare per una condizione, aggregare per gruppi, e infine produrre un grafico. Con le liste Python e i cicli `for` che conosciamo, servirebbero decine di righe di codice e il programma impiegherebbe secondi (o minuti) dove una soluzione ottimizzata richiede millisecondi.

L'ecosistema scientifico di Python risolve questo problema con tre librerie fondamentali: **NumPy** per il calcolo numerico veloce, **Pandas** per la manipolazione tabellare dei dati, e **Matplotlib** (con il suo compagno **Seaborn**) per la visualizzazione. Queste tre librerie formano la spina dorsale del lavoro quantitativo in Python e sono strumenti quotidiani per qualsiasi statistico, data scientist o ricercatore.

In questa lezione — la più densa del corso — le esploreremo tutte e tre, partendo dai fondamenti e arrivando a un livello sufficiente per affrontare analisi reali.

---

## 1. NumPy — il motore del calcolo numerico

### 1.1 Perché esiste NumPy

Le liste Python sono strutture dati generiche: possono contenere oggetti di qualsiasi tipo, e ogni elemento è un oggetto Python completo con il suo overhead di memoria e di gestione. Quando lavoriamo con dati numerici — vettori di misurazioni, matrici di covarianza, serie temporali — questa generalità diventa un peso. Ogni operazione aritmetica su una lista richiede un ciclo Python, e ogni iterazione paga il costo dell'interprete.

Il problema era noto fin dagli anni '90. Nel 1995 Jim Hugunin creò **Numeric**, la prima libreria per array numerici in Python. Il progetto ebbe successo ma si frammentò: nacque anche **Numarray**, con scelte di design diverse. Nel 2005 **Travis Oliphant** unificò i due progetti in un'unica libreria: **NumPy** (Numerical Python). Da allora NumPy è il fondamento su cui poggia tutto l'ecosistema scientifico di Python.

Il segreto di NumPy è semplice: memorizza i dati in **blocchi di memoria contigui** di tipo omogeneo (ad esempio, tutti `float64`), esattamente come farebbe un programma C o Fortran. Le operazioni sono implementate in C compilato, non in Python interpretato. Il risultato è un guadagno di velocità che può raggiungere due ordini di grandezza (100x) rispetto al codice Python puro.

```python
import numpy as np

# Lista Python: ogni elemento è un oggetto Python separato
lista: list[float] = [1.0, 2.0, 3.0, 4.0, 5.0]

# Array NumPy: blocco contiguo di float64 in memoria
array: np.ndarray = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
```

La convenzione universale è importare NumPy con l'alias `np`. Non usate mai `from numpy import *`: inquina il namespace e crea confusione.

### 1.2 Creare array: il tipo `ndarray`

L'oggetto fondamentale di NumPy è l'`ndarray` (*n-dimensional array*). Esistono molti modi per crearlo.

**Da una lista Python:**

```python
import numpy as np

# Vettore (1D)
voti: np.ndarray = np.array([28, 30, 25, 27, 30])

# Matrice (2D) — lista di liste
matrice: np.ndarray = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

**Con funzioni di costruzione:**

```python
import numpy as np

# Array di zeri
zeri: np.ndarray = np.zeros(10)            # 10 zeri float64
zeri_2d: np.ndarray = np.zeros((3, 4))     # Matrice 3×4 di zeri

# Array di uni
uni: np.ndarray = np.ones(5)               # 5 uno float64

# Sequenza con passo fisso (simile a range, ma per float)
intervallo: np.ndarray = np.arange(0, 10, 0.5)  # [0.0, 0.5, 1.0, ..., 9.5]

# Sequenza con numero di punti fisso (molto usata per grafici)
punti: np.ndarray = np.linspace(0, 1, 100)  # 100 punti equidistanti tra 0 e 1
```

La differenza tra `np.arange` e `np.linspace` è importante: `arange` specifica il *passo*, `linspace` specifica il *numero di punti*. Per generare ascisse di un grafico, `linspace` è quasi sempre la scelta migliore.

### 1.3 Attributi di un array

Ogni `ndarray` porta con sé informazioni sulla propria struttura:

```python
import numpy as np

dati: np.ndarray = np.array([[1.5, 2.3, 3.1],
                              [4.0, 5.7, 6.2]])

print(dati.shape)    # (2, 3) — 2 righe, 3 colonne
print(dati.dtype)    # float64 — tipo degli elementi
print(dati.ndim)     # 2 — numero di dimensioni
print(dati.size)     # 6 — numero totale di elementi
```

L'attributo `dtype` è cruciale: NumPy ottiene la sua velocità proprio perché *tutti* gli elementi hanno lo stesso tipo. I tipi più comuni sono `float64` (default per i float), `int64` (default per gli interi) e `bool`. Se mescolate tipi, NumPy promuove tutto al tipo più generale:

```python
import numpy as np

misto: np.ndarray = np.array([1, 2.5, 3])
print(misto.dtype)  # float64 — gli interi sono stati promossi a float
```

### 1.4 Vettorizzazione: operare senza cicli

Questo è il concetto più importante di NumPy. La **vettorizzazione** consiste nell'applicare operazioni a interi array senza scrivere cicli espliciti. Le operazioni vengono eseguite elemento per elemento dal codice C interno di NumPy.

```python
import numpy as np

# Con le liste Python — lento e verboso
valori_lista: list[float] = [1.0, 2.0, 3.0, 4.0, 5.0]
quadrati_lista: list[float] = []
for v in valori_lista:
    quadrati_lista.append(v ** 2)

# Con NumPy — veloce e conciso
valori: np.ndarray = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
quadrati: np.ndarray = valori ** 2  # [1.0, 4.0, 9.0, 16.0, 25.0]
```

Tutte le operazioni aritmetiche funzionano elemento per elemento:

```python
import numpy as np

a: np.ndarray = np.array([10, 20, 30])
b: np.ndarray = np.array([1, 2, 3])

print(a + b)     # [11, 22, 33]
print(a * b)     # [10, 40, 90]
print(a / b)     # [10.0, 10.0, 10.0]
print(a > 15)    # [False, True, True]  — confronto vettorizzato
```

Anche il confronto è vettorizzato e restituisce un array di booleani. Questo è fondamentale per il *filtraggio*:

```python
import numpy as np

temperature: np.ndarray = np.array([15.2, 22.1, 31.5, 18.7, 28.3])
calde: np.ndarray = temperature[temperature > 25]  # [31.5, 28.3]
```

**Confronto di performance.** Per apprezzare la differenza, considerate un'operazione su un milione di elementi:

```python
import numpy as np
import time

n: int = 1_000_000

# Lista Python
lista: list[float] = list(range(n))
inizio: float = time.time()
risultato_lista: list[float] = [x ** 2 + 2 * x + 1 for x in lista]
tempo_lista: float = time.time() - inizio

# NumPy
array: np.ndarray = np.arange(n, dtype=np.float64)
inizio = time.time()
risultato_array: np.ndarray = array ** 2 + 2 * array + 1
tempo_numpy: float = time.time() - inizio

print(f"Lista Python: {tempo_lista:.3f} s")
print(f"NumPy:        {tempo_numpy:.3f} s")
print(f"Speedup:      {tempo_lista / tempo_numpy:.0f}x")
# Output tipico: Lista Python: 0.350 s, NumPy: 0.004 s, Speedup: ~80x
```

La regola pratica è: **se vi trovate a scrivere un ciclo `for` su dati numerici, probabilmente esiste un modo vettorizzato per farlo con NumPy**.

### 1.5 Funzioni statistiche e broadcasting

NumPy offre tutte le funzioni statistiche di base:

```python
import numpy as np

voti: np.ndarray = np.array([28, 30, 25, 27, 30, 24, 29, 26])

print(np.mean(voti))    # 27.375  — media aritmetica
print(np.median(voti))  # 27.5    — mediana
print(np.std(voti))     # 2.155   — deviazione standard (popolazione)
print(np.std(voti, ddof=1))  # 2.326 — dev. standard campionaria
print(np.sum(voti))     # 219     — somma
print(np.min(voti))     # 24      — minimo
print(np.max(voti))     # 30      — massimo
print(np.var(voti))     # 4.484   — varianza (popolazione)
```

Nota per gli statistici: `np.std` e `np.var` calcolano per default la deviazione standard e la varianza *della popolazione* (dividendo per *n*). Per la versione *campionaria* (dividendo per *n - 1*), passate `ddof=1` (degrees of freedom adjustment).

**Broadcasting.** Quando si opera tra array di forma diversa, NumPy applica il *broadcasting*: "espande" automaticamente l'array più piccolo per rendere le dimensioni compatibili.

```python
import numpy as np

# Scalare + array: lo scalare viene "espanso"
dati: np.ndarray = np.array([10.0, 20.0, 30.0])
normalizzati: np.ndarray = dati / np.max(dati)  # [0.333, 0.667, 1.0]

# Standardizzazione (z-score)
media: np.floating = np.mean(dati)
dev_std: np.floating = np.std(dati, ddof=1)
z_scores: np.ndarray = (dati - media) / dev_std
```

Il broadcasting funziona anche con matrici. Ad esempio, se volete sottrarre la media di ogni colonna da una matrice:

```python
import numpy as np

matrice: np.ndarray = np.array([[1.0, 2.0, 3.0],
                                 [4.0, 5.0, 6.0],
                                 [7.0, 8.0, 9.0]])

# Media di ogni colonna: array di forma (3,)
medie_colonne: np.ndarray = np.mean(matrice, axis=0)  # [4.0, 5.0, 6.0]

# Broadcasting: la riga (3,) viene "espansa" a (3, 3)
centrata: np.ndarray = matrice - medie_colonne
```

Il parametro `axis` specifica lungo quale dimensione operare: `axis=0` opera lungo le righe (risultato per colonna), `axis=1` opera lungo le colonne (risultato per riga).

### 1.6 Generazione di campioni casuali

Il modulo `np.random` è essenziale per la simulazione statistica:

```python
import numpy as np

# Generatore moderno (preferito rispetto alle funzioni globali)
rng: np.random.Generator = np.random.default_rng(seed=42)

# Campione da una distribuzione uniforme [0, 1)
uniformi: np.ndarray = rng.uniform(low=0.0, high=1.0, size=1000)

# Campione da una normale (media=0, dev.std=1)
normali: np.ndarray = rng.normal(loc=0.0, scale=1.0, size=1000)

# Campione da una binomiale (n=10, p=0.5)
binomiali: np.ndarray = rng.binomial(n=10, p=0.5, size=1000)

# Interi casuali
interi: np.ndarray = rng.integers(low=1, high=7, size=100)  # Simulazione di un dado

# Permutazione casuale
ordine: np.ndarray = rng.permutation(10)  # [3, 7, 0, 5, ...]
```

Il parametro `seed` garantisce la **riproducibilità**: con lo stesso seed otterrete sempre gli stessi numeri "casuali". Questo è fondamentale nel lavoro scientifico: i risultati devono poter essere verificati e replicati.

---

## 2. Pandas — dati tabulari con potenza e semplicità

### 2.1 Origine e filosofia

Nel 2008 **Wes McKinney**, analista finanziario, si trovava frustrato dalla mancanza di uno strumento Python adeguato per l'analisi dei dati tabulari. Creò **Pandas** (il nome deriva da *panel data*, un termine dell'econometria) per colmare questa lacuna. Pandas è costruito sopra NumPy e ne sfrutta la velocità, aggiungendo però un livello di astrazione che rende il lavoro con i dati tabulari enormemente più comodo.

Se NumPy è il motore, Pandas è il cruscotto: vi permette di lavorare con dati etichettati (righe e colonne con nomi), gestire valori mancanti, leggere e scrivere diversi formati di file, e aggregare dati con poche righe di codice.

```python
import pandas as pd

# Convenzione: importare pandas come pd
```

### 2.2 Le strutture fondamentali: Series e DataFrame

Pandas ha due strutture dati principali:

- **`Series`**: un array unidimensionale etichettato (pensatelo come una colonna di un foglio di calcolo).
- **`DataFrame`**: una tabella bidimensionale con righe e colonne etichettate (pensatelo come un intero foglio di calcolo, o come un dizionario di Series).

```python
import pandas as pd
import numpy as np

# Series — una colonna con indice
voti: pd.Series = pd.Series(
    data=[28, 30, 25, 27],
    index=["Alice", "Bob", "Carla", "Dario"],
    name="voto"
)
print(voti["Alice"])   # 28
print(voti.mean())     # 27.5

# DataFrame — una tabella
df: pd.DataFrame = pd.DataFrame({
    "nome": ["Alice", "Bob", "Carla", "Dario"],
    "voto": [28, 30, 25, 27],
    "corso": ["Stat I", "Stat I", "Stat II", "Stat II"]
})
```

Nella pratica quotidiana si lavora quasi sempre con i DataFrame: le Series emergono quando si seleziona una singola colonna.

### 2.3 Leggere dati: `read_csv()` e l'esplorazione iniziale

Il modo più comune per creare un DataFrame è leggere un file CSV:

```python
import pandas as pd

# Lettura base
df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# Lettura con opzioni comuni
df = pd.read_csv(
    "dati/esami_europeo.csv",
    sep=";",                    # Separatore (default: virgola)
    encoding="utf-8",           # Encoding del file
    decimal=",",                # Separatore decimale europeo
    na_values=["", "NA", "?"],  # Valori da trattare come mancanti
)
```

Dopo aver caricato i dati, il primo passo è *esplorarli*. Pandas offre metodi rapidi per farsi un'idea del contenuto:

```python
import pandas as pd

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# Prime 5 righe (o prime n con head(n))
print(df.head())

# Ultime 5 righe
print(df.tail())

# Struttura: tipi, valori non nulli, memoria
print(df.info())

# Statistiche descrittive per le colonne numeriche
print(df.describe())

# Dimensioni
print(df.shape)  # (numero_righe, numero_colonne)

# Nomi delle colonne
print(df.columns)
```

Il metodo `describe()` è particolarmente utile: restituisce in un colpo solo conteggio, media, deviazione standard, minimo, massimo e quartili di ogni colonna numerica. Per le colonne categoriali, usate `describe(include="object")`.

Per le colonne categoriali, `value_counts()` è lo strumento chiave:

```python
import pandas as pd

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# Frequenze assolute
print(df["corso"].value_counts())

# Frequenze relative (proporzioni)
print(df["corso"].value_counts(normalize=True))
```

### 2.4 Selezione e filtro

La selezione dei dati in Pandas è uno degli aspetti più importanti e talvolta più confusi. Vediamo i modi principali.

**Selezione di colonne:**

```python
import pandas as pd

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# Una colonna → restituisce una Series
voti: pd.Series = df["voto"]

# Più colonne → restituisce un DataFrame
sottoinsieme: pd.DataFrame = df[["nome", "voto"]]
```

**Filtro di righe con condizioni booleane:**

```python
import pandas as pd

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# Filtro semplice
promossi: pd.DataFrame = df[df["voto"] >= 18]

# Filtro combinato (usare & per AND, | per OR, ~ per NOT)
# ATTENZIONE: le parentesi sono obbligatorie!
eccellenti_stat: pd.DataFrame = df[
    (df["voto"] >= 28) & (df["corso"] == "Statistica I")
]
```

**`loc` e `iloc` — selezione esplicita:**

- `loc`: selezione per *etichette* (nomi di righe e colonne).
- `iloc`: selezione per *posizione intera* (indici numerici).

```python
import pandas as pd

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# loc — per etichetta
riga_zero: pd.Series = df.loc[0]                      # Riga con indice 0
cella: object = df.loc[0, "nome"]                      # Riga 0, colonna "nome"
fetta: pd.DataFrame = df.loc[0:5, ["nome", "voto"]]   # Righe 0-5, due colonne

# iloc — per posizione (come gli indici delle liste)
prima_riga: pd.Series = df.iloc[0]                     # Prima riga
prime_tre: pd.DataFrame = df.iloc[:3]                  # Prime 3 righe
angolo: pd.DataFrame = df.iloc[:5, :2]                 # Prime 5 righe, prime 2 colonne
```

La differenza è sottile ma importante: `loc` include entrambi gli estremi dell'intervallo (`df.loc[0:5]` restituisce 6 righe), mentre `iloc` esclude l'estremo superiore (`df.iloc[0:5]` restituisce 5 righe), come il `range` di Python.

### 2.5 Pulizia dei dati

I dati reali sono quasi sempre sporchi: valori mancanti, duplicati, tipi sbagliati. Pandas offre strumenti specifici per ogni problema.

**Valori mancanti (`NaN`):**

```python
import pandas as pd
import numpy as np

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# Quanti valori mancanti per colonna?
print(df.isna().sum())

# Rimuovere righe con qualsiasi valore mancante
pulito: pd.DataFrame = df.dropna()

# Rimuovere righe solo se mancano valori in colonne specifiche
pulito = df.dropna(subset=["voto", "nome"])

# Sostituire i mancanti con un valore
riempito: pd.DataFrame = df.fillna({"voto": 0, "corso": "Sconosciuto"})

# Sostituire con la media della colonna
media_voto: float = df["voto"].mean()
df["voto"] = df["voto"].fillna(media_voto)
```

**Duplicati:**

```python
import pandas as pd

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# Ci sono duplicati?
print(df.duplicated().sum())

# Rimuovere duplicati (tiene la prima occorrenza)
senza_duplicati: pd.DataFrame = df.drop_duplicates()

# Duplicati su colonne specifiche
senza_dup_nome: pd.DataFrame = df.drop_duplicates(subset=["nome", "corso"])
```

**Conversione di tipo:**

```python
import pandas as pd

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# Convertire una colonna a un tipo specifico
df["voto"] = df["voto"].astype(int)
df["data"] = pd.to_datetime(df["data"])  # Conversione a datetime

# Rinominare colonne
df = df.rename(columns={"voto": "punteggio", "nome": "studente"})
```

### 2.6 Aggregazione con `groupby()` e `merge()`

Il metodo `groupby()` è uno degli strumenti più potenti di Pandas. Implementa il pattern *split-apply-combine*: divide i dati in gruppi, applica una funzione a ciascun gruppo, e combina i risultati.

```python
import pandas as pd

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# Media del voto per corso
medie: pd.DataFrame = df.groupby("corso")["voto"].mean()
print(medie)

# Più statistiche contemporaneamente
statistiche: pd.DataFrame = df.groupby("corso")["voto"].agg(
    ["mean", "std", "min", "max", "count"]
)
print(statistiche)

# Raggruppamento su più colonne
dettaglio: pd.DataFrame = df.groupby(["corso", "anno"])["voto"].mean()
print(dettaglio)
```

Per unire dati da tabelle diverse, Pandas offre `merge()` (equivalente al JOIN di SQL):

```python
import pandas as pd

# Due tabelle
esami: pd.DataFrame = pd.DataFrame({
    "studente_id": [1, 2, 3, 4],
    "voto": [28, 30, 25, 27]
})

anagrafica: pd.DataFrame = pd.DataFrame({
    "studente_id": [1, 2, 3, 5],
    "nome": ["Alice", "Bob", "Carla", "Eva"]
})

# Inner join (solo le corrispondenze presenti in entrambe)
risultato: pd.DataFrame = pd.merge(esami, anagrafica, on="studente_id")

# Left join (tutte le righe della tabella di sinistra)
risultato_left: pd.DataFrame = pd.merge(
    esami, anagrafica, on="studente_id", how="left"
)
```

### 2.7 Method chaining: concatenare operazioni

Un aspetto elegante di Pandas è la possibilità di concatenare più operazioni in sequenza, ciascuna che restituisce un nuovo DataFrame. Questo stile si chiama *method chaining* e produce codice molto leggibile:

```python
import pandas as pd

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# Senza method chaining — macchinoso
df1: pd.DataFrame = df.dropna(subset=["voto"])
df2: pd.DataFrame = df1[df1["voto"] >= 18]
df3: pd.DataFrame = df2.groupby("corso")["voto"].mean()
risultato: pd.DataFrame = df3.reset_index()

# Con method chaining — fluido e leggibile
risultato = (
    df
    .dropna(subset=["voto"])
    .query("voto >= 18")
    .groupby("corso")["voto"]
    .mean()
    .reset_index()
    .rename(columns={"voto": "media_voto"})
)
```

Il metodo `query()` è un'alternativa alla selezione booleana che si integra bene nel chaining. La stringa passata a `query()` viene interpretata come un'espressione di filtro.

---

## 3. Visualizzazione dei dati

### 3.1 Matplotlib — la base

**Matplotlib** è la libreria di visualizzazione più usata in Python. Fu creata nel 2003 da **John Hunter**, un neuroscienziato che voleva replicare le capacità grafiche di MATLAB in Python. Il nome stesso ("mat-plot-lib") riflette questa eredità.

Matplotlib è estremamente flessibile: può produrre qualsiasi tipo di grafico, dal più semplice al più complesso. Il prezzo di questa flessibilità è un'API a volte verbosa. Per l'uso quotidiano si utilizza il sottomodulo `pyplot`, che offre un'interfaccia procedurale semplice.

```python
import matplotlib.pyplot as plt
import numpy as np

# Convenzione: importare pyplot come plt
```

**Grafico a linee — il più semplice:**

```python
import matplotlib.pyplot as plt
import numpy as np

x: np.ndarray = np.linspace(0, 2 * np.pi, 100)
y: np.ndarray = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color="steelblue", linewidth=1.5, label="sin(x)")
plt.title("Funzione seno")
plt.xlabel("x (radianti)")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("seno.png", dpi=150)
plt.show()
```

**Istogramma — distribuzione di una variabile continua:**

```python
import matplotlib.pyplot as plt
import numpy as np

rng: np.random.Generator = np.random.default_rng(seed=42)
dati: np.ndarray = rng.normal(loc=170, scale=10, size=500)  # Altezze simulate

plt.figure(figsize=(8, 4))
plt.hist(dati, bins=25, color="steelblue", edgecolor="white", alpha=0.8)
plt.title("Distribuzione delle altezze (campione simulato)")
plt.xlabel("Altezza (cm)")
plt.ylabel("Frequenza")
plt.axvline(np.mean(dati), color="red", linestyle="--", label="Media")
plt.legend()
plt.tight_layout()
plt.show()
```

**Scatter plot — relazione tra due variabili:**

```python
import matplotlib.pyplot as plt
import numpy as np

rng: np.random.Generator = np.random.default_rng(seed=42)
ore_studio: np.ndarray = rng.uniform(2, 40, size=80)
voto: np.ndarray = 18 + 0.3 * ore_studio + rng.normal(0, 2, size=80)
voto = np.clip(voto, 18, 31)  # Limita tra 18 e 31

plt.figure(figsize=(7, 5))
plt.scatter(ore_studio, voto, alpha=0.6, color="steelblue", edgecolors="white")
plt.title("Relazione tra ore di studio e voto")
plt.xlabel("Ore di studio settimanali")
plt.ylabel("Voto esame")
plt.tight_layout()
plt.show()
```

**Bar plot — confronto tra categorie:**

```python
import matplotlib.pyplot as plt

corsi: list[str] = ["Stat I", "Stat II", "Informatica", "Matematica"]
medie: list[float] = [26.5, 24.8, 27.1, 23.2]

plt.figure(figsize=(7, 4))
plt.bar(corsi, medie, color="steelblue", edgecolor="white")
plt.title("Media voti per corso")
plt.ylabel("Voto medio")
plt.ylim(18, 31)
plt.tight_layout()
plt.show()
```

**Boxplot — distribuzione e outlier:**

```python
import matplotlib.pyplot as plt
import numpy as np

rng: np.random.Generator = np.random.default_rng(seed=42)
stat1: np.ndarray = rng.normal(26, 3, size=100)
stat2: np.ndarray = rng.normal(24, 4, size=100)
info: np.ndarray = rng.normal(27, 2, size=100)

plt.figure(figsize=(7, 4))
plt.boxplot(
    [stat1, stat2, info],
    labels=["Stat I", "Stat II", "Informatica"],
    patch_artist=True,
    boxprops=dict(facecolor="steelblue", alpha=0.5)
)
plt.title("Distribuzione dei voti per corso")
plt.ylabel("Voto")
plt.tight_layout()
plt.show()
```

### 3.2 Personalizzazione dei grafici

Un grafico senza titolo, senza etichette e senza legenda è un grafico inutile. Matplotlib offre un controllo totale sulla personalizzazione:

```python
import matplotlib.pyplot as plt

# Impostazioni globali (opzionale, ma utile per uniformità)
plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "figure.figsize": (8, 5),
    "figure.dpi": 100,
})
```

Elementi essenziali di ogni grafico:
- **Titolo** (`plt.title()`): descrive *cosa* mostra il grafico.
- **Etichette degli assi** (`plt.xlabel()`, `plt.ylabel()`): specificano *le variabili* e le *unità di misura*.
- **Legenda** (`plt.legend()`): necessaria quando ci sono più serie.
- **`tight_layout()`**: evita che le etichette vengano tagliate.
- **`savefig()`**: salvare sempre i grafici in formato file, non solo mostrarli a schermo.

### 3.3 Seaborn — grafici statistici belli e informativi

**Seaborn** è una libreria costruita sopra Matplotlib che semplifica la creazione di grafici statistici comuni. Il suo punto di forza è l'integrazione diretta con i DataFrame di Pandas e la produzione di grafici esteticamente curati con meno codice.

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Convenzione: importare seaborn come sns
```

**Boxplot con Seaborn:**

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="corso", y="voto", palette="Set2")
plt.title("Distribuzione dei voti per corso")
plt.tight_layout()
plt.show()
```

Notate la differenza con Matplotlib: in Seaborn passiamo direttamente il DataFrame e specifichiamo le colonne per nome. Non serve preparare i dati manualmente.

**Heatmap — matrice di correlazione:**

```python
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dati simulati
rng: np.random.Generator = np.random.default_rng(seed=42)
df: pd.DataFrame = pd.DataFrame({
    "ore_studio": rng.uniform(5, 40, 100),
    "ore_sonno": rng.uniform(4, 10, 100),
    "voto": rng.normal(25, 3, 100),
    "assenze": rng.integers(0, 20, 100),
})

correlazione: pd.DataFrame = df.corr()

plt.figure(figsize=(7, 6))
sns.heatmap(correlazione, annot=True, fmt=".2f", cmap="coolwarm",
            vmin=-1, vmax=1, center=0)
plt.title("Matrice di correlazione")
plt.tight_layout()
plt.show()
```

La heatmap della matrice di correlazione è uno dei grafici più usati nell'analisi esplorativa: permette di identificare a colpo d'occhio quali variabili sono correlate tra loro.

**Pairplot — tutte le relazioni a due a due:**

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df: pd.DataFrame = pd.read_csv("dati/esami.csv")

# Pairplot delle colonne numeriche, colorato per categoria
sns.pairplot(df, hue="corso", palette="Set2", diag_kind="kde")
plt.suptitle("Relazioni tra variabili numeriche", y=1.02)
plt.show()
```

Il `pairplot` è potente ma va usato con giudizio: con molte variabili genera una matrice enorme di grafici. È più utile con 3-6 variabili numeriche.

### 3.4 Edward Tufte e il data-ink ratio

Non possiamo parlare di visualizzazione senza menzionare **Edward Tufte**, il più influente teorico della visualizzazione dei dati. Nel suo libro *The Visual Display of Quantitative Information* (1983), Tufte introduce il concetto di **data-ink ratio**: il rapporto tra l'inchiostro usato per rappresentare i dati e l'inchiostro totale del grafico.

L'idea è semplice e profonda: **ogni elemento visivo che non comunica informazione è rumore e va eliminato**. Griglie troppo marcate, bordi inutili, colori decorativi, effetti 3D — tutto ciò che non aiuta il lettore a capire i dati è "chartjunk" (spazzatura grafica) e va rimosso.

Principi pratici derivati da Tufte:

1. **Massimizzare il data-ink ratio**: ogni pixel del grafico deve comunicare informazione.
2. **Evitare effetti 3D**: distorcono la percezione e non aggiungono informazione.
3. **Evitare colori decorativi**: il colore deve codificare una variabile, non abbellire.
4. **Preferire grafici piccoli e multipli** (*small multiples*) a un unico grafico complesso.
5. **Etichettare direttamente i dati** quando possibile, invece di usare legende separate.

Un esempio pratico: un istogramma con sfondo grigio, griglia pesante, bordi spessi e ombreggiature è meno efficace di un istogramma pulito con sfondo bianco, griglia leggera e colori sobri.

```python
import matplotlib.pyplot as plt
import numpy as np

rng: np.random.Generator = np.random.default_rng(seed=42)
dati: np.ndarray = rng.normal(0, 1, size=500)

# Stile "Tufte-inspired": minimale e chiaro
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(dati, bins=30, color="steelblue", edgecolor="white", alpha=0.85)
ax.set_title("Campione da distribuzione normale standard")
ax.set_xlabel("Valore")
ax.set_ylabel("Frequenza")
ax.spines["top"].set_visible(False)     # Rimuove bordo superiore
ax.spines["right"].set_visible(False)   # Rimuove bordo destro
ax.grid(axis="y", alpha=0.2)
fig.tight_layout()
plt.show()
```

Rimuovere i bordi superiore e destro (*spines*) è un piccolo cambiamento che rende il grafico immediatamente più pulito. È un'abitudine da adottare per tutti i grafici.

---

## 4. Orizzonti e best practice

### 4.1 SciPy e scikit-learn — cenni

L'ecosistema scientifico di Python si estende ben oltre NumPy e Pandas. Due librerie meritano una menzione:

**SciPy** (`scipy.stats`) estende NumPy con funzioni statistiche avanzate: test di ipotesi, distribuzioni di probabilità, intervalli di confidenza.

```python
from scipy import stats
import numpy as np

# Test t di Student per un campione
rng: np.random.Generator = np.random.default_rng(seed=42)
campione: np.ndarray = rng.normal(loc=100, scale=15, size=30)

risultato = stats.ttest_1samp(campione, popmean=100)
print(f"Statistica t: {risultato.statistic:.3f}")
print(f"p-value:      {risultato.pvalue:.4f}")

# Distribuzione normale: pdf, cdf, ppf (quantile)
print(stats.norm.cdf(1.96))   # ~0.975
print(stats.norm.ppf(0.975))  # ~1.96
```

**scikit-learn** è la libreria di riferimento per il machine learning in Python. Il suo design è elegante e uniforme: tutti i modelli seguono il pattern `fit` / `predict`.

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Dati (X deve essere 2D)
X: np.ndarray = np.array([[1], [2], [3], [4], [5]])
y: np.ndarray = np.array([2.1, 3.9, 6.2, 7.8, 10.1])

# Addestramento
modello: LinearRegression = LinearRegression()
modello.fit(X, y)

# Predizione
previsione: np.ndarray = modello.predict(np.array([[6]]))
print(f"Previsione per x=6: {previsione[0]:.2f}")
print(f"Coefficiente:        {modello.coef_[0]:.3f}")
print(f"Intercetta:          {modello.intercept_:.3f}")
```

Questi sono solo cenni: SciPy e scikit-learn richiederebbero corsi interi. L'obiettivo qui è sapere che esistono e riconoscerne il pattern d'uso.

### 4.2 Dati dal mondo esterno — cenni

I dati non arrivano solo da file CSV. Due fonti importanti meritano una menzione:

**API REST**: molti servizi web espongono dati attraverso interfacce programmatiche. Python può interrogarle con la libreria `requests`:

```python
import requests
import pandas as pd

# Esempio concettuale (l'URL è illustrativo)
risposta = requests.get("https://api.esempio.it/dati/istat/popolazione")
if risposta.status_code == 200:
    dati: list[dict] = risposta.json()
    df: pd.DataFrame = pd.DataFrame(dati)
```

**Database SQLite**: per dati strutturati e persistenti, Python include il modulo `sqlite3`. Pandas può leggere direttamente da un database:

```python
import sqlite3
import pandas as pd

connessione: sqlite3.Connection = sqlite3.connect("universita.db")
df: pd.DataFrame = pd.read_sql(
    "SELECT nome, voto FROM esami WHERE voto >= 18",
    connessione
)
connessione.close()
```

### 4.3 Intelligenza artificiale, LLM e il ruolo dello statistico

L'esplosione dei Large Language Model (ChatGPT, Claude, Gemini) sta trasformando il modo in cui si scrive codice. Questi strumenti possono generare codice Python, spiegare errori, suggerire approcci. È legittimo (e intelligente) usarli come assistenti.

Ma c'è un punto fondamentale: **un LLM non capisce i dati**. Può generare codice che calcola una media, ma non sa se quella media ha senso statistico. Può produrre un grafico, ma non sa se quel grafico è fuorviante. Può suggerire un modello, ma non sa se le assunzioni sono violate.

Il ruolo dello statistico non è scrivere codice velocemente — quello lo può fare una macchina. Il ruolo dello statistico è *pensare ai dati*: formulare domande, scegliere metodi appropriati, interpretare i risultati, comunicare le conclusioni con rigore e onestà. La competenza di programmazione che state acquisendo in questo corso vi rende capaci di *dialogare* con gli strumenti (inclusi gli LLM) in modo critico e informato. Chi non sa programmare è costretto a fidarsi ciecamente dell'output; chi sa programmare può verificare, modificare e comprendere.

### 4.4 Best practice consolidate

In questa ultima sezione raccogliamo le pratiche che distinguono un progetto Python professionale da un insieme disordinato di script.

**Linter e formatter.** Un *linter* analizza il codice alla ricerca di errori potenziali e violazioni di stile. Un *formatter* riformatta automaticamente il codice per renderlo uniforme.

- **Ruff**: il linter moderno per Python, scritto in Rust, estremamente veloce. Sostituisce `flake8`, `isort` e molti altri strumenti in uno solo.
- **Black**: il formatter "opinato" per Python. Non offre opzioni di configurazione (o quasi): sceglie uno stile e lo applica. Questo elimina le discussioni sullo stile e rende tutto il codice uniforme.

```bash
# Installazione
pip install ruff black

# Uso
ruff check mio_progetto/        # Analizza il codice
ruff check --fix mio_progetto/  # Corregge automaticamente dove possibile
black mio_progetto/              # Formatta tutto il codice
```

**Controllo dei tipi con mypy.** Python è un linguaggio a tipizzazione dinamica, ma i *type hints* che abbiamo usato in tutto il corso permettono di aggiungere un livello di controllo statico. **mypy** verifica che i tipi dichiarati siano coerenti con l'uso effettivo:

```bash
pip install mypy
mypy mio_programma.py
```

Se dichiariamo `x: int = "ciao"`, mypy segnalerà l'errore *prima* dell'esecuzione. In un progetto grande, questo previene intere categorie di bug.

**Test con pytest.** Abbiamo già visto i test nelle lezioni precedenti. **pytest** è lo strumento standard per scrivere ed eseguire test in Python:

```python
# test_statistiche.py
import numpy as np


def calcola_media(valori: list[float]) -> float:
    """Calcola la media aritmetica."""
    if not valori:
        raise ValueError("Lista vuota")
    return sum(valori) / len(valori)


def test_media_base() -> None:
    assert calcola_media([1, 2, 3]) == 2.0


def test_media_singolo() -> None:
    assert calcola_media([5.0]) == 5.0


def test_media_vuota() -> None:
    import pytest
    with pytest.raises(ValueError):
        calcola_media([])
```

```bash
pytest test_statistiche.py -v
```

**Debugging.** Quando un programma non funziona e non capite perché, usate il debugger integrato di Python:

```python
# Inserite questa riga dove volete fermarvi
breakpoint()
```

Questo apre il debugger interattivo `pdb`, dove potete ispezionare variabili, eseguire codice riga per riga e capire cosa sta succedendo. Gli IDE moderni (VS Code, PyCharm) offrono debugger grafici ancora più comodi.

**Struttura di un progetto.** Un progetto Python ben organizzato segue una struttura prevedibile:

```
progetto_analisi/
├── dati/
│   ├── raw/            # Dati originali (MAI modificarli)
│   └── processed/      # Dati elaborati
├── src/
│   ├── __init__.py
│   ├── caricamento.py
│   ├── pulizia.py
│   └── analisi.py
├── test/
│   ├── test_caricamento.py
│   └── test_pulizia.py
├── grafici/
├── requirements.txt    # Dipendenze (pip freeze > requirements.txt)
├── pyproject.toml      # Configurazione del progetto
└── README.md
```

**Principi guida:**

- **Riproducibilità**: chiunque deve poter eseguire il vostro codice e ottenere gli stessi risultati. Usate seed per la casualità, documentate le dipendenze, versionate il codice con Git.
- **DRY** (*Don't Repeat Yourself*): se copiate e incollate codice, probabilmente dovreste estrarre una funzione.
- **KISS** (*Keep It Simple, Stupid*): il codice più semplice che risolve il problema è il codice migliore. La complessità non è un segno di competenza; la semplicità lo è.

---

## Domande di verifica

1. Perché un array NumPy è molto più veloce di una lista Python per operazioni numeriche? Quali sono le due caratteristiche architetturali che rendono possibile questo vantaggio?

2. Qual è la differenza tra `np.arange(0, 10, 0.5)` e `np.linspace(0, 10, 20)`? In quale situazione preferireste l'uno o l'altro?

3. Spiegate cosa fa `np.std(dati, ddof=1)` e perché il parametro `ddof=1` è importante per uno statistico.

4. Qual è la differenza tra `df.loc[0:5]` e `df.iloc[0:5]` in Pandas? Quante righe restituisce ciascuno?

5. Date un DataFrame `df` con colonne `"regione"`, `"anno"` e `"reddito"`, scrivete il codice Pandas per calcolare il reddito medio per regione, ordinato in modo decrescente.

6. Perché Edward Tufte suggerisce di massimizzare il *data-ink ratio*? Fate un esempio di elemento grafico che andrebbe rimosso.

7. Spiegate la differenza tra Matplotlib e Seaborn: quando usereste l'uno e quando l'altro?

8. Cosa significa il principio DRY e perché è particolarmente importante nell'analisi dei dati?

---

## Esercizi

### Base

**Esercizio 1 — Statistica descrittiva con NumPy**

Scrivete una funzione `descrivi_campione(dati: np.ndarray) -> dict[str, float]` che riceve un array NumPy e restituisce un dizionario con le seguenti statistiche: `"media"`, `"mediana"`, `"dev_std"` (campionaria), `"minimo"`, `"massimo"`, `"n"`. Non usate cicli.

**Esercizio 2 — DataFrame da dizionario**

Create un DataFrame con i dati di almeno 10 studenti (nome, cognome, voto, corso). Calcolate la media e la deviazione standard del voto per corso usando `groupby()`. Stampate il risultato.

**Esercizio 3 — Istogramma da dati simulati**

Generate un campione di 1000 valori da una distribuzione normale con media 170 e deviazione standard 8 (altezze simulate). Create un istogramma con Matplotlib, aggiungendo una linea verticale per la media e una per la mediana. Salvate il grafico come file PNG.

### Intermedio

**Esercizio 4 — Analisi esplorativa completa**

Scrivete uno script che:
1. Carica un file CSV con `pd.read_csv()`.
2. Stampa `info()` e `describe()`.
3. Identifica e riporta le colonne con valori mancanti.
4. Produce un boxplot per ogni colonna numerica.
5. Produce una heatmap della matrice di correlazione.

Strutturate il codice in funzioni con type hints e docstring.

**Esercizio 5 — Pulizia e aggregazione**

Partendo da un DataFrame con colonne `"città"`, `"mese"`, `"temperatura"`, `"precipitazioni"`, scrivete una pipeline (method chaining) che:
1. Rimuove le righe con valori mancanti.
2. Filtra solo i mesi estivi (giugno, luglio, agosto).
3. Calcola la temperatura media e le precipitazioni totali per città.
4. Ordina il risultato per temperatura media decrescente.

**Esercizio 6 — Confronto di grafici**

Create due versioni dello stesso scatter plot: una "sovraccarica" (sfondo colorato, griglia pesante, bordi spessi, font piccolo) e una "minimale" (stile Tufte: sfondo bianco, griglia leggera, bordi superiore e destro rimossi). Usate `plt.subplots(1, 2)` per metterle affiancate.

### Avanzato

**Esercizio 7 — Simulazione Monte Carlo**

Scrivete una funzione `stima_pi_montecarlo(n: int, seed: int = 42) -> float` che stima il valore di pi greco lanciando `n` punti casuali in un quadrato unitario e contando quanti cadono nel cerchio inscritto. Usate NumPy (niente cicli). Producete un grafico che mostra come la stima converge al valore vero al crescere di `n`, usando `np.linspace` per generare i valori di `n` da testare.

**Esercizio 8 — Pipeline completa di analisi**

Scrivete un modulo Python (`analisi_esami.py`) che:
1. Carica dati da un CSV.
2. Pulisce i dati (rimuove duplicati, gestisce mancanti, converte tipi).
3. Calcola statistiche descrittive per gruppo.
4. Produce almeno tre grafici informativi (istogramma, boxplot, scatter o bar).
5. Salva i risultati in un CSV e i grafici in una cartella `output/`.
6. Usa type hints, docstring, e gestione degli errori.
7. Include almeno 3 test con pytest in un file separato.

Questo esercizio integra tutto ciò che avete imparato nel corso.

---

## Osservazioni finali

Questa lezione è stata la più densa del corso, e non a caso: NumPy, Pandas e Matplotlib sono gli strumenti che userete ogni giorno nel vostro lavoro di statistici. Non ci si aspetta che memorizziate ogni funzione e ogni parametro — nessuno lo fa. L'obiettivo è che sappiate *cosa è possibile fare* e *dove cercare* quando ne avrete bisogno.

Tre concetti da portare con sé:

1. **Vettorizzazione**: operare su interi array invece che su singoli elementi. È il salto concettuale che separa il codice lento dal codice veloce, e il codice verboso dal codice elegante.
2. **Il DataFrame come unità di lavoro**: nella pratica statistica, quasi tutto il lavoro si svolge su tabelle. Pandas vi dà un linguaggio per esprimere operazioni su tabelle (filtrare, aggregare, unire, trasformare) in modo conciso e leggibile.
3. **Il grafico come strumento di pensiero**: un buon grafico non è una decorazione per un report — è uno strumento per *capire* i dati. Seguite i principi di Tufte: ogni elemento deve informare, mai decorare.

Avete percorso molta strada dal primo giorno, quando un bit era un concetto astratto e una variabile era un mistero. Ora sapete programmare, leggere file, costruire classi, gestire errori, analizzare dati e produrre grafici. Questi strumenti non sono il punto di arrivo, ma un punto di partenza solido: qualunque direzione prenderà la vostra carriera — analisi statistica, data science, ricerca accademica, consulenza — le fondamenta che avete costruito in questo corso vi sosterranno.
