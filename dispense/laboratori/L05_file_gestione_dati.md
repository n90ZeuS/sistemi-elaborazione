# Laboratorio 5 --- File e gestione dati

**Prerequisiti**: Frontale F15 (File, dati e gestione degli errori)

**Obiettivo**: mettere in pratica la lettura e scrittura di file di testo, CSV e JSON, la costruzione di percorsi con `pathlib` e la gestione degli errori con `try`/`except`.

---

## Esercizio guidato 1 --- Leggere un file di testo e contare righe, parole, caratteri

Creiamo un file di testo di esempio e poi scriviamo una funzione che ne calcola le statistiche fondamentali.

### Passo 1: creare il file di prova

Create nella cartella di lavoro un file chiamato `poesia.txt` con il seguente contenuto:

```
Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura
che la diritta via era smarrita

Ahi quanto a dir qual era è cosa dura
esta selva selvaggia e aspra e forte
che nel pensier rinova la paura
```

### Passo 2: scrivere la funzione di analisi

```python
from pathlib import Path


def analizza_file(percorso: Path) -> dict[str, int]:
    """Legge un file di testo e restituisce statistiche di base.

    Args:
        percorso: Path al file da analizzare.

    Returns:
        Dizionario con chiavi 'righe', 'righe_non_vuote', 'parole', 'caratteri'.

    Raises:
        FileNotFoundError: Se il file non esiste.
    """
    num_righe: int = 0
    num_righe_non_vuote: int = 0
    num_parole: int = 0
    num_caratteri: int = 0

    with open(percorso, "r", encoding="utf-8") as f:
        for riga in f:
            num_righe += 1
            num_caratteri += len(riga)
            if riga.strip():
                num_righe_non_vuote += 1
                num_parole += len(riga.split())

    return {
        "righe": num_righe,
        "righe_non_vuote": num_righe_non_vuote,
        "parole": num_parole,
        "caratteri": num_caratteri,
    }


# --- Prova ---
if __name__ == "__main__":
    percorso_poesia: Path = Path("poesia.txt")
    statistiche: dict[str, int] = analizza_file(percorso_poesia)
    for chiave, valore in statistiche.items():
        print(f"{chiave:>20}: {valore}")
```

**Output atteso**:

```
               righe: 7
     righe_non_vuote: 6
              parole: 40
           caratteri: 235
```

**Osservazione**: iteriamo riga per riga sull'oggetto file --- questo funziona anche su file enormi perche' legge una riga alla volta dalla memoria. Notiamo che `riga.split()` senza argomenti divide su qualsiasi sequenza di spazi bianchi.

---

## Esercizio guidato 2 --- Scrivere risultati in file di output con `pathlib`

Prendiamo le statistiche calcolate nell'esercizio precedente e salviamole in un file, creando la directory di output se non esiste.

```python
from pathlib import Path


def salva_statistiche(
    percorso_output: Path,
    nome_sorgente: str,
    statistiche: dict[str, int],
) -> None:
    """Salva le statistiche di un file in un report testuale.

    Args:
        percorso_output: Path del file di output da creare.
        nome_sorgente: Nome del file sorgente analizzato.
        statistiche: Dizionario con le statistiche calcolate.
    """
    # Creiamo la directory genitore se non esiste
    percorso_output.parent.mkdir(parents=True, exist_ok=True)

    with open(percorso_output, "w", encoding="utf-8") as f:
        f.write(f"=== Report per: {nome_sorgente} ===\n\n")
        for chiave, valore in statistiche.items():
            f.write(f"  {chiave:>20}: {valore}\n")
        f.write(f"\n{'='*40}\n")

    print(f"Report salvato in: {percorso_output}")


# --- Prova ---
if __name__ == "__main__":
    statistiche: dict[str, int] = {
        "righe": 7,
        "righe_non_vuote": 6,
        "parole": 40,
        "caratteri": 235,
    }
    output: Path = Path("output") / "report_poesia.txt"
    salva_statistiche(output, "poesia.txt", statistiche)

    # Verifica: rileggiamo il file appena scritto
    contenuto: str = output.read_text(encoding="utf-8")
    print(contenuto)
```

