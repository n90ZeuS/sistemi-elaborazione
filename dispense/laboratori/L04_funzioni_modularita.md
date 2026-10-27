# Laboratorio 4 — Funzioni e modularità

**Prerequisiti:** lezioni T13 (Funzioni) e T14 (Funzioni avanzate e moduli).

Oggi ci sono solo esercizi, in ordine di difficoltà. Per ogni esercizio create un file `.py` con il nome indicato: dentro scrivete le funzioni richieste, con type hints e docstring, e poi chiamatele sui dati della consegna stampando i risultati. Non serve `input()`: i dati sono già scritti nella consegna. Tutto il codice di un esercizio sta in un solo file.

Ogni esercizio ha la consegna, un esempio di esecuzione e alcuni casi da provare: il programma è corretto quando dà gli stessi risultati. Alla fine c'è una challenge a scelta tra 5 temi. Le soluzioni le vediamo all'inizio della lezione T15.

| # | File | Esercizio |
|---|---|---|
| 1 | `esito.py` | Esito dell'esame |
| 2 | `media_ponderata.py` | Media ponderata |
| 3 | `descrittive.py` | Media e varianza a mano |
| 4 | `riassunto.py` | Tempi di viaggio |
| 5 | `esami_date.py` | Quanto manca all'esame |
| 6 | `classifica.py` | Classifica del corso |
| 7 | `questionario.py` | Come arrivate in università |
| 8 | `confronto_gruppi.py` | Frequentanti e non frequentanti |
| Challenge | a scelta | Mercati e finanza · Sport · Imprese e marketing · Salute e scienza · Caso e probabilità |

---

## Promemoria

Gli strumenti che servono oggi. Le funzioni restituiscono il risultato con `return`; a stamparlo ci pensa chi le chiama. Si possono usare `sum()`, `min()`, `max()`, `sorted()` e i moduli della libreria standard.

```python
import statistics

def intervallo(centro: float,
               errore: float = 1.0) -> tuple[float, float]:
    """Restituisce gli estremi centro - errore e centro + errore."""
    return centro - errore, centro + errore

basso, alto = intervallo(25.0)            # 24.0 26.0 (default)
basso, alto = intervallo(25.0, errore=2.5)  # 22.5 27.5

esami: list[tuple[str, int]] = [("Analisi", 24), ("Statistica", 30)]
print(sorted(esami, key=lambda e: -e[1]))  # prima Statistica
print(max(esami, key=lambda e: e[1])[0])   # Statistica
print(statistics.median([24, 30, 27]))     # 27
```

---

## Esercizio 1 — Esito dell'esame (`esito.py`)

**Consegna**

1. Scrivete `esito(voto: int, lode: bool = False) -> str`, che restituisce l'esito come stringa secondo la tabella. I casi si controllano nell'ordine della tabella.
2. La lode conta solo con 30: `esito(27, lode=True)` restituisce `promosso con 27`.
3. Stampate `esito(28)` e `esito(30, lode=True)`.
4. Scorrete la lista `appello: list[tuple[str, int, bool]] = [("Anna", 27, False), ("Marco", 15, False), ("Giulia", 30, True), ("Luca", 30, False)]` e stampate nome ed esito di ognuno.

| Caso | Valore restituito |
|---|---|
| voto minore di 0 o maggiore di 30 | `voto non valido` |
| voto minore di 18 | `respinto` |
| 30 con `lode=True` | `30 e lode` |
| tutti gli altri | `promosso con 27` (con il voto) |

**Esempio di esecuzione**

```
promosso con 28
30 e lode
Anna: promosso con 27
Marco: respinto
Giulia: 30 e lode
Luca: promosso con 30
```

**Provate anche**

- `esito(17)` → `respinto`
- `esito(27, lode=True)` → `promosso con 27`
- `esito(31)` → `voto non valido`

---

## Esercizio 2 — Media ponderata (`media_ponderata.py`)

**Consegna**

