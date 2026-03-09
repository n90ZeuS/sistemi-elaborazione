# Lezione Frontale 3 — Architettura degli elaboratori

## Introduzione

Nelle lezioni precedenti abbiamo visto come l'informazione può essere rappresentata con i bit e come la logica booleana permette di costruire circuiti capaci di eseguire operazioni. Oggi facciamo il passo successivo: come sono organizzate queste componenti per formare un **elaboratore**, cioè una macchina capace di eseguire programmi.

La risposta a questa domanda ha un nome e un cognome: **John von Neumann**. Il modello che propose nel 1945 è talmente elegante e potente che, con le dovute evoluzioni, è ancora alla base di praticamente ogni computer esistente — dal vostro smartphone al supercomputer più potente del mondo.

---

## Il modello di von Neumann

### Il contesto storico

Siamo nel 1945. La Seconda Guerra Mondiale sta finendo, e i primi computer elettronici — come l'ENIAC — sono appena nati. L'ENIAC era una macchina straordinaria per l'epoca: poteva eseguire 5.000 addizioni al secondo. Ma aveva un problema enorme: per cambiare programma, bisognava fisicamente **ricablare** la macchina, spostando cavi e interruttori. Cambiare un programma poteva richiedere giorni.

John von Neumann, matematico di origine ungherese che lavorava all'Institute for Advanced Study di Princeton, ebbe un'intuizione che cambiò tutto. Nel suo celebre documento *"First Draft of a Report on the EDVAC"* (1945), propose un'idea rivoluzionaria: **il programma deve essere memorizzato nella stessa memoria dei dati**. Prima di von Neumann, il programma era qualcosa di "esterno" alla macchina — un cablaggio, una sequenza di schede perforate. Dopo von Neumann, il programma diventa un dato come gli altri: una sequenza di numeri nella memoria.

Questa idea, apparentemente semplice, ha conseguenze profondissime: se il programma è in memoria, può essere modificato, copiato, trasmesso via rete, generato da un altro programma. Tutta l'informatica moderna — dai sistemi operativi ai compilatori, dall'intelligenza artificiale agli app store — discende da questa intuizione.

### Le componenti fondamentali

Il modello di von Neumann descrive un elaboratore composto da quattro componenti principali, collegate tra loro da canali di comunicazione chiamati **bus**.

#### La CPU (Central Processing Unit)

La CPU è il "cervello" del computer: è il componente che esegue le istruzioni. Al suo interno troviamo tre sotto-componenti:

- **ALU (Arithmetic Logic Unit):** esegue le operazioni aritmetiche (somma, sottrazione, moltiplicazione, divisione) e logiche (AND, OR, NOT, confronti). È qui che la logica booleana studiata nella lezione precedente prende vita nel silicio.

- **Unità di controllo:** è il "direttore d'orchestra" della CPU. Legge le istruzioni dalla memoria, le interpreta e coordina tutte le altre componenti per eseguirle. Decide cosa fare, quando farlo e in quale ordine.

- **Registri:** piccole memorie ultra-veloci interne alla CPU. Servono per conservare temporaneamente i dati su cui la CPU sta lavorando in quel preciso istante. Un registro tipico contiene 32 o 64 bit. Tra i registri più importanti c'è il **Program Counter (PC)**, che contiene l'indirizzo in memoria della prossima istruzione da eseguire, e l'**Instruction Register (IR)**, che contiene l'istruzione attualmente in esecuzione.

#### La memoria principale (RAM)

La RAM (*Random Access Memory*) è la memoria di lavoro del computer. "Random Access" significa che qualsiasi posizione è accessibile in tempo costante — non bisogna scorrere sequenzialmente come in un nastro magnetico. La RAM è:

- **Veloce:** molto più veloce di un disco, ma molto più lenta dei registri.
- **Volatile:** quando si spegne il computer, il contenuto della RAM si perde.
- **Limitata:** ha una capacità finita (tipicamente 8-32 GB in un computer moderno).

Nella RAM risiedono sia i **dati** che il **programma** in esecuzione — questa è esattamente l'intuizione di von Neumann. La memoria è organizzata come una sequenza di celle, ciascuna identificata da un **indirizzo** numerico. Ogni cella contiene tipicamente un byte (8 bit).

