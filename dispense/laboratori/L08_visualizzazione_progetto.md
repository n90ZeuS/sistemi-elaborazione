# Laboratorio 8 — Visualizzazione e progetto riepilogativo

**Prerequisiti:** Frontale F17 (NumPy, Pandas, analisi dati), Laboratorio 7

---

## Obiettivo del laboratorio

Questo laboratorio ha due parti. Nella prima imparerete a creare grafici con **Matplotlib** e **Seaborn**, le librerie di visualizzazione piu usate in Python. Nella seconda, un **mini-progetto riepilogativo** vi chiedera di combinare tutto cio che avete appreso nel corso: funzioni, type hints, strutture dati, file, Pandas e visualizzazione.

---

## Parte 1 — Esercizi guidati: visualizzazione

### 1.1 Matplotlib: istogramma, scatter plot, grafico a barre

Matplotlib e la libreria di visualizzazione di riferimento. Il modulo `pyplot` offre un'interfaccia simile a MATLAB.

```python
import matplotlib.pyplot as plt
import numpy as np

# Generare dati
rng: np.random.Generator = np.random.default_rng(seed=42)
altezze: np.ndarray = rng.normal(loc=170, scale=10, size=500)

# --- Istogramma ---
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(altezze, bins=25, color="steelblue", edgecolor="white", alpha=0.8)
ax.set_title("Distribuzione delle altezze")
ax.set_xlabel("Altezza (cm)")
ax.set_ylabel("Frequenza")
plt.tight_layout()
plt.savefig("istogramma_altezze.png", dpi=150)
plt.show()
```

```python
import matplotlib.pyplot as plt
import numpy as np

# --- Scatter plot ---
rng: np.random.Generator = np.random.default_rng(seed=42)
ore_studio: np.ndarray = rng.uniform(2, 40, size=100)
voti: np.ndarray = 18 + 0.3 * ore_studio + rng.normal(0, 2, size=100)
voti = np.clip(voti, 18, 30)

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(ore_studio, voti, alpha=0.6, color="coral", edgecolors="darkred", s=40)
ax.set_title("Ore di studio vs voto")
ax.set_xlabel("Ore di studio settimanali")
ax.set_ylabel("Voto medio")
plt.tight_layout()
plt.savefig("scatter_studio_voti.png", dpi=150)
plt.show()
```

```python
import matplotlib.pyplot as plt
import numpy as np

# --- Grafico a barre ---
corsi: list[str] = ["Statistica", "Economia", "Sociologia", "Informatica"]
media_voti: list[float] = [26.3, 24.8, 25.1, 27.2]

fig, ax = plt.subplots(figsize=(8, 5))
colori: list[str] = ["#4C72B0", "#55A868", "#C44E52", "#8172B2"]
barre = ax.bar(corsi, media_voti, color=colori, edgecolor="black", width=0.6)

# Aggiungere etichette sopra le barre
for barra, valore in zip(barre, media_voti):
    ax.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height() + 0.1,
        f"{valore:.1f}",
        ha="center", va="bottom", fontsize=11
    )

ax.set_title("Voto medio per corso di laurea")
ax.set_ylabel("Voto medio")
ax.set_ylim(22, 29)
plt.tight_layout()
plt.savefig("barre_corsi.png", dpi=150)
plt.show()
```

### 1.2 Personalizzazione: titoli, etichette, legende, colori, griglia

Un grafico senza etichette e un grafico inutile. Vediamo come personalizzare ogni aspetto.

```python
import matplotlib.pyplot as plt
import numpy as np

rng: np.random.Generator = np.random.default_rng(seed=42)
x: np.ndarray = np.linspace(0, 10, 100)
y1: np.ndarray = np.sin(x)
y2: np.ndarray = np.cos(x)
y3: np.ndarray = np.sin(x) * np.exp(-x / 5)

fig, ax = plt.subplots(figsize=(10, 6))

# Tre linee con stili diversi
ax.plot(x, y1, color="#E74C3C", linewidth=2, linestyle="-",
        label="sin(x)")
ax.plot(x, y2, color="#3498DB", linewidth=2, linestyle="--",
        label="cos(x)")
ax.plot(x, y3, color="#2ECC71", linewidth=2, linestyle="-.",
        label="sin(x) · e^(-x/5)")

# Personalizzazione
ax.set_title("Funzioni trigonometriche", fontsize=16, fontweight="bold")
ax.set_xlabel("x", fontsize=13)
ax.set_ylabel("f(x)", fontsize=13)
ax.legend(fontsize=11, loc="upper right", framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle="--")
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.axhline(y=0, color="black", linewidth=0.5)
ax.tick_params(labelsize=11)

plt.tight_layout()
plt.savefig("funzioni_personalizzate.png", dpi=150)
plt.show()
```