**Cosa notiamo**:

- `percorso_output.parent.mkdir(parents=True, exist_ok=True)` crea tutte le directory intermedie senza errore se gia' esistono.
- `Path.read_text()` e' una scorciatoia comoda per leggere un intero file in una stringa.
- L'operatore `/` di `Path` costruisce percorsi in modo portabile tra sistemi operativi.

---

## Esercizio guidato 3 --- CSV con `csv.DictReader` (encoding, separatore `;`)

Lavoriamo con un CSV "all'italiana": separatore `;` e caratteri accentati.

### Passo 1: creare il file CSV di prova

Create un file `studenti.csv` con questo contenuto (separatore `;`):

```
nome;cognome;voto;citta
Anna;Rossi;28;Milano
Marco;Bianchi;25;Roma
Lucia;Verdi;30;Napoli
Giuseppe;Neri;22;Torino
Francesca;Gialli;27;Bologna
```

### Passo 2: leggere e analizzare

```python
import csv
from pathlib import Path


def carica_studenti(percorso: Path) -> list[dict[str, str]]:
    """Carica un CSV di studenti con separatore punto e virgola.

    Args:
        percorso: Path al file CSV.

    Returns:
        Lista di dizionari, uno per ogni studente.
    """
    studenti: list[dict[str, str]] = []

    with open(percorso, "r", encoding="utf-8") as f:
        lettore = csv.DictReader(f, delimiter=";")
        for riga in lettore:
            studenti.append(dict(riga))

    return studenti


def stampa_tabella(studenti: list[dict[str, str]]) -> None:
    """Stampa una lista di studenti in formato tabellare."""
    if not studenti:
        print("Nessuno studente trovato.")
        return

    intestazione: str = f"{'Nome':<15} {'Cognome':<15} {'Voto':>5} {'Citta':<15}"
    print(intestazione)
    print("-" * len(intestazione))

    for s in studenti:
        print(f"{s['nome']:<15} {s['cognome']:<15} {s['voto']:>5} {s['citta']:<15}")


def calcola_media_voti(studenti: list[dict[str, str]]) -> float:
    """Calcola la media dei voti degli studenti.

    Args:
        studenti: Lista di dizionari con chiave 'voto'.

    Returns:
        Media aritmetica dei voti.

    Raises:
        ValueError: Se la lista e' vuota.
    """
    if not studenti:
        raise ValueError("Impossibile calcolare la media: lista vuota")

    voti: list[int] = [int(s["voto"]) for s in studenti]
    return sum(voti) / len(voti)


# --- Prova ---
if __name__ == "__main__":
    percorso: Path = Path("studenti.csv")
    studenti: list[dict[str, str]] = carica_studenti(percorso)
    stampa_tabella(studenti)
    print(f"\nMedia voti: {calcola_media_voti(studenti):.2f}")
```

**Output atteso**:

```
Nome            Cognome          Voto Citta
----------------------------------------------------
Anna            Rossi              28 Milano
Marco           Bianchi            25 Roma
Lucia           Verdi              30 Napoli
Giuseppe        Neri               22 Torino
Francesca       Gialli             27 Bologna

Media voti: 26.40
```

