"""
Progetto 3: Analisi dataset meteo
====================================
Questo programma analizza dati meteorologici di tre citta' italiane
(Roma, Milano, Napoli) nel mese di gennaio 2024.
Include analisi con Python base, NumPy, Pandas e visualizzazioni Matplotlib.

Argomenti trattati: F09, F10, F11, F12, F13, F15, F17
"""

import csv
from pathlib import Path

# Importazioni opzionali: il programma funziona anche senza queste librerie
try:
    import numpy as np
    NUMPY_DISPONIBILE = True
except ImportError:
    NUMPY_DISPONIBILE = False

try:
    import pandas as pd
    PANDAS_DISPONIBILE = True
except ImportError:
    PANDAS_DISPONIBILE = False

try:
    import matplotlib
    matplotlib.use('Agg')  # Backend non interattivo (salva su file senza finestra)
    import matplotlib.pyplot as plt
    MATPLOTLIB_DISPONIBILE = True
except ImportError:
    MATPLOTLIB_DISPONIBILE = False


# ===========================================================================
# Passo 1: Lettura dati CSV
# ===========================================================================

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


# ===========================================================================
# Passo 2: Pulizia dati e rilevamento anomalie
# ===========================================================================

def raggruppa_per_citta(dati):
    """Raggruppa i record per citta'. Restituisce un dizionario di liste."""
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
    contatore = 0

    for citta, records in gruppi.items():
        for campo in campi:
            validi = valori_validi(records, campo)
            if validi:
                media = sum(validi) / len(validi)
                for r in records:
                    if r[campo] is None:
                        r[campo] = round(media, 1)
                        contatore += 1
                        print(f"  Imputato: {citta}, {r['data']}, "
                              f"{campo} = {r[campo]} (media)")

    print(f"  Totale imputazioni: {contatore}")
    return dati


def rileva_outlier(dati, campo, soglia=2.0):
    """Rileva valori che si discostano dalla media di piu' di 'soglia' deviazioni standard."""
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


# ===========================================================================
# Passo 3: Analisi con Python base
# ===========================================================================

def analisi_base(dati):
    """Esegue un'analisi base dei dati meteo con Python standard."""
    gruppi = raggruppa_per_citta(dati)
    risultati = {}

    for citta, records in gruppi.items():
        temp_max_valori = valori_validi(records, 'temperatura_max')
        temp_min_valori = valori_validi(records, 'temperatura_min')
        pioggia_valori = valori_validi(records, 'pioggia_mm')
        umidita_valori = valori_validi(records, 'umidita_pct')

        # Giorno piu' caldo (con temperatura massima piu' alta)
        record_max = max(
            [r for r in records if r['temperatura_max'] is not None],
            key=lambda r: r['temperatura_max']
        )
        # Giorno piu' freddo (con temperatura minima piu' bassa)
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
    print("  ANALISI METEO - RISULTATI BASE (Python standard)")
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


# ===========================================================================
# Passo 4: Analisi con NumPy
# ===========================================================================

def analisi_numpy(dati):
    """Analisi dei dati meteo usando NumPy."""
    if not NUMPY_DISPONIBILE:
        print("\nNumPy non disponibile. Installa con: pip install numpy")
        return None

    print("\n" + "=" * 60)
    print("  ANALISI CON NUMPY")
    print("=" * 60)

    gruppi = raggruppa_per_citta(dati)
    risultati_numpy = {}

    for citta, records in gruppi.items():
        # Crea array NumPy dai valori validi
        temp_max = np.array(valori_validi(records, 'temperatura_max'))
        temp_min = np.array(valori_validi(records, 'temperatura_min'))
        pioggia = np.array(valori_validi(records, 'pioggia_mm'))
        umidita = np.array(valori_validi(records, 'umidita_pct'))

        print(f"\n--- {citta.upper()} ---")

        # Statistiche descrittive con NumPy
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
            if corr < -0.5:
                print("    -> Correlazione negativa: giorni caldi tendono a essere meno umidi")
            elif corr > 0.5:
                print("    -> Correlazione positiva: giorni caldi tendono a essere piu' umidi")
            else:
                print("    -> Correlazione debole")

        risultati_numpy[citta] = {
            'temp_max_array': temp_max,
            'temp_min_array': temp_min,
            'pioggia_array': pioggia,
            'escursione_media': round(float(np.mean(escursione)), 1),
        }

    return risultati_numpy


# ===========================================================================
# Passo 5: Analisi con Pandas
# ===========================================================================

