# Lezione 1 — Informazione, bit e sistemi di numerazione

## Perché questo corso

Nell'introduzione (T00) abbiamo visto perché uno studente di Scienze Statistiche studia come funziona un computer: le analisi statistiche si fanno con macchine che elaborano milioni di osservazioni in frazioni di secondo, e quando un risultato è sbagliato o un calcolo non termina bisogna sapere dove cercare la causa.

Il corso parte dai fondamenti dell'informazione, passa per l'architettura delle macchine e arriva alla programmazione. Non vi chiediamo di diventare ingegneri informatici, ma di capire come i dati vengono rappresentati ed elaborati dentro un computer. Questo vi servirà per capire perché un calcolo è lento, perché un numero perde precisione, perché un dataset non sta in memoria, e per imparare a ragionare in modo algoritmico, cioè a scomporre un problema in passi elementari e risolvibili.

Il primo argomento è l'informazione.

---

## Che cos'è l'informazione

Nella vita quotidiana usiamo la parola "informazione" in modo intuitivo: un messaggio, una notizia, un dato. In informatica e in teoria della comunicazione questa parola ha un significato preciso, e per arrivarci bisogna partire dal concetto di **incertezza**.

Immaginate di lanciare una moneta. Prima del lancio non sapete se uscirà testa o croce: siete in uno stato di incertezza. Dopo il lancio osservate il risultato e l'incertezza si annulla. In questo senso **l'informazione è ciò che riduce l'incertezza**: più siete incerti prima, più informazione ricevete dopo.

Se la moneta è truccata ed esce sempre testa, il lancio non vi dice nulla di nuovo: l'informazione è zero. Se invece la moneta è equilibrata, ogni lancio fornisce la massima quantità di informazione possibile per un evento con due esiti. Questa quantità si chiama **bit**.

### Il bit

La parola "bit" è una contrazione di *binary digit*, cifra binaria. Un bit è la quantità di informazione necessaria per distinguere tra due alternative equiprobabili: sì/no, vero/falso, 0/1, acceso/spento. È l'unità di misura dell'informazione digitale.

Un esempio: se vi dico "ho pensato un numero tra 1 e 8" e potete fare domande a cui rispondo solo sì o no, quante domande vi servono per indovinare? Tre. Con la prima dimezzate le possibilità (1-4 o 5-8?), con la seconda le dimezzate ancora (per esempio 1-2 o 3-4?), con la terza arrivate al numero. Tre domande, tre bit di informazione. In generale, per distinguere tra N alternative equiprobabili servono log_2(N) bit; se N non è una potenza di 2, per codificarle servono log_2(N) arrotondato per eccesso bit (per esempio, 10 alternative richiedono 4 bit).

---

## Claude Shannon e la nascita della teoria dell'informazione

Nel 1948 un ingegnere di 32 anni che lavorava ai Bell Telephone Laboratories, **Claude Elwood Shannon**, pubblicò l'articolo *"A Mathematical Theory of Communication"*. In quel lavoro Shannon trasformò il concetto intuitivo di "informazione" in una grandezza misurabile, con un'unità di misura e delle formule.