1. Scrivete `media_ponderata(voti: list[int], cfu: list[int]) -> float`: somma dei prodotti voto × crediti, divisa per il totale dei crediti. Scorrete le due liste insieme con `zip()`.
2. Se la lista dei voti è vuota o le due liste hanno lunghezze diverse, la funzione restituisce `0.0`.
3. Scrivete `base_laurea(media: float) -> float`, che porta la media in centodecimi: `media * 110 / 30`.
4. Con `voti = [28, 30, 25, 27, 30, 24]` e `cfu = [9, 6, 12, 6, 9, 6]` stampate la media aritmetica e la media ponderata con due decimali, e la base di laurea con un decimale.

**Esempio di esecuzione**

```
Media aritmetica: 27.33
Media ponderata: 27.25
Base di laurea: 99.9/110
```

**Provate anche**

- aggiungete un 30 da 12 CFU → ponderata `27.80`, base `101.9/110`
- `media_ponderata([], [])` → `0.0`
- `media_ponderata([28, 30], [9])` → `0.0` (lunghezze diverse)

---

## Esercizio 3 — Media e varianza a mano (`descrittive.py`)

**Consegna**

1. Scrivete `media(valori: list[float]) -> float`.
2. Scrivete `varianza(valori: list[float], campionaria: bool = True) -> float`: somma dei quadrati degli scarti dalla media, divisa per `n - 1` se `campionaria` è `True`, per `n` altrimenti. Dentro, chiamate `media()`.
3. Con le altezze in cm `[172.0, 165.5, 180.2, 158.0, 175.3, 169.8, 183.1, 162.4]` calcolate media, varianza campionaria, varianza di popolazione (`campionaria=False`) e deviazione standard (radice della varianza campionaria, `** 0.5`).
4. Importate `statistics` e accanto a ogni valore stampate quello di `mean`, `variance`, `pvariance` e `stdev`, per controllare i vostri calcoli. Due decimali.

**Esempio di esecuzione**

```
Media: 170.79 (statistics: 170.79)
Varianza campionaria: 74.98 (statistics: 74.98)
Varianza di popolazione: 65.60 (statistics: 65.60)
Deviazione standard: 8.66 (statistics: 8.66)
```

**Provate anche**

- `[10.0, 20.0, 30.0]` → media `20.00`, varianze `100.00` e `66.67`, deviazione standard `10.00`
- chiamate `varianza(altezze, False)` e `varianza(altezze, campionaria=False)`: danno lo stesso risultato

---

## Esercizio 4 — Tempi di viaggio (`riassunto.py`)

**Consegna**

1. La lista `tempi: list[float] = [35, 12, 50, 20, 75, 18, 40, 25]` contiene i minuti che otto studenti impiegano per arrivare in università.
2. Scrivete `mediana(valori: list[float]) -> float`: ordinate con `sorted()`; con `n` dispari la mediana è l'elemento centrale, con `n` pari la media dei due centrali.
3. Scrivete `riassunto(valori: list[float]) -> tuple[float, float, float]`, che restituisce minimo, mediana e massimo (usate `min()` e `max()`).
4. Spacchettate il risultato in tre variabili e stampate i tre valori e il campo di variazione (massimo − minimo), con un decimale.

**Esempio di esecuzione**

```
Minimo: 12.0 minuti
Mediana: 30.0 minuti
Massimo: 75.0 minuti
Campo di variazione: 63.0 minuti
```

**Provate anche**

- aggiungete `90` (nove studenti) → mediana `35.0`, campo `78.0`
- controllate la vostra mediana con `statistics.median(tempi)`
- dopo la chiamata, `tempi` deve essere ancora nell'ordine iniziale

---

## Esercizio 5 — Quanto manca all'esame (`esami_date.py`)

**Consegna**

1. Importate `date` dal modulo `datetime`. La differenza tra due date è un intervallo: `(d2 - d1).days` sono i giorni.
2. Scrivete `giorni_mancanti(esame: date, oggi: date) -> int` e `settimane_e_giorni(giorni: int) -> tuple[int, int]`, che usa `//` e `%`.
3. Scrivete `nome_giorno(giorno: date) -> str`: `giorno.weekday()` dà 0 per il lunedì e 6 per la domenica; usatelo come indice in una lista con i nomi dei giorni.
4. Con `oggi = date(2026, 11, 19)` e il dizionario degli appelli in tabella, stampate per ogni esame il giorno della settimana, la data e quanto manca. Se la data è già passata stampate `esame già passato`.