### 1.3 Seaborn: boxplot per confronto gruppi e heatmap

Seaborn e costruita sopra Matplotlib e semplifica la creazione di grafici statistici. Lavora direttamente con i DataFrame Pandas.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Creare un dataset di esempio
rng: np.random.Generator = np.random.default_rng(seed=42)
n: int = 300
df: pd.DataFrame = pd.DataFrame({
    "corso": rng.choice(
        ["Statistica", "Economia", "Sociologia", "Informatica"],
        size=n
    ),
    "voto": np.round(rng.normal(25, 3, size=n).clip(18, 30), 1),
    "ore_studio": np.round(rng.exponential(15, size=n).clip(2, 45), 1),
    "eta": rng.integers(19, 35, size=n),
    "stipendio_atteso": np.round(
        rng.normal(28000, 5000, size=n).clip(15000, 50000), 0
    ),
})

# --- Boxplot: confronto voti per corso ---
fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(
    data=df,
    x="corso",
    y="voto",
    palette="Set2",
    ax=ax
)
ax.set_title("Distribuzione dei voti per corso", fontsize=14)
ax.set_xlabel("Corso di laurea")
ax.set_ylabel("Voto medio")
plt.tight_layout()
plt.savefig("boxplot_voti_corso.png", dpi=150)
plt.show()
```

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Riutilizziamo il DataFrame df creato sopra (o ricrearlo)
rng: np.random.Generator = np.random.default_rng(seed=42)
n: int = 300
df: pd.DataFrame = pd.DataFrame({
    "voto": np.round(rng.normal(25, 3, size=n).clip(18, 30), 1),
    "ore_studio": np.round(rng.exponential(15, size=n).clip(2, 45), 1),
    "eta": rng.integers(19, 35, size=n),
    "stipendio_atteso": np.round(
        rng.normal(28000, 5000, size=n).clip(15000, 50000), 0
    ),
})

# --- Heatmap della matrice di correlazione ---
colonne_numeriche: list[str] = ["voto", "ore_studio", "eta", "stipendio_atteso"]
matrice_corr: pd.DataFrame = df[colonne_numeriche].corr()

fig, ax = plt.subplots(figsize=(7, 6))
sns.heatmap(
    matrice_corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    square=True,
    linewidths=1,
    ax=ax
)
ax.set_title("Matrice di correlazione", fontsize=14)
plt.tight_layout()
plt.savefig("heatmap_correlazione.png", dpi=150)
plt.show()
```

### 1.4 Subplots: quattro grafici in una figura (dashboard)

Combinare piu grafici in una sola figura e essenziale per creare dashboard sintetiche.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Generare il dataset
rng: np.random.Generator = np.random.default_rng(seed=42)
n: int = 400
df: pd.DataFrame = pd.DataFrame({
    "corso": rng.choice(
        ["Statistica", "Economia", "Sociologia", "Informatica"],
        size=n
    ),
    "voto": np.round(rng.normal(25, 3, size=n).clip(18, 30), 1),
    "ore_studio": np.round(rng.exponential(15, size=n).clip(2, 45), 1),
    "eta": rng.integers(19, 35, size=n),
    "stipendio_atteso": np.round(
        rng.normal(28000, 5000, size=n).clip(15000, 50000), 0
    ),
})

# Creare una figura con 4 sottografici (2x2)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Dashboard: analisi studenti universitari",
             fontsize=16, fontweight="bold", y=1.02)

