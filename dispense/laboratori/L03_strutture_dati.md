# Laboratorio 3 — Strutture dati

**Prerequisiti:** lezioni T11 (Liste e tuple), T12 (Dizionari e set) e T13 (Funzioni).

Oggi ci sono solo esercizi, in ordine di difficoltà, su liste, tuple, dizionari e set. Per ogni esercizio create un file `.py` con il nome indicato e scrivete il programma da soli. Le funzioni servono solo negli ultimi esercizi.

Ogni esercizio ha la consegna, un esempio di esecuzione e alcuni casi da provare: il programma è corretto quando dà gli stessi risultati. Alla fine c'è una challenge a scelta tra 5 temi. Le soluzioni le vediamo all'inizio della lezione T14.

| # | File | Esercizio |
|---|---|---|
| 1 | `voti_appello.py` | L'appello di Statistica |
| 2 | `coda_mensa.py` | La coda in mensa |
| 3 | `sondaggio.py` | Come arrivate in aula |
| 4 | `tre_corsi.py` | Chi segue cosa |
| 5 | `libretto.py` | Il libretto |
| 6 | `sessione.py` | La sessione invernale |
| 7 | `contingenza.py` | Scuola di provenienza ed esito |
| 8 | `descrittive.py` | Ore di studio |
| Challenge | a scelta | Mercati e finanza · Sport · Imprese e marketing · Salute e scienza · Caso e probabilità |

---

## Promemoria

Gli strumenti che servono oggi. Da oggi si possono usare `sum()`, `min()`, `max()` e `sorted()`; l'unico import ammesso è `from collections import Counter, defaultdict`.

```python
from collections import Counter, defaultdict

voti: list[int] = [int(v) for v in "28 18 30".split()]
print(sum(voti), min(voti), sorted(voti))   # 76 18 [18, 28, 30]
voti.append(24)            # in fondo; voti.pop(0) toglie il primo
cfu: dict[str, int] = {"Analisi": 9, "Informatica": 6}
for esame, n in cfu.items():    # coppie (chiave, valore)
    print(esame, n)             # Analisi 9, poi Informatica 6
print(cfu.get("Inglese", 0))    # 0: la chiave non c'è
a: set[str] = {"Anna", "Bruno"}
b: set[str] = {"Bruno", "Carla"}
print(sorted(a | b), a & b, a - b)  # ['Anna', ...] {'Bruno'} {'Anna'}
print(Counter("abbccc").most_common(1))     # [('c', 3)]
gruppi: defaultdict[str, list[int]] = defaultdict(list)
gruppi["Analisi"].append(27)    # la lista vuota si crea da sola
```

---

## Esercizio 1 — L'appello di Statistica (`voti_appello.py`)

**Consegna**

1. Chiedete i voti dell'appello su una riga, separati da spazi, e trasformateli in una lista di interi con `split()` e una list comprehension.
2. Stampate la lista ordinata (`sorted()`), il numero di presenti, la media con un decimale, il voto minimo e il massimo.
3. Con una seconda comprehension tenete i voti da 18 in su: stampate quanti sono, la loro percentuale con un decimale e la loro media.
4. Se nessuno è promosso, la media dei promossi non va stampata.

**Esempio di esecuzione**

```
Voti separati da spazi: 24 18 30 15 27 22 30 12 26 19
Voti ordinati: [12, 15, 18, 19, 22, 24, 26, 27, 30, 30]
Presenti: 10
Media: 22.3
Minimo: 12  Massimo: 30
Promossi: 8 (80.0%)
Media dei promossi: 24.5
```

**Provate anche**

- `30 30 30` → `Promossi: 3 (100.0%)`
- `12 15` → `Promossi: 0 (0.0%)` e nessuna media dei promossi
- `18` → un voto solo: media, minimo e massimo valgono 18

---

## Esercizio 2 — La coda in mensa (`coda_mensa.py`)

**Consegna**

