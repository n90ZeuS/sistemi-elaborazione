# Sistemi di Elaborazione — Calendario delle lezioni

**Lezioni frontali:** 17 | **Laboratori:** 8 | **Totale:** 25 incontri

---

## Blocco tematico — Fondamenti: la macchina e l'informazione

*Le sezioni qui sotto sono raggruppate per tema, non in ordine cronologico. L'ordine reale di svolgimento è nello schema in fondo alla pagina.*

---

### T01 — Informazione, bit e sistemi di numerazione

**Quando:** mercoledì 30 settembre 2026, 10:30-12:30 — P1 - Ricci Curbastro — nello stesso incontro anche T00, apertura del corso

**Argomenti dal programma:** §1.1.1, §1.1.2

| Tema | Contenuto |
|------|-----------|
| Apertura del corso | Cos'è questo corso, perché un futuro statistico deve capire le macchine e saper programmare |
| Che cos'è l'informazione | Il bit come unità elementare, riduzione dell'incertezza, Claude Shannon e la teoria dell'informazione (1948) |
| Unità di misura | Dal bit al byte, KB/MB/GB/TB, la distinzione SI vs IEC (perché il disco da 1 TB mostra 931 GB) |
| Sistemi di numerazione | Posizionale, base 10 (dieci dita), base 2 (due stati elettrici) — conversioni, aritmetica binaria |
| Esadecimale e ottale | Perché esistono, dove si incontrano (colori HTML, indirizzi di memoria) |

**Esercizi in aula:** conversioni tra basi, somme in binario.

**Filo conduttore:** *Tutto ciò che un computer fa è manipolare bit — ma noi possiamo pensare a livelli più alti.*

---

### T02 — Logica booleana e storia del calcolo

**Quando:** venerdì 2 ottobre 2026, 12:30-14:30 — B - Complesso Piovego

**Argomenti dal programma:** §1.1.3, §1.1.4

| Tema | Contenuto |
|------|-----------|
| Algebra di Boole | George Boole (1854): la logica come algebra. AND, OR, NOT — tabelle di verità |
| Porte logiche | NAND come porta universale. Shannon (1937): la tesi che collega Boole ai circuiti |
| Espressioni booleane | Semplificazione, applicazioni pratiche (ogni `if` è algebra booleana) |
| Storia del calcolo | Abaco → Pascal → Leibniz (binario e I Ching!) → Babbage e Ada Lovelace → Turing e la calcolabilità → Enigma |
| Dall'elettronica al silicio | ENIAC (30 tonnellate) → valvole → transistor (1947) → circuiti integrati (1958) → microprocessori (1971, Intel 4004) → legge di Moore |

**Filo conduttore:** *200 anni di idee per arrivare a un chip grande quanto un'unghia — ogni passo è un'astrazione in più.*

---

### T03 — Architettura degli elaboratori

**Quando:** mercoledì 7 ottobre 2026, 10:30-12:30 — P1 - Ricci Curbastro

**Argomenti dal programma:** §1.2.1, §1.2.2, §1.2.3, §1.2.4

| Tema | Contenuto |
|------|-----------|
| Modello di von Neumann | Il "First Draft" (1945), l'idea del programma memorizzato. CPU (ALU + Unità di controllo + Registri), RAM, I/O, Bus |
| Ciclo fetch-decode-execute | Il cuore della macchina: miliardi di volte al secondo. Clock e GHz. Cenni su pipelining |
| Gerarchia di memoria | La piramide: registri → cache (L1/L2/L3) → RAM → SSD/HDD → cloud. Principio di località (temporale e spaziale) |
| Parallelismo moderno | Fine della corsa ai GHz (~2005). Multi-core, GPU (perché dominano nel ML), cenni su TPU, ARM, Apple Silicon |
| Prospettiva futura | Limiti della miniaturizzazione, quantum computing |

**Dimostrazione live (opzionale):** mostrare il Task Manager / Activity Monitor per vedere CPU, RAM, processi in tempo reale — la teoria prende vita.

**Filo conduttore:** *Il modello di von Neumann ha 80 anni e funziona ancora — ma i suoi limiti guidano l'innovazione.*

---

### T04 — Sistemi operativi e software di sistema

**Quando:** mercoledì 2 dicembre 2026, 10:30-12:30 — P1 - Ricci Curbastro

**Argomenti dal programma:** §1.3

