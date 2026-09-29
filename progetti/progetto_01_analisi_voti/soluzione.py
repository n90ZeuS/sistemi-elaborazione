"""
Progetto 1: Analisi voti di un corso
=====================================
Questo programma legge i voti degli studenti da un file CSV,
calcola statistiche descrittive, classifica gli studenti
e genera un report testuale salvato su file.

Argomenti trattati: T07, T09, T11, T13, T15
"""

import csv
import statistics
from pathlib import Path


# ---------------------------------------------------------------------------
# Passo 1: Lettura del file CSV
# ---------------------------------------------------------------------------

def leggi_voti(percorso_file):
    """Legge il file CSV e restituisce una lista di dizionari."""
    studenti = []
    with open(percorso_file, mode='r', encoding='utf-8') as file:
        lettore = csv.DictReader(file)
        for riga in lettore:
            studenti.append(dict(riga))
    return studenti


# ---------------------------------------------------------------------------
# Passo 2: Pulizia dei dati
# ---------------------------------------------------------------------------

def converti_voto(valore):
    """Converte una stringa in intero. Restituisce None se non possibile."""
    try:
        return int(valore)
    except (ValueError, TypeError):
        return None


def pulisci_dati(studenti_raw):
    """Pulisce i dati convertendo i voti in numeri interi."""
    studenti_puliti = []
    for s in studenti_raw:
        studente = {
            'matricola': s['matricola'],
            'nome': s['nome'],
            'cognome': s['cognome'],
            'voto_scritto': converti_voto(s['voto_scritto']),
            'voto_orale': converti_voto(s['voto_orale']),
            'voto_finale': converti_voto(s['voto_finale']),
        }
        studenti_puliti.append(studente)
    return studenti_puliti


# ---------------------------------------------------------------------------
# Passo 3: Calcolo statistiche descrittive
# ---------------------------------------------------------------------------

def estrai_voti_validi(studenti, campo):
    """Estrae i voti validi (non None) per un dato campo."""
    return [s[campo] for s in studenti if s[campo] is not None]


def calcola_media(valori):
    """Calcola la media aritmetica."""
    if not valori:
        return 0
    return sum(valori) / len(valori)