1. Partite da `coda: list[str] = ["Anna", "Bruno", "Carla"]` e dagli eventi `["arriva Davide", "servito", "arriva Elena", "esce Bruno", "davanti Franco Elena", "servito", "esce Zeno"]`.
2. Dividete ogni evento con `split()`. `arriva X` mette X in fondo (`append`); `servito` toglie il primo (`pop(0)`) e lo aggiunge alla lista `serviti`; `esce X` toglie X (`remove`); `davanti X Y` mette X subito prima di Y (`insert` e `index`).
3. Se la persona non è in coda o il comando non esiste, stampate `Evento non valido: ...`; se arriva `servito` con la coda vuota, stampate `Nessuno da servire`.
4. Dopo ogni evento stampate l'evento e la coda; alla fine stampate i serviti e quante persone restano in coda.

**Esempio di esecuzione**

```
arriva Davide -> ['Anna', 'Bruno', 'Carla', 'Davide']
servito -> ['Bruno', 'Carla', 'Davide']
arriva Elena -> ['Bruno', 'Carla', 'Davide', 'Elena']
esce Bruno -> ['Carla', 'Davide', 'Elena']
davanti Franco Elena -> ['Carla', 'Davide', 'Franco', 'Elena']
servito -> ['Davide', 'Franco', 'Elena']
Evento non valido: esce Zeno
esce Zeno -> ['Davide', 'Franco', 'Elena']
Serviti: ['Anna', 'Carla']
Ancora in coda: 3
```

**Provate anche**

- aggiungete quattro `servito` in fondo agli eventi → l'ultimo stampa `Nessuno da servire`, serviti in 5
- `davanti Gino Zeno` al posto di `davanti Franco Elena` → evento non valido, alla fine `Ancora in coda: 2`

---

## Esercizio 3 — Come arrivate in aula (`sondaggio.py`)

**Consegna**

1. Alle matricole è stato chiesto con quale mezzo arrivano in università. Chiedete le risposte su una riga, separate da virgole.
2. Pulite ogni risposta con `strip()` e `lower()`, così `Bus` e ` bus` diventano uguali, e scartate le risposte vuote.
3. Contate le risposte con un `Counter`. Stampate il numero di risposte e di mezzi diversi, poi ogni mezzo dal più frequente (`most_common()`) con il conteggio e la percentuale con un decimale.
4. Stampate infine il mezzo più usato, cioè la moda.

**Esempio di esecuzione**

```
Risposte separate da virgole: bici, Bus, piedi, bici, treno, BICI, bus, piedi, bici, monopattino, bus, treno
Risposte: 12, mezzi diversi: 5
bici: 4 (33.3%)
bus: 3 (25.0%)
piedi: 2 (16.7%)
treno: 2 (16.7%)
monopattino: 1 (8.3%)
Mezzo più usato: bici
```

**Provate anche**

- `auto` → `auto: 1 (100.0%)`
- `bus,,Bus , treno` → 3 risposte, `bus: 2 (66.7%)`

---

## Esercizio 4 — Chi segue cosa (`tre_corsi.py`)

**Consegna**

1. Scrivete i set `statistica`, `analisi` e `informatica` con gli studenti che frequentano i tre corsi (tabella).
2. Con `|`, `&` e `-` calcolate: quanti studenti diversi ci sono, chi segue tutti e tre i corsi, chi segue solo Statistica, chi segue Statistica e Analisi ma non Informatica.
3. Per trovare chi segue un corso soltanto, unite i tre set in una lista (`list(statistica) + list(analisi) + ...`) e contate i nomi con un `Counter`.
4. Stampate i nomi con `sorted()`, così l'ordine è sempre lo stesso.

| Corso | Studenti |
|---|---|
| Statistica | Anna, Bruno, Chiara, Davide, Elisa, Fabio, Giulia |
| Analisi | Anna, Chiara, Davide, Hana, Ivan, Giulia |
| Informatica | Bruno, Chiara, Giulia, Ivan, Luca |

**Esempio di esecuzione**

```
Studenti diversi: 10
Tutti e tre i corsi: ['Chiara', 'Giulia']
Solo Statistica: ['Elisa', 'Fabio']
Statistica e Analisi, non Informatica: ['Anna', 'Davide']
Un corso soltanto: ['Elisa', 'Fabio', 'Hana', 'Luca']
```

