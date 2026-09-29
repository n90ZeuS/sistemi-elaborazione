# Lezione 6 — Dal problema al programma

## Introduzione

Nelle lezioni precedenti abbiamo visto come funziona la macchina dal basso verso l'alto: bit e sistemi di numerazione, logica booleana, architettura dell'elaboratore. Oggi passiamo all'altra domanda: **come si descrive alla macchina che cosa deve fare?**

Questa lezione collega la parte sul funzionamento del calcolatore con la parte di programmazione. Parleremo di algoritmi, programmi, processi, pensiero computazionale, linguaggi di programmazione e infine di Python, lo strumento che useremo per il resto del corso. Sistema operativo (T04) e rappresentazione dei dati (T05) verranno trattati più avanti nel corso: oggi ne anticipiamo solo quello che serve.

---

## L'algoritmo

### Definizione

Un **algoritmo** è una sequenza finita e non ambigua di passi che, a partire da un insieme di dati in ingresso, produce un risultato in un tempo finito.

La definizione è semplice, ma ogni parola conta:
- **Sequenza finita:** l'algoritmo deve avere un numero finito di passi. Un procedimento che non termina mai non è un algoritmo.
- **Non ambigua:** ogni passo deve essere definito in modo preciso. Non ci possono essere istruzioni vaghe come "fai la cosa giusta".
- **Dati in ingresso (input):** l'algoritmo riceve dei dati su cui operare.
- **Risultato (output):** l'algoritmo produce un risultato.

### Etimologia e storia

La parola "algoritmo" deriva dal nome latinizzato di **Muhammad ibn Musa al-Khwarizmi** (circa 780-850), matematico, astronomo e geografo persiano che lavorò nella Casa della Saggezza (*Bayt al-Hikma*) a Baghdad. Il suo trattato sull'algebra — *Al-Kitab al-mukhtasar fi hisab al-jabr wal-muqabala* — diede il nome all'algebra stessa (*al-jabr*). Un altro suo trattato, sull'aritmetica con le cifre indiane, fu tradotto in latino con un titolo che iniziava con *Algoritmi* (la forma latina del suo nome): da qui la parola "algoritmo".

Al-Khwarizmi non scrisse algoritmi nel senso informatico moderno, ma descrisse procedure sistematiche e non ambigue per risolvere equazioni, cioè algoritmi nel senso della definizione data sopra.

Il concetto fu formalizzato rigorosamente solo nel XX secolo, quando **Alan Turing** (1936) e **Alonzo Church** definirono matematicamente cosa significa "calcolare". La Macchina di Turing è un modello teorico molto semplice. Secondo la **tesi di Church-Turing**, qualsiasi calcolo che un essere umano può fare seguendo regole fisse può essere eseguito da questa macchina (è una tesi, cioè un'affermazione accettata ma non dimostrabile, perché "seguire regole fisse" non è un concetto matematico). Turing dimostrò anche che **esistono problemi che nessun algoritmo può risolvere** (il *problema della fermata*: è impossibile scrivere un programma che, dato un qualsiasi altro programma, determini se quest'ultimo terminerà o andrà in loop infinito).

### Le proprietà fondamentali

Un algoritmo deve possedere cinque proprietà:

1. **Finitezza:** deve terminare dopo un numero finito di passi.
2. **Determinismo:** ogni passo è definito senza ambiguità; dato lo stesso input, produce sempre lo stesso output.
3. **Input:** riceve zero o più dati in ingresso.
4. **Output:** produce uno o più risultati.
5. **Efficacia (o effettività):** ogni operazione deve essere concretamente eseguibile in un tempo finito.

A queste se ne aggiunge spesso una sesta, meno formale:

6. **Generalità:** un buon algoritmo risolve una *classe* di problemi, non un singolo caso. L'algoritmo per calcolare la media deve funzionare per qualsiasi lista di numeri, non solo per una lista specifica.

### Esempi classici

**L'algoritmo di Euclide** per il massimo comun divisore (MCD) è uno dei più antichi algoritmi conosciuti (~300 a.C.):

```
Dati due numeri a e b (con a > b > 0):
1. Calcola r = resto della divisione di a per b
2. Se r = 0, il MCD è b. FINE.
3. Altrimenti, poni a = b e b = r, e torna al passo 1.
```

