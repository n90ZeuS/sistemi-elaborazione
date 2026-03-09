# Lezione Frontale 4 — Sistemi operativi e software di sistema

## Introduzione

Nelle lezioni precedenti abbiamo costruito un elaboratore pezzo per pezzo: bit, porte logiche, CPU, memoria, bus. Abbiamo una macchina potentissima ma completamente "nuda". Se la accendeste ora, non fareste nulla: non c'è nessuno che gestisca le risorse, che vi permetta di interagire, che coordini l'esecuzione dei programmi. Manca il **software di sistema** — e il suo componente più importante è il **sistema operativo**.

Il sistema operativo è il programma più importante che non vedrete mai. Lavora silenziosamente sotto ogni cosa che fate al computer: quando aprite un file, quando navigare in internet, quando eseguite uno script Python, quando Jupyter Notebook mostra un grafico. Capire cosa fa e come lo fa vi darà una comprensione profonda del funzionamento reale delle macchine con cui lavorate ogni giorno.

---

## Perché serve un sistema operativo

Immaginate di avere un'orchestra con cento musicisti, decine di strumenti diversi e un programma di brani da eseguire. Senza un direttore d'orchestra, il risultato sarebbe il caos: chi suona quando? Chi aspetta chi? Come si gestisce il fatto che c'è un solo pianoforte ma tre pianisti?

Il sistema operativo è il direttore d'orchestra del computer. I musicisti sono i programmi, gli strumenti sono le risorse hardware (CPU, memoria, disco, rete), e il direttore deve garantire che tutto funzioni armoniosamente.

### Le funzioni fondamentali

Un sistema operativo svolge quattro ruoli essenziali:

**1. Astrazione dell'hardware.** L'hardware è complesso e diversificato: esistono centinaia di modelli di dischi, schede di rete, schermi, ognuno con le sue peculiarità. Il sistema operativo li nasconde dietro un'interfaccia uniforme. Quando in Python scrivete `open("dati.csv")`, non dovete sapere se il file è su un SSD Samsung o un HDD Seagate, se usa il file system NTFS o ext4. Il sistema operativo se ne occupa.

**2. Gestione delle risorse.** La CPU è una, la RAM è limitata, il disco è condiviso. Ma voi volete eseguire contemporaneamente il browser, Spotify, VS Code e un calcolo Python. Chi decide quanto tempo di CPU tocca a ciascun programma? Chi assegna la memoria? Chi evita che un programma sovrascriva i dati di un altro? Il sistema operativo.

**3. Interfaccia utente.** Il sistema operativo fornisce il modo in cui interagite con il computer: la riga di comando (terminale), l'interfaccia grafica (finestre, icone, menu), il touch screen. Senza di esso, dovreste comunicare in codice macchina.

**4. Sicurezza e protezione.** Ogni programma vive in uno spazio isolato: non può accedere alla memoria degli altri programmi, non può scrivere su file per cui non ha i permessi, non può prendere il controllo totale della macchina (a meno che non sia il sistema operativo stesso). Questa protezione è fondamentale: un bug in un programma non deve poter distruggere l'intero sistema.

---

## Una breve storia dei sistemi operativi

La storia dei sistemi operativi è affascinante perché riflette l'evoluzione del rapporto tra gli esseri umani e le macchine.

### L'era batch (anni '50-'60)

I primi computer non avevano un sistema operativo nel senso moderno. I programmatori scrivevano i programmi su **schede perforate** — cartoncini con fori che codificavano le istruzioni. Le schede venivano consegnate a un operatore, che le caricava nella macchina. Il computer eseguiva il programma, stampava i risultati, e passava al programma successivo. Non c'era nessuna interazione: si consegnava il lavoro la mattina e si ritiravano i risultati il giorno dopo (se tutto andava bene).

I primi sistemi operativi nacquero proprio per automatizzare questo processo: caricare un programma, eseguirlo, caricare il successivo. Si chiamavano **sistemi batch** (a lotti) perché elaboravano un "lotto" di programmi in sequenza.

### Il time-sharing (anni '60-'70)

L'idea rivoluzionaria del **time-sharing** (condivisione del tempo) cambiò tutto: invece di dedicare l'intera macchina a un utente alla volta, il sistema operativo suddivideva il tempo della CPU tra molti utenti, dando a ciascuno l'illusione di avere il computer tutto per sé. Ogni utente aveva un terminale (schermo e tastiera) collegato al computer centrale.

