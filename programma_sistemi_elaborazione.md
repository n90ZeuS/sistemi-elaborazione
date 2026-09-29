# Sistemi di Elaborazione

## Programma del corso

**Corso di Laurea:** Scienze Statistiche (Statistica per l'Economia e l'Impresa / Statistiche per le Scienze e le Tecnologie)
**Anno:** Primo
**Docente:** Prof. Nicola Salmaso

---

## PARTE 1 — Architettura degli elaboratori e fondamenti dell'informatica

### 1.1 Fondamenti: informazione, codifica e logica

#### 1.1.1 Che cos'è l'informazione
- Il concetto di informazione come riduzione dell'incertezza
- Il **bit** come unità elementare di informazione: perché proprio due stati? (semplicità, affidabilità, economia dei circuiti elettronici)
- Dal bit al byte: convenzioni e unità di misura (KB, MB, GB, TB — e la distinzione SI vs IEC: perché il vostro disco da 1 TB mostra 931 GB)
- **Riferimento storico:** Claude Shannon e la nascita della teoria dell'informazione (1948) — come un ingegnere delle telecomunicazioni ha formalizzato il concetto di informazione, gettando le basi dell'era digitale

#### 1.1.2 Sistemi di numerazione
- Il sistema posizionale: perché usiamo la base 10 (dieci dita) e perché i computer usano la base 2 (due stati elettrici)
- **Sistema binario:** conversioni da e verso il decimale, aritmetica binaria (somma, sottrazione, complemento a due)
- **Sistema esadecimale:** perché esiste (notazione compatta del binario), dove si incontra nella pratica (colori HTML, indirizzi di memoria, codici di errore)
- **Sistema ottale:** cenni storici e uso residuale
- Esercitazioni pratiche: convertire, calcolare, riconoscere la base giusta nel contesto giusto

#### 1.1.3 Logica booleana e porte logiche
- **George Boole** (1854) e l'idea rivoluzionaria di trattare la logica come algebra — perché un matematico del XIX secolo è il padre dei computer moderni
- Operatori fondamentali: AND, OR, NOT — significato logico e tabelle di verità
- Operatori derivati: NAND, NOR, XOR — perché NAND è "universale" (qualsiasi circuito può essere costruito con sole porte NAND)
- Espressioni booleane e semplificazione: dalla logica proposizionale ai circuiti
- **Claude Shannon** (1937): la tesi di laurea magistrale più influente della storia — dimostrò che l'algebra di Boole descrive perfettamente il comportamento dei circuiti elettrici a relè
- **Applicazione contemporanea:** ogni ricerca su Google, ogni query su un database, ogni `if` nel codice è algebra booleana applicata
- Dai transistor alle porte logiche ai circuiti integrati: come si materializza il pensiero logico nel silicio

#### 1.1.4 La storia del calcolo: dalle origini al computer moderno
- **L'abaco** e i primi strumenti di calcolo meccanico
- **Blaise Pascal** (1642) e la Pascalina: la prima calcolatrice meccanica
- **Gottfried Leibniz** (1694): il calcolo meccanico delle quattro operazioni e, prima ancora, la formalizzazione del sistema binario (1679) — ispirato dalla filosofia cinese dell'I Ching
- **Charles Babbage** e la Macchina Analitica (1837): il primo progetto di computer general-purpose, mai completato — conteneva già CPU, memoria, input/output
- **Ada Lovelace**: il primo algoritmo della storia, scritto per una macchina che non esisteva ancora — e la visione che la macchina potesse manipolare non solo numeri ma qualsiasi simbolo
- **Alan Turing** (1936): la Macchina di Turing e il concetto di calcolabilità — cosa si può e cosa non si può calcolare (il problema della fermata). Il lavoro a Bletchley Park e la decrittazione di Enigma
- **Konrad Zuse** e lo Z3 (1941): il primo computer programmabile funzionante
- **ENIAC** (1945): il primo computer elettronico general-purpose — 30 tonnellate, 18.000 valvole termoioniche, programmato ricablando fisicamente i circuiti
- **La transizione:** valvole → transistor (1947, Bell Labs) → circuiti integrati (1958, Jack Kilby) → microprocessori (1971, Intel 4004) — la legge di Moore e le sue implicazioni
- **Prospettiva futura:** i limiti fisici della miniaturizzazione, il quantum computing come orizzonte

---

### 1.2 Architettura degli elaboratori

#### 1.2.1 Il modello di von Neumann
- **John von Neumann** e il "First Draft of a Report on the EDVAC" (1945): l'idea rivoluzionaria del programma memorizzato — prima di von Neumann, il programma era esterno alla macchina (cavi, schede perforate)
- Le componenti fondamentali:
  - **CPU (Central Processing Unit):** l'unità che esegue le istruzioni
    - ALU (Arithmetic Logic Unit): esegue calcoli e operazioni logiche
    - Unità di controllo: orchestra il flusso di esecuzione
    - Registri: memoria ultra-veloce interna alla CPU
  - **Memoria principale (RAM):** dove risiedono dati e istruzioni durante l'esecuzione — volatile, veloce, limitata
  - **Dispositivi di I/O:** la comunicazione con il mondo esterno (tastiera, schermo, disco, rete)
  - **Bus di sistema:** le "autostrade" che collegano le componenti (bus dati, bus indirizzi, bus di controllo)
- Perché questo modello è ancora attuale dopo 80 anni — e dove mostra i suoi limiti (il "collo di bottiglia di von Neumann": la CPU è più veloce della memoria)

#### 1.2.2 Il ciclo fetch-decode-execute
- Il cuore del funzionamento di ogni computer: un ciclo che si ripete miliardi di volte al secondo
  1. **Fetch:** preleva l'istruzione dalla memoria all'indirizzo indicato dal Program Counter
  2. **Decode:** interpreta l'istruzione, capisce cosa deve fare
  3. **Execute:** esegue l'operazione (calcolo, spostamento dati, salto)
  4. Aggiorna il Program Counter e ricomincia
- Il **clock** e la frequenza: cosa significano i GHz — perché non basta aumentare la frequenza (dissipazione termica, limiti fisici)
- **Cenni sul pipelining:** l'idea geniale di sovrapporre le fasi (come una catena di montaggio) — più istruzioni in esecuzione contemporanea
- Dalla teoria alla pratica: cosa succede realmente quando si esegue `x = 3 + 5` in Python

#### 1.2.3 Gerarchia di memoria
- Il problema fondamentale: la memoria ideale sarebbe velocissima, enorme e a basso costo — ma la fisica impone un compromesso (velocità ↔ capacità ↔ costo)
- La piramide della memoria:
  - **Registri** (~1 ns): pochissimi, interni alla CPU, velocità massima
  - **Cache** (L1, L2, L3 — ~1-30 ns): piccola ma veloce, anticipa i bisogni della CPU (principio di località)
  - **RAM** (~50-100 ns): la memoria di lavoro, volatile
  - **SSD/HDD** (~0.1-10 ms): persistente, capiente, lenta rispetto alla RAM (SSD vs HDD: la rivoluzione della memoria flash)
  - **Cloud storage e archivi**: capacità virtualmente illimitata, latenza di rete
- **Principio di località** (temporale e spaziale): perché la cache funziona — se hai usato un dato, probabilmente lo riuserai presto (temporale) o userai dati vicini (spaziale)
- **Applicazione per la statistica:** perché caricare un dataset intero in RAM è diverso da leggerlo riga per riga dal disco; perché NumPy organizza i dati in memoria contigua

#### 1.2.4 Parallelismo e architetture moderne
- **La fine della corsa ai GHz** (~2005): la frequenza si è fermata, la potenza cresce con i core
- **Multi-core:** più CPU nello stesso chip — il problema non è avere tanti core, ma scrivere software che li sfrutti
- **GPU (Graphics Processing Unit):** nate per la grafica, oggi fondamentali per il calcolo scientifico — migliaia di core semplici per operazioni parallele massicce
  - Perché le GPU dominano il machine learning e il deep learning
  - CUDA (NVIDIA) e il calcolo general-purpose su GPU
- **Cenni su architetture specializzate:** TPU (Google, per il deep learning), chip ARM (efficienza energetica — perché il vostro smartphone è potente ma la batteria dura), Apple Silicon (M1/M2/M3: CPU + GPU + Neural Engine sullo stesso chip)
- **Prospettiva futura:** quantum computing (qubit, sovrapposizione, entanglement — cosa può fare e cosa no), computing neuromorfico, architetture per l'AI

---

### 1.3 Software di sistema

#### 1.3.1 Il sistema operativo: cosa fa e perché esiste
- Il problema: l'hardware è complesso, i programmi sono tanti, le risorse sono limitate — serve un "direttore d'orchestra"
- **Funzioni fondamentali:**
  - Astrazione dell'hardware: il programmatore non deve sapere come funziona ogni singolo disco o scheda di rete
  - Gestione delle risorse: CPU, memoria, dispositivi — chi li usa, quando, per quanto tempo
  - Interfaccia utente: dalla riga di comando alle GUI
  - Sicurezza e protezione: isolamento tra programmi, permessi, utenti
