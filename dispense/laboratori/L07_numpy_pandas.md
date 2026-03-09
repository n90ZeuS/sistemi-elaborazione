# Laboratorio 7 — NumPy e Pandas

**Prerequisiti:** Frontale F17 (NumPy, Pandas, analisi dati)

---

## Obiettivo del laboratorio

In questo laboratorio imparerete a usare le due librerie fondamentali dell'ecosistema Python per l'analisi dei dati: **NumPy** per il calcolo numerico vettorizzato e **Pandas** per la manipolazione di dati tabulari. Ogni esercizio guidato va eseguito cella per cella, osservando l'output e sperimentando variazioni.

---

## Parte 1 — Esercizi guidati

### 1.1 NumPy: creare array e operazioni vettorizzate

NumPy introduce il tipo `ndarray`, un contenitore di dati omogenei che permette di eseguire operazioni su interi vettori senza scrivere cicli espliciti.

```python
import numpy as np

# Creare array da liste Python
voti: np.ndarray = np.array([28, 25, 30, 22, 27, 18, 30, 24])
print(f"Array: {voti}")
print(f"Tipo: {type(voti)}")
print(f"Dtype: {voti.dtype}")
print(f"Shape: {voti.shape}")
print(f"Dimensione: {voti.size}")

# Array con funzioni di creazione
zeri: np.ndarray = np.zeros(10)
uni: np.ndarray = np.ones(5)
sequenza: np.ndarray = np.arange(0, 100, 5)        # da 0 a 95, passo 5
lineare: np.ndarray = np.linspace(0, 1, 11)         # 11 punti equispaziati tra 0 e 1

print(f"Zeri: {zeri}")
print(f"Uni: {uni}")
print(f"Sequenza: {sequenza}")
print(f"Lineare: {lineare}")
```

Le operazioni aritmetiche si applicano **elemento per elemento**, senza bisogno di cicli:

```python
import numpy as np

voti: np.ndarray = np.array([28, 25, 30, 22, 27, 18, 30, 24])

# Operazioni vettorizzate
voti_normalizzati: np.ndarray = voti / 30.0
voti_scalati: np.ndarray = voti * 10 / 3
voti_bonus: np.ndarray = voti + 2

print(f"Normalizzati (0-1): {voti_normalizzati}")
print(f"Scalati (0-100):    {np.round(voti_scalati, 1)}")
print(f"Con bonus +2:       {voti_bonus}")

# Operazioni tra array
pesi: np.ndarray = np.array([0.1, 0.1, 0.2, 0.1, 0.15, 0.1, 0.15, 0.1])
media_pesata: float = float(np.sum(voti * pesi))
print(f"Media pesata: {media_pesata:.2f}")

# Confronti vettorizzati (restituiscono array di bool)
sufficienti: np.ndarray = voti >= 18
eccellenti: np.ndarray = voti >= 28
print(f"Sufficienti: {sufficienti}")
print(f"Numero eccellenti: {np.sum(eccellenti)}")

# Indicizzazione booleana (filtering)
voti_alti: np.ndarray = voti[voti >= 27]
print(f"Voti >= 27: {voti_alti}")
```

### 1.2 Statistiche con NumPy e confronto di prestazioni

NumPy fornisce funzioni statistiche ottimizzate. Confrontiamole con l'equivalente Python puro per apprezzare la differenza di velocita.

```python
import numpy as np

voti: np.ndarray = np.array([28, 25, 30, 22, 27, 18, 30, 24, 26, 29])

# Statistiche descrittive
print(f"Media:              {np.mean(voti):.2f}")
print(f"Mediana:            {np.median(voti):.2f}")
print(f"Deviazione standard:{np.std(voti):.2f}")
print(f"Varianza:           {np.var(voti):.2f}")
print(f"Minimo:             {np.min(voti)}")
print(f"Massimo:            {np.max(voti)}")
print(f"Percentile 25:      {np.percentile(voti, 25):.2f}")
print(f"Percentile 75:      {np.percentile(voti, 75):.2f}")
```

Ora confrontiamo le prestazioni: ciclo Python vs operazione vettorizzata NumPy.