# Pannello 1: istogramma dei voti
axes[0, 0].hist(df["voto"], bins=20, color="steelblue",
                edgecolor="white", alpha=0.8)
axes[0, 0].set_title("Distribuzione dei voti")
axes[0, 0].set_xlabel("Voto medio")
axes[0, 0].set_ylabel("Frequenza")
axes[0, 0].axvline(df["voto"].mean(), color="red",
                   linestyle="--", label=f"Media: {df['voto'].mean():.1f}")
axes[0, 0].legend()

# Pannello 2: boxplot per corso
sns.boxplot(data=df, x="corso", y="voto", palette="Set2",
            ax=axes[0, 1])
axes[0, 1].set_title("Voti per corso")
axes[0, 1].set_xlabel("")
axes[0, 1].tick_params(axis="x", rotation=30)

# Pannello 3: scatter ore studio vs voto
axes[1, 0].scatter(df["ore_studio"], df["voto"],
                   alpha=0.4, color="coral", s=20)
axes[1, 0].set_title("Ore di studio vs voto")
axes[1, 0].set_xlabel("Ore di studio settimanali")
axes[1, 0].set_ylabel("Voto medio")

# Pannello 4: grafico a barre del conteggio per corso
conteggi: pd.Series = df["corso"].value_counts()
axes[1, 1].bar(conteggi.index, conteggi.values,
               color=["#4C72B0", "#55A868", "#C44E52", "#8172B2"],
               edgecolor="black")
axes[1, 1].set_title("Numero studenti per corso")
axes[1, 1].set_ylabel("Conteggio")
axes[1, 1].tick_params(axis="x", rotation=30)

plt.tight_layout()
plt.savefig("dashboard_studenti.png", dpi=150, bbox_inches="tight")
plt.show()
```

---

## Parte 2 — Mini-progetto riepilogativo

Questo progetto vi chiede di svolgere un'analisi end-to-end di un dataset, integrando tutte le competenze acquisite nel corso. Il codice deve essere organizzato in **funzioni** con **type hints** e **docstring**.

### Istruzioni

Costruite un programma completo che esegue i cinque passi descritti di seguito. Ogni passo deve essere implementato in una o piu funzioni dedicate. Il programma principale (blocco `if __name__ == "__main__"`) deve richiamare le funzioni in sequenza.

#### Passo 1 — Generazione e caricamento del dataset

Create (o caricate) un dataset CSV che simuli un'indagine su 500 dipendenti di diverse aziende. Il dataset deve contenere almeno le seguenti colonne:

| Colonna | Tipo | Descrizione |
|---------|------|-------------|
| `id` | int | Identificativo univoco |
| `settore` | str | Tecnologia, Sanita, Istruzione, Finanza, Commercio |
| `ruolo` | str | Junior, Mid, Senior, Manager |
| `anni_esperienza` | int | Da 0 a 35 |
| `stipendio` | float | In euro, correlato a settore e esperienza |
| `soddisfazione` | int | Scala 1-10 |
| `ore_settimanali` | float | Ore lavorate a settimana |
| `regione` | str | Almeno 5 regioni italiane |

Scrivete una funzione che genera il dataset e lo salva come CSV:

```python
def genera_dataset(n: int, percorso: str, seed: int = 42) -> pd.DataFrame:
    """Genera un dataset simulato di dipendenti e lo salva come CSV.

    Args:
        n: Numero di righe da generare.
        percorso: Percorso del file CSV di output.
        seed: Seed per la riproducibilita.

    Returns:
        Il DataFrame generato.
    """
    ...
```

Scrivete una funzione separata per il caricamento:

```python
def carica_dataset(percorso: str) -> pd.DataFrame:
    """Carica il dataset da un file CSV.

    Args:
        percorso: Percorso del file CSV.

    Returns:
        Il DataFrame caricato.
    """
    ...
```

#### Passo 2 — Esplorazione

Scrivete una funzione che stampa un riepilogo completo del dataset:

```python
def esplora_dataset(df: pd.DataFrame) -> None:
    """Stampa un riepilogo esplorativo del dataset.

    Mostra: dimensioni, tipi delle colonne, prime righe,
    statistiche descrittive, conteggio valori per ogni
    colonna categoriale, conteggio valori mancanti.

    Args:
        df: Il DataFrame da esplorare.
    """
    ...
