# Laboratorio 7 — NumPy e Pandas

**Prerequisiti:** lezioni T17 (NumPy, Pandas e visualizzazione).

Oggi ci sono solo esercizi, in ordine di difficoltà: i primi quattro con NumPy, gli altri con Pandas. Per ogni esercizio create un file `.py` con il nome indicato e importate `numpy as np` e `pandas as pd` all'inizio. I file CSV sono scritti nella slide dell'esercizio: create il file con l'editor nella stessa cartella e copiate il contenuto, compresa l'intestazione. Quando i dati sono casuali usate il seed indicato e fate le estrazioni nell'ordine della consegna: così i numeri coincidono con l'esempio. Alla fine c'è una challenge a scelta tra 5 temi.

Ogni esercizio ha la consegna, un esempio di esecuzione e alcuni casi da provare: il programma è corretto quando dà gli stessi risultati. Alla fine c'è una challenge a scelta tra 5 temi. Le soluzioni le vediamo all'inizio del laboratorio L08.

| # | File | Esercizio |
|---|---|---|
| 1 | `voti_numpy.py` | I voti in un array |
| 2 | `ore_studio.py` | Le ore di studio |
| 3 | `altezze.py` | Altezze simulate |
| 4 | `test_crocette.py` | Rispondere a caso |
| 5 | `libretto.py` | Il libretto in un DataFrame |
| 6 | `esami_csv.py` | Esplorare un CSV |
| 7 | `pulizia_questionario.py` | Pulire un questionario |
| 8 | `esami_primo_anno.py` | Gli esami del primo anno |
| Challenge | a scelta | Mercati e finanza · Sport · Imprese e marketing · Salute e scienza · Caso e probabilità |

---

## Promemoria

Gli strumenti che servono oggi. Con NumPy le operazioni si fanno su tutto l'array, senza cicli: `voti + 1`, `voti >= 18`, `np.mean(voti)`. Un array di booleani usato tra parentesi quadre filtra gli elementi; sommato conta i `True`. Con Pandas una colonna di un DataFrame è una Series: si calcola, si filtra e si raggruppa allo stesso modo. Niente `pivot_table` e niente grafici: arrivano in L08.

```python
import numpy as np
import pandas as pd

voti: np.ndarray = np.array([28, 17, 30, 24])
print(voti + 1, np.mean(voti))         # [29 18 31 25] 24.75
print(voti[voti >= 18])                # filtro: [28 30 24]
rng = np.random.default_rng(42)        # stesso seed, stessi numeri
dadi: np.ndarray = rng.integers(1, 7, size=1000)
print(np.mean(dadi == 6))              # stima di 1/6
df: pd.DataFrame = pd.DataFrame({"corso": ["Stat", "Stat", "Info"],
                                 "voto": [28, 24, 30]})
df["promosso"] = df["voto"] >= 18      # colonna calcolata
print(df[df["voto"] > 25])             # righe filtrate
print(df.groupby("corso")["voto"].mean())  # media per gruppo
```

---

## Esercizio 1 — I voti in un array (`voti_numpy.py`)

**Consegna**

1. Create l'array `voti` con i voti di un appello: 28, 17, 30, 24, 15, 21, 27, 19, 30, 23. Stampate la forma (`.shape`) e il tipo degli elementi (`.dtype`).
2. Calcolate media e mediana con un decimale e la deviazione standard campionaria (`np.std(voti, ddof=1)`) con due decimali.
3. Con il filtro `voti[voti >= 18]` ottenete i voti dei promossi. Contateli con `np.sum(voti >= 18)`, perché ogni `True` vale 1, e stampate la percentuale, i voti e la loro media.
4. Senza cicli calcolate gli scarti dalla media (`voti - media`), stampateli arrotondati con `np.round(scarti, 1)` e stampate la loro somma con un decimale.

**Esempio di esecuzione**

```
Forma: (10,), tipo: int64
Media: 23.4, mediana: 23.5
Dev. std campionaria: 5.36
Promossi: 8 su 10 (80.0%)
Voti dei promossi: [28 30 24 21 27 19 30 23]
Media dei promossi: 25.2
Scarti dalla media: [ 4.6 -6.4  6.6  0.6 -8.4 -2.4  3.6 -4.4  6.6 -0.4]
Somma degli scarti: 0.0
```