Questo algoritmo ha tutte le proprietà: è finito (a ogni passo i numeri diminuiscono), deterministico, riceve input, produce output, ed è generale (funziona per qualsiasi coppia di interi positivi).

---

## Programma e processo

### Il programma

Un **programma** è un algoritmo espresso in un linguaggio che il computer può comprendere (direttamente o tramite traduzione). È un **testo statico**: un file che esiste sul disco anche quando nessuno lo esegue.

L'informatico svizzero **Niklaus Wirth** (1934-2024), creatore del linguaggio Pascal, sintetizzò questo concetto in una formula, titolo del suo libro del 1976:

> **Algoritmi + Strutture Dati = Programmi**

Un programma non è solo una sequenza di istruzioni: è la combinazione di un procedimento risolutivo (l'algoritmo) con un modo di organizzare i dati su cui opera (le strutture dati). La scelta della struttura dati conta quanto la scelta dell'algoritmo.

### Il processo

Un **processo** è un programma in esecuzione. È un'entità **dinamica**: ha uno stato che evolve nel tempo, occupa memoria, usa la CPU, interagisce con il sistema operativo (che studieremo in T04).

Un'analogia:
- Un programma è come una ricetta scritta su un foglio (testo statico).
- Un processo è come la preparazione effettiva del piatto (azione dinamica): servono ingredienti (dati in memoria), strumenti (CPU), tempo, e lo stato cambia continuamente (le patate sono crude, poi bollite, poi schiacciate...).

Lo stesso programma può generare più processi: se aprite due terminali ed eseguite lo stesso script Python, avete un programma e due processi.

### Il percorso completo

Il cammino da un problema alla sua soluzione attraversa quattro stadi:

```
PROBLEMA → ALGORITMO → PROGRAMMA → PROCESSO
 (reale)    (astratto)   (statico)   (dinamico)
```

"Come calcolo la media dei voti?" → Procedimento: somma tutti i voti e dividi per il numero di voti → Codice Python in un file `.py` → Esecuzione del file con l'interprete Python.

---

## Pensiero computazionale

### L'idea

Nel 2006 l'informatica **Jeannette Wing** pubblicò un articolo (*Computational Thinking*, Communications of the ACM) in cui sosteneva che il **pensiero computazionale** (*computational thinking*) è una competenza fondamentale per tutti, non solo per gli informatici, al pari del leggere, scrivere e far di conto.

Pensare computazionalmente significa **usare concetti e strategie dell'informatica per affrontare problemi complessi**, in qualsiasi campo; non significa "pensare come un computer".

### I quattro pilastri

Nella didattica il pensiero computazionale viene spesso descritto con quattro componenti (questa suddivisione è successiva all'articolo di Wing).

**1. Decomposizione:** spezzare un problema complesso in sotto-problemi più piccoli e gestibili.

Anche in statistica si lavora così: un'analisi di dati si scompone in raccolta, pulizia, esplorazione, modellazione e interpretazione. Un programma complesso si scompone in funzioni, ciascuna con un compito specifico.

**2. Riconoscimento di pattern (pattern recognition):** individuare regolarità, somiglianze e strutture ricorrenti.

In statistica si cercano regolarità nei dati. In programmazione, riconoscere pattern significa identificare strutture che si ripetono e astrarre soluzioni riutilizzabili.

**3. Astrazione:** ignorare i dettagli irrilevanti per concentrarsi sull'essenza del problema.

Un modello statistico è un'astrazione: trascura molti dettagli della realtà per descrivere le relazioni principali. In informatica, un'interfaccia è un'astrazione: in Python `open("file.csv")` apre un file senza che dobbiate sapere come i dati sono disposti sul disco (se ne occupa il sistema operativo, T04).

**4. Progettazione algoritmica:** definire una sequenza precisa di passi per arrivare alla soluzione.

### Problem solving strutturato

Il pensiero computazionale si traduce in un metodo di lavoro strutturato:

1. **Comprendere il problema.** Cosa mi viene chiesto? Quali sono gli input? Qual è l'output atteso? Quali sono i vincoli? Conviene non saltare questo passo: se si comincia a scrivere codice senza aver capito bene il problema, spesso poi bisogna riscriverlo.

2. **Pianificare la soluzione.** Scegliere l'approccio, scomporre in passi. Usare pseudocodice o diagrammi di flusso.

3. **Implementare.** Scrivere il codice, un pezzo alla volta.

4. **Verificare.** Testare con casi noti, casi limite, casi patologici.

5. **Rivedere.** Il codice è chiaro? Efficiente? Gestisce anche input inattesi? Si può migliorare?

Questa sequenza ricalca il **metodo scientifico** (osservazione → ipotesi → esperimento → analisi → conclusione): entrambi sono approcci sistematici alla soluzione di problemi.

---

## Strumenti di progettazione

### Pseudocodice

Il **pseudocodice** è una descrizione dell'algoritmo in linguaggio naturale strutturato, a metà strada tra il pensiero e il codice. Non ha una sintassi rigida, ma segue convenzioni che lo rendono non ambiguo:

```
FUNZIONE calcolaMedia(voti)
    SE la lista è vuota
        RESTITUISCI errore "lista vuota"

    somma ← 0
    PER OGNI voto IN voti
        somma ← somma + voto

    media ← somma / lunghezza(voti)
    RESTITUISCI media
```

Il vantaggio dello pseudocodice è che è **indipendente dal linguaggio**: concentra l'attenzione sulla logica, non sulla sintassi. Quando il problema è complesso, conviene scrivere prima lo pseudocodice e poi tradurlo in Python.

### Diagrammi di flusso (flowchart)

I diagrammi di flusso rappresentano l'algoritmo graficamente:

- **Rettangolo:** operazione/istruzione
- **Rombo:** decisione (condizione con rami sì/no)
- **Parallelogramma:** input/output
- **Ovale:** inizio/fine
- **Frecce:** flusso di esecuzione

Sono utili per algoritmi semplici e per comunicare la logica a persone non tecniche. Per algoritmi complessi diventano difficili da leggere, perché le frecce si moltiplicano e si incrociano.

### Top-down vs bottom-up

**Top-down:** si parte dal problema complessivo e si scompone in sotto-problemi, poi ogni sotto-problema in sotto-sotto-problemi, fino ad arrivare a operazioni elementari. È utile in fase di progettazione.

**Bottom-up:** si costruiscono prima i "mattoni" elementari (funzioni di base) e poi si assemblano in strutture più complesse. È utile quando si scrive e si prova il codice.

Nella pratica, si usa un **mix di entrambi**: si pensa top-down (scomponi il problema) e si costruisce bottom-up (scrivi prima le funzioni semplici, poi componi).

### Il debugging come metodo scientifico

Il debugging, cioè la ricerca e correzione degli errori nel codice, si fa con un'indagine sistematica e non per tentativi a caso:

1. **Osserva** il sintomo (cosa va storto? Qual è il messaggio di errore?)
2. **Formula un'ipotesi** (cosa potrebbe causarlo?)
3. **Progetta un esperimento** (come verifico l'ipotesi? Quale print o test devo inserire?)
4. **Verifica** i risultati e correggi
5. Se l'ipotesi era sbagliata, formulane un'altra

È lo stesso schema del metodo scientifico, applicato al codice.

---

## Linguaggi di programmazione

### L'evoluzione: dal codice macchina a Python

**Codice macchina:** sequenze di 0 e 1, l'unica forma che la CPU esegue direttamente. Ogni operazione è codificata come un numero binario (le istruzioni e il ciclo fetch-decode-execute sono stati visti in T03). Scrivere a mano in codice macchina è lento e facile da sbagliare:

```
10110000 01100001  (carica il valore 97 nel registro AL, architettura x86)
```

**Assembly (fine anni '40 – anni '50):** sostituisce i numeri con **mnemonici** leggibili: `MOV AL, 97`. Ogni istruzione assembly corrisponde direttamente a un'istruzione macchina. Resta legato alla specifica architettura: il codice assembly x86 non funziona su ARM.

**Linguaggi ad alto livello (anni '50-'60):** si scrive in una forma più vicina al linguaggio matematico e naturale. Ogni istruzione ad alto livello viene tradotta in molte istruzioni macchina.

Alcune tappe:

- **Fortran** (1957, IBM, John Backus): *FORmula TRANslation*. Il primo linguaggio ad alto livello ad avere larga diffusione, nato per il calcolo scientifico. È ancora usato nei supercomputer per simulazioni meteorologiche, fluidodinamica, fisica nucleare.

- **COBOL** (1959, comitato CODASYL, sulla base del lavoro di Grace Hopper): pensato per le applicazioni gestionali. Grace Hopper, matematica e contrammiraglio della Marina americana, fu una delle prime programmatrici (lavorò sull'Harvard Mark I) e il suo linguaggio FLOW-MATIC fu il modello principale di COBOL. COBOL è ancora usato in molti sistemi bancari e assicurativi.

- **C** (1972, Dennis Ritchie, Bell Labs): nato per scrivere il sistema operativo Unix, riscritto in C nel 1973. Sono scritti in C (o in gran parte in C) anche il kernel Linux, buona parte del kernel di Windows, database come PostgreSQL e SQLite, molti sistemi embedded e l'interprete Python di riferimento (CPython).

- **Python** (1991, Guido van Rossum): ne parliamo più avanti in questa lezione.

### Livelli di astrazione

Ogni livello nasconde la complessità del livello sottostante:

```
Python:       media = sum(voti) / len(voti)
C:            float media = 0; for(int i=0; i<n; i++) media += voti[i]; media /= n;
Assembly:     XOR EAX, EAX; XOR ECX, ECX; somma: ADD EAX, [ESI+ECX*4]; INC ECX; ...
Macchina:     10001011 00000100 10001110 ...
```

Nessun linguaggio è il migliore in tutti i casi; la scelta dipende dal **contesto**: C per i sistemi operativi (serve controllo fine sull'hardware), Python per l'analisi dei dati (serve produttività e leggibilità), JavaScript per il web.

### Paradigmi di programmazione

I linguaggi si distinguono anche per il **paradigma** — il modo in cui strutturano la soluzione:

- **Imperativo:** si descrivono i passi da eseguire, uno dopo l'altro. "Fai questo, poi fai quello." È il più intuitivo. C, Fortran, Python.
- **Procedurale:** imperativo + organizzazione in procedure/funzioni. C, Pascal.
- **Orientato agli oggetti (OOP):** si modella il mondo come oggetti con proprietà e comportamenti. Java, C++, Python.
- **Funzionale:** si descrivono trasformazioni di dati senza effetti collaterali. Haskell, Lisp; elementi funzionali in Python.

**Python è multi-paradigma:** supporta lo stile imperativo, procedurale e a oggetti, più diversi elementi funzionali; si sceglie lo stile più adatto al problema.

---

## Compilazione e interpretazione

### Compilazione

Un **compilatore** traduce l'intero codice sorgente in codice macchina **prima** dell'esecuzione. Il risultato è un file eseguibile autonomo.

```
Sorgente (.c) → [Compilatore] → Eseguibile (.exe) → [CPU] → Risultato
```

**Vantaggi:** il programma compilato è veloce (codice macchina nativo); molti errori (per esempio gli errori di tipo, nei linguaggi con tipi dichiarati come C) vengono scoperti prima dell'esecuzione.
**Svantaggi:** il ciclo edit-compile-run è più lungo; l'eseguibile è specifico per la piattaforma (un .exe di Windows non gira su macOS).

Esempi: C, C++, Rust, Go, Fortran.

### Interpretazione

Un **interprete** traduce ed esegue il codice **istruzione per istruzione**, al momento dell'esecuzione.

```
Sorgente (.py) → [Interprete] → Risultato (passo per passo)
```

**Vantaggi:** interattività (REPL), portabilità (lo stesso codice gira ovunque ci sia l'interprete), ciclo di sviluppo rapido.
**Svantaggi:** più lento in esecuzione; molti errori vengono scoperti solo quando la riga problematica viene raggiunta.

### La realtà è sfumata

Molti linguaggi moderni usano approcci **ibridi**:

- **Java:** il codice viene compilato in *bytecode* (intermedio), che viene eseguito dalla JVM (*Java Virtual Machine*). La JVM a sua volta usa la compilazione **JIT** (*Just-In-Time*): traduce al volo in codice macchina le parti di bytecode più eseguite.

- **Python:** anche Python non è puramente interpretato, come vediamo nella prossima sezione.

---

## L'interprete Python: CPython

### Come funziona

**CPython** è l'implementazione di riferimento di Python, scritta in C. Quando si dice "Python" si intende quasi sempre CPython.

L'esecuzione di un programma Python avviene in tre fasi:

**1. Parsing (analisi sintattica).** Il codice sorgente `.py` viene analizzato e trasformato in un **AST** (*Abstract Syntax Tree*), una rappresentazione ad albero della struttura del programma.

**2. Compilazione in bytecode.** L'AST viene compilato in **bytecode**, un linguaggio intermedio per la Python Virtual Machine. Questa compilazione è automatica. Per i moduli importati il bytecode viene salvato in file `.pyc` nella cartella `__pycache__/`, così la volta successiva non serve ricompilarli; lo script lanciato direttamente viene compilato in memoria, senza creare un `.pyc`.

**3. Esecuzione sulla PVM.** La Python Virtual Machine (PVM) interpreta il bytecode istruzione per istruzione.

Python è quindi un linguaggio **semi-compilato**: compilazione in bytecode (automatica) + interpretazione del bytecode. È un compromesso tra velocità di sviluppo e prestazioni.

### Il GIL (Global Interpreter Lock)

Un processo può contenere più **thread**, cioè più flussi di esecuzione che condividono la stessa memoria (processi e thread si vedono in T04). CPython ha il **GIL**, un blocco globale che impedisce a più thread Python di eseguire bytecode contemporaneamente. Il GIL semplifica la gestione della memoria interna di CPython ma limita il parallelismo. Le soluzioni usuali: `multiprocessing` (processi separati, ognuno con il proprio GIL), programmazione asincrona con `asyncio` (utile quando il programma passa molto tempo in attesa di rete o disco, non per il calcolo) e librerie che rilasciano il GIL (NumPy, quando esegue codice C). Da Python 3.13 esiste anche una versione di CPython senza GIL (*free-threaded*), inizialmente sperimentale.

### Implementazioni alternative

- **PyPy:** implementazione di Python scritta in RPython (un sottoinsieme di Python), con compilazione JIT. Su codice Python puro è spesso diverse volte più veloce di CPython.
- **MicroPython:** Python per microcontrollori (per esempio ESP32 o Raspberry Pi Pico).
- **Cython:** permette di scrivere codice simile a Python che viene tradotto in C e poi compilato. Usato internamente da molte librerie scientifiche.

### Velocità di Python

Per il calcolo puro Python è circa 10-100 volte più lento di C. Nella pratica questo pesa meno di quanto sembri:

1. Spesso conta di più il **tempo per scrivere il programma** che il tempo di esecuzione: la stessa analisi in Python richiede molte meno righe e molto meno tempo che in C.
2. Per la parte computazionalmente intensiva, Python chiama **librerie scritte in C e Fortran** (NumPy, Pandas, SciPy). Il codice Python si limita a chiamarle e a collegare i risultati.
3. Molti programmi passano gran parte del tempo **in attesa** (lettura dal disco, rete, input dell'utente), non a calcolare.

### Modalità di utilizzo

- **REPL (Read-Eval-Print Loop):** l'interprete interattivo. Si scrive un comando, Python lo esegue subito e mostra il risultato. Adatto per esplorare e provare.
- **Script (.py):** il programma scritto in un file, eseguito con `python nome_script.py`. Per codice completo e riutilizzabile.
- **Jupyter Notebook (.ipynb):** celle di codice, testo e visualizzazioni insieme. Nato dal progetto IPython (Fernando Pérez, 2001), evoluto in Jupyter (2014, il nome omaggia **Ju**lia, **Py**thon e **R**). È molto diffuso nella data science.

### Python: chi è e da dove viene

**Guido van Rossum**, programmatore olandese, iniziò a sviluppare Python durante le vacanze di **Natale 1989** ad Amsterdam, come progetto personale. Il nome viene dai **Monty Python**, il gruppo comico britannico, e non dal serpente. La prima versione pubblica è del **1991**.

I principi di progettazione di Python sono riassunti nello **Zen of Python** (provate: `import this` nell'interprete):

> *Beautiful is better than ugly.*
> *Explicit is better than implicit.*
> *Simple is better than complex.*
> *Readability counts.*

Python è: alto livello, multi-paradigma, interpretato (semi-compilato), tipizzato dinamicamente (il tipo è associato ai valori e non alle variabili; li vedremo in T07; esistono anche annotazioni di tipo facoltative, i *type hints*), con *garbage collection* (la memoria non più usata viene liberata automaticamente).

**Perché Python per la statistica:**
- Leggibilità: il codice si legge quasi come l'inglese
- Ecosistema scientifico maturo: NumPy, Pandas, SciPy, scikit-learn, matplotlib
- Comunità molto ampia: per la maggior parte dei problemi comuni si trovano esempi e risposte già pubblicati
- Curva di apprendimento dolce: si può essere produttivi rapidamente
- Versatile: dallo scripting al web development, dal machine learning all'automazione

---

## Domande di verifica

1. **Quali sono le cinque proprietà fondamentali di un algoritmo?** Spiegate ciascuna con un esempio.

2. **Qual è la differenza tra programma e processo?** Fate un'analogia con un concetto della vita quotidiana.

3. **Cosa intende Jeannette Wing per "pensiero computazionale"?** Elencate e spiegate i quattro pilastri con cui viene di solito descritto.

4. **Perché esistono tanti linguaggi di programmazione?** Non basterebbe uno solo?

5. **Qual è la differenza fondamentale tra compilazione e interpretazione?** Quali sono i vantaggi e gli svantaggi di ciascun approccio?

6. **Python è un linguaggio compilato o interpretato?** Descrivete le fasi di esecuzione in CPython.

7. **Cos'è il GIL e perché è rilevante per la programmazione parallela in Python?**

8. **"Programma = algoritmo + strutture dati" (Wirth). Cosa significa questa formula?**

---

## Esercizi

### Base

1. Scrivete in **pseudocodice** un algoritmo che, data una lista di numeri, trova il valore massimo.

2. Disegnate il **diagramma di flusso** per un algoritmo che determina se un numero è pari o dispari.

3. Aprite il REPL di Python e digitate `import this`. Leggete lo Zen of Python e scegliete i tre principi che vi sembrano più importanti. Motivate la scelta.

### Intermedio

4. Scrivete in pseudocodice un algoritmo che, data una lista di voti (numeri interi tra 0 e 30), calcola:
   - La media
   - Il voto massimo
   - Il voto minimo
   - Il numero di sufficienze (voto ≥ 18)

5. Lo stesso algoritmo dell'esercizio 4, tradotto in Python:
   ```python
   voti: list[int] = [28, 22, 18, 30, 15, 25, 27]
   # Completate il programma...
   ```

6. Spiegate, con un esempio concreto, la differenza tra l'approccio top-down e l'approccio bottom-up nella progettazione di un programma che analizza i dati di un questionario.

### Avanzato

7. L'**algoritmo di Euclide** per il MCD, descritto nel testo, termina sempre? Dimostrate informalmente che sì, argomentando sul fatto che il resto della divisione è sempre strettamente minore del divisore.

8. Scrivete in Python l'algoritmo di Euclide e verificatelo su diverse coppie di numeri:
   ```python
   def mcd(a: int, b: int) -> int:
       """Calcola il MCD di a e b con l'algoritmo di Euclide."""
       # Completate...

   # Test
   assert mcd(48, 18) == 6
   assert mcd(100, 75) == 25
   assert mcd(17, 5) == 1
   ```

---

## Osservazioni finali

Questa lezione ha collegato il funzionamento del calcolatore con la programmazione. Abbiamo visto:

- **L'algoritmo** come concetto astratto, indipendente da qualsiasi macchina o linguaggio; procedure di questo tipo esistevano molti secoli prima dei computer.
- **Il programma** come traduzione concreta dell'algoritmo in un linguaggio formale.
- **Il processo** come il programma in esecuzione nella macchina.
- **Il pensiero computazionale** come un modo di ragionare che si applica anche fuori dall'informatica, statistica compresa.
- **I linguaggi di programmazione** come strumenti con filosofie e punti di forza diversi, nati per risolvere problemi diversi.
- **Python** come lo strumento del corso: leggibile, adatto alla statistica, con un'implementazione (CPython) che combina compilazione in bytecode e interpretazione.

Nella prossima lezione (T07, Primi passi in Python) scriveremo il primo programma Python: variabili e tipi di dato. Prima di scrivere codice conviene capire il problema e progettare la soluzione, poi implementarla.

> *"Weeks of coding can save you hours of planning."* — detto ironico diffuso tra i programmatori: saltare la progettazione di solito fa perdere più tempo di quanto ne faccia risparmiare.