| Esame | Data |
|---|---|
| Analisi 1 | `date(2027, 1, 18)` |
| Statistica 1 | `date(2027, 1, 28)` |
| Sistemi di elaborazione | `date(2027, 2, 10)` |

**Esempio di esecuzione**

```
Analisi 1: lunedì 2027-01-18
  tra 60 giorni: 8 settimane e 4 giorni
Statistica 1: giovedì 2027-01-28
  tra 70 giorni: 10 settimane e 0 giorni
Sistemi di elaborazione: mercoledì 2027-02-10
  tra 83 giorni: 11 settimane e 6 giorni
```

**Provate anche**

- `oggi = date(2027, 1, 25)` → Analisi 1 già passato, Statistica 1 `tra 3 giorni`, Sistemi `tra 16 giorni: 2 settimane e 2 giorni`
- `nome_giorno(date(2026, 12, 25))` → `venerdì`

---

## Esercizio 6 — Classifica del corso (`classifica.py`)

**Consegna**

1. Ogni studente è una tupla (nome, media, crediti): `studenti = [("Marco", 26.4, 66), ("Anna", 28.1, 54), ("Sara", 26.4, 72), ("Luca", 24.9, 48), ("Giulia", 29.3, 60)]`.
2. Scrivete `classifica(studenti: list[tuple[str, float, int]]) -> list[tuple[str, float, int]]`, che restituisce una nuova lista ordinata per media decrescente e, a parità di media, per nome: `sorted()` con `key=lambda s: (-s[1], s[0])`.
3. Scrivete `in_regola(studenti: list[tuple[str, float, int]], cfu_minimi: int = 60) -> list[str]`, che restituisce i nomi di chi ha almeno `cfu_minimi` crediti.
4. Stampate la classifica numerata (con `enumerate`), lo studente con più crediti (`max()` con `key`) e i nomi in regola con 60 e con 70 crediti.

**Esempio di esecuzione**

```
1. Giulia: 29.3 (60 CFU)
2. Anna: 28.1 (54 CFU)
3. Marco: 26.4 (66 CFU)
4. Sara: 26.4 (72 CFU)
5. Luca: 24.9 (48 CFU)
Più crediti: Sara con 72
In regola con 60 CFU: ['Marco', 'Sara', 'Giulia']
In regola con 70 CFU: ['Sara']
```

**Provate anche**

- aggiungete `("Elena", 28.1, 61)` → Elena è terza, dopo Anna
- `in_regola(studenti, cfu_minimi=0)` → tutti i nomi
- dopo `classifica(studenti)` la lista `studenti` non è cambiata

---

## Esercizio 7 — Come arrivate in università (`questionario.py`)

**Consegna**

1. Le risposte a un questionario sono scritte in modo disordinato: `grezze = ["Bici", " autobus", "treno ", "BICI", "", "a piedi", "Treno", "bici", "Autobus ", "treno", "autobus", "  "]`.
2. Scrivete `pulisci(risposte: list[str]) -> list[str]`: toglie gli spazi ai lati, passa in minuscolo e scarta le risposte vuote (una comprehension con filtro).
3. Scrivete `frequenze_relative(risposte: list[str]) -> dict[str, float]`: con `Counter` e `most_common()`, dalla risposta più comune alla meno comune.
4. Scrivete `mode(risposte: list[str]) -> list[str]`: tutte le risposte con la frequenza massima, in ordine alfabetico; `[]` se la lista è vuota.
5. Stampate le risposte valide sul totale, le frequenze in percentuale con un decimale e le mode.

**Esempio di esecuzione**

```
Risposte valide: 10 su 12
bici: 30.0%
autobus: 30.0%
treno: 30.0%
a piedi: 10.0%
Moda: ['autobus', 'bici', 'treno']
```

**Provate anche**

- aggiungete `"Bici "` → `bici: 36.4%`, moda `['bici']`
- `grezze = ["", " "]` → `Risposte valide: 0 su 2` e `Moda: []`

---