**Provate anche**

- aggiungete il voto 18 → `Promossi: 9 su 11 (81.8%)`, `Media dei promossi: 24.4`; la somma degli scarti esce `-0.0`, per l'arrotondamento dei float
- togliete `ddof=1` → `5.08`: `np.std` divide per n invece che per n − 1

---

## Esercizio 2 — Le ore di studio (`ore_studio.py`)

**Consegna**

1. Una matrice contiene le ore di studio di 4 settimane (righe) per 3 corsi (colonne: Statistica, Analisi, Informatica). Le righe sono `[6, 4, 3]`, `[8, 5, 2]`, `[5, 7, 4]` e `[10, 6, 5]`.
2. Stampate forma e ore totali. Sommate per corso con `np.sum(ore, axis=0)` e per settimana con `axis=1`.
3. Dividete le ore per corso per il totale (un array diviso uno scalare) e stampate la quota di ogni corso, scorrendo nomi e quote con `zip`.
4. Create i numeri delle settimane con `np.arange(1, ore.shape[0] + 1)` e filtrate quelle con più di 15 ore.
5. Calcolate la media per corso (`np.mean(ore, axis=0)`) e sottraetela a tutta la matrice: con il broadcasting la riga delle medie viene ripetuta su ogni settimana. Stampate le medie e la matrice degli scarti.

**Esempio di esecuzione**

```
Forma: (4, 3), ore totali: 65
Ore per corso: [29 22 14]
Ore per settimana: [13 15 16 21]
Statistica: 44.6%
Analisi: 33.8%
Informatica: 21.5%
Settimane oltre 15 ore: [3 4]
Medie per corso: [7.25 5.5  3.5 ]
Scarti dalla media del corso:
[[-1.25 -1.5  -0.5 ]
 [ 0.75 -0.5  -1.5 ]
 [-2.25  1.5   0.5 ]
 [ 2.75  0.5   1.5 ]]
```

**Provate anche**

- aggiungete la settimana `[7, 3, 6]` → `Forma: (5, 3), ore totali: 81`, `Settimane oltre 15 ore: [3 4 5]`
- sommate la matrice degli scarti con `axis=0` → `[0. 0. 0.]`: in ogni colonna gli scarti dalla media si compensano

---

## Esercizio 3 — Altezze simulate (`altezze.py`)

**Consegna**

1. Create il generatore `rng = np.random.default_rng(42)` e simulate 500 altezze in cm con `rng.normal(loc=170, scale=10, size=500)`. Stampate le prime 5 (`altezze[:5]`) arrotondate a un decimale.
2. Stampate media, deviazione standard campionaria, minimo e massimo con un decimale.
3. Standardizzate senza cicli: `z = (altezze - media) / dev`. Controllate che la deviazione standard degli z sia 1.
4. `np.abs(z) <= 1` è un array di booleani e `np.mean` ne dà la quota di `True`. Stampate la quota entro 1 deviazione standard e quella oltre 2, accanto ai valori teorici della normale: 68.3% e 4.6%.
5. Contate le altezze tra 185 cm (incluso) e 195 cm con un filtro combinato: `(altezze >= 185) & (altezze < 195)`.

**Esempio di esecuzione**

```
Prime 5 altezze: [173.  159.6 177.5 179.4 150.5]
Media: 169.9 cm, dev. std: 9.6 cm
Minimo: 144.3, massimo: 199.1
Dev. std degli z: 1.00
Entro 1 dev. std: 69.0% (teorica 68.3%)
Oltre 2 dev. std: 5.2% (teorica 4.6%)
Tra 185 e 195 cm: 27
```

**Provate anche**

- rieseguite il programma: i numeri sono gli stessi. Con seed 1 → `Prime 5 altezze: [173.5 178.2 173.3 157.  179.1]`, `Entro 1 dev. std: 70.0%`
- 500 → 100 000 altezze → `Entro 1 dev. std: 68.4%`, `Oltre 2 dev. std: 4.6%`: con più dati le quote si avvicinano a quelle teoriche
- togliete le parentesi nel filtro combinato → `TypeError`: `&` viene calcolato prima di `>=` e `<`

---

