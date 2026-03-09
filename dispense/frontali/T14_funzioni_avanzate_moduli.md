# Lezione 14 — Funzioni avanzate, moduli e ambienti

## Introduzione

Nelle lezioni precedenti abbiamo imparato a definire funzioni con `def`, a passare argomenti, a restituire valori e ad annotare i tipi. Le funzioni che avete scritto fino ad ora sono strumenti potenti, ma Python offre molto di piu: le funzioni non sono semplici blocchi di codice da invocare, sono **oggetti** a tutti gli effetti, manipolabili come qualsiasi altro dato. Potete assegnarle a variabili, passarle come argomenti ad altre funzioni, restituirle come risultato. Questa proprieta -- che i linguaggi di programmazione chiamano *funzioni come oggetti di prima classe* -- apre la porta a uno stile di programmazione elegante e conciso, particolarmente utile quando si lavora con dati.

Nella seconda parte della lezione cambiamo prospettiva: passiamo dall'interno di un singolo file all'organizzazione di un progetto. Scopriamo cosa sono i **moduli**, come importarli, come sfruttare la ricchissima **libreria standard** di Python e come installare **pacchetti esterni** da PyPI. Infine, affrontiamo un tema cruciale per la riproducibilita del lavoro scientifico: i **virtual environment**.

---

## 1. Funzioni come oggetti di prima classe

In Python, ogni funzione e un oggetto. Questo significa che una funzione ha un tipo (`function`), occupa memoria, e puo essere trattata esattamente come un numero, una stringa o una lista. Vediamo cosa questo implica in pratica.

### Assegnare una funzione a una variabile

Quando scriviamo il nome di una funzione **senza parentesi**, non la invochiamo: otteniamo un riferimento all'oggetto funzione stesso.

```python
def quadrato(x: float) -> float:
    return x ** 2

# Assegniamo la funzione (non il risultato!) a una variabile
operazione: callable = quadrato

print(operazione(5))    # 25
print(type(operazione)) # <class 'function'>
```

La variabile `operazione` ora punta allo stesso oggetto funzione di `quadrato`. Invocare `operazione(5)` e identico a invocare `quadrato(5)`. Questo puo sembrare una curiosita, ma e la base di pattern molto potenti.

### Passare una funzione come argomento

Se una funzione e un oggetto, possiamo passarla come argomento a un'altra funzione. Una funzione che riceve un'altra funzione come parametro si chiama **funzione di ordine superiore** (*higher-order function*).

```python
def applica_a_lista(f: callable, valori: list[float]) -> list[float]:
    """Applica la funzione f a ogni elemento della lista."""
    risultati: list[float] = []
    for v in valori:
        risultati.append(f(v))
    return risultati

def radice_quadrata(x: float) -> float:
    return x ** 0.5

numeri: list[float] = [4.0, 9.0, 16.0, 25.0]

print(applica_a_lista(quadrato, numeri))        # [16.0, 81.0, 256.0, 625.0]
print(applica_a_lista(radice_quadrata, numeri))  # [2.0, 3.0, 4.0, 5.0]
```

Notate che `applica_a_lista` non sa *quale* funzione ricevera: sa solo che ricevera *una* funzione e la applichera a ogni elemento. Questo rende il codice **generico** e **riusabile**. Lo stesso pattern e alla base di strumenti come `map()`, `filter()` e `sorted()` con `key`, che vedremo tra poco.

### Restituire una funzione da un'altra funzione

Python permette anche di creare funzioni che *restituiscono* altre funzioni. Questo pattern, piu avanzato, e alla base dei decoratori (che vedremo in lezioni successive), ma vale la pena vederne un esempio semplice.

```python
def crea_moltiplicatore(fattore: float) -> callable:
    """Restituisce una funzione che moltiplica per il fattore dato."""
    def moltiplicatore(x: float) -> float:
        return x * fattore
    return moltiplicatore

doppio: callable = crea_moltiplicatore(2)
triplo: callable = crea_moltiplicatore(3)

print(doppio(10))  # 20
print(triplo(10))  # 30
```

La funzione `crea_moltiplicatore` costruisce una nuova funzione ogni volta che viene invocata. La funzione interna "ricorda" il valore di `fattore` grazie a un meccanismo chiamato *closure*: la variabile `fattore` resta accessibile anche dopo che `crea_moltiplicatore` ha terminato la sua esecuzione.

