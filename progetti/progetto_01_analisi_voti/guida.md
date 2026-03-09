# Progetto 1: Analisi voti di un corso

## Introduzione

In questo progetto costruirai un programma Python che analizza i voti di un esame universitario. Partendo da un file CSV con i dati degli studenti, imparerai a:

- Leggere file CSV (**F07** - Input/Output su file)
- Memorizzare dati strutturati in liste e dizionari (**F09** - Strutture dati)
- Calcolare statistiche descrittive (**F11** - Librerie scientifiche di base)
- Filtrare e selezionare dati con condizioni (**F13** - Controllo di flusso)
- Scrivere funzioni riutilizzabili (**F15** - Funzioni)

Il file `dati_voti.csv` contiene i dati di 20 studenti con le colonne: matricola, nome, cognome, voto_scritto, voto_orale e voto_finale. Alcuni studenti hanno il valore "assente" e alcuni hanno voti insufficienti (sotto il 18).

---

## Passo 1: Leggere il file CSV

### Cosa imparerai
- Aprire un file con `with open()`
- Usare il modulo `csv` per leggere file CSV
- Capire la differenza tra `csv.reader` e `csv.DictReader`

### Spiegazione

Un file CSV (Comma-Separated Values) e' un file di testo dove ogni riga rappresenta un record e le colonne sono separate da virgole. Python ha un modulo built-in chiamato `csv` che semplifica la lettura di questi file.

Usiamo `with open()` perche' garantisce che il file venga chiuso correttamente anche in caso di errore.

### Suggerimenti
- Usa `csv.DictReader` per avere accesso alle colonne per nome
- Ricorda di specificare `encoding='utf-8'` nell'apertura del file
- Usa `pathlib.Path` per costruire il percorso del file in modo portabile

### Scheletro di codice

```python
import csv
from pathlib import Path

def leggi_voti(percorso_file):
    """Legge il file CSV e restituisce una lista di dizionari."""
    studenti = []
    with open(percorso_file, mode='r', encoding='utf-8') as file:
        lettore = csv.DictReader(file)
        for riga in lettore:
            # TODO: aggiungi ogni riga alla lista studenti
            pass
    return studenti

# Prova la funzione
percorso = Path(__file__).parent / "dati_voti.csv"
dati = leggi_voti(percorso)
print(f"Letti {len(dati)} studenti")
print(f"Primo studente: {dati[0]}")
```

<details>
<summary>Soluzione Passo 1</summary>

```python
import csv
from pathlib import Path

def leggi_voti(percorso_file):
    """Legge il file CSV e restituisce una lista di dizionari."""
    studenti = []
    with open(percorso_file, mode='r', encoding='utf-8') as file:
        lettore = csv.DictReader(file)
        for riga in lettore:
            studenti.append(dict(riga))
    return studenti

# Prova la funzione
percorso = Path(__file__).parent / "dati_voti.csv"
dati = leggi_voti(percorso)
print(f"Letti {len(dati)} studenti")
print(f"Primo studente: {dati[0]}")
```
</details>

---

## Passo 2: Pulire e strutturare i dati

### Cosa imparerai
- Convertire stringhe in numeri con gestione degli errori
- Gestire valori mancanti o speciali (come "assente")
- Costruire strutture dati pulite

### Spiegazione

I dati letti dal CSV sono tutti stringhe. Dobbiamo convertire i voti in numeri interi, ma alcuni valori sono "assente" e non possono essere convertiti. Usiamo una funzione di supporto che restituisce `None` quando il valore non e' un numero valido.

### Suggerimenti
- Usa `try/except ValueError` per gestire la conversione
- Il valore `None` in Python rappresenta l'assenza di un dato
- Puoi usare una funzione di supporto per la conversione

### Scheletro di codice