Shannon non si occupava del *significato* dei messaggi: che una frase parlasse di poesia o di bulloni era irrilevante. Il suo problema era ingegneristico: come trasmettere messaggi in modo affidabile attraverso un canale rumoroso (un filo telefonico, un'onda radio). Per farlo doveva quantificare l'informazione contenuta in un messaggio.

La formula che propose è nota come **entropia di Shannon**:

```
H = - somma_i  p(x_i) * log_2(p(x_i))
```

dove p(x_i) è la probabilità dell'i-esimo simbolo del messaggio. Il nome richiama l'entropia della termodinamica, che ha una formula della stessa forma. Secondo un aneddoto molto citato, fu John von Neumann a suggerire a Shannon il nome "entropia", con questa motivazione: *"Chiamala entropia: nessuno sa davvero cosa sia l'entropia, quindi in un dibattito avrai sempre il vantaggio."*

Per la statistica la teoria di Shannon è importante. L'entropia misura il grado di imprevedibilità di una distribuzione di probabilità. Una distribuzione uniforme ha entropia massima (massima incertezza); una distribuzione concentrata su un solo valore ha entropia zero (nessuna incertezza). Il concetto ritorna in molti contesti: alberi decisionali, divergenza di Kullback-Leibler, compressione dei dati.

---

## Dal bit al byte: le unità di misura dell'informazione

Un singolo bit può rappresentare solo due stati. Per rappresentare informazioni più complesse (una lettera dell'alfabeto, un numero, un colore) servono più bit combinati insieme. Con 2 bit abbiamo 4 combinazioni (00, 01, 10, 11); con 3 bit ne abbiamo 8; con n bit ne abbiamo 2^n.

Per convenzione storica il raggruppamento fondamentale è il **byte**, che corrisponde a **8 bit**. Con un byte si rappresentano 2^8 = 256 valori distinti. Lo standard **ASCII** (American Standard Code for Information Interchange), definito negli anni '60, usa 7 bit, cioè 128 codici (da 0 a 127), per le lettere dell'alfabeto latino (maiuscole e minuscole), le cifre, i segni di punteggiatura e alcuni caratteri di controllo; in memoria ogni carattere ASCII occupa comunque un byte.

Da qui si costruisce la scala delle unità di misura. Qui esistono **due convenzioni diverse**, che spesso generano confusione.

### Convenzione SI (Sistema Internazionale) — potenze di 10

| Unità      | Simbolo | Valore                |
|------------|---------|----------------------|
| Kilobyte   | kB      | 10^3 = 1.000 byte    |
| Megabyte   | MB      | 10^6 = 1.000.000 byte|
| Gigabyte   | GB      | 10^9 byte            |
| Terabyte   | TB      | 10^12 byte           |

Nel SI il prefisso kilo si scrive con la k minuscola (kB); la forma KB con la maiuscola è molto diffusa ma non standard.

### Convenzione IEC (binaria) — potenze di 2

| Unità      | Simbolo | Valore                   |
|------------|---------|--------------------------|
| Kibibyte   | KiB     | 2^10 = 1.024 byte        |
| Mebibyte   | MiB     | 2^20 = 1.048.576 byte    |
| Gibibyte   | GiB     | 2^30 = 1.073.741.824 byte|
| Tebibyte   | TiB     | 2^40 byte                |

### Perché il disco da 1 TB mostra 931 GB

Questa doppia convenzione spiega perché, quando comprate un disco da "1 TB", alcuni sistemi operativi (per esempio Windows) mostrano circa 931 GB. Il produttore del disco usa la convenzione SI: 1 TB = 1.000.000.000.000 byte. Il sistema operativo divide invece per potenze di 2: 1.000.000.000.000 / 1.073.741.824 ≈ 931 GiB, che però visualizza come "931 GB". I byte sono gli stessi: cambia solo l'unità con cui vengono contati. L'ambiguità ha causato anche cause legali collettive contro alcuni produttori di dischi, per esempio Western Digital e Seagate negli anni 2000.

---

## I sistemi di numerazione posizionali

### Perché usiamo la base 10

Noi contiamo in **base 10**, molto probabilmente perché abbiamo dieci dita. Altre civiltà hanno usato basi diverse: i Maya la base 20 (contando anche le dita dei piedi), i Babilonesi la base 60 (da cui derivano i nostri 60 minuti e 60 secondi).

In un **sistema posizionale** in base b, ogni cifra ha un peso che dipende dalla sua posizione. Il numero 347 in base 10 significa:

```
3 * 10^2  +  4 * 10^1  +  7 * 10^0  =  300 + 40 + 7  =  347
```

La notazione posizionale decimale fu sviluppata in India intorno al V-VI secolo. Il matematico persiano al-Khwarizmi (IX secolo) la descrisse in un trattato che, tradotto in latino nel XII secolo, contribuì a diffonderla in Europa; dalla versione latinizzata del suo nome, "Algoritmi", deriva la parola "algoritmo".

### Perché i computer usano la base 2

I computer sono fatti di **transistor**, che si possono usare come interruttori microscopici con due stati, acceso o spento, corrispondenti a due livelli di tensione elettrica. Costruire circuiti che distinguano in modo affidabile tra due livelli di tensione è molto più semplice e robusto che distinguerne dieci. Per questo i computer operano in **base 2**, il sistema **binario**.

In base 2 le uniche cifre disponibili sono 0 e 1. Il numero 1101 in base 2 si legge così:

```
1 * 2^3  +  1 * 2^2  +  0 * 2^1  +  1 * 2^0  =  8 + 4 + 0 + 1  =  13 (in base 10)
```

---

## Il sistema binario in dettaglio

### Conversione da binario a decimale

Per convertire un numero binario in decimale si moltiplicano le cifre per le potenze di 2 corrispondenti alla loro posizione (partendo da 0 a destra) e si sommano i risultati.

**Esempio**: convertire 10110 in decimale.

```
1 * 2^4  +  0 * 2^3  +  1 * 2^2  +  1 * 2^1  +  0 * 2^0
=  16   +   0     +   4     +   2     +   0
=  22
```

Potenze di 2 da ricordare: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024.

### Conversione da decimale a binario

Per convertire un numero decimale in binario si divide ripetutamente il numero per 2 e si annotano i resti, leggendoli poi dal basso verso l'alto.

**Esempio**: convertire 42 in binario.

```
42 / 2 = 21  resto 0
21 / 2 = 10  resto 1
10 / 2 = 5   resto 0
 5 / 2 = 2   resto 1
 2 / 2 = 1   resto 0
 1 / 2 = 0   resto 1
```

Leggendo i resti dal basso verso l'alto: **101010**. Verifica: 32 + 8 + 2 = 42.

Una curiosità: 42 in binario è 101010, un'alternanza regolare di 1 e 0. Douglas Adams, autore della *Guida galattica per gli autostoppisti*, scelse 42 come "la risposta alla domanda fondamentale sulla vita, l'universo e tutto quanto"; non c'è indicazione che la rappresentazione binaria abbia influito sulla scelta.

### Aritmetica binaria: la somma

La somma in binario funziona come quella in decimale, con la differenza che si va in riporto già quando si supera 1 (invece che 9).

Le regole elementari sono:
- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 10 (cioè 0 con riporto di 1)
- 1 + 1 + 1 = 11 (cioè 1 con riporto di 1)

**Esempio**: sommare 1011 (11) e 1101 (13).

```
    1 0 1 1
+   1 1 0 1
-----------
  1 1 0 0 0
```

Verifica: 11 + 13 = 24, e 11000 in binario vale 16 + 8 = 24.

### Aritmetica binaria: la sottrazione

La sottrazione in binario segue regole analoghe. Quando si deve sottrarre 1 da 0 si prende in prestito dalla cifra a sinistra, come nel decimale:

- 0 - 0 = 0
- 1 - 0 = 1
- 1 - 1 = 0
- 0 - 1 = 1 con prestito di 1 dalla posizione successiva

**Esempio**: sottrarre 0101 (5) da 1100 (12).

```
    1 1 0 0
-   0 1 0 1
-----------
    0 1 1 1
```

Verifica: 12 - 5 = 7, e 0111 in binario vale 4 + 2 + 1 = 7.

In pratica i computer non eseguono la sottrazione direttamente: usano una tecnica chiamata *complemento a due*, che permette di ricondurre la sottrazione a una somma. La vedremo nella lezione T05, dedicata alla rappresentazione dei dati e dei numeri negativi.

---

## Il sistema esadecimale

Scrivere lunghe sequenze di 0 e 1 è lento e porta facilmente a errori. Per scrivere dati binari in forma compatta si usa il sistema **esadecimale** (base 16).

In base 16 servono 16 simboli. Si usano le cifre da 0 a 9 e poi le lettere da A a F:

| Decimale | Binario | Esadecimale |
|----------|---------|-------------|
| 0        | 0000    | 0           |
| 1        | 0001    | 1           |
| 2        | 0010    | 2           |
| 3        | 0011    | 3           |
| 4        | 0100    | 4           |
| 5        | 0101    | 5           |
| 6        | 0110    | 6           |
| 7        | 0111    | 7           |
| 8        | 1000    | 8           |
| 9        | 1001    | 9           |
| 10       | 1010    | A           |
| 11       | 1011    | B           |
| 12       | 1100    | C           |
| 13       | 1101    | D           |
| 14       | 1110    | E           |
| 15       | 1111    | F           |

**Ogni cifra esadecimale corrisponde a 4 bit**, perché 16 = 2^4. Di conseguenza la conversione tra binario ed esadecimale è immediata: basta raggruppare i bit a gruppi di 4 partendo da destra. Per esempio, i 32 bit 11010110101011111100101000011011 si scrivono con 8 cifre esadecimali: D6AFCA1B.

**Esempio**: convertire il binario 11010110 in esadecimale.

```
1101  0110
 D      6
```

Risultato: D6 (in esadecimale). Per indicare che un numero è in base 16 si usa spesso il prefisso "0x": 0xD6.

Il procedimento inverso espande ogni cifra esadecimale in 4 bit: 0x2A3 = 0010 1010 0011.

### Conversione da esadecimale a decimale

**Esempio**: convertire 2A3 in base 16 a decimale.

```
2 * 16^2  +  A * 16^1  +  3 * 16^0
= 2 * 256 + 10 * 16   + 3 * 1
= 512     + 160        + 3
= 675
```

### Dove si incontra l'esadecimale

L'esadecimale è molto usato in informatica:

- **Colori HTML/CSS**: il colore #FF5733 indica le componenti Rosso=FF (255), Verde=57 (87), Blu=33 (51). Ogni coppia di cifre esadecimali rappresenta un byte (256 livelli di intensità per canale).
- **Indirizzi di memoria**: quando un programma va in errore e mostra un indirizzo come 0x7FFF5FBFF8C0, quello è l'indirizzo, in esadecimale, della cella di memoria coinvolta.
- **Indirizzi MAC**: l'indirizzo fisico delle schede di rete (es. A4:5E:60:B8:3D:1F) è scritto in esadecimale.
- **Codifiche Unicode**: il carattere è si scrive U+00E8 in notazione Unicode.

---

## Il sistema ottale

Il sistema **ottale** (base 8) ha avuto importanza storica ma oggi ha un uso pratico limitato. Utilizza le cifre da 0 a 7, e ogni cifra ottale corrisponde a 3 bit (perché 8 = 2^3).

L'ottale fu popolare nei primi decenni dell'informatica perché molte architetture avevano parole di 12, 24 o 36 bit, che si dividono in gruppi di 3. Quando si diffusero le architetture a 8, 16, 32 e 64 bit, l'esadecimale (con i suoi gruppi di 4 bit) si rivelò più pratico.

Oggi l'ottale si usa soprattutto per i **permessi dei file nei sistemi Unix/Linux**. Quando scrivete `chmod 755 file.txt`, i tre numeri (7, 5, 5) sono cifre ottali che rappresentano i permessi del proprietario (7 = 111 = rwx = lettura+scrittura+esecuzione), del gruppo (5 = 101 = r-x = lettura+esecuzione) e degli altri utenti (5 = r-x). Ciascuna cifra corrisponde a 3 bit, uno per ciascun permesso.

Per convertire da binario a ottale si raggruppano i bit a gruppi di 3 partendo da destra: 11010110 = 11 010 110 = 326 in ottale.

---

## Domande di verifica

1. Che cos'è un bit e qual è la sua relazione con il concetto di incertezza?

2. Shannon, nella sua teoria dell'informazione, si preoccupava del significato dei messaggi o di un altro aspetto? Quale?

3. Perché un disco etichettato come "1 TB" dal produttore viene mostrato da alcuni sistemi operativi come circa 931 GB? Quale ambiguità di notazione è alla base di questa discrepanza?

4. Perché i computer usano il sistema binario anziché il sistema decimale che ci è più familiare?

5. Spiegate la relazione tra il sistema esadecimale e il sistema binario: perché l'esadecimale è comodo per rappresentare dati binari?

6. Se un sistema ha esattamente 64 alternative equiprobabili, quanti bit sono necessari per rappresentare ciascuna di esse?

7. In che contesto si usa ancora oggi il sistema ottale?

8. Che cosa misura l'entropia di Shannon e quali sono i suoi valori estremi (massimo e minimo)?

---

## Esercizi

### Base

1. Convertire i seguenti numeri binari in decimale:
   - a) 1010
   - b) 11100
   - c) 10000001

