# Frontale 15 — File, dati e gestione degli errori

## Introduzione: il programma incontra il mondo reale

Fino ad ora abbiamo lavorato con dati definiti direttamente nel codice: liste scritte a mano, dizionari costruiti riga per riga, variabili inizializzate con valori inventati. Questo è utile per imparare, ma non è il modo in cui si lavora davvero. Nella pratica statistica, i dati arrivano *da fuori*: file CSV esportati da un database, file JSON restituiti da un'API, fogli di calcolo salvati da un collega. Il programma deve saper leggere questi dati, elaborarli e scrivere i risultati.

C'è però un problema: il mondo reale è disordinato. I file possono non esistere, avere un encoding sbagliato, contenere righe malformate, mancare di colonne attese. Un programma robusto non può semplicemente sperare che tutto vada bene: deve *gestire gli errori* in modo esplicito e controllato.

In questa lezione impariamo a far dialogare Python con il filesystem, a leggere e scrivere i formati di dati più comuni (testo, CSV, JSON), e a proteggerci dagli errori con il meccanismo delle eccezioni.

---

## 1. Aprire e chiudere file: `open()` e il context manager `with`

### La funzione `open()`

Per lavorare con un file, il primo passo è *aprirlo*. Python offre la funzione built-in `open()`, che restituisce un oggetto file (un "handle") attraverso il quale possiamo leggere o scrivere.

```python
# Apertura base — NON fare così (spiegheremo perché)
f = open("dati.txt", "r", encoding="utf-8")
contenuto: str = f.read()
f.close()
```

I parametri principali di `open()` sono:

| Parametro   | Significato |
|-------------|-------------|
| `file`      | Percorso del file (stringa o oggetto `Path`) |
| `mode`      | Modalità di apertura |
| `encoding`  | Codifica del testo (quasi sempre `"utf-8"`) |

### Le modalità di apertura

| Modalità | Significato | Il file deve esistere? |
|----------|-------------|------------------------|
| `"r"` | Lettura (read) — default | Sì |
| `"w"` | Scrittura (write) — sovrascrive | No (lo crea) |
| `"a"` | Aggiunta (append) — scrive in fondo | No (lo crea) |
| `"x"` | Creazione esclusiva — errore se esiste | No (lo crea) |

A queste si può aggiungere `"b"` per la modalità binaria (`"rb"`, `"wb"`), utile per immagini, file compressi e simili. Per i file di testo, la modalità predefinita è sufficiente.

### Perché specificare sempre `encoding="utf-8"`

L'encoding predefinito dipende dal sistema operativo. Su Windows è spesso `"cp1252"`, su macOS e Linux è `"utf-8"`. Questo significa che un programma che funziona su macOS potrebbe produrre caratteri incomprensibili su Windows. Specificare esplicitamente `encoding="utf-8"` rende il codice *portabile* e prevedibile.

### Il context manager `with` — usarlo SEMPRE