**Provate anche**

- aggiungete Luca a Statistica → Luca non segue più un corso soltanto
- aggiungete Marta a Informatica → `Studenti diversi: 11`

---

## Esercizio 5 — Il libretto (`libretto.py`)

**Consegna**

1. Scrivete il libretto come dizionario esame → tupla (voto, CFU), `libretto: dict[str, tuple[int, int]]`, con i dati della tabella.
2. Scorrete `libretto.items()` con `for esame, (voto, cfu) in ...`: stampate ogni esame e accumulate la somma dei voti, la somma di voto × CFU e i CFU totali.
3. Stampate i CFU totali, la media aritmetica e la media ponderata sui CFU, con due decimali.
4. La base di laurea è la media ponderata × 110 / 30: stampatela con un decimale.

| Esame | Voto e CFU |
|---|---|
| Analisi 1 | 24, 9 CFU |
| Statistica 1 | 28, 9 CFU |
| Informatica | 30, 6 CFU |
| Economia politica | 22, 9 CFU |
| Algebra lineare | 27, 6 CFU |

**Esempio di esecuzione**

```
Analisi 1: 24 (9 CFU)
Statistica 1: 28 (9 CFU)
Informatica: 30 (6 CFU)
Economia politica: 22 (9 CFU)
Algebra lineare: 27 (6 CFU)
CFU totali: 39
Media aritmetica: 26.20
Media ponderata: 25.85
Base di laurea: 94.8
```

**Provate anche**

- aggiungete `"Probabilità": (30, 9)` → 48 CFU, media ponderata `26.62`, base `97.6`
- date 6 CFU a tutti gli esami → le due medie valgono entrambe `26.20`

---

## Esercizio 6 — La sessione invernale (`sessione.py`)

**Consegna**

1. Scrivete gli esiti come lista di tuple (studente, esame, voto), nell'ordine della tabella: `esiti: list[tuple[str, str, int]]`.
2. In un solo ciclo riempite due `defaultdict(list)`: esame → voti, studente → esami superati (voto da 18 in su). Raccogliete anche tutti i nomi in un set.
3. Per ogni esame stampate il numero di prove, la media con un decimale e i promossi.
4. Per ogni studente, in ordine alfabetico, stampate gli esami superati; poi stampate chi non ne ha superato nessuno (differenza tra set).

| Studente | Esame e voto |
|---|---|
| Anna | Statistica 28, Analisi 30 |
| Bruno | Statistica 16, Analisi 17, Informatica 23 |
| Chiara | Analisi 25, Statistica 30 |
| Davide | Statistica 21, Informatica 26 |
| Elisa | Analisi 12 |

**Esempio di esecuzione**

```
Statistica: 4 prove, media 23.8, promossi 3
Analisi: 4 prove, media 21.0, promossi 2
Informatica: 2 prove, media 24.5, promossi 2
Anna ha superato ['Statistica', 'Analisi']
Bruno ha superato ['Informatica']
Chiara ha superato ['Analisi', 'Statistica']
Davide ha superato ['Statistica', 'Informatica']
Nessun esame superato: ['Elisa']
```

**Provate anche**

- aggiungete `("Elisa", "Statistica", 18)` → `Statistica: 5 prove, media 22.6, promossi 4` e `Nessun esame superato: []`

---

## Esercizio 7 — Scuola di provenienza ed esito (`contingenza.py`)

**Consegna**

1. Per 12 matricole conoscete la scuola di provenienza e se hanno superato Statistica al primo appello: `scuola = ["liceo", "tecnico", "liceo", "altro", "liceo", "tecnico", "tecnico", "liceo", "altro", "tecnico", "liceo", "tecnico"]` e `superato = [True, False, True, False, True, True, False, False, True, False, True, True]`.
2. Con `zip()` formate le coppie (scuola, esito) e contatele con un `Counter`: le chiavi sono tuple, per esempio `("liceo", True)`.
3. Con un secondo `Counter` contate le matricole per scuola.
4. Per ogni scuola, in ordine alfabetico, stampate superati, non superati e percentuale di superati con un decimale; alla fine stampate il totale.

