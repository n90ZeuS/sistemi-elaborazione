# Lezione Frontale 1 — Informazione, bit e sistemi di numerazione

## Benvenuti: perche questo corso esiste

Siete iscritti a Scienze Statistiche. Forse vi state chiedendo: perche devo studiare come funziona un computer? La risposta e semplice e profonda al tempo stesso. Oggi la statistica non si fa piu con carta, penna e tavole dei logaritmi: si fa con macchine che elaborano milioni di osservazioni in frazioni di secondo. Un futuro statistico che non capisce come funziona un elaboratore e come un chirurgo che non conosce l'anatomia: puo anche seguire le procedure, ma quando qualcosa va storto — e qualcosa va sempre storto — non sa dove guardare.

In questo corso faremo un viaggio che parte dai fondamenti teorici dell'informazione, attraversa l'architettura delle macchine, e arriva fino alla programmazione. Non vi chiediamo di diventare ingegneri informatici. Vi chiediamo di sviluppare un'intuizione solida su come i dati nascono, vivono e vengono elaborati dentro un computer. Questa intuizione vi rendera statistici migliori: saprete perche un calcolo e lento, perche un numero perde precisione, perche un dataset non sta in memoria, e soprattutto saprete ragionare in modo algoritmico, cioe scomporre un problema complesso in passi elementari e risolvibili.

Cominciamo dall'inizio. Cominciamo dall'informazione.

---

## Che cos'e l'informazione

Nella vita quotidiana usiamo la parola "informazione" in modo intuitivo: un messaggio, una notizia, un dato. Ma in informatica e in teoria della comunicazione questa parola ha un significato preciso, e per arrivarci dobbiamo fare un passo indietro e parlare di **incertezza**.

Immaginate di lanciare una moneta. Prima del lancio, non sapete se uscira testa o croce: siete in uno stato di incertezza. Dopo il lancio, osservate il risultato e la vostra incertezza si riduce. Ecco: **l'informazione e cio che riduce l'incertezza**. Piu siete incerti prima, piu informazione ricevete dopo.

Se la moneta e truccata e esce sempre testa, il lancio non vi dice nulla di nuovo: l'informazione e zero. Se invece la moneta e perfettamente equilibrata, ogni lancio vi fornisce la massima quantita di informazione possibile per un evento con due esiti. Questa quantita ha un nome: si chiama **bit**.

### Il bit: l'atomo dell'informazione

La parola "bit" e una contrazione di *binary digit*, cifra binaria. Un bit e la quantita di informazione necessaria per distinguere tra due alternative equiprobabili: si/no, vero/falso, 0/1, acceso/spento. E l'unita fondamentale, indivisibile, dell'informazione digitale.

Pensateci cosi: se vi dico "ho pensato un numero tra 1 e 8" e voi potete fare domande a cui rispondo solo si o no, quante domande vi servono per indovinare? Tre. Con la prima dimezzate le possibilita (1-4 o 5-8?), con la seconda le dimezzate ancora (1-2 o 3-4?), con la terza arrivate al numero esatto. Tre domande, tre bit di informazione. In generale, per distinguere tra N alternative equiprobabili servono log_2(N) bit.

Questa non e solo una curiosita matematica. E il fondamento su cui poggia tutta l'informatica moderna.

---

## Claude Shannon e la nascita della teoria dell'informazione

Nel 1948, un ingegnere di 32 anni che lavorava ai Bell Telephone Laboratories pubblico un articolo destinato a cambiare il mondo. Si chiamava **Claude Elwood Shannon** e l'articolo si intitolava *"A Mathematical Theory of Communication"*. In quel lavoro, Shannon fece qualcosa di straordinario: trasformo il concetto vago e intuitivo di "informazione" in una grandezza misurabile, con tanto di unita di misura e formule matematiche.