**Attenzione all'encoding**: se aprite un CSV esportato da Excel su Windows e vedete caratteri strani (es. `citt\xe0` invece di `citta'`), provate con `encoding="latin-1"` oppure `encoding="cp1252"`.

---

## Esercizio guidato 4 --- JSON: leggere e navigare una struttura

I file JSON possono contenere strutture annidate (dizionari dentro dizionari, liste dentro dizionari). Impariamo a navigarle.

### Passo 1: creare il file JSON di prova

Create un file `corso.json`:

```json
{
  "nome_corso": "Sistemi di Elaborazione",
  "anno_accademico": "2025-2026",
  "docente": {
    "nome": "Mario",
    "cognome": "Rossi",
    "email": "mario.rossi@universita.it"
  },
  "studenti": [
    {"matricola": "S001", "nome": "Anna",  "voti": [28, 25, 30]},
    {"matricola": "S002", "nome": "Marco", "voti": [22, 24]},
    {"matricola": "S003", "nome": "Lucia", "voti": [30, 30, 28, 27]},
    {"matricola": "S004", "nome": "Giuseppe", "voti": []}
  ]
}
```

### Passo 2: leggere e navigare

```python
import json
from pathlib import Path


def carica_corso(percorso: Path) -> dict:
    """Carica i dati di un corso da file JSON.

    Args:
        percorso: Path al file JSON.

    Returns:
        Dizionario con i dati del corso.
    """
    with open(percorso, "r", encoding="utf-8") as f:
        dati: dict = json.load(f)
    return dati


def riepilogo_corso(dati: dict) -> None:
    """Stampa un riepilogo del corso con le medie di ogni studente."""
    print(f"Corso: {dati['nome_corso']}")
    print(f"Anno: {dati['anno_accademico']}")
    docente: dict[str, str] = dati["docente"]
    print(f"Docente: {docente['nome']} {docente['cognome']}")
    print(f"Email: {docente['email']}")
    print()

    studenti: list[dict] = dati["studenti"]
    print(f"{'Matricola':<12} {'Nome':<12} {'N. voti':>8} {'Media':>8}")
    print("-" * 44)

    for s in studenti:
        matricola: str = s["matricola"]
        nome: str = s["nome"]
        voti: list[int] = s["voti"]

        if voti:
            media: float = sum(voti) / len(voti)
            print(f"{matricola:<12} {nome:<12} {len(voti):>8} {media:>8.2f}")
        else:
            print(f"{matricola:<12} {nome:<12} {len(voti):>8} {'N/D':>8}")


