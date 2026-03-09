# Progetto 3: Analisi dataset meteo

## Introduzione

In questo progetto analizzerai dati meteorologici di tre citta' italiane (Roma, Milano, Napoli) nel mese di gennaio 2024. Imparerai a gestire dati realistici con valori mancanti, a calcolare statistiche, e a creare visualizzazioni. Il progetto copre:

- Lavorare con strutture dati complesse (**F09** - Strutture dati)
- Gestire errori e dati mancanti (**F10** - Gestione errori)
- Usare NumPy per calcoli numerici (**F11** - Librerie scientifiche)
- Organizzare codice con funzioni (**F12**, **F15** - Funzioni)
- Controllare il flusso con condizioni e cicli (**F13** - Controllo di flusso)
- Usare Pandas e Matplotlib (**F17** - Analisi e visualizzazione dati)

Il file `dati_meteo.csv` contiene 90 righe (30 giorni x 3 citta') con le colonne: data, citta, temperatura_max, temperatura_min, pioggia_mm, umidita_pct. Alcuni valori sono mancanti (celle vuote).

---

## Passo 1: Leggere i dati CSV e gestire valori mancanti

### Cosa imparerai
- Leggere file CSV con il modulo `csv`
- Riconoscere e gestire valori mancanti
- Convertire stringhe in numeri con gestione errori

### Spiegazione

I dati reali spesso contengono valori mancanti. Nel nostro CSV, alcuni campi numerici sono vuoti. Dobbiamo gestirli in modo sicuro, senza far crashare il programma.

### Suggerimenti
- Usa `csv.DictReader` per accedere alle colonne per nome
- Crea una funzione `converti_float()` che restituisce `None` se la conversione fallisce
- Conta quanti valori mancanti ci sono per ogni colonna

### Scheletro di codice

```python
import csv
from pathlib import Path

def converti_float(valore):
    """Converte una stringa in float. Restituisce None se vuota o non valida."""
    # TODO: gestisci stringhe vuote e errori di conversione
    pass

def leggi_dati_meteo(percorso):
    """Legge il CSV e restituisce una lista di dizionari con dati convertiti."""
    dati = []
    with open(percorso, 'r', encoding='utf-8') as file:
        lettore = csv.DictReader(file)
        for riga in lettore:
            record = {
                'data': riga['data'],
                'citta': riga['citta'],
                # TODO: converti i campi numerici
            }
            dati.append(record)
    return dati

# Prova
percorso = Path(__file__).parent / "dati_meteo.csv"
dati = leggi_dati_meteo(percorso)
print(f"Letti {len(dati)} record")

# Conta valori mancanti
campi_numerici = ['temperatura_max', 'temperatura_min', 'pioggia_mm', 'umidita_pct']
for campo in campi_numerici:
    mancanti = sum(1 for d in dati if d[campo] is None)
    print(f"  {campo}: {mancanti} valori mancanti")
```

<details>
<summary>Soluzione Passo 1</summary>

```python
import csv
from pathlib import Path

def converti_float(valore):
    """Converte una stringa in float. Restituisce None se vuota o non valida."""
    if valore is None or valore.strip() == '':
        return None
    try:
        return float(valore)
    except ValueError:
        return None

def leggi_dati_meteo(percorso):
    """Legge il CSV e restituisce una lista di dizionari con dati convertiti."""
    dati = []
    with open(percorso, 'r', encoding='utf-8') as file:
        lettore = csv.DictReader(file)
        for riga in lettore:
            record = {
                'data': riga['data'],
                'citta': riga['citta'],
                'temperatura_max': converti_float(riga['temperatura_max']),
                'temperatura_min': converti_float(riga['temperatura_min']),
                'pioggia_mm': converti_float(riga['pioggia_mm']),
                'umidita_pct': converti_float(riga['umidita_pct']),
            }
            dati.append(record)
    return dati

percorso = Path(__file__).parent / "dati_meteo.csv"
dati = leggi_dati_meteo(percorso)
print(f"Letti {len(dati)} record")

campi_numerici = ['temperatura_max', 'temperatura_min', 'pioggia_mm', 'umidita_pct']
for campo in campi_numerici:
    mancanti = sum(1 for d in dati if d[campo] is None)
    print(f"  {campo}: {mancanti} valori mancanti")
```
</details>

---

## Passo 2: Pulizia dei dati e rilevamento anomalie

### Cosa imparerai
- Strategie per gestire valori mancanti (esclusione, imputazione)
- Rilevare outlier con metodi statistici semplici
- Organizzare dati per citta'

### Spiegazione

Ci sono diversi approcci per i valori mancanti:
1. **Escluderli**: ignorare i record incompleti
2. **Imputarli**: sostituirli con la media o la mediana della colonna

Per gli outlier (valori anomali), un metodo semplice e' verificare se un valore si discosta dalla media di piu' di 2 deviazioni standard.

### Suggerimenti
- Raggruppa i dati per citta' usando un dizionario di liste
- Per l'imputazione, calcola la media solo sui valori non-None
- Per gli outlier, calcola media e deviazione standard per citta'

### Scheletro di codice

```python
def raggruppa_per_citta(dati):
    """Raggruppa i record per citta'. Restituisce un dizionario."""
    gruppi = {}
    for record in dati:
        citta = record['citta']
        # TODO: aggiungi il record alla lista della citta'
    return gruppi

def valori_validi(records, campo):
    """Estrae i valori non-None di un campo da una lista di record."""
    # TODO: restituisci solo i valori non-None
    pass

def imputa_valori_mancanti(dati):
    """Sostituisce i None con la media della citta' per quel campo."""
    gruppi = raggruppa_per_citta(dati)
    campi = ['temperatura_max', 'temperatura_min', 'pioggia_mm', 'umidita_pct']

    for citta, records in gruppi.items():
        for campo in campi:
            validi = valori_validi(records, campo)
            if validi:
                media = sum(validi) / len(validi)
                for r in records:
                    if r[campo] is None:
                        r[campo] = round(media, 1)
                        # TODO: stampa un messaggio per tracciare l'imputazione
    return dati
```

<details>
<summary>Soluzione Passo 2</summary>

```python
def raggruppa_per_citta(dati):
    """Raggruppa i record per citta'. Restituisce un dizionario."""
    gruppi = {}
    for record in dati:
        citta = record['citta']
        if citta not in gruppi:
            gruppi[citta] = []
        gruppi[citta].append(record)
    return gruppi

def valori_validi(records, campo):
    """Estrae i valori non-None di un campo da una lista di record."""
    return [r[campo] for r in records if r[campo] is not None]

def imputa_valori_mancanti(dati):
    """Sostituisce i None con la media della citta' per quel campo."""
    gruppi = raggruppa_per_citta(dati)
    campi = ['temperatura_max', 'temperatura_min', 'pioggia_mm', 'umidita_pct']
    contatore_imputazioni = 0

    for citta, records in gruppi.items():
        for campo in campi:
            validi = valori_validi(records, campo)
            if validi:
                media = sum(validi) / len(validi)
                for r in records:
                    if r[campo] is None:
                        r[campo] = round(media, 1)
                        contatore_imputazioni += 1
                        print(f"  Imputato: {citta}, {r['data']}, "
                              f"{campo} = {r[campo]} (media)")

    print(f"  Totale imputazioni: {contatore_imputazioni}")
    return dati

def rileva_outlier(dati, campo, soglia=2.0):
    """Rileva valori anomali che si discostano dalla media di piu' di 'soglia' dev. std."""
    gruppi = raggruppa_per_citta(dati)
    outlier = []

    for citta, records in gruppi.items():
        validi = valori_validi(records, campo)
        if len(validi) < 3:
            continue
        media = sum(validi) / len(validi)
        varianza = sum((x - media) ** 2 for x in validi) / (len(validi) - 1)
        dev_std = varianza ** 0.5

        for r in records:
            val = r[campo]
            if val is not None and abs(val - media) > soglia * dev_std:
                outlier.append({
                    'citta': citta,
                    'data': r['data'],
                    'campo': campo,
                    'valore': val,
                    'media': round(media, 2),
                    'dev_std': round(dev_std, 2),
                })
    return outlier
```
</details>

---

## Passo 3: Analisi con liste e dizionari (Python base)

### Cosa imparerai
- Calcolare statistiche aggregate per gruppi
- Trovare massimi e minimi con informazioni associate
- Confrontare dati tra citta'

### Spiegazione

Prima di usare librerie esterne, e' importante saper fare analisi con gli strumenti base di Python. Calcoleremo: temperatura media per citta', giorno piu' caldo e piu' freddo, pioggia totale per citta', e giorni di pioggia.

### Suggerimenti
- Usa `raggruppa_per_citta()` per lavorare citta' per citta'
- Per trovare il record con il massimo, puoi usare `max()` con `key=`
- Un giorno di pioggia e' quando `pioggia_mm > 0`

### Scheletro di codice

```python
def analisi_base(dati):
    """Esegue un'analisi base dei dati meteo con Python standard."""
    gruppi = raggruppa_per_citta(dati)
    risultati = {}

    for citta, records in gruppi.items():
        temp_max_valori = valori_validi(records, 'temperatura_max')
        temp_min_valori = valori_validi(records, 'temperatura_min')
        pioggia_valori = valori_validi(records, 'pioggia_mm')

        risultati[citta] = {
            # TODO: calcola media temperatura massima
            # TODO: calcola media temperatura minima
            # TODO: trova la temperatura massima assoluta e il giorno
            # TODO: trova la temperatura minima assoluta e il giorno
            # TODO: calcola pioggia totale
            # TODO: conta giorni di pioggia (pioggia_mm > 0)
        }

    return risultati
```

<details>
<summary>Soluzione Passo 3</summary>

```python
def analisi_base(dati):
    """Esegue un'analisi base dei dati meteo con Python standard."""
    gruppi = raggruppa_per_citta(dati)
    risultati = {}

    for citta, records in gruppi.items():
        temp_max_valori = valori_validi(records, 'temperatura_max')
        temp_min_valori = valori_validi(records, 'temperatura_min')
        pioggia_valori = valori_validi(records, 'pioggia_mm')
        umidita_valori = valori_validi(records, 'umidita_pct')

        # Giorno piu' caldo
        record_max = max(
            [r for r in records if r['temperatura_max'] is not None],
            key=lambda r: r['temperatura_max']
        )
        # Giorno piu' freddo
        record_min = min(
            [r for r in records if r['temperatura_min'] is not None],
            key=lambda r: r['temperatura_min']
        )

        giorni_pioggia = sum(1 for v in pioggia_valori if v > 0)

        risultati[citta] = {
            'temp_max_media': round(sum(temp_max_valori) / len(temp_max_valori), 1),
            'temp_min_media': round(sum(temp_min_valori) / len(temp_min_valori), 1),
            'temp_max_assoluta': record_max['temperatura_max'],
            'giorno_piu_caldo': record_max['data'],
            'temp_min_assoluta': record_min['temperatura_min'],
            'giorno_piu_freddo': record_min['data'],
            'pioggia_totale': round(sum(pioggia_valori), 1),
            'giorni_pioggia': giorni_pioggia,
            'giorni_totali': len(records),
            'umidita_media': round(sum(umidita_valori) / len(umidita_valori), 1),
        }

    return risultati

def stampa_analisi_base(risultati):
    """Stampa i risultati dell'analisi in modo formattato."""
    print("\n" + "=" * 60)
    print("  ANALISI METEO - RISULTATI BASE")
    print("=" * 60)

    for citta, stats in risultati.items():
        print(f"\n--- {citta.upper()} ---")
        print(f"  Temperatura massima media: {stats['temp_max_media']}C")
        print(f"  Temperatura minima media:  {stats['temp_min_media']}C")
        print(f"  Giorno piu' caldo: {stats['giorno_piu_caldo']} "
              f"({stats['temp_max_assoluta']}C)")
        print(f"  Giorno piu' freddo: {stats['giorno_piu_freddo']} "
              f"({stats['temp_min_assoluta']}C)")
        print(f"  Pioggia totale: {stats['pioggia_totale']} mm")
        print(f"  Giorni di pioggia: {stats['giorni_pioggia']}/{stats['giorni_totali']}")
        print(f"  Umidita' media: {stats['umidita_media']}%")
```
</details>

---

## Passo 4: Analisi con NumPy

### Cosa imparerai
- Creare array NumPy da liste Python
- Usare funzioni NumPy: `mean()`, `std()`, `min()`, `max()`
- Calcolare correlazioni tra variabili
- Vantaggi di NumPy rispetto al Python base

### Spiegazione

NumPy e' la libreria fondamentale per il calcolo numerico in Python. Gli array NumPy sono piu' efficienti delle liste Python per operazioni matematiche. Useremo NumPy per ricalcolare le statistiche e per calcolare la correlazione tra temperatura e umidita'.

### Suggerimenti
- Importa NumPy con `import numpy as np`
- `np.array()` converte una lista in un array NumPy
- `np.corrcoef()` calcola la matrice di correlazione
- Usa `try/except ImportError` per gestire il caso in cui NumPy non sia installato

### Scheletro di codice

```python
try:
    import numpy as np
    NUMPY_DISPONIBILE = True
except ImportError:
    NUMPY_DISPONIBILE = False
    print("NumPy non installato. Saltare il Passo 4.")

def analisi_numpy(dati):
    """Analisi dei dati meteo usando NumPy."""
    if not NUMPY_DISPONIBILE:
        print("NumPy non disponibile.")
        return

    gruppi = raggruppa_per_citta(dati)

    for citta, records in gruppi.items():
        # TODO: crea array NumPy per ogni campo
        # TODO: calcola media, deviazione standard, min, max
        # TODO: calcola correlazione temperatura-umidita'
        pass
```

<details>
<summary>Soluzione Passo 4</summary>

```python
try:
    import numpy as np
    NUMPY_DISPONIBILE = True
except ImportError:
    NUMPY_DISPONIBILE = False

def analisi_numpy(dati):
    """Analisi dei dati meteo usando NumPy."""
    if not NUMPY_DISPONIBILE:
        print("NumPy non disponibile. Installa con: pip install numpy")
        return None

    print("\n" + "=" * 60)
    print("  ANALISI CON NUMPY")
    print("=" * 60)

    gruppi = raggruppa_per_citta(dati)
    risultati_numpy = {}

    for citta, records in gruppi.items():
        # Crea array NumPy
        temp_max = np.array(valori_validi(records, 'temperatura_max'))
        temp_min = np.array(valori_validi(records, 'temperatura_min'))
        pioggia = np.array(valori_validi(records, 'pioggia_mm'))
        umidita = np.array(valori_validi(records, 'umidita_pct'))

        print(f"\n--- {citta.upper()} ---")

        # Statistiche con NumPy
        print(f"  Temp. max: media={np.mean(temp_max):.1f}, "
              f"std={np.std(temp_max, ddof=1):.1f}, "
              f"min={np.min(temp_max):.1f}, max={np.max(temp_max):.1f}")
        print(f"  Temp. min: media={np.mean(temp_min):.1f}, "
              f"std={np.std(temp_min, ddof=1):.1f}, "
              f"min={np.min(temp_min):.1f}, max={np.max(temp_min):.1f}")
        print(f"  Pioggia:   totale={np.sum(pioggia):.1f} mm, "
              f"media giornaliera={np.mean(pioggia):.1f} mm")

        # Escursione termica giornaliera
        n = min(len(temp_max), len(temp_min))
        escursione = temp_max[:n] - temp_min[:n]
        print(f"  Escursione termica media: {np.mean(escursione):.1f}C")

        # Correlazione temperatura massima - umidita'
        n_corr = min(len(temp_max), len(umidita))
        if n_corr > 2:
            corr = np.corrcoef(temp_max[:n_corr], umidita[:n_corr])[0, 1]
            print(f"  Correlazione temp_max/umidita': {corr:.3f}")

        risultati_numpy[citta] = {
            'temp_max_array': temp_max,
            'temp_min_array': temp_min,
            'pioggia_array': pioggia,
            'escursione_media': round(float(np.mean(escursione)), 1),
        }

    return risultati_numpy
```
</details>

---

## Passo 5: Analisi con Pandas

### Cosa imparerai
- Creare un DataFrame da un file CSV
- Usare `groupby()` per analisi aggregate
- Usare `describe()` per statistiche automatiche
- Gestire valori mancanti con `dropna()` e `fillna()`

### Spiegazione

Pandas e' la libreria di riferimento per l'analisi dati in Python. Il suo oggetto principale, il DataFrame, e' come una tabella di dati con righe e colonne nominate. Pandas rende semplicissime operazioni come raggruppamento, filtraggio e statistiche.

### Suggerimenti
- `pd.read_csv()` legge direttamente il CSV in un DataFrame
- `.groupby('citta')` raggruppa per citta'
- `.describe()` calcola automaticamente le statistiche descrittive
- `.isna()` e `.notna()` identificano i valori mancanti
- `.fillna()` sostituisce i mancanti

### Scheletro di codice

```python
try:
    import pandas as pd
    PANDAS_DISPONIBILE = True
except ImportError:
    PANDAS_DISPONIBILE = False

def analisi_pandas(percorso):
    """Analisi dei dati meteo usando Pandas."""
    if not PANDAS_DISPONIBILE:
        print("Pandas non disponibile.")
        return

    # TODO: leggi il CSV con pd.read_csv()
    # TODO: mostra le prime righe con .head()
    # TODO: mostra info sui dati con .info()
    # TODO: conta i valori mancanti
    # TODO: riempi i valori mancanti con la media per citta'
    # TODO: statistiche descrittive con .describe()
    # TODO: raggruppa per citta' e calcola medie
    pass
```

<details>
<summary>Soluzione Passo 5</summary>

```python
try:
    import pandas as pd
    PANDAS_DISPONIBILE = True
except ImportError:
    PANDAS_DISPONIBILE = False

def analisi_pandas(percorso):
    """Analisi dei dati meteo usando Pandas."""
    if not PANDAS_DISPONIBILE:
        print("Pandas non disponibile. Installa con: pip install pandas")
        return None

    print("\n" + "=" * 60)
    print("  ANALISI CON PANDAS")
    print("=" * 60)

    # Leggi il CSV
    df = pd.read_csv(percorso)
    print(f"\nDimensioni dataset: {df.shape[0]} righe, {df.shape[1]} colonne")

    # Prime righe
    print("\nPrime 5 righe:")
    print(df.head().to_string(index=False))

    # Valori mancanti
    print("\nValori mancanti per colonna:")
    mancanti = df.isna().sum()
    for col, n in mancanti.items():
        if n > 0:
            print(f"  {col}: {n}")

    # Riempi i valori mancanti con la media per citta'
    campi_numerici = ['temperatura_max', 'temperatura_min', 'pioggia_mm', 'umidita_pct']
    for campo in campi_numerici:
        df[campo] = df.groupby('citta')[campo].transform(
            lambda x: x.fillna(x.mean())
        )
    print("\nValori mancanti dopo imputazione:", df.isna().sum().sum())

    # Statistiche descrittive generali
    print("\nStatistiche descrittive:")
    print(df[campi_numerici].describe().round(2).to_string())

    # Statistiche per citta'
    print("\nMedie per citta':")
    medie = df.groupby('citta')[campi_numerici].mean().round(1)
    print(medie.to_string())

    # Pioggia totale per citta'
    print("\nPioggia totale per citta' (mm):")
    pioggia_tot = df.groupby('citta')['pioggia_mm'].sum().round(1)
    for citta, tot in pioggia_tot.items():
        print(f"  {citta}: {tot} mm")

    # Giorni di pioggia per citta'
    print("\nGiorni di pioggia per citta':")
    giorni_pioggia = df[df['pioggia_mm'] > 0].groupby('citta').size()
    for citta, n in giorni_pioggia.items():
        print(f"  {citta}: {n} giorni")

    # Escursione termica
    df['escursione'] = df['temperatura_max'] - df['temperatura_min']
    print("\nEscursione termica media per citta':")
    esc_media = df.groupby('citta')['escursione'].mean().round(1)
    for citta, esc in esc_media.items():
        print(f"  {citta}: {esc}C")

    return df
```
</details>

---

## Passo 6: Visualizzazione con Matplotlib

### Cosa imparerai
- Creare grafici a linee (andamento temporale)
- Creare grafici a barre (confronto tra citta')
- Personalizzare i grafici (titoli, etichette, legende, colori)
- Salvare grafici come file immagine

### Spiegazione

Matplotlib e' la libreria di visualizzazione piu' usata in Python. Creeremo quattro grafici:
1. Andamento della temperatura massima nel tempo per tutte le citta'
2. Confronto pioggia totale tra citta' (grafico a barre)
3. Distribuzione delle temperature (boxplot)
4. Relazione temperatura-umidita' (scatter plot)

### Suggerimenti
- Usa `plt.figure(figsize=(larghezza, altezza))` per impostare le dimensioni
- Usa `plt.savefig()` invece di `plt.show()` per salvare su file
- `plt.tight_layout()` evita che le etichette si sovrappongano
- Chiudi sempre la figura con `plt.close()` dopo il salvataggio

### Scheletro di codice

```python
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_DISPONIBILE = True
except ImportError:
    MATPLOTLIB_DISPONIBILE = False

def crea_grafici(df, cartella_output):
    """Crea e salva i grafici dell'analisi meteo."""
    if not MATPLOTLIB_DISPONIBILE:
        print("Matplotlib non disponibile.")
        return

    # TODO: Grafico 1 - Andamento temperatura massima
    # TODO: Grafico 2 - Pioggia totale per citta' (barre)
    # TODO: Grafico 3 - Boxplot temperature
    # TODO: Grafico 4 - Scatter temperatura vs umidita'
    pass
```

<details>
<summary>Soluzione Passo 6</summary>

```python
try:
    import matplotlib
    matplotlib.use('Agg')  # Backend non interattivo per salvare su file
    import matplotlib.pyplot as plt
    MATPLOTLIB_DISPONIBILE = True
except ImportError:
    MATPLOTLIB_DISPONIBILE = False

def crea_grafici(df, cartella_output):
    """Crea e salva i grafici dell'analisi meteo."""
    if not MATPLOTLIB_DISPONIBILE:
        print("Matplotlib non disponibile. Installa con: pip install matplotlib")
        return
    if df is None:
        print("Nessun DataFrame disponibile per i grafici.")
        return

    print("\n" + "=" * 60)
    print("  CREAZIONE GRAFICI")
    print("=" * 60)

    citta_lista = df['citta'].unique()
    colori = {'Roma': '#e74c3c', 'Milano': '#3498db', 'Napoli': '#2ecc71'}

    # --- Grafico 1: Andamento temperatura massima ---
    fig, ax = plt.subplots(figsize=(12, 5))
    for citta in citta_lista:
        dati_citta = df[df['citta'] == citta].sort_values('data')
        giorni = range(1, len(dati_citta) + 1)
        ax.plot(giorni, dati_citta['temperatura_max'],
                label=citta, color=colori.get(citta, None),
                marker='o', markersize=3, linewidth=1.5)
    ax.set_xlabel('Giorno di gennaio 2024')
    ax.set_ylabel('Temperatura massima (C)')
    ax.set_title('Andamento temperatura massima - Gennaio 2024')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    percorso1 = cartella_output / "grafico_temperatura.png"
    plt.savefig(percorso1, dpi=150)
    plt.close()
    print(f"  Salvato: {percorso1.name}")

    # --- Grafico 2: Pioggia totale per citta' (barre) ---
    fig, ax = plt.subplots(figsize=(8, 5))
    pioggia_tot = df.groupby('citta')['pioggia_mm'].sum()
    barre = ax.bar(pioggia_tot.index, pioggia_tot.values,
                   color=[colori.get(c, '#95a5a6') for c in pioggia_tot.index])
    for barra, valore in zip(barre, pioggia_tot.values):
        ax.text(barra.get_x() + barra.get_width() / 2, barra.get_height() + 1,
                f'{valore:.1f}', ha='center', va='bottom', fontsize=11)
    ax.set_ylabel('Pioggia totale (mm)')
    ax.set_title('Pioggia totale per citta\' - Gennaio 2024')
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    percorso2 = cartella_output / "grafico_pioggia.png"
    plt.savefig(percorso2, dpi=150)
    plt.close()
    print(f"  Salvato: {percorso2.name}")

    # --- Grafico 3: Boxplot temperature per citta' ---
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Boxplot temp max
    dati_box_max = [df[df['citta'] == c]['temperatura_max'].dropna().values
                    for c in citta_lista]
    bp1 = axes[0].boxplot(dati_box_max, labels=citta_lista, patch_artist=True)
    for patch, citta in zip(bp1['boxes'], citta_lista):
        patch.set_facecolor(colori.get(citta, '#95a5a6'))
        patch.set_alpha(0.6)
    axes[0].set_ylabel('Temperatura (C)')
    axes[0].set_title('Distribuzione temperatura massima')
    axes[0].grid(axis='y', alpha=0.3)

    # Boxplot temp min
    dati_box_min = [df[df['citta'] == c]['temperatura_min'].dropna().values
                    for c in citta_lista]
    bp2 = axes[1].boxplot(dati_box_min, labels=citta_lista, patch_artist=True)
    for patch, citta in zip(bp2['boxes'], citta_lista):
        patch.set_facecolor(colori.get(citta, '#95a5a6'))
        patch.set_alpha(0.6)
    axes[1].set_ylabel('Temperatura (C)')
    axes[1].set_title('Distribuzione temperatura minima')
    axes[1].grid(axis='y', alpha=0.3)

    plt.tight_layout()
    percorso3 = cartella_output / "grafico_boxplot.png"
    plt.savefig(percorso3, dpi=150)
    plt.close()
    print(f"  Salvato: {percorso3.name}")

    # --- Grafico 4: Scatter temperatura vs umidita' ---
    fig, ax = plt.subplots(figsize=(8, 6))
    for citta in citta_lista:
        dati_citta = df[df['citta'] == citta]
        ax.scatter(dati_citta['temperatura_max'], dati_citta['umidita_pct'],
                   label=citta, color=colori.get(citta, None),
                   alpha=0.7, s=40)
    ax.set_xlabel('Temperatura massima (C)')
    ax.set_ylabel('Umidita\' (%)')
    ax.set_title('Relazione temperatura massima - umidita\'')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    percorso4 = cartella_output / "grafico_scatter.png"
    plt.savefig(percorso4, dpi=150)
    plt.close()
    print(f"  Salvato: {percorso4.name}")

    print("\nTutti i grafici sono stati salvati nella cartella del progetto.")
```
</details>

---

## Complimenti!

Hai completato il Progetto 3. Ora sai:
- Leggere e pulire dati reali con valori mancanti
- Rilevare anomalie nei dati
- Analizzare dati con Python base, NumPy e Pandas
- Creare visualizzazioni con Matplotlib
- Gestire dipendenze opzionali con `try/except ImportError`

La soluzione completa e' nel file `soluzione.py`. I grafici generati vengono salvati come file PNG nella cartella del progetto.
