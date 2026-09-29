# Lezione 3 — Architettura degli elaboratori

## Introduzione

Nelle lezioni precedenti abbiamo visto come l'informazione può essere rappresentata con i bit e come la logica booleana permette di costruire circuiti capaci di eseguire operazioni. Oggi vediamo come queste componenti sono organizzate per formare un **elaboratore**, cioè una macchina capace di eseguire programmi.

Lo schema di riferimento è quello descritto da **John von Neumann** nel 1945. Con molte evoluzioni, è ancora alla base di quasi tutti i computer in uso, dallo smartphone ai supercomputer.

---

## Il modello di von Neumann

### Il contesto storico

Nel 1945 i primi computer elettronici, come l'ENIAC, erano appena nati. L'ENIAC poteva eseguire circa 5.000 addizioni al secondo, ma per cambiare programma bisognava **ricablare** fisicamente la macchina, spostando cavi e interruttori. Un cambio di programma poteva richiedere giorni.

John von Neumann, matematico di origine ungherese dell'Institute for Advanced Study di Princeton, partecipava come consulente al progetto del successore dell'ENIAC, l'EDVAC. Nel documento *"First Draft of a Report on the EDVAC"* (1945) descrisse l'idea, maturata nel gruppo di progetto insieme a J. Presper Eckert e John Mauchly, che **il programma deve essere memorizzato nella stessa memoria dei dati**. Prima il programma era "esterno" alla macchina: un cablaggio, una sequenza di schede perforate. Con questa idea il programma diventa un dato come gli altri: una sequenza di numeri nella memoria.

Ne segue che un programma, stando in memoria, può essere modificato, copiato, trasmesso via rete e generato da un altro programma. Compilatori, sistemi operativi e l'installazione di un'app si basano su questa possibilità.

### Le componenti fondamentali

Il modello di von Neumann descrive un elaboratore composto da quattro componenti principali: la CPU, la memoria, i dispositivi di input/output e il **bus**, cioè i canali di comunicazione che collegano le altre tre.

#### La CPU (Central Processing Unit)

La CPU è il componente che esegue le istruzioni. Al suo interno troviamo tre sotto-componenti:

- **ALU (Arithmetic Logic Unit):** esegue le operazioni aritmetiche (somma, sottrazione, moltiplicazione, divisione) e logiche (AND, OR, NOT, confronti). L'ALU è costruita con le porte logiche viste nella lezione precedente.

- **Unità di controllo:** legge le istruzioni dalla memoria, le interpreta e coordina le altre componenti per eseguirle, stabilendo quali operazioni fare e in quale ordine.

- **Registri:** piccole memorie velocissime interne alla CPU. Conservano i dati su cui la CPU sta lavorando in quel momento. Nei processori attuali un registro generale contiene 64 bit (32 nei modelli più vecchi o più semplici). Due registri hanno un ruolo speciale: il **Program Counter (PC)**, che contiene l'indirizzo in memoria della prossima istruzione da eseguire, e l'**Instruction Register (IR)**, che contiene l'istruzione in esecuzione.

#### La memoria principale (RAM)

La RAM (*Random Access Memory*) è la memoria di lavoro del computer. "Random Access" significa che si può leggere qualsiasi posizione in un tempo che non dipende dalla posizione, senza scorrere i dati in sequenza come su un nastro magnetico. La RAM è:

- **Veloce:** molto più veloce di un disco, ma più lenta dei registri.
- **Volatile:** quando si spegne il computer, il contenuto della RAM si perde.
- **Limitata:** ha una capacità finita (tipicamente 8-32 GB in un computer attuale).

Nella RAM si trovano sia i **dati** sia il **programma** in esecuzione: è l'idea di von Neumann. La memoria è organizzata come una sequenza di celle, ciascuna identificata da un **indirizzo** numerico. Ogni cella contiene un byte (8 bit).

#### I dispositivi di Input/Output (I/O)

Sono i componenti che permettono al computer di comunicare con l'esterno:

- **Input:** tastiera, mouse, microfono, sensori, connessione di rete, disco (in lettura).
- **Output:** schermo, stampante, altoparlante, connessione di rete, disco (in scrittura).

I dispositivi di I/O sono molto più lenti della CPU: una lettura da disco dura quanto centinaia di migliaia di cicli di clock (SSD) o decine di milioni (disco magnetico).

