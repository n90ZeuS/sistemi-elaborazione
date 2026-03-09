# Lezione 2 — Logica booleana e storia del calcolo

## Introduzione: quando la logica diventa algebra

Nella lezione precedente abbiamo visto come l'informazione si misura in bit e come i numeri si rappresentano in binario. Oggi facciamo un passo concettuale fondamentale: passiamo dai numeri alla **logica**. Vedremo come le operazioni logiche — quelle che usiamo quando diciamo "se piove E non ho l'ombrello, allora mi bagno" — possano essere trattate come operazioni matematiche. E vedremo come questa idea, nata nella mente di un matematico autodidatta nell'Inghilterra vittoriana, sia diventata il fondamento fisico di ogni computer mai costruito.

Dopo aver esplorato la logica booleana, ripercorreremo la storia del calcolo automatico: un viaggio che copre millenni e che ci portera dall'abaco ai microprocessori, passando per alcune delle menti piu brillanti della storia umana.

---

## George Boole e la nascita dell'algebra della logica

**George Boole** (1815-1864) fu un personaggio singolare. Figlio di un calzolaio di Lincoln, in Inghilterra, fu quasi interamente autodidatta: imparo il latino, il greco, il francese e il tedesco da solo, e a sedici anni insegnava gia in una scuola. A vent'anni apri una scuola propria e, nei ritagli di tempo, studiava matematica leggendo i lavori di Lagrange e Laplace.

Nel 1847 pubblico un libretto intitolato *The Mathematical Analysis of Logic*, e nel 1854 la sua opera principale: *An Investigation of the Laws of Thought, on Which are Founded the Mathematical Theories of Logic and Probabilities*. Il titolo e lungo, ma l'idea centrale e rivoluzionaria nella sua semplicita: **la logica puo essere trattata come un'algebra**.

Boole osservo che le proposizioni logiche — affermazioni che possono essere vere o false — si possono manipolare con operazioni simili a quelle dell'algebra ordinaria. Invece di numeri, si lavora con valori di verita; invece di addizione e moltiplicazione, si usano operazioni logiche. I valori possibili sono solo due: **Vero** (1) e **Falso** (0).

Questa scelta — usare 1 e 0, gli stessi simboli del sistema binario — non e una coincidenza: e il ponte che collega la logica astratta ai circuiti elettronici. Ma Boole non poteva saperlo. I computer non esistevano, e sarebbero arrivati quasi un secolo dopo. Boole mori nel 1864, a soli 49 anni (di polmonite, contratta, secondo la leggenda, perche la moglie, credendo nell'omeopatia, lo mise a letto bagnato con secchiate d'acqua fredda per curare la febbre). Non vide mai la realizzazione pratica della sua algebra, ma il suo lavoro cambio il mondo.

---

## Gli operatori booleani fondamentali

### AND (congiunzione logica)

L'operatore AND restituisce Vero solo quando **entrambi** gli operandi sono Veri. Corrisponde alla congiunzione "e" del linguaggio naturale. In notazione matematica si scrive spesso come moltiplicazione: A AND B = A * B, oppure A ∧ B.

**Tabella di verita di AND:**

| A | B | A AND B |
|---|---|---------|
| 0 | 0 |    0    |
| 0 | 1 |    0    |
| 1 | 0 |    0    |
| 1 | 1 |    1    |

*Esempio nella vita reale*: "Supero l'esame SE studio E sono presente all'appello." Entrambe le condizioni devono essere vere.

*Esempio per statistici*: quando filtrate un dataset e chiedete "righe dove eta > 30 AND reddito > 50000", state applicando un AND logico.

### OR (disgiunzione logica)

L'operatore OR restituisce Vero quando **almeno uno** degli operandi e Vero. E importante notare che e un OR **inclusivo**: e vero anche quando entrambi sono veri (a differenza del "o" italiano, che spesso usiamo in senso esclusivo). Si scrive come addizione: A OR B = A + B, oppure A ∨ B.

**Tabella di verita di OR:**