## Esercizio 4 — Rispondere a caso (`test_crocette.py`)

**Consegna**

1. Un test ha 10 domande con 4 risposte possibili, una sola giusta, e si supera con almeno 6 risposte giuste. Simulate 100 000 studenti che rispondono a caso, con `rng = np.random.default_rng(2027)`.
2. `rng.integers(0, 4, size=(N, 10))` è una matrice con una riga per studente e una colonna per domanda. La risposta giusta è sempre la 0: `np.sum(risposte == 0, axis=1)` conta le risposte giuste di ogni studente.
3. Stampate le giuste dei primi 5 studenti, la media (teorica 10 · 0.25 = 2.5), la quota di studenti senza risposte giuste e la quota di chi supera il test.
4. Stimate di nuovo la quota con `rng.binomial(n=10, p=0.25, size=N)` e calcolate la probabilità esatta con `math.comb`: la somma di C(10, k) · 0.25^k · 0.75^(10 − k) per k da 6 a 10.
5. Con una penalità di 1/3 di punto per ogni risposta sbagliata il punteggio è `giuste - (10 - giuste) / 3`. Stampate il punteggio medio e la quota di punteggi negativi.

**Esempio di esecuzione**

```
Giuste dei primi 5 studenti: [3 3 2 2 3]
Media di risposte giuste: 2.50 (teorica 2.50)
Nessuna risposta giusta: 5.6%
Test superato (simulato): 1.97%
Test superato (binomiale): 1.95%
Test superato (esatta): 1.97%
Punteggio medio con penalità: 0.00
Punteggio negativo: 52.5%
```

**Provate anche**

- soglia 5 → simulato `7.78%`, binomiale `7.79%`, esatta `7.81%`
- 100 000 → 1000 studenti → simulato `1.80%`, binomiale `2.50%`: con pochi studenti le stime si allontanano dal valore esatto

---

## Esercizio 5 — Il libretto in un DataFrame (`libretto.py`)

**Consegna**

1. Create un DataFrame da un dizionario di liste con gli esami di una studentessa (tabella): colonne `esame`, `anno`, `crediti`, `voto`. Stampatelo con la sua forma.
2. Aggiungete la colonna calcolata `pesato`, voto per crediti.
3. Stampate i crediti totali, la media aritmetica e la media ponderata (somma di `pesato` diviso crediti totali) con due decimali, e la base di laurea: media ponderata / 30 · 110.
4. Selezionate gli esami con voto almeno 26, ordinateli con `sort_values("voto", ascending=False)` e stampate solo le colonne `esame` e `voto`.
5. Contate gli esami da 9 crediti del primo anno con un filtro combinato con `&`.

| esame | anno | crediti | voto |
|---|---|---|---|
| Analisi I | 1 | 9 | 24 |
| Statistica I | 1 | 9 | 28 |
| Informatica | 1 | 6 | 30 |
| Economia | 1 | 9 | 22 |
| Probabilità | 2 | 9 | 26 |
| Demografia | 2 | 6 | 27 |

**Esempio di esecuzione**

```
          esame  anno  crediti  voto
0     Analisi I     1        9    24
1  Statistica I     1        9    28
2   Informatica     1        6    30
3      Economia     1        9    22
4   Probabilità     2        9    26
5    Demografia     2        6    27
Righe e colonne: (6, 4)
Crediti: 48
Media aritmetica: 26.17, ponderata: 25.88
Base di laurea: 94.9
          esame  voto
2   Informatica    30
1  Statistica I    28
5    Demografia    27
4   Probabilità    26
Esami da 9 crediti del primo anno: 3
```

**Provate anche**

- aggiungete `Algebra`, anno 2, 6 crediti, voto 30 → `Crediti: 54`, `ponderata: 26.33`, `Base di laurea: 96.6`
- nel dizionario scrivete `"voti"` al posto di `"voto"` → `KeyError: 'voto'` alla prima riga che usa la colonna

---

## Esercizio 6 — Esplorare un CSV (`esami_csv.py`)

**Consegna**