**Esempio di esecuzione**

```
altro: superato 1, non superato 1, percentuale 50.0%
liceo: superato 4, non superato 1, percentuale 80.0%
tecnico: superato 2, non superato 3, percentuale 40.0%
Totale: 7 su 12 (58.3%)
```

**Provate anche**

- aggiungete una matricola del liceo che non ha superato l'esame → liceo `66.7%`, `Totale: 7 su 13 (53.8%)`
- una coppia che non compare non dà errore: `tabella[("professionale", True)]` vale `0`

---

## Esercizio 8 — Ore di studio (`descrittive.py`)

**Consegna**

1. Scrivete la funzione `descrittive(valori: list[float]) -> tuple[float, float, float]` che restituisce media, mediana e deviazione standard campionaria.
2. Mediana: ordinate i valori con `sorted()`; se sono in numero dispari è il valore centrale, se sono pari è la media dei due centrali.
3. Deviazione standard: somma dei quadrati degli scarti dalla media, divisa per n − 1, poi radice quadrata (`** 0.5`).
4. Partite da `ore_studio = {"Primo anno": [12, 15, 8, 20, 10, 14, 9], "Secondo anno": [18, 22, 15, 25, 30, 16], "Terzo anno": [20, 8, 35, 12, 28, 6, 14, 25]}` (ore di studio settimanali). Per ogni anno chiamate la funzione e stampate media e mediana con un decimale, deviazione standard con due.

**Esempio di esecuzione**

```
Primo anno: media 12.6, mediana 12.0, dev. std 4.16
Secondo anno: media 21.0, mediana 20.0, dev. std 5.80
Terzo anno: media 18.5, mediana 17.0, dev. std 10.25
```

**Provate anche**

- `descrittive([1, 2, 3, 4])` → media `2.5`, mediana `2.5`, deviazione standard `1.29`
- aggiungete `"Fuori corso": [5, 5, 5]` → `dev. std 0.00`

---

## Challenge a scelta

Scegliete un tema. Le cinque challenge hanno la stessa difficoltà e usano gli stessi strumenti: cambiano la storia e i dati. Ogni tema continua nei laboratori successivi.

| Tema | Challenge | File |
|---|---|---|
| Mercati e finanza | Il portafoglio | `ch_mercati.py` |
| Sport | Il campionato | `ch_sport.py` |
| Imprese e marketing | Il negozio online | `ch_negozio.py` |
| Salute e scienza | Lo studio clinico | `ch_salute.py` |
| Caso e probabilità | Il tavolo da gioco | `ch_probabilita.py` |

**Tutte le challenge chiedono:**

- Ogni challenge usa: una lista di tuple con i dati, scritta nel codice copiando la tabella o la consegna.
- Un raggruppamento con `defaultdict(list)` e un `Counter`, letto con `most_common(1)`.
- Una list comprehension con filtro e una percentuale stampata con `.1%`.
- Un'operazione tra set (`-`, `&` o `|`), stampata con `sorted()` così l'ordine è sempre lo stesso.
- Una funzione `def` con type hints e docstring che restituisce una tupla di due valori, spacchettata da chi la chiama.
- L'unico import è `from collections import Counter, defaultdict`; niente `random`, `lambda`, `sorted` con `key` e `try`. L'output ha da 6 a 7 righe, come nell'esempio.

---

### Challenge · Mercati e finanza — Il portafoglio (`ch_mercati.py`)

**Consegna**