---

## 2. Funzioni lambda

Quando serve una funzione breve, usa-e-getta, definirla con `def` puo sembrare eccessivo. Python offre una sintassi compatta per creare **funzioni anonime**: le espressioni `lambda`.

### Sintassi

```python
lambda parametri: espressione
```

Una lambda e una funzione che:
- non ha nome (e anonima);
- accetta zero o piu parametri;
- contiene **una sola espressione** (non istruzioni come `if`, `for`, `print` su piu righe);
- restituisce automaticamente il risultato dell'espressione.

```python
# Funzione lambda che calcola il quadrato
quadrato_lambda = lambda x: x ** 2
print(quadrato_lambda(5))  # 25

# Lambda con piu parametri
somma = lambda a, b: a + b
print(somma(3, 7))  # 10

# Lambda senza parametri
saluto = lambda: "Ciao!"
print(saluto())  # Ciao!
```

### Equivalenza con `def`

Una lambda e solo zucchero sintattico. Questa lambda:

```python
media = lambda valori: sum(valori) / len(valori)
```

e equivalente a:

```python
def media(valori: list[float]) -> float:
    return sum(valori) / len(valori)
```

La versione con `def` e piu leggibile, ha un nome significativo e supporta le annotazioni di tipo. Per questo motivo, **assegnare una lambda a una variabile e considerato cattivo stile**: se la funzione ha bisogno di un nome, usate `def`.

### Quando usare le lambda

Le lambda sono utili quando servono come **argomento inline** di un'altra funzione, specialmente con `sorted()`, `map()` e `filter()`. In questi casi, la brevita della lambda migliora la leggibilita:

```python
# BENE: lambda come argomento inline
nomi: list[str] = ["Marco", "Anna", "Giulia", "Bo"]
nomi_ordinati: list[str] = sorted(nomi, key=lambda s: len(s))
```

### Quando NON usare le lambda

- **Se la logica e complessa**: una lambda deve restare su una riga. Se vi trovate a scrivere espressioni contorte, usate `def`.
- **Se serve un nome descrittivo**: `def calcola_sconto(prezzo, percentuale)` e infinitamente piu chiaro di `lambda p, s: p * (1 - s / 100)`.
- **Se servono istruzioni**: le lambda accettano solo espressioni, non istruzioni come `for`, `while`, `try`.

La regola pratica e semplice: usate lambda quando la funzione e cosi breve e ovvia che darle un nome la renderebbe *meno* leggibile.

---

## 3. `sorted()` con `key=`: un pattern potentissimo

La funzione built-in `sorted()` restituisce una nuova lista ordinata. Nella sua forma base, ordina per ordine naturale (numerico per i numeri, lessicografico per le stringhe). Ma il vero potere di `sorted()` sta nel parametro `key`.

### Come funziona `key`

Il parametro `key` accetta una **funzione** che viene applicata a ogni elemento *prima* del confronto. L'ordinamento avviene sui valori restituiti dalla funzione, ma la lista risultante contiene gli elementi originali.

```python
parole: list[str] = ["Python", "è", "fantastico", "e", "potente"]

# Ordinamento lessicografico (default)
print(sorted(parole))
# ['Python', 'e', 'fantastico', 'potente', 'è']

# Ordinamento per lunghezza
print(sorted(parole, key=lambda s: len(s)))
# ['è', 'e', 'Python', 'potente', 'fantastico']
```

### Ordinare strutture complesse

Il pattern `sorted` + `key` diventa indispensabile quando lavoriamo con liste di dizionari o di tuple, una situazione comunissima nell'analisi dati.

```python
studenti: list[dict[str, object]] = [
    {"nome": "Anna",   "media": 28.5},
    {"nome": "Marco",  "media": 24.0},
    {"nome": "Giulia", "media": 30.0},
    {"nome": "Luca",   "media": 26.5},
]

# Ordinare per media (crescente)
per_media: list[dict[str, object]] = sorted(
    studenti, key=lambda s: s["media"]
)
for s in per_media:
    print(f"{s['nome']}: {s['media']}")
# Marco: 24.0
# Luca: 26.5
# Anna: 28.5
# Giulia: 30.0

# Ordinare per media (decrescente)
per_media_desc: list[dict[str, object]] = sorted(
    studenti, key=lambda s: s["media"], reverse=True
)
```