Il progetto più ambizioso fu **Multics** (1964-69), nato dalla collaborazione tra MIT, Bell Labs e General Electric. Multics era straordinariamente avanzato per l'epoca: supportava molti utenti contemporanei, aveva un file system gerarchico, gestiva la sicurezza. Ma era anche enormemente complesso. Quando Bell Labs abbandonò il progetto, due dei suoi ricercatori — **Ken Thompson** e **Dennis Ritchie** — presero le idee migliori di Multics e le semplificarono radicalmente. Il risultato fu **Unix**.

### Unix (1969)

Unix è forse il sistema operativo più influente della storia. Nato nel 1969 ai Bell Labs, si fondava su principi che sono ancora oggi considerati paradigmatici:

- **"Fare una cosa sola e farla bene":** ogni strumento (programma) deve svolgere un compito specifico e farlo eccellentemente. La potenza nasce dalla combinazione di strumenti semplici (attraverso i *pipe*, le "tubature" che collegano l'output di un programma all'input di un altro).

- **"Tutto è un file":** dispositivi hardware, connessioni di rete, processi — tutto viene rappresentato come un file. Questo rende l'interfaccia uniforme e composibile.

- **Portabilità:** nel 1973, Thompson e Ritchie riscrissero Unix in **C** (un linguaggio ad alto livello creato da Ritchie stesso), rendendolo indipendente dalla specifica macchina. Prima, i sistemi operativi erano scritti in assembly per un'architettura specifica. Dopo Unix, un sistema operativo poteva essere portato su macchine diverse ricompilando il codice.

Da Unix discende un'intera famiglia di sistemi operativi: BSD, Solaris, macOS (il Mac usa un kernel derivato da BSD), Linux, Android. La filosofia Unix pervade anche gli strumenti moderni di sviluppo software.

### L'era dei personal computer

Con la nascita dei personal computer alla fine degli anni '70, servivano sistemi operativi adatti a utenti non specialisti:

- **MS-DOS** (1981): il sistema operativo testuale che IBM scelse per i suoi PC, fornito da una giovane Microsoft. Riga di comando, niente grafica, un solo programma alla volta.
- **Windows** (dal 1985): l'interfaccia grafica sopra MS-DOS, che evolse fino a diventare un sistema operativo completo. Oggi domina il mercato desktop (~72%).
- **Macintosh** (1984): Apple introdusse l'interfaccia grafica con mouse e icone per il grande pubblico (ispirata dal lavoro di Xerox PARC). Evolse in **macOS**, che sotto la superficie è un sistema Unix.

### Linux (1991)

Nel 1991, **Linus Torvalds**, studente finlandese di 21 anni, pubblicò su un newsgroup un messaggio che iniziava con: *"Sto facendo un sistema operativo (gratis) (solo un hobby, non sarà grande e professionale come gnu)"*. Quel "hobby" è diventato **Linux**, il sistema operativo open-source che:

- Fa girare il **96% dei server mondiali** (compresi quelli di Google, Amazon, Facebook).
- Alimenta **tutti** i primi 500 supercomputer del mondo.
- È alla base di **Android** (il sistema operativo mobile più diffuso al mondo, con oltre 3 miliardi di dispositivi).
- Costituisce la spina dorsale del **cloud computing** (AWS, Google Cloud, Azure usano Linux).

La forza di Linux sta nel suo modello di sviluppo: il codice sorgente è pubblico e chiunque può contribuire. Migliaia di sviluppatori nel mondo collaborano per migliorarlo. È gratuito, robusto, flessibile e trasparente. Per un ricercatore, sapere che il software su cui girano le proprie analisi è ispezionabile e verificabile è un valore enorme.

---

## Gestione dei processi

### Cos'è un processo

Quando eseguite un programma Python, il sistema operativo crea un **processo**: un'istanza del programma in esecuzione, con il proprio spazio di memoria, il proprio stato, le proprie risorse. Lo stesso programma può generare più processi indipendenti (ad esempio, potete aprire due terminali e lanciare due script Python diversi contemporaneamente — sono due processi distinti).

Ogni processo ha:
- Uno **spazio di indirizzamento** privato (la sua porzione di memoria, isolata dagli altri).
- Uno **stato** (in esecuzione, in attesa, terminato).
- Un **identificatore** univoco (PID, *Process ID*).
- Risorse associate (file aperti, connessioni di rete, ecc.).

### Multitasking

Il vostro computer sembra eseguire molti programmi contemporaneamente: browser, editor, player musicale, script Python, decine di processi di sistema. Ma se avete, per esempio, 8 core, al massimo 8 processi possono essere realmente in esecuzione nello stesso istante. Come è possibile l'illusione della simultaneità?