```python
def converti_voto(valore):
    """Converte una stringa in intero. Restituisce None se non possibile."""
    # TODO: prova a convertire in int, se fallisce restituisci None
    pass

def pulisci_dati(studenti_raw):
    """Pulisce i dati convertendo i voti in numeri."""
    studenti_puliti = []
    for s in studenti_raw:
        studente = {
            'matricola': s['matricola'],
            'nome': s['nome'],
            'cognome': s['cognome'],
            # TODO: converti i tre voti usando converti_voto
        }
        studenti_puliti.append(studente)
    return studenti_puliti
```

<details>
<summary>Soluzione Passo 2</summary>

```python
def converti_voto(valore):
    """Converte una stringa in intero. Restituisce None se non possibile."""
    try:
        return int(valore)
    except (ValueError, TypeError):
        return None

def pulisci_dati(studenti_raw):
    """Pulisce i dati convertendo i voti in numeri."""
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
```
</details>

---

## Passo 3: Calcolare statistiche descrittive

### Cosa imparerai
- Calcolare media, mediana, moda e varianza
- Lavorare con liste filtrate (escludendo i `None`)
- Usare le funzioni del modulo `statistics`

### Spiegazione

Le statistiche descrittive ci permettono di riassumere i dati. Calcoleremo:
- **Media**: somma dei valori diviso il numero di valori
- **Mediana**: valore centrale quando i dati sono ordinati
- **Moda**: valore piu' frequente
- **Varianza**: misura di dispersione dei dati rispetto alla media

Prima calcoleremo tutto "a mano" con Python base, poi useremo il modulo `statistics`.

### Suggerimenti
- Filtra i valori `None` prima di calcolare le statistiche
- Per la mediana: ordina la lista, poi prendi il valore centrale
- Per la moda: usa un dizionario per contare le occorrenze
- Il modulo `statistics` ha funzioni pronte: `mean()`, `median()`, `mode()`, `variance()`

### Scheletro di codice

```python
def estrai_voti_validi(studenti, campo):
    """Estrae i voti validi (non None) per un dato campo."""
    # TODO: restituisci una lista con solo i voti non-None
    pass

def calcola_media(valori):
    """Calcola la media aritmetica."""
    if not valori:
        return 0
    # TODO: somma / lunghezza
    pass

def calcola_mediana(valori):
    """Calcola la mediana."""
    if not valori:
        return 0
    ordinati = sorted(valori)
    n = len(ordinati)
    # TODO: se n e' dispari prendi l'elemento centrale,
    #       se n e' pari fai la media dei due centrali
    pass

def calcola_varianza(valori):
    """Calcola la varianza campionaria."""
    if len(valori) < 2:
        return 0
    media = calcola_media(valori)
    # TODO: somma dei quadrati degli scarti / (n - 1)
    pass
```

<details>
<summary>Soluzione Passo 3</summary>

```python
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

# Verifica con il modulo statistics
import statistics

voti_finali = estrai_voti_validi(studenti, 'voto_finale')
print(f"Media (manuale):     {calcola_media(voti_finali):.2f}")
print(f"Media (statistics):  {statistics.mean(voti_finali):.2f}")
print(f"Mediana (manuale):   {calcola_mediana(voti_finali)}")
print(f"Mediana (statistics):{statistics.median(voti_finali)}")
```
</details>

---

## Passo 4: Filtrare studenti per criteri

### Cosa imparerai
- Filtrare liste con condizioni (list comprehension o cicli)
- Combinare piu' condizioni con `and`/`or`
- Classificare gli studenti in categorie

### Spiegazione

Ora che abbiamo i dati puliti, possiamo filtrare gli studenti per diversi criteri:
- Chi ha superato l'esame (voto finale >= 18)
- Chi e' stato assente
- Chi e' insufficiente
- Chi ha un voto sopra la media

### Suggerimenti
- Usa le list comprehension per filtrare in modo compatto
- Ricorda di controllare che il voto non sia `None` prima di confrontarlo
- Puoi creare una funzione per ogni tipo di filtro

### Scheletro di codice