```

#### Passo 3 — Pulizia

Inserite intenzionalmente dei "difetti" nel dataset (5-10% di valori mancanti nello stipendio, qualche valore anomalo nelle ore settimanali, stringhe con capitalizzazione inconsistente nei settori). Poi scrivete una funzione che pulisce il dataset:

```python
def pulisci_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Pulisce il dataset: gestisce mancanti, anomali, inconsistenze.

    Strategia:
    - Stipendio mancante: sostituito con la mediana del settore.
    - Ore settimanali > 80 o < 5: sostituite con la mediana.
    - Stringhe: normalizzate con strip() e capitalize().

    Args:
        df: Il DataFrame da pulire.

    Returns:
        Il DataFrame pulito.
    """
    ...
```

#### Passo 4 — Analisi per gruppi

Scrivete una funzione che produce le statistiche richieste:

```python
def analisi_per_gruppi(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Calcola statistiche aggregate per diversi raggruppamenti.

    Analisi da produrre:
    - Stipendio medio e mediano per settore.
    - Soddisfazione media per ruolo.
    - Stipendio medio per settore e ruolo (pivot table).
    - Correlazione tra anni_esperienza, stipendio e soddisfazione.

    Args:
        df: Il DataFrame pulito.

    Returns:
        Dizionario con nome analisi -> DataFrame risultato.
    """
    ...
```

#### Passo 5 — Visualizzazioni

Scrivete una funzione che crea una dashboard con 4 grafici in una singola figura:

```python
def crea_dashboard(df: pd.DataFrame, percorso_output: str) -> None:
    """Crea una dashboard con 4 grafici e la salva come immagine.

    Grafici:
    1. Istogramma della distribuzione degli stipendi.
    2. Boxplot degli stipendi per settore.
    3. Scatter plot anni_esperienza vs stipendio, colorato per settore.
    4. Heatmap della correlazione tra variabili numeriche.

    Args:
        df: Il DataFrame pulito.
        percorso_output: Percorso del file immagine di output.
    """
    ...
```

#### Struttura del programma principale

Il programma completo deve avere questa struttura:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Le funzioni definite sopra: genera_dataset, carica_dataset,
# esplora_dataset, pulisci_dataset, analisi_per_gruppi, crea_dashboard


def main() -> None:
    """Funzione principale: esegue l'analisi completa."""
    # 1. Generazione
    percorso_csv: str = "dipendenti.csv"
    df: pd.DataFrame = genera_dataset(500, percorso_csv)

    # 2. Caricamento (per dimostrare il ciclo salva/carica)
    df = carica_dataset(percorso_csv)

    # 3. Esplorazione
    esplora_dataset(df)

    # 4. Pulizia
    df_pulito: pd.DataFrame = pulisci_dataset(df)

    # 5. Analisi
    risultati: dict[str, pd.DataFrame] = analisi_per_gruppi(df_pulito)
    for nome, tabella in risultati.items():
        print(f"\n{'=' * 50}")
        print(f"  {nome}")
        print(f"{'=' * 50}")
        print(tabella)

    # 6. Visualizzazione
    crea_dashboard(df_pulito, "dashboard_dipendenti.png")

    # 7. Export risultati
    df_pulito.to_csv("dipendenti_pulito.csv", index=False)
    print("\nDataset pulito salvato come 'dipendenti_pulito.csv'")


if __name__ == "__main__":
    main()
```

#### Criteri di qualita

Il progetto e completo quando:

- [ ] Ogni funzione ha type hints su tutti i parametri e sul valore di ritorno.
- [ ] Ogni funzione ha una docstring che spiega cosa fa, i parametri e il valore restituito.
- [ ] Il dataset generato e realistico (correlazione stipendio-esperienza, stipendi diversi per settore).
- [ ] La pulizia gestisce almeno tre tipi di problema (mancanti, anomali, inconsistenze).
- [ ] L'analisi produce almeno 4 tabelle statistiche di riepilogo.
- [ ] La dashboard contiene 4 grafici diversi, tutti con titolo, etichette e legende.
- [ ] Il programma e eseguibile da terminale senza errori.
- [ ] Il codice non contiene variabili globali: tutto passa attraverso parametri e valori di ritorno.