1. Il file `esami.csv` contiene 10 esami di studenti di Scienze Statistiche. Leggetelo con `pd.read_csv("esami.csv", sep=";")`.
2. Esplorate i dati: stampate le prime 3 righe (`head(3)`), la forma, i nomi delle colonne (`columns.tolist()`), le statistiche del voto con `describe().round(1)` e il numero di esami per corso con `value_counts()`.
3. Contate i promossi (voto almeno 18) e stampate le matricole di Statistica del secondo anno, con un filtro combinato e `.tolist()`.
4. Stampate il voto medio per corso con `groupby("corso")["voto"].mean().round(1)`.

**File `esami.csv`** (createlo nella cartella del programma)

```
matricola;corso;anno;voto
2101234;Statistica;1;28
2101567;Analisi;1;17
2102001;Informatica;1;30
2102345;Statistica;1;24
2102890;Analisi;1;21
2103112;Statistica;2;19
2103456;Informatica;2;27
2103789;Analisi;2;15
2104012;Statistica;2;26
2104333;Informatica;1;23
```

**Esempio di esecuzione**

```
   matricola        corso  anno  voto
0    2101234   Statistica     1    28
1    2101567      Analisi     1    17
2    2102001  Informatica     1    30
Righe e colonne: (10, 4)
Colonne: ['matricola', 'corso', 'anno', 'voto']
count    10.0
mean     23.0
std       4.9
min      15.0
25%      19.5
50%      23.5
75%      26.8
max      30.0
Name: voto, dtype: float64
corso
Statistica     4
Analisi        3
Informatica    3
Name: count, dtype: int64
Promossi: 8 su 10
Statistica, secondo anno: [2103112, 2104012]
corso
Analisi        17.7
Informatica    26.7
Statistica     24.2
Name: voto, dtype: float64
```

**Provate anche**

- aggiungete la riga `2104555;Analisi;2;29` → `Righe e colonne: (11, 4)`, `Promossi: 9 su 11`, Analisi `20.5`
- togliete `sep=";"` → c'è una sola colonna, `matricola;corso;anno;voto`, e poi `KeyError: 'voto'`
- aggiungete `esami.info()`: per ogni colonna mostra tipo e valori non nulli; `corso` è di tipo testo (`object`, o `str` con Pandas 3)

---

## Esercizio 7 — Pulire un questionario (`pulizia_questionario.py`)

**Consegna**

1. Il file `questionario.csv` contiene le ore di studio settimanali e il voto di alcuni studenti. C'è una riga ripetuta e mancano alcuni valori, scritti in tre modi: campo vuoto, `NA` e `?`.
2. Leggetelo con `na_values=["", "NA", "?"]` e stampate le righe lette e i valori mancanti per colonna (`isna().sum()`).
3. Contate e togliete le righe duplicate (`duplicated().sum()`, `drop_duplicates()`), poi togliete le righe senza voto con `dropna(subset=["voto"])`.
4. Sostituite le ore mancanti con la media delle ore arrotondata a un decimale (`fillna({"ore_studio": ...})`) e convertite il voto in intero con `astype(int)`.
5. Stampate le righe rimaste, i mancanti rimasti (`isna().sum().sum()`), voto e ore medi con due decimali e le medie per corso di ore e voto con `groupby` e `round(1)`.

**File `questionario.csv`** (createlo nella cartella del programma)

```
matricola;corso;ore_studio;voto
2101234;Statistica;12;28
2101567;Analisi;;24
2102001;Statistica;8;NA
2102345;Informatica;15;30
2102890;Analisi;6;18
2102345;Informatica;15;30
2103112;Statistica;?;22
2103456;Informatica;10;
2103789;Analisi;9;21
2104012;Statistica;14;27
2104333;Informatica;11;26
```

**Esempio di esecuzione**

```
Righe lette: 11
Valori mancanti per colonna:
matricola     0
corso         0
ore_studio    2
voto          2
dtype: int64
Righe duplicate tolte: 1
Righe senza voto tolte: 2
Ore mancanti sostituite con la media: 11.2
Righe pulite: 8, mancanti: 0
Voto medio: 24.50
Ore medie: 11.18
             ore_studio  voto
corso                        
Analisi             8.7  21.0
Informatica        13.0  28.0
Statistica         12.4  25.7
```

**Provate anche**