def salva_medie_json(dati: dict, percorso_output: Path) -> None:
    """Calcola le medie e le salva in un nuovo file JSON.

    Args:
        dati: Dizionario con i dati del corso.
        percorso_output: Path del file JSON di output.
    """
    risultati: list[dict[str, str | float | None]] = []

    for s in dati["studenti"]:
        voti: list[int] = s["voti"]
        media: float | None = sum(voti) / len(voti) if voti else None
        risultati.append({
            "matricola": s["matricola"],
            "nome": s["nome"],
            "media": round(media, 2) if media is not None else None,
        })

    output: dict[str, str | list] = {
        "corso": dati["nome_corso"],
        "medie": risultati,
    }

    percorso_output.parent.mkdir(parents=True, exist_ok=True)
    with open(percorso_output, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Medie salvate in: {percorso_output}")


# --- Prova ---
if __name__ == "__main__":
    dati: dict = carica_corso(Path("corso.json"))
    riepilogo_corso(dati)
    salva_medie_json(dati, Path("output") / "medie_corso.json")
```

**Punti chiave**:

- `json.load()` legge da file, `json.loads()` da stringa (la `s` finale sta per *string*).
- `indent=2` produce JSON leggibile; `ensure_ascii=False` preserva i caratteri accentati.
- `round(media, 2)` evita output come `27.333333333333332`.

---

## Esercizio guidato 5 --- `try`/`except` per file non trovato, formato sbagliato, valori mancanti

Scriviamo una funzione robusta che carica un CSV di misurazioni, gestendo tutti i problemi comuni.

```python
import csv
from pathlib import Path


def carica_misurazioni(percorso: Path) -> list[dict[str, float | None]]:
    """Carica misurazioni da un CSV gestendo tutti gli errori comuni.

    Il CSV atteso ha colonne: id, temperatura, umidita, pressione.
    Valori mancanti o non numerici vengono sostituiti con None.

    Args:
        percorso: Path al file CSV.

    Returns:
        Lista di dizionari con le misurazioni pulite.
    """
    # 1. Verificare che il file esista
    if not percorso.exists():
        print(f"ERRORE: il file '{percorso}' non esiste.")
        return []

    misurazioni: list[dict[str, float | None]] = []
    errori: list[str] = []

    try:
        with open(percorso, "r", encoding="utf-8") as f:
            lettore = csv.DictReader(f, delimiter=";")

            # 2. Verificare che le colonne attese siano presenti
            colonne_attese: set[str] = {"id", "temperatura", "umidita", "pressione"}
            if lettore.fieldnames is None:
                print("ERRORE: il file sembra vuoto.")
                return []

            colonne_presenti: set[str] = set(lettore.fieldnames)
            colonne_mancanti: set[str] = colonne_attese - colonne_presenti
            if colonne_mancanti:
                print(f"ATTENZIONE: colonne mancanti: {colonne_mancanti}")

            for num_riga, riga in enumerate(lettore, start=2):
                misurazione: dict[str, float | None] = {}

                # 3. Gestire valori non numerici
                for campo in ["temperatura", "umidita", "pressione"]:
                    valore_raw: str | None = riga.get(campo)
                    if valore_raw is None or valore_raw.strip() == "":
                        misurazione[campo] = None
                        errori.append(
                            f"Riga {num_riga}: '{campo}' mancante"
                        )
                    else:
                        try:
                            misurazione[campo] = float(
                                valore_raw.strip().replace(",", ".")
                            )
                        except ValueError:
                            misurazione[campo] = None
                            errori.append(
                                f"Riga {num_riga}: '{campo}' non numerico "
                                f"('{valore_raw}')"
                            )

                misurazioni.append(misurazione)

    except UnicodeDecodeError:
        print("ERRORE: il file non e' codificato in UTF-8.")
        print("Provate con encoding='latin-1' o 'cp1252'.")
        return []

    # Stampa riepilogo errori
    if errori:
        print(f"\nTrovati {len(errori)} problemi:")
        for e in errori[:10]:  # Mostra solo i primi 10
            print(f"  - {e}")
        if len(errori) > 10:
            print(f"  ... e altri {len(errori) - 10}")

    print(f"\nCaricate {len(misurazioni)} misurazioni.")
    return misurazioni


# --- Prova con un file inesistente ---
if __name__ == "__main__":
    # Test 1: file inesistente
    risultato: list[dict[str, float | None]] = carica_misurazioni(
        Path("non_esiste.csv")
    )
    print(f"Risultato: {risultato}")
    print()

    # Test 2: file reale (se disponibile)
    percorso_dati: Path = Path("misurazioni.csv")
    if percorso_dati.exists():
        dati: list[dict[str, float | None]] = carica_misurazioni(percorso_dati)
        for d in dati[:3]:
            print(d)
```

**Pattern fondamentale**: ogni operazione che puo' fallire (apertura file, conversione di tipo, accesso a chiave) va protetta con il `try`/`except` appropriato. Catturate sempre eccezioni *specifiche* --- mai un generico `except Exception`.

---

## Esercizi autonomi

### Base

**Esercizio 1 --- Analisi di un file di log**

Vi viene fornito un file `server.log` dove ogni riga ha il formato:

```
2025-11-20 08:15:32 INFO Avvio del server
2025-11-20 08:15:33 WARNING Memoria disponibile sotto il 20%
2025-11-20 08:15:35 ERROR Connessione al database fallita
2025-11-20 08:16:01 INFO Riconnessione riuscita
```

Scrivete una funzione `analizza_log(percorso: Path) -> dict[str, int]` che:

1. Legge il file riga per riga.
2. Conta quante righe ci sono per ogni livello (`INFO`, `WARNING`, `ERROR`).
3. Gestisce eventuali righe vuote o malformate senza interrompersi.
4. Restituisce un dizionario con i conteggi, ad esempio `{"INFO": 12, "WARNING": 3, "ERROR": 5}`.

Scrivete poi una seconda funzione `salva_errori(percorso_log: Path, percorso_output: Path) -> int` che estrae solo le righe `ERROR` e le salva in un file separato, restituendo il numero di errori trovati.

Usate `pathlib` per tutti i percorsi.

---

### Base

**Esercizio 2 --- Pulizia di un CSV sporco**

Avete un file `vendite_sporco.csv` (separatore `;`) con problemi tipici:

```
prodotto;quantita;prezzo_unitario;citta
Mela;10;1.50;Roma
Pera;;2.30;Milano
Banana;cinque;0.80;
;8;1.20;Napoli
Arancia;15;N/D;Torino
Mela;20;1.50;Roma
```

Scrivete una funzione `pulisci_csv(percorso_input: Path, percorso_output: Path) -> dict[str, int]` che:

1. Legge il file riga per riga con `csv.DictReader`.
2. Scarta le righe senza `prodotto`.
3. Converte `quantita` in `int` e `prezzo_unitario` in `float`, sostituendo con `None` i valori non validi.
4. Scrive un CSV pulito nel file di output contenente solo le righe con tutti i campi numerici validi.
5. Restituisce un dizionario con: `{"righe_lette": ..., "righe_valide": ..., "righe_scartate": ...}`.

---

### Intermedio

**Esercizio 3 --- Conversione CSV verso JSON**

Scrivete una funzione `csv_a_json(percorso_csv: Path, percorso_json: Path) -> int` che:

1. Legge un CSV (rilevando automaticamente se il separatore e' `,` o `;`).
2. Converte ogni riga in un dizionario.
3. Tenta di convertire i valori numerici (interi e decimali) nei tipi Python corrispondenti.
4. Salva il risultato come JSON con `indent=2` e `ensure_ascii=False`.
5. Restituisce il numero di record convertiti.

Scrivete anche la funzione inversa `json_a_csv(percorso_json: Path, percorso_csv: Path) -> int` che fa il percorso contrario.

Gestite i casi di errore: file non trovato, JSON malformato, CSV vuoto.

---

### Intermedio

**Esercizio 4 --- Unione e riepilogo di piu' CSV**

In una cartella `dati_mensili/` ci sono piu' file CSV (uno per mese) con la stessa struttura:

```
data;prodotto;quantita;importo
2025-01-05;Mela;10;15.00
2025-01-12;Pera;5;11.50
```

Scrivete una funzione `unisci_e_riepiloga(cartella: Path, output_unito: Path, output_riepilogo: Path) -> None` che:

1. Trova tutti i file `.csv` nella cartella con `glob`.
2. Li unisce in un unico CSV (`output_unito`), mantenendo una sola intestazione.
3. Calcola il totale delle quantita' e degli importi per ogni prodotto.
4. Salva il riepilogo per prodotto in `output_riepilogo` come CSV con colonne `prodotto;quantita_totale;importo_totale`.

Gestite il caso in cui la cartella sia vuota o non esista.

---

### Avanzato

**Esercizio 5 --- Analisi incrociata di dati eterogenei**

Avete due file:

- `dipendenti.json`: lista di dizionari con `id`, `nome`, `reparto`.
- `presenze.csv`: con colonne `id_dipendente;data;ore_lavorate`.

Scrivete una funzione `report_presenze(path_dipendenti: Path, path_presenze: Path, path_output: Path) -> None` che:

1. Carica entrambi i file.
2. Per ogni dipendente, calcola il totale delle ore lavorate e la media giornaliera.
3. Raggruppa i risultati per reparto.
4. Genera un report JSON con la struttura:

```json
{
  "reparti": {
    "Vendite": {
      "dipendenti": [
        {"nome": "Anna Rossi", "ore_totali": 160, "media_giornaliera": 8.0}
      ],
      "ore_totali_reparto": 160
    }
  }
}
```

Gestite: dipendenti senza presenze, presenze con `id_dipendente` inesistente, ore non numeriche.

---

## Sfida finale --- Pipeline completa: CSV sporco, pulizia, statistiche, output

Vi viene fornito un file `rilevazioni_meteo.csv` (separatore `;`) con dati meteorologici grezzi, pieni di problemi:

```
stazione;data;temperatura;umidita;vento_kmh
Roma;2025-03-01;15.2;65;12
Roma;2025-03-02;N/D;70;8
Milano;2025-03-01;;80;
Milano;2025-03-02;5.1;75;22
Napoli;2025-03-01;18.3;errore;15
Roma;2025-03-03;16.0;62;10
;2025-03-01;20.0;55;5
Milano;2025-03-03;6.5;78;18
Napoli;2025-03-02;17.8;60;abc
Napoli;2025-03-03;19.1;58;12
```

Scrivete un programma completo (non una singola funzione, ma un modulo organizzato in piu' funzioni) che esegue questa pipeline:

1. **Caricamento**: leggere il CSV, gestendo encoding e separatore.
2. **Pulizia**: scartare righe senza stazione; convertire i campi numerici, sostituendo i valori non validi con `None`; contare i problemi trovati.
3. **Statistiche per stazione**: per ogni stazione, calcolare media, minimo e massimo di ogni campo numerico (ignorando i `None`).
4. **Output CSV**: salvare le statistiche in un file `output/statistiche_meteo.csv`.
5. **Output JSON**: salvare le statistiche in un file `output/statistiche_meteo.json` con struttura annidata per stazione.
6. **Report testuale**: stampare a video un riepilogo formattato.

Ogni funzione deve avere type hints completi e gestire gli errori in modo appropriato. Il programma deve funzionare anche se il file di input ha problemi (ma non deve crashare).

---

## Domande di verifica

1. Qual e' la differenza tra leggere un file con `f.read()`, `f.readlines()` e iterare con `for riga in f`? Quando preferireste ciascun metodo?

2. Perche' e' importante specificare `newline=""` quando si apre un file per la scrittura CSV su Windows?

3. Un collega vi invia un CSV e quando lo leggete vedete `Ã©` al posto di `e'`. Cosa e' successo e come risolvete?

4. Qual e' la differenza tra `json.load()` e `json.loads()`? Scrivete un esempio d'uso per ciascuna.

5. Avete un file CSV con 10 milioni di righe. Perche' e' sbagliato usare `f.readlines()` e come lo leggereste invece?

6. Scrivete un blocco `try`/`except` che gestisce separatamente: file non trovato, errore di encoding, e valore non convertibile a numero. Per ciascuno, spiegate quale eccezione catturate.

7. Perche' `Path("dati") / "output" / "risultati.csv"` e' preferibile a `"dati/output/risultati.csv"`?

---

## Osservazioni finali

In questo laboratorio avete messo le mani su un flusso di lavoro che incontrerete continuamente nella pratica statistica: dati che arrivano in formati diversi (testo, CSV, JSON), spesso sporchi o malformati, che devono essere caricati, puliti, analizzati e salvati in un formato utilizzabile.

I punti chiave da portare con se':

- **`with open(...)` sempre**: non esiste un buon motivo per non usare il context manager.
- **`pathlib` per i percorsi**: rende il codice portabile e leggibile.
- **`csv.DictReader` con `delimiter`**: leggete CSV europei senza problemi.
- **`try`/`except` specifico**: catturate solo le eccezioni che sapete gestire. Un `except Exception` generico nasconde i bug.
- **Separare caricamento, pulizia e analisi**: ogni fase in una funzione dedicata rende il codice piu' facile da testare e da correggere.

Quando in futuro userete Pandas, molte di queste operazioni diventeranno una sola riga di codice (`pd.read_csv(...)`). Ma capire cosa succede sotto il cofano vi permettera' di diagnosticare i problemi che Pandas non riesce a risolvere da solo.