- **Breve storia:**
  - Sistemi batch (anni '50-'60): nessuna interazione, si consegnava il programma su schede perforate e si aspettava il risultato
  - Time-sharing (anni '60-'70): più utenti contemporaneamente — la nascita dell'interattività (Multics → Unix)
  - **Unix** (1969, Ken Thompson e Dennis Ritchie, Bell Labs): filosofia "fare una cosa sola e farla bene", portabilità (scritto in C), ha generato una famiglia intera: Linux, macOS, Android, BSD
  - **L'era dei personal computer:** MS-DOS → Windows; Macintosh → macOS
  - **Linux** (1991, Linus Torvalds): il sistema operativo open-source che fa girare il 96% dei server mondiali, tutti i supercomputer, Android, e la maggior parte dell'infrastruttura cloud
- **Applicazione contemporanea:** ogni volta che aprite Jupyter notebook, il sistema operativo gestisce processi, memoria, accesso ai file e rete — tutto invisibilmente

#### 1.3.2 Gestione dei processi
- **Processo:** un programma in esecuzione con il proprio spazio di memoria, stato e risorse (si ricollega alla sezione ponte)
- Multitasking: come il sistema operativo dà l'illusione che molti programmi girino contemporaneamente su una CPU con pochi core
- **Scheduling:** algoritmi per decidere chi usa la CPU e per quanto tempo (round-robin, priorità)
- Cenni su thread: processi "leggeri" che condividono la memoria — vantaggi e rischi (race condition)
- **Applicazione per la statistica:** perché un calcolo pesante "blocca" l'interfaccia, perché il multiprocessing in Python aggira il GIL

#### 1.3.3 Gestione della memoria
- Memoria virtuale: l'illusione di avere più memoria di quella fisica — ogni processo crede di avere tutta la memoria per sé
- Paginazione: la memoria divisa in blocchi gestibili
- Swap: quando la RAM non basta, il disco fa da estensione (lentissimo)
- **Applicazione pratica:** il famigerato `MemoryError` in Python quando si carica un dataset troppo grande; perché il computer rallenta quando ha troppi programmi aperti