#### I dispositivi di Input/Output (I/O)

Sono i componenti che permettono al computer di comunicare con il mondo esterno:

- **Input:** tastiera, mouse, microfono, sensori, connessione di rete, disco (in lettura).
- **Output:** schermo, stampante, altoparlante, connessione di rete, disco (in scrittura).

I dispositivi di I/O sono enormemente più lenti della CPU — questa asimmetria è una delle sfide fondamentali dell'architettura dei computer.

#### Il bus di sistema

Il bus è l'insieme dei canali di comunicazione che collegano le componenti. Si divide in:

- **Bus dati:** trasporta i dati tra CPU, memoria e dispositivi.
- **Bus indirizzi:** trasporta gli indirizzi di memoria (la CPU dice "voglio il dato alla posizione X").
- **Bus di controllo:** trasporta i segnali di coordinamento (lettura/scrittura, interruzioni).

### Il collo di bottiglia di von Neumann

Il modello è elegante, ma ha un limite intrinseco: la CPU e la memoria comunicano attraverso un unico bus, e la CPU è molto più veloce della memoria. Il risultato è che la CPU spesso **aspetta** che i dati arrivino dalla memoria. Questo limite si chiama il *"von Neumann bottleneck"* ed è stato identificato già negli anni '70 da John Backus (l'inventore del Fortran).

Gran parte dell'evoluzione dell'architettura dei computer negli ultimi 50 anni è stata dedicata ad aggirare questo collo di bottiglia: la cache, il pipelining, l'esecuzione fuori ordine, il prefetching. Ne parleremo tra poco.

---

## Il ciclo fetch-decode-execute

Il funzionamento della CPU si riduce a un ciclo semplicissimo che si ripete miliardi di volte al secondo:

### 1. Fetch (prelievo)

La CPU legge dalla memoria l'istruzione che si trova all'indirizzo indicato dal Program Counter. L'istruzione viene copiata nell'Instruction Register.

### 2. Decode (decodifica)

L'unità di controllo interpreta l'istruzione: capisce che tipo di operazione è (aritmetica? salto? lettura dalla memoria?) e quali operandi coinvolge.

### 3. Execute (esecuzione)

L'operazione viene effettivamente eseguita. Se è un'operazione aritmetica, la esegue l'ALU. Se è un accesso alla memoria, vengono letti o scritti dati. Se è un salto, viene modificato il Program Counter.

### 4. Aggiornamento del Program Counter

Il Program Counter viene aggiornato per puntare all'istruzione successiva (normalmente l'indirizzo successivo, a meno di un salto) e il ciclo ricomincia.

### Il clock

Il ciclo fetch-decode-execute è scandito da un segnale periodico chiamato **clock**. La frequenza del clock si misura in **Hertz (Hz)**: un clock a 3 GHz (3 miliardi di Hertz) batte 3 miliardi di volte al secondo. Ogni battito definisce un intervallo di tempo minimo in cui può avvenire un'operazione elementare.

Attenzione però: un clock più veloce non significa automaticamente un computer più veloce. Ci sono limiti fisici: aumentare la frequenza genera più calore (la potenza dissipata cresce con il cubo della frequenza), e i segnali elettrici hanno bisogno di tempo per propagarsi nel circuito. Intorno al 2005, la corsa ai GHz si è sostanzialmente fermata intorno ai 4-5 GHz — un muro che ha cambiato la direzione dell'intera industria, come vedremo.

### Cenni sul pipelining

Un'idea geniale per aumentare le prestazioni senza aumentare la frequenza è il **pipelining**: sovrapporre le fasi del ciclo, proprio come in una catena di montaggio.

Immaginate una lavanderia: lavare richiede 30 minuti, asciugare 30 minuti, piegare 30 minuti. Senza pipeline, tre carichi richiedono 270 minuti (3 × 90). Con il pipeline, mentre il primo carico asciuga, il secondo lava; mentre il primo piega, il secondo asciuga e il terzo lava. I tre carichi finiscono in 150 minuti.

