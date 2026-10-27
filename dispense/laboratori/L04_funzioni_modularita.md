# Laboratorio 4 — Funzioni e modularità

**Prerequisiti:** lezioni T13 (Funzioni) e T14 (Funzioni avanzate e moduli).

Oggi ci sono solo esercizi, in ordine di difficoltà. Per ogni esercizio create un file `.py` con il nome indicato: dentro scrivete le funzioni richieste, con type hints e docstring, e poi chiamatele sui dati della consegna stampando i risultati. Non serve `input()`: i dati sono già scritti nella consegna. Tutto il codice di un esercizio sta in un solo file.

Ogni esercizio ha la consegna, un esempio di esecuzione e alcuni casi da provare: il programma è corretto quando dà gli stessi risultati. La sfida è per chi finisce prima. Le soluzioni le vediamo all'inizio della lezione T15.

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
| Sfida | `compleanni.py` | Compleanni in aula |

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

## Sfida — Compleanni in aula (`compleanni.py`)

**Consegna**

1. Con quanti studenti in aula diventa probabile che due compiano gli anni lo stesso giorno? Ignorate il 29 febbraio: i giorni sono 365.
2. Scrivete `compleanno_comune(n: int) -> bool`: estrae `n` compleanni con `random.randint(1, 365)` e restituisce `True` se almeno due coincidono (confrontate la lunghezza della lista con quella del suo `set`).
3. Scrivete `stima(n_studenti: int, prove: int = 10000) -> float`, che ripete la simulazione `prove` volte e restituisce la quota di volte con un compleanno in comune.
4. Scrivete `esatta(n_studenti: int) -> float`: la probabilità che i compleanni siano tutti diversi è 365/365 × 364/365 × … × (365 − n + 1)/365; il risultato è 1 meno questo prodotto.
5. Chiamate `random.seed(2026)` una volta, poi per 10, 23, 30 e 50 studenti, in quest'ordine, stampate stima e valore esatto in percentuale con un decimale. Infine trovate con un `while` il primo numero di studenti con probabilità esatta oltre il 50%.

**Esempio di esecuzione**

```
10 studenti: simulata 11.7%, esatta 11.7%
23 studenti: simulata 50.9%, esatta 50.7%
30 studenti: simulata 71.1%, esatta 70.6%
50 studenti: simulata 97.3%, esatta 97.0%
Si supera il 50% con 23 studenti
```

**Provate anche**

- `esatta(40)` → `89.1%`
- il 90% si supera con `41` studenti
- con `prove=1000` le stime cambiano ma restano vicine ai valori esatti

---

## Domande di verifica

1. In `esito.py`, cosa stampa `print(esito(28))` se nella funzione si scrive `print` al posto di `return`?
2. In `media_ponderata.py`, cosa succederebbe senza il controllo sulle lunghezze se `cfu` avesse un elemento in meno di `voti`?
3. In `descrittive.py`, perché la varianza campionaria è più grande di quella di popolazione? Di quanto, con 8 valori?
4. In `riassunto.py`, cosa cambierebbe se `mediana` usasse `valori.sort()` invece di `sorted(valori)`?
5. In `classifica.py`, perché nella chiave si scrive `-s[1]` invece di usare `reverse=True`?
6. In `confronto_gruppi.py`, che differenza c'è tra scrivere `statistics.mean` e `statistics.mean(frequentanti)`?
7. Nella sfida, a cosa serve `random.seed(2026)`? Cosa succede togliendolo?
