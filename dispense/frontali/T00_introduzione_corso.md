# Introduzione al corso

## Benvenuto

Benvenuti al corso di **Sistemi di Elaborazione 1**, rivolto agli studenti del primo anno di Scienze Statistiche. Questo documento presenta il corso nella sua interezza: cosa imparerete, come si svolge, come viene valutato, e quali strumenti vi serviranno.

La prima sezione spiega perché l'informatica serve a chi studia statistica.

---

## Perché informatica per statistici

Oggi le analisi statistiche si fanno al computer, su insiemi di dati che possono contenere milioni di osservazioni elaborate in frazioni di secondo. Chi usa questi strumenti senza sapere come funziona un elaboratore può seguire le procedure, ma quando un risultato è sbagliato fatica a capire dove cercare l'errore.

### Casi reali

- **Ottobre 2020, Inghilterra.** 15.841 casi positivi al COVID non sono entrati nel conteggio ufficiale per circa una settimana. I risultati dei test passavano per un file in formato `.xls`, che accetta al massimo 65.536 righe: le righe in eccesso sono state scartate senza avvisi. I limiti dei formati e della rappresentazione dei dati sono l'argomento di T05.

- **Numeri decimali.** In Python l'espressione `0.1 + 0.2 == 0.3` restituisce `False`. Il valore 0,1 non ha una rappresentazione esatta in binario, quindi la somma vale 0.30000000000000004. Per confrontare numeri decimali si usa una tolleranza, per esempio `math.isclose`. Lo vedrete studiando la virgola mobile.

- **Nomi di geni trasformati in date.** Excel interpreta alcuni nomi di geni come date: SEPT2 diventa 2-set, MARCH1 diventa 1-mar. Uno studio del 2016 ha trovato questo errore in circa un quinto degli articoli di genomica che allegavano liste di geni in Excel. In un programma i tipi di dato si dichiarano e si controllano esplicitamente.

- **Un errore in un foglio di calcolo.** Nel 2013 uno studente di dottorato ha provato a rifare i calcoli di un articolo di economia molto citato (Reinhart e Rogoff, sul rapporto tra debito pubblico e crescita). Ha trovato una formula Excel che escludeva cinque paesi dalla media. Un'analisi scritta come script si può rieseguire e controllare riga per riga.

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

Queste sei lezioni costruiscono le basi teoriche dell'informatica:

| Lezione | Argomento |
|---------|-----------|
| T01 | Informazione, bit e numerazione |
| T02 | Logica booleana e storia del calcolo |
| T03 | Architettura degli elaboratori |
| T04 | Sistemi operativi |
| T05 | Rappresentazione dei dati |
| T06 | Dal problema al programma |

Qui imparerete come funziona un computer "sotto il cofano": come rappresenta l'informazione, come ragiona (logica booleana), come è fatto fisicamente (CPU, memoria, bus), come il sistema operativo gestisce il tutto, come i dati vengono codificati in binario e come si passa da un problema a una soluzione algoritmica.

L'ordine in cui si svolgono non segue la numerazione: T06 si tiene a ottobre, prima delle lezioni di Python, mentre T04 e T05 si tengono a dicembre, dopo T15. Il calendario aggiornato è sul portale.

### Parte 2 — Python (T07-T17)

La seconda parte insegna a programmare in Python.

| Lezione | Argomento |
|---------|-----------|
| T07 | Primi passi in Python |
| T08 | Operatori, I/O e condizionali |
| T09 | Cicli |
| T10 | Comprehension e stringhe |
| T11 | Liste e tuple |
| T12 | Dizionari, set e mutabilità |
| T13 | Funzioni: fondamenti |
| T14 | Funzioni avanzate e moduli |
| T15 | File, dati e gestione errori |
| T16 | Programmazione a oggetti |
| T17 | NumPy, Pandas e visualizzazione |

Si parte dalle basi (variabili, tipi, stampa a schermo) e si arriva alle librerie scientifiche che userete nel resto del percorso universitario.

### Laboratori (L01-L08)

Otto sessioni pratiche in cui scrivete ed eseguite programmi al computer:

| Laboratorio | Argomento |
|-------------|-----------|
| L01 | Ambiente, variabili e condizionali |
| L02 | Cicli, comprehension e stringhe |
| L03 | Strutture dati |
| L04 | Funzioni e modularità |
| L05 | File e gestione dati |
| L06 | Classi e oggetti |
| L07 | NumPy e Pandas |
| L08 | Visualizzazione e progetto |

I laboratori seguono le lezioni frontali e vi permettono di consolidare ogni argomento con esercizi guidati.

Gli argomenti dei laboratori e delle ultime lezioni potrebbero cambiare durante il corso. Il portale riporta sempre la versione aggiornata.

### Corsi collegati

Questo corso è il primo di un percorso che prosegue negli anni successivi:

- **Strutture dati e algoritmi** — I Anno, II Semestre (6 CFU)
- **Sistemi di elaborazione 2** — III Anno, I Semestre (9 CFU)