| A | B | A OR B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   1    |

*Esempio nella vita reale*: "Puoi pagare con carta O con contanti." (Anche con entrambi, volendo.)

*Esempio per statistici*: "Seleziona i record dove regione = 'Lazio' OR regione = 'Toscana'."

### NOT (negazione)

L'operatore NOT inverte il valore di verita: cio che era Vero diventa Falso e viceversa. E un operatore **unario** (agisce su un solo operando). Si scrive NOT A, oppure A con una barra sopra, oppure ¬A.

**Tabella di verita di NOT:**

| A | NOT A |
|---|-------|
| 0 |   1   |
| 1 |   0   |

*Esempio nella vita reale*: "Se NON piove, esco senza ombrello."

Con questi tre operatori — AND, OR, NOT — si puo esprimere qualsiasi funzione logica. Sono la base di tutto.

---

## Operatori derivati

### NAND (NOT AND)

NAND e la negazione dell'AND: restituisce Falso solo quando entrambi gli input sono Veri. In tutti gli altri casi restituisce Vero.

**Tabella di verita di NAND:**

| A | B | A NAND B |
|---|---|----------|
| 0 | 0 |    1     |
| 0 | 1 |    1     |
| 1 | 0 |    1     |
| 1 | 1 |    0     |

Il NAND ha una proprieta straordinaria: e un operatore **universale**. Cio significa che qualsiasi funzione logica — AND, OR, NOT, e qualunque altra — puo essere costruita usando **solamente** porte NAND. Questa proprieta, apparentemente teorica, ha un'importanza pratica enorme. I transistor piu semplici ed economici da fabbricare formano naturalmente porte NAND, e l'intera industria dei semiconduttori sfrutta questo fatto. Le memorie flash dei vostri smartphone e SSD si chiamano proprio "NAND flash" per questo motivo.

Vediamo come costruire gli operatori base usando solo NAND:
- **NOT A** = A NAND A (cioe: collegate entrambi gli input allo stesso segnale)
- **A AND B** = NOT (A NAND B) = (A NAND B) NAND (A NAND B)
- **A OR B** = (A NAND A) NAND (B NAND B)

### NOR (NOT OR)

Il NOR e la negazione dell'OR: restituisce Vero solo quando entrambi gli input sono Falsi. Anche il NOR e un operatore universale.

**Tabella di verita di NOR:**

| A | B | A NOR B |
|---|---|---------|
| 0 | 0 |    1    |
| 0 | 1 |    0    |
| 1 | 0 |    0    |
| 1 | 1 |    0    |

### XOR (OR esclusivo)

Lo XOR (*exclusive OR*) restituisce Vero quando gli input sono **diversi** tra loro. E l'equivalente logico del "o" esclusivo italiano: "O l'uno o l'altro, ma non entrambi."

**Tabella di verita di XOR:**

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 |    0    |
| 0 | 1 |    1    |
| 1 | 0 |    1    |
| 1 | 1 |    0    |

Lo XOR e fondamentale nell'aritmetica binaria (e il cuore del circuito sommatore) e nella crittografia. Un'operazione XOR applicata due volte allo stesso valore restituisce il dato originale, proprieta sfruttata in molti algoritmi di cifratura.

---

## Claude Shannon e i circuiti elettrici (1937)

Se Boole creo l'algebra della logica e il sistema binario gia esisteva da secoli (Leibniz lo formalizzo nel 1703), chi li mise insieme e realizzo che si potevano usare per costruire macchine?

La risposta e, ancora una volta, **Claude Shannon**. Lo stesso Shannon della teoria dell'informazione, ma undici anni prima. Nel 1937, Shannon era un ventunenne studente al MIT e stava scrivendo la sua tesi di laurea magistrale (*master's thesis*). Il titolo era: *"A Symbolic Analysis of Relay and Switching Circuits"*. In quella tesi, Shannon dimostro che **l'algebra di Boole descrive perfettamente il comportamento dei circuiti elettrici a rele**.