---

## Parte 3 — Interpretazione dei risultati

Dopo aver completato il mini-progetto, rispondete per iscritto alle seguenti domande, basandovi sui risultati della vostra analisi:

1. Quale settore ha lo stipendio medio piu alto? E' anche quello con la soddisfazione piu alta? Se no, come lo spiegate?

2. Osservando lo scatter plot esperienza-stipendio, la relazione vi sembra lineare? Ci sono pattern diversi per settori diversi?

3. Dalla heatmap di correlazione, quali coppie di variabili sono piu correlate? Quali sono indipendenti?

4. I boxplot mostrano outlier? In quale settore la variabilita degli stipendi e maggiore? Cosa potrebbe significare?

5. Se doveste comunicare i risultati a un committente non tecnico, quali due grafici scegliereste e perche?

---

## Domande di verifica

1. Qual e' la differenza tra `plt.plot()` e `ax.plot()`? Perche l'approccio con `fig, ax = plt.subplots()` e preferibile?

2. Cosa fa il parametro `alpha` nei grafici? Quando e' utile?

3. Spiegate la differenza tra un istogramma e un grafico a barre. Quando si usa l'uno e quando l'altro?

4. Perche la heatmap di correlazione ha sempre 1.0 sulla diagonale? Cosa indica un valore vicino a 0?

5. In un boxplot, cosa rappresentano la linea centrale, i bordi della scatola, i "baffi" e i punti isolati?

6. Qual e' il vantaggio di organizzare il codice in funzioni piuttosto che scriverlo in un unico blocco sequenziale?

7. Perche `plt.tight_layout()` e importante? Cosa succede se non lo usate con i subplots?

8. Cosa significa `dpi=150` in `plt.savefig()`? Quando usereste un valore piu alto?

---

## Osservazioni finali

Con questo laboratorio si chiude il percorso pratico del corso. Ripercorriamo la strada fatta.

Siete partiti dai **primi passi in Python**: variabili, tipi, assegnamenti. Avete poi imparato a far prendere **decisioni** ai programmi con le strutture condizionali, e a **ripetere operazioni** con i cicli. Avete organizzato il codice in **funzioni** riutilizzabili, e avete scoperto le **strutture dati** fondamentali — liste, dizionari, tuple, insiemi — che permettono di modellare informazioni complesse. Avete imparato a far dialogare i programmi con il **filesystem**, leggendo e scrivendo file CSV e JSON, e a proteggervi dagli errori con le **eccezioni**. Infine, in questi ultimi due laboratori, avete usato **NumPy** per il calcolo vettorizzato, **Pandas** per l'analisi tabellare, e **Matplotlib/Seaborn** per la visualizzazione.

Il mini-progetto di oggi vi ha chiesto di mettere insieme tutti questi pezzi in un programma coerente. Questa capacita di integrazione e esattamente cio che vi servira nella pratica: un'analisi statistica reale non e mai "solo" caricare un file, o "solo" fare un grafico. E un flusso che parte dai dati grezzi e arriva a risultati interpretabili, passando per pulizia, trasformazione, calcolo e comunicazione visiva.

Tre lezioni da portare con se:

1. **I dati vanno sempre esplorati prima di analizzarli.** Un `head()`, un `describe()`, un istogramma: bastano pochi secondi per evitare ore di lavoro su dati sbagliati.

2. **Il codice deve essere organizzato in funzioni con interfacce chiare.** Type hints e docstring non sono un lusso: sono il modo in cui il codice comunica le proprie intenzioni a chi lo legge (incluso il vostro se futuro).

3. **Un grafico senza etichette e un grafico inutile.** Titolo, assi, legenda, unita di misura: ogni grafico deve essere comprensibile anche senza leggere il codice che lo ha generato.

Il linguaggio e le librerie sono strumenti. La vera competenza e saper formulare la domanda giusta, scegliere l'analisi appropriata e comunicare il risultato in modo onesto e chiaro. Buon lavoro.
