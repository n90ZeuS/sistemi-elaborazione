# Lezione 5 — Rappresentazione dei dati

## Introduzione

Ogni dato con cui lavorerete nella vostra carriera di statistici — un reddito, un nome, una temperatura, un'immagine medica, un tracciato audio — all'interno del computer è una sequenza di bit. Ma come si passa da un numero reale a una sequenza di 0 e 1? E soprattutto: **cosa si perde in questa traduzione?**

Questa lezione è forse la più importante per uno statistico che vuole capire le macchine. Non perché i dettagli tecnici delle codifiche siano affascinanti in sé (anche se lo sono), ma perché le scelte di rappresentazione hanno conseguenze concrete e talvolta devastanti: razzi che esplodono, missili che mancano il bersaglio, geni umani rinominati per errore. Comprendere come il computer rappresenta i dati vi proteggerà da errori che altrimenti sarebbero invisibili.

---

## Numeri interi

### Rappresentazione in binario

I numeri interi positivi si rappresentano in binario nel modo naturale che abbiamo visto nella prima lezione: il numero 42 in base 10 diventa 101010 in base 2. Con *n* bit si possono rappresentare i numeri da 0 a 2ⁿ − 1: con 8 bit, da 0 a 255; con 32 bit, da 0 a circa 4,3 miliardi.

### Il problema dei numeri negativi

Ma come rappresentare i numeri negativi? Servono le stesse sequenze di bit per codificare sia positivi che negativi. Nel corso della storia sono state proposte diverse soluzioni.

**Modulo e segno:** il primo bit indica il segno (0 = positivo, 1 = negativo) e i restanti bit il valore assoluto. Semplice da capire, ma problematico: esistono due rappresentazioni dello zero (+0 e -0) e la sottrazione richiede circuiti speciali.

**Complemento a uno:** per ottenere il negativo di un numero, si invertono tutti i bit. Anche qui, due zeri e complicazioni aritmetiche.

**Complemento a due:** la soluzione elegante adottata universalmente. Per ottenere il negativo di un numero: si invertono tutti i bit e si aggiunge 1. La proprietà geniale del complemento a due è che **la sottrazione diventa un'addizione**: per calcolare A − B, basta calcolare A + (−B), usando lo stesso circuito sommatore. Con un unico circuito si eseguono sia somme che sottrazioni. Inoltre, esiste un solo zero.

Con *n* bit in complemento a due si rappresentano i numeri da −2ⁿ⁻¹ a 2ⁿ⁻¹ − 1. Con 32 bit: da −2.147.483.648 a 2.147.483.647 (circa ±2,1 miliardi).

### Overflow: quando i numeri "traboccano"

Cosa succede quando il risultato di un'operazione è troppo grande per la rappresentazione? Si verifica un **overflow**: i bit in eccesso vengono persi e il risultato è sbagliato, spesso silenziosamente (senza messaggi di errore).

Due casi celebri mostrano la gravità del problema:

**Il bug dell'anno 2038.** Molti sistemi Unix rappresentano il tempo come il numero di secondi trascorsi dal 1° gennaio 1970 (il cosiddetto *Unix epoch*), memorizzato come un intero con segno a 32 bit. Il 19 gennaio 2038 alle ore 03:14:07 UTC, questo contatore raggiungerà il valore massimo (2.147.483.647) e andrà in overflow, tornando a un valore negativo. I sistemi che non saranno aggiornati interpreteranno la data come il 13 dicembre 1901. La soluzione: passare a interi a 64 bit (già in corso nei sistemi moderni).

**L'esplosione dell'Ariane 5 (1996).** Il razzo europeo Ariane 5 esplose 37 secondi dopo il lancio. La causa: un software ereditato dal predecessore Ariane 4 convertiva un valore di velocità orizzontale da un numero in virgola mobile a 64 bit in un intero con segno a 16 bit. L'Ariane 5, più veloce dell'Ariane 4, generava un valore che non stava in 16 bit: overflow, errore di navigazione, autodistruzione. Danni: 370 milioni di dollari. Un bug di conversione di tipo.