- togliete `na_values` → `?` resta come testo, la colonna `ore_studio` diventa di testo e `mean()` dà `TypeError`
- togliete `drop_duplicates()` → `Righe pulite: 9`, `Voto medio: 25.11`: la riga ripetuta pesa due volte
- al posto di `fillna` scrivete `q = q.dropna()` → `Righe pulite: 6`, `Voto medio: 25.00`

---

## Esercizio 8 — Gli esami del primo anno (`esami_primo_anno.py`)

**Consegna**

1. Generate 150 esami con `rng = np.random.default_rng(2026)`: prima i voti con `np.round(rng.normal(23, 5, size=150))`, poi il corso con `rng.choice(CORSI, size=150)`, dove `CORSI` contiene Analisi, Statistica e Informatica. Cambiando l'ordine cambiano i numeri.
2. Mettete tutto nel DataFrame `esami`: i voti oltre 30 diventano 30 con `np.minimum(voti, 30)`, poi `astype(int)`. Stampate il numero di esami e di 30.
3. Aggiungete la colonna `promosso` (voto almeno 18) e stampate la quota di promossi per corso con `groupby("corso")["promosso"].mean()`: la media di booleani è una quota. Scorrete il risultato con `.items()`.
4. Create la tabella `corsi` con i crediti: Analisi 9, Statistica 9, Informatica 6, Economia 9. Con una catena di metodi unite le tabelle (`merge(corsi, on="corso", how="left")`), tenete i promossi (`query("promosso")`) e stampate i crediti acquisiti in totale.
5. Con un'altra catena calcolate per corso numero, media, minimo e massimo dei voti dei promossi (`agg(["count", "mean", "min", "max"])`, poi `round(1)`) e stampate la tabella.

**Esempio di esecuzione**

```
Esami: 150, voti 30: 21
Analisi: promossi 87.3%
Informatica: promossi 88.4%
Statistica: promossi 86.5%
Crediti acquisiti: 1065
             count  mean  min  max
corso                             
Analisi         48  24.2   18   30
Informatica     38  24.4   18   30
Statistica      45  24.2   18   30
```

**Provate anche**

- `how="inner"` → stesso risultato: tutti i corsi degli esami sono in `corsi`. Economia non compare perché non ha esami
- seed 1 → `voti 30: 6`, `Crediti acquisiti: 1029`
- `query("voto >= 27")` → `Crediti acquisiti: 330` e tutti i minimi a 27

---

## Challenge a scelta

Scegliete un tema. Le cinque challenge hanno la stessa difficoltà e usano gli stessi strumenti: cambiano la storia e i dati. Ogni tema continua nei laboratori successivi.

| Tema | Challenge | File |
|---|---|---|
| Mercati e finanza | Il portafoglio simulato | `ch_mercati.py` |
| Sport | La gara simulata | `ch_sport.py` |
| Imprese e marketing | Un mese di vendite | `ch_negozio.py` |
| Salute e scienza | Lo studio simulato | `ch_salute.py` |
| Caso e probabilità | Dadi e porte | `ch_probabilita.py` |

**Tutte le challenge chiedono:**

- Generate i dati del tema con `rng = np.random.default_rng(seed)`, con il seed indicato e le estrazioni nell'ordine della consegna, così l'output coincide con l'esempio.
- Almeno un calcolo vettorizzato su un array o una matrice, senza cicli `for`.
- Almeno un filtro booleano: `array[condizione]` oppure `np.sum(condizione)`.
- Una simulazione Monte Carlo di 10 000 ripetizioni, anche questa senza cicli, che stima una probabilità.
- Un DataFrame Pandas costruito da un dizionario o da un array, con una colonna calcolata.
- Una statistica per gruppo con `groupby`.
- Type hints sulle variabili principali; niente `pivot_table` e niente grafici.

---

### Challenge · Mercati e finanza — Il portafoglio simulato (`ch_mercati.py`)

**Consegna**