| Tema | Contenuto |
|------|-----------|
| Perché serve un sistema operativo | Il problema: hardware complesso, programmi tanti, risorse limitate — serve un "direttore d'orchestra". Astrazione dell'hardware, gestione risorse, interfaccia utente, sicurezza |
| Storia dei SO | Sistemi batch (anni '50-'60, schede perforate) → time-sharing (anni '60, Multics) → **Unix** (1969, Thompson e Ritchie, Bell Labs: "fare una cosa sola e farla bene") → MS-DOS → Windows → Macintosh → macOS |
| Linux | Linus Torvalds (1991): open-source, 96% dei server mondiali, tutti i supercomputer, Android. Filosofia e impatto |
| Gestione dei processi | Multitasking, scheduling (round-robin, priorità), l'illusione della simultaneità. Cenni su thread e race condition |
| Gestione della memoria | Memoria virtuale: ogni processo crede di avere tutta la memoria. Paginazione, swap. Perché il PC rallenta con troppi programmi |
| File system | Organizzazione logica: file, directory, percorsi assoluti e relativi. Metadati. NTFS, ext4, APFS. Perché la chiavetta USB usa FAT32/exFAT |
| Reti e internet | TCP/IP, HTTP/HTTPS, client-server. Internet vs World Wide Web (Berners-Lee, 1989, CERN). Cloud computing. API: come i programmi parlano tra loro |

**Dimostrazione live (opzionale):** aprire il terminale, mostrare i processi (`ps`, Activity Monitor), navigare il file system, mostrare un percorso assoluto vs relativo.

**Filo conduttore:** *Il sistema operativo è il software più importante che non vedete mai — fa funzionare tutto il resto.*

---

### T05 — Rappresentazione dei dati

**Quando:** venerdì 4 dicembre 2026, 12:30-14:30 — B - Complesso Piovego

**Argomenti dal programma:** §1.4

| Tema | Contenuto |
|------|-----------|
| Numeri interi | Rappresentazione binaria, complemento a due (la sottrazione diventa addizione). Overflow: il bug dell'anno 2038, l'esplosione dell'Ariane 5 (1996). Interi a 32 vs 64 bit |
| Floating point | **IEEE 754** (1985): segno, esponente, mantissa. Perché `0.1 + 0.2 ≠ 0.3` — non è un bug, è la natura della rappresentazione. Il disastro del Patriot (1991). Valori speciali: ∞, NaN |
| Testo e codifiche | **ASCII** (1963, 128 caratteri, solo inglese) → il caos delle estensioni (ISO 8859, Shift-JIS, mojibake) → **Unicode** e **UTF-8** (Thompson e Pike, 1992, su una tovaglietta di carta). Perché UTF-8 ha vinto (compatibilità ASCII, efficienza, universalità) |
| Immagini, audio, video | Pixel e RGB, risoluzione, profondità di colore. JPEG vs PNG (con perdita vs senza). Campionamento audio (Nyquist-Shannon): perché il CD è 44.100 Hz. Compressione video. **Un'immagine è una matrice di numeri** — collegamento diretto con NumPy |
| Formati di dati strutturati | **CSV**: semplice, universale, problematico (separatori, virgolette). **JSON**: gerarchico, formato delle API. **XML**: verboso, istituzionale. **Excel**: onnipresente, pericoloso (geni rinominati come date!). **Parquet/HDF5**: binari, veloci per grandi dataset |

**Dimostrazione live:** aprire un file CSV con encoding sbagliato (mojibake dal vivo); mostrare `0.1 + 0.2` in un terminale Python; aprire un'immagine come matrice di numeri.

**Filo conduttore:** *I dati sono rappresentazioni imperfette della realtà — capire come sono codificati evita errori gravi.*

---

### T06 — Dal problema al programma

**Quando:** venerdì 9 ottobre 2026, 12:30-14:30 — B - Complesso Piovego

**Argomenti dal programma:** §P.1, §P.2, §P.3, §P.4

| Tema | Contenuto |
|------|-----------|
| Algoritmo | Definizione, proprietà (finitezza, determinismo, generalità). Da al-Khwarizmi alla formalizzazione di Turing |
| Programma e processo | Programma = algoritmo codificato (testo statico). Processo = programma in esecuzione (entità dinamica). Il percorso: problema → algoritmo → programma → processo |
| Pensiero computazionale | Wing (2006): decomposizione, pattern, astrazione, progettazione algoritmica. Problem solving strutturato. Analogia col metodo scientifico |
| Strumenti di progettazione | Pseudocodice, diagrammi di flusso, raffinamenti successivi (Wirth). Top-down vs bottom-up. Debugging come metodo scientifico |
| Linguaggi di programmazione | Codice macchina → Assembly → alto livello. Fortran, COBOL, C, Python. Livelli di astrazione. Paradigmi: imperativo, procedurale, OOP, funzionale |
| Compilazione vs interpretazione | Vantaggi e svantaggi. L'approccio ibrido. Java e il JIT |
| L'interprete Python | CPython: sorgente → bytecode (.pyc) → PVM. REPL, script, Jupyter. Perché Python è "lento" e perché spesso non importa. Cenni: PyPy, Cython. GIL |
| Dove si colloca Python | Guido van Rossum, Natale 1989. Alto livello, multi-paradigma, tipizzato dinamicamente con type hints. Lo Zen of Python |

**Dimostrazione live:** mostrare `import this` (Zen of Python). Risolvere un problema semplice: prima in pseudocodice, poi in Python.

**Filo conduttore:** *Questa lezione è il ponte tra capire la macchina e parlarle. Da qui in poi, programmiamo.*

---

## Blocco tematico — Python, strutture dati e librerie

*Le sezioni qui sotto sono raggruppate per tema, non in ordine cronologico. L'ordine reale di svolgimento è nello schema in fondo alla pagina.*

---

### T07 — Primi passi in Python

**Quando:** mercoledì 14 ottobre 2026, 10:30-12:30 — P1 - Ricci Curbastro

**Argomenti dal programma:** §2.1.1, §2.1.2, §2.1.3

| Tema | Contenuto |
|------|-----------|
| Il primo programma | `print("Hello, World!")` — Kernighan (1978). Anatomia di un'istruzione. L'indentazione come sintassi |
| Variabili e assegnamento | Un nome che punta a un oggetto (non una scatola). `=` come etichetta. Assegnamento multiplo e unpacking |
| Naming conventions | PEP 8: `snake_case`, `UPPER_CASE`, nomi significativi. Il nome come documentazione |
| Tipi fondamentali | `int`, `float`, `str`, `bool`, `None`. `type()` e conversioni. Tutto è un oggetto |
| Type hints fin da subito | `eta: int = 25`, `nome: str = "Mario"` — perché li usiamo: chiarezza, rigore, strumenti |

**Live coding:** scrivere piccoli programmi passo per passo, mostrando il REPL e poi un file .py. Mostrare i type hints come pratica naturale.

---

### T08 — Operatori, I/O e strutture condizionali

**Quando:** venerdì 16 ottobre 2026, 12:30-14:30 — B - Complesso Piovego

**Argomenti dal programma:** §2.1.4, §2.1.5, §2.2.1

| Tema | Contenuto |
|------|-----------|
| Operatori | Aritmetici (`/` vs `//`, perché Python 3 ha corretto `/`), confronto (`==` vs `is`), logici (`and`, `or`, `not` — short-circuit), appartenenza (`in`), precedenza |
| Input e output | `print()` con opzioni, f-string (`f"{media:.2f}"`), `input()` restituisce sempre str |
| Condizionali | `if`, `if/else`, `if/elif/else`. Condizioni composte. Operatore ternario |
| Best practice | Early return, evitare nesting, truthy/falsy, non confrontare con `== True` |
| Validazione input | Sempre validare i dati dall'esterno — prima applicazione del pensiero difensivo |

**Live coding:** programma interattivo che chiede un voto e restituisce la valutazione (insufficiente/sufficiente/buono/ottimo), con validazione dell'input.

---

### 🖥️ L01 — Ambiente Python, variabili, tipi e condizionali

**Quando:** giovedì 22 ottobre 2026, 12:30-14:30 e 14:30-16:30 — SC140 (due turni)

**Prerequisiti frontali:** F7, F8

| Attività | Descrizione |
|----------|-------------|
| Setup ambiente | Installazione/verifica Python, VS Code, familiarizzazione con l'interfaccia, terminale, REPL |
| Esercizi su variabili e tipi | Creare variabili tipizzate, conversioni, esplorare `type()`, operatori aritmetici e di confronto |
| Esercizi su I/O | Programmi che leggono input, calcolano e stampano risultati formattati con f-string |
| Esercizi su condizionali | Classificatore di dati (es: dato un reddito, determinare la fascia ISEE), calcolatrice con scelta dell'operazione |
| Sfida | Data una temperatura in Celsius, convertirla in Fahrenheit e classificarla (gelido/freddo/mite/caldo/torrido) con type hints e output formattato |

**Nota metodologica:** tutti gli esercizi usano type hints. Il linter viene introdotto come strumento di feedback immediato.

---

### T09 — Cicli

**Quando:** mercoledì 21 ottobre 2026, 10:30-12:30 — P1 - Ricci Curbastro

**Argomenti dal programma:** §2.2.2, §2.2.3

| Tema | Contenuto |
|------|-----------|
| Il ciclo `for` | Iterazione su sequenze. `range(start, stop, step)` — perché stop è escluso |
| `enumerate()` e `zip()` | Iterare con indice, iterare in parallelo — pattern idiomatici |
| Il ciclo `while` | Quando non sai quante iterazioni servono. Il pericolo del ciclo infinito |
| Controllo del flusso | `break`, `continue`, `while True + break`. `for` vs `while`: nel 90% dei casi, `for` è la scelta giusta |
| Cicli annidati | Quando servono (matrici, combinazioni) e quando sono un segnale di allarme |
| Pattern comuni | Accumulatore, contatore, ricerca, filtro — riconoscere i pattern ricorrenti |

**Live coding:** calcolo di statistiche descrittive (media, varianza) su una lista di valori usando solo cicli — poi confronto con le funzioni built-in.

---

### T10 — Comprehension e stringhe

**Quando:** mercoledì 28 ottobre 2026, 10:30-12:30 — P1 - Ricci Curbastro

**Argomenti dal programma:** §2.2.4, §2.3.6

| Tema | Contenuto |
|------|-----------|
| List comprehension | Sintassi, filtri, quando usarle vs cicli espliciti |
| Dict e set comprehension | `{k: v for ...}`, `{x for ...}` |
| Generator expression | Lazy evaluation, risparmio di memoria — `(x for x in ...)` |
| Best practice | Comprehension semplici sì, annidate o complesse no. Mai per side effect |
| Stringhe come struttura dati | Sequenze immutabili, indicizzazione, slicing |
| Metodi fondamentali | `strip()`, `split()`, `join()`, `replace()`, `find()`, `upper()`, `lower()`, `isdigit()` |
| Pattern di pulizia dati | Split + strip per parsing CSV manuale. Cenni su regex (`re`) |

**Live coding:** da una stringa grezza di dati (es: `"Roma;2850000;Lazio"`) estrarre, pulire e trasformare i campi. List comprehension per filtrare una lista di temperature.

---

### 🖥️ L02 — Cicli, comprehension e stringhe

**Quando:** giovedì 29 ottobre 2026, 12:30-14:30 e 14:30-16:30 — SC140 (due turni)

**Prerequisiti frontali:** F9, T10

| Attività | Descrizione |
|----------|-------------|
| Esercizi sui cicli | Calcolare media, minimo, massimo di una serie di numeri inseriti dall'utente (con `while` per input variabile). Tavola pitagorica con cicli annidati |
| Pattern recognition | Dato un elenco di valori, contare quanti sono sopra/sotto la media (pattern accumulatore + contatore) |
| Comprehension | Riscrivere i cicli precedenti come comprehension dove appropriato. Creare un dizionario frequenze da una lista |
| Manipolazione stringhe | Pulire e normalizzare dati testuali (nomi con spazi, maiuscole/minuscole inconsistenti, separatori variabili) |
| Sfida | Leggere una stringa multi-riga con dati separati da `;`, pulirla, calcolare statistiche descrittive e stampare un report formattato |

---

### T11 — Liste e tuple

**Quando:** mercoledì 4 novembre 2026, 10:30-12:30 — P1 - Ricci Curbastro

**Argomenti dal programma:** §2.3.1, §2.3.2

| Tema | Contenuto |
|------|-----------|
| Liste | Sequenza ordinata e mutabile. Indicizzazione (perché da 0 — Dijkstra), indici negativi, slicing |
| Metodi delle liste | `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `index()`, `count()` |
| Riferimenti e copie | `b = a` non copia! Alias vs copia shallow vs deep copy — disegnare i diagrammi in memoria |
| Tuple | Sequenza ordinata e immutabile. Perché esistono: garanzia, hashabilità, efficienza |
| Unpacking | `lat, lon = coordinate` — idiomatico con tuple, valori di ritorno multipli |
| Named tuple | Cenni: tuple con campi nominati, un passo verso le classi |

**Live coding:** gestione di un elenco di studenti con operazioni CRUD (create, read, update, delete) su lista. Mostrare visivamente il problema alias vs copia.

---

### T12 — Dizionari, set e mutabilità

**Quando:** venerdì 6 novembre 2026, 12:30-14:30 — B - Complesso Piovego

**Argomenti dal programma:** §2.3.3, §2.3.4, §2.3.5

| Tema | Contenuto |
|------|-----------|
| Dizionari | Coppie chiave-valore, accesso O(1). Hash table sotto il cofano. Perché le chiavi devono essere immutabili |
| Metodi dei dizionari | `get()` con default, `keys()`, `values()`, `items()`, `update()`, `pop()` |
| `defaultdict` e `Counter` | Dal modulo `collections`: strumenti potentissimi per conteggi e raggruppamenti |
| Set | Insiemi matematici in Python. Operazioni: `\|`, `&`, `-`, `^`. Test di appartenenza O(1) |
| Mutabilità vs immutabilità | Mutabili: list, dict, set. Immutabili: int, float, str, tuple, frozenset. Perché importa: side effect, chiavi dizionario, prevedibilità |
| Scegliere la struttura giusta | Lista vs tupla vs dizionario vs set: regola del "meno potente che risolve il problema" |
| Cenni sulla complessità | Perché `x in set` è O(1) e `x in list` è O(n) — introduzione informale alla notazione Big O. Perché conta quando i dati crescono |

**Live coding:** analisi di frequenza delle parole in un testo usando `Counter`. Operazioni insiemistiche su due gruppi di studenti (iscritti a due corsi diversi: chi segue entrambi? chi solo uno?).

---

### 🖥️ L03 — Strutture dati

**Quando:** giovedì 12 novembre 2026, 12:30-14:30 e 14:30-16:30 — SC140 (due turni)

**Prerequisiti frontali:** T11, T12

| Attività | Descrizione |
|----------|-------------|
| Liste | Gestire una lista di misurazioni: aggiungere, rimuovere, ordinare, cercare. Capire alias vs copia con esperimenti pratici |
| Tuple | Rappresentare punti geografici, calcolare distanze. Unpacking in cicli for |
| Dizionari | Costruire un registro studenti (matricola → dati). Cercare, aggiungere, modificare, eliminare |
| Set | Date due liste di codici fiscali (iscritti anno corrente e anno precedente), trovare nuovi iscritti, abbandoni, confermati |
| Conteggi | Dato un testo, produrre la distribuzione di frequenza delle parole usando `Counter` |
| Sfida | Dato un dataset (lista di dizionari), calcolare statistiche per gruppo (es: media voti per corso di laurea) usando le strutture dati appropriate |

---

### T13 — Funzioni: fondamenti

**Quando:** mercoledì 11 novembre 2026, 10:30-12:30 — P1 - Ricci Curbastro

**Argomenti dal programma:** §2.4.1, §2.4.2, §2.4.3, §2.4.4

| Tema | Contenuto |
|------|-----------|
| Perché le funzioni | Riuso, astrazione, decomposizione. Storia delle subroutine |
| Definire funzioni | `def`, parametri tipizzati, `-> tipo_ritorno`, docstring, `return`. Return multipli (tuple) |
| Parametri | Posizionali, con default, keyword. `*args` e `**kwargs` (cenni). Il pericolo del default mutabile |
| Scope e namespace | Locale, globale, built-in. Regola LEGB. Perché evitare `global` |
| Docstring | Formato consigliato: descrizione, Args, Returns, Raises. `help()` |
| Best practice | Funzioni brevi e focalizzate. Comunicare via parametri/return, non via globali. Type hints su ogni funzione |

**Live coding:** refactoring — prendere un programma monolitico (calcolo statistiche) e scomporlo in funzioni con type hints e docstring.

---

### T14 — Funzioni avanzate, moduli e ambienti

**Quando:** mercoledì 18 novembre 2026, 10:30-12:30 — P1 - Ricci Curbastro

**Argomenti dal programma:** §2.4.5, §2.4.6

| Tema | Contenuto |
|------|-----------|
| Funzioni come oggetti | Funzioni di prima classe: assegnare a variabili, passare come argomenti |
| Lambda | Funzioni anonime: `lambda x: x**2`. Quando usarle (argomento di `sorted`, `map`, `filter`) e quando no |
| `sorted()` con `key=` | Pattern potentissimo: ordinare per criterio personalizzato |
| `map()`, `filter()` | Strumenti funzionali, confronto con comprehension (in Python le comprehension sono generalmente preferite) |
| Moduli e `import` | Un file .py è un modulo. `import`, `from ... import`, alias. La libreria standard ("batteries included") |
| Pacchetti esterni e `pip` | PyPI (500.000+ pacchetti). `pip install` |
| Virtual environment | Perché servono, come crearli e usarli. `requirements.txt` per la riproducibilità |

**Live coding:** usare `sorted()` con `key=lambda` per ordinare dati complessi. Creare un modulo con funzioni statistiche e importarlo.

---

### 🖥️ L04 — Funzioni e modularità

**Quando:** giovedì 19 novembre 2026, 12:30-14:30 e 14:30-16:30 — SC140 (due turni)

**Prerequisiti frontali:** T13, T14

| Attività | Descrizione |
|----------|-------------|
| Scrivere funzioni | Implementare funzioni statistiche di base (`media`, `varianza`, `mediana`, `moda`) con type hints e docstring |
| Testing con assert | Scrivere `assert` per verificare ogni funzione su casi noti e casi limite (lista vuota, singolo elemento) |
| Refactoring | Prendere un esercizio dei lab precedenti (monolitico) e scomporlo in funzioni ben definite |
| Lambda e sorted | Ordinare una lista di dizionari per diversi criteri (nome, voto, data) |
| Modularità | Creare un file `statistiche.py` con le funzioni implementate, importarlo in un altro file e usarlo |
| Sfida | Creare un mini-toolkit statistico: un modulo con funzioni per media, mediana, moda, deviazione standard, intervallo, con validazione degli input e gestione degli errori |

---

### T15 — File, dati e gestione degli errori

**Quando:** mercoledì 25 novembre 2026, 10:30-12:30 — P1 - Ricci Curbastro

**Argomenti dal programma:** §2.5.1, §2.5.2, §2.5.3, §2.5.4

| Tema | Contenuto |
|------|-----------|
| Aprire file | `open()`, modalità (`r`, `w`, `a`), encoding. Il context manager `with` — sempre |
| Leggere e scrivere | `read()`, `readline()`, iterazione riga per riga, `write()` |
| `pathlib` | Percorsi cross-platform moderni: `Path("dati") / "file.csv"` |
| CSV | Modulo `csv`, `DictReader`, separatori europei (`;`). Anticipazione: Pandas semplificherà tutto |
| JSON | `json.load()`, `json.dump()`. Corrispondenza tipi JSON ↔ Python. Uso con API |
| Eccezioni | `try/except`: catturare errori specifici. Gerarchia delle eccezioni |
| Best practice | EAFP vs LBYL. `else` e `finally`. `raise` per validare input. Mai `except Exception:` generico |

**Live coding:** leggere un CSV reale (con problemi: encoding sbagliato, righe mancanti, valori anomali), gestire ogni errore con try/except, produrre un report pulito.

---

### 🖥️ L05 — File e gestione dati

**Quando:** giovedì 10 dicembre 2026, 12:30-14:30 e 14:30-16:30 — SC140 (due turni)

**Prerequisiti frontali:** T15

| Attività | Descrizione |
|----------|-------------|
| File di testo | Leggere un file di log, estrarre informazioni, scrivere un riepilogo |
| CSV | Leggere un dataset CSV reale (es: dati ISTAT), gestire encoding e separatori, estrarre statistiche |
| JSON | Leggere un file JSON strutturato (es: risposta API simulata), navigare la struttura, estrarre dati |
| Gestione errori | Scrivere un programma robusto che gestisce: file non trovato, formato sbagliato, valori mancanti, tipi invalidi |
| Sfida | Pipeline completa: leggere un CSV sporco → pulire (gestire errori, valori mancanti, conversioni) → calcolare statistiche → scrivere i risultati in un nuovo CSV e in un JSON |

---

### T16 — Programmazione orientata agli oggetti

**Quando:** mercoledì 9 dicembre 2026, 10:30-12:30 — P1 - Ricci Curbastro

**Argomenti dal programma:** §2.6

| Tema | Contenuto |
|------|-----------|
| Perché gli oggetti | Il problema della crescita. Stato + comportamento. "Già usate oggetti: `'ciao'.upper()`" |
| Storia | Simula 67 (Dahl e Nygaard), Smalltalk (Alan Kay). "Il miglior modo di predire il futuro è inventarlo" |
| Classi e istanze | `class`, `__init__`, `self`, attributi, metodi. Type hints negli attributi |
| Esempio completo | La classe `Studente`: attributi tipizzati, metodi con validazione, docstring |
| Metodi speciali | `__str__`, `__repr__`, `__len__`, `__eq__` — le classi si comportano come i tipi built-in |
| Ereditarietà | `super()`, relazione "è un" vs "ha un", preferire la composizione |
| Cenni avanzati | Incapsulamento (convenzione `_`), `@property`. Classi nelle librerie: DataFrame è un oggetto, un modello scikit-learn è un oggetto |

**Live coding:** costruire la classe `Studente` passo per passo, aggiungendo progressivamente attributi, metodi, validazione, `__str__`, e infine `StudenteLavoratore` con ereditarietà.

---

### 🖥️ L06 — Classi e oggetti

**Quando:** giovedì 17 dicembre 2026, 12:30-14:30 e 14:30-16:30 — SC140 (due turni)

**Prerequisiti frontali:** T16

| Attività | Descrizione |
|----------|-------------|
| Prima classe | Implementare la classe `Punto2D` con coordinate, distanza dall'origine, distanza da un altro punto, `__str__` |
| Classe Studente | Implementare `Studente` con libretto voti: aggiungere voti (con validazione), calcolare media, verificare se in corso |
| Metodi speciali | Aggiungere `__repr__`, `__eq__`, `__lt__` (confronto per media) a Studente, usare `sorted()` su una lista di studenti |
| Composizione | Creare `Corso` che contiene una lista di `Studente`: iscrizione, statistiche del corso, studente migliore |
| Sfida | Implementare una classe `Dataset` che incapsula una lista di dizionari e offre metodi: `carica_da_csv()`, `filtra()`, `raggruppa()`, `statistiche()` — un mini-Pandas |

---

### T17 — NumPy, Pandas e visualizzazione

**Quando:** mercoledì 16 dicembre 2026, 10:30-12:30 — P1 - Ricci Curbastro

**Argomenti dal programma:** §2.7.1, §2.7.2, §2.7.3, §2.7.4 (cenni), §2.8 (cenni), §2.9 (consolidamento)

*Questa è la lezione più densa: il ritmo è volutamente rapido perché gli studenti hanno ormai le basi per assorbire concetti nuovi velocemente. Il laboratorio 7 e 8 daranno il tempo di praticare.*

| Tema | Contenuto |
|------|-----------|
| **NumPy** | |
| Perché esiste | Liste Python lente per il calcolo numerico. Memoria contigua vs oggetti sparsi. Da Numeric (1995) a NumPy (2005, Travis Oliphant) |
| `ndarray` | Creazione, `shape`, `dtype`, indicizzazione, slicing. Array 1D e 2D |
| Vettorizzazione | Il concetto fondamentale: operazioni sull'intero array senza cicli. Confronto performance vs lista Python |
| Funzioni | `np.mean`, `np.std`, `np.sum`. Broadcasting. `np.random` per generare campioni da distribuzioni |
| **Pandas** | |
| La rivoluzione | Wes McKinney (2008). Series e DataFrame |
| Caricare e esplorare | `read_csv()`, `head()`, `info()`, `describe()`, `value_counts()` |
| Selezionare e filtrare | Selezione colonne, filtro righe, `iloc` e `loc` |
| Pulizia e trasformazioni | `dropna()`, `fillna()`, `groupby()` + aggregazioni, `merge()`, method chaining |
| **Visualizzazione** | |
| Matplotlib | `pyplot`: `hist`, `scatter`, `bar`, `boxplot`. Etichette, titoli, legende, subplots. John Hunter (2003) |
| Seaborn | Grafici statistici: `boxplot`, `heatmap`, `pairplot`. Integrazione con Pandas |
| Grammatica visiva | Edward Tufte e il data-ink ratio: massimizzare l'informazione, minimizzare il superfluo |
| **Orizzonti** | |
| SciPy e scikit-learn | Cenni: `scipy.stats` (test t, distribuzioni), scikit-learn (pattern fit/predict) |
| API e automazione | Cenni: raccogliere dati da API REST (`requests`), basi di dati e SQL (`sqlite3`, `pandas.read_sql`), automazione con script |
| AI e futuro | LLM come strumenti per il programmatore. Il ruolo dello statistico nell'era dell'AI: pensiero critico, interpretazione, bias |
| **Best practice consolidate** | |
| Strumenti professionali | Linter (`ruff`), formatter (`black`), type checker (`mypy`). Testing (`assert`, cenni `pytest`). Debugging sistematico (traceback, print strategico, debugger VS Code). Struttura di un progetto. Riproducibilità (venv, seed, `requirements.txt`). DRY, KISS |

**Live coding:** caricare un dataset CSV in Pandas, esplorarlo, pulirlo, calcolare statistiche per gruppo, visualizzare con Matplotlib/Seaborn — il percorso completo in 15 minuti.

**Messaggio finale:** *La programmazione è un mezzo, non un fine. Ma è il mezzo più potente che avete per trasformare i dati in conoscenza. I fondamenti che avete acquisito vi permetteranno di imparare qualsiasi strumento futuro.*

---

### 🖥️ L07 — NumPy e Pandas

**Quando:** giovedì 7 gennaio 2027, 12:30-14:30 e 14:30-16:30 — SC140 (due turni)

**Prerequisiti frontali:** T17

| Attività | Descrizione |
|----------|-------------|
| NumPy base | Creare array, operazioni vettorizzate, calcolare statistiche. Confronto tempi: ciclo Python vs NumPy |
| NumPy random | Generare campioni casuali da distribuzioni (uniforme, normale). Simulazione Monte Carlo semplice (es: stima di π) |
| Pandas: esplorare | Caricare un dataset reale (CSV), esplorarlo con `head`, `info`, `describe`, `value_counts` |
| Pandas: pulire | Gestire valori mancanti, duplicati, tipi sbagliati. Rinominare colonne, filtrare righe |
| Pandas: analizzare | `groupby` per calcolare statistiche per categoria. Pivot table. Merge tra due DataFrame |
| Sfida | Analisi completa di un dataset reale: caricamento → esplorazione → pulizia → analisi per gruppi → esportazione risultati |

---

### 🖥️ L08 — Visualizzazione e progetto riepilogativo

**Quando:** giovedì 14 gennaio 2027, 12:30-14:30 e 14:30-16:30 — SC140 (due turni)

**Prerequisiti frontali:** T17

| Attività | Descrizione |
|----------|-------------|
| Matplotlib | Creare istogrammi, scatter plot, grafici a barre da un dataset Pandas. Personalizzare: titoli, etichette, colori, legende |
| Seaborn | Boxplot per confrontare distribuzioni tra gruppi. Heatmap di correlazione. Pair plot per esplorare relazioni |
| Subplots | Comporre più grafici in una figura: dashboard di analisi esplorativa |
| **Mini-progetto riepilogativo** | Analisi completa end-to-end di un dataset reale: |
| | 1. Caricare i dati (CSV) con Pandas |
| | 2. Esplorare e pulire (valori mancanti, tipi, outlier) |
| | 3. Calcolare statistiche descrittive per gruppi |
| | 4. Creare visualizzazioni informative |
| | 5. Scrivere codice con funzioni, type hints, docstring |
| | 6. Interpretare i risultati |

**Nota:** il mini-progetto è un esercizio di sintesi che tocca tutto il percorso: dal pensiero computazionale (scomporre il problema) alle best practice (codice pulito e documentato), dalle strutture dati alle librerie.

---

## Schema riassuntivo

*Ordine reale di svolgimento, dall'orario ufficiale dell'Ateneo.*

| # | Data | Tipo | Contenuto | Aula |
|---|------|------|-----------|------|
| 1 | mer 30/09 | Frontale | **T00** Introduzione al corso + **T01** Informazione, bit e sistemi di numerazione | P1 - Ricci Curbastro |
| 2 | ven 02/10 | Frontale | **T02** Logica booleana e storia del calcolo | B - Complesso Piovego |
| 3 | mer 07/10 | Frontale | **T03** Architettura degli elaboratori | P1 - Ricci Curbastro |
| 4 | ven 09/10 | Frontale | **T06** Dal problema al programma | B - Complesso Piovego |
| 5 | mer 14/10 | Frontale | **T07** Primi passi in Python | P1 - Ricci Curbastro |
| 6 | ven 16/10 | Frontale | **T08** Operatori, I/O e strutture condizionali | B - Complesso Piovego |
| 7 | mer 21/10 | Frontale | **T09** Cicli | P1 - Ricci Curbastro |
| 8 | gio 22/10 | **Lab** | **L01** Ambiente Python, variabili, tipi e condizionali | SC140 |
| 9 | mer 28/10 | Frontale | **T10** Comprehension e stringhe | P1 - Ricci Curbastro |
| 10 | gio 29/10 | **Lab** | **L02** Cicli, comprehension e stringhe | SC140 |
| 11 | mer 04/11 | Frontale | **T11** Liste e tuple | P1 - Ricci Curbastro |
| 12 | ven 06/11 | Frontale | **T12** Dizionari, set e mutabilità | B - Complesso Piovego |
| 13 | mer 11/11 | Frontale | **T13** Funzioni: fondamenti | P1 - Ricci Curbastro |
| 14 | gio 12/11 | **Lab** | **L03** Strutture dati | SC140 |
| 15 | mer 18/11 | Frontale | **T14** Funzioni avanzate, moduli e ambienti | P1 - Ricci Curbastro |
| 16 | gio 19/11 | **Lab** | **L04** Funzioni e modularità | SC140 |
| 17 | mer 25/11 | Frontale | **T15** File, dati e gestione degli errori | P1 - Ricci Curbastro |
| 18 | mer 02/12 | Frontale | **T04** Sistemi operativi e software di sistema | P1 - Ricci Curbastro |
| 19 | ven 04/12 | Frontale | **T05** Rappresentazione dei dati | B - Complesso Piovego |
| 20 | mer 09/12 | Frontale | **T16** Programmazione orientata agli oggetti | P1 - Ricci Curbastro |
| 21 | gio 10/12 | **Lab** | **L05** File e gestione dati | SC140 |
| 22 | mer 16/12 | Frontale | **T17** NumPy, Pandas e visualizzazione | P1 - Ricci Curbastro |
| 23 | gio 17/12 | **Lab** | **L06** Classi e oggetti | SC140 |
| 24 | mer 23/12 | — | *riserva / recupero* | P1 - Ricci Curbastro |
| 25 | gio 07/01 | **Lab** | **L07** NumPy e Pandas | SC140 |
| 26 | mer 13/01 | — | *riserva / recupero* | P1 - Ricci Curbastro |
| 27 | gio 14/01 | **Lab** | **L08** Visualizzazione e progetto riepilogativo | SC140 |