Allo stesso modo, mentre la CPU esegue un'istruzione, sta già decodificando la successiva e prelevando quella dopo ancora. Il risultato netto è che, anche se ogni singola istruzione richiede lo stesso tempo, il **throughput** (numero di istruzioni completate per unità di tempo) aumenta significativamente.

### Dalla teoria alla pratica

Cosa succede concretamente quando scrivete `x = 3 + 5` in Python? Il percorso è lungo ma istruttivo:

1. L'interprete Python legge la riga di codice (testo).
2. La traduce in **bytecode** (istruzioni per la Python Virtual Machine).
3. La PVM interpreta il bytecode e chiama le routine C appropriate.
4. Il compilatore C le ha già tradotte in **codice macchina** (istruzioni native della CPU).
5. La CPU esegue queste istruzioni attraverso il ciclo fetch-decode-execute: carica il valore 3 in un registro, carica il valore 5 in un altro registro, somma i due registri, memorizza il risultato.

Tutto questo avviene in meno di un milionesimo di secondo.

---

## La gerarchia di memoria

### Il compromesso fondamentale

Esiste un problema fisico ineludibile: **non è possibile costruire una memoria che sia contemporaneamente velocissima, enorme e a basso costo**. La fisica impone un compromesso:

- Le memorie più veloci (registri, cache) sono piccole e costose.
- Le memorie più grandi (dischi, cloud) sono lente ed economiche.

La soluzione è organizzare la memoria come una **piramide gerarchica**, dove ogni livello è più grande ma più lento del precedente:

| Livello | Tempo di accesso | Capacità tipica | Costo relativo |
|---------|-----------------|-----------------|----------------|
| **Registri** | ~1 ns | ~1 KB (decine di registri) | Altissimo |
| **Cache L1** | ~1-2 ns | 32-64 KB per core | Molto alto |
| **Cache L2** | ~5-10 ns | 256 KB - 1 MB per core | Alto |
| **Cache L3** | ~20-30 ns | 8-64 MB (condivisa) | Medio-alto |
| **RAM** | ~50-100 ns | 8-64 GB | Medio |
| **SSD** | ~0,1 ms (100.000 ns) | 256 GB - 4 TB | Basso |
| **HDD** | ~5-10 ms | 1-20 TB | Molto basso |
| **Cloud/Archivi** | ms - secondi | Virtualmente illimitata | Variabile |

Guardate i numeri: tra un registro e un disco rigido c'è un fattore di **10 milioni**. È come la differenza tra prendere un libro dalla scrivania (registri) e ordinarlo da una libreria all'estero e aspettare la consegna (HDD).

### La cache e il principio di località

La cache è una memoria piccola e veloce che si interpone tra la CPU e la RAM. Il suo funzionamento si basa su un'osservazione empirica fondamentale chiamata **principio di località**:

- **Località temporale:** se un dato è stato usato di recente, è probabile che verrà usato di nuovo a breve. Esempio: una variabile contatore in un ciclo viene letta e scritta ad ogni iterazione.

- **Località spaziale:** se un dato è stato usato, è probabile che i dati vicini in memoria verranno usati presto. Esempio: scorrere gli elementi di un array significa accedere a posizioni consecutive di memoria.

Quando la CPU ha bisogno di un dato, lo cerca prima nella cache. Se lo trova (**cache hit**), lo ottiene velocemente. Se non lo trova (**cache miss**), deve andare a cercarlo nella RAM (molto più lento) e ne approfitta per copiare in cache anche i dati vicini (sfruttando la località spaziale).

I processori moderni hanno tipicamente tre livelli di cache (L1, L2, L3), ciascuno più grande e leggermente più lento del precedente. La cache L1 è separata in cache dati e cache istruzioni, entrambe interne al singolo core. La cache L3 è generalmente condivisa tra tutti i core.

### SSD vs HDD: la rivoluzione della memoria flash

I dischi rigidi tradizionali (HDD, *Hard Disk Drive*) conservano i dati su piatti magnetici rotanti, letti da una testina meccanica. Sono economici e capienti, ma lenti: la testina deve fisicamente spostarsi sulla posizione giusta.