## Esercizio 8 — Frequentanti e non frequentanti (`confronto_gruppi.py`)

**Consegna**

1. Punteggi di una prova intermedia: `frequentanti = [27, 24, 30, 22, 28, 19, 26, 25, 29, 16]` e `non_frequentanti = [21, 18, 30, 14, 23, 25, 13, 20]`.
2. Scrivete `confronta(a: list[float], b: list[float], statistica: callable) -> tuple[float, float, float]`: chiama la funzione `statistica` su ciascun gruppo e restituisce i due valori e la differenza a − b.
3. Scrivete `campo(valori: list[float]) -> float`, che restituisce massimo − minimo.
4. Mettete in un dizionario nome → funzione le misure della tabella, senza parentesi dopo il nome della funzione. Scorrete il dizionario, chiamate `confronta` e stampate una riga per misura, con due decimali.

| Nome | Funzione |
|---|---|
| Media | `statistics.mean` |
| Mediana | `statistics.median` |
| Deviazione standard | `statistics.stdev` |
| Campo di variazione | `campo` |
| Minimo | `min` |

**Esempio di esecuzione**

```
Media: 24.60 contro 20.50 (differenza 4.10)
Mediana: 25.50 contro 20.50 (differenza 5.00)
Deviazione standard: 4.48 contro 5.63 (differenza -1.15)
Campo di variazione: 14.00 contro 17.00 (differenza -3.00)
Minimo: 16.00 contro 13.00 (differenza 3.00)
```

**Provate anche**

- `confronta([18, 30], [24], statistics.mean)` → `(24, 24, 0)`
- aggiungete `"Quota di sufficienti"` con `lambda v: len([x for x in v if x >= 18]) / len(v)` → `0.90 contro 0.75 (differenza 0.15)`

---

## Challenge a scelta

Scegliete un tema. Le cinque challenge hanno la stessa difficoltà e usano gli stessi strumenti: cambiano la storia e i dati. Ogni tema continua nei laboratori successivi.

| Tema | Challenge | File |
|---|---|---|
| Mercati e finanza | Rischio e rendimento | `ch_mercati.py` |
| Sport | Il passo gara | `ch_sport.py` |
| Imprese e marketing | Margini e sconti | `ch_negozio.py` |
| Salute e scienza | Le variazioni di pressione | `ch_salute.py` |
| Caso e probabilità | Tanti lanci | `ch_probabilita.py` |

**Tutte le challenge chiedono:**

- Ogni challenge usa: almeno tre funzioni, ciascuna con type hints e una docstring di una riga; le funzioni restituiscono i risultati e la stampa la fa chi le chiama.
- Una funzione con un parametro di default, chiamata sia senza quell'argomento sia con l'argomento keyword (per esempio `soglia=5`).
- Una funzione che restituisce una tupla, spacchettata da chi la chiama (`media, dev = ...`).
- Un `sorted`, `max` o `min` con `key=lambda ...`.
- Il modulo `statistics` per controllare un calcolo fatto a mano; nella challenge sul caso anche `random`, con `random.seed(2026)`.
- Un controllo con `if` sui dati sbagliati o impossibili, che vanno scartati prima dei calcoli. Niente `try`, file e classi.

---

### Challenge · Mercati e finanza — Rischio e rendimento (`ch_mercati.py`)

**Consegna**

1. Il portafoglio costruito in L03 è `{"ENRG": 40, "BANK": 20, "TECH": 20}`. Scrivete i prezzi di chiusura di otto giorni in `prezzi: dict[str, list[float]]` (tabella). Il quinto prezzo di ENRG manca ed è registrato come `0.0`.
2. Scrivete `rendimenti(prezzi: list[float]) -> list[float]`: scarta con una comprehension con `if` i prezzi non positivi, poi calcola i rendimenti giornalieri `(p_oggi - p_ieri) / p_ieri`.
3. Scrivete `rischio(rend: list[float]) -> tuple[float, float]`, che restituisce il rendimento medio e la deviazione standard campionaria (la volatilità), calcolati a mano. Per ogni titolo spacchettate il risultato e stampatelo con `.2%`, accanto al valore di `statistics.stdev`.
4. Con `max` e `key=lambda` trovate il titolo più volatile.
5. Scrivete `valore(azioni: dict[str, int], prezzi: dict[str, list[float]], giorno: int = -1) -> float`, il valore del portafoglio in un giorno, di default l'ultimo. Stampate il valore del primo giorno (`giorno=0`) e dell'ultimo, con due decimali.