```python
def filtra_promossi(studenti):
    """Restituisce gli studenti con voto finale >= 18."""
    # TODO: filtra gli studenti promossi
    pass

def filtra_assenti(studenti):
    """Restituisce gli studenti assenti (voto finale None)."""
    # TODO: filtra gli studenti assenti
    pass

def filtra_sopra_media(studenti, media):
    """Restituisce gli studenti con voto finale sopra la media."""
    # TODO: filtra gli studenti sopra la media
    pass

def classifica_studenti(studenti):
    """Classifica gli studenti in categorie."""
    classificazione = {
        'eccellente': [],   # voto >= 28
        'buono': [],        # 24 <= voto < 28
        'sufficiente': [],  # 18 <= voto < 24
        'insufficiente': [],# voto < 18
        'assente': []       # voto is None
    }
    # TODO: classifica ogni studente
    return classificazione
```

<details>
<summary>Soluzione Passo 4</summary>

```python
def filtra_promossi(studenti):
    """Restituisce gli studenti con voto finale >= 18."""
    return [s for s in studenti if s['voto_finale'] is not None and s['voto_finale'] >= 18]

def filtra_assenti(studenti):
    """Restituisce gli studenti assenti (voto finale None)."""
    return [s for s in studenti if s['voto_finale'] is None]

def filtra_sopra_media(studenti, media):
    """Restituisce gli studenti con voto finale sopra la media."""
    return [s for s in studenti
            if s['voto_finale'] is not None and s['voto_finale'] > media]

def classifica_studenti(studenti):
    """Classifica gli studenti in categorie."""
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
```
</details>

---

## Passo 5: Generare un report testuale

### Cosa imparerai
- Formattare stringhe con f-string
- Costruire un report strutturato
- Allineare testo in colonne

### Spiegazione

Il report finale riassume tutte le analisi fatte. Deve essere leggibile e ben formattato, con sezioni chiare per le statistiche, la classificazione e i dettagli.

### Suggerimenti
- Usa le f-string per formattare i numeri: `f"{valore:.2f}"` per 2 decimali
- Usa `str.ljust()` o `str.rjust()` per allineare il testo
- Costruisci il report come una lista di stringhe, poi uniscile con `'\n'.join()`

### Scheletro di codice

```python
def genera_report(studenti, statistiche, classificazione):
    """Genera un report testuale completo."""
    righe = []
    righe.append("=" * 60)
    righe.append("REPORT ANALISI VOTI DEL CORSO")
    righe.append("=" * 60)
    righe.append("")

    # TODO: Sezione 1 - Panoramica generale
    # Numero totale studenti, promossi, bocciati, assenti

    # TODO: Sezione 2 - Statistiche descrittive
    # Media, mediana, moda, varianza, deviazione standard

    # TODO: Sezione 3 - Classificazione
    # Per ogni categoria, elenca gli studenti

    # TODO: Sezione 4 - Tabella riepilogativa
    # Tabella con tutti gli studenti e i loro voti

    return '\n'.join(righe)
```

<details>
<summary>Soluzione Passo 5</summary>

```python
def genera_report(studenti, statistiche, classificazione):
    """Genera un report testuale completo."""
    righe = []
    righe.append("=" * 60)
    righe.append("         REPORT ANALISI VOTI DEL CORSO")
    righe.append("=" * 60)
    righe.append("")

    # Sezione 1 - Panoramica generale
    promossi = [s for s in studenti if s['voto_finale'] is not None and s['voto_finale'] >= 18]
    assenti = [s for s in studenti if s['voto_finale'] is None]
    righe.append("--- PANORAMICA GENERALE ---")
    righe.append(f"  Studenti totali:    {len(studenti)}")
    righe.append(f"  Promossi:           {len(promossi)}")
    righe.append(f"  Assenti:            {len(assenti)}")
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
        for n in nomi:
            righe.append(f"    - {n}")
    righe.append("")

    # Sezione 4 - Tabella riepilogativa
    righe.append("--- TABELLA RIEPILOGATIVA ---")
    intestazione = f"  {'Matricola':<10} {'Nome':<12} {'Cognome':<12} {'Scritto':>8} {'Orale':>8} {'Finale':>8}"
    righe.append(intestazione)
    righe.append("  " + "-" * 62)
    for s in studenti:
        scritto = str(s['voto_scritto']) if s['voto_scritto'] is not None else "assente"
        orale = str(s['voto_orale']) if s['voto_orale'] is not None else "assente"
        finale = str(s['voto_finale']) if s['voto_finale'] is not None else "assente"
        riga = f"  {s['matricola']:<10} {s['nome']:<12} {s['cognome']:<12} {scritto:>8} {orale:>8} {finale:>8}"
        righe.append(riga)
    righe.append("")
    righe.append("=" * 60)

    return '\n'.join(righe)
```
</details>