Gli SSD (*Solid State Drive*) usano memoria flash (la stessa tecnologia delle chiavette USB), senza parti meccaniche in movimento. Sono enormemente più veloci per gli accessi casuali (fino a 100 volte), più resistenti agli urti, silenziosi, ma più costosi per gigabyte.

### Applicazione per la statistica

Perché tutto questo è rilevante per uno statistico? Perché la gerarchia di memoria determina direttamente le prestazioni delle vostre analisi:

- **Caricare un dataset intero in RAM** (come fa Pandas con `read_csv()`) è veloce per le operazioni successive, ma richiede che il dataset stia nella RAM disponibile. Se non ci sta, il sistema operativo inizia a usare lo swap (disco come estensione della RAM) e tutto rallenta drasticamente.

- **NumPy** organizza i dati in **blocchi contigui di memoria** (array C-style), sfruttando al massimo la località spaziale e quindi la cache. Le liste Python, al contrario, disperdono gli oggetti in posizioni sparse della memoria. Ecco perché NumPy è ordini di grandezza più veloce per il calcolo numerico.

- Quando lavorate con un dataset molto grande, la scelta tra leggerlo tutto in RAM o elaborarlo riga per riga ("streaming") dipende esattamente da questo compromesso.

---

## Parallelismo e architetture moderne

### La fine della corsa ai GHz

Per decenni, l'industria dei processori ha seguito una strategia semplice: aumentare la frequenza del clock. Ogni anno, i processori diventavano più veloci, e i programmi ne beneficiavano automaticamente senza dover cambiare una riga di codice.

Intorno al 2005, questo approccio ha raggiunto un muro: a 4-5 GHz, la dissipazione termica diventa ingestibile. Un processore a frequenze più alte genererebbe tanto calore da non poter essere raffreddato con sistemi convenzionali. La densità di potenza si avvicinerebbe a quella della superficie del sole.

L'industria ha quindi cambiato strategia: non più processori singoli più veloci, ma **più processori** (core) sullo stesso chip. È nata l'era multi-core.

### Multi-core

Un processore **multi-core** contiene due, quattro, otto o più CPU indipendenti sullo stesso chip. Ogni core può eseguire un flusso di istruzioni separato.

Ma c'è un problema fondamentale: avere 8 core non significa automaticamente che il programma va 8 volte più veloce. Bisogna che il **software** sia scritto per sfruttare il parallelismo — dividere il lavoro in parti indipendenti che possono essere eseguite contemporaneamente. Non tutti i problemi si prestano a questa divisione: se il passo 2 dipende dal risultato del passo 1, non si può parallelizzare.

### GPU (Graphics Processing Unit)

Le GPU nacquero negli anni '90 per un compito specifico: calcolare le immagini dei videogiochi in tempo reale. Ogni pixel sullo schermo richiede calcoli indipendenti dagli altri pixel, quindi le GPU furono progettate con **migliaia di core semplici** capaci di eseguire la stessa operazione su dati diversi contemporaneamente.

I ricercatori di machine learning si accorsero che le operazioni fondamentali delle reti neurali — moltiplicazioni di matrici, trasformazioni vettoriali — hanno esattamente la stessa struttura: migliaia di operazioni identiche su dati diversi. Così le GPU, nate per i giochi, sono diventate il motore del deep learning e dell'intelligenza artificiale moderna.

NVIDIA, con la sua piattaforma **CUDA** (2006), ha reso possibile programmare le GPU per scopi generici (*GPGPU, General-Purpose computing on GPU*). Oggi, l'addestramento di modelli come GPT o i sistemi di riconoscimento di immagini sarebbe impossibile senza GPU.

### Cenni su architetture specializzate

- **TPU (Tensor Processing Unit):** chip progettati da Google specificamente per il deep learning. Ottimizzati per le operazioni tensoriali (moltiplicazioni di matrici di grandi dimensioni), usati nei data center di Google per addestrare e servire i loro modelli AI.

- **Chip ARM:** architettura basata su un design a basso consumo energetico (*RISC, Reduced Instruction Set Computer*). Domina il mondo mobile: praticamente tutti gli smartphone usano processori ARM. Il vostro telefono è potente ma la batteria dura tutto il giorno grazie a questa architettura.