Un rele e un interruttore controllato elettricamente: puo essere aperto (0) o chiuso (1). Due rele in serie si comportano come un AND (la corrente passa solo se entrambi sono chiusi). Due rele in parallelo si comportano come un OR (la corrente passa se almeno uno e chiuso). Un rele normalmente chiuso che si apre quando riceve un segnale si comporta come un NOT.

Shannon non invento i rele, ne scopri Boole. Il suo genio fu nel **vedere il collegamento**: un ponte tra la matematica pura del XIX secolo e l'ingegneria elettrica del XX. Quella tesi e stata definita "la piu importante tesi di master del XX secolo", e a ragione. Ogni circuito digitale mai progettato — dal calcolatore piu semplice al processore piu potente — si basa su quel collegamento.

---

## Espressioni booleane e semplificazione

Un'**espressione booleana** combina variabili e operatori logici per definire una funzione. Per esempio:

```
F(A, B, C) = (A AND B) OR (NOT A AND C)
```

Questa espressione vale 1 quando A e B sono entrambi 1, oppure quando A e 0 e C e 1.

La **semplificazione** delle espressioni booleane e importante perche un'espressione piu semplice corrisponde a un circuito con meno porte logiche, quindi meno transistor, meno consumo energetico, meno costo e maggiore velocita. Alcune regole utili:

- **Identita**: A AND 1 = A; A OR 0 = A
- **Annullamento**: A AND 0 = 0; A OR 1 = 1
- **Idempotenza**: A AND A = A; A OR A = A
- **Complemento**: A AND (NOT A) = 0; A OR (NOT A) = 1
- **Leggi di De Morgan**: NOT(A AND B) = (NOT A) OR (NOT B); NOT(A OR B) = (NOT A) AND (NOT B)

Le **leggi di De Morgan** sono particolarmente importanti e meritano un esempio. Considerate la frase: "Non e vero che piove e fa freddo." Secondo De Morgan, equivale a: "Non piove oppure non fa freddo." In simboli: NOT(A AND B) = (NOT A) OR (NOT B). Provate a verificarlo con la tabella di verita: i risultati coincidono per tutte le combinazioni di A e B.

**Esempio di semplificazione**:

```
F = (A AND B) OR (A AND NOT B)
  = A AND (B OR NOT B)          [raccogliendo A]
  = A AND 1                     [complemento: B OR NOT B = 1]
  = A                           [identita]
```

L'espressione originale richiedeva 4 porte logiche; quella semplificata ne richiede 0 (e semplicemente il segnale A). Nella progettazione di circuiti integrati con miliardi di transistor, queste semplificazioni fanno la differenza tra un chip che funziona e uno che si surriscalda.

---

## Dai transistor ai circuiti integrati

Prima di tuffarci nella grande storia del calcolo automatico, e utile capire la catena che porta dalla logica booleana ai computer fisici:

1. **Transistor**: un componente elettronico che funziona come un interruttore microscopico. Puo essere acceso o spento, e il suo stato puo essere controllato da un segnale elettrico. Fu inventato nel 1947 ai Bell Labs (ne parleremo tra poco).

2. **Porta logica**: un piccolo circuito composto da pochi transistor che realizza un'operazione booleana (AND, OR, NOT, NAND, ecc.). Una porta NAND a due input richiede tipicamente 4 transistor.

3. **Circuito combinatorio**: una rete di porte logiche che realizza una funzione piu complessa. Per esempio, un sommatore a un bit (che somma due bit e un riporto) si costruisce con un paio di porte XOR e un paio di porte AND e una OR.

4. **Circuito integrato**: milioni (o miliardi) di transistor incisi su una singola piastrina di silicio, che realizzano circuiti combinatori e sequenziali complessi. Un moderno processore contiene decine di miliardi di transistor.

Questo e il filo rosso che va dall'algebra di Boole al chip che esegue i vostri programmi.

---

## Storia del calcolo: dalle origini meccaniche

### L'abaco (circa 2400 a.C.)