### Python e gli interi a precisione arbitraria

Python ha una caratteristica unica tra i linguaggi più diffusi: i suoi interi hanno **precisione arbitraria**. Non c'è limite alla dimensione di un numero intero in Python: internamente, Python alloca dinamicamente la memoria necessaria per rappresentarlo.

```python
# In C, questo causerebbe overflow con un int a 32 bit:
risultato: int = 2 ** 100
print(risultato)  # 1267650600228229401496703205376

# Python gestisce numeri arbitrariamente grandi:
fattoriale_100: int = 1
for i in range(1, 101):
    fattoriale_100 *= i
print(fattoriale_100)  # un numero con 158 cifre!
```

Il prezzo di questa comodità è una leggera penalità di prestazioni: le operazioni su interi grandi sono più lente che in linguaggi con interi a dimensione fissa. Ma per la maggior parte delle applicazioni statistiche, la correttezza è più importante della velocità.

---

## Numeri in virgola mobile (floating point)

### Il problema fondamentale

Come rappresentare i numeri reali — che sono infiniti e continui — con un numero finito di bit — che sono discreti? La risposta è: **non perfettamente**. La rappresentazione in virgola mobile è un'approssimazione, e comprenderne i limiti è essenziale per chiunque lavori con dati numerici.

### Lo standard IEEE 754

Nel 1985, l'IEEE (*Institute of Electrical and Electronics Engineers*) pubblicò lo standard **IEEE 754**, che definisce come i numeri in virgola mobile devono essere rappresentati e manipolati. Prima di questo standard, ogni produttore di computer usava la propria rappresentazione, con risultati diversi per gli stessi calcoli.

L'idea è una versione binaria della **notazione scientifica**. Così come scriviamo 6,022 × 10²³ in base 10, in IEEE 754 un numero è rappresentato come:

**(-1)ˢ × 1,mantissa × 2^(esponente-bias)**

dove:
- **s** è il bit di segno (0 = positivo, 1 = negativo)
- **mantissa** (o significando) contiene le cifre significative
- **esponente** determina l'ordine di grandezza

Esistono due formati principali:

| Formato | Bit totali | Bit segno | Bit esponente | Bit mantissa | Cifre decimali significative |
|---------|-----------|-----------|--------------|-------------|----------------------------|
| Single precision | 32 | 1 | 8 | 23 | ~7 |
| Double precision | 64 | 1 | 11 | 52 | ~15-16 |

Python usa la **double precision** per i suoi `float`: 64 bit, con circa 15-16 cifre decimali di precisione.

Lo standard definisce anche valori speciali:
- **+∞ e −∞:** risultato di divisioni come `1.0 / 0.0` (in Python: `float('inf')`)
- **NaN** (*Not a Number*): risultato di operazioni indeterminate come `0.0 / 0.0` o `float('inf') - float('inf')`. NaN ha la proprietà unica che `NaN != NaN` è `True` — è l'unico valore non uguale a se stesso.

### Perché 0.1 + 0.2 ≠ 0.3

Questo è il momento della verità. Aprite un qualsiasi interprete Python e digitate:

```python
>>> 0.1 + 0.2
0.30000000000000004
```

Non è un bug di Python. Succede in **qualsiasi** linguaggio di programmazione che usa IEEE 754 (cioè praticamente tutti). Il motivo è fondamentale: il numero 0,1 in base 10 è un **numero periodico** in base 2, esattamente come 1/3 = 0,333... è periodico in base 10.

Non potendo rappresentare esattamente 0,1 in binario, il computer memorizza l'approssimazione più vicina possibile a 64 bit. Lo stesso per 0,2. La somma di queste due approssimazioni produce un risultato che è *quasi* 0,3, ma non esattamente.

### Implicazioni per la statistica

Questo ha conseguenze importanti:

**Mai confrontare float con `==`.** Il codice `if media == 0.3:` potrebbe non funzionare come vi aspettate. Usate invece:
```python
import math
if math.isclose(media, 0.3, rel_tol=1e-9):
    print("Approssimativamente uguale")
```

