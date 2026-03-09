# Introduzione al corso

## Benvenuto

Benvenuti al corso di **Sistemi di Elaborazione 1**, rivolto agli studenti del primo anno di Scienze Statistiche. Questo documento presenta il corso nella sua interezza: cosa imparerete, come si svolge, come viene valutato, e quali strumenti vi serviranno.

Prima di entrare nel merito tecnico, vale la pena rispondere alla domanda che probabilmente vi state ponendo: *perche devo studiare informatica se ho scelto statistica?*

---

## Perche informatica per statistici

La statistica moderna non si fa piu con carta, penna e tavole dei logaritmi. Si fa con macchine che elaborano milioni di osservazioni in frazioni di secondo. Un futuro statistico che non capisce come funziona un elaboratore e come un chirurgo che non conosce l'anatomia: puo seguire le procedure, ma quando qualcosa va storto — e qualcosa va sempre storto — non sa dove guardare.

### Esempi concreti

Pensate a queste situazioni, tutte reali e frequenti:

- State analizzando un dataset con 10 milioni di righe e il programma si blocca. Perche? Forse i dati non stanno in memoria. Ma quanta memoria serve? Come si calcola? Lo vedrete studiando la rappresentazione dei dati e l'architettura degli elaboratori.

- Un calcolo statistico produce un risultato leggermente diverso su due computer. Non e un bug: e un problema di precisione numerica in virgola mobile. Lo capirete studiando come i numeri vengono rappresentati in binario.

- Dovete automatizzare un'analisi che fate ogni settimana su dati aggiornati. Senza saper programmare, la rifate a mano ogni volta. Con Python, scrivete uno script una volta e lo eseguite in un secondo.

- Dovete pulire e trasformare dati provenienti da fonti diverse (CSV, JSON, database). La capacita di scrivere codice per manipolare dati e una competenza fondamentale che nessun foglio di calcolo puo sostituire completamente.

### Cosa imparerete

Al termine del corso sarete in grado di:

- **Comprendere** come raccogliere, archiviare, gestire ed elaborare dati di diversa natura
- **Comprendere** il funzionamento dei moderni sistemi di elaborazione
- **Sviluppare** un pensiero algoritmico: scomporre un problema complesso in passi elementari e risolvibili
- **Scrivere** programmi Python in grado di risolvere problemi di varia natura
- **Organizzare** i dati a seconda dell'esigenza per ottenerne informazione
- **Apprendere** nuovi linguaggi di programmazione in autonomia, partendo dalle basi solide acquisite qui

---

## Struttura del corso

Il corso si articola in **17 lezioni frontali** e **8 laboratori di programmazione**, per un totale di **25 incontri** e **6 CFU**. Questa lezione introduttiva (T00) non rientra nel conteggio ufficiale.

### Parte 1 — Fondamenti (T01-T06)

Le prime sei lezioni costruiscono le basi teoriche dell'informatica:

| Lezione | Argomento |
|---------|-----------|
| T01 | Informazione, bit e numerazione |
| T02 | Logica booleana e storia del calcolo |
| T03 | Architettura degli elaboratori |
| T04 | Sistemi operativi |
| T05 | Rappresentazione dei dati |
| T06 | Dal problema al programma |

Qui imparerete come funziona un computer "sotto il cofano": come rappresenta l'informazione, come ragiona (logica booleana), come è fatto fisicamente (CPU, memoria, bus), come il sistema operativo gestisce il tutto, come i dati vengono codificati in binario e come si passa da un problema a una soluzione algoritmica.

### Parte 2 — Python (T07-T17)

Il cuore pratico del corso: imparare a programmare in Python.

| Lezione | Argomento |
|---------|-----------|
| T07 | Primi passi in Python |
| T08 | Operatori, I/O e condizionali |
| T09 | Cicli |
| T10 | Comprehension e stringhe |
| T11 | Liste e tuple |
| T12 | Dizionari, set e mutabilita |
| T13 | Funzioni: fondamenti |
| T14 | Funzioni avanzate e moduli |
| T15 | File, dati e gestione errori |
| T16 | Programmazione a oggetti |
| T17 | NumPy, Pandas e visualizzazione |