```python
import numpy as np
import time

# Creare un array grande
n: int = 1_000_000
dati_np: np.ndarray = np.random.randn(n)
dati_lista: list[float] = dati_np.tolist()

# Calcolo media con ciclo Python
inizio: float = time.time()
somma: float = 0.0
for valore in dati_lista:
    somma += valore
media_ciclo: float = somma / n
tempo_ciclo: float = time.time() - inizio

# Calcolo media con NumPy
inizio = time.time()
media_numpy: float = float(np.mean(dati_np))
tempo_numpy: float = time.time() - inizio

print(f"Media (ciclo):  {media_ciclo:.6f}  — tempo: {tempo_ciclo:.4f} s")
print(f"Media (NumPy):  {media_numpy:.6f}  — tempo: {tempo_numpy:.6f} s")
print(f"NumPy è circa {tempo_ciclo / tempo_numpy:.0f}x più veloce")
```

Il vantaggio di NumPy cresce con la dimensione dei dati: le operazioni sono implementate in C e operano su blocchi contigui di memoria.

### 1.3 NumPy random e simulazione Monte Carlo

NumPy offre un generatore di numeri pseudocasuali molto piu efficiente di quello della libreria standard.

```python
import numpy as np

# Generatore con seed per riproducibilita
rng: np.random.Generator = np.random.default_rng(seed=42)

# Campione da distribuzione uniforme
uniforme: np.ndarray = rng.uniform(low=0.0, high=1.0, size=10)
print(f"Uniforme [0,1]: {np.round(uniforme, 3)}")

# Campione da distribuzione normale
normale: np.ndarray = rng.normal(loc=25.0, scale=3.0, size=10)
print(f"Normale (mu=25, sigma=3): {np.round(normale, 2)}")

# Campione da distribuzione di Poisson
poisson: np.ndarray = rng.poisson(lam=5, size=10)
print(f"Poisson (lambda=5): {poisson}")

# Statistiche del campione normale grande
campione: np.ndarray = rng.normal(loc=170, scale=10, size=10_000)
print(f"\nCampione N(170, 10) con n=10000:")
print(f"  Media campionaria:  {np.mean(campione):.2f}")
print(f"  Dev. std campionaria: {np.std(campione):.2f}")
```

**Stimare pi greco con il metodo Monte Carlo:** generiamo punti casuali in un quadrato di lato 2 centrato nell'origine e contiamo quanti cadono nel cerchio unitario.

```python
import numpy as np

def stima_pi_montecarlo(n_punti: int, seed: int = 42) -> float:
    """Stima pi greco con il metodo Monte Carlo.

    Genera punti casuali nel quadrato [-1,1] x [-1,1] e conta
    la frazione che cade nel cerchio unitario.

    Args:
        n_punti: Numero di punti da generare.
        seed: Seed per la riproducibilita.

    Returns:
        Stima di pi greco.
    """
    rng: np.random.Generator = np.random.default_rng(seed=seed)
    x: np.ndarray = rng.uniform(-1, 1, size=n_punti)
    y: np.ndarray = rng.uniform(-1, 1, size=n_punti)

    # Distanza dall'origine
    distanza_quadrata: np.ndarray = x**2 + y**2

    # Punti dentro il cerchio unitario
    dentro: int = int(np.sum(distanza_quadrata <= 1.0))

    # Area cerchio / Area quadrato = pi/4
    pi_stimato: float = 4.0 * dentro / n_punti
    return pi_stimato


# Proviamo con dimensioni crescenti
for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
    stima: float = stima_pi_montecarlo(n)
    errore: float = abs(stima - np.pi)
    print(f"n = {n:>10,}  ->  pi ≈ {stima:.6f}  (errore: {errore:.6f})")
```

### 1.4 Pandas: caricare e esplorare un dataset CSV

Passiamo ora a Pandas, la libreria per dati tabulari. Useremo un dataset di esempio che creiamo direttamente.