def calcola_mediana(valori):
    """Calcola la mediana."""
    if not valori:
        return 0
    ordinati = sorted(valori)
    n = len(ordinati)
    if n % 2 == 1:
        return ordinati[n // 2]
    else:
        return (ordinati[n // 2 - 1] + ordinati[n // 2]) / 2


def calcola_moda(valori):
    """Calcola la moda (valore piu' frequente)."""
    if not valori:
        return None
    conteggio = {}
    for v in valori:
        conteggio[v] = conteggio.get(v, 0) + 1
    massimo = max(conteggio.values())
    mode = [k for k, v in conteggio.items() if v == massimo]
    return mode[0] if len(mode) == 1 else mode


def calcola_varianza(valori):
    """Calcola la varianza campionaria."""
    if len(valori) < 2:
        return 0
    media = calcola_media(valori)
    scarti_quadrati = [(x - media) ** 2 for x in valori]
    return sum(scarti_quadrati) / (len(valori) - 1)


def calcola_tutte_statistiche(voti):
    """Calcola tutte le statistiche per una lista di voti."""
    if not voti:
        return {}
    return {
        'media': calcola_media(voti),
        'mediana': calcola_mediana(voti),
        'moda': calcola_moda(voti),
        'varianza': calcola_varianza(voti),
        'dev. standard': calcola_varianza(voti) ** 0.5,
        'minimo': min(voti),
        'massimo': max(voti),
        'conteggio': len(voti),
    }


# ---------------------------------------------------------------------------
# Passo 4: Filtraggio studenti
# ---------------------------------------------------------------------------

def filtra_promossi(studenti):
    """Restituisce gli studenti con voto finale >= 18."""
    return [s for s in studenti
            if s['voto_finale'] is not None and s['voto_finale'] >= 18]


def filtra_assenti(studenti):
    """Restituisce gli studenti assenti (voto finale None)."""
    return [s for s in studenti if s['voto_finale'] is None]


def filtra_sopra_media(studenti, media):
    """Restituisce gli studenti con voto finale sopra la media."""
    return [s for s in studenti
            if s['voto_finale'] is not None and s['voto_finale'] > media]


def classifica_studenti(studenti):
    """Classifica gli studenti in categorie di merito."""
    classificazione = {
        'eccellente': [],
        'buono': [],
        'sufficiente': [],
        'insufficiente': [],
        'assente': []
    }
    for s in studenti:
        voto = s['voto_finale']
        nome_completo = f"{s['nome']} {s['cognome']}"
        if voto is None:
            classificazione['assente'].append(nome_completo)
        elif voto >= 28:
            classificazione['eccellente'].append(nome_completo)
        elif voto >= 24:
            classificazione['buono'].append(nome_completo)
        elif voto >= 18:
            classificazione['sufficiente'].append(nome_completo)
        else:
            classificazione['insufficiente'].append(nome_completo)
    return classificazione


# ---------------------------------------------------------------------------
# Passo 5: Generazione report
# ---------------------------------------------------------------------------

def genera_report(studenti, statistiche, classificazione):
    """Genera un report testuale completo dell'analisi dei voti."""
    righe = []
    righe.append("=" * 60)
    righe.append("         REPORT ANALISI VOTI DEL CORSO")
    righe.append("=" * 60)
    righe.append("")

    # Sezione 1 - Panoramica generale
    promossi = filtra_promossi(studenti)
    assenti = filtra_assenti(studenti)
    n_totale = len(studenti)
    n_promossi = len(promossi)
    n_assenti = len(assenti)
    n_insufficienti = n_totale - n_promossi - n_assenti

    righe.append("--- PANORAMICA GENERALE ---")
    righe.append(f"  Studenti totali:       {n_totale}")
    righe.append(f"  Promossi:              {n_promossi}")
    righe.append(f"  Insufficienti:         {n_insufficienti}")
    righe.append(f"  Assenti:               {n_assenti}")
    if n_totale - n_assenti > 0:
        tasso = n_promossi / (n_totale - n_assenti) * 100
        righe.append(f"  Tasso di promozione:   {tasso:.1f}%")
    righe.append("")

    # Sezione 2 - Statistiche descrittive
    righe.append("--- STATISTICHE DESCRITTIVE (voto finale) ---")
    for nome, valore in statistiche.items():
        if isinstance(valore, float):
            righe.append(f"  {nome.capitalize():20s} {valore:.2f}")
        else:
            righe.append(f"  {nome.capitalize():20s} {valore}")
    righe.append("")

    # Sezione 3 - Classificazione
    righe.append("--- CLASSIFICAZIONE STUDENTI ---")
    for categoria, nomi in classificazione.items():
        righe.append(f"  {categoria.upper()} ({len(nomi)}):")
        if nomi:
            for n in nomi:
                righe.append(f"    - {n}")
        else:
            righe.append("    (nessuno)")
    righe.append("")

    # Sezione 4 - Tabella riepilogativa
    righe.append("--- TABELLA RIEPILOGATIVA ---")
    intestazione = (f"  {'Matricola':<10} {'Nome':<12} {'Cognome':<12} "
                    f"{'Scritto':>8} {'Orale':>8} {'Finale':>8}")
    righe.append(intestazione)
    righe.append("  " + "-" * 62)
    for s in studenti:
        scritto = str(s['voto_scritto']) if s['voto_scritto'] is not None else "assente"
        orale = str(s['voto_orale']) if s['voto_orale'] is not None else "assente"
        finale = str(s['voto_finale']) if s['voto_finale'] is not None else "assente"
        riga = (f"  {s['matricola']:<10} {s['nome']:<12} {s['cognome']:<12} "
                f"{scritto:>8} {orale:>8} {finale:>8}")
        righe.append(riga)
    righe.append("")
    righe.append("=" * 60)

    return '\n'.join(righe)


# ---------------------------------------------------------------------------
# Passo 6: Salvataggio e funzione principale
# ---------------------------------------------------------------------------

def salva_report(report, percorso_output):
    """Salva il report su file di testo."""
    with open(percorso_output, 'w', encoding='utf-8') as file:
        file.write(report)
    print(f"\nReport salvato in: {percorso_output}")


def main():
    """Funzione principale che coordina tutte le operazioni."""
    # Percorso della directory corrente del progetto
    cartella_progetto = Path(__file__).parent

    # 1. Lettura dei dati dal file CSV
    percorso_csv = cartella_progetto / "dati_voti.csv"
    print(f"Lettura dati da: {percorso_csv.name}")
    studenti_raw = leggi_voti(percorso_csv)
    print(f"  Letti {len(studenti_raw)} record")

    # 2. Pulizia dei dati
    studenti = pulisci_dati(studenti_raw)
    n_assenti = len([s for s in studenti if s['voto_finale'] is None])
    print(f"  Di cui {n_assenti} assenti o con dati mancanti")

    # 3. Calcolo statistiche sui voti finali validi
    voti_finali = estrai_voti_validi(studenti, 'voto_finale')
    statistiche = calcola_tutte_statistiche(voti_finali)

    # Verifica con il modulo statistics della libreria standard
    print("\n--- Verifica con modulo statistics ---")
    print(f"  Media (manuale):     {statistiche['media']:.2f}")
    print(f"  Media (statistics):  {statistics.mean(voti_finali):.2f}")
    print(f"  Mediana (manuale):   {statistiche['mediana']}")
    print(f"  Mediana (statistics):{statistics.median(voti_finali)}")

    # 4. Classificazione studenti
    classificazione = classifica_studenti(studenti)

    # 5. Generazione report
    report = genera_report(studenti, statistiche, classificazione)

    # 6. Stampa a schermo e salvataggio su file
    print("\n")
    print(report)
    percorso_output = cartella_progetto / "report_voti.txt"
    salva_report(report, percorso_output)


if __name__ == "__main__":
    main()
