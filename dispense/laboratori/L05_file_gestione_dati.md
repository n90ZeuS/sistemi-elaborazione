# Laboratorio 5 — File e gestione dati

**Prerequisiti:** lezioni T15 (File, dati ed errori).

Oggi si lavora con dati che stanno nei file: testo, CSV e JSON. Per ogni esercizio create un file `.py` con il nome indicato, nella stessa cartella dei file di dati. I file di dati sono scritti nella slide dell'esercizio: create il file con l'editor e copiate il contenuto, compresa la riga di intestazione, e lasciate un a capo dopo l'ultima riga. Le classi non servono.

Ogni esercizio ha la consegna, un esempio di esecuzione e alcuni casi da provare: il programma è corretto quando dà gli stessi risultati. Alla fine c'è una challenge a scelta tra 5 temi. Le soluzioni le vediamo all'inizio della lezione T17.

| # | File | Esercizio |
|---|---|---|
| 1 | `conta_righe.py` | Commenti al corso |
| 2 | `parole_frequenti.py` | Le parole più usate |
| 3 | `esiti_appello.py` | Gli esiti dell'appello |
| 4 | `verbale.py` | Il verbale d'esame |
| 5 | `spese.py` | Il registro delle spese |
| 6 | `sondaggio.py` | Il sondaggio in JSON |
| 7 | `appello_robusto.py` | Un appello con errori |
| 8 | `config_soglia.py` | Configurazione in JSON |
| Challenge | a scelta | Mercati e finanza · Sport · Imprese e marketing · Salute e scienza · Caso e probabilità |

---

## Promemoria

Gli strumenti che servono oggi. Aprite sempre i file con `with` e `encoding="utf-8"`. `csv.DictReader` restituisce i valori come stringhe: i numeri vanno convertiti con `int()` o `float()`. Nel `try` mettete solo le istruzioni che possono fallire e catturate eccezioni specifiche.

```python
import csv
import json
from pathlib import Path

with open("note.txt", "w", encoding="utf-8") as f:  # "a" aggiunge
    f.write("prima riga\nseconda riga\n")  # l'a capo va scritto
with open(Path("note.txt"), "r", encoding="utf-8") as f:
    for riga in f:                         # una riga alla volta
        print(riga.strip())                # prima riga ...
with open("appello.csv", "r", encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter=";"):  # r è un dict
        print(r["cognome"], int(r["voto"]))     # Rossi 28 ...
try:
    with open("sondaggio.json", "r", encoding="utf-8") as f:
        dati: dict = json.load(f)          # JSON → dict e list
    print(dati["lode"])
except KeyError as e:
    print("Chiave mancante:", e)           # Chiave mancante: 'lode'
```

---

## Esercizio 1 — Commenti al corso (`conta_righe.py`)

**Consegna**

1. Il file `commenti.txt` contiene i commenti liberi di un questionario sul corso, uno per riga. Una riga è vuota.
2. Apritelo con `with open(..., encoding="utf-8")` e leggetelo riga per riga con un `for`.
3. Contate le righe, le righe vuote e le parole (`len(riga.split())`).
4. Stampate il nome del file (`Path(...).name`), i conteggi, le parole per commento (righe non vuote) con un decimale e il numero di riga del commento più lungo.

**File `commenti.txt`** (createlo nella cartella del programma)

```
Lezioni chiare, esempi utili.
Molto lavoro a casa, poco tempo per gli esercizi.
Le slide sono utili, il ritmo è veloce.

Vorrei più esempi con dati reali.
Laboratori utili, ma le aule sono troppo affollate.
Esercizi utili per capire meglio.
Più esercizi in aula e meno teoria.
```

**Esempio di esecuzione**

```
File: commenti.txt
Righe: 8, di cui vuote: 1
Parole: 47
Parole per commento: 6.7
Commento più lungo: riga 2, 9 parole
```

**Provate anche**