**Errori di accumulazione.** Se sommate milioni di piccoli numeri, gli errori di arrotondamento si accumulano. In statistica, questo può distorcere medie, varianze e test statistici su grandi campioni. Algoritmi numericamente stabili (come l'algoritmo di Kahan per la somma) mitigano il problema.

**Il modulo `decimal`.** Per calcoli finanziari o dove la precisione decimale esatta è cruciale, Python offre il modulo `decimal`:
```python
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3 (esatto!)
```

**Pandas e NaN.** In Pandas, i valori mancanti nelle colonne numeriche sono rappresentati come `NaN` (Not a Number) IEEE 754. Comprendere la natura di NaN — che non è uguale a nulla, nemmeno a se stesso — è essenziale per la pulizia dei dati.

### Il disastro del Patriot (1991)

Il 25 febbraio 1991, durante la Guerra del Golfo, una batteria di missili Patriot a Dhahran, Arabia Saudita, non intercettò un missile Scud iracheno, che colpì una caserma uccidendo 28 soldati americani.

La causa: il sistema del Patriot misurava il tempo in decimi di secondo usando un registro a 24 bit. Il numero 0,1 in binario è periodico, e l'errore di troncamento, piccolissimo a ogni singolo tick (circa 0,000000095 secondi), si **accumulava** nel tempo. Dopo 100 ore di funzionamento continuo, l'errore cumulato era di circa 0,34 secondi — sufficiente perché il Patriot cercasse lo Scud in una posizione sbagliata di oltre 600 metri.

Un errore di arrotondamento floating point ha causato la morte di 28 persone. Ecco perché questa lezione è importante.

---

## Testo e codifiche

### Il problema

Come rappresentare lettere, cifre e simboli con sequenze di bit? La risposta sembra semplice: assegnare un numero a ogni carattere. Ma *quale* numero a *quale* carattere? E quanti bit per carattere?

### ASCII (1963)

Lo standard **ASCII** (*American Standard Code for Information Interchange*) fu pubblicato nel 1963. Usa 7 bit per carattere, codificando 128 simboli:

- 26 lettere maiuscole (A-Z): codici 65-90
- 26 lettere minuscole (a-z): codici 97-122
- 10 cifre (0-9): codici 48-57
- Simboli di punteggiatura e speciali: `! @ # $ % ...`
- Caratteri di controllo: a capo, tabulazione, ecc.

ASCII funzionava perfettamente — per l'inglese. Ma non prevedeva lettere accentate (à, è, ù), la ñ spagnola, l'ü tedesca, per non parlare del cirillico, del giapponese o dell'arabo.

### Il caos delle estensioni

Negli anni successivi, ogni paese e produttore creò le proprie estensioni di ASCII a 8 bit (256 caratteri):

- **ISO 8859-1** (Latin-1): per le lingue dell'Europa occidentale (include à, è, ù, ñ, ü)
- **ISO 8859-5**: per il cirillico
- **Shift-JIS**: per il giapponese
- **GB2312**: per il cinese semplificato

Il risultato fu il caos: lo stesso byte poteva rappresentare un carattere diverso a seconda della codifica. Un file scritto in Shift-JIS e aperto come Latin-1 mostra un'accozzaglia di simboli senza senso. Questo fenomeno ha un nome giapponese: **mojibake** (文字化け, "caratteri trasformati").

Se avete mai aperto un CSV e visto "caffÃ¨" al posto di "caffè", avete sperimentato il mojibake — la codifica del file non corrispondeva alla codifica usata per leggerlo.

### Unicode e UTF-8

**Unicode** (1991-oggi) è il progetto ambizioso di codificare **ogni carattere di ogni sistema di scrittura umano** (e non solo: emoji, simboli matematici, note musicali, scritture antiche). Ad oggi include oltre 150.000 caratteri da 161 scritture diverse.

Unicode assegna a ogni carattere un **code point** univoco, scritto come U+XXXX. Ad esempio: A = U+0041, à = U+00E0, 你 = U+4F60, 🎓 = U+1F393.

Ma Unicode è un *catalogo*, non una codifica. Come si memorizzano concretamente questi code point in byte? Esistono diverse codifiche:

**UTF-8** è la codifica che ha vinto. Fu inventata nel 1992 da **Ken Thompson** (il co-creatore di Unix) e **Rob Pike**, su una tovaglietta di carta durante una cena in un ristorante di New Jersey. Le sue proprietà sono geniali:

- **Compatibile con ASCII:** i primi 128 caratteri sono identici ad ASCII, usando un solo byte. Questo significa che qualsiasi file ASCII è automaticamente un file UTF-8 valido.
- **Lunghezza variabile:** i caratteri comuni (latini) usano 1 byte, i caratteri meno comuni (cinese, giapponese, arabo) usano 2-4 byte. Efficiente senza sprecare spazio.
- **Auto-sincronizzante:** è impossibile confondere un byte iniziale con un byte di continuazione, rendendo la decodifica robusta.

Oggi, oltre il 97% delle pagine web usa UTF-8. È lo standard de facto di internet.

### Python 3 e Unicode

Python 3 ha fatto una scelta radicale: le stringhe (`str`) sono Unicode nativamente. Ogni stringa Python è una sequenza di caratteri Unicode, indipendentemente dalla lingua:

```python
nome: str = "François"
citta: str = "東京"       # Tokyo in giapponese
saluto: str = "Ciao 👋"  # con emoji
print(len(saluto))        # 6 (emoji conta come 1 carattere)
```

Il temuto `UnicodeDecodeError` si verifica quando tentate di leggere un file con la codifica sbagliata:

```python
# Se il file è codificato in Latin-1 ma provate a leggerlo come UTF-8:
with open("dati.csv", encoding="utf-8") as f:
    f.read()  # UnicodeDecodeError!

# Soluzione: specificare la codifica corretta
with open("dati.csv", encoding="latin-1") as f:
    f.read()  # Funziona!
```

**Consiglio pratico:** salvate sempre i vostri file in UTF-8. Quando leggete file di terze parti e ottenete errori di codifica, provate `encoding="latin-1"` o `encoding="cp1252"` (la codifica di Windows per l'Europa occidentale).

---

## Immagini, audio e video

### Immagini digitali

Un'immagine digitale è una griglia di **pixel** (*picture element*). Ogni pixel ha un colore, e il colore è rappresentato da numeri.

Il modello di colore più comune è **RGB** (*Red, Green, Blue*): ogni pixel è definito da tre valori, uno per l'intensità di rosso, verde e blu. Con 8 bit per canale (256 livelli), un pixel richiede 24 bit (3 byte) e può assumere 256³ = 16.777.216 colori diversi.

- **Risoluzione:** il numero di pixel (es: 1920×1080 = circa 2 milioni di pixel = 2 megapixel).
- **Profondità di colore:** il numero di bit per canale (8, 16, 32 bit).

**L'intuizione fondamentale:** un'immagine è una **matrice di numeri**. Un'immagine RGB 1920×1080 è un array tridimensionale di dimensione 1080 × 1920 × 3. Questo è esattamente il tipo di dato che NumPy gestisce in modo nativo. L'analisi di immagini è, in fondo, algebra lineare applicata.

I formati più comuni:
- **BMP:** non compresso. Un'immagine 1920×1080 a 24 bit occupa circa 6 MB.
- **JPEG:** compressione **con perdita** (*lossy*). Riduce drasticamente la dimensione scartando dettagli impercettibili all'occhio umano. Ma ogni salvataggio perde qualità: non salvate ripetutamente in JPEG un'immagine su cui state lavorando.
- **PNG:** compressione **senza perdita** (*lossless*). Il file è più piccolo del BMP ma identico all'originale. Supporta la trasparenza.

### Audio digitale

Un suono è un'onda continua. Per digitalizzarlo, lo si **campiona**: si misura l'ampiezza dell'onda a intervalli regolari.

Il **teorema di Nyquist-Shannon** stabilisce che per catturare fedelmente un suono, bisogna campionarlo ad almeno **il doppio della sua frequenza massima**. L'orecchio umano percepisce suoni fino a circa 20.000 Hz, quindi servono almeno 40.000 campioni al secondo. Il CD audio usa 44.100 Hz e 16 bit per campione — ecco perché questi numeri non sono arbitrari.

### Video digitale

Un video è una sequenza di immagini (frame) accompagnata da una traccia audio. A 30 frame al secondo, un video Full HD non compresso richiederebbe circa 6 MB × 30 = 180 MB al secondo, cioè circa 650 GB per un'ora. La **compressione video** (codec H.264, H.265, AV1) sfrutta la ridondanza tra frame consecutivi per ridurre enormemente la dimensione.

### Perché è rilevante per la statistica

I dati statistici moderni non sono solo tabelle di numeri. L'analisi di immagini mediche (radiografie, risonanze), i dati satellitari, l'analisi del parlato, il riconoscimento di pattern in video — tutto questo richiede che uno statistico comprenda la natura digitale di questi dati.

---

## Formati di dati strutturati

### CSV (Comma-Separated Values)

Il formato più semplice e più usato in statistica: un file di testo dove ogni riga è un record e i campi sono separati da un delimitatore (tipicamente la virgola).

```
nome,cognome,voto,data_esame
Mario,Rossi,28,2024-01-15
Anna,Bianchi,30,2024-01-15
```

**Vantaggi:** universale, leggibile, supportato da qualsiasi software.

**Problemi:** nessun tipo di dato (tutto è testo), ambiguità con i separatori (cosa succede se un campo contiene una virgola?), nessuno standard rigido sui dettagli.

**La trappola europea:** in Italia e in molti paesi europei, il separatore decimale è la virgola (3,14 non 3.14). Per evitare conflitti con il separatore CSV, si usa il **punto e virgola** come separatore di campo. Quando leggete un CSV e vedete dati illeggibili, verificate sempre il separatore.

### JSON (JavaScript Object Notation)

Formato per dati strutturati gerarchicamente, nato dal mondo JavaScript ma ormai universale. È il formato standard delle API web.

```json
{
    "nome": "Mario",
    "cognome": "Rossi",
    "voti": [28, 30, 27],
    "indirizzo": {
        "citta": "Milano",
        "cap": "20100"
    }
}
```

JSON supporta tipi di dato: stringhe, numeri, booleani, null, array e oggetti annidati. È leggibile da umani e facile da elaborare per le macchine.

### XML (eXtensible Markup Language)

Più verboso di JSON ma più espressivo, ancora diffuso nei contesti istituzionali:

```xml
<studente>
    <nome>Mario</nome>
    <cognome>Rossi</cognome>
    <voto>28</voto>
</studente>
```

Lo troverete nei dati della pubblica amministrazione, nei servizi web SOAP, nei file di configurazione.

### Excel (.xlsx)

Onnipresente nel mondo aziendale e spesso usato (impropriamente) come formato di scambio dati. I problemi per l'uso scientifico sono seri:

- **Conversioni automatiche non richieste:** il caso più famoso riguarda la genetica. Excel convertiva automaticamente nomi di geni come MARCH1 e SEPT2 in date (1 marzo, 2 settembre). Il problema era così diffuso che nel 2020 l'organizzazione HUGO Gene Nomenclature Committee **ha rinominato 27 geni umani** per evitare le conversioni di Excel. Un software ha costretto la scienza a cambiare i nomi dei geni.
- Formattazione che si perde nel trasferimento.
- Limiti sul numero di righe (1.048.576).
- Formato binario proprietario.

### Formati binari per grandi dataset

Quando i dataset diventano grandi (milioni di righe, gigabyte), i formati testuali come CSV diventano lenti. Esistono formati binari ottimizzati:

- **Parquet:** formato colonnare (memorizza i dati per colonna anziché per riga), compressione efficiente, tipi nativi. Ideale per l'analisi di grandi dataset con Pandas.
- **HDF5:** formato gerarchico per dati scientifici, usato in fisica, astronomia, bioinformatica.
- **Feather:** formato ottimizzato per lo scambio veloce di DataFrame tra Python e R.

---

## Domande di verifica

1. **Cos'è il complemento a due e perché è stato scelto come rappresentazione standard per gli interi negativi?**

2. **Perché `0.1 + 0.2` non è esattamente `0.3` in Python?** È un bug di Python?

3. **Cosa sono overflow e underflow?** Descrivete un caso reale in cui l'overflow ha avuto conseguenze gravi.

4. **Cos'è il mojibake e perché si verifica?** Come si risolve?

5. **Perché UTF-8 ha vinto sulle altre codifiche?** Elencate le sue proprietà chiave.

6. **Perché non si dovrebbero confrontare due float con `==`?** Quale alternativa offre Python?

7. **Un'immagine RGB 800×600 a 8 bit per canale quanti byte occupa senza compressione?** Quale formato usereste per salvarla senza perdita di qualità?

8. **Perché Excel è problematico come formato per dati scientifici?** Descrivete il caso dei geni rinominati.

---

## Esercizi

### Base

1. Rappresentate il numero −13 in complemento a due usando 8 bit. Verificate sommandolo a +13: il risultato deve essere 0 (ignorando il bit di riporto).

2. In Python, calcolate:
   ```python
   print(0.1 + 0.2 == 0.3)
   print(0.1 + 0.2)
   ```
   Spiegate il risultato. Poi riscrivete il confronto usando `math.isclose()`.

3. Quanti caratteri ASCII esistono? Perché ASCII non è sufficiente per l'italiano?

### Intermedio

4. Un'immagine ha risoluzione 3840×2160 (4K) con 24 bit per pixel. Calcolate:
   - La dimensione non compressa in MB.
   - Quante immagini di questo tipo stanno in 1 GB di RAM.
   - La dimensione approssimativa in JPEG con rapporto di compressione 10:1.

5. Scrivete un breve programma Python che dimostra che gli interi Python hanno precisione arbitraria, calcolando 2¹⁰⁰⁰. Poi mostrate che i float hanno precisione limitata calcolando `float(2**1000)`.

6. Aprite un file di testo in Python prima con `encoding="utf-8"`, poi con `encoding="latin-1"`. Se il file contiene caratteri accentati, osservate le differenze. Cosa succede con l'encoding sbagliato?

### Avanzato

7. Scrivete un programma Python che simula l'errore cumulativo del sistema Patriot: partite dal valore 0,1 e sommatelo a se stesso 1.000.000 di volte. Confrontate il risultato con 100.000 (il risultato matematicamente corretto). Quanto è grande l'errore? Poi ripetete usando il modulo `decimal`.

8. Un collega vi invia un file CSV che quando aperto mostra `"caffÃ¨"` al posto di `"caffè"` e `"â‚¬"` al posto di `"€"`. Spiegate tecnicamente cosa è successo (quale codifica è stata usata per scrivere e quale per leggere). Come risolvereste il problema in Python?

---

## Osservazioni finali

Questa lezione ci ha insegnato una verità fondamentale: **la rappresentazione digitale dei dati è sempre un'approssimazione**. I numeri interi possono traboccare, i numeri reali perdono precisione, i testi possono essere fraintesi, le immagini perdono dettagli nella compressione. Nessun dato digitale è perfetto.

Per uno statistico, questa consapevolezza è particolarmente importante:

1. **Non fidatevi ciecamente dei numeri.** Quando calcolate una media con 15 cifre decimali, solo le prime 15-16 sono significative. L'illusione di precisione può essere pericolosa.

2. **Conoscete i vostri dati.** Prima di analizzare un dataset, chiedetevi: come sono codificati i numeri? Qual è l'encoding del testo? Ci sono valori mancanti rappresentati come NaN? Ci sono conversioni implicite?

3. **Scegliete il formato giusto.** CSV per la semplicità e la portabilità. Parquet per le prestazioni su grandi dataset. JSON per i dati gerarchici. Mai Excel per il lavoro scientifico serio.

Nella prossima lezione faremo il grande salto dalla macchina al pensiero: parleremo di algoritmi, programmi, processi e del pensiero computazionale — il ponte tra capire il computer e dirgli cosa fare.
