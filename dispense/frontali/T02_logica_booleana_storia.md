# Lezione 2 — Logica booleana e storia del calcolo

## Introduzione: la logica come algebra

Nella lezione precedente abbiamo visto come l'informazione si misura in bit e come i numeri si rappresentano in binario. Oggi passiamo dai numeri alla **logica**. Vedremo come le operazioni logiche — quelle che usiamo quando diciamo "se piove E non ho l'ombrello, allora mi bagno" — possano essere trattate come operazioni matematiche, e come questa idea, proposta da un matematico inglese a metà Ottocento, sia diventata la base dei circuiti di ogni computer.

Dopo la logica booleana ripercorreremo la storia del calcolo automatico, dall'abaco ai microprocessori.

---

## George Boole e la nascita dell'algebra della logica

**George Boole** (1815-1864) era figlio di un calzolaio di Lincoln, in Inghilterra, e fu quasi interamente autodidatta: imparò da solo il latino, il greco, il francese e il tedesco, e a sedici anni insegnava già in una scuola. A diciannove anni aprì una scuola propria e, nel tempo libero, studiava matematica leggendo i lavori di Lagrange e Laplace. Nel 1849, senza aver mai frequentato l'università, divenne professore di matematica al Queen's College di Cork, in Irlanda.

Nel 1847 pubblicò un libretto intitolato *The Mathematical Analysis of Logic*, e nel 1854 la sua opera principale: *An Investigation of the Laws of Thought, on Which are Founded the Mathematical Theories of Logic and Probabilities*. L'idea centrale è che **la logica può essere trattata come un'algebra**.

Boole osservò che le proposizioni logiche — affermazioni che possono essere vere o false — si possono manipolare con operazioni simili a quelle dell'algebra ordinaria. Invece di numeri si lavora con valori di verità; invece di addizione e moltiplicazione si usano operazioni logiche. I valori possibili sono solo due: **Vero** (1) e **Falso** (0). (L'algebra booleana nella forma che usiamo oggi è stata poi sistemata da altri matematici, tra cui Jevons, Peirce e Schröder.)

Usare 1 e 0, gli stessi simboli del sistema binario, è ciò che permette di collegare la logica ai circuiti elettronici. Boole però non poteva saperlo: i primi calcolatori sarebbero arrivati quasi un secolo dopo. Morì nel 1864, a 49 anni, di polmonite. Secondo un racconto molto diffuso, ma non documentato con certezza, la moglie Mary Everest lo curò avvolgendolo in lenzuola bagnate, convinta che il rimedio dovesse somigliare alla causa del male (Boole si era ammalato dopo aver camminato sotto la pioggia).

---

## Gli operatori booleani fondamentali

### AND (congiunzione logica)

L'operatore AND restituisce Vero solo quando **entrambi** gli operandi sono Veri. Corrisponde alla congiunzione "e" del linguaggio naturale. In notazione matematica si scrive spesso come moltiplicazione: A AND B = A · B, oppure A ∧ B.

**Tabella di verità di AND:**

| A | B | A AND B |
|---|---|---------|
| 0 | 0 |    0    |
| 0 | 1 |    0    |
| 1 | 0 |    0    |
| 1 | 1 |    1    |

*Esempio nella vita reale*: "Supero l'esame SE studio E sono presente all'appello." Entrambe le condizioni devono essere vere.

*Esempio per statistici*: quando filtrate un dataset e chiedete "righe dove età > 30 AND reddito > 50000", state applicando un AND logico.

### OR (disgiunzione logica)

L'operatore OR restituisce Vero quando **almeno uno** degli operandi è Vero. È un OR **inclusivo**: è vero anche quando entrambi sono veri (a differenza della "o" italiana, che spesso usiamo in senso esclusivo). Si scrive come addizione: A OR B = A + B, oppure A ∨ B.

**Tabella di verità di OR:**

| A | B | A OR B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   1    |

*Esempio nella vita reale*: "Puoi pagare con carta O con contanti." (Anche con entrambi, volendo.)

*Esempio per statistici*: "Seleziona i record dove regione = 'Lazio' OR regione = 'Toscana'."

### NOT (negazione)