- aggiungete in fondo la riga `Grazie.` → `Righe: 9`, `Parole: 48`, `Parole per commento: 6.0`
- cambiate il nome in `commenti2.txt` → il programma si ferma con `FileNotFoundError` (lo gestirete nell'esercizio 7)

---

## Esercizio 2 — Le parole più usate (`parole_frequenti.py`)

**Consegna**

1. Usate lo stesso `commenti.txt`. Scrivete una funzione `parole_del_file(percorso: Path) -> list[str]` che legge il file e restituisce tutte le parole in minuscolo.
2. Togliete la punteggiatura attaccata alle parole con `parola.strip(".,;:!?")`.
3. Stampate il numero di parole e di parole distinte (`set`).
4. Tenete le parole di almeno 5 lettere, contatele con `Counter` e stampate le 3 più frequenti con `most_common(3)`.

**File `commenti.txt`** (createlo nella cartella del programma)

```
Lezioni chiare, esempi utili.
Molto lavoro a casa, poco tempo per gli esercizi.
Le slide sono utili, il ritmo è veloce.

Vorrei più esempi con dati reali.
Laboratori utili, ma le aule sono troppo affollate.
Esercizi utili per capire meglio.
Più esercizi in aula e meno teoria.
```

**Esempio di esecuzione**

```
Parole: 47, distinte: 37
Parole di almeno 5 lettere: 25
utili: 4
esercizi: 3
esempi: 2
```

**Provate anche**

- `Utili,` e `utili.` contano come la stessa parola
- con la riga `Grazie.` in più → `Parole: 48, distinte: 38`

---

## Esercizio 3 — Gli esiti dell'appello (`esiti_appello.py`)

**Consegna**

1. Il file `appello.csv` contiene i voti di un appello, separati da `;`.
2. Leggetelo con `csv.DictReader(f, delimiter=";")` dentro una funzione che restituisce la lista delle righe (`list(...)`).
3. I valori sono stringhe: convertite i voti con `int()`.
4. Stampate iscritti, promossi (voto da 18 in su) con la percentuale, la media di tutti e quella dei promossi con un decimale, il voto più alto con cognome e nome (`max` con `key=lambda ...`).

**File `appello.csv`** (createlo nella cartella del programma)

```
matricola;cognome;nome;voto
2101234;Rossi;Anna;28
2101567;Bianchi;Marco;17
2102001;Verdi;Giulia;30
2102345;Russo;Luca;24
2102890;Ferrari;Sara;15
2103112;Esposito;Paolo;21
2103456;Romano;Elena;27
2103789;Gallo;Davide;19
```

**Esempio di esecuzione**

```
Iscritti: 8
Promossi: 6 (75.0%)
Media di tutti: 22.6
Media dei promossi: 24.8
Voto più alto: 30 (Verdi Giulia)
```

**Provate anche**

- aggiungete la riga `2104000;Conti;Marta;18` → `Iscritti: 9`, `Promossi: 7 (77.8%)`, medie `22.1` e `23.9`
- togliete `delimiter=";"` e stampate una riga letta: c'è una sola chiave, `matricola;cognome;nome;voto`

---

## Esercizio 4 — Il verbale d'esame (`verbale.py`)

**Consegna**

1. Leggete di nuovo `appello.csv` e ordinate gli studenti per cognome con `sorted(..., key=lambda s: s["cognome"])`.
2. Aprite `verbale.txt` in scrittura (`"w"`) e scrivete con `f.write()` un'intestazione, una riga per studente con matricola, cognome, nome, voto ed esito, e in fondo il numero di promossi. Ricordate `\n` alla fine di ogni riga.
3. Dopo aver chiuso il file, rileggetelo con `Path("verbale.txt").read_text(encoding="utf-8")` e stampatelo.

**File `appello.csv`** (createlo nella cartella del programma)

```
matricola;cognome;nome;voto
2101234;Rossi;Anna;28
2101567;Bianchi;Marco;17
2102001;Verdi;Giulia;30
2102345;Russo;Luca;24
2102890;Ferrari;Sara;15
2103112;Esposito;Paolo;21
2103456;Romano;Elena;27
2103789;Gallo;Davide;19
```

**Esempio di esecuzione**

```
Verbale dell'appello
2101567 Bianchi Marco: 17, respinto
2103112 Esposito Paolo: 21, promosso
2102890 Ferrari Sara: 15, respinto
2103789 Gallo Davide: 19, promosso
2103456 Romano Elena: 27, promosso
2101234 Rossi Anna: 28, promosso
2102345 Russo Luca: 24, promosso
2102001 Verdi Giulia: 30, promosso
Promossi: 6 su 8
```

**Provate anche**

- eseguite il programma due volte: `verbale.txt` viene riscritto da capo, le righe non si ripetono
- con la riga `2104000;Conti;Marta;18` → Conti è la seconda, `Promossi: 7 su 9`

---

## Esercizio 5 — Il registro delle spese (`spese.py`)

**Consegna**

1. Il file `spese.csv` è un registro delle spese di uno studente fuori sede.
2. Chiedete data, categoria (in minuscolo) e importo. Se l'importo non è un numero (`ValueError`) stampate un messaggio e non scrivete niente.
3. Altrimenti aggiungete la spesa in fondo al file: `open(..., "a", encoding="utf-8", newline="")` e `csv.writer(f, delimiter=";").writerow([...])`.
4. Rileggete tutto il file e sommate gli importi per categoria con un `defaultdict(float)`. Stampate le categorie dalla più costosa e il totale, con due decimali.

**File `spese.csv`** (createlo nella cartella del programma)

```
data;categoria;importo
2026-12-01;affitto;350.00
2026-12-02;spesa;42.50
2026-12-03;trasporti;25.00
2026-12-05;spesa;18.20
2026-12-06;libri;39.90
```

**Esempio di esecuzione**

```
Data (aaaa-mm-gg): 2026-12-07
Categoria: Spesa
Importo: 12.30
affitto: 350.00 EUR
spesa: 73.00 EUR
libri: 39.90 EUR
trasporti: 25.00 EUR
Totale: 487.90 EUR
```

**Provate anche**

- sul file originale, `2026-12-07`, `cinema`, `8.50` → compare `cinema: 8.50 EUR`, totale `484.10 EUR`
- importo `dieci` → `Importo non valido: spesa non registrata` e il file non cambia
- ogni esecuzione aggiunge una riga: aprite `spese.csv` e controllate

---

## Esercizio 6 — Il sondaggio in JSON (`sondaggio.py`)

**Consegna**

1. Il file `sondaggio.json` contiene le risposte a un questionario: per ogni studente il voto di soddisfazione (da 1 a 5) e se frequenta le lezioni.
2. Caricatelo con `json.load(f)`: si ottiene un dizionario che contiene una lista di dizionari.
3. Calcolate la media dei voti di tutti, dei frequentanti e dei non frequentanti (arrotondate con `round(..., 2)`) e la quota di frequentanti (`round(..., 3)`).
4. Mettete i risultati in un dizionario `riepilogo`, salvatelo in `riepilogo.json` con `json.dump(..., indent=2, ensure_ascii=False)` e stampatelo con `json.dumps`.

**File `sondaggio.json`** (createlo nella cartella del programma)

```
{
  "corso": "Sistemi di Elaborazione",
  "anno": 2026,
  "risposte": [
    {"matricola": "2101234", "voto": 4, "frequenta": true},
    {"matricola": "2101567", "voto": 2, "frequenta": false},
    {"matricola": "2102001", "voto": 5, "frequenta": true},
    {"matricola": "2102345", "voto": 3, "frequenta": true},
    {"matricola": "2102890", "voto": 4, "frequenta": false},
    {"matricola": "2103112", "voto": 5, "frequenta": true}
  ]
}
```

**Esempio di esecuzione**

```
Sistemi di Elaborazione (2026)
Risposte: 6
Salvato riepilogo.json:
{
  "corso": "Sistemi di Elaborazione",
  "risposte": 6,
  "media": 3.83,
  "media_frequentanti": 4.25,
  "media_non_frequentanti": 3.0,
  "quota_frequentanti": 0.667
}
```

**Provate anche**

- aggiungete la risposta `{"matricola": "2103456", "voto": 1, "frequenta": false}` → `media 3.43`, `media_non_frequentanti 2.33`, `quota_frequentanti 0.571`
- togliete la virgola dopo `"anno": 2026` → `json.JSONDecodeError` (lo gestirete nell'esercizio 8)

---

## Esercizio 7 — Un appello con errori (`appello_robusto.py`)

**Consegna**

1. Chiedete il nome del file da leggere. Se non esiste (`FileNotFoundError`) stampate un messaggio; se non ha la colonna `voto` (`KeyError`) stampatene un altro.
2. Leggete le righe con `DictReader` e numeratele con `enumerate(lettore, start=2)`: la riga 1 è l'intestazione.
3. Per ogni riga convertite il voto con `int()` dentro un `try`: se c'è `ValueError` stampate il numero di riga e il testo letto, poi passate alla riga dopo. Scartate anche i voti fuori da 0–30.
4. Alla fine stampate i voti validi, le righe scartate e la media con un decimale.

**File `appello_sporco.csv`** (createlo nella cartella del programma)

```
matricola;cognome;voto
2101234;Rossi;28
2101567;Bianchi;assente
2102001;Verdi;30
2102345;Russo;
2102890;Ferrari;33
2103112;Esposito;21
2103456;Romano;27
```

**Esempio di esecuzione**

```
File da leggere: appello_sporco.csv
Riga 3: voto non valido 'assente'
Riga 5: voto non valido ''
Riga 6: voto fuori scala 33
Voti validi: 4, righe scartate: 3
Media: 26.5
```

**Provate anche**

- `appello.csv` → `Voti validi: 8, righe scartate: 0`, `Media: 22.6`
- `voti.csv` → `Il file voti.csv non esiste`
- `commenti.txt` → `Il file commenti.txt non ha la colonna voto`

---

## Esercizio 8 — Configurazione in JSON (`config_soglia.py`)

**Consegna**

1. Il file `config.json` dice quale CSV leggere, quale colonna usare e la soglia. Il CSV è `appello.csv` dell'esercizio 3.
2. Scrivete una funzione `sopra_soglia(file: str, colonna: str, soglia: int) -> list[str]` che restituisce i cognomi degli studenti con valore maggiore o uguale alla soglia.
3. In un solo `try` caricate la configurazione e chiamate la funzione. Gestite con `except` separati: `FileNotFoundError` (stampate `e.filename`), `json.JSONDecodeError` (stampate `e.lineno`), `KeyError` e `ValueError`.
4. Nel blocco `else` stampate file, soglia, numero di studenti e cognomi in ordine alfabetico separati da virgola (`", ".join(...)`).

**File `config.json`** (createlo nella cartella del programma)

```
{
  "file": "appello.csv",
  "colonna": "voto",
  "soglia": 27
}
```

**Esempio di esecuzione**

```
File: appello.csv, soglia: 27
Sopra soglia: 3
Romano, Rossi, Verdi
```

**Provate anche**

- `"soglia": 18` → 6 studenti, da `Esposito` a `Verdi`
- togliete la riga di `"soglia"` → `Chiave mancante: 'soglia'`; `"colonna": "punteggio"` → `Chiave mancante: 'punteggio'`
- `"file": "appello2.csv"` → `File non trovato: appello2.csv`; rinominate `config.json` → `File non trovato: config.json`
- togliete la virgola dopo `"voto"` → `config.json non valido alla riga 4`; `"colonna": "cognome"` → la colonna non contiene numeri

---

## Challenge a scelta

Scegliete un tema. Le cinque challenge hanno la stessa difficoltà e usano gli stessi strumenti: cambiano la storia e i dati. Ogni tema continua nei laboratori successivi.

| Tema | Challenge | File |
|---|---|---|
| Mercati e finanza | Il portafoglio: prezzi da file | `ch_mercati.py` |
| Sport | Il campionato: tempi da file | `ch_sport.py` |
| Imprese e marketing | Il negozio online: ordini da file | `ch_negozio.py` |
| Salute e scienza | Lo studio clinico: misure da file | `ch_salute.py` |
| Caso e probabilità | Il tavolo da gioco: lanci da file | `ch_probabilita.py` |

**Tutte le challenge chiedono:**

- Create il file CSV della consegna con l'editor, nella stessa cartella del programma: copiate anche l'intestazione e lasciate un a capo dopo l'ultima riga. Una o due righe contengono un valore sbagliato.
- Scrivete una funzione `leggi(percorso: Path)` che legge il file con `csv.DictReader(f, delimiter=";")` e restituisce una tupla: un `defaultdict(list)` con i valori raggruppati e il numero di righe scartate.
- Dentro la funzione convertite il valore di ogni riga in un `try`: se c'è `ValueError` contate la riga come scartata e passate alla successiva.
- Nel blocco `if __name__ == "__main__":` chiamate la funzione dentro un `try`. Se il file non esiste (`FileNotFoundError`) stampate `File non trovato:` e il nome del file (`e.filename`).
- Per ogni gruppo, in ordine alfabetico, stampate una riga con le statistiche richieste. Mettete le stesse statistiche in un dizionario di dizionari e salvatelo in JSON con `json.dump(..., indent=2, ensure_ascii=False)`.
- Alla fine stampate il numero di righe scartate e il nome del file JSON salvato.

---

### Challenge · Mercati e finanza — Il portafoglio: prezzi da file (`ch_mercati.py`)

**Consegna**

1. Il file `chiusure.csv` contiene i prezzi di chiusura di `ENRG`, `BANK` e `TECH` dal 1° al 4 dicembre, copiati a mano. In due righe il prezzo manca o non è un numero.
2. La funzione `leggi` raggruppa i prezzi per titolo, nell'ordine del file.
3. Per ogni titolo stampate il numero di prezzi validi, la media con due decimali e il rendimento dal primo all'ultimo prezzo, `(ultimo - primo) / primo`, in percentuale con un decimale.
4. Salvate il riepilogo in `titoli.json`: per ogni titolo `prezzi`, `media` (arrotondata a 2 decimali) e `rendimento` (arrotondato a 4).

**File `chiusure.csv`** (createlo nella cartella del programma)

```
giorno;titolo;prezzo
01/12;ENRG;24.10
01/12;BANK;12.40
01/12;TECH;48.00
02/12;ENRG;24.60
02/12;BANK;12.20
02/12;TECH;sospeso
03/12;ENRG;25.30
03/12;BANK;12.70
03/12;TECH;50.40
04/12;BANK;
04/12;TECH;51.20
```

**Esempio di esecuzione**

```
BANK: 3 prezzi, media 12.43, rendimento 2.4%
ENRG: 3 prezzi, media 24.67, rendimento 5.0%
TECH: 3 prezzi, media 49.87, rendimento 6.7%
Righe scartate: 2. Salvato titoli.json
```

**Provate anche**

- aggiungete la riga `04/12;ENRG;25.10` → `ENRG: 4 prezzi, media 24.78, rendimento 4.1%`
- aggiungete invece `04/12;ENRG;25,10`, con la virgola → `Righe scartate: 3` e la riga di ENRG non cambia
- rinominate il file in `chiusure2.csv` → `File non trovato: chiusure.csv`

---

### Challenge · Sport — Il campionato: tempi da file (`ch_sport.py`)

**Consegna**

1. Il file `giri.csv` contiene i tempi sul giro, in secondi, dei primi tre giri di una gara, scritti dal cronometrista. In due righe al posto del tempo c'è una nota (`SC` per safety car, `box` per il pit stop).
2. La funzione `leggi` raggruppa i tempi per pilota.
3. Per ogni pilota stampate il numero di giri validi, il tempo medio e il giro migliore (`min`), con due decimali.
4. Salvate il riepilogo in `piloti.json`: per ogni pilota `giri`, `media` (arrotondata a 2 decimali) e `migliore`.

**File `giri.csv`** (createlo nella cartella del programma)

```
giro;pilota;tempo
1;Ferri;92.4
1;Lanza;92.9
1;Moro;93.1
1;Neri;93.6
2;Ferri;92.1
2;Lanza;SC
2;Moro;92.8
2;Neri;93.0
3;Ferri;92.6
3;Lanza;92.5
3;Moro;box
```

**Esempio di esecuzione**

```
Ferri: 3 giri, media 92.37, migliore 92.10
Lanza: 2 giri, media 92.70, migliore 92.50
Moro: 2 giri, media 92.95, migliore 92.80
Neri: 2 giri, media 93.30, migliore 93.00
Righe scartate: 2. Salvato piloti.json
```

**Provate anche**

- aggiungete la riga `3;Neri;93.4` → `Neri: 3 giri, media 93.33, migliore 93.00`
- aggiungete invece `3;Neri;1:33.4` → `Righe scartate: 3` e la riga di Neri non cambia
- rinominate il file in `giri2.csv` → `File non trovato: giri.csv`

---

### Challenge · Imprese e marketing — Il negozio online: ordini da file (`ch_negozio.py`)

**Consegna**

1. Il file `ordini.csv` contiene gli ordini di una settimana: cliente, città e importo in euro. In due righe l'importo manca o non è un numero.
2. La funzione `leggi` raggruppa gli importi per città.
3. Per ogni città stampate il numero di ordini validi, l'importo medio e il totale, con due decimali.
4. Salvate il riepilogo in `citta.json`: per ogni città `ordini`, `media` e `totale`, arrotondati a 2 decimali.

**File `ordini.csv`** (createlo nella cartella del programma)

```
cliente;citta;importo
Giulia;Padova;45.90
Marco;Venezia;18.50
Sara;Padova;32.00
Luca;Verona;64.80
Elena;Vicenza;12.90
Paolo;Venezia;omaggio
Anna;Padova;27.40
Davide;Verona;29.90
Marta;Vicenza;38.00
Giulia;Padova;
Marco;Venezia;22.00
```

**Esempio di esecuzione**

```
Padova: 3 ordini, media 35.10, totale 105.30
Venezia: 2 ordini, media 20.25, totale 40.50
Verona: 2 ordini, media 47.35, totale 94.70
Vicenza: 2 ordini, media 25.45, totale 50.90
Righe scartate: 2. Salvato citta.json
```

**Provate anche**

- completate la riga di Giulia con `Giulia;Padova;15.50` → `Padova: 4 ordini, media 30.20, totale 120.80`, `Righe scartate: 1`
- aggiungete `Sara;Padova;20 EUR` → `Righe scartate: 3` e la riga di Padova non cambia
- rinominate il file in `ordini2.csv` → `File non trovato: ordini.csv`

---

### Challenge · Salute e scienza — Lo studio clinico: misure da file (`ch_salute.py`)

**Consegna**

1. Il file `pressione.csv` contiene la pressione sistolica (mmHg) dei pazienti dello studio alla fine del trattamento. Per due pazienti la misura manca.
2. La funzione `leggi` raggruppa le misure per gruppo (`trattamento` o `controllo`).
3. Per ogni gruppo stampate il numero di pazienti con una misura valida, la media con un decimale e la quota di pazienti sotto 140 mmHg, in percentuale con un decimale.
4. Salvate il riepilogo in `gruppi.json`: per ogni gruppo `pazienti`, `media` (arrotondata a 1 decimale) e `sotto_140` (arrotondata a 3).

**File `pressione.csv`** (createlo nella cartella del programma)

```
paziente;gruppo;sistolica
P01;trattamento;128
P02;controllo;142
P03;trattamento;135
P04;controllo;138
P05;trattamento;n.d.
P06;controllo;151
P07;trattamento;131
P08;controllo;
P09;trattamento;144
P10;controllo;135
P11;trattamento;126
```

**Esempio di esecuzione**

```
controllo: 4 pazienti, media 141.5 mmHg, sotto 140: 50.0%
trattamento: 5 pazienti, media 132.8 mmHg, sotto 140: 80.0%
Righe scartate: 2. Salvato gruppi.json
```

**Provate anche**

- completate la riga di P08 con `P08;controllo;139` → `controllo: 5 pazienti, media 141.0 mmHg, sotto 140: 60.0%`, `Righe scartate: 1`
- aggiungete `P12;trattamento;130 mmHg` → `Righe scartate: 3` e la riga del trattamento non cambia
- rinominate il file in `pressione2.csv` → `File non trovato: pressione.csv`

---

### Challenge · Caso e probabilità — Il tavolo da gioco: lanci da file (`ch_probabilita.py`)

**Consegna**

1. Il file `lanci.csv` contiene i lanci di un dado fatti da tre giocatori e registrati a mano. In due righe il risultato manca o è scritto in lettere.
2. La funzione `leggi` raggruppa i risultati per giocatore; convertiteli con `int()`.
3. Per ogni giocatore stampate il numero di lanci validi, la media con due decimali e la quota di 6 (`count(6)`), in percentuale con un decimale.
4. Salvate il riepilogo in `giocatori.json`: per ogni giocatore `lanci`, `media` (arrotondata a 2 decimali) e `quota_sei` (arrotondata a 3).

**File `lanci.csv`** (createlo nella cartella del programma)

```
lancio;giocatore;dado
1;Anna;4
2;Marco;6
3;Giulia;2
4;Anna;6
5;Marco;3
6;Giulia;sei
7;Anna;1
8;Marco;6
9;Giulia;5
10;Anna;
11;Giulia;6
```

**Esempio di esecuzione**

```
Anna: 3 lanci, media 3.67, quota di 6: 33.3%
Giulia: 3 lanci, media 4.33, quota di 6: 33.3%
Marco: 3 lanci, media 5.00, quota di 6: 66.7%
Righe scartate: 2. Salvato giocatori.json
```

**Provate anche**

- completate la riga 10 con `10;Anna;6` → `Anna: 4 lanci, media 4.25, quota di 6: 50.0%`, `Righe scartate: 1`
- aggiungete `12;Marco;4.5` → `int("4.5")` dà `ValueError`: `Righe scartate: 3`
- rinominate il file in `lanci2.csv` → `File non trovato: lanci.csv`

---

## Domande di verifica

1. Che differenza c'è tra aprire un file con `"w"` e con `"a"`? Cosa succederebbe a `spese.csv` usando `"w"`?
2. In `conta_righe.py`, perché una riga vuota dà 0 parole anche se contiene il carattere `\n`?
3. `csv.DictReader` restituisce `{'voto': '28', ...}`. Perché serve `int()` prima di fare la media?
4. Che differenza c'è tra `json.load` e `json.loads`? E tra `json.dump` e `json.dumps`?
5. In `appello_robusto.py` il `try` sul voto è dentro il `for`. Cosa cambierebbe mettendolo fuori dal ciclo?
6. In `config_soglia.py`, cosa succede se nel JSON scrivete `"soglia": "27"`, tra virgolette? Quale eccezione si ottiene?
7. Nella sfida, perché `float("38,5")` dà errore e come lo si evita?
