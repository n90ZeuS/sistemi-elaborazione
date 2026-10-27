# Laboratorio 5 — File e gestione dati

**Prerequisiti:** lezioni T15 (File, dati ed errori).

Oggi si lavora con dati che stanno nei file: testo, CSV e JSON. Per ogni esercizio create un file `.py` con il nome indicato, nella stessa cartella dei file di dati. I file di dati sono scritti nella slide dell'esercizio: create il file con l'editor e copiate il contenuto, compresa la riga di intestazione, e lasciate un a capo dopo l'ultima riga. Le classi non servono.

Ogni esercizio ha la consegna, un esempio di esecuzione e alcuni casi da provare: il programma è corretto quando dà gli stessi risultati. La sfida è per chi finisce prima. Le soluzioni le vediamo all'inizio della lezione T17.

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
| Sfida | `pipeline_pm10.py` | PM10 a Padova |

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

## Sfida — PM10 a Padova (`pipeline_pm10.py`)

**Consegna**

1. Il file `rilevazioni.csv` contiene le misure giornaliere di PM10 (µg/m³) di tre stazioni di Padova, scritte a mano e con diversi problemi (vedi tabella).
2. Scrivete una funzione `pulisci(percorso: Path)` che restituisce un dizionario stazione → lista di misure valide (`defaultdict(list)`) e il numero di righe scartate.
3. Nel blocco `if __name__ == "__main__":` calcolate per ogni stazione, in ordine alfabetico, media (`round(..., 1)`), massimo e giorni oltre il limite di 50, e stampate il dizionario di ogni stazione.
4. Salvate tutto in `pm10.json` (un dizionario di dizionari) e stampate il numero di righe scartate.

| Problema | Cosa fare |
|---|---|
| spazi e maiuscole nel nome | `strip()` e `title()` |
| stazione vuota | scartare la riga |
| virgola decimale | `replace(",", ".")` prima di `float()` |
| `N/D` o campo vuoto | scartare la riga |
| valore negativo | scartare la riga |

**File `rilevazioni.csv`** (createlo nella cartella del programma)

```
stazione;data;pm10
Mandria;01/12/2026;38,5
Arcella;01/12/2026;52
 mandria ;02/12/2026;61,2
Arcella;02/12/2026;N/D
;02/12/2026;44
Granze;01/12/2026;27,8
Granze;02/12/2026;
ARCELLA;03/12/2026;48,9
Mandria;03/12/2026;55
Granze;03/12/2026;-3
```

**Esempio di esecuzione**

```
Arcella: {'media': 50.5, 'massimo': 52.0, 'giorni_oltre': 1}
Granze: {'media': 27.8, 'massimo': 27.8, 'giorni_oltre': 0}
Mandria: {'media': 51.6, 'massimo': 61.2, 'giorni_oltre': 2}
Righe scartate: 4. Salvato pm10.json
```

**Provate anche**

- aggiungete `Granze;04/12/2026;71,0` → `Granze: {'media': 49.4, 'massimo': 71.0, 'giorni_oltre': 1}`
- un file con la sola intestazione → `Righe scartate: 0` e `pm10.json` contiene `{}`
- aggiungete al JSON il numero di misure valide di ogni stazione

---

## Domande di verifica

1. Che differenza c'è tra aprire un file con `"w"` e con `"a"`? Cosa succederebbe a `spese.csv` usando `"w"`?
2. In `conta_righe.py`, perché una riga vuota dà 0 parole anche se contiene il carattere `\n`?
3. `csv.DictReader` restituisce `{'voto': '28', ...}`. Perché serve `int()` prima di fare la media?
4. Che differenza c'è tra `json.load` e `json.loads`? E tra `json.dump` e `json.dumps`?
5. In `appello_robusto.py` il `try` sul voto è dentro il `for`. Cosa cambierebbe mettendolo fuori dal ciclo?
6. In `config_soglia.py`, cosa succede se nel JSON scrivete `"soglia": "27"`, tra virgolette? Quale eccezione si ottiene?
7. Nella sfida, perché `float("38,5")` dà errore e come lo si evita?