La storia del calcolo automatico inizia migliaia di anni fa con l'**abaco**, uno strumento che permette di eseguire operazioni aritmetiche spostando palline lungo aste. L'abaco non "calcola" da solo — e l'operatore umano che esegue i passaggi — ma e il primo esempio di strumento progettato per assistere il calcolo. Versioni dell'abaco furono sviluppate indipendentemente in Mesopotamia, Cina, Giappone e Roma. Il *suanpan* cinese e il *soroban* giapponese sono ancora usati oggi, e un operatore esperto puo eseguire addizioni e sottrazioni con una velocita sorprendente.

### Blaise Pascal e la Pascalina (1642)

**Blaise Pascal** (1623-1662), matematico, fisico e filosofo francese, costrui a soli 19 anni la prima calcolatrice meccanica della storia: la **Pascalina**. La motivazione era pratica e toccante: suo padre, Etienne, era un esattore delle tasse e doveva eseguire interminabili calcoli aritmetici. Il giovane Blaise volle alleviare la sua fatica.

La Pascalina usava un sistema di ruote dentate: girando una ruota, quando questa completava un giro intero (passando dal 9 allo 0), un meccanismo a scatto faceva avanzare di una posizione la ruota successiva, realizzando automaticamente il riporto. Poteva eseguire somme e sottrazioni. Ne furono costruite circa cinquanta esemplari, ma il costo elevato ne impedi la diffusione commerciale.

### Gottfried Leibniz, il sistema binario e l'I Ching (1694)

**Gottfried Wilhelm Leibniz** (1646-1716) e una figura colossale nella storia del pensiero. Co-inventore del calcolo infinitesimale (indipendentemente da Newton), filosofo, diplomatico, e anche inventore di macchine calcolatrici. Nel 1694 costrui la **Stepped Reckoner**, una macchina che poteva eseguire le quattro operazioni aritmetiche grazie a un ingegnoso meccanismo a tamburo scanalato.

Ma il contributo di Leibniz che piu ci interessa e un altro: la formalizzazione del **sistema binario**. Nel suo articolo *"Explication de l'Arithmetique Binaire"* (1703), Leibniz mostro che tutti i numeri si possono esprimere con sole due cifre, 0 e 1. Fu affascinato dal parallelismo con l'**I Ching**, l'antico testo cinese di divinazione, in cui gli esagrammi sono costruiti combinando linee intere (yang) e spezzate (yin) — un sistema binario ante litteram vecchio di tremila anni. Leibniz, uomo profondamente religioso, vide nel binario una metafora della creazione: Dio (1) crea tutto dal nulla (0).

Ci vollero quasi 250 anni perche il sistema binario di Leibniz trovasse la sua applicazione naturale nei circuiti elettronici.

### Charles Babbage e Ada Lovelace: l'alba del computer programmabile

**Charles Babbage** (1791-1871), matematico e ingegnere britannico, e spesso chiamato "il padre del computer". Nel 1822 inizio a progettare la **Macchina Differenziale** (*Difference Engine*), un dispositivo meccanico per calcolare tabelle matematiche eliminando gli errori umani. Ma il progetto piu visionario fu la **Macchina Analitica** (*Analytical Engine*), concepita nel 1837.

La Macchina Analitica, mai completata, anticipava tutte le componenti fondamentali di un computer moderno:
- Un **mulino** (*mill*): l'equivalente dell'unita aritmetico-logica (ALU), che esegue le operazioni.
- Un **magazzino** (*store*): l'equivalente della memoria, che conserva i dati.
- Un sistema di **schede perforate** per fornire istruzioni: l'equivalente di un programma.
- La capacita di eseguire **salti condizionali**: "se il risultato e negativo, vai all'istruzione numero 15."

