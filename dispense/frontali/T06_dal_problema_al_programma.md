# Lezione 6 — Dal problema al programma

## Introduzione

Nelle prime cinque lezioni abbiamo costruito una comprensione dal basso verso l'alto: bit, logica, circuiti, architettura, sistema operativo, rappresentazione dei dati. Sapete come funziona la macchina. Oggi facciamo il salto dall'altra parte: **come si dice alla macchina cosa fare?**

Questa lezione è il cuore concettuale del corso. È il ponte tra capire il computer e usarlo per risolvere problemi. Parleremo di algoritmi, programmi, processi, pensiero computazionale, linguaggi di programmazione e infine di Python — lo strumento che useremo per il resto del corso.

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

La parola "algoritmo" ha un'origine affascinante. Deriva dal nome latinizzato di **Muhammad ibn Musa al-Khwarizmi** (circa 780-850), matematico, astronomo e geografo persiano che lavorò nella Casa della Saggezza (*Bayt al-Hikma*) a Baghdad. Il suo trattato sull'algebra — *Al-Kitab al-mukhtasar fi hisab al-jabr wal-muqabala* — diede il nome all'algebra stessa (*al-jabr*) e la traduzione latina del suo nome (*Algoritmi*) diede origine alla parola "algoritmo".

Al-Khwarizmi non scrisse algoritmi nel senso informatico moderno, ma descrisse procedure sistematiche e non ambigue per risolvere equazioni — lo spirito è lo stesso.