| Titolo | Prezzi di chiusura (euro) |
|---|---|
| ENRG | 12.40, 12.10, 12.55, 12.80, 0.0, 13.05, 12.90, 13.20 |
| BANK | 8.15, 8.30, 8.60, 8.45, 8.75, 8.70, 8.90, 8.85 |
| TECH | 45.20, 47.80, 44.90, 46.30, 48.10, 45.60, 49.20, 50.10 |

**Esempio di esecuzione**

```
ENRG: media 1.07%, volatilità 2.34% (statistics: 2.34%)
BANK: media 1.20%, volatilità 2.16% (statistics: 2.16%)
TECH: media 1.60%, volatilità 5.31% (statistics: 5.31%)
Più volatile: TECH
Valore il primo giorno: 1563.00 euro
Valore l'ultimo giorno: 1707.00 euro
```

**Provate anche**

- togliete lo `0.0` dalla serie di ENRG → l'output non cambia
- `valore(portafoglio, prezzi, giorno=1)` → `1606.0`; con `giorno=4` → `1137.0`, perché il prezzo mancante di ENRG conta come 0
- portafoglio con 40 azioni TECH → `Valore l'ultimo giorno: 2709.00 euro`

---

### Challenge · Sport — Il passo gara (`ch_sport.py`)

**Consegna**

1. Nell'ultima gara del campionato sono stati cronometrati otto giri per pilota, in secondi (tabella): `tempi: dict[str, list[float]]`. I giri sopra i 100 secondi sono pit stop; lo `0.0` di Neri è un giro non registrato.
2. Scrivete `validi(tempi: list[float], limite: float = 100.0) -> list[float]`, che tiene con una comprehension con `if` i tempi maggiori di 0 e minori di `limite`.
3. Scrivete `passo(tempi: list[float]) -> tuple[float, float]`, che restituisce media e deviazione standard campionaria calcolate a mano. Per ogni pilota spacchettate il risultato sui giri validi e stampate il numero di giri validi, il passo e la deviazione standard con due decimali, accanto al valore di `statistics.stdev`.
4. Scrivete `piu_veloce(tempi: dict[str, list[float]]) -> str`, che con `min` e `key=lambda` restituisce il pilota con il passo medio più basso sui giri validi.
5. Con una dict comprehension e `validi(giri, limite=93.0)` stampate quanti giri sotto i 93 secondi ha fatto ogni pilota.

| Pilota | Tempi sul giro (secondi) |
|---|---|
| Ferri | 92.8, 92.4, 92.1, 113.6, 92.6, 92.3, 92.9, 93.1 |
| Lanza | 93.2, 92.9, 93.4, 93.0, 114.8, 93.3, 93.6, 93.8 |
| Moro | 92.5, 92.0, 91.8, 92.2, 112.9, 92.1, 92.4, 92.7 |
| Neri | 93.5, 93.9, 115.2, 93.4, 93.7, 94.1, 0.0, 94.3 |

**Esempio di esecuzione**

```
Ferri: 7 giri validi, passo 92.60 s, dev. std 0.36 (statistics: 0.36)
Lanza: 7 giri validi, passo 93.31 s, dev. std 0.32 (statistics: 0.32)
Moro: 7 giri validi, passo 92.24 s, dev. std 0.31 (statistics: 0.31)
Neri: 6 giri validi, passo 93.82 s, dev. std 0.35 (statistics: 0.35)
Passo migliore: Moro
Giri sotto 93 secondi: {'Ferri': 6, 'Lanza': 1, 'Moro': 7, 'Neri': 0}
```

**Provate anche**