```python
import pandas as pd
import numpy as np

# Creare un dataset di esempio (simulando un CSV reale)
rng: np.random.Generator = np.random.default_rng(seed=42)
n: int = 200

df: pd.DataFrame = pd.DataFrame({
    "id_studente": range(1, n + 1),
    "nome": [f"Studente_{i}" for i in range(1, n + 1)],
    "corso": rng.choice(
        ["Statistica", "Economia", "Sociologia", "Informatica"],
        size=n
    ),
    "anno": rng.choice([1, 2, 3], size=n),
    "voto_medio": np.round(rng.normal(25, 3, size=n).clip(18, 30), 1),
    "crediti": rng.choice([30, 60, 90, 120, 150, 180], size=n),
    "regione": rng.choice(
        ["Lombardia", "Lazio", "Campania", "Sicilia",
         "Veneto", "Emilia-Romagna", "Toscana"],
        size=n
    ),
})

# Salviamo il CSV per usarlo dopo
df.to_csv("studenti.csv", index=False)
print("Dataset salvato come 'studenti.csv'")
print(f"Dimensioni: {df.shape[0]} righe x {df.shape[1]} colonne")
```

Ora esploriamolo con i metodi fondamentali di Pandas:

```python
import pandas as pd

# Caricare il CSV
df: pd.DataFrame = pd.read_csv("studenti.csv")

# Le prime 5 righe
print("=== HEAD ===")
print(df.head())
print()

# Informazioni sulla struttura
print("=== INFO ===")
df.info()
print()

# Statistiche descrittive (solo colonne numeriche)
print("=== DESCRIBE ===")
print(df.describe())
print()

# Conteggio valori per una colonna categoriale
print("=== VALUE COUNTS (corso) ===")
print(df["corso"].value_counts())
print()

# Conteggio valori per regione
print("=== VALUE COUNTS (regione) ===")
print(df["regione"].value_counts())
```

### 1.5 Pandas: gestire valori mancanti, duplicati e tipi sbagliati

I dati reali sono quasi sempre "sporchi". Simuliamo un dataset con problemi tipici.

```python
import pandas as pd
import numpy as np

# Dataset con problemi intenzionali
dati_sporchi: dict[str, list] = {
    "nome": ["Anna", "Marco", "Anna", "Luca", None, "Sara", "Marco", "Elena"],
    "eta": ["22", "25", "22", "abc", "30", "28", "25", "24"],
    "voto": [28, 25, 28, 30, np.nan, 22, 25, np.nan],
    "corso": ["Stat", "Econ", "Stat", "Stat", "Econ", "stat", "Econ", "STAT"],
}

df: pd.DataFrame = pd.DataFrame(dati_sporchi)
print("=== Dataset originale ===")
print(df)
print()

# 1. Individuare valori mancanti
print("=== Valori mancanti per colonna ===")
print(df.isnull().sum())
print()

# 2. Rimuovere duplicati
print(f"Righe duplicate: {df.duplicated().sum()}")
df_no_dup: pd.DataFrame = df.drop_duplicates()
print(f"Righe dopo rimozione duplicati: {len(df_no_dup)}")
print()

# 3. Correggere tipi sbagliati
# La colonna "eta" e' una stringa, deve diventare un intero
df_pulito: pd.DataFrame = df_no_dup.copy()
df_pulito["eta"] = pd.to_numeric(df_pulito["eta"], errors="coerce")
print("=== Eta dopo conversione (errori -> NaN) ===")
print(df_pulito["eta"])
print()

# 4. Normalizzare stringhe (maiuscole/minuscole inconsistenti)
df_pulito["corso"] = df_pulito["corso"].str.strip().str.capitalize()
print("=== Corsi normalizzati ===")
print(df_pulito["corso"].value_counts())
print()

# 5. Gestire i valori mancanti
# Strategia 1: rimuovere righe con nome mancante
df_pulito = df_pulito.dropna(subset=["nome"])

# Strategia 2: riempire voti mancanti con la mediana
mediana_voto: float = df_pulito["voto"].median()
df_pulito["voto"] = df_pulito["voto"].fillna(mediana_voto)

# Strategia 3: riempire eta mancante con la media
media_eta: float = df_pulito["eta"].mean()
df_pulito["eta"] = df_pulito["eta"].fillna(round(media_eta))

print("=== Dataset pulito ===")
print(df_pulito)
print()
print("Valori mancanti residui:")
print(df_pulito.isnull().sum())
```

### 1.6 Pandas: groupby per statistiche per categoria