#### 1.3.4 File system
- L'organizzazione logica dei dati: file, directory, percorsi (assoluti e relativi)
- Metadati: nome, dimensione, data di modifica, permessi
- File system diversi per sistemi diversi: NTFS (Windows), ext4 (Linux), APFS (macOS) — perché la chiavetta USB usa FAT32/exFAT (compatibilità universale)
- **Applicazione pratica:** perché `open("dati/file.csv")` funziona diversamente su Windows e Unix (separatore `\` vs `/`); perché Python offre `os.path` e `pathlib` per gestire i percorsi in modo portabile

#### 1.3.5 Reti e internet
- Il problema della comunicazione tra computer: servono regole condivise (protocolli)
- **Il modello a livelli:** perché stratificare la comunicazione (analogia postale: busta dentro busta)
  - Cenni su TCP/IP: il protocollo che fa funzionare internet
  - HTTP/HTTPS: come funziona una richiesta web
  - Client-server: il modello fondamentale (il browser chiede, il server risponde)
- **Internet e il World Wide Web:** non sono la stessa cosa — internet è l'infrastruttura, il web è un servizio sopra di essa (Tim Berners-Lee, 1989, CERN)
- **Cloud computing:** cos'è realmente (i computer di qualcun altro), IaaS/PaaS/SaaS, perché è rilevante (Google Colab, server di calcolo per la statistica)
- **API (Application Programming Interface):** come i programmi parlano tra loro — fondamentale per la raccolta dati automatizzata
- **Applicazione per la statistica:** scaricare dati da API pubbliche (ISTAT, Eurostat, World Bank), eseguire calcoli in cloud, web scraping

---

### 1.4 Rappresentazione dei dati

#### 1.4.1 Numeri interi
- Rappresentazione in binario puro (numeri positivi)
- Il problema dei numeri negativi: modulo e segno, complemento a uno, **complemento a due** (la soluzione elegante usata universalmente) — perché funziona: trasforma la sottrazione in addizione
- **Overflow e underflow:** cosa succede quando un numero è troppo grande per la sua rappresentazione — il bug dell'anno 2038 (time_t a 32 bit su Unix), l'esplosione dell'Ariane 5 (1996, conversione float a int a 16 bit)
- Interi a 32 bit vs 64 bit: range e implicazioni pratiche
- **Python e gli interi:** precisione arbitraria — Python gestisce interi grandi quanto serve, a differenza di C o Java. Perché questa scelta e quale il costo

#### 1.4.2 Numeri in virgola mobile (floating point)
- Il problema: come rappresentare numeri reali con un numero finito di bit?
- **Standard IEEE 754** (1985): segno, esponente, mantissa — la notazione scientifica in binario
  - Single precision (32 bit) vs double precision (64 bit)
  - Valori speciali: +∞, -∞, NaN (Not a Number)
- **L'errore di arrotondamento:** perché `0.1 + 0.2 ≠ 0.3` in Python (e in qualsiasi linguaggio) — non è un bug, è la natura della rappresentazione
  - Implicazioni per la statistica: confrontare float con `==` è pericoloso; il modulo `decimal` per la precisione; `math.isclose()` per i confronti
  - Il disastro del Patriot (1991): un errore di arrotondamento cumulato in 100 ore di funzionamento causò la morte di 28 soldati
- **Applicazione pratica:** quando usare `int` vs `float` in Python, perché `pandas` ha `NaN` e come gestirlo nei dati statistici

#### 1.4.3 Testo e codifiche
- Il problema: come rappresentare lettere e simboli con numeri?
- **ASCII** (1963): 128 caratteri, pensato per l'inglese — 7 bit, sufficiente per lettere, cifre e simboli base
- **Il caos delle estensioni:** ISO 8859-1 (Latin-1) per le lingue europee, Shift-JIS per il giapponese, decine di codifiche incompatibili — i "caratteri strani" che tutti abbiamo visto almeno una volta (mojibake)
- **Unicode** (1991-oggi): l'ambizione di codificare ogni carattere di ogni scrittura umana (e non solo: emoji, simboli matematici, lingue morte)
  - UTF-8: la codifica geniale che è compatibile con ASCII e domina il web (97%+ delle pagine web) — ideata da Ken Thompson e Rob Pike in una sera su una tovaglietta di carta (1992)
  - UTF-16, UTF-32: quando servono e perché
- **Python e le stringhe:** str è Unicode nativamente (dal Python 3) — `encode()` e `decode()`, il temuto `UnicodeDecodeError` quando si leggono file con la codifica sbagliata
- **Applicazione pratica:** aprire un CSV con caratteri accentati (`encoding='utf-8'` o `'latin-1'`), gestire dati multilingue

#### 1.4.4 Immagini, audio e video
- **Immagini:** pixel, risoluzione, profondità di colore
  - Modelli di colore: RGB (schermo), CMYK (stampa), scala di grigi
  - Formati: BMP (non compresso), JPEG (compressione con perdita — perché le foto ripetutamente salvate in JPEG peggiorano), PNG (compressione senza perdita, trasparenza)
  - Un'immagine è una matrice di numeri — il collegamento naturale con NumPy e l'analisi di immagini
- **Audio:** campionamento e quantizzazione — il teorema di Nyquist-Shannon (per catturare un suono, devi campionare al doppio della sua frequenza massima)
  - CD audio: 44.100 Hz, 16 bit — perché proprio questi numeri
- **Video:** sequenza di immagini + audio, il peso enorme e la necessità di compressione (codec H.264, H.265, AV1)
- **Perché tutto questo è rilevante:** i dati statistici moderni non sono solo numeri — immagini mediche, dati audio, video di sorveglianza, satellite imagery

#### 1.4.5 Formati di dati strutturati
- **CSV (Comma-Separated Values):** il formato più semplice e più usato in statistica — limiti (nessun tipo, ambiguità con separatori e virgolette), forza (universalità, leggibilità)
- **JSON (JavaScript Object Notation):** dati strutturati gerarchicamente — il formato delle API web, leggibile e flessibile
- **XML:** verboso ma espressivo — ancora presente in molti contesti istituzionali (dati ISTAT, pubblica amministrazione)
- **Formati binari:** Parquet, HDF5, Feather — perché esistono (velocità, compressione, tipi nativi), quando usarli (dataset grandi)
- **Excel (.xlsx):** onnipresente nel mondo aziendale, problematico per la scienza (il caso dei geni umani rinominati da Excel — MARCH1 diventava una data)
- **Applicazione pratica:** leggere e scrivere ciascun formato con Python e Pandas

---

## SEZIONE PONTE — Dal problema al programma

### P.1 Programma, algoritmo e processo

#### P.1.1 L'algoritmo
- **Definizione:** una sequenza finita e non ambigua di passi che risolve un problema
- **Etimologia e storia:** Muhammad ibn Musa **al-Khwarizmi** (IX secolo, Baghdad) — il matematico il cui nome latinizzato divenne "algoritmo" e il cui libro sull'algebra diede il nome a un'intera branca della matematica
- **Proprietà fondamentali:**
  - **Finitezza:** deve terminare dopo un numero finito di passi
  - **Determinismo:** ogni passo è definito senza ambiguità
  - **Input e output:** riceve dati, produce risultati
  - **Efficacia:** ogni operazione è concretamente eseguibile
  - **Generalità:** risolve una classe di problemi, non un singolo caso
- Esempi classici: algoritmo di Euclide per il MCD, ricerca sequenziale e binaria, ordinamento
- La differenza tra "risolvere un problema" e "avere un algoritmo efficiente per risolverlo"

#### P.1.2 Il programma
- L'algoritmo reso concreto: tradotto in un linguaggio che la macchina può comprendere (direttamente o tramite traduzione)
- **Programma = algoritmo + strutture dati** (Niklaus Wirth, 1976)
- Il programma è un **testo statico**: un file, una sequenza di istruzioni scritte, che esiste anche quando non viene eseguito
- Dal sorgente all'eseguibile: il codice sorgente è leggibile dall'umano, la macchina ha bisogno di una traduzione

#### P.1.3 Il processo
- Il processo è un **programma in esecuzione**: un'entità dinamica con stato, memoria allocata, risorse del sistema
- Lo stesso programma può generare più processi (più istanze di uno stesso software)
- **Il percorso completo:** problema → algoritmo → programma (codice sorgente) → processo (esecuzione)
- Collegamento con la Parte 1: il processo vive nella RAM, usa la CPU, comunica tramite I/O — tutto ciò che abbiamo studiato nell'architettura prende vita qui

---

### P.2 Pensiero computazionale e tecniche di progettazione

#### P.2.1 Il pensiero computazionale
- **Jeannette Wing** (2006): il pensiero computazionale come competenza fondamentale per tutti, non solo per gli informatici — "pensare come un informatico" non significa pensare come un computer, ma usare l'astrazione per affrontare la complessità
- **I quattro pilastri:**
  1. **Decomposizione:** spezzare un problema complesso in sotto-problemi gestibili — come uno statistico scompone un'analisi in raccolta dati, pulizia, esplorazione, modellazione, interpretazione
  2. **Riconoscimento di pattern:** individuare regolarità e similitudini — la base stessa del pensiero statistico
  3. **Astrazione:** ignorare i dettagli irrilevanti, concentrarsi sull'essenza — un modello statistico è un'astrazione della realtà
  4. **Progettazione algoritmica:** definire una sequenza di passi per arrivare alla soluzione

#### P.2.2 Problem solving strutturato
- **Prima capire, poi risolvere:** resistere alla tentazione di scrivere codice immediatamente
- Il metodo:
  1. **Comprendere il problema:** cosa mi viene chiesto? Quali sono gli input? Qual è l'output atteso? Quali sono i vincoli?
  2. **Pianificare la soluzione:** scegliere l'approccio, scomporre in passi
  3. **Implementare:** scrivere il codice
  4. **Verificare:** testare con casi noti, casi limite, casi patologici
  5. **Riflettere:** il codice è chiaro? Si può migliorare?
- **Analogia con il metodo scientifico:** ipotesi → esperimento → analisi → conclusione

#### P.2.3 Strumenti di progettazione
- **Pseudocodice:** descrivere l'algoritmo in linguaggio naturale strutturato — a metà strada tra il pensiero e il codice
  - Convenzioni comuni: INIZIO/FINE, SE/ALLORA/ALTRIMENTI, MENTRE, PER OGNI, RESTITUISCI
  - Vantaggi: indipendente dal linguaggio, concentra l'attenzione sulla logica
- **Diagrammi di flusso (flowchart):** rappresentazione grafica dell'algoritmo
  - Simboli standard: rettangolo (operazione), rombo (decisione), parallelogramma (I/O), ovali (inizio/fine), frecce (flusso)
  - Quando sono utili e quando diventano controproducenti (algoritmi complessi)
- **Raffinamenti successivi (stepwise refinement):** partire da una descrizione ad alto livello e dettagliare progressivamente — tecnica di Niklaus Wirth
- **Esempi pratici:** progettare un algoritmo per calcolare la mediana, per validare un input, per analizzare un file CSV

#### P.2.4 Approcci alla progettazione
- **Top-down:** dal generale al particolare — si parte dal problema complessivo e si scompone
- **Bottom-up:** dal particolare al generale — si costruiscono i mattoni e poi si assemblano
- **Nella pratica:** si usa un mix di entrambi — il pensiero va top-down, la costruzione spesso va bottom-up
- **Il debugging come metodo scientifico:** osserva il sintomo → formula un'ipotesi → progetta un esperimento (test) → verifica → correggi. Il debugging non è "provare a caso", è indagine sistematica

---

### P.3 Linguaggi di programmazione: storia, livelli e paradigmi

#### P.3.1 L'evoluzione dei linguaggi
- **Codice macchina:** sequenze di 0 e 1, l'unica cosa che la CPU capisce — potente ma inumano
- **Assembly** (anni '50): mnemonici al posto dei numeri (`ADD`, `MOV`, `JMP`) — un'astrazione minima, ancora legato alla specifica architettura
  - Ogni famiglia di CPU ha il proprio assembly: x86, ARM, RISC-V
- **Linguaggi ad alto livello** (anni '50-'60): finalmente si scrive in modo vicino al linguaggio umano
  - **Fortran** (1957, IBM, John Backus): il primo linguaggio ad alto livello — "FORmula TRANslation", nato per il calcolo scientifico, ancora usato oggi nei supercomputer e nella meteorologia
  - **COBOL** (1959, Grace Hopper): pensato per il business, ancora in esecuzione nel 95% dei sistemi bancari mondiali
  - **C** (1972, Dennis Ritchie, Bell Labs): il linguaggio che ha scritto il mondo moderno — Unix, Linux, Windows, i database, i linguaggi stessi (Python è scritto in C)
  - **C++** (1979, Bjarne Stroustrup): C con gli oggetti — sistemi operativi, giochi, browser
- **Linguaggi moderni:** Python (1991), Java (1995), JavaScript (1995), R (1993), Rust (2010), Go (2009), Julia (2012) — ognuno nato per risolvere un problema specifico

#### P.3.2 Livelli di astrazione
- L'idea chiave: ogni livello nasconde la complessità del livello sottostante
- **Basso livello:** controllo totale, massima efficienza, massima complessità per il programmatore (Assembly, C)
- **Alto livello:** produttività, leggibilità, portabilità, minor controllo sui dettagli (Python, R, Julia)
- Non esiste "il linguaggio migliore" in assoluto — esiste il linguaggio più adatto al problema e al contesto
- **Analogia:** guidare un'auto con cambio automatico (Python) vs manuale (C) vs costruire il motore (Assembly) — tutte scelte valide in contesti diversi

#### P.3.3 Paradigmi di programmazione
- **Paradigma imperativo:** si descrivono i passi da eseguire, uno dopo l'altro — il più intuitivo, "fai questo, poi fai quello"
- **Paradigma procedurale:** imperativo + organizzazione in procedure/funzioni — C, Pascal
- **Paradigma orientato agli oggetti (OOP):** si modella il mondo come oggetti che hanno proprietà e comportamenti — Java, C++, Python
- **Paradigma funzionale:** si descrivono trasformazioni di dati senza effetti collaterali — Haskell, Lisp; elementi funzionali in Python (map, filter, lambda)
- **Python è multi-paradigma:** supporta tutti questi approcci — la libertà di scegliere lo stile più adatto al problema
- Cenni: dove si colloca R (funzionale + vettoriale), dove Julia (multiple dispatch, pensato per la scienza)

#### P.3.4 Dove si colloca Python
- **Guido van Rossum**, Natale 1989, Amsterdam: un progetto per le vacanze di Natale che diventerà il linguaggio più popolare al mondo
- Il nome: dai Monty Python, non dal serpente
- **Filosofia:** "There should be one — and preferably only one — obvious way to do it" — The Zen of Python (`import this`)
- Alto livello, interpretato, tipizzato dinamicamente (con supporto per type hints), multi-paradigma, garbage collected
- Perché Python per la statistica: leggibilità, ecosistema scientifico (NumPy, Pandas, SciPy, scikit-learn, matplotlib), comunità enorme, curva di apprendimento dolce

---

### P.4 Compilazione, interpretazione e l'interprete Python

#### P.4.1 Compilazione vs interpretazione
- **Compilazione:** traduzione dell'intero programma in codice macchina prima dell'esecuzione
  - Il **compilatore** legge il sorgente, lo traduce, produce un eseguibile autonomo
  - Vantaggi: velocità di esecuzione, ottimizzazione, errori scoperti prima di eseguire
  - Svantaggi: ciclo edit-compile-run più lungo, eseguibile specifico per la piattaforma
  - Esempi: C, C++, Rust, Go, Fortran
- **Interpretazione:** traduzione e esecuzione istruzione per istruzione
  - L'**interprete** legge, traduce ed esegue ogni riga al momento
  - Vantaggi: interattività, portabilità, ciclo di sviluppo rapido
  - Svantaggi: più lento in esecuzione, errori scoperti solo a runtime
  - Esempi: Python, Ruby, JavaScript (storicamente)
- **La realtà è sfumata:** molti linguaggi moderni usano approcci ibridi
  - Java: compilazione in bytecode → esecuzione su JVM (con JIT compilation)
  - JavaScript moderno: motori come V8 compilano al volo (JIT)
  - Python: non è puramente interpretato...

#### P.4.2 L'interprete Python: CPython
- **CPython:** l'implementazione di riferimento di Python, scritta in C — quando si dice "Python" si intende (quasi sempre) CPython
- **Il processo di esecuzione reale:**
  1. **Parsing:** il codice sorgente `.py` viene analizzato sintatticamente (AST — Abstract Syntax Tree)
  2. **Compilazione in bytecode:** l'AST viene tradotto in bytecode (file `.pyc` nella cartella `__pycache__`) — un linguaggio intermedio per la Python Virtual Machine
  3. **Esecuzione sulla PVM (Python Virtual Machine):** la PVM interpreta il bytecode istruzione per istruzione
- Python è quindi un linguaggio **semi-compilato:** compilazione in bytecode (automatica, trasparente) + interpretazione del bytecode
- Il **GIL (Global Interpreter Lock):** il "blocco globale" che impedisce l'esecuzione parallela di thread Python — perché esiste (gestione della memoria), perché è un limite (parallelismo), come si aggira (multiprocessing, async, librerie C)
- **Cenni su implementazioni alternative:**
  - **PyPy:** interprete Python scritto in Python, con compilazione JIT — spesso 5-10x più veloce di CPython
  - **MicroPython:** Python per microcontrollori e sistemi embedded
  - **Cython:** scrivere Python che viene compilato in C — usato internamente da molte librerie scientifiche
- **Perché Python è "lento" e perché (spesso) non importa:** il collo di bottiglia è la produttività del programmatore, non la velocità del programma; per la parte computazionalmente intensiva si usa NumPy/Pandas (scritti in C/Fortran)

#### P.4.3 Modalità di utilizzo di Python
- **Interprete interattivo (REPL — Read-Eval-Print Loop):** si scrive un comando, Python lo esegue subito e mostra il risultato — perfetto per l'esplorazione e il debug
- **Script (file .py):** si scrive il programma in un file e lo si esegue interamente — per programmi completi e riutilizzabili
- **Jupyter Notebook (.ipynb):** celle di codice, testo e visualizzazioni insieme — nato per la scienza, ideale per l'analisi dei dati, la sperimentazione e la comunicazione dei risultati
  - **Storia:** il progetto IPython (Fernando Pérez, 2001) → Jupyter (2014) — il nome è un omaggio a Julia, Python e R
  - Perché è diventato lo standard nella data science
- **Quale usare quando:** REPL per provare velocemente, script per il codice di produzione, notebook per l'analisi esplorativa e la presentazione
- **Ambiente di sviluppo:** VS Code, cenni sul terminale/shell

---

## PARTE 2 — Programmazione in Python

*Nota metodologica: i type hints vengono introdotti fin dalla prima lezione e usati sistematicamente in tutto il corso. Le best practice di scrittura del codice sono integrate in ogni argomento.*

---

### 2.1 Primi passi: il linguaggio e i suoi tipi

#### 2.1.1 Il primo programma
- `print("Hello, World!")` — perché è tradizione (Brian Kernighan, "The C Programming Language", 1978)
- Anatomia di un'istruzione Python: parole chiave, nomi, letterali, operatori, delimitatori
- I commenti: `#` per una riga — scrivere per chi leggerà il codice (incluso il sé del futuro)
- L'importanza dell'**indentazione** in Python: non è estetica, è sintassi — scelta deliberata di Guido van Rossum per forzare la leggibilità

#### 2.1.2 Variabili, assegnamento e nomi
- Cos'è una variabile in Python: un **nome che punta a un oggetto** (non una scatola che contiene un valore — modello mentale importante)
- Assegnamento: `=` non è l'uguaglianza matematica, è un'etichetta che si attacca a un oggetto
- **Regole di naming (PEP 8):**
  - `snake_case` per variabili e funzioni
  - `UPPER_SNAKE_CASE` per costanti
  - Nomi significativi: `media_voti` è meglio di `x`; `reddito_annuale` è meglio di `ra`
  - Evitare: `l`, `O`, `I` (confusione visiva con numeri)
- Assegnamento multiplo e unpacking: `a, b = 1, 2`
- **Best practice:** un nome di variabile è una forma di documentazione — se serve un commento per spiegare cosa contiene, probabilmente il nome è sbagliato

#### 2.1.3 Tipi di dato fondamentali
- Python è **tipizzato dinamicamente:** il tipo è dell'oggetto, non della variabile — una variabile può puntare a oggetti di tipo diverso nel tempo
- **Type hints:** pur non essendo obbligatori, li useremo sempre — rendono il codice più chiaro e meno soggetto a errori
  ```python
  eta: int = 25
  nome: str = "Mario"
  media: float = 27.5
  iscritto: bool = True
  ```
- I tipi fondamentali:
  - `int`: numeri interi a precisione arbitraria
  - `float`: numeri in virgola mobile (IEEE 754, double precision)
  - `str`: stringhe di testo (Unicode)
  - `bool`: `True` o `False` — in realtà sottotipo di `int` (perché? Retrocompatibilità e praticità: `True + True == 2`)
  - `NoneType`: il tipo di `None` — rappresenta l'assenza di valore
- La funzione `type()` per verificare il tipo di un oggetto
- Conversioni di tipo (casting): `int()`, `float()`, `str()`, `bool()` — conversioni esplicite vs implicite (coercion)
- **Tutto in Python è un oggetto:** anche `42` è un oggetto con metodi — `(42).bit_length()` restituisce 6

#### 2.1.4 Operatori e espressioni
- **Operatori aritmetici:** `+`, `-`, `*`, `/` (divisione vera), `//` (divisione intera), `%` (modulo), `**` (potenza)
  - Perché Python ha sia `/` che `//`: in Python 2, `/` tra interi dava un intero — fonte di bug infiniti, corretto in Python 3
- **Operatori di confronto:** `==`, `!=`, `<`, `>`, `<=`, `>=`
  - `==` confronta il valore, `is` confronta l'identità (stesso oggetto in memoria) — una distinzione sottile ma fondamentale
- **Operatori logici:** `and`, `or`, `not` — collegamento diretto con l'algebra booleana della Parte 1
  - Short-circuit evaluation: Python smette di valutare appena conosce il risultato
- **Operatori di appartenenza:** `in`, `not in`
- **Precedenza degli operatori:** la gerarchia, e perché è meglio usare le parentesi per la chiarezza piuttosto che affidarsi alla memorizzazione della precedenza
- Espressioni: combinazioni di valori e operatori che producono un risultato

#### 2.1.5 Input e output
- `print()`: opzioni di formattazione — `sep`, `end`, `file`
- **f-string** (formatted string literal, Python 3.6+): il modo moderno e leggibile di formattare stringhe
  ```python
  nome: str = "Anna"
  media: float = 28.67
  print(f"{nome} ha una media di {media:.2f}")
  ```
- `input()`: leggere dati dall'utente — restituisce **sempre** una stringa (il type casting diventa necessario)
- **Best practice:** validare sempre l'input dell'utente — non fidarsi mai dei dati che vengono dall'esterno

---

### 2.2 Strutture di controllo

#### 2.2.1 Esecuzione condizionale
- Il flusso sequenziale: normalmente Python esegue le istruzioni una dopo l'altra, dall'alto verso il basso
- `if`: esegui questo blocco **solo se** la condizione è vera
  ```python
  def valuta_esame(voto: int) -> str:
      if voto >= 18:
          return "Promosso"
  ```
- `if/else`: due strade, una sola viene percorsa
- `if/elif/else`: decisioni multiple — perché `elif` e non una catena di `if` (efficienza, mutua esclusione)
- **Condizioni composte:** combinare con `and`, `or`, `not`
- **Operatore ternario:** `risultato = "Promosso" if voto >= 18 else "Bocciato"` — quando usarlo (espressioni semplici) e quando evitarlo (logica complessa)
- **Best practice:**
  - Evitare il nesting eccessivo: `if` dentro `if` dentro `if` rende il codice illeggibile
  - Early return: gestire i casi anomali all'inizio e uscire, lasciare il caso principale non indentato
  - Non confrontare con `True`/`False` esplicitamente: `if attivo:` non `if attivo == True:`
  - Attenzione ai valori "truthy" e "falsy": `0`, `""`, `[]`, `None` sono falsy — una caratteristica potente ma anche fonte di bug se non compresa

#### 2.2.2 Cicli: for
- `for` in Python è un **ciclo di iterazione**: scorre gli elementi di una sequenza, uno alla volta
  ```python
  voti: list[int] = [28, 30, 25, 27]
  for voto in voti:
      print(voto)
  ```
- **`range()`**: generare sequenze di numeri — `range(start, stop, step)` — perché `stop` è escluso (convenzione matematica dell'intervallo semiaperto, coerenza con l'indicizzazione da 0)
- `enumerate()`: quando servono sia l'indice che il valore — più elegante e meno error-prone di `range(len(...))`
- `zip()`: iterare su più sequenze in parallelo
- Cicli annidati: quando servono (matrici, combinazioni) e quando è un segnale di allarme (complessità)

#### 2.2.3 Cicli: while
- `while`: ripeti finché la condizione è vera — quando non sai in anticipo quante iterazioni servono
  ```python
  risposta: str = ""
  while risposta != "esci":
      risposta = input("Comando: ")
  ```
- Il pericolo del ciclo infinito: condizioni che non diventano mai false — e come uscirne (`Ctrl+C`, o meglio: progettare correttamente la condizione)
- `break` e `continue`: controllare il flusso dentro il ciclo — `break` esce, `continue` salta all'iterazione successiva
- `while True` + `break`: un pattern comune per cicli con condizione di uscita nel mezzo
- **`for` vs `while`:** usare `for` quando si itera su una collezione o un numero noto di volte, `while` quando la terminazione dipende da una condizione — nel 90% dei casi, `for` è la scelta giusta in Python

#### 2.2.4 Comprehension
- **List comprehension:** creare liste in modo conciso e leggibile
  ```python
  quadrati: list[int] = [x**2 for x in range(10)]
  pari: list[int] = [x for x in range(100) if x % 2 == 0]
  ```
- Perché esistono: esprimono un pattern molto comune (trasforma e/o filtra una sequenza) in modo dichiarativo — si dice cosa si vuole, non come ottenerlo
- **Dict comprehension:** `{k: v for k, v in ...}`
- **Set comprehension:** `{x for x in ...}`
- **Generator expression:** `(x**2 for x in range(10))` — come una list comprehension ma lazy (calcola un elemento alla volta, risparmia memoria)
- **Best practice:**
  - Le comprehension sono ottime per trasformazioni semplici
  - Se la logica diventa complessa (più di una condizione, comprehension annidate), meglio un ciclo esplicito: la leggibilità vince sulla concisione
  - Non usare comprehension per i side effect (non fare `[print(x) for x in lista]`)

---

### 2.3 Strutture dati

#### 2.3.1 Liste
- La struttura dati più versatile e usata in Python: una sequenza **ordinata e mutabile** di elementi
  ```python
  temperature: list[float] = [20.5, 21.3, 19.8, 22.1]
  ```
- **Indicizzazione:** accesso posizionale a partire da 0 (perché da 0? Dijkstra e l'offset dalla base: `a[i]` = elemento all'indirizzo `base + i`)
  - Indici negativi: `-1` è l'ultimo elemento — un'eleganza di Python
- **Slicing:** `lista[start:stop:step]` — potente e conciso, `stop` escluso per coerenza con `range()`
- **Metodi fondamentali:** `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `index()`, `count()`
- Operazioni: `+` (concatenazione), `*` (ripetizione), `in` (appartenenza), `len()` (lunghezza)
- **Riferimenti e copie:** `b = a` **non copia** la lista, crea un alias — entrambi i nomi puntano allo stesso oggetto. Per copiare: `b = a.copy()` o `b = a[:]` o `b = list(a)`. Per strutture annidate: `copy.deepcopy()`
- **Applicazione:** una lista di osservazioni, una serie di misurazioni, i risultati di un esperimento

#### 2.3.2 Tuple
- Sequenza **ordinata e immutabile** — una volta creata, non si può modificare
  ```python
  coordinate: tuple[float, float] = (45.46, 9.19)
  ```
- Perché esistono se ci sono le liste?
  - Immutabilità come garanzia: "questo dato non cambierà"
  - Possono essere chiavi di dizionario (le liste no)
  - Leggermente più efficienti in memoria
- **Named tuple** (cenni): `from collections import namedtuple` — tuple con campi nominati, un passo verso le classi
- **Unpacking:** `lat, lon = coordinate` — funziona anche con le liste, ma è idiomatico con le tuple
- **Applicazione:** coordinate, record di dati a struttura fissa, valori di ritorno multipli dalle funzioni

#### 2.3.3 Dizionari
- Collezione di coppie **chiave-valore**, non ordinata (in realtà ordinata per inserimento dal Python 3.7+), mutabile
  ```python
  studente: dict[str, str | int] = {
      "nome": "Luca",
      "cognome": "Rossi",
      "matricola": 123456
  }
  ```
- **Perché sono fondamentali:** accesso ai dati per nome anziché per posizione — più leggibile, meno errori
- **Hash table sotto il cofano:** la ricerca per chiave è O(1) — costante indipendentemente dalla dimensione (ecco perché le chiavi devono essere immutabili: il loro hash deve rimanere stabile)
- **Metodi fondamentali:** `get()` (con valore di default), `keys()`, `values()`, `items()`, `update()`, `pop()`
- `defaultdict` e `Counter` dal modulo `collections`: strumenti potentissimi per l'analisi dei dati
- **Applicazione:** dataset riga per riga, conteggio frequenze, configurazioni, dati JSON

#### 2.3.4 Set (insiemi)
- Collezione **non ordinata di elementi unici** — direttamente ispirata agli insiemi matematici
  ```python
  valori_unici: set[int] = {1, 2, 3, 4, 5}
  ```
- **Operazioni insiemistiche:** unione (`|`), intersezione (`&`), differenza (`-`), differenza simmetrica (`^`), sottoinsieme (`<=`)
- **Perché sono utili:** rimuovere duplicati, test di appartenenza veloce (O(1) come i dizionari), operazioni su insiemi
- `frozenset`: la versione immutabile — può essere usata come chiave di dizionario
- **Applicazione:** trovare valori unici in un dataset, intersezione tra gruppi di dati, confronto tra insiemi di categorie

#### 2.3.5 Mutabilità vs immutabilità
- **Concetto chiave:** alcuni oggetti possono essere modificati dopo la creazione (mutabili), altri no (immutabili)
  - Mutabili: `list`, `dict`, `set`
  - Immutabili: `int`, `float`, `str`, `tuple`, `frozenset`
- **Perché importa:**
  - I parametri di funzione passano il riferimento: modificare una lista dentro una funzione la modifica anche fuori — effetto collaterale (side effect)
  - Le chiavi di dizionario devono essere immutabili (hashable)
  - L'immutabilità rende il codice più prevedibile e sicuro
- **Scegliere la struttura giusta:**
  - Sequenza ordinata modificabile → `list`
  - Sequenza ordinata fissa → `tuple`
  - Accesso per chiave → `dict`
  - Elementi unici, operazioni insiemistiche → `set`
  - **Regola pratica:** usare la struttura meno potente che risolve il problema — se non serve la mutabilità, usare una tupla

#### 2.3.6 Stringhe come struttura dati
- Le stringhe sono **sequenze immutabili di caratteri** — supportano indicizzazione, slicing, iterazione
- **Metodi fondamentali:** `strip()`, `split()`, `join()`, `replace()`, `find()`, `startswith()`, `endswith()`, `upper()`, `lower()`, `isdigit()`, `isalpha()`
- Ogni metodo restituisce una **nuova stringa** (immutabilità)
- **Pattern comuni nella pulizia dei dati:**
  ```python
  riga: str = "  Roma ; 2850000 ; Lazio  "
  campi: list[str] = [campo.strip() for campo in riga.split(";")]
  ```
- Espressioni regolari (cenni): il modulo `re` per pattern matching avanzato — uno strumento potentissimo per la pulizia e l'estrazione di dati da testo

---

### 2.4 Funzioni e modularità

#### 2.4.1 Perché le funzioni
- Il problema: il codice si ripete, cresce, diventa ingestibile
- **Funzione = sotto-programma con un nome:** si definisce una volta, si usa quante volte serve
- I tre benefici fondamentali:
  1. **Riuso:** scrivi una volta, usa ovunque
  2. **Astrazione:** nascondi la complessità dietro un nome significativo — chi chiama la funzione non deve sapere come funziona dentro
  3. **Decomposizione:** spezzare un problema grande in problemi piccoli e gestibili
- **Riferimento storico:** il concetto di subroutine risale agli anni '50 — prima del suo uso sistematico, i programmi erano monoliti illeggibili

#### 2.4.2 Definire e chiamare funzioni
- Sintassi di definizione con type hints:
  ```python
  def calcola_media(valori: list[float]) -> float:
      """Calcola la media aritmetica di una lista di valori."""
      return sum(valori) / len(valori)
  ```
- **Anatomia:** `def`, nome, parametri tipizzati, `-> tipo_ritorno`, docstring, corpo, `return`
- La differenza tra **parametro** (nella definizione) e **argomento** (nella chiamata)
- `return`: restituisce un valore e termina la funzione — senza `return`, la funzione restituisce `None`
- Return multipli: restituire una tupla — `return media, varianza`
- **Docstring:** la prima stringa nella funzione, è la documentazione — accessibile con `help()` e dagli strumenti di sviluppo. Formato consigliato: una riga di descrizione, poi parametri e ritorno

#### 2.4.3 Parametri e argomenti
- **Parametri posizionali:** l'ordine conta
- **Parametri con valore di default:** `def saluta(nome: str = "mondo") -> str:` — i parametri con default devono venire dopo quelli senza
- **Argomenti keyword:** `calcola(base=10, altezza=5)` — l'ordine non conta, la leggibilità aumenta
- **`*args` e `**kwargs`** (cenni): parametri variabili — utili per funzioni flessibili, presenti in molte librerie
- **Il pericolo del default mutabile:**
  ```python
  # MAI FARE QUESTO:
  def aggiungi(elemento: int, lista: list[int] = []) -> list[int]:
      lista.append(elemento)
      return lista
  # Il default [] è creato UNA SOLA VOLTA e condiviso tra le chiamate!

  # Fare invece:
  def aggiungi(elemento: int, lista: list[int] | None = None) -> list[int]:
      if lista is None:
          lista = []
      lista.append(elemento)
      return lista
  ```

#### 2.4.4 Scope e namespace
- **Scope (ambito di visibilità):** dove un nome è visibile e accessibile
  - **Locale:** dentro la funzione — nasce e muore con la funzione
  - **Globale:** al livello del modulo — visibile ovunque nel file
  - **Built-in:** i nomi predefiniti di Python (`print`, `len`, `range`, ...)
- **Regola LEGB:** Local → Enclosing → Global → Built-in — Python cerca i nomi in quest'ordine
- `global` e `nonlocal`: permettono di modificare variabili di scope esterno — da usare con estrema parsimonia (quasi mai)
- **Best practice:** le funzioni dovrebbero comunicare attraverso parametri e return, non attraverso variabili globali — le variabili globali rendono il codice imprevedibile e difficile da testare

#### 2.4.5 Funzioni come oggetti e lambda
- In Python le funzioni sono **oggetti di prima classe:** possono essere assegnate a variabili, passate come argomenti, restituite da altre funzioni
  ```python
  operazioni: dict[str, callable] = {
      "somma": lambda a, b: a + b,
      "media": lambda a, b: (a + b) / 2
  }
  ```
- **Funzioni lambda:** funzioni anonime per operazioni semplici — `lambda x: x**2`
  - Quando usarle: come argomento di `sorted()`, `map()`, `filter()`
  - Quando non usarle: se la logica è complessa, meglio una funzione con nome
- **`map()`, `filter()`, `reduce()`** — strumenti funzionali, spesso sostituibili con comprehension (che in Python sono generalmente preferite per leggibilità)
- `sorted()` con `key=`: un pattern potentissimo
  ```python
  studenti: list[dict[str, any]] = [...]
  ordinati: list[dict] = sorted(studenti, key=lambda s: s["media"], reverse=True)
  ```

#### 2.4.6 Moduli e import
- **Modulo:** un file `.py` è un modulo — il primo livello di organizzazione del codice
- **`import`:** importare un modulo intero, singole funzioni, con alias
  ```python
  import math
  from math import sqrt, pi
  import numpy as np  # convenzione della comunità
  ```
- **La libreria standard:** "batteries included" — Python viene con centinaia di moduli pronti all'uso (`math`, `statistics`, `random`, `os`, `sys`, `csv`, `json`, `datetime`, `collections`, `itertools`, ...)
- **Pacchetti esterni e `pip`:** il Python Package Index (PyPI) — oltre 500.000 pacchetti. `pip install nome_pacchetto`
- **Virtual environment:** perché sono necessari — ogni progetto può avere le proprie versioni delle librerie senza conflitti
  - `python -m venv nome_ambiente` → `source nome_ambiente/bin/activate`
  - `requirements.txt`: il file che elenca le dipendenze — fondamentale per la riproducibilità scientifica
- **Best practice:** importare sempre all'inizio del file, raggruppare (libreria standard, pacchetti esterni, moduli propri)

---

### 2.5 Gestione di file e dati

#### 2.5.1 Leggere e scrivere file di testo
- **Aprire un file:** `open()` con modalità (`'r'`, `'w'`, `'a'`, `'x'`) e encoding
  ```python
  with open("dati.txt", "r", encoding="utf-8") as file:
      contenuto: str = file.read()
  ```
- **Il context manager `with`:** garantisce che il file venga chiuso anche in caso di errore — la pratica corretta, sempre
- Leggere: `read()`, `readline()`, `readlines()`, iterazione riga per riga
- Scrivere: `write()`, `writelines()`
- **Percorsi dei file:** assoluti vs relativi, il modulo `pathlib` (moderno e cross-platform)
  ```python
  from pathlib import Path
  percorso: Path = Path("dati") / "dataset.csv"
  ```

#### 2.5.2 Lavorare con i CSV
- **Il modulo `csv`:** leggere e scrivere CSV con gestione corretta di virgolette, separatori, escape
  ```python
  import csv

  with open("studenti.csv", "r", encoding="utf-8") as file:
      lettore = csv.DictReader(file)
      for riga in lettore:
          nome: str = riga["nome"]
          voto: int = int(riga["voto"])
  ```
- Dialetti CSV: separatori diversi (`;` nei CSV italiani/europei!), gestione dei caratteri speciali
- **Anticipazione:** Pandas rende tutto questo enormemente più semplice — ma è fondamentale capire cosa succede "sotto"

#### 2.5.3 Lavorare con JSON
- Leggere e scrivere dati strutturati:
  ```python
  import json

  with open("config.json", "r") as file:
      dati: dict = json.load(file)

  with open("output.json", "w") as file:
      json.dump(risultati, file, indent=2)
  ```
- Corrispondenza tipi JSON ↔ Python: object ↔ dict, array ↔ list, string ↔ str, number ↔ int/float, true/false ↔ True/False, null ↔ None
- **Applicazione:** leggere risposte da API web, configurazioni, dati semi-strutturati

#### 2.5.4 Gestione degli errori: eccezioni
- **Il problema:** il programma può fallire in modi prevedibili (file non trovato, divisione per zero, input invalido) — senza gestione, il programma si interrompe
- **Try/except:** catturare e gestire gli errori
  ```python
  def leggi_valore(prompt: str) -> float:
      while True:
          try:
              return float(input(prompt))
          except ValueError:
              print("Inserisci un numero valido.")
  ```
- **Gerarchia delle eccezioni:** `BaseException` → `Exception` → eccezioni specifiche (`ValueError`, `TypeError`, `FileNotFoundError`, `KeyError`, `IndexError`, ...)
- **Best practice:**
  - Catturare eccezioni **specifiche**, mai `except Exception:` generico (nasconde bug)
  - **EAFP vs LBYL:** "È più facile chiedere perdono che permesso" (try/except) vs "Guarda prima di saltare" (if/check) — Python idiomatico preferisce EAFP
  - `else` nel try: codice che si esegue solo se non ci sono errori
  - `finally`: codice che si esegue sempre (pulizia risorse)
- **Sollevare eccezioni:** `raise ValueError("Il voto deve essere tra 0 e 30")` — validare i dati in ingresso alle funzioni

---

### 2.6 Programmazione orientata agli oggetti

#### 2.6.1 Perché gli oggetti
- **Il problema della crescita:** quando un programma diventa grande, le funzioni da sole non bastano — servono modi per raggruppare dati e comportamenti correlati
- **L'idea fondamentale dell'OOP:** un oggetto è un'entità che ha **stato** (attributi/dati) e **comportamento** (metodi/funzioni)
- **Analogia:** uno studente ha un nome, un cognome, una lista di voti (stato) e può iscriversi a un esame, calcolare la media, stampare il libretto (comportamento)
- **Storia:** Simula 67 (Dahl e Nygaard, Norvegia) — il primo linguaggio con classi e oggetti, nato per le simulazioni. Poi Smalltalk (Alan Kay, Xerox PARC, anni '70) — "il miglior modo di predire il futuro è inventarlo"
- **In Python già usiamo oggetti:** `"ciao".upper()` — `"ciao"` è un oggetto stringa, `upper()` è un metodo. `lista.append(42)` — `lista` è un oggetto, `append()` è un metodo. **Tutto in Python è un oggetto.**

#### 2.6.2 Classi e istanze
- **Classe = modello/progetto**, **Istanza = oggetto concreto creato dal modello**
  ```python
  class Studente:
      """Rappresenta uno studente universitario."""

      def __init__(self, nome: str, cognome: str, matricola: int) -> None:
          self.nome: str = nome
          self.cognome: str = cognome
          self.matricola: int = matricola
          self.voti: list[int] = []

      def aggiungi_voto(self, voto: int) -> None:
          """Aggiunge un voto al libretto dello studente."""
          if not 18 <= voto <= 30:
              raise ValueError(f"Voto {voto} non valido (deve essere tra 18 e 30)")
          self.voti.append(voto)

      def media(self) -> float:
          """Calcola la media dei voti."""
          if not self.voti:
              raise ValueError("Nessun voto registrato")
          return sum(self.voti) / len(self.voti)
  ```
- **`__init__`:** il metodo di inizializzazione (non è un costruttore in senso stretto — l'oggetto esiste già quando `__init__` viene chiamato)
- **`self`:** il riferimento all'istanza corrente — ogni metodo lo riceve come primo parametro. È esplicito in Python (a differenza di `this` implicito in Java/C++) — "explicit is better than implicit" (Zen of Python)
- **Attributi di istanza vs attributi di classe:** i primi appartengono al singolo oggetto, i secondi sono condivisi da tutte le istanze

#### 2.6.3 Metodi speciali (dunder methods)
- I metodi con doppio underscore (`__nome__`) permettono di personalizzare il comportamento degli operatori e delle funzioni built-in
- I più importanti:
  - `__str__`: rappresentazione leggibile (`print()`, `str()`)
  - `__repr__`: rappresentazione non ambigua (debugging, REPL)
  - `__len__`: permette `len(oggetto)`
  - `__eq__`: permette `oggetto1 == oggetto2`
  - `__lt__`, `__gt__`, ecc.: permettono il confronto e l'ordinamento
  - `__getitem__`: permette `oggetto[indice]`
- **Perché esistono:** rendono le classi personalizzate naturali da usare — si comportano come i tipi built-in

#### 2.6.4 Ereditarietà
- **L'idea:** creare nuove classi partendo da classi esistenti — la nuova classe "eredita" attributi e metodi della classe base e può aggiungerne di nuovi o modificare quelli esistenti
  ```python
  class StudenteLavoratore(Studente):
      """Studente che lavora, con informazioni sull'impiego."""

      def __init__(self, nome: str, cognome: str, matricola: int,
                   azienda: str) -> None:
          super().__init__(nome, cognome, matricola)
          self.azienda: str = azienda
  ```
- `super()`: richiamare i metodi della classe base
- **Quando usarla:** relazione "è un" (uno StudenteLavoratore È UNO Studente)
- **Quando NON usarla:** relazione "ha un" — in quel caso, usare la composizione (uno Studente HA una lista di voti, non EREDITA da lista)
- **Best practice:** preferire la composizione all'ereditarietà nella maggior parte dei casi — l'ereditarietà crea accoppiamento forte

#### 2.6.5 Cenni avanzati
- **Incapsulamento:** convenzione Python — attributi "privati" con underscore `_attributo` (nessuna protezione forzata, solo convenzione — "siamo tutti adulti consenzienti")
- **Proprietà (`@property`):** accedere a un attributo calcolato come se fosse un attributo semplice
- **Classi e statistica:** modellare dataset, distribuzioni, test statistici come oggetti — è esattamente quello che fanno le librerie che userete (un `DataFrame` di Pandas è un oggetto, un modello di scikit-learn è un oggetto)

---

### 2.7 Librerie per la statistica e i dati

#### 2.7.1 NumPy: il fondamento del calcolo scientifico in Python
- **Cos'è:** la libreria che ha reso Python il linguaggio della scienza — fornisce l'`ndarray`, un array multidimensionale efficiente
- **Storia:** evoluzione da Numeric (1995) e Numarray → NumPy (2005, Travis Oliphant) — ha unificato la comunità scientifica Python
- **Perché esiste:** le liste Python sono lente per il calcolo numerico (ogni elemento è un oggetto separato in memoria). NumPy memorizza dati in blocchi contigui di memoria, come C e Fortran
- **`ndarray`:** creazione, attributi (`shape`, `dtype`, `ndim`, `size`), indicizzazione e slicing
  ```python
  import numpy as np

  dati: np.ndarray = np.array([1.5, 2.3, 3.7, 4.1, 5.0])
  matrice: np.ndarray = np.array([[1, 2, 3], [4, 5, 6]])
  ```
- **Vettorizzazione:** operare sull'intero array senza cicli espliciti — il concetto fondamentale
  ```python
  # Lento (Python puro):
  risultato: list[float] = [x**2 + 2*x + 1 for x in dati_lista]

  # Veloce (NumPy vettorizzato):
  risultato: np.ndarray = dati**2 + 2*dati + 1
  ```
- **Operazioni fondamentali:** aritmetica element-wise, funzioni universali (`np.sum`, `np.mean`, `np.std`, `np.sqrt`, `np.log`), broadcasting
- **Generazione di dati:** `np.zeros`, `np.ones`, `np.arange`, `np.linspace`, `np.random` (generazione di campioni casuali — distribuzione uniforme, normale, ecc.)
- **Algebra lineare** (cenni): `np.dot`, `@` (moltiplicazione matriciale), `np.linalg`
- **Applicazione statistica:** campionamento, simulazioni Monte Carlo, operazioni su vettori di osservazioni

#### 2.7.2 Pandas: l'analisi dei dati
- **Cos'è:** la libreria che ha rivoluzionato l'analisi dei dati in Python — il "foglio di calcolo programmabile"
- **Storia:** creata da Wes McKinney nel 2008 alla AQR Capital Management per l'analisi finanziaria — il nome viene da "Panel Data" (econometria)
- **Le due strutture fondamentali:**
  - **`Series`:** un array monodimensionale con indice (come una colonna di un foglio di calcolo)
  - **`DataFrame`:** una tabella bidimensionale con righe e colonne etichettate (come un intero foglio di calcolo)
  ```python
  import pandas as pd

  df: pd.DataFrame = pd.read_csv("studenti.csv")
  ```
- **Caricare dati:** `read_csv`, `read_excel`, `read_json`, `read_sql`, `read_parquet` — Pandas legge quasi tutto
- **Esplorare i dati:** `head()`, `tail()`, `info()`, `describe()`, `shape`, `dtypes`, `value_counts()`
- **Selezionare e filtrare:**
  ```python
  # Selezione colonne
  nomi: pd.Series = df["nome"]

  # Filtro righe
  promossi: pd.DataFrame = df[df["voto"] >= 18]

  # Selezione per posizione e per etichetta
  df.iloc[0:5]      # per posizione
  df.loc[df["anno"] == 2024]  # per condizione
  ```
- **Pulizia dei dati:** gestione valori mancanti (`isna()`, `dropna()`, `fillna()`), duplicati (`drop_duplicates()`), conversioni di tipo (`astype()`), rinominare colonne
- **Trasformazioni:** `apply()`, `map()`, `groupby()` + aggregazioni (`sum`, `mean`, `count`, `agg`), `merge()` (join tra tabelle), `pivot_table()`
- **Operazioni con le date:** il tipo `datetime`, parsing di date, raggruppamento per periodo
- **Esportare:** `to_csv`, `to_excel`, `to_json`, `to_parquet`
- **Best practice:** metodo chaining per pipeline leggibili
  ```python
  risultato: pd.DataFrame = (
      df
      .dropna(subset=["reddito"])
      .query("eta >= 18")
      .groupby("regione")["reddito"]
      .mean()
      .sort_values(ascending=False)
  )
  ```

#### 2.7.3 Matplotlib e Seaborn: visualizzazione dei dati
- **Matplotlib:** la libreria fondamentale per i grafici in Python
  - **Storia:** John Hunter (2003), ispirata a MATLAB — il nome è un omaggio
  - L'interfaccia `pyplot`: grafici rapidi con sintassi semplice
  ```python
  import matplotlib.pyplot as plt

  plt.figure(figsize=(10, 6))
  plt.hist(df["voto"], bins=13, edgecolor="black")
  plt.xlabel("Voto")
  plt.ylabel("Frequenza")
  plt.title("Distribuzione dei voti")
  plt.show()
  ```
  - Tipi di grafico: `plot` (linee), `scatter` (dispersione), `bar` (barre), `hist` (istogramma), `boxplot`, `pie`
  - Personalizzazione: colori, etichette, legende, griglie, titoli, annotazioni
  - Subplots: più grafici nella stessa figura
- **Seaborn:** grafici statistici belli e informativi con meno codice
  - Costruito sopra Matplotlib, integrato con Pandas
  - Grafici specifici per la statistica: `distplot`, `boxplot`, `violinplot`, `heatmap` (correlazione), `pairplot`, `regplot`
  ```python
  import seaborn as sns

  sns.boxplot(data=df, x="corso", y="voto")
  plt.title("Distribuzione voti per corso")
  plt.show()
  ```
- **La grammatica dei grafici:** cenni sulla filosofia della visualizzazione dei dati (Edward Tufte, il "data-ink ratio" — massimizzare l'informazione, minimizzare il superfluo)
- **Best practice:** ogni grafico deve avere titolo, etichette degli assi e, se necessario, legenda. Un buon grafico racconta una storia senza bisogno di spiegazioni

#### 2.7.4 SciPy e Scikit-learn: cenni
- **SciPy** (`scipy.stats`): test statistici, distribuzioni, intervalli di confidenza
  ```python
  from scipy import stats

  t_stat, p_value = stats.ttest_ind(gruppo_a, gruppo_b)
  ```
  - Distribuzione normale, t di Student, chi-quadrato, test di ipotesi — gli strumenti che userete nei corsi di statistica, implementati e pronti all'uso
- **Scikit-learn** (cenni introduttivi): il machine learning accessibile
  - Il pattern universale: `fit()` → `predict()` / `transform()`
  - Regressione lineare, k-means clustering, alberi di decisione — cenni per mostrare dove porta il percorso
  - **Prospettiva futura:** la data science come sintesi di statistica, informatica e conoscenza del dominio

---

### 2.8 Argomenti avanzati

#### 2.8.1 Algoritmi e complessità computazionale
- **Il problema:** non basta che un algoritmo funzioni — deve funzionare in un tempo ragionevole
- **La notazione O-grande (Big O):** misurare come cresce il tempo di esecuzione al crescere dei dati
  - O(1): tempo costante — accesso a un elemento di un dizionario
  - O(log n): logaritmico — ricerca binaria
  - O(n): lineare — scorrere una lista
  - O(n log n): quasi-lineare — ordinamento efficiente (merge sort, Timsort usato da Python)
  - O(n²): quadratico — cicli annidati, ordinamento a bolle
  - O(2ⁿ): esponenziale — forza bruta su combinazioni
- **Perché conta per la statistica:** la differenza tra elaborare 1.000 e 1.000.000 di osservazioni può essere secondi vs ore/giorni
- **Applicazione pratica:** perché `x in lista` è lento e `x in set` è veloce (O(n) vs O(1)); perché `pandas.merge()` è più veloce di un ciclo annidato
- **Cenni su algoritmi fondamentali:** ricerca (sequenziale, binaria), ordinamento (perché Python usa Timsort — un ibrido inventato da Tim Peters nel 2002 specificamente per Python)

#### 2.8.2 Web scraping e API per la raccolta dati
- **API REST:** come i servizi web espongono i dati — richieste HTTP, formato JSON
  ```python
  import requests

  risposta = requests.get("https://api.example.com/dati")
  dati: dict = risposta.json()
  ```
- **Web scraping** (cenni): estrarre dati da pagine web con `BeautifulSoup` — quando le API non esistono
- **Aspetti etici e legali:** rispettare i termini di servizio, il file `robots.txt`, non sovraccaricare i server, GDPR e dati personali
- **Applicazione:** raccogliere dati da fonti pubbliche (ISTAT, Eurostat, World Bank, OpenData) per analisi statistiche

#### 2.8.3 Basi di dati e SQL da Python
- **Perché le basi di dati:** quando i file non bastano — integrità, concorrenza, efficienza su grandi volumi
- **Il modello relazionale** (cenni): tabelle, righe, colonne, chiavi primarie e esterne — Edgar Codd (1970, IBM)
- **SQL** (cenni base): `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `ORDER BY`, `JOIN`
- **Python e i database:** il modulo `sqlite3` (database locale, senza server), `pandas.read_sql()` per leggere direttamente in DataFrame
  ```python
  import sqlite3
  import pandas as pd

  conn = sqlite3.connect("dati.db")
  df: pd.DataFrame = pd.read_sql("SELECT * FROM studenti WHERE anno = 2024", conn)
  ```
- **Prospettiva:** i data warehouse, i data lake, e perché la statistica moderna richiede competenze di gestione dei dati

#### 2.8.4 Automazione e scripting
- **Python come "colla":** automatizzare operazioni ripetitive — rinominare file, convertire formati, generare report
- **Il modulo `os` e `pathlib`:** interagire con il sistema operativo
- **Elaborazione batch:** applicare la stessa analisi a centinaia di file — un ciclo che vi risparmia ore di lavoro manuale
- **Cenni su scheduling:** eseguire script periodicamente (cron su Linux/macOS, Task Scheduler su Windows)
- **Applicazione:** automatizzare la pulizia settimanale dei dati, generare report periodici, monitorare l'aggiornamento di dataset pubblici

#### 2.8.5 L'intelligenza artificiale e il futuro della programmazione
- **La rivoluzione dei Large Language Models:** cosa sono (cenni), cosa possono fare, cosa non possono fare
- **AI come strumento per il programmatore:** assistenti al codice, generazione di codice, debugging assistito — le opportunità e i limiti
- **Il ruolo dello statistico nell'era dell'AI:** comprendere i dati, progettare esperimenti, interpretare i risultati, identificare bias — competenze che l'AI amplifica ma non sostituisce
- **Pensiero critico:** l'AI può generare codice, ma solo chi capisce i fondamenti può valutarne la correttezza, l'efficienza e l'appropriatezza
- **Prospettiva:** la programmazione non sta scomparendo, sta evolvendo — capire i fondamenti diventa ancora più importante, non meno

---

### 2.9 Scrivere codice professionale

*Questa sezione consolida e approfondisce le best practice introdotte durante tutto il corso.*

#### 2.9.1 Stile e leggibilità
- **PEP 8:** la guida di stile ufficiale di Python — non è un capriccio estetico, è comunicazione
  - Indentazione a 4 spazi (mai tab)
  - Lunghezza massima delle righe (79-120 caratteri)
  - Spazi intorno agli operatori
  - Righe vuote per separare blocchi logici
  - Naming conventions: `snake_case` per funzioni/variabili, `PascalCase` per classi, `UPPER_CASE` per costanti
- **Strumenti automatici:**
  - **Linter (`ruff`, `flake8`):** analizza il codice e segnala violazioni di stile e potenziali errori
  - **Formatter (`black`, `ruff format`):** formatta automaticamente il codice secondo le convenzioni — elimina le discussioni sullo stile
  - **Type checker (`mypy`):** verifica la coerenza dei type hints — trova errori prima dell'esecuzione
- **Il codice si legge molto più di quanto si scrive:** ottimizzare per la leggibilità, non per la brevità

#### 2.9.2 Documentazione e type hints
- **Docstring:** ogni funzione pubblica deve avere una docstring che spiega cosa fa, cosa riceve e cosa restituisce
- **Type hints come documentazione vivente:** dichiarano le intenzioni del programmatore e vengono verificate dagli strumenti
  ```python
  def intervallo_confidenza(
      dati: list[float],
      livello: float = 0.95
  ) -> tuple[float, float]:
      """Calcola l'intervallo di confidenza per la media.

      Args:
          dati: Lista di osservazioni numeriche.
          livello: Livello di confidenza (default: 0.95).

      Returns:
          Tupla (limite_inferiore, limite_superiore).

      Raises:
          ValueError: Se la lista è vuota o il livello non è tra 0 e 1.
      """
  ```
- **Commenti:** spiegano il *perché*, non il *cosa* — il codice stesso deve spiegare il cosa
  ```python
  # MALE: incrementa i di 1
  i += 1

  # BENE: salta l'intestazione del CSV (la prima riga contiene i nomi delle colonne)
  i += 1
  ```

#### 2.9.3 Testing e verifica
- **Perché testare:** "il codice non testato è codice rotto" — ogni funzione dovrebbe avere dei test che ne verificano il comportamento
- **`assert`:** il modo più semplice per verificare le aspettative
  ```python
  assert calcola_media([10, 20, 30]) == 20.0
  assert calcola_media([5]) == 5.0
  ```
- **Cenni su `pytest`:** il framework di testing più usato in Python
  ```python
  def test_media_valori_positivi() -> None:
      assert calcola_media([10, 20, 30]) == 20.0

  def test_media_lista_singola() -> None:
      assert calcola_media([42]) == 42.0

  def test_media_lista_vuota() -> None:
      with pytest.raises(ValueError):
          calcola_media([])
  ```
- **Casi limite (edge cases):** testare sempre con lista vuota, un solo elemento, valori negativi, valori molto grandi — i bug si nascondono ai confini
- **Applicazione per la statistica:** verificare che le funzioni statistiche producano risultati corretti su dati noti

#### 2.9.4 Debugging sistematico
- **Leggere i traceback:** dal basso verso l'alto — l'ultimo frame è dove si è verificato l'errore, i frame superiori mostrano il percorso che ci ha portato
- **Tecniche di debugging:**
  1. **Print strategico:** inserire `print()` nei punti critici per osservare lo stato — semplice ma efficace
  2. **Il debugger di VS Code:** breakpoint, step-by-step, ispezione variabili — lo strumento professionale
  3. **Rubber duck debugging:** spiegare il problema ad alta voce (a un'anatra di gomma, a un collega, a se stessi) — spesso la soluzione emerge mentre si formula il problema
- **Il metodo scientifico applicato al debugging:**
  1. Osserva il sintomo (cosa va storto?)
  2. Formula un'ipotesi (cosa potrebbe causarlo?)
  3. Progetta un esperimento (come verifico?)
  4. Testa e concludi
- **Best practice:** quando trovi un bug, prima scrivi un test che lo riproduce, poi correggi il codice — così il bug non tornerà

#### 2.9.5 Organizzazione del codice e riproducibilità
- **Struttura di un progetto Python:**
  ```
  progetto/
  ├── dati/              # dati grezzi (non modificare)
  ├── risultati/         # output dell'analisi
  ├── src/               # codice sorgente
  │   ├── pulizia.py
  │   ├── analisi.py
  │   └── grafici.py
  ├── test/              # test
  ├── requirements.txt   # dipendenze
  └── README.md          # documentazione del progetto
  ```
- **Riproducibilità scientifica:** un'analisi deve poter essere rieseguita da chiunque, ottenendo gli stessi risultati — virtual environment, seed per generazione casuale (`np.random.seed()`/`np.random.default_rng()`), documentazione dei passi
- **DRY (Don't Repeat Yourself):** se copi-incolli codice, probabilmente dovresti scrivere una funzione
- **KISS (Keep It Simple, Stupid):** la soluzione più semplice che funziona è quasi sempre la migliore
- **Leggibilità conta:** "I programmi devono essere scritti per essere letti dagli esseri umani e solo incidentalmente per essere eseguiti dai computer" — Harold Abelson

---

## Filosofia del corso

> Questo corso non si limita a insegnare la sintassi di un linguaggio di programmazione. L'obiettivo è fornire gli strumenti concettuali per **pensare in modo computazionale**, comprendere come funzionano le macchine che processano i nostri dati, e sviluppare la capacità di tradurre problemi statistici in soluzioni informatiche eleganti, corrette e riproducibili.
>
> Ogni concetto viene presentato nel suo contesto storico — per capire *perché* le cose sono fatte così — e con applicazioni contemporanee e prospettive future — per capire *dove* ci porta questa conoscenza.
>
> La programmazione non è un fine, ma un mezzo: il mezzo più potente che uno statistico ha a disposizione per trasformare i dati in conoscenza.