---

## Passo 6: Salvare i risultati su file

### Cosa imparerai
- Scrivere su file di testo con `with open(... , 'w')`
- Organizzare il codice con una funzione `main()`
- Usare il pattern `if __name__ == "__main__"`

### Spiegazione

L'ultimo passo e' salvare il report su un file di testo. Organizziamo tutto il codice in una funzione `main()` che coordina tutte le operazioni: lettura, pulizia, analisi, report e salvataggio.

Il pattern `if __name__ == "__main__"` garantisce che `main()` venga eseguita solo quando il file e' lanciato direttamente (non quando viene importato da un altro modulo).

### Suggerimenti
- Usa `with open(percorso, 'w', encoding='utf-8')` per scrivere
- Usa `file.write(testo)` per scrivere il contenuto
- Metti tutto il flusso principale dentro `main()`

### Scheletro di codice

```python
def salva_report(report, percorso_output):
    """Salva il report su file di testo."""
    # TODO: apri il file in scrittura e scrivi il report
    pass

def main():
    """Funzione principale che coordina tutte le operazioni."""
    # 1. Leggi i dati
    # 2. Pulisci i dati
    # 3. Calcola statistiche
    # 4. Classifica studenti
    # 5. Genera report
    # 6. Stampa e salva
    pass

if __name__ == "__main__":
    main()
```

<details>
<summary>Soluzione Passo 6</summary>

```python
def salva_report(report, percorso_output):
    """Salva il report su file di testo."""
    with open(percorso_output, 'w', encoding='utf-8') as file:
        file.write(report)
    print(f"Report salvato in: {percorso_output}")

def main():
    """Funzione principale che coordina tutte le operazioni."""
    # 1. Leggi i dati
    percorso_csv = Path(__file__).parent / "dati_voti.csv"
    studenti_raw = leggi_voti(percorso_csv)
    print(f"Letti {len(studenti_raw)} studenti dal file CSV")

    # 2. Pulisci i dati
    studenti = pulisci_dati(studenti_raw)

    # 3. Calcola statistiche
    voti_finali = estrai_voti_validi(studenti, 'voto_finale')
    statistiche = {
        'media': calcola_media(voti_finali),
        'mediana': calcola_mediana(voti_finali),
        'moda': calcola_moda(voti_finali),
        'varianza': calcola_varianza(voti_finali),
        'dev. standard': calcola_varianza(voti_finali) ** 0.5,
        'minimo': min(voti_finali),
        'massimo': max(voti_finali),
    }

    # 4. Classifica studenti
    classificazione = classifica_studenti(studenti)

    # 5. Genera report
    report = genera_report(studenti, statistiche, classificazione)

    # 6. Stampa e salva
    print(report)
    percorso_output = Path(__file__).parent / "report_voti.txt"
    salva_report(report, percorso_output)

if __name__ == "__main__":
    main()
```
</details>

---

## Complimenti!

Hai completato il Progetto 1. Ora sai:
- Leggere e scrivere file CSV
- Pulire dati con valori mancanti
- Calcolare statistiche descrittive da zero
- Filtrare e classificare dati
- Generare report formattati
- Organizzare il codice con funzioni e `main()`

La soluzione completa e' nel file `soluzione.py`. Confronta il tuo codice con la soluzione per vedere approcci alternativi.