2. Convertire i seguenti numeri decimali in binario:
   - a) 25
   - b) 100
   - c) 255

3. Convertire i seguenti numeri binari in esadecimale:
   - a) 10101111
   - b) 11001010
   - c) 11111111

4. Eseguire le seguenti somme in binario e verificare il risultato in decimale:
   - a) 1010 + 0101
   - b) 1111 + 0001
   - c) 10110 + 01101

### Intermedio

5. Convertire il numero esadecimale 0xBEEF in decimale e in binario.

6. Un'immagine a colori ha 1920 x 1080 pixel, e ogni pixel è codificato con 3 byte (un byte per canale: rosso, verde, blu). Quanti byte occupa l'immagine non compressa? Esprimere il risultato in MB (base 10) e in MiB (base 2).

7. Quanti bit servono per rappresentare tutti i possibili esiti del lancio di 5 dadi a sei facce? (Suggerimento: quanti sono i possibili esiti totali?)

8. Eseguire la sottrazione in binario: 11000 - 01011. Verificare il risultato in decimale.

### Avanzato

9. L'entropia di Shannon di una sorgente che emette due simboli con probabilità p e (1-p) è H = -p*log_2(p) - (1-p)*log_2(1-p). Calcolate H per p = 0.5, p = 0.9 e p = 1.0 (per convenzione 0 * log_2(0) = 0). Commentate i risultati.