Il metodo `groupby` e lo strumento principale per calcolare statistiche suddivise per gruppi, operazione fondamentale nell'analisi statistica.

```python
import pandas as pd

# Ricaricare il dataset pulito
df: pd.DataFrame = pd.read_csv("studenti.csv")

# Statistiche per corso
print("=== Media voto per corso ===")
media_per_corso: pd.DataFrame = (
    df.groupby("corso")["voto_medio"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)
print(media_per_corso)
print()

# Statistiche multiple per corso
print("=== Statistiche multiple per corso ===")
stats_corso: pd.DataFrame = (
    df.groupby("corso")["voto_medio"]
    .agg(["count", "mean", "std", "min", "max"])
    .round(2)
)
print(stats_corso)
print()

# Groupby con piu colonne
print("=== Media voto per corso e anno ===")
media_corso_anno: pd.DataFrame = (
    df.groupby(["corso", "anno"])["voto_medio"]
    .mean()
    .round(2)
    .unstack()
)
print(media_corso_anno)
print()

# Filtro + groupby: media crediti per regione, solo studenti con voto >= 27
bravi: pd.DataFrame = df[df["voto_medio"] >= 27]
print("=== Media crediti studenti con voto >= 27, per regione ===")
crediti_regione: pd.Series = (
    bravi.groupby("regione")["crediti"]
    .mean()
    .round(1)
    .sort_values(ascending=False)
)
print(crediti_regione)
```

---

## Parte 2 — Esercizi autonomi

Risolvete gli esercizi seguenti senza guardare le soluzioni degli esercizi guidati. Usate sempre type hints.

### Base

**Esercizio 1 — Statistiche di un array NumPy**

Create un array NumPy di 1000 valori estratti da una distribuzione normale con media 170 e deviazione standard 8 (simulando altezze in cm). Calcolate e stampate: media, mediana, deviazione standard, minimo, massimo, percentile 5 e percentile 95. Contate quanti valori cadono nell'intervallo [media - 2*std, media + 2*std] e verificate che la percentuale sia vicina al 95%.

**Esercizio 2 — Selezione e filtro con Pandas**

Caricate il file `studenti.csv` creato negli esercizi guidati. Eseguite le seguenti operazioni:
- Selezionate solo le colonne `nome`, `corso`, `voto_medio`.
- Filtrate gli studenti del corso "Statistica" con voto medio superiore a 26.
- Ordinate il risultato per voto medio decrescente.
- Stampate le prime 10 righe.

**Esercizio 3 — Nuova colonna calcolata**

Caricate `studenti.csv` e aggiungete una nuova colonna `fascia_voto` che vale:
- `"insufficiente"` se il voto medio e' sotto 20
- `"sufficiente"` se e' tra 20 e 24 (inclusi)
- `"buono"` se e' tra 25 e 27 (inclusi)
- `"ottimo"` se e' 28 o superiore

Stampate il conteggio per ogni fascia con `value_counts()`.

### Intermedio

**Esercizio 4 — Confronto tra gruppi**

Caricate `studenti.csv` e rispondete alle seguenti domande usando `groupby`:
- Qual e' il corso con la media voti piu alta?
- Qual e' la regione con il numero medio di crediti piu alto?
- C'e' differenza significativa nella media dei voti tra studenti del primo e del terzo anno?

Presentate i risultati in modo chiaro, con stampe formattate.

**Esercizio 5 — Merge di DataFrame**

Create due DataFrame:
1. `esami`: con colonne `id_studente`, `materia`, `voto`, `data` (almeno 20 righe).
2. `anagrafica`: con colonne `id_studente`, `nome`, `cognome`, `corso` (almeno 8 studenti, alcuni con piu esami).

Eseguite un merge (join) tra i due DataFrame sulla colonna `id_studente`. Poi calcolate la media voti per ogni studente e la media voti per ogni materia.

**Esercizio 6 — Pivot table**

Partendo dal DataFrame unito dell'esercizio precedente, create una pivot table che mostri la media dei voti con:
- righe: `corso`
- colonne: `materia`
- valori: `voto` (media)

Usate `pd.pivot_table()`. Sostituite eventuali `NaN` con la stringa `"-"` per la stampa.

### Avanzato