- `validi(tempi["Neri"])` → `[93.5, 93.9, 93.4, 93.7, 94.1, 94.3]`
- con `limite=92.5` → `{'Ferri': 3, 'Lanza': 0, 'Moro': 5, 'Neri': 0}`
- il 114.8 di Lanza diventa 94.8 (un giro dietro la safety car) → `Lanza: 8 giri validi, passo 93.50 s, dev. std 0.60 (statistics: 0.60)`

---

### Challenge · Imprese e marketing — Margini e sconti (`ch_negozio.py`)

**Consegna**

1. Il catalogo del negozio ha ora anche il costo di ogni prodotto: `CATALOGO: dict[str, tuple[float, float]]`, prodotto → (prezzo, costo), con i dati della tabella. I pezzi venduti in settimana sono `{"zaino": 2, "borraccia": 5, "quaderno": 12, "cuffie": 2, "lampada": 3, "penna": 4}`; la penna non è in catalogo.
2. Scrivete `valido(prodotto: str, pezzi: int) -> bool` (prodotto in catalogo e pezzi positivi) e usatela in una dict comprehension con `if` per tenere solo le vendite valide.
3. Scrivete `bilancio(prodotto: str, pezzi: int, sconto: float = 0.0) -> tuple[float, float]`, che restituisce incasso e margine (incasso − costo × pezzi). Lo sconto riduce il prezzo: `sconto=0.2` vuol dire 20% in meno.
4. Scrivete `classifica(venduti: dict[str, int]) -> list[str]`, che ordina i prodotti dal margine più alto al più basso con `sorted` e `key=lambda`. Scorrete la classifica, spacchettate il risultato di `bilancio` e stampate incasso e margine di ogni prodotto.
5. Stampate l'incasso medio per prodotto, calcolato a mano e con `statistics.mean`. Infine stampate incasso e margine degli zaini con lo sconto del 20%.

| Prodotto | Prezzo e costo (euro) |
|---|---|
| zaino | 39.90 e 22.00 |
| borraccia | 12.50 e 5.20 |
| quaderno | 3.20 e 1.10 |
| cuffie | 24.90 e 14.50 |
| lampada | 18.00 e 9.80 |

**Esempio di esecuzione**

```
borraccia: incasso 62.50, margine 36.50
zaino: incasso 79.80, margine 35.80
quaderno: incasso 38.40, margine 25.20
lampada: incasso 54.00, margine 24.60
cuffie: incasso 49.80, margine 20.80
Incasso medio: 56.90 (statistics: 56.90)
Zaini con lo sconto del 20%: incasso 63.84, margine 19.84
```

**Provate anche**

- `bilancio("cuffie", 2, sconto=0.5)` → incasso `24.9` e margine circa `-4.1`: con la metà del prezzo si vende sotto costo
- aggiungete al catalogo `"penna": (1.50, 0.40)` → nuova riga `penna: incasso 6.00, margine 4.40` e `Incasso medio: 48.42 (statistics: 48.42)`
- `valido("zaino", 0)` → `False`

---

### Challenge · Salute e scienza — Le variazioni di pressione (`ch_salute.py`)

**Consegna**

1. Lo studio di L03 è arrivato a 12 pazienti. I dati sono in un dizionario gruppo → lista di tuple (codice, prima, dopo): `studio: dict[str, list[tuple[str, int, int]]]` (tabella). Due misure sono sbagliate: P07 non ha la seconda misura (0) e per P12 è stato scritto 15 invece di 150.
2. Scrivete `valido(riga: tuple[str, int, int]) -> bool`: le due pressioni devono stare tra 60 e 250 mmHg. Per ogni gruppo tenete le righe valide con una comprehension con `if` e calcolate le variazioni dopo − prima.
3. Scrivete `descrivi(diff: list[int]) -> tuple[float, float]`, che restituisce media e deviazione standard campionaria calcolate a mano. Spacchettate il risultato e stampatelo accanto al valore di `statistics.stdev`.
4. Scrivete `migliorati(diff: list[int], soglia: int = 10) -> float`, la quota di pazienti scesi di almeno `soglia` mmHg. Stampate il numero di pazienti validi e la quota con la soglia di default e con `soglia=5`.
5. Con `min` e `key=lambda` trovate in ogni gruppo il paziente con il calo maggiore.