1. Uno studente investe su tre titoli fittizi: `ENRG` (energia), `BANK` (banca) e `TECH` (tecnologia). Scrivete i suoi ordini come lista di tuple (titolo, quantità, prezzo), `ordini: list[tuple[str, int, float]]`, con i dati della tabella. Una quantità negativa è una vendita.
2. Scrivete `escursione(prezzi: list[float]) -> tuple[float, float]`, che restituisce il prezzo minimo e il prezzo massimo.
3. In un solo ciclo raggruppate i prezzi per titolo in un `defaultdict(list)` e sommate le quantità in un `Counter` chiamato `portafoglio`. Per ogni titolo, in ordine alfabetico, stampate il numero di ordini, il prezzo minimo e massimo con due decimali e le azioni in portafoglio.
4. Stampate la posizione più grande con `most_common(1)`. Con una comprehension con filtro tenete le vendite e stampate quante sono e la loro percentuale sugli ordini.
5. Costruite il set dei titoli comprati e quello dei titoli venduti e, con una differenza, stampate i titoli mai venduti.

| Titolo | Ordini (quantità a prezzo) |
|---|---|
| ENRG | 30 a 12.40, 20 a 12.10, -10 a 13.05 |
| BANK | 20 a 8.15, -5 a 8.60, 10 a 8.30, -5 a 8.75 |
| TECH | 10 a 45.20, 5 a 47.80, 5 a 44.90 |

**Esempio di esecuzione**

```
BANK: 4 ordini, prezzo da 8.15 a 8.75, in portafoglio 20
ENRG: 3 ordini, prezzo da 12.10 a 13.05, in portafoglio 40
TECH: 3 ordini, prezzo da 44.90 a 47.80, in portafoglio 20
Posizione più grande: ENRG con 40 azioni
Vendite: 3 su 10 (30.0%)
Mai venduti: ['TECH']
```

**Provate anche**

- aggiungete `("TECH", -20, 50.10)` → `TECH: 4 ordini, prezzo da 44.90 a 50.10, in portafoglio 0`, `Vendite: 4 su 11 (36.4%)` e `Mai venduti: []`
- aggiungete `("BANK", 30, 8.40)` → `Posizione più grande: BANK con 50 azioni`

---

### Challenge · Sport — Il campionato (`ch_sport.py`)

**Consegna**

1. Il campionato ha quattro piloti: Ferri e Lanza corrono per la Scuderia Rossa, Moro e Neri per la Scuderia Blu. Scrivete l'ordine d'arrivo di ogni gara come tupla di quattro nomi, dal primo al quarto, e mettete le cinque tuple nella lista `gare` (tabella). Scrivete anche `rossa: set[str] = {"Ferri", "Lanza"}`.
2. Scrivete `bilancio(posizioni: list[int]) -> tuple[int, int]`: riceve i piazzamenti di un pilota (da 1 a 4) e restituisce i punti totali, con `PUNTI = [25, 18, 15, 12]`, e il miglior piazzamento.
3. In un ciclo raggruppate i piazzamenti per pilota in un `defaultdict(list)` e contate le vittorie con un `Counter`. Per ogni pilota, in ordine alfabetico, stampate punti e miglior piazzamento.
4. Stampate il pilota con più vittorie (`most_common(1)`). Con una comprehension con filtro tenete i vincitori della Scuderia Rossa e stampate quante gare ha vinto la scuderia e in che percentuale.
5. Con una differenza tra set (piloti e vincitori) stampate i piloti senza vittorie.

| Gara | Ordine d'arrivo |
|---|---|
| 1 | Ferri, Moro, Lanza, Neri |
| 2 | Moro, Ferri, Neri, Lanza |
| 3 | Ferri, Lanza, Moro, Neri |
| 4 | Moro, Lanza, Ferri, Neri |
| 5 | Moro, Neri, Ferri, Lanza |

**Esempio di esecuzione**

```
Ferri: 98 punti, miglior piazzamento 1
Lanza: 75 punti, miglior piazzamento 2
Moro: 108 punti, miglior piazzamento 1
Neri: 69 punti, miglior piazzamento 2
Più vittorie: Moro con 3
Gare vinte dalla Scuderia Rossa: 2 su 5 (40.0%)
Senza vittorie: ['Lanza', 'Neri']
```

**Provate anche**

- aggiungete la gara `("Neri", "Lanza", "Moro", "Ferri")` → `Neri: 94 punti, miglior piazzamento 1`, `Gare vinte dalla Scuderia Rossa: 2 su 6 (33.3%)` e `Senza vittorie: ['Lanza']`
- `PUNTI = [10, 6, 4, 3]` → `Ferri: 34 punti` e `Moro: 40 punti`; le altre righe non cambiano