L'operatore NOT inverte il valore di verità: ciò che era Vero diventa Falso e viceversa. È un operatore **unario** (agisce su un solo operando). Si scrive NOT A, oppure A con una barra sopra, oppure ¬A.

**Tabella di verità di NOT:**

| A | NOT A |
|---|-------|
| 0 |   1   |
| 1 |   0   |

*Esempio nella vita reale*: "Se NON piove, esco senza ombrello."

Con questi tre operatori — AND, OR, NOT — si può esprimere qualsiasi funzione logica.

---

## Operatori derivati

### NAND (NOT AND)

NAND è la negazione dell'AND: restituisce Falso solo quando entrambi gli input sono Veri. In tutti gli altri casi restituisce Vero.

**Tabella di verità di NAND:**

| A | B | A NAND B |
|---|---|----------|
| 0 | 0 |    1     |
| 0 | 1 |    1     |
| 1 | 0 |    1     |
| 1 | 1 |    0     |

Il NAND è un operatore **universale**: qualsiasi funzione logica — AND, OR, NOT e qualunque altra — può essere costruita usando **solamente** porte NAND. La proprietà ha anche un risvolto pratico. Nella tecnologia CMOS, usata nei chip di oggi, le porte più semplici sono quelle che invertono l'uscita: un NOT richiede 2 transistor, un NAND o un NOR a due ingressi 4 transistor, mentre un AND si ottiene come NAND seguito da NOT (6 transistor). Per questo i progettisti usano molto le porte NAND. Le memorie "NAND flash" di smartphone e SSD prendono invece il nome dal modo in cui sono collegate le celle di memoria (in serie, come i transistor di una porta NAND).

Vediamo come costruire gli operatori base usando solo NAND:
- **NOT A** = A NAND A (cioè: collegate entrambi gli input allo stesso segnale)
- **A AND B** = NOT (A NAND B) = (A NAND B) NAND (A NAND B)
- **A OR B** = (A NAND A) NAND (B NAND B)

### NOR (NOT OR)

Il NOR è la negazione dell'OR: restituisce Vero solo quando entrambi gli input sono Falsi. Anche il NOR è un operatore universale.

**Tabella di verità di NOR:**

| A | B | A NOR B |
|---|---|---------|
| 0 | 0 |    1    |
| 0 | 1 |    0    |
| 1 | 0 |    0    |
| 1 | 1 |    0    |

### XOR (OR esclusivo)

Lo XOR (*exclusive OR*) restituisce Vero quando gli input sono **diversi** tra loro. Corrisponde alla "o" esclusiva dell'italiano: "o l'uno o l'altro, ma non entrambi."

**Tabella di verità di XOR:**

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 |    0    |
| 0 | 1 |    1    |
| 1 | 0 |    1    |
| 1 | 1 |    0    |

Lo XOR serve nell'aritmetica binaria (è la cifra della somma nel circuito sommatore) e nella crittografia: applicando due volte lo XOR con la stessa chiave si riottiene il dato originale, (A XOR B) XOR B = A, proprietà usata in molti algoritmi di cifratura.

---

## Claude Shannon e i circuiti elettrici (1937)