1. Lo studente investitore ha diviso 10 000 EUR tra ENRG, BANK e TECH con i pesi della tabella. Simulate 20 giorni di rendimenti con `rng = np.random.default_rng(7)` e `rng.normal(MEDIE, VOL, size=(20, 3))`: una riga per giorno, una colonna per titolo. Gli array `MEDIE` e `VOL` valgono colonna per colonna (broadcasting).
2. Stampate la volatilità di ogni titolo, cioè la deviazione standard campionaria per colonna (`axis=0`), in percentuale con due decimali.
3. Il rendimento giornaliero del portafoglio è `np.sum(rend * PESI, axis=1)` e il valore finale è 10 000 · `np.prod(1 + port)`. Stampate il valore finale, i giorni in perdita (filtro) e il peggior giorno.
4. Monte Carlo: simulate 10 000 mesi di 20 giorni di TECH (`size=(10_000, 20)`), sommate i rendimenti di ogni mese e stimate la probabilità che TECH perda più del 5%.
5. Mettete i rendimenti in un DataFrame con `pd.DataFrame(rend, columns=TITOLI)`, aggiungete le colonne `settimana` (`np.arange(20) // 5 + 1`) e `portafoglio`, e stampate il rendimento medio del portafoglio per settimana con `groupby`.

| Titolo | Rendimento medio giornaliero | Volatilità giornaliera | Peso |
|---|---|---|---|
| ENRG | 0.10% | 1.2% | 30% |
| BANK | 0.05% | 0.9% | 50% |
| TECH | 0.20% | 2.5% | 20% |

**Esempio di esecuzione**

```
Volatilità ENRG: 0.88%
Volatilità BANK: 0.86%
Volatilità TECH: 2.21%
Valore finale di 10000 EUR: 9682.07 EUR
Giorni in perdita: 11 su 20
Peggior giorno: -2.09%
P(TECH perde più del 5% in un mese): 21.1%
Settimana 1: rendimento medio -0.08%
Settimana 2: rendimento medio -0.85%
Settimana 3: rendimento medio -0.12%
Settimana 4: rendimento medio 0.41%
```

**Provate anche**

- tutto su TECH (`PESI = [0.0, 0.0, 1.0]`) → `Valore finale di 10000 EUR: 8892.68 EUR`, `Peggior giorno: -6.09%`
- mesi di 60 giorni nella simulazione → `18.6%`: su un periodo più lungo pesa di più il rendimento medio positivo
- seed 8 → `Volatilità TECH: 2.65%`, `Valore finale di 10000 EUR: 9897.43 EUR`

---

### Challenge · Sport — La gara simulata (`ch_sport.py`)

**Consegna**

1. Simulate i tempi sul giro di una gara di 15 giri per Ferri, Lanza, Moro e Neri con `rng = np.random.default_rng(15)` e `rng.normal(BASE, 0.6, size=(15, 4))`: una riga per giro, una colonna per pilota. `BASE` contiene il passo di ogni pilota (tabella).
2. Al giro 8 tutti fanno il pit stop: aggiungete 20 secondi alla riga `tempi[7]`. Contate i giri anomali (oltre 100 s) e, per ogni pilota, i giri sotto i 92 s con `np.sum(tempi < 92, axis=0)`.
3. Monte Carlo: simulate 10 000 gare di 15 giri per Ferri (passo 92.0 s) e poi per Moro (92.2 s), sempre con deviazione standard 0.6, sommate i tempi di ogni gara e stimate la probabilità che Moro arrivi davanti a Ferri.
4. Create un DataFrame con pilota, scuderia, tempo totale e giro migliore (`np.min(tempi, axis=0)`), aggiungete la colonna `distacco` dal più veloce e stampatelo ordinato per tempo totale, con `round(1)`.
5. Stampate il tempo totale medio di ogni scuderia con `groupby`.

| Pilota | Scuderia | Passo (s) |
|---|---|---|
| Ferri | Scuderia Rossa | 92.0 |
| Lanza | Scuderia Rossa | 92.4 |
| Moro | Scuderia Blu | 92.2 |
| Neri | Scuderia Blu | 92.6 |

**Esempio di esecuzione**

```
Giri anomali (oltre 100 s): 4
Ferri, giri sotto i 92 s: 7
Lanza, giri sotto i 92 s: 5
Moro, giri sotto i 92 s: 1
Neri, giri sotto i 92 s: 1
P(Moro batte Ferri): 18.5%
  pilota        scuderia  totale  migliore  distacco
0  Ferri  Scuderia Rossa  1399.1      91.0       0.0
1  Lanza  Scuderia Rossa  1405.4      91.4       6.3
2   Moro    Scuderia Blu  1405.6      91.3       6.5
3   Neri    Scuderia Blu  1409.2      91.8      10.1
scuderia
Scuderia Blu      1407.4
Scuderia Rossa    1402.3
Name: totale, dtype: float64
```