#### Il bus di sistema

Il bus è l'insieme dei canali di comunicazione che collegano le componenti. Si divide in:

- **Bus dati:** trasporta i dati tra CPU, memoria e dispositivi.
- **Bus indirizzi:** trasporta gli indirizzi di memoria (la CPU dice "voglio il dato alla posizione X").
- **Bus di controllo:** trasporta i segnali di coordinamento (lettura/scrittura, interruzioni).

### Il collo di bottiglia di von Neumann

Il modello ha un limite: la CPU e la memoria comunicano attraverso un unico canale, e la CPU è molto più veloce della memoria. Per questo la CPU spesso **aspetta** che i dati arrivino dalla memoria. Il limite si chiama *"von Neumann bottleneck"*; il nome è stato proposto nel 1977 da John Backus, che aveva guidato lo sviluppo del Fortran.

Gran parte dell'evoluzione dell'architettura dei computer negli ultimi 50 anni è servita ad aggirare questo limite: la cache, il pipelining, l'esecuzione fuori ordine, il prefetching (caricare in anticipo i dati che probabilmente serviranno). Alcune di queste tecniche le vediamo più avanti in questa lezione.

---

## Il ciclo fetch-decode-execute

La CPU lavora ripetendo un ciclo semplice, miliardi di volte al secondo:

### 1. Fetch (prelievo)

La CPU legge dalla memoria l'istruzione che si trova all'indirizzo indicato dal Program Counter. L'istruzione viene copiata nell'Instruction Register.

### 2. Decode (decodifica)

L'unità di controllo interpreta l'istruzione: stabilisce che tipo di operazione è (aritmetica, salto, lettura dalla memoria...) e quali operandi coinvolge.

### 3. Execute (esecuzione)

L'operazione viene eseguita. Se è un'operazione aritmetica, la esegue l'ALU. Se è un accesso alla memoria, vengono letti o scritti dati. Se è un salto, viene modificato il Program Counter.

### 4. Aggiornamento del Program Counter

Il Program Counter viene aggiornato per puntare all'istruzione successiva (normalmente quella all'indirizzo seguente, a meno di un salto) e il ciclo ricomincia.

### Il clock

Il ciclo fetch-decode-execute è scandito da un segnale periodico chiamato **clock**. La frequenza del clock si misura in **Hertz (Hz)**: un clock a 3 GHz (3 miliardi di Hertz) batte 3 miliardi di volte al secondo, quindi un ciclo dura circa 0,33 ns. Ogni ciclo è l'intervallo di tempo in cui avviene un'operazione elementare.

Aumentare la frequenza ha però dei limiti fisici. La potenza dissipata cresce con la frequenza e con il quadrato della tensione, e per salire di frequenza serve anche più tensione: in pratica il calore prodotto cresce circa con il cubo della frequenza. Inoltre i segnali elettrici hanno bisogno di tempo per propagarsi nel circuito. Intorno al 2004-2005 la crescita della frequenza si è fermata poco sotto i 4 GHz; da allora è salita lentamente, fino ai 5-6 GHz che i processori di punta raggiungono oggi per brevi periodi (modalità turbo). Come vedremo, questo ha cambiato il modo di progettare i processori.

### Cenni sul pipelining

Un modo per aumentare le prestazioni senza aumentare la frequenza è il **pipelining**: sovrapporre le fasi del ciclo, come in una catena di montaggio.

Pensate a una lavanderia: lavare richiede 30 minuti, asciugare 30 minuti, piegare 30 minuti. Senza pipeline, tre carichi richiedono 270 minuti (3 × 90). Con la pipeline, mentre il primo carico asciuga, il secondo lava; mentre il primo viene piegato, il secondo asciuga e il terzo lava. I tre carichi finiscono in 150 minuti (90 + 30 + 30).

Allo stesso modo, mentre la CPU esegue un'istruzione, sta già decodificando la successiva e prelevando quella dopo ancora. Ogni singola istruzione richiede lo stesso tempo, ma il **throughput** (numero di istruzioni completate per unità di tempo) aumenta: con tre fasi da un ciclo ciascuna, tre istruzioni richiedono 5 cicli invece di 9.

### Dalla teoria alla pratica

Cosa succede quando scrivete `x = 3 + 5` in Python? In modo semplificato:

1. L'interprete Python legge la riga di codice (testo).
2. La traduce in **bytecode** (istruzioni per la Python Virtual Machine, PVM).
3. La PVM interpreta il bytecode e chiama le routine C appropriate.
4. Queste routine sono state tradotte in anticipo dal compilatore C in **codice macchina** (istruzioni native della CPU).
5. La CPU esegue queste istruzioni attraverso il ciclo fetch-decode-execute: carica il valore 3 in un registro, carica il valore 5 in un altro registro, somma i due registri, memorizza il risultato.

L'esecuzione di questa riga richiede meno di un milionesimo di secondo.

---

## La gerarchia di memoria

### Il compromesso fondamentale

Non si riesce a costruire una memoria che sia contemporaneamente molto veloce, molto grande ed economica. Bisogna scegliere:

- Le memorie più veloci (registri, cache) sono piccole e costose.
- Le memorie più grandi (dischi, cloud) sono lente ed economiche.

La soluzione è organizzare la memoria come una **piramide gerarchica**, in cui ogni livello è più grande ma più lento del precedente. I valori della tabella sono ordini di grandezza tipici per un computer attuale:

| Livello | Tempo di accesso | Capacità tipica | Costo relativo |
|---------|-----------------|-----------------|----------------|
| **Registri** | < 1 ns (1 ciclo) | ~1 KB (decine di registri) | Altissimo |
| **Cache L1** | ~1 ns | 32-64 KB per core | Molto alto |
| **Cache L2** | ~3-5 ns | 1-3 MB per core | Alto |
| **Cache L3** | ~10-20 ns | 8-64 MB (condivisa) | Medio-alto |
| **RAM** | ~50-100 ns | 8-32 GB | Medio |
| **SSD** | ~0,1 ms (100.000 ns) | 256 GB - 4 TB | Basso |
| **HDD** | ~5-10 ms | 1-30 TB | Molto basso |
| **Cloud/Archivi** | ms - secondi | Praticamente illimitata | Variabile |

Tra un registro e un disco rigido c'è un fattore di circa **10 milioni**. È come la differenza tra prendere un libro dalla scrivania (registri) e ordinarlo da una libreria all'estero e aspettare la consegna (HDD).

### La cache e il principio di località

La cache è una memoria piccola e veloce che si trova tra la CPU e la RAM. Funziona grazie a un'osservazione empirica chiamata **principio di località**:

- **Località temporale:** se un dato è stato usato di recente, è probabile che venga usato di nuovo a breve. Esempio: una variabile contatore in un ciclo viene letta e scritta a ogni iterazione.

- **Località spaziale:** se un dato è stato usato, è probabile che i dati vicini in memoria vengano usati presto. Esempio: scorrere gli elementi di un array significa accedere a posizioni consecutive di memoria.

Quando la CPU ha bisogno di un dato, lo cerca prima nella cache. Se lo trova (**cache hit**), lo ottiene in circa 1 ns. Se non lo trova (**cache miss**), deve leggerlo dalla RAM (circa 100 ns) e ne approfitta per copiare in cache anche i dati vicini (sfruttando la località spaziale).

I processori attuali hanno in genere tre livelli di cache (L1, L2, L3), ciascuno più grande e più lento del precedente. La cache L1 è separata in cache dati e cache istruzioni, entrambe interne al singolo core; la L2 è di solito dedicata a un core; la L3 è condivisa tra tutti i core.

### SSD e HDD

I dischi rigidi tradizionali (HDD, *Hard Disk Drive*) conservano i dati su piatti magnetici rotanti, letti da una testina meccanica. Sono economici e capienti, ma lenti: la testina deve spostarsi fisicamente sulla posizione giusta.

Gli SSD (*Solid State Drive*) usano memoria flash (la stessa tecnologia delle chiavette USB), senza parti meccaniche in movimento. Negli accessi casuali hanno un tempo di accesso circa 50-100 volte più basso (0,1 ms contro 5-10 ms); sono inoltre più resistenti agli urti e silenziosi, ma costano di più per gigabyte.

### Applicazione per la statistica

La gerarchia di memoria incide direttamente sui tempi delle vostre analisi:

- **Caricare un dataset intero in RAM** (come fa Pandas con `read_csv()`) rende veloci le operazioni successive, ma richiede che il dataset stia nella RAM disponibile. Se non ci sta, il sistema operativo inizia a usare lo swap (una parte del disco usata come estensione della RAM) e tutto rallenta molto, oppure il programma si ferma con un errore di memoria esaurita.