### Ordinare per piu criteri

Per ordinare su piu criteri, basta restituire una **tupla** dalla funzione `key`:

```python
esami: list[dict[str, object]] = [
    {"materia": "Statistica",   "voto": 28, "data": "2025-06-15"},
    {"materia": "Informatica",  "voto": 30, "data": "2025-06-10"},
    {"materia": "Matematica",   "voto": 28, "data": "2025-07-01"},
]

# Prima per voto (decrescente), poi per data (crescente)
ordinati: list[dict[str, object]] = sorted(
    esami, key=lambda e: (-e["voto"], e["data"])
)
```

Il trucco del segno meno (`-e["voto"]`) inverte l'ordine solo per quel criterio, mantenendo l'ordine crescente per gli altri.

### `min()` e `max()` con `key`

Lo stesso parametro `key` funziona anche con `min()` e `max()`:

```python
# Studente con la media piu alta
migliore: dict[str, object] = max(studenti, key=lambda s: s["media"])
print(migliore["nome"])  # Giulia
```

---

## 4. `map()` e `filter()`: strumenti funzionali

Python offre due funzioni built-in che incarnano lo stile **funzionale**: `map()` applica una funzione a ogni elemento, `filter()` seleziona gli elementi che soddisfano una condizione.

### `map()`

```python
voti: list[int] = [25, 28, 30, 22, 27]

# Convertire i voti in scala 0-100
voti_percentuale: list[float] = list(map(lambda v: v / 30 * 100, voti))
print(voti_percentuale)  # [83.33, 93.33, 100.0, 73.33, 90.0]
```

`map(f, iterabile)` restituisce un *iteratore* (non una lista), quindi va avvolto in `list()` se si vuole una lista. Applica la funzione `f` a ogni elemento dell'iterabile.

### `filter()`

```python
voti: list[int] = [25, 28, 30, 22, 27, 18, 31]

# Selezionare solo i voti sufficienti (>= 18) e validi (<= 30)
validi: list[int] = list(filter(lambda v: 18 <= v <= 30, voti))
print(validi)  # [25, 28, 30, 22, 27, 18]
```

`filter(f, iterabile)` restituisce gli elementi per cui `f` restituisce `True`.

### Confronto con le list comprehension

In Python, le stesse operazioni si possono esprimere con le **comprehension**, spesso in modo piu leggibile:

```python
# map equivalente
voti_percentuale: list[float] = [v / 30 * 100 for v in voti]

# filter equivalente
validi: list[int] = [v for v in voti if 18 <= v <= 30]

# map + filter combinati
voti_validi_percentuale: list[float] = [
    v / 30 * 100 for v in voti if 18 <= v <= 30
]
```

**Quale scegliere?** La comunita Python tende a preferire le comprehension per la loro leggibilita. Usate `map()` e `filter()` quando la funzione da applicare esiste gia con un nome:

```python
# map con funzione esistente: pulito
numeri_stringa: list[str] = ["1", "2", "3", "4"]
numeri: list[int] = list(map(int, numeri_stringa))

# Equivalente con comprehension: piu verboso senza vantaggio
numeri: list[int] = [int(s) for s in numeri_stringa]
```

In generale: se avete una funzione con un nome, `map()` e spesso piu conciso; se serve una lambda, la comprehension e quasi sempre piu chiara.

---

## 5. Moduli e `import`

Fino ad ora, tutto il codice era in un unico file. Ma i programmi reali sono fatti di molti file, ciascuno con una responsabilita specifica. In Python, **ogni file `.py` e un modulo**.

### Cos'e un modulo

Un modulo e semplicemente un file Python che contiene definizioni (funzioni, classi, variabili) e, eventualmente, codice eseguibile. Quando importate un modulo, Python esegue il file e rende disponibili le sue definizioni.

Supponiamo di avere un file `statistiche.py`:

```python
# statistiche.py
def media(valori: list[float]) -> float:
    """Calcola la media aritmetica."""
    return sum(valori) / len(valori)

def varianza(valori: list[float]) -> float:
    """Calcola la varianza campionaria."""
    m: float = media(valori)
    return sum((x - m) ** 2 for x in valori) / (len(valori) - 1)
```

### Importare un modulo

Ci sono diversi modi per importare:

```python
# 1. import del modulo intero
import statistiche

risultato: float = statistiche.media([1, 2, 3, 4, 5])
```

Con `import statistiche`, tutte le funzioni del modulo sono accessibili con il prefisso `statistiche.`. Questo e il modo piu esplicito e meno ambiguo.

```python
# 2. from ... import: importare nomi specifici
from statistiche import media, varianza

risultato: float = media([1, 2, 3, 4, 5])
```

Con `from ... import`, i nomi vengono importati direttamente nel namespace corrente: non serve il prefisso, ma si perde la tracciabilita dell'origine.

```python
# 3. Alias con as
import statistiche as stat

risultato: float = stat.media([1, 2, 3, 4, 5])
```

L'alias e utile per moduli con nomi lunghi. Alcune convenzioni sono universali: `import numpy as np`, `import pandas as pd`.

```python
# 4. MALE: import con asterisco — non fatelo mai
from statistiche import *  # Importa TUTTO, inquinando il namespace
```

L'import con `*` e pericoloso perche rende impossibile capire da dove vengono i nomi. Se due moduli definiscono una funzione con lo stesso nome, l'ultima sovrascrive la prima senza avvertimenti. Evitatelo sempre.

---

## 6. La libreria standard: "batteries included"

Python viene distribuito con una **libreria standard** vastissima: centinaia di moduli pronti all'uso, senza installare nulla. Questa filosofia si chiama *batteries included* ("batterie incluse"): Python arriva gia equipaggiato per la maggior parte dei compiti comuni.

Vediamo i moduli piu utili per il vostro percorso.

### `math` — Funzioni matematiche

```python
import math

print(math.sqrt(16))       # 4.0
print(math.log(100, 10))   # 2.0 (logaritmo in base 10)
print(math.log(math.e))    # 1.0 (logaritmo naturale)
print(math.pi)             # 3.141592653589793
print(math.factorial(5))   # 120
print(math.ceil(3.2))      # 4
print(math.floor(3.8))     # 3
```

### `statistics` — Statistica descrittiva

```python
import statistics

dati: list[float] = [2.5, 3.1, 2.8, 3.5, 2.9, 3.3, 3.0]

print(statistics.mean(dati))      # 3.014...
print(statistics.median(dati))    # 3.0
print(statistics.stdev(dati))     # 0.329...  (deviazione standard campionaria)
print(statistics.variance(dati))  # 0.108...  (varianza campionaria)
print(statistics.mode([1, 2, 2, 3, 3, 3]))  # 3
```

Questo modulo e perfetto per calcoli statistici di base. Per analisi piu avanzate si usera `numpy` o `scipy`.

### `random` — Numeri casuali

```python
import random

# Riproducibilita: fissare il seed
random.seed(42)

print(random.random())              # Float casuale in [0, 1)
print(random.randint(1, 100))       # Intero casuale in [1, 100]
print(random.uniform(0.0, 10.0))    # Float casuale in [0, 10]

nomi: list[str] = ["Anna", "Marco", "Giulia", "Luca"]
print(random.choice(nomi))          # Elemento casuale
print(random.sample(nomi, 2))       # 2 elementi senza ripetizione

random.shuffle(nomi)                # Mescola in-place
print(nomi)
```

**Nota fondamentale per la statistica**: `random.seed()` fissa il generatore di numeri pseudocasuali. Usandolo, otterrete sempre gli stessi risultati, rendendo le vostre analisi **riproducibili**.

### `csv` — Leggere e scrivere file CSV

```python
import csv

# Lettura
with open("dati.csv", "r", encoding="utf-8") as f:
    lettore = csv.DictReader(f)
    for riga in lettore:
        print(riga["nome"], riga["voto"])
```

### `json` — Dati strutturati

```python
import json

# Da stringa JSON a dizionario Python
testo: str = '{"nome": "Anna", "eta": 20}'
dati: dict[str, object] = json.loads(testo)
print(dati["nome"])  # Anna

# Da dizionario Python a stringa JSON
output: str = json.dumps(dati, indent=2, ensure_ascii=False)
print(output)
```

### `datetime` — Date e orari

```python
from datetime import date, datetime, timedelta

oggi: date = date.today()
print(oggi)  # 2026-03-08

tra_una_settimana: date = oggi + timedelta(days=7)
print(tra_una_settimana)  # 2026-03-15

nascita: date = date(2005, 6, 15)
eta: timedelta = oggi - nascita
print(f"Giorni vissuti: {eta.days}")
```