Il codice mostrato sopra ha un difetto grave: se si verifica un errore tra `open()` e `close()`, il file resta aperto. I file aperti consumano risorse del sistema operativo, e se ne accumulate troppi il programma (o l'intero sistema) può bloccarsi.

Il *context manager* `with` risolve il problema in modo elegante: garantisce che il file venga chiuso automaticamente all'uscita dal blocco, anche se si verifica un'eccezione.

```python
# Il modo CORRETTO di aprire un file
with open("dati.txt", "r", encoding="utf-8") as f:
    contenuto: str = f.read()
# Qui il file è già chiuso, qualunque cosa sia successa
```

Questa è una regola senza eccezioni: **usate sempre `with` per aprire i file**. Non esiste un caso in cui sia meglio fare diversamente.

---

## 2. Leggere file di testo

Una volta aperto un file in lettura, abbiamo diversi modi per accedere al contenuto.

### `read()` — tutto in una volta

```python
with open("romanzo.txt", "r", encoding="utf-8") as f:
    testo: str = f.read()

print(len(testo))  # Numero di caratteri
```

Comodo per file piccoli, ma pericoloso per file grandi: se il file pesa 4 GB, Python cercherà di caricare 4 GB in memoria.

### `readline()` — una riga alla volta

```python
with open("dati.txt", "r", encoding="utf-8") as f:
    prima_riga: str = f.readline()   # Include il '\n' finale
    seconda_riga: str = f.readline()
```

### `readlines()` — tutte le righe in una lista

```python
with open("dati.txt", "r", encoding="utf-8") as f:
    righe: list[str] = f.readlines()  # Ogni elemento include '\n'

print(righe[0].strip())  # .strip() rimuove spazi e '\n'
```

### Iterazione riga per riga — il modo migliore

Per file di qualsiasi dimensione, il modo più efficiente e idiomatico è iterare direttamente sull'oggetto file:

```python
def conta_righe_non_vuote(percorso: str) -> int:
    """Conta le righe che contengono almeno un carattere non-spazio."""
    conteggio: int = 0
    with open(percorso, "r", encoding="utf-8") as f:
        for riga in f:
            if riga.strip():
                conteggio += 1
    return conteggio
```

Questo approccio legge una riga alla volta dalla memoria, quindi funziona anche su file enormi.

---

## 3. Scrivere file di testo

### `write()` — scrivere una stringa

```python
def salva_risultato(percorso: str, media: float, n: int) -> None:
    """Salva un riepilogo statistico su file."""
    with open(percorso, "w", encoding="utf-8") as f:
        f.write(f"Numero osservazioni: {n}\n")
        f.write(f"Media: {media:.4f}\n")
```

Notate che `write()` non aggiunge automaticamente il carattere di "a capo" (`\n`): dovete inserirlo voi.

### `writelines()` — scrivere una sequenza di stringhe

```python
def salva_nomi(percorso: str, nomi: list[str]) -> None:
    """Salva una lista di nomi, uno per riga."""
    righe: list[str] = [nome + "\n" for nome in nomi]
    with open(percorso, "w", encoding="utf-8") as f:
        f.writelines(righe)
```

Anche `writelines()` non aggiunge `\n` automaticamente: le righe devono già contenere il terminatore.

### Aggiungere a un file esistente

```python
def registra_evento(percorso: str, evento: str) -> None:
    """Aggiunge un evento al file di log."""
    with open(percorso, "a", encoding="utf-8") as f:
        f.write(f"{evento}\n")
```

La modalità `"a"` (append) non cancella il contenuto esistente: scrive in fondo.

---

## 4. `pathlib` — percorsi cross-platform moderni

Concatenare percorsi con le stringhe è fragile e non portabile:

```python
# MALE: funziona solo su Unix, si rompe su Windows
percorso: str = "dati" + "/" + "2024" + "/" + "risultati.csv"
```

Il modulo `pathlib`, introdotto in Python 3.4, offre un'alternativa elegante e sicura:

```python
from pathlib import Path

# L'operatore / costruisce percorsi in modo cross-platform
percorso: Path = Path("dati") / "2024" / "risultati.csv"
print(percorso)  # dati/2024/risultati.csv (Unix) o dati\2024\risultati.csv (Windows)
```

### Operazioni comuni con `Path`

```python
from pathlib import Path

p: Path = Path("dati") / "esperimento" / "misure.csv"

# Informazioni sul percorso
print(p.name)       # "misure.csv"
print(p.stem)       # "misure"
print(p.suffix)     # ".csv"
print(p.parent)     # dati/esperimento

# Verifica esistenza
if p.exists():
    print("Il file esiste")

if p.is_file():
    print("È un file (non una directory)")

# Creare directory (anche annidate)
cartella: Path = Path("output") / "grafici"
cartella.mkdir(parents=True, exist_ok=True)

# Elencare file in una directory
cartella_dati: Path = Path("dati")
for file_csv in cartella_dati.glob("*.csv"):
    print(file_csv.name)
```

### `Path` e `open()`

Gli oggetti `Path` funzionano direttamente con `open()`:

```python
from pathlib import Path

percorso: Path = Path("dati") / "studenti.csv"
with open(percorso, "r", encoding="utf-8") as f:
    contenuto: str = f.read()
```

Oppure, ancora più conciso:

```python
from pathlib import Path

percorso: Path = Path("dati") / "studenti.csv"
contenuto: str = percorso.read_text(encoding="utf-8")
```

Usate `pathlib` in ogni progetto: rende il codice più leggibile e portabile.

---

## 5. Lavorare con file CSV

Il formato CSV (*Comma-Separated Values*) è lo standard de facto per i dati tabulari. Ogni riga è un record, ogni campo è separato da un delimitatore (tipicamente la virgola).

```
nome,cognome,voto
Anna,Rossi,28
Marco,Bianchi,25
```

### Leggere CSV con `csv.reader`

```python
import csv

def leggi_voti(percorso: str) -> list[tuple[str, str, int]]:
    """Legge un CSV di studenti e restituisce una lista di tuple."""
    risultati: list[tuple[str, str, int]] = []
    with open(percorso, "r", encoding="utf-8") as f:
        lettore = csv.reader(f)
        intestazione = next(lettore)  # Salta la riga di intestazione
        for riga in lettore:
            nome: str = riga[0]
            cognome: str = riga[1]
            voto: int = int(riga[2])
            risultati.append((nome, cognome, voto))
    return risultati
```

### Leggere CSV con `csv.DictReader` — più leggibile

`DictReader` usa la prima riga come chiavi e restituisce ogni riga come dizionario:

```python
import csv

def leggi_voti_dict(percorso: str) -> list[dict[str, str]]:
    """Legge un CSV e restituisce una lista di dizionari."""
    with open(percorso, "r", encoding="utf-8") as f:
        lettore = csv.DictReader(f)
        return list(lettore)

# Uso:
studenti: list[dict[str, str]] = leggi_voti_dict("voti.csv")
for s in studenti:
    print(f"{s['nome']} {s['cognome']}: {s['voto']}")
```

### Il problema del separatore nei CSV europei

In molti paesi europei (Italia inclusa), la virgola è il separatore decimale. Per evitare confusione, i CSV esportati da Excel in italiano usano il *punto e virgola* come delimitatore:

```
nome;cognome;voto
Anna;Rossi;28
Marco;Bianchi;25
```

Per gestirlo, basta specificare il parametro `delimiter`:

```python
import csv

with open("dati_italiani.csv", "r", encoding="utf-8") as f:
    lettore = csv.DictReader(f, delimiter=";")
    for riga in lettore:
        print(riga)
```

### Scrivere CSV

```python
import csv

def salva_risultati(percorso: str, dati: list[dict[str, str | float]]) -> None:
    """Salva una lista di dizionari come CSV."""
    if not dati:
        return
    campi: list[str] = list(dati[0].keys())
    with open(percorso, "w", encoding="utf-8", newline="") as f:
        scrittore = csv.DictWriter(f, fieldnames=campi)
        scrittore.writeheader()
        scrittore.writerows(dati)
```

Il parametro `newline=""` è importante su Windows per evitare righe vuote extra nel file.

**Anticipazione**: quando lavoreremo con Pandas (Lezione 17), caricare un CSV sarà una singola riga: `pd.read_csv("file.csv")`. Ma capire cosa succede "sotto il cofano" è essenziale per diagnosticare problemi.

---

## 6. Lavorare con file JSON

JSON (*JavaScript Object Notation*) è il formato standard per lo scambio di dati strutturati, specialmente con le API web. La sua sintassi è molto simile ai dizionari Python.

### Corrispondenza tipi JSON e Python

| JSON | Python |
|------|--------|
| `object` `{...}` | `dict` |
| `array` `[...]` | `list` |
| `string` `"..."` | `str` |
| `number` (intero) | `int` |
| `number` (decimale) | `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

### Le quattro funzioni del modulo `json`

```python
import json
```

| Funzione | Input | Output | Uso |
|----------|-------|--------|-----|
| `json.load(f)` | File | Oggetto Python | Leggere da file |
| `json.dump(obj, f)` | Oggetto Python | File | Scrivere su file |
| `json.loads(s)` | Stringa | Oggetto Python | Parsare stringa JSON |
| `json.dumps(obj)` | Oggetto Python | Stringa | Serializzare a stringa |

Il trucco mnemonico: la `s` finale sta per *string*.

### Leggere JSON da file

```python
import json
from pathlib import Path

def carica_configurazione(percorso: Path) -> dict[str, str | int | bool]:
    """Carica un file di configurazione JSON."""
    with open(percorso, "r", encoding="utf-8") as f:
        config: dict[str, str | int | bool] = json.load(f)
    return config

# Uso
config: dict[str, str | int | bool] = carica_configurazione(
    Path("config.json")
)
print(config["database_host"])
```

### Scrivere JSON su file

```python
import json
from pathlib import Path

def salva_risultati_json(
    percorso: Path,
    risultati: dict[str, float]
) -> None:
    """Salva risultati statistici in formato JSON."""
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(risultati, f, indent=2, ensure_ascii=False)

# Uso
risultati: dict[str, float] = {
    "media": 25.7,
    "deviazione_standard": 3.2,
    "mediana": 26.0
}
salva_risultati_json(Path("risultati.json"), risultati)
```

Il parametro `indent=2` produce JSON leggibile (indentato con 2 spazi). Il parametro `ensure_ascii=False` permette di scrivere caratteri come `à`, `è`, `ù` senza codificarli come sequenze di escape.

### JSON da stringa — utile con le API

Quando si ricevono dati da un'API web, la risposta è tipicamente una stringa JSON:

```python
import json

risposta_api: str = '{"temperatura": 22.5, "città": "Roma", "umidità": 65}'
dati: dict[str, float | str] = json.loads(risposta_api)
print(f"A {dati['città']} ci sono {dati['temperatura']}°C")
```

---

## 7. Eccezioni e gestione degli errori

### Il problema

Considerate questo codice innocente:

```python
valore: int = int(input("Inserisci un numero: "))
```

Cosa succede se l'utente scrive `"ciao"`? Python solleva un `ValueError` e il programma termina bruscamente. In un programma reale — che magari sta analizzando migliaia di righe di dati — un singolo valore malformato non dovrebbe far crollare tutto.

### `try` / `except`

Il blocco `try`/`except` permette di *catturare* un'eccezione e decidere cosa fare:

```python
def leggi_intero(prompt: str) -> int:
    """Chiede un intero all'utente, ripetendo in caso di errore."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Non è un numero valido. Riprova.")
```

Il flusso è:
1. Python esegue il codice nel blocco `try`.
2. Se non ci sono errori, il blocco `except` viene saltato.
3. Se si verifica l'eccezione specificata, il controllo passa al blocco `except`.

### La gerarchia delle eccezioni

Le eccezioni Python formano una gerarchia ad albero. Ecco le più importanti:

```
BaseException
├── KeyboardInterrupt      # Ctrl+C
├── SystemExit             # sys.exit()
└── Exception
    ├── ValueError          # Valore sbagliato ("abc" per int())
    ├── TypeError           # Tipo sbagliato (1 + "a")
    ├── KeyError            # Chiave mancante in un dizionario
    ├── IndexError          # Indice fuori range
    ├── FileNotFoundError   # File non trovato
    ├── PermissionError     # Permessi insufficienti
    ├── ZeroDivisionError   # Divisione per zero
    ├── OSError             # Errori del sistema operativo
    └── ...
```

Notate che `KeyboardInterrupt` e `SystemExit` *non* ereditano da `Exception`. Questo è intenzionale: catturare `Exception` non blocca Ctrl+C.

### Catturare eccezioni specifiche — regola fondamentale

```python
# MALE — cattura TUTTO, anche errori che non vi aspettavate
try:
    risultato = calcola_qualcosa(dati)
except Exception:
    print("Qualcosa è andato storto")  # Ma cosa?!

# BENE — cattura solo gli errori prevedibili
try:
    risultato = calcola_qualcosa(dati)
except ValueError as e:
    print(f"Valore non valido: {e}")
except ZeroDivisionError:
    print("Divisione per zero nel calcolo")
```

Catturare eccezioni troppo generiche nasconde i bug: il programma sembra funzionare, ma produce risultati sbagliati. La regola è: **catturate solo le eccezioni che sapete gestire**.

### `else` e `finally`

Il blocco `try` ha due clausole opzionali poco conosciute ma molto utili:

```python
def leggi_dati_sicuro(percorso: str) -> list[str]:
    """Legge un file, gestendo l'assenza e gli errori di encoding."""
    try:
        f = open(percorso, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"File non trovato: {percorso}")
        return []
    except PermissionError:
        print(f"Permessi insufficienti per: {percorso}")
        return []
    else:
        # Eseguito SOLO se try è andato a buon fine
        contenuto: list[str] = f.readlines()
        return contenuto
    finally:
        # Eseguito SEMPRE, errore o no
        print("Tentativo di lettura completato.")
```

- **`else`**: eseguito solo se il `try` non ha generato eccezioni. Utile per separare il codice "che può fallire" dal codice "che segue il successo".
- **`finally`**: eseguito *sempre*, che ci sia stato un errore o meno. Utile per operazioni di cleanup (chiudere connessioni, rilasciare risorse). Con `with` il `finally` è meno necessario, ma resta utile in altri contesti.

### `raise` — sollevare eccezioni intenzionalmente

A volte siete voi a dover segnalare un errore. La parola chiave `raise` solleva un'eccezione:

```python
def calcola_media(voti: list[int]) -> float:
    """Calcola la media aritmetica dei voti.

    Raises:
        ValueError: Se la lista è vuota o contiene voti fuori range.
    """
    if not voti:
        raise ValueError("Impossibile calcolare la media di una lista vuota")
    for voto in voti:
        if not 0 <= voto <= 30:
            raise ValueError(f"Voto fuori range: {voto}")
    return sum(voti) / len(voti)
```

Sollevare eccezioni con messaggi chiari è un atto di gentilezza verso chi userà il vostro codice (incluso il vostro sé futuro).

### EAFP vs LBYL

Python adotta la filosofia **EAFP** (*Easier to Ask Forgiveness than Permission*): è meglio provare e gestire l'errore piuttosto che controllare tutto in anticipo.

```python
# LBYL (Look Before You Leap) — stile non-pythonic
def ottieni_valore_lbyl(dati: dict[str, int], chiave: str) -> int | None:
    if chiave in dati:
        return dati[chiave]
    else:
        return None

# EAFP (Easier to Ask Forgiveness than Permission) — stile pythonic
def ottieni_valore_eafp(dati: dict[str, int], chiave: str) -> int | None:
    try:
        return dati[chiave]
    except KeyError:
        return None
```

Perché EAFP è preferito? Perché evita *race condition* (il dato potrebbe cambiare tra il controllo e l'accesso) e perché il caso "normale" (nessun errore) è più veloce.

---

## 8. Esempio completo: leggere un CSV problematico

Mettiamo tutto insieme con un esempio realistico. Immaginate di ricevere un file CSV di risposte a un questionario. Il file ha diversi problemi:
- Potrebbe non esistere.
- Potrebbe usare il separatore `;` (CSV europeo).
- Alcune righe hanno campi mancanti.
- Il campo "età" contiene a volte valori non numerici.

```python
import csv
from pathlib import Path


def carica_risposte(percorso: Path) -> list[dict[str, str | int | None]]:
    """Carica risposte da un CSV, gestendo errori comuni.

    Args:
        percorso: Path al file CSV.

    Returns:
        Lista di dizionari con le risposte valide.

    Raises:
        FileNotFoundError: Se il file non esiste.
    """
    risposte: list[dict[str, str | int | None]] = []
    righe_problematiche: int = 0

    try:
        with open(percorso, "r", encoding="utf-8") as f:
            # Rileva il dialetto (separatore) automaticamente
            campione: str = f.read(1024)
            f.seek(0)  # Torna all'inizio

            try:
                dialetto = csv.Sniffer().sniff(campione, delimiters=",;\t")
            except csv.Error:
                # Se il rilevamento fallisce, usa la virgola
                dialetto = csv.excel

            lettore = csv.DictReader(f, dialect=dialetto)

            for numero_riga, riga in enumerate(lettore, start=2):
                try:
                    risposta: dict[str, str | int | None] = {
                        "nome": riga.get("nome", "").strip(),
                        "cognome": riga.get("cognome", "").strip(),
                    }

                    # Gestione del campo età
                    eta_raw: str | None = riga.get("età", riga.get("eta"))
                    if eta_raw and eta_raw.strip():
                        try:
                            risposta["età"] = int(eta_raw.strip())
                        except ValueError:
                            print(f"  Riga {numero_riga}: età non valida "
                                  f"'{eta_raw}', impostata a None")
                            risposta["età"] = None
                    else:
                        risposta["età"] = None

                    # Scarta righe senza nome
                    if not risposta["nome"]:
                        print(f"  Riga {numero_riga}: nome mancante, "
                              f"riga scartata")
                        righe_problematiche += 1
                        continue

                    risposte.append(risposta)

                except Exception as e:
                    print(f"  Riga {numero_riga}: errore imprevisto: {e}")
                    righe_problematiche += 1

    except FileNotFoundError:
        print(f"File non trovato: {percorso}")
        raise
    except UnicodeDecodeError:
        print(f"Errore di encoding in {percorso}. "
              f"Provare con encoding diverso (es. 'latin-1').")
        raise

    print(f"Caricate {len(risposte)} risposte valide, "
          f"{righe_problematiche} righe scartate.")
    return risposte


# Uso
if __name__ == "__main__":
    percorso_dati: Path = Path("dati") / "questionario.csv"
    try:
        risposte: list[dict[str, str | int | None]] = carica_risposte(
            percorso_dati
        )
        for r in risposte[:5]:
            print(r)
    except (FileNotFoundError, UnicodeDecodeError):
        print("Impossibile caricare i dati.")
```

Questo esempio mostra come i concetti di questa lezione — `open()` con `with`, lettura CSV, gestione eccezioni, `pathlib` — si combinano in un programma reale. Non è necessario scrivere codice così complesso per ogni esercizio, ma è importante capire il *pattern*: provare, catturare l'errore specifico, gestirlo o rilanciarlo.

---

## Domande di verifica

1. Perché è importante usare sempre `with open(...)` invece di `open()` seguito da `close()`? Cosa potrebbe andare storto senza il context manager?

2. Qual è la differenza tra le modalità `"w"` e `"a"` di `open()`? Cosa succede al contenuto esistente del file in ciascun caso?

3. Perché dovremmo specificare sempre `encoding="utf-8"` quando apriamo un file di testo?

4. Qual è la differenza tra `csv.reader` e `csv.DictReader`? In quale situazione preferireste l'uno o l'altro?

5. Spiegate la differenza tra `json.load()` e `json.loads()`. Quando si usa ciascuna?

6. Perché è sbagliato scrivere `except Exception` per catturare tutti gli errori? Che problema causa?

7. Cosa significa la filosofia EAFP? Fate un esempio pratico di codice EAFP vs LBYL.

8. Nel modulo `pathlib`, perché `Path("dati") / "file.csv"` è preferibile a `"dati" + "/" + "file.csv"`?

---

## Esercizi

### Base

**Esercizio 1 — Contaparole**

Scrivete una funzione `conta_parole(percorso: Path) -> dict[str, int]` che legge un file di testo e restituisce un dizionario con la frequenza di ogni parola (convertita in minuscolo). Usate `pathlib` per il percorso.

**Esercizio 2 — Scrittura di un report**

Scrivete una funzione `scrivi_report(percorso: Path, titolo: str, valori: list[float]) -> None` che crea un file di testo contenente: il titolo, il numero di valori, la media e il valore massimo. Ogni informazione su una riga separata.

**Esercizio 3 — Lettura CSV sicura**

Scrivete una funzione `leggi_csv_sicuro(percorso: Path) -> list[dict[str, str]]` che tenta di leggere un CSV. Se il file non esiste, stampa un messaggio e restituisce una lista vuota. Se il file esiste ma è vuoto, stampa un avviso e restituisce una lista vuota.

### Intermedio

**Esercizio 4 — Conversione CSV-JSON**

Scrivete un programma che legge un file CSV e lo converte in un file JSON equivalente. Il programma deve accettare il percorso del CSV come argomento e creare il JSON nella stessa directory con lo stesso nome ma estensione `.json`.

**Esercizio 5 — Unione di CSV**

Scrivete una funzione `unisci_csv(cartella: Path, output: Path) -> int` che trova tutti i file `.csv` in una cartella (usando `glob`), li unisce in un unico file CSV (mantenendo una sola riga di intestazione), e restituisce il numero totale di righe scritte.

**Esercizio 6 — Validazione dati**

Scrivete una funzione `valida_record(record: dict[str, str]) -> dict[str, str | int | float]` che riceve un dizionario letto da un CSV con chiavi `"nome"`, `"età"`, `"reddito"`. La funzione deve:
- Verificare che `"nome"` non sia vuoto (altrimenti `ValueError`).
- Convertire `"età"` a `int` (gestendo `ValueError` se non numerico).
- Convertire `"reddito"` a `float` (gestendo `ValueError`).
- Restituire il record "pulito" con i tipi corretti.

### Avanzato

**Esercizio 7 — Analizzatore di log**

Scrivete un programma che legge un file di log dove ogni riga ha il formato:
```
2024-03-15 14:32:01 INFO Avvio del sistema
2024-03-15 14:32:05 ERROR Connessione al database fallita
```

Il programma deve:
- Contare il numero di messaggi per ogni livello (INFO, WARNING, ERROR).
- Estrarre e salvare in un file separato tutti i messaggi di ERROR.
- Gestire righe malformate senza interrompere l'esecuzione.

**Esercizio 8 — Cache JSON**

Scrivete una classe `CacheSemplice` che memorizza coppie chiave-valore in un file JSON. La classe deve avere:
- `__init__(self, percorso: Path) -> None` — carica la cache dal file (se esiste).
- `get(self, chiave: str) -> str | None` — restituisce il valore o `None`.
- `set(self, chiave: str, valore: str) -> None` — inserisce o aggiorna e salva su disco.
- Tutta la gestione degli errori necessaria (file corrotto, permessi, ecc.).

---

## Osservazioni finali

In questa lezione abbiamo affrontato un passaggio fondamentale: far uscire i nostri programmi dall'isolamento del codice "autocontenuto" e metterli in comunicazione con il mondo esterno attraverso i file. Questo passaggio porta con sé una responsabilità nuova — la gestione degli errori — che distingue un programma "giocattolo" da un programma robusto e affidabile.

Le tre regole da portare con sé:
1. **Usate sempre `with`** per aprire i file.
2. **Catturate eccezioni specifiche**, mai generiche.
3. **Usate `pathlib`** per i percorsi: è più sicuro, più leggibile e più portabile.

Nella prossima lezione faremo un grande salto concettuale: passeremo dalla programmazione *procedurale* (funzioni che operano su dati) alla programmazione *orientata agli oggetti* (dati e comportamento uniti in un'unica entità). Scoprirete che molte delle cose che avete usato fin qui — stringhe, liste, dizionari, file — sono già oggetti. La lezione 16 vi darà gli strumenti per creare i vostri.