Il concetto fu formalizzato rigorosamente solo nel XX secolo, quando **Alan Turing** (1936) e **Alonzo Church** definirono matematicamente cosa significa "calcolare". La Macchina di Turing — un modello teorico estremamente semplice — mostrò che qualsiasi calcolo che un essere umano può fare seguendo regole fisse può essere eseguito da questa macchina. E, sorprendentemente, dimostrò anche che **esistono problemi che nessun algoritmo può risolvere** (il *problema della fermata*: è impossibile scrivere un programma che, dato un qualsiasi altro programma, determini se quest'ultimo terminerà o andrà in loop infinito).

### Le proprietà fondamentali

Un algoritmo deve possedere cinque proprietà:

1. **Finitezza:** deve terminare dopo un numero finito di passi.
2. **Determinismo:** ogni passo è definito senza ambiguità; dato lo stesso input, produce sempre lo stesso output.
3. **Input:** riceve zero o più dati in ingresso.
4. **Output:** produce uno o più risultati.
5. **Efficacia (o effettività):** ogni operazione deve essere concretamente eseguibile in un tempo finito.

A queste se ne aggiunge spesso una sesta, meno formale ma altrettanto importante:

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

Il grande informatico svizzero **Niklaus Wirth** (1934-2024), creatore del linguaggio Pascal, sintetizzò questo concetto in una formula celebre, titolo del suo libro del 1976:

> **Algoritmi + Strutture Dati = Programmi**

Un programma non è solo una sequenza di istruzioni: è la combinazione di un procedimento risolutivo (l'algoritmo) con un modo di organizzare i dati su cui opera (le strutture dati). La scelta della struttura dati giusta è tanto importante quanto la scelta dell'algoritmo giusto.

### Il processo

Un **processo** è un programma in esecuzione. È un'entità **dinamica**: ha uno stato che evolve nel tempo, occupa memoria, usa la CPU, interagisce con il sistema operativo.

La distinzione è fondamentale:
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

Nel 2006, la scienziata informatica **Jeannette Wing** pubblicò un articolo influente in cui sosteneva che il **pensiero computazionale** (*computational thinking*) è una competenza fondamentale per tutti, non solo per gli informatici, al pari del leggere, scrivere e far di conto.

Pensare computazionalmente non significa "pensare come un computer" — i computer non pensano. Significa **usare concetti e strategie dell'informatica per affrontare problemi complessi**, in qualsiasi campo.

### I quattro pilastri

**1. Decomposizione:** spezzare un problema complesso in sotto-problemi più piccoli e gestibili.

Uno statistico lo fa naturalmente: un'analisi di dati si scompone in raccolta, pulizia, esplorazione, modellazione e interpretazione. Un programma complesso si scompone in funzioni, ciascuna con un compito specifico.

**2. Riconoscimento di pattern (pattern recognition):** individuare regolarità, somiglianze e strutture ricorrenti.

Questo è il cuore della statistica! Cercare pattern nei dati è esattamente ciò che fate. In programmazione, riconoscere pattern significa identificare strutture che si ripetono e astrarre soluzioni riutilizzabili.

**3. Astrazione:** ignorare i dettagli irrilevanti per concentrarsi sull'essenza del problema.

Un modello statistico è un'astrazione: ignora la complessità infinita della realtà per catturare le relazioni fondamentali. In informatica, un'interfaccia è un'astrazione: `open("file.csv")` nasconde migliaia di righe di codice di gestione del file system.

**4. Progettazione algoritmica:** definire una sequenza precisa di passi per arrivare alla soluzione.

### Problem solving strutturato

Il pensiero computazionale si traduce in un metodo di lavoro strutturato:

1. **Comprendere il problema.** Cosa mi viene chiesto? Quali sono gli input? Qual è l'output atteso? Quali sono i vincoli? — Non saltate questo passo. La tentazione di iniziare subito a scrivere codice è forte, ma la maggior parte del tempo perso in programmazione è dovuta a una comprensione insufficiente del problema.

2. **Pianificare la soluzione.** Scegliere l'approccio, scomporre in passi. Usare pseudocodice o diagrammi di flusso.

3. **Implementare.** Scrivere il codice, un pezzo alla volta.

4. **Verificare.** Testare con casi noti, casi limite, casi patologici.

5. **Riflettere.** Il codice è chiaro? Efficiente? Robusto? Si può migliorare?

Questa sequenza ricalca il **metodo scientifico** (osservazione → ipotesi → esperimento → analisi → conclusione) — e non è un caso. Entrambi sono approcci sistematici alla soluzione di problemi.

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

Il vantaggio dello pseudocodice è che è **indipendente dal linguaggio**: concentra l'attenzione sulla logica, non sulla sintassi. Quando il problema è complesso, scrivere prima lo pseudocodice e poi tradurlo in Python è una strategia vincente.

### Diagrammi di flusso (flowchart)

I diagrammi di flusso rappresentano l'algoritmo graficamente:

- **Rettangolo:** operazione/istruzione
- **Rombo:** decisione (condizione con rami sì/no)
- **Parallelogramma:** input/output
- **Ovale:** inizio/fine
- **Frecce:** flusso di esecuzione

Sono utili per algoritmi semplici e per comunicare la logica a persone non tecniche. Diventano controproducenti per algoritmi complessi (il diagramma diventa un groviglio di frecce).

### Top-down vs bottom-up

**Top-down:** si parte dal problema complessivo e si scompone in sotto-problemi, poi ogni sotto-problema in sotto-sotto-problemi, fino ad arrivare a operazioni elementari. È l'approccio naturale del pensiero.

**Bottom-up:** si costruiscono prima i "mattoni" elementari (funzioni di base) e poi si assemblano in strutture più complesse. È spesso l'approccio naturale della costruzione.

Nella pratica, si usa un **mix di entrambi**: si pensa top-down (scomponi il problema) e si costruisce bottom-up (scrivi prima le funzioni semplici, poi componi).

### Il debugging come metodo scientifico

Il debugging — la ricerca e correzione degli errori nel codice — non è "provare a caso". È un'indagine sistematica:

1. **Osserva** il sintomo (cosa va storto? Qual è il messaggio di errore?)
2. **Formula un'ipotesi** (cosa potrebbe causarlo?)
3. **Progetta un esperimento** (come verifico l'ipotesi? Quale print o test devo inserire?)
4. **Verifica** i risultati e correggi
5. Se l'ipotesi era sbagliata, formulane un'altra

Questo è il metodo scientifico applicato al codice. Per studenti di statistica, dovrebbe suonare familiare.

---

## Linguaggi di programmazione

### L'evoluzione: dal codice macchina a Python

**Codice macchina:** sequenze di 0 e 1, l'unica cosa che la CPU capisce davvero. Ogni operazione è codificata come un numero binario. Scrivere in codice macchina è come parlare la lingua nativa della macchina — potente ma disumano:

```
10110000 01100001  (carica il valore 97 nel registro AL, architettura x86)
```

**Assembly (anni '50):** sostituisce i numeri con **mnemonici** leggibili: `MOV AL, 97`. Ogni istruzione assembly corrisponde direttamente a un'istruzione macchina. Resta legato alla specifica architettura: il codice assembly x86 non funziona su ARM.

**Linguaggi ad alto livello (anni '50-'60):** finalmente si scrive in un modo più vicino al pensiero umano. Ogni istruzione ad alto livello viene tradotta in molte istruzioni macchina.

La storia dei linguaggi ad alto livello è ricca:

- **Fortran** (1957, IBM, John Backus): *FORmula TRANslation*. Il primo linguaggio ad alto livello, nato per il calcolo scientifico. Ancora usato oggi nei supercomputer per simulazioni meteorologiche, fluidodinamica, fisica nucleare. La sua longevità è straordinaria.

- **COBOL** (1959, Grace Hopper): pensato per il business. Grace Hopper, matematica e ammiraglio della Marina americana, fu una delle prime programmatrici al mondo (lavorò sull'Harvard Mark I). COBOL è ancora in esecuzione nel 95% dei sistemi bancari mondiali — miliardi di transazioni al giorno.

- **C** (1972, Dennis Ritchie, Bell Labs): il linguaggio che ha costruito il mondo moderno. Unix è scritto in C. Linux è scritto in C. Il kernel di Windows è scritto in C. I database (MySQL, PostgreSQL), i linguaggi stessi (Python è scritto in C!), i sistemi embedded — tutto passa per C.

- **Python** (1991, Guido van Rossum): ma di questo parleremo tra poco.

### Livelli di astrazione

Ogni livello nasconde la complessità del livello sottostante:

```
Python:       media = sum(voti) / len(voti)
C:            float media = 0; for(int i=0; i<n; i++) media += voti[i]; media /= n;
Assembly:     MOV ECX, n; XOR EAX, EAX; loop: ADD EAX, [ESI+ECX*4]; ...
Macchina:     10001011 00000100 10001110 ...
```

Non esiste "il linguaggio migliore" in assoluto. Esiste il linguaggio più adatto al **contesto**: C per i sistemi operativi (serve controllo fine sull'hardware), Python per l'analisi dei dati (serve produttività e leggibilità), JavaScript per il web.

### Paradigmi di programmazione

I linguaggi si distinguono anche per il **paradigma** — il modo in cui strutturano la soluzione:

- **Imperativo:** si descrivono i passi da eseguire, uno dopo l'altro. "Fai questo, poi fai quello." Il più intuitivo.
- **Procedurale:** imperativo + organizzazione in procedure/funzioni. C, Pascal.
- **Orientato agli oggetti (OOP):** si modella il mondo come oggetti con proprietà e comportamenti. Java, C++, Python.
- **Funzionale:** si descrivono trasformazioni di dati senza effetti collaterali. Haskell, Lisp; elementi funzionali in Python.

**Python è multi-paradigma:** supporta tutti questi approcci, lasciando al programmatore la libertà di scegliere lo stile più adatto al problema.

---

## Compilazione e interpretazione

### Compilazione

Un **compilatore** traduce l'intero codice sorgente in codice macchina **prima** dell'esecuzione. Il risultato è un file eseguibile autonomo.

```
Sorgente (.c) → [Compilatore] → Eseguibile (.exe) → [CPU] → Risultato
```

**Vantaggi:** il programma compilato è veloce (codice macchina nativo), gli errori di tipo vengono scoperti prima dell'esecuzione.
**Svantaggi:** il ciclo edit-compile-run è più lungo; l'eseguibile è specifico per la piattaforma (un .exe di Windows non gira su macOS).

Esempi: C, C++, Rust, Go, Fortran.

### Interpretazione

Un **interprete** traduce e esegue il codice **istruzione per istruzione**, al momento dell'esecuzione.

```
Sorgente (.py) → [Interprete] → Risultato (passo per passo)
```

**Vantaggi:** interattività (REPL), portabilità (lo stesso codice gira ovunque ci sia l'interprete), ciclo di sviluppo rapidissimo.
**Svantaggi:** più lento in esecuzione, gli errori vengono scoperti solo quando la riga problematica viene raggiunta.

### La realtà è sfumata

Molti linguaggi moderni usano approcci **ibridi**:

- **Java:** il codice viene compilato in *bytecode* (intermedio), che viene eseguito dalla JVM (*Java Virtual Machine*). La JVM a sua volta usa la compilazione **JIT** (*Just-In-Time*): traduce al volo in codice macchina le parti di bytecode più eseguite.

- **Python:** non è puramente interpretato...

---

## L'interprete Python: CPython

### Come funziona realmente

**CPython** è l'implementazione di riferimento di Python, scritta in C. Quando si dice "Python" si intende quasi sempre CPython.

L'esecuzione di un programma Python avviene in tre fasi:

**1. Parsing (analisi sintattica).** Il codice sorgente `.py` viene analizzato e trasformato in un **AST** (*Abstract Syntax Tree*), una rappresentazione ad albero della struttura del programma.

**2. Compilazione in bytecode.** L'AST viene compilato in **bytecode**, un linguaggio intermedio per la Python Virtual Machine. Il bytecode viene salvato in file `.pyc` nella cartella `__pycache__/`. Questa compilazione è automatica e trasparente.

**3. Esecuzione sulla PVM.** La Python Virtual Machine (PVM) interpreta il bytecode istruzione per istruzione.

Python è quindi un linguaggio **semi-compilato**: compilazione in bytecode (automatica) + interpretazione del bytecode. È un compromesso che bilancia velocità di sviluppo e prestazioni ragionevoli.

### Il GIL (Global Interpreter Lock)

CPython ha una particolarità importante: il **GIL**, un blocco globale che impedisce a più thread Python di eseguire bytecode contemporaneamente. Il GIL semplifica enormemente la gestione della memoria interna di CPython ma limita il parallelismo. Per aggirarlo: `multiprocessing` (processi separati), programmazione asincrona (`asyncio`), o librerie che rilasciano il GIL (NumPy, quando esegue codice C).

### Implementazioni alternative

- **PyPy:** interprete Python scritto in Python, con compilazione JIT. Spesso 5-10x più veloce di CPython per codice Python puro.
- **MicroPython:** Python per microcontrollori (Arduino, ESP32) — programmare dispositivi embedded in Python.
- **Cython:** permette di scrivere codice simil-Python che viene compilato in C. Usato internamente da molte librerie scientifiche.

### Perché Python è "lento" (e perché spesso non importa)

Python è circa 10-100 volte più lento di C per il calcolo puro. Ma nella pratica:

1. Il **collo di bottiglia è la produttività del programmatore**, non la velocità del programma. Scrivere un'analisi in Python richiede ore; in C, giorni.
2. Per la parte computazionalmente intensiva, Python chiama **librerie scritte in C e Fortran** (NumPy, Pandas, SciPy). Il codice "lento" è solo il collante.
3. La maggior parte del tempo di un programma è spesa **aspettando** (I/O su disco, rete, input utente), non calcolando.

### Modalità di utilizzo

- **REPL (Read-Eval-Print Loop):** l'interprete interattivo. Si scrive un comando, Python lo esegue subito e mostra il risultato. Perfetto per esplorare e provare.
- **Script (.py):** il programma scritto in un file, eseguito con `python nome_script.py`. Per codice completo e riutilizzabile.
- **Jupyter Notebook (.ipynb):** celle di codice, testo e visualizzazioni insieme. Nato dal progetto IPython (Fernando Pérez, 2001), evoluto in Jupyter (2014, il nome omaggia **Ju**lia, **Py**thon e **R**). È diventato lo standard nella data science.

### Python: chi è e da dove viene

**Guido van Rossum**, programmatore olandese, iniziò a sviluppare Python durante le vacanze di **Natale 1989** ad Amsterdam, come progetto personale. Il nome non viene dal serpente ma dai **Monty Python**, il gruppo comico britannico che van Rossum adorava.

Python fu progettato con una filosofia chiara, codificata nello **Zen of Python** (provate: `import this` nell'interprete):

> *Beautiful is better than ugly.*
> *Explicit is better than implicit.*
> *Simple is better than complex.*
> *Readability counts.*

Python è: alto livello, multi-paradigma, interpretato (semi-compilato), tipizzato dinamicamente (ma con supporto per type hints volontari), garbage collected (la memoria viene gestita automaticamente).

**Perché Python per la statistica:**
- Leggibilità: il codice si legge quasi come l'inglese
- Ecosistema scientifico maturo: NumPy, Pandas, SciPy, scikit-learn, matplotlib
- Comunità enorme: qualsiasi problema sia già stato risolto da qualcuno
- Curva di apprendimento dolce: si può essere produttivi rapidamente
- Versatile: dallo scripting al web development, dal machine learning all'automazione

---

## Domande di verifica

1. **Quali sono le cinque proprietà fondamentali di un algoritmo?** Spiegate ciascuna con un esempio.

2. **Qual è la differenza tra programma e processo?** Fate un'analogia con un concetto della vita quotidiana.

3. **Cosa intende Jeannette Wing per "pensiero computazionale"?** Elencate e spiegate i quattro pilastri.

4. **Perché esistono tanti linguaggi di programmazione?** Non basterebbe uno solo?

5. **Qual è la differenza fondamentale tra compilazione e interpretazione?** Quali sono i vantaggi e gli svantaggi di ciascun approccio?

6. **Python è un linguaggio compilato o interpretato?** La risposta corretta è più sfumata di quanto sembri — spiegatela.

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

Questa lezione ha costruito il ponte tra le due parti del corso. Avete visto:

- **L'algoritmo** come concetto astratto, indipendente da qualsiasi macchina o linguaggio — un'idea tanto antica da precedere i computer di mille anni.
- **Il programma** come traduzione concreta dell'algoritmo in un linguaggio formale.
- **Il processo** come il programma che prende vita nella macchina.
- **Il pensiero computazionale** come un modo di ragionare che trascende l'informatica e si applica a qualsiasi disciplina — e che ha un legame profondo con il metodo statistico.
- **I linguaggi di programmazione** come strumenti con filosofie e punti di forza diversi, nati per risolvere problemi diversi.
- **Python** come il nostro strumento scelto: leggibile, potente, adatto alla statistica, con un interprete che bilancia elegantemente compilazione e interpretazione.

Da qui in poi, programmiamo. Nella prossima lezione scriveremo il nostro primo codice Python: variabili, tipi, espressioni. Ma ricordate: prima di scrivere codice, **pensate**. Capite il problema, progettate la soluzione, poi implementatela. Il codice è l'ultimo passo, non il primo.

> *"Weeks of coding can save you hours of planning."* — Detto popolare tra i programmatori