Si parte dalle basi assolute (variabili, tipi, stampa a schermo) e si arriva fino alle librerie scientifiche che userete per tutto il percorso universitario.

### Laboratori (L01-L08)

Otto sessioni pratiche in cui mettete le mani sulla tastiera:

| Laboratorio | Argomento |
|-------------|-----------|
| L01 | Ambiente, variabili e condizionali |
| L02 | Cicli, comprehension e stringhe |
| L03 | Strutture dati |
| L04 | Funzioni e modularita |
| L05 | File e gestione dati |
| L06 | Classi e oggetti |
| L07 | NumPy e Pandas |
| L08 | Visualizzazione e progetto |

I laboratori seguono le lezioni frontali e vi permettono di consolidare ogni argomento con esercizi guidati.

### Corsi collegati

Questo corso e il primo di un percorso che prosegue negli anni successivi:

- **Strutture dati e algoritmi** — I Anno, II Semestre (6 CFU)
- **Sistemi di elaborazione 2** — III Anno, I Semestre (9 CFU)

---

## Modalita d'esame

L'esame si compone di due prove, entrambe **obbligatorie**.

### Prova scritta al PC

- **Durata**: 90 minuti
- **Contenuto**: esercizi di programmazione in Python
- **Modalita**: si svolge in laboratorio informatico (non si usa il proprio PC)
- **Consentiti**: appunti, libri, file personali
- **Non consentiti**: chat, intelligenza artificiale, internet
- **Voto minimo per accedere all'orale**: 17/30
- **Appelli disponibili**: 5 nel corso dell'anno accademico

La prova scritta verifica la vostra capacita di scrivere codice Python funzionante per risolvere problemi concreti. Non si tratta di domande teoriche a risposta multipla, ma di esercizi in cui dovete produrre programmi che vengono poi eseguiti e valutati.

### Prova orale

- **Requisito**: aver superato lo scritto con almeno 17/30
- **Durata**: circa 10-15 minuti
- **Contenuto**: domande di teoria e/o esercizi Python
- **Modalita**: frontale, con eventuale uso di computer
- **Punteggio**: puo modificare il voto dello scritto di **+/- 3 punti**

L'orale serve a verificare la comprensione profonda degli argomenti. Non basta saper scrivere codice: dovete anche saper spiegare *perche* funziona e *come* ragionate.

### Criteri di valutazione

Nello scritto si valutano:

- **Correttezza**: il programma produce l'output atteso?
- **Completezza**: tutti i casi sono gestiti?
- **Stile**: il codice e leggibile, ben organizzato, con nomi di variabili sensati?
- **Efficienza**: la soluzione e ragionevolmente efficiente? (non si richiede ottimizzazione estrema, ma neanche soluzioni inutilmente lente)

---

## Strumenti necessari

Per seguire il corso e fare pratica avrete bisogno di tre strumenti, tutti gratuiti.

### Python 3

Il linguaggio di programmazione che useremo. Scaricatelo dal sito ufficiale:

- **Windows/macOS**: https://www.python.org/downloads/ — scaricate l'ultima versione stabile (3.12 o successiva)
- **Linux**: di solito e gia installato; verificate con `python3 --version` nel terminale

Durante l'installazione su Windows, **spuntate la casella "Add Python to PATH"**: e fondamentale.

### Editor di codice

Vi consiglio **Visual Studio Code** (VS Code), un editor gratuito, potente e molto diffuso:

- **Download**: https://code.visualstudio.com/
- Dopo l'installazione, aggiungete l'estensione **Python** di Microsoft (la trovate nel marketplace delle estensioni)