**Esercizio 7 — Sfida: analisi completa di un dataset**

Svolgete un'analisi completa seguendo questo schema:

1. **Creazione del dataset.** Generate un DataFrame di almeno 500 righe che simuli i dati di un'indagine sulla soddisfazione lavorativa, con colonne: `id`, `settore` (Tecnologia, Sanita, Istruzione, Finanza, Commercio), `anni_esperienza` (1-40, distribuzione realistica), `stipendio` (correlato al settore e all'esperienza, con rumore), `soddisfazione` (scala 1-10), `regione`, `titolo_studio` (Diploma, Laurea triennale, Laurea magistrale, Dottorato).

2. **Esplorazione.** Stampate le dimensioni, i tipi, le prime righe, le statistiche descrittive e il conteggio per ogni variabile categoriale.

3. **Pulizia.** Inserite intenzionalmente il 5% di valori mancanti in `stipendio` e `soddisfazione`. Poi gestite i mancanti con strategie appropriate (mediana per stipendio, moda per soddisfazione).

4. **Analisi per gruppi.** Calcolate:
   - Stipendio medio e mediano per settore.
   - Soddisfazione media per titolo di studio.
   - Correlazione tra anni di esperienza e stipendio (usate `np.corrcoef` o il metodo `.corr()` di Pandas).

5. **Export.** Salvate il dataset pulito come CSV e un riepilogo statistico come secondo CSV.

---

## Domande di verifica

1. Qual e' la differenza principale tra una lista Python e un array NumPy? Perche le operazioni NumPy sono piu veloci?

2. Cosa fa il metodo `np.sum(array > 5)`? Perche funziona, dato che il confronto produce booleani?

3. Spiegate la differenza tra `dropna()` e `fillna()` in Pandas. Quando preferireste l'uno all'altro?

4. Qual e' la differenza tra `df["colonna"]` e `df[["colonna"]]`? Che tipo restituisce ciascuna?

5. Come funziona il metodo `groupby`? Descrivete il pattern "split-apply-combine" con un esempio.

6. Cosa succede se fate un merge tra due DataFrame e una chiave del DataFrame sinistro non ha corrispondenza nel destro? Come cambia il risultato con `how="inner"` vs `how="left"`?

7. Perche nel metodo Monte Carlo per stimare pi greco l'errore diminuisce aumentando il numero di punti? A quale velocita diminuisce (in termini di n)?

8. Cosa fa `pd.to_numeric(colonna, errors="coerce")`? Perche e' preferibile a un cast diretto come `colonna.astype(int)`?

---

## Osservazioni finali

In questo laboratorio avete sperimentato due strumenti che trasformano Python da linguaggio di programmazione generico a piattaforma per l'analisi dei dati.

**NumPy** vi ha mostrato il concetto di *vettorizzazione*: sostituire i cicli espliciti con operazioni su interi array. Non e' solo una questione di comodita sintattica, ma di prestazioni: le operazioni NumPy sono tipicamente 50-100 volte piu veloci dei cicli Python equivalenti. Questo perche NumPy delega il lavoro a codice C ottimizzato che opera su blocchi contigui di memoria, sfruttando le istruzioni SIMD del processore.

**Pandas** vi ha dato gli strumenti per l'intero ciclo di vita dei dati tabulari: caricamento, esplorazione, pulizia, trasformazione e aggregazione. Il metodo `groupby`, in particolare, implementa il pattern *split-apply-combine* che e' alla base di gran parte dell'analisi statistica: dividere i dati in gruppi omogenei, applicare una funzione a ciascun gruppo, ricombinare i risultati.

Un punto importante: in questo laboratorio avete visto che i dati reali sono quasi sempre "sporchi" — valori mancanti, tipi sbagliati, stringhe inconsistenti, duplicati. La pulizia dei dati non e' un passaggio preliminare fastidioso, ma una fase critica dell'analisi. Decisioni prese in questa fase (come riempire un valore mancante con la mediana piuttosto che eliminare la riga) possono influenzare significativamente i risultati finali.

Nel prossimo laboratorio aggiungeremo la visualizzazione: imparerete a trasformare numeri e tabelle in grafici che comunicano i risultati in modo immediato ed efficace.