Boole aveva creato l'algebra della logica e il sistema binario esisteva già da tempo (Leibniz lo aveva descritto nel 1703). Chi collegò le due cose ai circuiti elettrici fu **Claude Shannon**, lo stesso della teoria dell'informazione vista nella lezione precedente, undici anni prima di quel lavoro. Nel 1937 Shannon aveva 21 anni, era studente al MIT e stava scrivendo la sua tesi di master (*master's thesis*), intitolata *"A Symbolic Analysis of Relay and Switching Circuits"* (pubblicata nel 1938). In quella tesi Shannon dimostrò che **l'algebra di Boole descrive il comportamento dei circuiti elettrici a relè**. Negli stessi anni risultati simili furono ottenuti in modo indipendente da Akira Nakashima in Giappone e da Victor Šestakov in Unione Sovietica.

Un relè è un interruttore controllato elettricamente: può essere aperto (0) o chiuso (1). Due relè in serie si comportano come un AND (la corrente passa solo se entrambi sono chiusi). Due relè in parallelo si comportano come un OR (la corrente passa se almeno uno è chiuso). Un relè normalmente chiuso, che si apre quando riceve un segnale, si comporta come un NOT.

Shannon non inventò i relè né scoprì Boole: il suo contributo fu vedere il collegamento tra la matematica del XIX secolo e l'ingegneria elettrica del XX. Lo psicologo Howard Gardner ha definito questa tesi "forse la più importante tesi di master del secolo". Da allora i circuiti digitali si progettano scrivendo e semplificando espressioni booleane.

---

## Espressioni booleane e semplificazione

Un'**espressione booleana** combina variabili e operatori logici per definire una funzione. Per esempio:

```
F(A, B, C) = (A AND B) OR (NOT A AND C)
```

Questa espressione vale 1 quando A e B sono entrambi 1, oppure quando A è 0 e C è 1.

La **semplificazione** delle espressioni booleane è importante perché un'espressione più semplice corrisponde a un circuito con meno porte logiche, quindi meno transistor, meno consumo, meno costo e maggiore velocità. Alcune regole utili:

- **Identità**: A AND 1 = A; A OR 0 = A
- **Annullamento**: A AND 0 = 0; A OR 1 = 1
- **Idempotenza**: A AND A = A; A OR A = A
- **Complemento**: A AND (NOT A) = 0; A OR (NOT A) = 1
- **Leggi di De Morgan**: NOT(A AND B) = (NOT A) OR (NOT B); NOT(A OR B) = (NOT A) AND (NOT B)

Vediamo un esempio delle **leggi di De Morgan**. Considerate la frase: "Non è vero che piove e fa freddo." Per De Morgan equivale a: "Non piove oppure non fa freddo." In simboli: NOT(A AND B) = (NOT A) OR (NOT B). Provate a verificarlo con la tabella di verità: i risultati coincidono per tutte le combinazioni di A e B.

**Esempio di semplificazione**:

```
F = (A AND B) OR (A AND NOT B)
  = A AND (B OR NOT B)          [raccogliendo A]
  = A AND 1                     [complemento: B OR NOT B = 1]
  = A                           [identità]
```

L'espressione originale richiedeva 4 porte logiche (due AND, una OR, una NOT); quella semplificata non ne richiede nessuna (è semplicemente il segnale A). In un chip con miliardi di transistor queste semplificazioni riducono area, consumo e ritardi; oggi le eseguono in automatico i programmi di progettazione dei circuiti.

---

## Dai transistor ai circuiti integrati

Prima della storia del calcolo, vediamo la catena che porta dalla logica booleana ai computer fisici:

1. **Transistor**: un componente elettronico che funziona come un interruttore microscopico. Può essere acceso o spento, e il suo stato può essere controllato da un segnale elettrico. Fu inventato nel 1947 ai Bell Labs (ne parleremo tra poco).

2. **Porta logica**: un piccolo circuito composto da pochi transistor che realizza un'operazione booleana (AND, OR, NOT, NAND, ecc.). Una porta NAND a due input richiede tipicamente 4 transistor.

3. **Circuito combinatorio**: una rete di porte logiche che realizza una funzione più complessa. Per esempio, un sommatore a un bit (che somma due bit e un riporto) si costruisce con due porte XOR, due porte AND e una porta OR.

4. **Circuito integrato**: milioni (o miliardi) di transistor realizzati su una singola piastrina di silicio, che formano circuiti combinatori e sequenziali complessi. Un processore moderno contiene decine di miliardi di transistor.

Questa è la catena che va dall'algebra di Boole al chip che esegue i vostri programmi.

---

## Storia del calcolo: dalle origini meccaniche

### L'abaco

La storia degli strumenti di calcolo inizia con l'**abaco**, che permette di eseguire operazioni aritmetiche spostando palline (o sassolini) lungo aste o scanalature. Le prime forme risalgono forse alla Mesopotamia, tra il 2700 e il 2300 a.C., ma la datazione è incerta. L'abaco non "calcola" da solo — è l'operatore umano che esegue i passaggi — ma è uno dei primi strumenti progettati per assistere il calcolo. Se ne conoscono versioni greche, romane e cinesi; il *soroban* giapponese deriva dal *suanpan* cinese. Suanpan e soroban sono usati ancora oggi, e un operatore esperto esegue addizioni e sottrazioni molto velocemente.

### Blaise Pascal e la Pascalina (1642)

**Blaise Pascal** (1623-1662), matematico, fisico e filosofo francese, iniziò nel 1642, non ancora ventenne, a costruire una calcolatrice meccanica: la **Pascalina**. Voleva aiutare il padre, Étienne, che come commissario per le imposte in Normandia doveva eseguire lunghi calcoli aritmetici.

La Pascalina usava un sistema di ruote dentate: quando una ruota completava un giro (passando dal 9 allo 0), un meccanismo a scatto faceva avanzare di una posizione la ruota successiva, realizzando automaticamente il riporto. Eseguiva somme e sottrazioni. Pascal costruì circa cinquanta prototipi e, nel decennio successivo, una ventina di esemplari; il costo elevato ne impedì la diffusione commerciale.

Non fu la prima calcolatrice meccanica in assoluto: nel 1623 Wilhelm Schickard aveva progettato un "orologio calcolatore", di cui però non resta alcun esemplare. La Pascalina è la più antica calcolatrice meccanica di cui abbiamo esemplari originali (nove sono conservati).

### Gottfried Leibniz, il sistema binario e l'I Ching (1703)

**Gottfried Wilhelm Leibniz** (1646-1716) fu matematico, filosofo e diplomatico. Inventò il calcolo infinitesimale indipendentemente da Newton e progettò anche macchine calcolatrici: la **Stepped Reckoner** (progettata dal 1672, l'esemplare conservato è del 1694) eseguiva le quattro operazioni aritmetiche grazie a un cilindro a denti di lunghezza scalata, oggi chiamato "ruota di Leibniz".

Il contributo di Leibniz che più ci interessa è la descrizione del **sistema binario**. Nell'articolo *"Explication de l'Arithmétique Binaire"* (1703), Leibniz mostrò che tutti i numeri si possono esprimere con sole due cifre, 0 e 1. Fu colpito dal parallelismo con l'**I Ching**, l'antico testo cinese di divinazione, in cui gli esagrammi sono costruiti combinando linee intere (yang) e spezzate (yin): un sistema binario ante litteram, di circa tremila anni fa. Leibniz, uomo profondamente religioso, vide nel binario una metafora della creazione: Dio (1) crea tutto dal nulla (0).

Il binario entrò nei calcolatori solo più di due secoli dopo, con le macchine a relè degli anni '30 e '40 del Novecento.

### Charles Babbage e Ada Lovelace: il primo progetto di computer programmabile

**Charles Babbage** (1791-1871), matematico e ingegnere britannico, è spesso chiamato "il padre del computer". Nel 1822 iniziò a progettare la **Macchina Differenziale** (*Difference Engine*), un dispositivo meccanico per calcolare tabelle matematiche senza errori umani. Nel 1837 descrisse un progetto più generale, la **Macchina Analitica** (*Analytical Engine*).

La Macchina Analitica, mai completata, aveva già le componenti fondamentali di un computer moderno:
- Un **mulino** (*mill*): l'equivalente dell'unità aritmetico-logica (ALU), che esegue le operazioni.
- Un **magazzino** (*store*): l'equivalente della memoria, che conserva i dati.
- Un sistema di **schede perforate** (riprese dal telaio Jacquard) per fornire istruzioni e dati: l'equivalente di un programma.
- La capacità di eseguire **salti condizionali**: "se il risultato è negativo, vai all'istruzione numero 15."

Babbage non riuscì mai a costruirla, per mancanza di fondi e per i continui cambiamenti al progetto. **Augusta Ada King, contessa di Lovelace** (1815-1852), figlia del poeta Lord Byron, ne comprese a fondo il funzionamento. Nel 1843 Ada tradusse in inglese un articolo sulla Macchina Analitica scritto dall'ingegnere italiano Luigi Federico Menabrea, aggiungendo note circa tre volte più lunghe dell'articolo originale. In quelle note descrisse un algoritmo per calcolare i numeri di Bernoulli con la macchina: è spesso considerato il **primo programma pubblicato** (Babbage ne aveva già abbozzati altri, rimasti inediti). Ada osservò anche che la macchina non era solo un calcolatore numerico: poteva manipolare qualsiasi tipo di simbolo — note musicali, lettere — purché fosse possibile codificarlo in numeri. È l'idea di *general-purpose computer*, che si realizzerà un secolo dopo.

---

## Alan Turing e la nascita dell'informatica teorica

**Alan Mathison Turing** (1912-1954) è una delle figure centrali della storia dell'informatica. Nel 1936, a 24 anni, scrisse l'articolo *"On Computable Numbers, with an Application to the Entscheidungsproblem"*, in cui definì un modello matematico di calcolo che oggi chiamiamo **Macchina di Turing**.

### La Macchina di Turing

Una Macchina di Turing è un dispositivo immaginario composto da:
- Un **nastro** infinito diviso in celle, ciascuna contenente un simbolo (per esempio, 0 o 1).
- Una **testina** che può leggere e scrivere sul nastro e spostarsi di una cella a destra o a sinistra.
- Un **insieme finito di stati** e una **tabella di transizione** che dice: "Se sei nello stato X e leggi il simbolo Y, scrivi il simbolo Z, spostati in direzione D e passa allo stato W."

Il modello è molto semplice, ma la **tesi di Church-Turing** afferma che qualsiasi procedimento di calcolo che possiamo descrivere come algoritmo può essere eseguito da una Macchina di Turing. È una tesi, non un teorema (non si può dimostrare, perché "algoritmo" non ha una definizione formale indipendente), ma finora nessun modello di calcolo l'ha smentita ed è uno dei pilastri dell'informatica teorica.

Turing dimostrò anche che esistono problemi che **nessuna** macchina può risolvere. Il più famoso è il **problema della fermata** (*halting problem*): non esiste un algoritmo generale che, dato un programma qualsiasi, possa determinare se quel programma terminerà o girerà all'infinito. (Turing lo dimostrò in una forma equivalente; il nome "problema della fermata" è successivo.)

### Bletchley Park e la decrittazione di Enigma

Durante la Seconda guerra mondiale Turing lavorò a **Bletchley Park**, il centro segreto di crittoanalisi britannico, alla decrittazione di **Enigma**, la macchina cifrante usata dalle forze armate tedesche; si occupò in particolare dei messaggi della marina. Partendo dalla *bomba* costruita dai crittoanalisti polacchi (Marian Rejewski, 1938), Turing progettò la **Bombe**, una macchina elettromeccanica che automatizzava la ricerca delle chiavi di cifratura; Gordon Welchman vi aggiunse un miglioramento importante. Secondo lo storico Harry Hinsley, il lavoro di Bletchley Park accorciò la guerra di due-quattro anni; la stima è discussa, ma il contributo è riconosciuto come molto rilevante.

Nel 1952 Turing fu condannato per omosessualità (allora reato in Gran Bretagna) e sottoposto a castrazione chimica. Morì nel 1954 per avvelenamento da cianuro; l'inchiesta concluse per il suicidio. Accanto al corpo fu trovata una mela morsicata, che però non fu mai analizzata. Nel 2013 ricevette la grazia postuma dalla regina Elisabetta II. Il logo di Apple con la mela morsicata non è un riferimento a Turing: il grafico che lo disegnò, Rob Janoff, ha spiegato che il morso serviva a far riconoscere la mela.

---

## I primi computer

### Konrad Zuse e lo Z3 (1941)

Negli stessi anni, in Germania, l'ingegnere civile **Konrad Zuse** (1910-1995) costruì i suoi primi calcolatori a Berlino, cominciando nel 1936 con lo Z1, montato nel soggiorno di casa dei genitori. Lo **Z3**, completato nel 1941, è considerato il primo computer programmabile e completamente automatico funzionante. Era elettromeccanico, non elettronico: usava circa 2.600 relè telefonici, lavorava in binario e leggeva il programma da pellicola cinematografica perforata. Non aveva però salti condizionali. Zuse lavorò in quasi completo isolamento e non conosceva il lavoro di Turing. Lo Z1 e lo Z3 furono distrutti dai bombardamenti alleati del 1943; il successivo Z4 si salvò e fu usato al Politecnico di Zurigo dal 1950. Il suo lavoro fu riconosciuto a livello internazionale solo decenni dopo.

### ENIAC (1945)

L'**ENIAC** (*Electronic Numerical Integrator and Computer*), progettato da John Mauchly e J. Presper Eckert e completato alla fine del 1945 all'Università della Pennsylvania, fu il primo computer **elettronico** programmabile e general-purpose. (Il Colossus britannico, usato a Bletchley Park dal 1944, era già elettronico, ma costruito solo per la crittoanalisi.) L'ENIAC usava circa 18.000 valvole termoioniche, pesava 27 tonnellate, occupava una stanza intera e consumava circa 150 kilowatt. Eseguiva 5.000 addizioni al secondo: molto per l'epoca, ma enormemente meno di qualsiasi calcolatrice tascabile di oggi.

La programmazione dell'ENIAC era affidata a sei donne con formazione matematica — Kay McNulty, Betty Jennings, Betty Snyder, Marlyn Meltzer, Fran Bilas e Ruth Lichterman — che dovevano collegare fisicamente cavi e impostare interruttori. Furono tra le prime programmatrici della storia, ma il loro contributo fu a lungo ignorato.

---

## Dalle valvole ai microprocessori

### Valvole termoioniche (anni '40)

I primi computer elettronici usavano **valvole termoioniche** (o *vacuum tubes*): dispositivi che controllano il flusso di elettroni nel vuoto. Funzionavano, ma erano ingombranti, fragili, consumavano molta energia e si guastavano spesso. L'ENIAC doveva sostituire in media una valvola ogni due giorni.

### Il transistor (1947, Bell Labs)

Nel dicembre 1947, ai **Bell Telephone Laboratories** nel New Jersey, **John Bardeen** e **Walter Brattain**, nel gruppo diretto da **William Shockley**, realizzarono il primo **transistor** funzionante (il 23 dicembre lo presentarono ai dirigenti dei laboratori); Shockley ideò poco dopo il transistor a giunzione. Un transistor fa lo stesso lavoro di una valvola — funziona come un interruttore controllato elettricamente — ma è più piccolo, più veloce, più affidabile, consuma meno energia e costa meno. I tre ricevettero il Nobel per la Fisica nel 1956.

Il transistor è il componente di base di tutta l'elettronica digitale: computer, smartphone e reti sono costruiti con transistor.

### Circuiti integrati (1958)

Nel 1958 **Jack Kilby** alla Texas Instruments (e, indipendentemente, **Robert Noyce** alla Fairchild Semiconductor nel 1959) inventò il **circuito integrato**: l'idea di realizzare più transistor, resistenze e condensatori su un unico pezzo di semiconduttore (Kilby usò il germanio, Noyce il silicio, che divenne lo standard). Questo eliminò la necessità di saldare a mano migliaia di componenti separati e aprì la strada alla miniaturizzazione.

Kilby ricevette il Nobel per la Fisica nel 2000. Noyce, che nel frattempo aveva co-fondato Intel, era morto nel 1990 e il Nobel non si assegna postumo.

### Il microprocessore (1971, Intel 4004)

Nel 1971 Intel mise in commercio l'**Intel 4004**, il primo **microprocessore** commerciale: un'intera CPU su un singolo chip. Il progetto del chip fu guidato da **Federico Faggin**, fisico nato a Vicenza e laureato all'Università di Padova, con Ted Hoff, Stanley Mazor e Masatoshi Shima. Il 4004 aveva 2.300 transistor e una frequenza di clock di 740 kHz. Per confronto, un processore Apple M3 del 2023 contiene circa 25 miliardi di transistor e opera a frequenze di alcuni GHz.

### La legge di Moore

Nel 1965 **Gordon Moore** (allora alla Fairchild, poi co-fondatore di Intel) osservò che il numero di transistor su un circuito integrato raddoppiava ogni anno; nel 1975 corresse la stima a un raddoppio circa ogni due anni. Questa osservazione empirica, nota come **legge di Moore**, ha descritto bene l'andamento per circa cinquant'anni e ha guidato l'industria dei semiconduttori. Non è una legge fisica: è piuttosto una profezia che si autoavvera, un obiettivo che l'industria si è sforzata di raggiungere. Da qualche anno sta rallentando, perché ci si avvicina ai limiti fisici della miniaturizzazione: quando le strutture di un transistor misurano pochi nanometri (poche decine di atomi), effetti quantistici come il *tunneling* rendono difficile controllarne il comportamento.

---

## Domande di verifica

1. Qual è l'idea fondamentale introdotta da George Boole nel 1854? Perché è importante per i computer?

2. Completate la tabella di verità dell'operatore XOR e spiegate in che senso si differenzia dall'OR inclusivo.

3. Perché la porta NAND è definita "universale"? Cosa significa in termini pratici per la costruzione di circuiti?

4. Qual è il contributo di Claude Shannon del 1937 e perché è diverso dal suo contributo del 1948?

5. Spiegate le leggi di De Morgan con un esempio tratto dal linguaggio naturale.

6. In che senso la Macchina Analitica di Babbage anticipava i computer moderni? Quali componenti aveva?

7. Che cos'è la Macchina di Turing e cosa dimostrò Turing con essa?

8. Descrivete la sequenza tecnologica: valvole -> transistor -> circuiti integrati -> microprocessori. Per ciascun passaggio, indicate l'anno e il vantaggio principale.

---

## Esercizi

### Base

1. Costruite la tabella di verità per l'espressione: F = A AND (B OR C).

2. Costruite la tabella di verità per l'espressione: G = (NOT A) OR (A AND B).

3. Verificate, usando le tabelle di verità, che NOT(A OR B) = (NOT A) AND (NOT B) (seconda legge di De Morgan).

4. Un circuito di allarme deve attivarsi (output = 1) quando la porta è aperta (P = 1) e l'allarme è inserito (A = 1). Quale operatore booleano lo descrive? Scrivete la tabella di verità.

### Intermedio

5. Semplificate l'espressione F = (A AND B) OR (A AND NOT B) OR (NOT A AND B). Mostrate ogni passaggio e verificate il risultato con la tabella di verità.

6. Esprimete NOT A, A AND B e A OR B usando **solo** porte NAND. Disegnate (o descrivete a parole) i circuiti risultanti.

7. Un sistema di voto elettronico ha tre membri (A, B, C). La proposta passa se almeno due membri votano a favore. Scrivete l'espressione booleana corrispondente e la sua tabella di verità.

### Avanzato

8. Dimostrate, usando le leggi dell'algebra booleana, che:
   (A OR B) AND (A OR NOT B) = A

9. Un **half adder** (semi-sommatore) è un circuito che somma due bit A e B producendo una Somma (S) e un Riporto (R). Mostrate che S = A XOR B e R = A AND B costruendo le tabelle di verità e confrontandole con l'addizione binaria.

10. Scrivete una breve cronologia (massimo 10 righe) che colleghi Leibniz (1703), Boole (1854), Shannon (1937), Bardeen-Brattain-Shockley (1947), Kilby (1958) e Faggin (1971), indicando come ogni contributo dipenda dai precedenti.

---

## Osservazioni finali

In questa lezione abbiamo percorso un arco temporale molto lungo, dall'abaco ai microprocessori, e un percorso che va dalla logica ai circuiti integrati. In più casi un'idea è stata applicata molto tempo dopo essere stata formulata.

L'algebra di Boole (1854) fu applicata ai circuiti da Shannon nel 1937, oltre ottant'anni dopo. Il sistema binario di Leibniz (1703) entrò nei calcolatori con le macchine a relè degli anni '30 e '40. La Macchina Analitica di Babbage (1837) aveva già memoria, unità di calcolo e salti condizionali, un secolo prima dei computer elettronici, ma non fu mai costruita.

Per voi futuri statistici, la logica booleana è il linguaggio con cui scriverete le condizioni nei vostri programmi (`if`, `and`, `or`, `not`), filtrerete i dati e costruirete query. La storia del calcolo aiuta a capire da dove vengono gli strumenti che userete ogni giorno.

Nella prossima lezione entreremo dentro la macchina: vedremo come sono fatte le componenti di un computer moderno, come collaborano, e perché la loro architettura — ancora oggi basata sul modello descritto da von Neumann nel 1945 — influisce sulle prestazioni dei vostri calcoli statistici.