- **Apple Silicon (M1/M2/M3/M4):** Apple ha portato l'architettura ARM nei computer portatili e desktop, integrando CPU, GPU, acceleratore per il machine learning ("Neural Engine") e memoria sullo stesso chip. Questo approccio (*System on a Chip, SoC*) riduce le distanze fisiche tra i componenti e il consumo energetico, con prestazioni sorprendenti.

### Prospettiva futura: il quantum computing

I computer quantistici sfruttano le leggi della meccanica quantistica per eseguire calcoli impossibili per i computer classici. Il **qubit** (quantum bit), a differenza del bit classico che è 0 o 1, può trovarsi in una **sovrapposizione** di entrambi gli stati contemporaneamente. Quando più qubit sono **entangled** (correlati quantisticamente), il numero di stati rappresentabili cresce esponenzialmente.

Per certi problemi — come la fattorizzazione di numeri grandi (crittografia), la simulazione di molecole (chimica e farmacologia), l'ottimizzazione combinatoria — i computer quantistici promettono di essere esponenzialmente più veloci. Per la maggior parte dei compiti quotidiani, però, i computer classici resteranno la scelta giusta.

Il quantum computing è ancora nelle fasi iniziali: i qubit attuali sono fragili, richiedono temperature prossime allo zero assoluto, e i tassi di errore sono alti. Ma il progresso è rapido e le implicazioni per la statistica e il machine learning potrebbero essere profonde.

---

## Domande di verifica

1. **Qual è l'idea rivoluzionaria introdotta dal modello di von Neumann rispetto ai computer precedenti come l'ENIAC?**

2. **Descrivete le quattro componenti principali del modello di von Neumann e il ruolo di ciascuna.**

3. **Cosa fa ciascuna delle tre fasi del ciclo fetch-decode-execute? Qual è il ruolo del Program Counter?**

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

4. Un dataset occupa 16 GB. La RAM disponibile è di 8 GB. **Cosa succede** quando provate a caricarlo interamente in memoria? Quale componente della gerarchia di memoria entra in gioco e perché le prestazioni degradano?

5. Spiegate con un esempio concreto (non quello del testo) il concetto di **località spaziale** e come la cache ne trae vantaggio.

6. Un programma esegue un ciclo che somma gli elementi di un array di 1.000.000 di numeri. Un altro programma accede a posizioni casuali di un array della stessa dimensione. **Quale dei due sarà più veloce e perché**, anche se entrambi eseguono lo stesso numero di operazioni?

### Avanzato

7. Immaginate di dover calcolare la media di 10 miliardi di numeri. La RAM del vostro computer è di 16 GB e ogni numero occupa 8 byte. **Potete caricare tutti i numeri in RAM?** Se no, progettate (in pseudocodice) un algoritmo che calcoli la media senza caricare tutti i dati in memoria contemporaneamente.

8. Spiegate perché il passaggio da single-core a multi-core non raddoppia automaticamente le prestazioni di un programma. Fate un esempio di un calcolo **parallelizzabile** e uno **non parallelizzabile**.

---

## Osservazioni finali

In questa lezione abbiamo visto come i componenti fisici di un elaboratore — CPU, memoria, bus, dispositivi — si organizzano per eseguire programmi. Il modello di von Neumann, con la sua idea geniale del programma memorizzato, è ancora il fondamento dell'informatica moderna dopo ottant'anni.

Ma abbiamo anche visto i limiti: il collo di bottiglia della memoria, il muro dei GHz, la sfida del parallelismo. Questi limiti non sono fallimenti — sono i motori dell'innovazione. Ogni generazione di ingegneri ha trovato modi creativi per aggirarli: la cache, il pipelining, il multi-core, le GPU, e forse domani il quantum computing.

Per uno statistico, la lezione più importante è pratica: **sapere dove risiedono i vostri dati (RAM, disco, cloud) e come sono organizzati in memoria determina direttamente la velocità delle vostre analisi.** Quando tra qualche lezione userete NumPy e Pandas, ricorderete che la loro velocità non è magia — è architettura.

Nella prossima lezione parleremo del software che gestisce tutto questo: il **sistema operativo**, il "direttore d'orchestra" che permette a programmi, utenti e hardware di convivere.