---

### Challenge · Imprese e marketing — Il negozio online (`ch_negozio.py`)

**Consegna**

1. Un negozio online vende cinque prodotti per lo studio: scrivete i prezzi della tabella in `prezzi: dict[str, float]`. Gli ordini della settimana sono tuple (cliente, prodotto, quantità): `[("Irene", "zaino", 1), ("Tommaso", "quaderno", 5), ("Giada", "cuffie", 1), ("Pietro", "borraccia", 2), ("Irene", "quaderno", 3), ("Noemi", "zaino", 1), ("Tommaso", "borraccia", 1), ("Irene", "cuffie", 1), ("Giada", "quaderno", 4), ("Noemi", "borraccia", 2)]`.
2. Scrivete `vendite(quantita: list[int]) -> tuple[int, int]`, che restituisce il numero di ordini e il numero di pezzi.
3. In un ciclo raggruppate le quantità per prodotto in un `defaultdict(list)` e contate gli ordini di ogni cliente con un `Counter`. Per ogni prodotto venduto, in ordine alfabetico, stampate ordini, pezzi e incasso (pezzi × prezzo) con due decimali.
4. Stampate il cliente con più ordini (`most_common(1)`). Con una comprehension con filtro tenete gli ordini con più di un pezzo e stampate quanti sono e la loro percentuale.
5. Con una differenza tra set (i prodotti di `prezzi` e quelli venduti) stampate i prodotti mai venduti.

| Prodotto | Prezzo (euro) |
|---|---|
| zaino | 39.90 |
| borraccia | 12.50 |
| quaderno | 3.20 |
| cuffie | 24.90 |
| lampada | 18.00 |

**Esempio di esecuzione**

```
borraccia: 3 ordini, 5 pezzi, incasso 62.50 euro
cuffie: 2 ordini, 2 pezzi, incasso 49.80 euro
quaderno: 3 ordini, 12 pezzi, incasso 38.40 euro
zaino: 2 ordini, 2 pezzi, incasso 79.80 euro
Cliente più assiduo: Irene con 3 ordini
Ordini con più di un pezzo: 5 su 10 (50.0%)
Mai venduti: ['lampada']
```

**Provate anche**

- aggiungete `("Pietro", "lampada", 2)` → `Ordini con più di un pezzo: 6 su 11 (54.5%)` e `Mai venduti: []`
- aggiungete `("Pietro", "zaino", 2)` → `zaino: 3 ordini, 4 pezzi, incasso 159.60 euro`

---

### Challenge · Salute e scienza — Lo studio clinico (`ch_salute.py`)

**Consegna**

1. Uno studio prova un integratore per la pressione su 10 pazienti, metà nel gruppo `trattamento` e metà nel gruppo `controllo`. Scrivete i dati come lista di tuple (codice, gruppo, pressione sistolica prima, dopo), `pazienti: list[tuple[str, str, int, int]]` (tabella). P07 non è tornato alla seconda visita: la sua pressione dopo è registrata come 0.
2. Con una comprehension con filtro tenete i pazienti con la misura dopo maggiore di 0 e stampate quanti sono e la loro percentuale. Con una differenza tra set di codici stampate chi non ha la seconda misura.
3. Scrivete `variazione(differenze: list[int]) -> tuple[int, float]`, che restituisce il numero di pazienti e la variazione media (dopo − prima).
4. Sui pazienti validi raggruppate le variazioni per gruppo in un `defaultdict(list)` e contate per gruppo i migliorati, cioè chi è sceso di almeno 10 mmHg, con un `Counter`. Per ogni gruppo, in ordine alfabetico, stampate pazienti, variazione media con un decimale e migliorati.
5. Stampate il totale dei migliorati sui pazienti validi e il gruppo con più migliorati (`most_common(1)`).