Babbage, irascibile e perfezionista, non riusci mai a costruirla. Ma una persona capì appieno il potenziale della macchina: **Augusta Ada King, contessa di Lovelace** (1815-1852), figlia del poeta Lord Byron. Ada tradusse un articolo sulla Macchina Analitica scritto dal matematico italiano Luigi Menabrea, aggiungendo note che erano tre volte piu lunghe dell'articolo originale. In quelle note, descrisse un algoritmo per calcolare i numeri di Bernoulli usando la macchina: e considerato il **primo programma della storia**. Ma il contributo piu profondo di Ada fu concettuale: comprese che la macchina non era solo un calcolatore, ma poteva manipolare qualsiasi tipo di simbolo — note musicali, lettere, concetti — purche fosse possibile codificarli in numeri. Un'intuizione che anticipo di un secolo il concetto di *general-purpose computer*.

---

## Alan Turing e la nascita dell'informatica teorica

**Alan Mathison Turing** (1912-1954) e forse la figura piu importante di tutta la storia dell'informatica. Nel 1936, a soli 24 anni, pubblico l'articolo *"On Computable Numbers, with an Application to the Entscheidungsproblem"*, in cui defini un modello matematico di calcolo che oggi chiamiamo **Macchina di Turing**.

### La Macchina di Turing

Una Macchina di Turing e un dispositivo immaginario composto da:
- Un **nastro** infinito diviso in celle, ciascuna contenente un simbolo (per esempio, 0 o 1).
- Una **testina** che puo leggere e scrivere sul nastro e spostarsi di una cella a destra o a sinistra.
- Un **insieme finito di stati** e una **tabella di transizione** che dice: "Se sei nello stato X e leggi il simbolo Y, scrivi il simbolo Z, spostati in direzione D e passa allo stato W."

Questo modello, nella sua disarmante semplicita, e in grado di calcolare tutto cio che e calcolabile. Qualsiasi algoritmo — per quanto complesso — puo essere eseguito da una Macchina di Turing. Questa affermazione, nota come **tesi di Church-Turing**, e uno dei pilastri dell'informatica teorica.

Ma Turing dimostro anche qualcosa di altrettanto profondo: esistono problemi che **nessuna** macchina puo risolvere. Il piu famoso e il **problema della fermata** (*halting problem*): non esiste un algoritmo generale che, dato un programma qualsiasi, possa determinare se quel programma terminera o girera all'infinito.

### Bletchley Park e la decrittazione di Enigma

Durante la Seconda Guerra Mondiale, Turing fu reclutato a **Bletchley Park**, il centro segreto di crittoanalisi britannico. Qui lavoro alla decrittazione di **Enigma**, la macchina cifrante usata dalla marina tedesca. Turing progetto la **Bombe**, una macchina elettromeccanica che automatizzava la ricerca delle chiavi di cifratura. Si stima che il lavoro di Bletchley Park abbia accorciato la guerra di almeno due anni, salvando milioni di vite.

La storia personale di Turing e tragica. Nel 1952 fu condannato per omosessualita (allora reato in Gran Bretagna) e sottoposto a castrazione chimica. Mori nel 1954, apparentemente suicida, mordendo una mela avvelenata con cianuro. Solo nel 2013 ricevette la grazia postuma dalla regina Elisabetta II. La mela morsicata nel logo di Apple non e un riferimento a Turing (secondo Steve Jobs fu una coincidenza), ma molti nella comunita informatica amano pensarlo.

---

## I primi computer elettronici

### Konrad Zuse e lo Z3 (1941)

Mentre Turing lavorava in Inghilterra, in Germania un giovane ingegnere civile, **Konrad Zuse** (1910-1995), costruiva computer nel salotto di casa dei genitori a Berlino. Lo **Z3**, completato nel 1941, e considerato il primo computer programmabile funzionante della storia. Usava rele telefonici (era elettromeccanico, non elettronico), operava in binario, e poteva essere programmato tramite pellicola cinematografica perforata. Zuse lavoro in quasi completo isolamento — non conosceva il lavoro di Turing — e i suoi computer furono distrutti dai bombardamenti alleati. Solo decenni dopo ricevette il riconoscimento che meritava.

### ENIAC (1945)