**Provate anche**

- safety car al giro 4 (`tempi[3]` più 15 s) → `Giri anomali (oltre 100 s): 8` e tutti i totali crescono di 15 s
- Moro con passo 92.6 nella simulazione → `P(Moro batte Ferri): 0.2%`
- deviazione standard 0.3 sui giri della gara → Moro passa davanti a Lanza con distacco `4.8`

---

### Challenge · Imprese e marketing — Un mese di vendite (`ch_negozio.py`)

**Consegna**

1. Simulate i pezzi venduti in 30 giorni per i 5 prodotti del negozio con `rng = np.random.default_rng(30)` e `rng.integers(0, 6, size=(30, 5))`: una riga per giorno, una colonna per prodotto, nell'ordine della tabella.
2. L'incasso di ogni giorno è `np.sum(pezzi * PREZZI, axis=1)`. Stampate il fatturato del mese, l'incasso medio giornaliero e i giorni sopra 300 EUR.
3. Monte Carlo per il test A/B: ogni versione della pagina ha 1000 visitatori; la A converte con probabilità 4%, la B con 5%. Simulate 10 000 volte gli acquisti con `rng.binomial`, prima per A e poi per B, e stimate la probabilità che B venda più di A.
4. Create un DataFrame dei prodotti con categoria, pezzi venduti (`np.sum(pezzi, axis=0)`), prezzo e costo. Aggiungete la colonna `margine`, pezzi per (prezzo − costo), e stampate prodotto, pezzi e margine con `round(2)`.
5. Stampate il margine totale per categoria con `groupby`.

| Prodotto | Categoria | Prezzo (EUR) | Costo (EUR) |
|---|---|---|---|
| zaino | scuola | 39.90 | 22.00 |
| borraccia | casa | 14.50 | 6.00 |
| quaderno | scuola | 3.20 | 1.10 |
| cuffie | tech | 59.00 | 38.00 |
| lampada | casa | 24.90 | 13.50 |

**Esempio di esecuzione**

```
Fatturato del mese: 9588.20 EUR
Incasso medio giornaliero: 319.61 EUR
Giorni sopra 300 EUR: 18 su 30
P(la pagina B vende più della A): 84.7%
    prodotto  pezzi  margine
0      zaino     71   1270.9
1  borraccia     73    620.5
2   quaderno     74    155.4
3     cuffie     63   1323.0
4    lampada     70    798.0
categoria
casa      1418.5
scuola    1426.3
tech      1323.0
Name: margine, dtype: float64
```

**Provate anche**

- 5000 visitatori per versione → `99.2%`: con più visitatori il test distingue meglio le due pagine
- zaino a 35.90 EUR → `Fatturato del mese: 9304.20 EUR`, margine di `scuola` `1142.3`

---

### Challenge · Salute e scienza — Lo studio simulato (`ch_salute.py`)

**Consegna**

1. Simulate 20 pazienti, da `P01` a `P20` (`"P" + str(i).zfill(2)`): i primi 10 nel gruppo `trattamento`, gli altri nel `controllo`. Con `rng = np.random.default_rng(11)` estraete in quest'ordine l'età (`rng.integers(35, 71, size=20)`), la pressione sistolica prima (`np.round(rng.normal(150, 12, size=20))`) e il calo (`rng.normal(2 + 6 * (gruppo == "trattamento"), 5)`): in media 8 mmHg nel trattamento e 2 nel controllo.
2. Calcolate senza cicli la pressione dopo (`np.round(prima - calo)`) e la differenza prima − dopo. Un paziente è migliorato se la pressione scende di almeno 5 mmHg. Stampate il calo medio, i migliorati di ogni gruppo (filtro sul gruppo) e la quota complessiva di migliorati.
3. Monte Carlo: se l'integratore non avesse effetto, ogni paziente migliorerebbe con la stessa probabilità, pari alla quota complessiva. Simulate 10 000 gruppi di 10 pazienti con `rng.binomial` e stimate la probabilità di avere almeno tanti migliorati quanti nel gruppo trattamento.
4. Create un DataFrame con codice, età, gruppo, pressione prima e dopo, aggiungete la colonna `differenza` e stampate le prime 3 righe.
5. Stampate età media e differenza media per gruppo con `groupby` e `round(1)`.