Shannon non era interessato al *significato* dei messaggi — che una frase parlasse di poesia o di bulloni gli era indifferente. A lui interessava il problema ingegneristico: come trasmettere messaggi in modo affidabile attraverso un canale rumoroso (un filo telefonico, un'onda radio). Per farlo, doveva quantificare l'informazione contenuta in un messaggio.

La formula che propose e nota come **entropia di Shannon**:

```
H = - somma_i  p(x_i) * log_2(p(x_i))
```

dove p(x_i) e la probabilita dell'i-esimo simbolo del messaggio. Notate la somiglianza con l'entropia della termodinamica: non e un caso. Lo stesso Shannon scelse il nome "entropia" su suggerimento del grande matematico John von Neumann, il quale — racconta la leggenda — gli disse: *"Chiamala entropia: nessuno sa davvero cosa sia l'entropia, quindi in un dibattito avrai sempre il vantaggio."*

Per la statistica, la teoria di Shannon e fondamentale. L'entropia misura il grado di "disordine" o "imprevedibilita" di una distribuzione di probabilita. Una distribuzione uniforme ha entropia massima (massima incertezza); una distribuzione concentrata su un solo valore ha entropia zero (nessuna incertezza). Vedrete che questo concetto ritorna in molti contesti: alberi decisionali, teoria dell'informazione di Fisher, compressione dei dati.

---

## Dal bit al byte: le unita di misura dell'informazione

Un singolo bit puo rappresentare solo due stati. Per rappresentare informazioni piu complesse — una lettera dell'alfabeto, un numero, un colore — servono piu bit combinati insieme. Con 2 bit abbiamo 4 combinazioni (00, 01, 10, 11); con 3 bit ne abbiamo 8; con n bit ne abbiamo 2^n.

Per convenzione storica, il raggruppamento fondamentale e il **byte**, che corrisponde a **8 bit**. Con un byte possiamo rappresentare 2^8 = 256 valori distinti, sufficienti per tutte le lettere dell'alfabeto latino (maiuscole e minuscole), le cifre, i segni di punteggiatura e un buon numero di simboli speciali. Questa corrispondenza tra numeri e caratteri e codificata nello standard **ASCII** (American Standard Code for Information Interchange), definito negli anni '60.

Da qui si costruisce la scala delle unita di misura. Ed e qui che le cose si complicano, perche esistono **due convenzioni diverse** che generano confusione.

### Convenzione SI (Sistema Internazionale) — potenze di 10

| Unita      | Simbolo | Valore                |
|------------|---------|----------------------|
| Kilobyte   | KB      | 10^3 = 1.000 byte    |
| Megabyte   | MB      | 10^6 = 1.000.000 byte|
| Gigabyte   | GB      | 10^9 byte            |
| Terabyte   | TB      | 10^12 byte           |

### Convenzione IEC (binaria) — potenze di 2

| Unita      | Simbolo | Valore                   |
|------------|---------|--------------------------|
| Kibibyte   | KiB     | 2^10 = 1.024 byte        |
| Mebibyte   | MiB     | 2^20 = 1.048.576 byte    |
| Gibibyte   | GiB     | 2^30 = 1.073.741.824 byte|
| Tebibyte   | TiB     | 2^40 byte                |

### Perche il disco da 1 TB mostra 931 GB

Questa doppia convenzione e la ragione per cui, quando comprate un disco fisso da "1 TB", il vostro sistema operativo vi mostra solo circa 931 GB. Il produttore del disco usa la convenzione SI: 1 TB = 1.000.000.000.000 byte. Il sistema operativo, invece, divide per potenze di 2: 1.000.000.000.000 / 1.073.741.824 ≈ 931 GiB, che visualizza come "931 GB". Nessuno vi sta imbrogliando: e solo un'ambiguita di notazione. Ma genera innumerevoli lamentele online e, occasionalmente, cause legali (nel 2007 Apple fu citata in giudizio proprio per questo).

---

## I sistemi di numerazione posizionali

### Perche usiamo la base 10

Noi esseri umani contiamo in **base 10**. I motivi sono anatomici, non matematici: abbiamo dieci dita. Le civilta che hanno sviluppato sistemi di numerazione alternativi lo confermano: i Maya usavano la base 20 (contando anche le dita dei piedi), i Babilonesi la base 60 (da cui derivano i nostri 60 minuti e 60 secondi).

In un **sistema posizionale** in base b, ogni cifra ha un peso che dipende dalla sua posizione. Il numero 347 in base 10 significa:

```
3 * 10^2  +  4 * 10^1  +  7 * 10^0  =  300 + 40 + 7  =  347
```

Questo principio — che a noi sembra ovvio — e in realta un'invenzione straordinaria, sviluppata in India intorno al V-VI secolo e trasmessa all'Europa dal matematico persiano al-Khwarizmi nel IX secolo (dalla cui versione latinizzata del nome, "Algoritmi", deriva la parola "algoritmo").

### Perche i computer usano la base 2

I computer non hanno dita. Hanno **transistor**, che sono essenzialmente interruttori microscopici con due stati: acceso o spento, che corrispondono a due livelli di tensione elettrica. Costruire circuiti che distinguano in modo affidabile tra due livelli di tensione e molto piu semplice e robusto che distinguerne dieci. Per questo i computer operano in **base 2**, il sistema **binario**.

In base 2 le uniche cifre disponibili sono 0 e 1. Il numero 1101 in base 2 si legge cosi:

```
1 * 2^3  +  1 * 2^2  +  0 * 2^1  +  1 * 2^0  =  8 + 4 + 0 + 1  =  13 (in base 10)
```

---

## Il sistema binario in dettaglio

### Conversione da binario a decimale

Per convertire un numero binario in decimale, si moltiplicano le cifre per le potenze di 2 corrispondenti alla loro posizione (partendo da 0 a destra) e si sommano i risultati.

**Esempio**: convertire 10110 in decimale.

```
1 * 2^4  +  0 * 2^3  +  1 * 2^2  +  1 * 2^1  +  0 * 2^0
=  16   +   0     +   4     +   2     +   0
=  22
```

### Conversione da decimale a binario

Per convertire un numero decimale in binario, si divide ripetutamente il numero per 2 e si annotano i resti, leggendoli poi dal basso verso l'alto.

**Esempio**: convertire 42 in binario.

```
42 / 2 = 21  resto 0
21 / 2 = 10  resto 1
10 / 2 = 5   resto 0
 5 / 2 = 2   resto 1
 2 / 2 = 1   resto 0
 1 / 2 = 0   resto 1
```

Leggendo i resti dal basso verso l'alto: **101010**. Verifica: 32 + 8 + 2 = 42. Corretto.

Un dettaglio curioso: 42 in binario e 101010, un pattern regolare. Douglas Adams, autore della *Guida galattica per gli autostoppisti*, scelse 42 come "la risposta alla domanda fondamentale sulla vita, l'universo e tutto quanto". Non e chiaro se la bellezza della sua rappresentazione binaria abbia influenzato la scelta, ma la coincidenza piace agli informatici.

### Aritmetica binaria: la somma

La somma in binario funziona esattamente come quella in decimale, con la differenza che si va in riporto gia quando si supera 1 (invece che 9).

Le regole elementari sono:
- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 10 (cioe 0 con riporto di 1)
- 1 + 1 + 1 = 11 (cioe 1 con riporto di 1)

**Esempio**: sommare 1011 (11) e 1101 (13).

```
    1 0 1 1
+   1 1 0 1
-----------
  1 1 0 0 0
```

Verifica: 11 + 13 = 24. E 11000 in binario e 16 + 8 = 24. Corretto.

### Aritmetica binaria: la sottrazione

La sottrazione in binario segue regole analoghe. Quando si deve sottrarre 1 da 0, si prende in prestito dalla cifra a sinistra (come nel decimale):

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

Verifica: 12 - 5 = 7. E 0111 in binario e 4 + 2 + 1 = 7. Corretto.

Nella pratica, i computer non eseguono la sottrazione direttamente: usano una tecnica chiamata *complemento a due*, che permette di ricondurre la sottrazione a una somma. Ne parleremo quando affronteremo la rappresentazione dei numeri negativi.

---

## Il sistema esadecimale

Se il binario e il linguaggio naturale dei computer, l'esadecimale e il suo interprete per gli esseri umani. Scrivere lunghe sequenze di 0 e 1 e tedioso e soggetto a errori. Il sistema **esadecimale** (base 16) risolve questo problema in modo elegante.

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

La bellezza dell'esadecimale sta nel fatto che **ogni cifra esadecimale corrisponde esattamente a 4 bit**. Questo perche 16 = 2^4. Di conseguenza, la conversione tra binario ed esadecimale e immediata: basta raggruppare i bit a gruppi di 4.

**Esempio**: convertire il binario 11010110 in esadecimale.

```
1101  0110
 D      6
```

Risultato: D6 (in esadecimale). Per indicare che un numero e in base 16, si usa spesso il prefisso "0x": 0xD6.

### Dove si incontra l'esadecimale

L'esadecimale e onnipresente nel mondo dell'informatica:

- **Colori HTML/CSS**: il colore #FF5733 indica le componenti Rosso=FF (255), Verde=57 (87), Blu=33 (51). Ogni coppia di cifre esadecimali rappresenta un byte (256 livelli di intensita per canale).
- **Indirizzi di memoria**: quando un programma va in errore e vi mostra un indirizzo come 0x7FFF5FBFF8C0, quello e un indirizzo esadecimale della cella di memoria coinvolta.
- **Indirizzi MAC**: l'indirizzo fisico delle schede di rete (es. A4:5E:60:B8:3D:1F) e scritto in esadecimale.
- **Codifiche Unicode**: il carattere e si scrive U+00E8 in notazione Unicode.

### Conversione da esadecimale a decimale

**Esempio**: convertire 2A3 in base 16 a decimale.

```
2 * 16^2  +  A * 16^1  +  3 * 16^0
= 2 * 256 + 10 * 16   + 3 * 1
= 512     + 160        + 3
= 675
```

---

## Il sistema ottale

Il sistema **ottale** (base 8) ha un'importanza storica significativa ma un uso pratico oggi molto limitato. Utilizza le cifre da 0 a 7, e ogni cifra ottale corrisponde a esattamente 3 bit (perche 8 = 2^3).

L'ottale fu popolare nei primi decenni dell'informatica perche molte architetture avevano parole di 12, 24 o 36 bit, che si dividono comodamente in gruppi di 3. Quando le architetture a 8, 16, 32 e 64 bit divennero dominanti, l'esadecimale (con i suoi gruppi di 4 bit) si rivelo piu pratico.

Oggi l'ottale sopravvive principalmente in un contesto: i **permessi dei file nei sistemi Unix/Linux**. Quando scrivete `chmod 755 file.txt`, quei tre numeri (7, 5, 5) sono cifre ottali che rappresentano i permessi del proprietario (7 = rwx = lettura+scrittura+esecuzione), del gruppo (5 = r-x = lettura+esecuzione) e degli altri utenti (5 = r-x). Ciascuna cifra corrisponde a 3 bit, uno per ciascun permesso.

---

## Domande di verifica

1. Che cos'e un bit e qual e la sua relazione con il concetto di incertezza?

2. Shannon, nella sua teoria dell'informazione, si preoccupava del significato dei messaggi o di un altro aspetto? Quale?

3. Perche un disco etichettato come "1 TB" dal produttore viene mostrato dal sistema operativo come circa 931 GB? Quale ambiguita di notazione e alla base di questa discrepanza?

4. Perche i computer usano il sistema binario anziche il sistema decimale che ci e piu familiare?

5. Spiegate la relazione tra il sistema esadecimale e il sistema binario: perche l'esadecimale e particolarmente comodo per rappresentare dati binari?

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

6. Un'immagine a colori ha 1920 x 1080 pixel, e ogni pixel e codificato con 3 byte (un byte per canale: rosso, verde, blu). Quanti byte occupa l'immagine non compressa? Esprimere il risultato in MB (base 10) e in MiB (base 2).

7. Quanti bit servono per rappresentare tutti i possibili esiti del lancio di 5 dadi a sei facce? (Suggerimento: quanti sono i possibili esiti totali?)

8. Eseguire la sottrazione in binario: 11000 - 01011. Verificare il risultato in decimale.

### Avanzato

9. L'entropia di Shannon di una sorgente che emette simboli con probabilita p e (1-p) e H = -p*log_2(p) - (1-p)*log_2((1-p)). Calcolate H per p = 0.5, p = 0.9 e p = 1.0. Commentate i risultati.

10. Un file di testo contiene 10.000 caratteri ASCII (7 bit ciascuno). Il file viene memorizzato usando byte (8 bit per carattere, con il bit piu significativo sempre a 0). Quanta "capacita" viene sprecata? E quanti byte occupa il file?

11. Progettate un sistema di codifica binaria per rappresentare i 20 aminoacidi naturali. Quanti bit al minimo servono per ogni aminoacido? Se usate quel numero di bit, quante "parole" restano inutilizzate?

---

## Osservazioni finali

In questa prima lezione abbiamo gettato le fondamenta su cui costruiremo tutto il resto del corso. Abbiamo visto che l'informazione non e un concetto vago, ma una grandezza misurabile, e che il bit ne e l'unita elementare. Abbiamo esplorato i sistemi di numerazione — decimale, binario, esadecimale, ottale — e abbiamo praticato le conversioni e l'aritmetica binaria.

Queste non sono astrazioni fini a se stesse. Ogni volta che caricherete un dataset in R o in Python, ogni numero, ogni carattere, ogni valore mancante sara rappresentato come una sequenza di bit. Comprendere questa rappresentazione vi aiutera a capire fenomeni altrimenti misteriosi: perche 0.1 + 0.2 non fa esattamente 0.3 in un computer (lo scopriremo nelle prossime lezioni), perche un intero ha un valore massimo, perche un file CSV da 100 MB puo diventare 30 MB se compresso.

Nella prossima lezione faremo un salto dalla rappresentazione dei dati alla **logica**: vedremo come l'algebra inventata da George Boole nel 1854 — quasi un secolo prima dei computer — sia diventata il linguaggio con cui le macchine "ragionano". E ripercorreremo la storia affascinante del calcolo automatico, dalle macchine meccaniche di Pascal e Babbage fino ai transistor e ai microprocessori.