VS Code vi offre: evidenziazione della sintassi, completamento automatico, esecuzione del codice con un clic, e un terminale integrato. Potete usare anche altri editor (PyCharm, Sublime Text, IDLE), ma le istruzioni del corso faranno riferimento a VS Code.

### Terminale

Il terminale (o "riga di comando") e l'interfaccia testuale del sistema operativo. Lo userete per eseguire i vostri programmi Python.

- **Windows**: cercate "Terminale" o "PowerShell" nel menu Start
- **macOS**: aprite l'applicazione "Terminale" (in Utility)
- **Linux**: di solito si apre con Ctrl+Alt+T

Non preoccupatevi se non avete mai usato un terminale: lo vedrete in dettaglio nel primo laboratorio.

---

## Riferimenti e risorse

### Contatti del docente

- **Email**: nicola.salmaso@unipd.it
- **Ricevimento**: https://unipd.zoom.us/my/nicola.salmaso

### Piattaforma del corso

Lezioni, materiale e annunci sono pubblicati su Moodle:

- https://stem.elearning.unipd.it/course/view.php?id=12908

### Libro di testo

- Horstmann, Cay; Necaise, Rance D.; Dalpasso, Marcello — *Concetti di informatica e fondamenti di Python*

### Portale web del corso

Su questo portale trovate tutto il materiale organizzato per lezione:

- **Presentazioni** (slides): le stesse usate a lezione, navigabili nel browser
- **Dispense**: versione narrativa e approfondita di ogni lezione
- **Codice**: esempi ed esercizi Python scaricabili
- **Autovalutazione**: quiz per verificare la propria comprensione
- **Errori comuni**: raccolta degli errori piu frequenti con spiegazioni
- **Schede di confronto**: tabelle riassuntive su strutture dati, operatori, ecc.
- **Mini-progetti guidati**: progetti completi per mettere insieme piu argomenti
- **Glossario**: definizioni dei termini tecnici usati nel corso
- **Cheatsheet Python**: riferimento rapido della sintassi

---

## Consigli pratici per lo studio

Programmare e un'abilita pratica, come suonare uno strumento o imparare una lingua. Non si impara solo leggendo o guardando: si impara **facendo**. Ecco alcuni consigli basati sull'esperienza.

### Programmate ogni giorno

Anche solo 20-30 minuti al giorno sono piu efficaci di una maratona di 8 ore il giorno prima dell'esame. La programmazione richiede che certi schemi mentali diventino automatici, e questo avviene solo con la pratica regolare.

### Non copiate

Copiare codice da un compagno o da internet senza capirlo e il modo piu sicuro per fallire l'esame. Potete (e dovete) leggere codice altrui, studiare soluzioni, chiedere aiuto — ma poi dovete essere in grado di riscrivere la soluzione da soli, senza guardare.

### Sbagliare e normale

Nessun programmatore, nemmeno il piu esperto, scrive codice corretto al primo tentativo. Gli errori non sono un segno di incapacita: sono il meccanismo fondamentale dell'apprendimento. Quando il programma non funziona, leggete il messaggio di errore con attenzione: Python e piuttosto bravo a dirvi cosa e andato storto e dove.

### Usate le risorse del corso

Le dispense, gli esercizi, le autovalutazioni e gli errori comuni sono stati progettati per accompagnarvi passo dopo passo. Non saltate gli esercizi pensando "questo lo so gia fare": provatelo davvero, e verificate che il vostro codice produca il risultato corretto.

### Fate domande

Se qualcosa non e chiaro, chiedete. A lezione, in laboratorio, via email, al ricevimento. Non esiste una domanda stupida — esiste solo il rischio di restare indietro in silenzio.

---

## Prossimi passi

Nella prossima lezione (T01) entreremo nel vivo del corso, partendo dalle fondamenta teoriche: cos'e l'informazione, come si misura, e come i computer rappresentano i numeri. Preparatevi installando Python e VS Code, cosi al primo laboratorio sarete gia pronti per scrivere il vostro primo programma.

Buon corso a tutti!