### `collections` — Strutture dati specializzate

```python
from collections import Counter, defaultdict

# Counter: contare frequenze
voti: list[int] = [28, 30, 28, 25, 30, 30, 27, 28]
frequenze: Counter = Counter(voti)
print(frequenze)              # Counter({30: 3, 28: 3, 25: 1, 27: 1})
print(frequenze.most_common(2))  # [(30, 3), (28, 3)]

# defaultdict: dizionario con valore predefinito
studenti_per_corso: defaultdict[str, list[str]] = defaultdict(list)
studenti_per_corso["Statistica"].append("Anna")
studenti_per_corso["Statistica"].append("Marco")
studenti_per_corso["Informatica"].append("Giulia")
print(dict(studenti_per_corso))
# {'Statistica': ['Anna', 'Marco'], 'Informatica': ['Giulia']}
```

---

## 7. Pacchetti esterni e pip

La libreria standard copre moltissimi casi, ma per il lavoro scientifico servono strumenti piu specializzati. L'ecosistema Python offre centinaia di migliaia di pacchetti tramite **PyPI** (Python Package Index, disponibile su [pypi.org](https://pypi.org)).

### Installare pacchetti con `pip`

`pip` e il gestore di pacchetti di Python. Si usa da terminale:

```bash
# Installare un pacchetto
pip install numpy

# Installare una versione specifica
pip install pandas==2.2.0

# Installare piu pacchetti
pip install numpy pandas matplotlib

# Aggiornare un pacchetto
pip install --upgrade numpy

# Vedere cosa e installato
pip list

# Disinstallare
pip uninstall numpy
```

Tra i pacchetti che userete nel vostro percorso:

| Pacchetto     | Scopo |
|---------------|-------|
| `numpy`       | Calcolo numerico con array multidimensionali |
| `pandas`      | Manipolazione e analisi di dati tabulari |
| `matplotlib`  | Grafici e visualizzazioni |
| `scipy`       | Statistica avanzata, ottimizzazione |
| `seaborn`     | Grafici statistici eleganti |

---

## 8. Virtual environment: isolamento e riproducibilita

### Il problema

Immaginate di lavorare a due progetti diversi. Il primo richiede `pandas` versione 1.5, il secondo richiede `pandas` versione 2.2. Se installate i pacchetti "globalmente" (cioe nel Python di sistema), potete avere una sola versione alla volta. Installare la 2.2 rompe il primo progetto; reinstallare la 1.5 rompe il secondo.

Questo problema si moltiplica quando collaborate con altre persone: ognuno ha versioni diverse, e il codice che funziona sul vostro computer non funziona su quello del collega.

### La soluzione: `venv`

Un **virtual environment** (ambiente virtuale) e una copia isolata dell'interprete Python con i propri pacchetti, separata dal Python di sistema e da altri ambienti. Ogni progetto ha il suo ambiente, con le proprie dipendenze.

```bash
# Creare un ambiente virtuale (una sola volta per progetto)
python -m venv .venv

# Attivare l'ambiente (ogni volta che si lavora al progetto)
# Su macOS/Linux:
source .venv/bin/activate

# Su Windows:
.venv\Scripts\activate
```

Quando l'ambiente e attivo, il prompt del terminale cambia per mostrare il nome dell'ambiente:

```
(.venv) $ python --version
Python 3.12.0
(.venv) $ pip install numpy
```

Tutti i pacchetti installati con `pip` finiscono dentro `.venv/`, non nel Python di sistema.

```bash
# Disattivare l'ambiente
deactivate
```

### `requirements.txt`: congelare le dipendenze

Per garantire che chiunque possa ricreare esattamente lo stesso ambiente, si usa un file `requirements.txt`:

```bash
# Generare il file con le versioni esatte installate
pip freeze > requirements.txt
```

Il file avra un aspetto simile a:

```
numpy==1.26.4
pandas==2.2.0
matplotlib==3.8.2
```

Un collega (o voi stessi su un altro computer) puo ricreare l'ambiente con:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Questo garantisce **riproducibilita**: la stessa analisi produrra gli stessi risultati, perche le versioni dei pacchetti sono identiche.