| Paziente | Gruppo, pressione prima → dopo (mmHg) |
|---|---|
| P01 | trattamento, 152 → 138 |
| P02 | controllo, 148 → 145 |
| P03 | trattamento, 160 → 147 |
| P04 | controllo, 155 → 150 |
| P05 | trattamento, 145 → 140 |
| P06 | controllo, 150 → 152 |
| P07 | trattamento, 158 → 0 |
| P08 | controllo, 149 → 138 |
| P09 | trattamento, 162 → 148 |
| P10 | controllo, 157 → 155 |

**Esempio di esecuzione**

```
Misure valide: 9 su 10 (90.0%)
Senza seconda misura: ['P07']
controllo: 5 pazienti, variazione media -3.8 mmHg, migliorati 1
trattamento: 4 pazienti, variazione media -11.5 mmHg, migliorati 3
Migliorati: 4 su 9
Gruppo con più migliorati: trattamento (3)
```

**Provate anche**

- P07 con la misura dopo `145` → `Misure valide: 10 su 10 (100.0%)`, `Senza seconda misura: []` e `trattamento: 5 pazienti, variazione media -11.8 mmHg, migliorati 4`
- aggiungete `("P11", "controllo", 151, 0)` → `Misure valide: 9 su 11 (81.8%)` e `Senza seconda misura: ['P07', 'P11']`

---

### Challenge · Caso e probabilità — Il tavolo da gioco (`ch_probabilita.py`)

**Consegna**

1. Ada, Bea e Ciro giocano con due dadi e annotano ogni lancio come tupla (giocatore, primo dado, secondo dado). Scrivete la lista `lanci: list[tuple[str, int, int]]` con i 12 lanci della tabella.
2. Scrivete `riassunto(somme: list[int]) -> tuple[float, int]`, che restituisce la somma media e la somma più alta.
3. In un ciclo raggruppate le somme dei due dadi per giocatore in un `defaultdict(list)` e contate quante volte esce ogni somma con un `Counter`. Per ogni giocatore, in ordine alfabetico, stampate la somma media con due decimali e la somma più alta.
4. Stampate la somma uscita più spesso (`most_common(1)`). Con una comprehension con filtro tenete i doppi (due dadi uguali) e stampate quanti sono e la loro percentuale.
5. Con una set comprehension su due cicli costruite tutte le somme possibili con due dadi; con una differenza tra set stampate le somme mai uscite.

| Giocatore | Lanci (primo e secondo dado) |
|---|---|
| Ada | 3 e 4, 1 e 3, 6 e 5, 2 e 2 |
| Bea | 6 e 6, 5 e 2, 3 e 1, 4 e 3 |
| Ciro | 2 e 5, 4 e 4, 6 e 2, 5 e 3 |

**Esempio di esecuzione**

```
Ada: somma media 6.50, più alta 11
Bea: somma media 7.50, più alta 12
Ciro: somma media 7.75, più alta 8
Somma più uscita: 7 (4 volte)
Doppi: 3 su 12 (25.0%)
Somme mai uscite: [2, 3, 5, 6, 9, 10]
```

**Provate anche**

- aggiungete `("Ada", 5, 5)` → `Ada: somma media 7.20, più alta 11`, `Doppi: 4 su 13 (30.8%)` e `Somme mai uscite: [2, 3, 5, 6, 9]`
- aggiungete `("Bea", 1, 1)` → `Somme mai uscite: [3, 5, 6, 9, 10]`

---

## Domande di verifica

1. Che differenza c'è tra `sorted(voti)` e `voti.sort()`? Quale dei due modifica la lista?
2. In `coda_mensa.py`, cosa succede con `coda.remove("Zeno")` se prima non si controlla con `in`?
3. In `sondaggio.py`, perché le risposte vanno pulite prima di passarle a `Counter`?
4. Perché, per stampare un set, conviene usare `sorted()`?
5. In `libretto.py`, quando la media ponderata coincide con la media aritmetica?
6. In `contingenza.py` le chiavi del `Counter` sono tuple. Si potrebbero usare liste? Perché?
7. In `descrittive.py` la funzione restituisce tre valori: che tipo ha il risultato e come si separa in tre variabili?