L'**ENIAC** (*Electronic Numerical Integrator and Computer*), completato nel 1945 all'Universita della Pennsylvania, fu il primo computer **elettronico** general-purpose. Usava circa 18.000 valvole termoioniche, pesava 27 tonnellate, occupava una stanza intera e consumava 150 kilowatt di potenza (abbastanza per alimentare un piccolo quartiere). Poteva eseguire 5.000 addizioni al secondo — impressionante per l'epoca, ma enormemente meno di qualsiasi calcolatrice tascabile di oggi.

Un fatto poco noto: la programmazione dell'ENIAC era affidata a un gruppo di sei donne matematiche — Kay McNulty, Betty Jennings, Betty Snyder, Marlyn Meltzer, Fran Bilas e Ruth Lichterman — che dovevano collegare fisicamente cavi e impostare interruttori. Furono tra le prime programmatrici della storia, ma il loro contributo fu a lungo ignorato.

---

## La grande transizione: dalle valvole ai microprocessori

### Valvole termoioniche (1940s)

I primi computer elettronici usavano **valvole termoioniche** (o *vacuum tubes*): dispositivi che controllano il flusso di elettroni nel vuoto. Funzionavano, ma erano enormi, fragili, consumavano molta energia e si bruciavano continuamente. L'ENIAC doveva sostituire in media una valvola ogni due giorni.

### Il transistor (1947, Bell Labs)

Il 23 dicembre 1947, ai **Bell Telephone Laboratories** nel New Jersey, **John Bardeen**, **Walter Brattain** e **William Shockley** dimostrarono il primo **transistor** funzionante. Un transistor fa lo stesso lavoro di una valvola — funziona come un interruttore controllato elettricamente — ma e piu piccolo, piu veloce, piu affidabile, consuma meno energia e costa meno. I tre ricevettero il Nobel per la Fisica nel 1956.

Il transistor e stato chiamato "la piu grande invenzione del XX secolo", e non e un'esagerazione. Senza di esso, non avremmo computer, smartphone, internet, ne nessuna delle tecnologie digitali che definiscono la nostra epoca.

### Circuiti integrati (1958)

Nel 1958, **Jack Kilby** alla Texas Instruments (e, indipendentemente, Robert Noyce alla Fairchild Semiconductor nel 1959) invento il **circuito integrato**: l'idea di realizzare piu transistor, resistenze e condensatori su un unico pezzo di semiconduttore (tipicamente silicio). Questo elimino la necessita di saldare manualmente migliaia di componenti separati e apri la strada alla miniaturizzazione.

Kilby ricevette il Nobel per la Fisica nel 2000. Noyce, che nel frattempo aveva co-fondato Intel, era gia morto e non pote condividerlo.

### Il microprocessore (1971, Intel 4004)

Nel 1971, un team di ingegneri Intel guidato da **Federico Faggin** (un italiano!) progetto l'**Intel 4004**, il primo **microprocessore** commerciale: un'intera CPU su un singolo chip. Aveva 2.300 transistor e una frequenza di clock di 740 kHz. Per confronto, un processore Apple M3 del 2023 contiene circa 25 miliardi di transistor e opera a frequenze di diversi GHz.

### La legge di Moore

Nel 1965, **Gordon Moore** (co-fondatore di Intel) osservo che il numero di transistor su un circuito integrato raddoppiava approssimativamente ogni due anni. Questa osservazione empirica, nota come **legge di Moore**, si e rivelata straordinariamente accurata per oltre cinquant'anni, guidando l'intera industria dei semiconduttori. Non e una legge fisica — e piuttosto una profezia autoavverante, un obiettivo che l'industria si e sforzata di raggiungere — e da qualche anno sta rallentando, perche ci avviciniamo ai limiti fisici della miniaturizzazione: quando un transistor e largo pochi nanometri (pochi atomi), effetti quantistici come il *tunneling* rendono il suo comportamento imprevedibile.

---

## Domande di verifica

1. Qual e l'idea fondamentale introdotta da George Boole nel 1854? Perche fu rivoluzionaria?