### Perche `.venv` e non un altro nome?

Il nome `.venv` e una convenzione ampiamente adottata. Il punto iniziale rende la cartella nascosta su macOS e Linux. I file `.gitignore` standard per Python gia includono `.venv/`, evitando di caricare l'ambiente nel repository.

---

## 9. Best practice per gli import

L'ordine e l'organizzazione degli import non sono un dettaglio estetico: sono una questione di leggibilita e manutenibilita. La guida di stile PEP 8 stabilisce regole chiare.

### Posizione: sempre all'inizio del file

Gli import vanno in cima al file, subito dopo l'eventuale docstring del modulo e i commenti iniziali. Non disperdete gli import nel mezzo del codice: rende impossibile capire a colpo d'occhio da cosa dipende il modulo.

### Ordine: tre gruppi separati da una riga vuota

```python
# 1. Libreria standard
import math
import statistics
from collections import Counter
from datetime import date

# 2. Pacchetti di terze parti (installati con pip)
import numpy as np
import pandas as pd

# 3. Moduli propri del progetto
from mio_progetto.utils import pulisci_dati
from mio_progetto.modelli import regressione
```

Questa organizzazione permette di distinguere immediatamente le dipendenze esterne (che devono essere installate) dai moduli propri (che devono esistere nel progetto).

### Un import per riga

```python
# BENE
import math
import statistics
import random

# MALE
import math, statistics, random
```

L'eccezione e `from ... import`, dove e accettabile importare piu nomi dallo stesso modulo:

```python
from datetime import date, datetime, timedelta
```

### Non importare piu del necessario

Importate solo cio che usate. Un import inutilizzato e rumore: confonde chi legge il codice e puo rallentare leggermente l'avvio del programma. Molti editor (VS Code, PyCharm) segnalano automaticamente gli import non utilizzati.

---

## Domande di verifica

1. **Cosa significa che le funzioni in Python sono "oggetti di prima classe"?** Fate un esempio pratico di una conseguenza di questa proprieta.

2. **Qual e la differenza tra `quadrato` e `quadrato(5)`?** Cosa restituiscono rispettivamente?

3. **In quali situazioni e preferibile usare una lambda rispetto a una funzione definita con `def`?** E quando e meglio evitare le lambda?

4. **Spiegate cosa fa il parametro `key` di `sorted()`.** La funzione passata a `key` viene applicata agli elementi della lista risultante?

5. **Qual e la differenza tra `import math` e `from math import sqrt`?** Quali sono i vantaggi e svantaggi di ciascuna forma?

6. **Cosa significa "batteries included" in riferimento a Python?** Fate tre esempi di moduli della libreria standard utili per la statistica.

7. **Perche servono i virtual environment?** Quale problema risolvono che non si potrebbe risolvere semplicemente installando i pacchetti con `pip`?

8. **Cosa contiene un file `requirements.txt` e perche e importante per la riproducibilita?**

---

## Esercizi

### Base

**Esercizio 1 — Ordinare per criteri diversi.**
Data la seguente lista di dizionari:

```python
citta: list[dict[str, object]] = [
    {"nome": "Roma",    "popolazione": 2873000, "regione": "Lazio"},
    {"nome": "Milano",  "popolazione": 1396000, "regione": "Lombardia"},
    {"nome": "Napoli",  "popolazione": 967000,  "regione": "Campania"},
    {"nome": "Torino",  "popolazione": 870000,  "regione": "Piemonte"},
    {"nome": "Palermo", "popolazione": 657000,  "regione": "Sicilia"},
]
```

Usate `sorted()` con `key` per:
- (a) ordinare le citta per popolazione (crescente);
- (b) ordinare le citta per nome (ordine alfabetico);
- (c) trovare la citta piu popolosa con `max()`.

**Esercizio 2 — map e filter.**
Data una lista di temperature in Fahrenheit:

```python
fahrenheit: list[float] = [32.0, 68.0, 95.0, 14.0, 77.0, 104.0, 50.0]
```

- (a) Usate `map()` per convertirle in Celsius (formula: `(F - 32) * 5 / 9`).
- (b) Usate `filter()` per selezionare solo le temperature sopra i 20 gradi Celsius (dal risultato del punto a).
- (c) Riscrivete entrambe le operazioni con una list comprehension.