10. Un file di testo contiene 10.000 caratteri ASCII (7 bit ciascuno). Il file viene memorizzato usando byte (8 bit per carattere, con il bit più significativo sempre a 0). Quanti bit vengono sprecati? E quanti byte occupa il file?

11. Progettate un sistema di codifica binaria per rappresentare i 20 aminoacidi naturali. Quanti bit al minimo servono per ogni aminoacido? Se usate quel numero di bit, quante "parole" restano inutilizzate?

---

## Riepilogo

In questa lezione abbiamo visto che l'informazione è una grandezza misurabile e che il bit ne è l'unità elementare. Abbiamo visto i sistemi di numerazione decimale, binario, esadecimale e ottale, le conversioni tra basi e l'aritmetica binaria.

Questi concetti servono in pratica. Quando caricate un dataset in R o in Python, ogni numero, ogni carattere e ogni valore mancante è rappresentato come una sequenza di bit. Conoscere questa rappresentazione aiuta a capire perché 0.1 + 0.2 non fa esattamente 0.3 in un computer (lo vedremo in T05), perché un intero ha un valore massimo, perché un file CSV da 100 MB può occupare molto meno spazio se compresso.

Nella prossima lezione (T02) passeremo dalla rappresentazione dei dati alla **logica**: vedremo come l'algebra introdotta da George Boole nel 1854 sia diventata la base dei circuiti dei computer, e ripercorreremo la storia del calcolo automatico, dalle macchine meccaniche di Pascal e Babbage fino ai transistor e ai microprocessori.