def analisi_pandas(percorso):
    """Analisi dei dati meteo usando Pandas."""
    if not PANDAS_DISPONIBILE:
        print("\nPandas non disponibile. Installa con: pip install pandas")
        return None

    print("\n" + "=" * 60)
    print("  ANALISI CON PANDAS")
    print("=" * 60)

    # Leggi il CSV direttamente in un DataFrame
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
    print(f"\nValori mancanti dopo imputazione: {df.isna().sum().sum()}")

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


# ===========================================================================
# Passo 6: Visualizzazione con Matplotlib
# ===========================================================================

def crea_grafici(df, cartella_output):
    """Crea e salva i grafici dell'analisi meteo."""
    if not MATPLOTLIB_DISPONIBILE:
        print("\nMatplotlib non disponibile. Installa con: pip install matplotlib")
        return
    if df is None:
        print("\nNessun DataFrame disponibile per i grafici (Pandas richiesto).")
        return

    print("\n" + "=" * 60)
    print("  CREAZIONE GRAFICI")
    print("=" * 60)

    citta_lista = df['citta'].unique()
    colori = {'Roma': '#e74c3c', 'Milano': '#3498db', 'Napoli': '#2ecc71'}

    # --- Grafico 1: Andamento temperatura massima nel tempo ---
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

    # Boxplot temperatura massima
    dati_box_max = [df[df['citta'] == c]['temperatura_max'].dropna().values
                    for c in citta_lista]
    bp1 = axes[0].boxplot(dati_box_max, labels=citta_lista, patch_artist=True)
    for patch, citta in zip(bp1['boxes'], citta_lista):
        patch.set_facecolor(colori.get(citta, '#95a5a6'))
        patch.set_alpha(0.6)
    axes[0].set_ylabel('Temperatura (C)')
    axes[0].set_title('Distribuzione temperatura massima')
    axes[0].grid(axis='y', alpha=0.3)

    # Boxplot temperatura minima
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


# ===========================================================================
# Funzione principale
# ===========================================================================

def main():
    """Funzione principale che coordina tutte le analisi."""
    cartella_progetto = Path(__file__).parent
    percorso_csv = cartella_progetto / "dati_meteo.csv"

    print("=" * 60)
    print("  PROGETTO 3: ANALISI DATASET METEO")
    print("=" * 60)

    # Mostra quali librerie sono disponibili
    print(f"\nLibrerie disponibili:")
    print(f"  NumPy:      {'si' if NUMPY_DISPONIBILE else 'no'}")
    print(f"  Pandas:     {'si' if PANDAS_DISPONIBILE else 'no'}")
    print(f"  Matplotlib: {'si' if MATPLOTLIB_DISPONIBILE else 'no'}")

    # --- Passo 1: Lettura dati ---
    print("\n--- PASSO 1: Lettura dati ---")
    dati = leggi_dati_meteo(percorso_csv)
    print(f"Letti {len(dati)} record")

    # Conta valori mancanti
    campi_numerici = ['temperatura_max', 'temperatura_min', 'pioggia_mm', 'umidita_pct']
    print("Valori mancanti:")
    for campo in campi_numerici:
        mancanti = sum(1 for d in dati if d[campo] is None)
        if mancanti > 0:
            print(f"  {campo}: {mancanti}")

    # --- Passo 2: Pulizia dati ---
    print("\n--- PASSO 2: Pulizia dati ---")
    dati = imputa_valori_mancanti(dati)

    # Rilevamento outlier
    print("\nRicerca outlier (soglia: 2 dev. std.):")
    outlier_trovati = False
    for campo in campi_numerici:
        outlier = rileva_outlier(dati, campo)
        for o in outlier:
            outlier_trovati = True
            print(f"  {o['citta']}, {o['data']}: {o['campo']}={o['valore']} "
                  f"(media={o['media']}, std={o['dev_std']})")
    if not outlier_trovati:
        print("  Nessun outlier rilevato.")

    # --- Passo 3: Analisi base ---
    print("\n--- PASSO 3: Analisi base ---")
    risultati_base = analisi_base(dati)
    stampa_analisi_base(risultati_base)

    # --- Passo 4: Analisi NumPy ---
    print("\n--- PASSO 4: Analisi NumPy ---")
    analisi_numpy(dati)

    # --- Passo 5: Analisi Pandas ---
    print("\n--- PASSO 5: Analisi Pandas ---")
    df = analisi_pandas(percorso_csv)

    # --- Passo 6: Grafici ---
    print("\n--- PASSO 6: Grafici ---")
    crea_grafici(df, cartella_progetto)

    print("\n" + "=" * 60)
    print("  Analisi completata!")
    print("=" * 60)


if __name__ == "__main__":
    main()