2. Completate la tabella di verita dell'operatore XOR e spiegate in che senso si differenzia dall'OR inclusivo.

3. Perche la porta NAND e definita "universale"? Cosa significa in termini pratici per la costruzione di circuiti?

4. Qual e il contributo di Claude Shannon del 1937 e perche e diverso dal suo contributo del 1948?

5. Spiegate le leggi di De Morgan con un esempio tratto dal linguaggio naturale.

6. In che senso la Macchina Analitica di Babbage anticipava i computer moderni? Quali componenti aveva?

7. Che cos'e la Macchina di Turing e cosa dimostro Turing con essa?

8. Descrivete la sequenza tecnologica: valvole -> transistor -> circuiti integrati -> microprocessori. Per ciascun passaggio, indicate l'anno e il vantaggio principale.

---

## Esercizi

### Base

1. Costruite la tabella di verita per l'espressione: F = A AND (B OR C).

2. Costruite la tabella di verita per l'espressione: G = (NOT A) OR (A AND B).

3. Verificate, usando le tabelle di verita, che NOT(A OR B) = (NOT A) AND (NOT B) (seconda legge di De Morgan).

4. Un circuito di allarme deve attivarsi (output = 1) quando la porta e aperta (P = 1) e l'allarme e inserito (A = 1). Quale operatore booleano lo descrive? Scrivete la tabella di verita.

### Intermedio

5. Semplificate l'espressione F = (A AND B) OR (A AND NOT B) OR (NOT A AND B). Mostrate ogni passaggio e verificate il risultato con la tabella di verita.

6. Esprimete NOT A, A AND B e A OR B usando **solo** porte NAND. Disegnate (o descrivete a parole) i circuiti risultanti.

7. Un sistema di voto elettronico ha tre membri (A, B, C). La proposta passa se almeno due membri votano a favore. Scrivete l'espressione booleana corrispondente e la sua tabella di verita.

### Avanzato

8. Dimostrate, usando le leggi dell'algebra booleana, che:
   (A OR B) AND (A OR NOT B) = A

9. Un **half adder** (semi-sommatore) e un circuito che somma due bit A e B producendo una Somma (S) e un Riporto (R). Mostrate che S = A XOR B e R = A AND B costruendo le tabelle di verita e confrontandole con l'addizione binaria.

10. Scrivete una breve cronologia (massimo 10 righe) che colleghi Leibniz (1703), Boole (1854), Shannon (1937), Bardeen-Brattain-Shockley (1947), Kilby (1958), e Faggin (1971), evidenziando come ogni contributo dipenda dai precedenti.

---

## Osservazioni finali

In questa lezione abbiamo percorso un arco temporale enorme — dall'abaco sumero ai microprocessori — e un arco concettuale altrettanto vasto — dalla logica filosofica ai circuiti integrati. Il filo conduttore e questo: le idee astratte, quando trovano il contesto giusto, diventano tecnologie concrete che cambiano il mondo.

L'algebra di Boole dormi per quasi un secolo prima che Shannon la svegliasse. Il sistema binario di Leibniz attese 250 anni prima di incontrare i transistor. La Macchina Analitica di Babbage anticipo i computer di un secolo, ma non pote essere costruita con la tecnologia dell'epoca. Questa storia ci ricorda che il progresso non e lineare: e fatto di intuizioni geniali che aspettano — a volte per generazioni — le condizioni materiali per realizzarsi.

Per voi futuri statistici, la logica booleana non e un esercizio accademico: e il linguaggio con cui scriverete le condizioni nei vostri programmi (`if`, `and`, `or`, `not`), filtrerete i dati, e costruirete query. E la storia del calcolo vi da la prospettiva per capire da dove vengono gli strumenti che userete ogni giorno.

Nella prossima lezione entreremo dentro la macchina: vedremo come sono fatte le componenti di un computer moderno, come collaborano, e perche la loro architettura — ancora oggi basata sulle idee di von Neumann del 1945 — determina le prestazioni dei vostri calcoli statistici.