| Gruppo | Pazienti: pressione prima → dopo (mmHg) |
|---|---|
| trattamento | P01 152 → 138, P03 160 → 147, P05 145 → 140, P07 158 → 0, P09 162 → 148, P11 154 → 139 |
| controllo | P02 148 → 145, P04 155 → 150, P06 150 → 152, P08 149 → 138, P10 157 → 155, P12 15 → 146 |

**Esempio di esecuzione**

```
trattamento: media -12.2 mmHg, dev. std 4.09 (statistics: 4.09)
  5 validi, migliorati 80.0%, con soglia 5: 100.0%
  calo maggiore: P11
controllo: media -3.8 mmHg, dev. std 4.76 (statistics: 4.76)
  5 validi, migliorati 20.0%, con soglia 5: 40.0%
  calo maggiore: P08
```

**Provate anche**

- `migliorati([-14, -13, -5, -14, -15], soglia=15)` → `0.2`
- correggete P12 in `("P12", 150, 146)` → `controllo: media -3.8 mmHg, dev. std 4.26 (statistics: 4.26)` e `6 validi, migliorati 16.7%, con soglia 5: 33.3%`

---

### Challenge · Caso e probabilità — Tanti lanci (`ch_probabilita.py`)

**Consegna**

1. Nella serata di L03 Ada, Bea e Ciro hanno fatto solo 12 lanci. Ora i lanci di due dadi si simulano: chiamate `random.seed(2026)` una volta, prima di tutte le simulazioni.
2. Scrivete `simula(n: int) -> list[int]`, che restituisce le somme di `n` lanci di due dadi (`random.randint(1, 6)`), e `riassunto(somme: list[int]) -> tuple[float, float]`, che restituisce media e deviazione standard campionaria calcolate a mano.
3. Per 10, 100, 1000 e 10000 lanci, in quest'ordine, spacchettate il risultato di `riassunto` e stampate media e deviazione standard con due decimali, accanto al valore di `statistics.stdev`.
4. Scrivete `esatta(somma: int, facce: int = 6) -> float`: se la somma è impossibile (minore di 2 o maggiore di `2 * facce`) restituisce `0.0`, altrimenti conta con una comprehension su due cicli le coppie con quella somma e divide per `facce ** 2`.
5. Sui 10000 lanci trovate con `max` e `key=lambda` la somma uscita più spesso e confrontate la sua frequenza con la probabilità esatta. Stampate infine la probabilità di fare 5 con due dadi da 4 facce (`facce=4`).

**Esempio di esecuzione**

```
10 lanci: media 7.90, dev. std 2.23 (statistics: 2.23)
100 lanci: media 7.42, dev. std 2.43 (statistics: 2.43)
1000 lanci: media 6.98, dev. std 2.47 (statistics: 2.47)
10000 lanci: media 6.95, dev. std 2.43 (statistics: 2.43)
Somma più frequente: 7, 16.4% dei lanci (esatta 16.7%)
Somma 5 con due dadi da 4 facce: 25.0%
```

**Provate anche**

- `random.seed(1)` → numeri diversi, ma con 10000 lanci la media resta vicina a 7 (`6.97`)
- `esatta(12)` → `0.0277...` (1 caso su 36); `esatta(13)` → `0.0`
- `esatta(3, facce=4)` → `0.125`

---

## Domande di verifica

1. In `esito.py`, cosa stampa `print(esito(28))` se nella funzione si scrive `print` al posto di `return`?
2. In `media_ponderata.py`, cosa succederebbe senza il controllo sulle lunghezze se `cfu` avesse un elemento in meno di `voti`?
3. In `descrittive.py`, perché la varianza campionaria è più grande di quella di popolazione? Di quanto, con 8 valori?
4. In `riassunto.py`, cosa cambierebbe se `mediana` usasse `valori.sort()` invece di `sorted(valori)`?
5. In `classifica.py`, perché nella chiave si scrive `-s[1]` invece di usare `reverse=True`?
6. In `confronto_gruppi.py`, che differenza c'è tra scrivere `statistics.mean` e `statistics.mean(frequentanti)`?
7. Nella sfida, a cosa serve `random.seed(2026)`? Cosa succede togliendolo?