**Esercizio 3 — Esplorare la libreria standard.**
Scrivete un programma che:
- importa il modulo `random` e genera una lista di 20 interi casuali tra 1 e 100;
- importa il modulo `statistics` e calcola media, mediana e deviazione standard della lista;
- importa `Counter` da `collections` e stampa le frequenze dei valori (usate `seed(42)` per la riproducibilita).

### Intermedio

**Esercizio 4 — Funzione generica di trasformazione.**
Scrivete una funzione `trasforma` che accetta una lista di float e una funzione, e restituisce una nuova lista con la funzione applicata a ogni elemento. Testatela con almeno tre funzioni diverse (una definita con `def`, una lambda e una funzione della libreria standard come `math.sqrt`).

```python
def trasforma(valori: list[float], f: callable) -> list[float]:
    ...
```

**Esercizio 5 — Analisi con moduli standard.**
Scrivete un programma che:
- genera un campione di 1000 numeri casuali con distribuzione normale (usate `random.gauss(mu=170, sigma=10)` per simulare altezze in cm);
- calcola media, mediana, deviazione standard, minimo e massimo;
- conta quanti valori cadono entro una, due e tre deviazioni standard dalla media;
- stampa un report formattato.

Usate `random`, `statistics` e `collections`.

**Esercizio 6 — Moduli propri.**
Create due file:
- `utilita.py` con funzioni `media(valori)`, `mediana(valori)` e `deviazione_standard(valori)` (implementatele voi, senza usare il modulo `statistics`);
- `analisi.py` che importa `utilita` e lo usa per analizzare una lista di dati.

Provate sia `import utilita` sia `from utilita import media, mediana`.

### Avanzato

**Esercizio 7 — Pipeline di trasformazione.**
Scrivete una funzione `pipeline` che accetta un valore iniziale e una lista di funzioni, e applica le funzioni in sequenza, passando il risultato di ciascuna come input della successiva:

```python
def pipeline(valore: float, funzioni: list[callable]) -> float:
    ...

# Esempio di utilizzo
import math

risultato: float = pipeline(
    -16.0,
    [abs, math.sqrt, lambda x: x + 1, lambda x: x ** 2]
)
print(risultato)  # abs(-16) = 16 -> sqrt(16) = 4 -> 4+1 = 5 -> 5**2 = 25
```

**Esercizio 8 — Virtual environment e requirements.**
Esercizio pratico (non di codice):
- Create un nuovo virtual environment per un progetto chiamato "analisi_dati";
- Attivate l'ambiente;
- Installate `numpy`, `pandas` e `matplotlib`;
- Generate il file `requirements.txt`;
- Disattivate l'ambiente;
- Create un secondo ambiente e installate le dipendenze dal `requirements.txt` per verificare che tutto funzioni.

Documentate i comandi utilizzati e l'output ottenuto.

---

## Osservazioni finali

Questa lezione ha introdotto due cambiamenti di prospettiva nel vostro modo di programmare.

Il primo riguarda le **funzioni**: non sono solo blocchi di codice da invocare, ma oggetti che si possono manipolare, passare, combinare. Questa idea e alla base della *programmazione funzionale*, uno stile che si affianca naturalmente alla programmazione imperativa che avete usato finora. Non dovete scegliere l'uno o l'altro: Python vi permette di mescolarli, usando lo stile piu appropriato per ogni situazione. Il pattern `sorted()` con `key` e un esempio perfetto: e funzionale (passate una funzione come argomento), ma si inserisce in un flusso di codice imperativo senza forzature.

Il secondo riguarda l'**organizzazione**: un programma non vive in un unico file e non dipende solo dal codice che scrivete voi. Dipende da moduli della libreria standard, da pacchetti esterni, da specifiche versioni di quei pacchetti. Imparare a gestire queste dipendenze -- con import ordinati, virtual environment e file `requirements.txt` -- non e un dettaglio tecnico: e una competenza fondamentale per il lavoro scientifico riproducibile.

Nelle prossime lezioni userete intensamente questi strumenti. Quando importerete `csv` per leggere un dataset, `statistics` per calcolarne le metriche, o `matplotlib` per visualizzarlo, ogni passaggio si appoggera su cio che avete imparato oggi: come importare moduli, come passare funzioni a `sorted()` per ordinare i dati, come gestire le dipendenze di un progetto.