La risposta è lo **scheduling**: il sistema operativo assegna a ogni processo brevi "fette di tempo" (*time slice*) sulla CPU, tipicamente di pochi millisecondi. Il processore salta da un processo all'altro talmente velocemente che l'utente percepisce tutti i programmi come simultanei. Questa tecnica si chiama **multitasking preemptivo** ("preemptivo" perché è il sistema operativo a decidere quando interrompere un processo, non il processo stesso).

Gli algoritmi di scheduling devono bilanciare obiettivi contrastanti: dare tempo a tutti i processi (equità), rispondere rapidamente all'utente (reattività), massimizzare l'uso della CPU (efficienza). Un algoritmo classico è il **round-robin**: ogni processo riceve la stessa fetta di tempo, a turno, in ordine circolare. Nella pratica, i sistemi moderni usano algoritmi più sofisticati basati su **priorità**: i processi interattivi (come l'interfaccia grafica) hanno priorità alta per garantire reattività, i processi di calcolo pesante hanno priorità più bassa.

### Cenni su thread e concorrenza

Un **thread** (filo) è un'unità di esecuzione all'interno di un processo. Un processo può contenere più thread che condividono lo stesso spazio di memoria ma hanno ciascuno il proprio flusso di esecuzione. I thread sono più "leggeri" dei processi (creare un thread è molto meno costoso che creare un processo).

Condividere la memoria è un vantaggio (comunicazione veloce tra thread) ma anche un rischio: se due thread modificano lo stesso dato contemporaneamente, il risultato può essere imprevedibile. Questo problema si chiama **race condition** (condizione di corsa) ed è una delle fonti di bug più insidiose nel software concorrente.

**Applicazione per Python:** Python ha una particolarità chiamata **GIL** (*Global Interpreter Lock*): un blocco che impedisce a più thread Python di eseguire bytecode contemporaneamente. Il GIL semplifica la gestione della memoria di CPython ma limita il parallelismo. Per aggirare il GIL, si usa il modulo `multiprocessing` (processi separati invece di thread) o librerie che eseguono codice C/Fortran in parallelo (come NumPy).

---

## Gestione della memoria

### Memoria virtuale

Ogni processo "crede" di avere a disposizione un'enorme spazio di memoria tutto per sé, che parte dall'indirizzo 0 e arriva fino a un massimo (ad esempio, 256 TB in un sistema a 64 bit). Questa è la **memoria virtuale**: un'illusione creata dal sistema operativo.

In realtà, la memoria fisica (RAM) è condivisa tra tutti i processi. Il sistema operativo, con l'aiuto dell'hardware (la **MMU**, *Memory Management Unit*), traduce gli indirizzi virtuali usati dal processo negli indirizzi fisici reali della RAM. Questa traduzione è trasparente: il programma non sa (e non deve sapere) dove i suoi dati risiedono fisicamente.

### Paginazione

La memoria virtuale è divisa in blocchi di dimensione fissa chiamati **pagine** (tipicamente 4 KB). Anche la RAM fisica è divisa in blocchi della stessa dimensione, chiamati **frame**. Il sistema operativo mantiene una tabella che mappa ogni pagina virtuale al frame fisico corrispondente.

Non tutte le pagine di un processo devono essere in RAM contemporaneamente: le pagine non usate di recente possono essere spostate su disco (in un'area chiamata **swap**). Quando il processo cerca di accedere a una pagina che non è in RAM, si verifica un **page fault**: il sistema operativo sospende il processo, carica la pagina dal disco nella RAM, aggiorna la tabella di traduzione e riprende il processo. Tutto questo avviene automaticamente e in modo trasparente.

### Perché il computer rallenta

Ora capite perché il computer rallenta quando avete troppi programmi aperti: quando la RAM è satura, il sistema operativo deve continuamente spostare pagine dalla RAM al disco e viceversa (*thrashing*). Poiché il disco è migliaia di volte più lento della RAM, tutto diventa lentissimo. Il famoso `MemoryError` di Python si verifica quando il processo richiede più memoria di quanta il sistema sia disposto ad allocargli.

---

## Il file system

### Organizzazione logica

Il file system è il modo in cui il sistema operativo organizza i dati sul disco. L'astrazione fondamentale è semplice e familiare:

- **File:** un contenitore di dati con un nome. Può essere un documento, un'immagine, un programma, un dataset CSV.
- **Directory (cartella):** un contenitore di file e altre directory, creando una struttura **gerarchica** (ad albero).

Ogni file ha dei **metadati**: nome, dimensione, data di creazione, data di ultima modifica, permessi di accesso (chi può leggere, scrivere, eseguire).

### Percorsi assoluti e relativi

Per identificare un file nel file system, si usa un **percorso** (*path*):

- **Percorso assoluto:** parte dalla radice del file system e specifica l'intera posizione.
  - Unix/macOS: `/home/nicola/dati/studenti.csv` (la radice è `/`)
  - Windows: `C:\Users\nicola\dati\studenti.csv` (la radice è `C:\`)

- **Percorso relativo:** parte dalla directory corrente.
  - Se siete in `/home/nicola/`, il percorso relativo per lo stesso file è `dati/studenti.csv`.

Notate la differenza nel separatore: Unix usa `/` (slash), Windows usa `\` (backslash). Questa differenza apparentemente banale è fonte di infiniti problemi di compatibilità. In Python, il modulo `pathlib` risolve il problema: `Path("dati") / "studenti.csv"` funziona correttamente su entrambi i sistemi.

### File system diversi

Sistemi operativi diversi usano file system diversi:

- **NTFS:** il file system di Windows. Supporta permessi, crittografia, file di grandi dimensioni.
- **ext4:** il file system standard di Linux. Robusto, efficiente, ben collaudato.
- **APFS (Apple File System):** il file system di macOS e iOS. Ottimizzato per SSD, supporta crittografia nativa.
- **FAT32/exFAT:** file system semplici, supportati da praticamente tutti i sistemi operativi. Per questo le chiavette USB usano FAT32 o exFAT: compatibilità universale. FAT32 ha un limite di 4 GB per singolo file.

---

## Reti e internet

### Il problema della comunicazione

Quando due computer devono comunicare, servono regole condivise: come iniziare la conversazione, come formattare i messaggi, come gestire gli errori, come terminare. Queste regole si chiamano **protocolli**.

### Il modello a livelli

La comunicazione di rete è organizzata a **livelli** (layer), ciascuno con una responsabilità specifica. L'analogia più intuitiva è quella postale: per spedire una lettera, la scrivete (contenuto), la mettete in una busta con l'indirizzo (instradamento), la portate all'ufficio postale (trasporto), che la affida al corriere (trasmissione fisica). Ogni livello "incapsula" il messaggio del livello superiore.

Il protocollo fondamentale di internet è **TCP/IP**:

- **IP (Internet Protocol):** si occupa dell'instradamento: ogni dispositivo ha un indirizzo IP (es: `192.168.1.100`), e IP trova la strada per far arrivare i pacchetti a destinazione.
- **TCP (Transmission Control Protocol):** si occupa dell'affidabilità: garantisce che i dati arrivino completi, nell'ordine giusto, senza errori. Se un pacchetto si perde, TCP lo ritrasmette.

### HTTP e il World Wide Web

**HTTP** (*HyperText Transfer Protocol*) è il protocollo che fa funzionare il web. Il modello è semplice:

1. Il **client** (il vostro browser) invia una **richiesta** al server ("dammi la pagina X").
2. Il **server** risponde con i dati (la pagina HTML, un'immagine, un file JSON).

**HTTPS** è la versione crittografata di HTTP: i dati viaggiano cifrati, proteggendo la privacy e l'integrità della comunicazione.

### Internet vs World Wide Web

È importante distinguere:

- **Internet** è l'infrastruttura: la rete globale di reti, i cavi, i router, i protocolli (TCP/IP). Esiste dal 1969 (ARPANET).
- **Il World Wide Web** è un servizio che funziona *sopra* internet: pagine collegate da link ipertestuali. Fu inventato da **Tim Berners-Lee** nel 1989 al CERN di Ginevra, per permettere ai fisici di condividere documenti.

### Cloud computing

Il "cloud" non è una nuvola magica: sono **i computer di qualcun altro**, ospitati in enormi data center sparsi nel mondo. Quando usate Google Colab per eseguire un notebook Python, il vostro codice gira su un server Google, non sul vostro computer.

Il cloud si divide in livelli di servizio:
- **IaaS** (Infrastructure as a Service): vi danno macchine virtuali (AWS EC2, Google Compute Engine).
- **PaaS** (Platform as a Service): vi danno un ambiente pronto per eseguire codice (Heroku, Google App Engine).
- **SaaS** (Software as a Service): vi danno un'applicazione completa (Gmail, Google Docs, Dropbox).

### API (Application Programming Interface)

Le **API** sono interfacce che permettono ai programmi di parlare tra loro. Quando il vostro script Python scarica dati dall'ISTAT o da Eurostat, sta usando un'API: invia una richiesta HTTP a un server, riceve una risposta (tipicamente in formato JSON) e la elabora.

Le API sono fondamentali per la statistica moderna: permettono di raccogliere dati in modo automatizzato, riproducibile e aggiornato, senza dover scaricare file manualmente da siti web.

---

## Domande di verifica

1. **Quali sono le quattro funzioni fondamentali di un sistema operativo?** Spiegate ciascuna con un esempio concreto.

2. **Cosa distingue un sistema batch da un sistema time-sharing?** Quale problema risolve il time-sharing?

3. **Quali principi fondamentali caratterizzano la filosofia di Unix?** Perché sono stati così influenti?

4. **Qual è la differenza tra un processo e un thread?** Cos'è una race condition?

5. **Cos'è la memoria virtuale e quale problema risolve?** Cosa succede quando la RAM è satura?

6. **Spiegate la differenza tra percorso assoluto e percorso relativo.** Perché Python offre il modulo `pathlib`?

7. **Qual è la differenza tra internet e il World Wide Web?**

8. **Cos'è un'API e perché è rilevante per uno statistico?** Fate un esempio concreto.

---

## Esercizi

### Base

1. Aprite il **Task Manager** (Windows) o **Activity Monitor** (macOS) o il comando `top`/`htop` (Linux). Identificate:
   - Quanti processi sono in esecuzione.
   - Quanto CPU e RAM sta usando il vostro sistema.
   - Qual è il processo che consuma più memoria.

2. Aprite il **terminale** (o il prompt dei comandi) e navigate il file system usando i comandi base:
   - `pwd` (mostra la directory corrente)
   - `ls` (elenca i file nella directory corrente)
   - `cd nome_directory` (entra in una directory)
   - `cd ..` (torna alla directory padre)
   - Scrivete il percorso assoluto della vostra home directory.

3. Indicate quale file system usa il vostro computer e quale file system usa una chiavetta USB. Perché sono diversi?

### Intermedio

4. Spiegate cosa succede, passo per passo, dal punto di vista del sistema operativo quando fate doppio clic su un file Python (.py):
   - Quale processo viene creato?
   - Come viene allocata la memoria?
   - Cosa succede quando lo script termina?

5. Avete un server con 4 core e 10 processi da eseguire, ciascuno richiede 1 secondo di CPU. Stimate il tempo totale di completamento con uno scheduling round-robin (fetta di tempo: 100 ms). Confrontatelo con l'esecuzione sequenziale.

### Avanzato

6. Spiegate perché Linux domina il mercato dei server e del cloud computing, mentre Windows domina il mercato desktop. Quali fattori tecnici, economici e storici contribuiscono a questa divisione?

7. Un data scientist usa Google Colab per addestrare un modello di machine learning. Descrivete tutti i livelli di software (dal sistema operativo del suo portatile al server Google) che sono coinvolti quando clicca "Run" su una cella del notebook.

---

## Osservazioni finali

Il sistema operativo è il ponte tra l'hardware — che abbiamo studiato nella lezione precedente — e il software applicativo che scriveremo nelle lezioni successive. È il software che rende il computer utilizzabile, trasformando un ammasso di circuiti in uno strumento produttivo.

Tre lezioni da portare a casa:

1. **L'astrazione è potenza.** Il sistema operativo nasconde l'enorme complessità dell'hardware dietro interfacce semplici. Quando in Python scriverete `open("file.csv")`, decine di strati di software si attiveranno sotto di voi: dal file system al driver del disco, dal sistema di permessi alla cache del sistema operativo. Non dovrete sapere nulla di tutto questo — ma ora sapete che esiste.

2. **Le risorse sono limitate e condivise.** CPU, memoria, disco, rete: tutto è finito e conteso tra i processi. Capire questo vi aiuterà a scrivere programmi più efficienti e a diagnosticare problemi di prestazioni.

3. **La storia conta.** Le scelte progettuali fatte negli anni '60 e '70 (Unix, TCP/IP, il file system gerarchico) sono ancora le fondamenta del software moderno. Capire *perché* le cose sono fatte così vi rende utenti e programmatori più consapevoli.

Nella prossima lezione affronteremo un tema cruciale per la statistica: come i computer rappresentano i dati — numeri, testo, immagini — e le trappole che si nascondono in queste rappresentazioni.