- **NumPy** organizza i dati in **blocchi contigui di memoria** (array in stile C) e quindi sfrutta bene la località spaziale e la cache. Una lista Python, invece, contiene puntatori a oggetti che possono trovarsi in posizioni sparse della memoria. Questo è uno dei motivi per cui NumPy è molto più veloce nel calcolo numerico (l'altro è che i suoi cicli sono eseguiti in codice C compilato).

- Quando lavorate con un dataset molto grande, la scelta tra leggerlo tutto in RAM o elaborarlo a pezzi, riga per riga o blocco per blocco ("streaming"), dipende da questo compromesso.

---

## Parallelismo e architetture moderne

### La fine della corsa ai GHz

Per decenni l'industria dei processori ha aumentato la frequenza del clock. Ogni anno i processori diventavano più veloci, e i programmi ne beneficiavano senza modifiche al codice.

Intorno al 2004-2005 questo approccio si è fermato: oltre i 4 GHz circa il chip produce più calore di quanto i normali sistemi di raffreddamento riescano a smaltire.

L'industria ha quindi cambiato strategia: invece di un singolo processore più veloce, **più processori** (core) sullo stesso chip. Sono nati i processori multi-core.

### Multi-core

Un processore **multi-core** contiene due, quattro, otto o più unità di elaborazione indipendenti (core) sullo stesso chip. Ogni core può eseguire un flusso di istruzioni separato.

Avere 8 core, però, non rende automaticamente un programma 8 volte più veloce. Il **software** deve essere scritto per sfruttare il parallelismo, cioè dividere il lavoro in parti indipendenti da eseguire contemporaneamente. Non tutti i problemi si prestano a questa divisione: se il passo 2 dipende dal risultato del passo 1, i due passi non si possono eseguire in parallelo.

### GPU (Graphics Processing Unit)

Le GPU sono nate negli anni '90 per un compito specifico: calcolare le immagini dei videogiochi in tempo reale. Il colore di ogni pixel si calcola in modo indipendente dagli altri, quindi le GPU sono state progettate con molte unità di calcolo semplici che eseguono la stessa operazione su dati diversi contemporaneamente; oggi una GPU ha migliaia di core.

Le operazioni fondamentali delle reti neurali (moltiplicazioni di matrici, trasformazioni vettoriali) hanno la stessa struttura: tante operazioni identiche su dati diversi. Per questo le GPU, nate per i giochi, sono diventate lo strumento principale per il deep learning.

NVIDIA, con la piattaforma **CUDA** (2006), ha reso possibile programmare le GPU per scopi generici (*GPGPU, General-Purpose computing on GPU*). Oggi i grandi modelli, come GPT o i sistemi di riconoscimento di immagini, si addestrano su GPU o su acceleratori simili.

### Cenni su architetture specializzate

- **TPU (Tensor Processing Unit):** chip progettati da Google per il deep learning, ottimizzati per le operazioni tensoriali (moltiplicazioni di matrici di grandi dimensioni). Sono usati nei data center di Google per addestrare ed eseguire i loro modelli.

- **Chip ARM:** architettura di tipo *RISC* (*Reduced Instruction Set Computer*, con un insieme ridotto di istruzioni semplici), nota per il basso consumo energetico. Quasi tutti gli smartphone usano processori ARM, e il basso consumo è uno dei motivi per cui la batteria dura una giornata.

- **Apple Silicon (serie M, dal 2020):** Apple ha portato l'architettura ARM nei computer portatili e desktop, integrando CPU, GPU e acceleratore per il machine learning ("Neural Engine") sullo stesso chip, con la memoria nello stesso contenitore (*package*). Questo approccio (*System on a Chip, SoC*) riduce le distanze fisiche tra i componenti e il consumo energetico.

### Prospettiva futura: il quantum computing

I computer quantistici sfruttano le leggi della meccanica quantistica. Il **qubit** (quantum bit), a differenza del bit classico che vale 0 o 1, può trovarsi in una **sovrapposizione** dei due stati. Per descrivere lo stato di n qubit **entangled** (correlati quantisticamente) servono 2ⁿ numeri: con 50 qubit sono circa un milione di miliardi.

Per alcuni problemi sono noti algoritmi quantistici molto più veloci dei migliori algoritmi classici: la fattorizzazione di numeri grandi (algoritmo di Shor, rilevante per la crittografia) e la simulazione di molecole (chimica e farmacologia). Per l'ottimizzazione combinatoria il vantaggio è ancora oggetto di ricerca. Per la maggior parte dei compiti quotidiani i computer classici restano la scelta giusta.

Il quantum computing è ancora nelle fasi iniziali: i qubit attuali sono fragili, molte tecnologie richiedono temperature prossime allo zero assoluto, e i tassi di errore sono alti.

---

## Domande di verifica

1. **Quale idea introduce il modello di von Neumann rispetto ai computer precedenti come l'ENIAC?**

2. **Descrivete le quattro componenti principali del modello di von Neumann e il ruolo di ciascuna.**

3. **Cosa fa ciascuna delle fasi del ciclo fetch-decode-execute? Qual è il ruolo del Program Counter?**

4. **Cos'è il "collo di bottiglia di von Neumann" e perché è ancora un problema rilevante?**

5. **Spiegate il principio di località (temporale e spaziale) e come viene sfruttato dalla cache.**

6. **Perché la corsa ai GHz si è fermata intorno al 2005? Quale strategia alternativa è stata adottata?**

7. **Perché le GPU, nate per i videogiochi, sono diventate fondamentali per il machine learning?**

8. **Un programma che lavora su un grande dataset trae più vantaggio da una maggiore quantità di RAM o da un processore con più GHz? Motivate la risposta.**

---

## Esercizi

### Base

1. **Ordinate** i seguenti supporti di memoria dal più veloce al più lento: RAM, cache L1, SSD, registri, HDD, cache L3. Per ciascuno, indicate un ordine di grandezza del tempo di accesso.

2. Un processore ha un clock a 3 GHz. **Quanti cicli di clock** esegue in un secondo? E in un millisecondo?

3. Supponiamo che un'istruzione richieda 4 cicli di clock. **Quante istruzioni** può completare il processore in un secondo?

### Intermedio

4. Un dataset occupa 16 GB. La RAM disponibile è di 8 GB. **Cosa succede** quando provate a caricarlo interamente in memoria? Quale componente della gerarchia di memoria entra in gioco e perché le prestazioni peggiorano?

5. Spiegate con un esempio concreto (non quello del testo) il concetto di **località spaziale** e come la cache ne trae vantaggio.

6. Un programma esegue un ciclo che somma gli elementi di un array di 1.000.000 di numeri. Un altro programma accede a posizioni casuali di un array della stessa dimensione. **Quale dei due sarà più veloce e perché**, anche se entrambi eseguono lo stesso numero di operazioni?

### Avanzato

7. Immaginate di dover calcolare la media di 10 miliardi di numeri. La RAM del vostro computer è di 16 GB e ogni numero occupa 8 byte. **Potete caricare tutti i numeri in RAM?** Se no, progettate (in pseudocodice) un algoritmo che calcoli la media senza caricare tutti i dati in memoria contemporaneamente.

8. Spiegate perché il passaggio da single-core a multi-core non raddoppia automaticamente le prestazioni di un programma. Fate un esempio di un calcolo **parallelizzabile** e uno **non parallelizzabile**.

---

## Osservazioni finali

In questa lezione abbiamo visto come i componenti fisici di un elaboratore (CPU, memoria, bus, dispositivi di I/O) si organizzano per eseguire programmi. Il modello di von Neumann, con il programma memorizzato nella stessa memoria dei dati, è ancora il riferimento dopo ottant'anni.

Abbiamo visto anche i suoi limiti: il collo di bottiglia tra CPU e memoria, il limite termico alla frequenza del clock, la difficoltà di scrivere software parallelo. Cache, pipelining, multi-core e GPU sono le soluzioni adottate finora.

Per uno statistico la conseguenza pratica è questa: la velocità di un'analisi dipende da dove si trovano i dati (RAM, disco, rete) e da come sono disposti in memoria. Quando userete NumPy e Pandas, una parte della loro velocità si spiega con quanto visto oggi: dati contigui in memoria e buon uso della cache.

Nella prossima lezione passiamo dalla macchina ai programmi: vedremo che cos'è un algoritmo e come si passa **dal problema al programma**. Il sistema operativo, il software che gestisce le risorse della macchina, sarà l'argomento di una lezione successiva (T04).