**Esempio di esecuzione**

```
Calo medio: 4.6 mmHg
Migliorati trattamento: 8 su 10
Migliorati controllo: 2 su 10
Migliorati in tutto: 50%
P(almeno 8 su 10 senza effetto): 5.3%
  codice  eta       gruppo  prima   dopo  differenza
0    P01   39  trattamento  169.0  157.0        12.0
1    P02   39  trattamento  149.0  142.0         7.0
2    P03   63  trattamento  158.0  154.0         4.0
              eta  differenza
gruppo                       
controllo    55.9         0.6
trattamento  49.3         8.6
```

**Provate anche**

- soglia di 10 mmHg → `Migliorati trattamento: 5 su 10`, `Migliorati controllo: 0 su 10`, `P(almeno 5 su 10 senza effetto): 7.5%`
- integratore senza effetto (`2 + 0 * (gruppo == "trattamento")`) → `Migliorati trattamento: 4 su 10`, `34.8%`

---

### Challenge · Caso e probabilità — Dadi e porte (`ch_probabilita.py`)

**Consegna**

1. Simulate 1000 lanci di due dadi con `rng = np.random.default_rng(6)`: prima `dado1`, poi `dado2`, ciascuno con `rng.integers(1, 7, size=1000)`. Calcolate la somma senza cicli.
2. Stampate la somma media e la frequenza della somma 7, delle somme almeno 10 (con un filtro) e dei doppi, accanto alle probabilità esatte 6/36, 6/36 e 1/6.
3. Monte Carlo per Monty Hall: in 10 000 partite estraete la porta dell'auto e la prima scelta del giocatore, ciascuna con `rng.integers(0, 3, size=10_000)`. Chi resta vince quando le due porte coincidono, chi cambia vince negli altri casi: stimate le due probabilità.
4. Mettete i lanci in un DataFrame con le colonne `dado1` e `dado2` e aggiungete la colonna `somma`.
5. Stampate la somma media per ogni valore del primo dado con `groupby`, accanto al valore teorico (faccia + 3.5).

**Esempio di esecuzione**

```
Somma media: 7.05 (teorica 7.00)
Somma 7: 15.1% (esatta 16.7%)
Somma almeno 10: 188 lanci (18.8%, esatta 16.7%)
Doppi: 16.8% (esatta 16.7%)
Monty Hall, vince chi resta: 33.8%
Monty Hall, vince chi cambia: 66.2%
Primo dado 1: somma media 4.30 (teorica 4.50)
Primo dado 2: somma media 5.70 (teorica 5.50)
Primo dado 3: somma media 6.26 (teorica 6.50)
Primo dado 4: somma media 7.60 (teorica 7.50)
Primo dado 5: somma media 8.54 (teorica 8.50)
Primo dado 6: somma media 9.60 (teorica 9.50)
```

**Provate anche**

- 100 000 lanci → `Somma 7: 16.6%`, `Somma almeno 10: 16493 lanci (16.5%, esatta 16.7%)` e medie per gruppo vicine a quelle teoriche
- raggruppate per il secondo dado → stessi valori teorici, medie diverse (`Secondo dado 3: somma media 6.37`)

---

## Domande di verifica

1. In `voti_numpy.py`, cosa contiene `voti >= 18`? Perché `voti[voti >= 18]` non ha bisogno di un ciclo?
2. In `ore_studio.py`, che differenza c'è tra `axis=0` e `axis=1`? Quale serve per la media di ogni corso?
3. Perché `np.mean(np.abs(z) > 2)` è una quota? Cosa diventano `True` e `False` nel calcolo?
4. A cosa serve il seed in `np.random.default_rng(42)`? Perché conviene fissarlo quando si consegna un'analisi?
5. In `test_crocette.py`, perché il punteggio medio con la penalità di 1/3 è circa 0?
6. In `pulizia_questionario.py`, quando conviene togliere le righe con valori mancanti e quando sostituirli con la media?
7. Che differenza c'è tra `how="left"` e `how="inner"` in `merge`? Quando danno lo stesso risultato?