---

## Modalità d'esame

L'esame si compone di due prove, entrambe **obbligatorie**: una prova scritta al PC e un quiz di teoria.

### Prova scritta al PC

- **Durata**: 90 minuti
- **Contenuto**: esercizi di programmazione in Python
- **Modalità**: si svolge in laboratorio informatico (non si usa il proprio PC)
- **Consentiti**: appunti, libri, file personali
- **Non consentiti**: chat, intelligenza artificiale, internet
- **Appelli disponibili**: 5 nel corso dell'anno accademico

La prova scritta verifica la vostra capacità di scrivere codice Python funzionante per risolvere problemi concreti. Non si tratta di domande teoriche a risposta multipla, ma di esercizi in cui dovete produrre programmi che vengono poi eseguiti e valutati.

### Quiz di teoria

- **Novità**: con buona probabilità il quiz sostituisce la prova orale degli anni precedenti
- **Contenuto**: domande sugli argomenti di teoria del corso
- **Punteggio**: da definire; le regole saranno comunicate sul portale e su Moodle prima del primo appello

### Criteri di valutazione

Nello scritto si valutano:

- **Correttezza**: il programma produce l'output atteso?
- **Completezza**: tutti i casi sono gestiti?
- **Stile**: il codice è leggibile, ben organizzato, con nomi di variabili sensati?
- **Efficienza**: la soluzione è ragionevolmente efficiente? (non si richiede ottimizzazione estrema, ma neanche soluzioni inutilmente lente)

---

## Strumenti necessari

Per seguire il corso e fare pratica avrete bisogno di tre strumenti, tutti gratuiti.

### Python 3

Il linguaggio di programmazione che useremo. Scaricatelo dal sito ufficiale:

- **Windows/macOS**: https://www.python.org/downloads/ — scaricate l'ultima versione stabile (3.12 o successiva)
- **Linux**: di solito è già installato; verificate con `python3 --version` nel terminale

Durante l'installazione su Windows, **spuntate la casella "Add Python to PATH"**: senza questa opzione il terminale non trova il comando `python`.

### Editor di codice

Vi consiglio **Visual Studio Code** (VS Code), un editor gratuito e molto diffuso:

- **Download**: https://code.visualstudio.com/
- Dopo l'installazione, aggiungete l'estensione **Python** di Microsoft (la trovate nel marketplace delle estensioni)

VS Code vi offre: evidenziazione della sintassi, completamento automatico, esecuzione del codice con un clic, e un terminale integrato. Potete usare anche altri editor (PyCharm, Sublime Text, IDLE), ma le istruzioni del corso faranno riferimento a VS Code.

### Terminale

Il terminale (o "riga di comando") è l'interfaccia testuale del sistema operativo. Lo userete per eseguire i vostri programmi Python.

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
- **Errori comuni**: raccolta degli errori più frequenti con spiegazioni
- **Schede di confronto**: tabelle riassuntive su strutture dati, operatori, ecc.
- **Mini-progetti guidati**: progetti completi per mettere insieme più argomenti
- **Glossario**: definizioni dei termini tecnici usati nel corso
- **Cheatsheet Python**: riferimento rapido della sintassi

---

## Consigli pratici per lo studio

Programmare è un'abilità pratica, come suonare uno strumento o imparare una lingua: oltre a leggere e ascoltare, bisogna esercitarsi scrivendo codice. Ecco alcuni consigli.

### Programmate ogni giorno

Anche solo 20-30 minuti al giorno sono più efficaci di una maratona di 8 ore il giorno prima dell'esame. La programmazione richiede che certi schemi mentali diventino automatici, e questo avviene solo con la pratica regolare.

### Non copiate

Copiare codice da un compagno o da internet senza capirlo non prepara all'esame, dove le soluzioni vanno scritte da soli. Potete (e dovete) leggere codice altrui, studiare soluzioni, chiedere aiuto — ma poi dovete essere in grado di riscrivere la soluzione da soli, senza guardare.

### Sbagliare è normale

Nessun programmatore, nemmeno il più esperto, scrive codice corretto al primo tentativo: correggere gli errori fa parte del lavoro. Quando il programma non funziona, leggete il messaggio di errore: Python indica il tipo di errore e la riga in cui si è verificato.

### Usate le risorse del corso

Le dispense, gli esercizi, le autovalutazioni e gli errori comuni sono stati progettati per accompagnarvi passo dopo passo. Non saltate gli esercizi pensando "questo lo so già fare": provateli e verificate che il vostro codice produca il risultato corretto.

### Fate domande

Se qualcosa non è chiaro, chiedete: a lezione, in laboratorio, via email o al ricevimento.

---

## Prossimi passi

Subito dopo questa introduzione inizia T01, la prima lezione di teoria: che cos'è l'informazione, come si misura e come i computer rappresentano i numeri. Prima del primo laboratorio installate Python e VS Code, così potrete scrivere subito il vostro primo programma.

Buon corso a tutti!
