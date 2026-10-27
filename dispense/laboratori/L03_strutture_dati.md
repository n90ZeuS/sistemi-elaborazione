# Laboratorio 3 — Strutture dati

**Prerequisiti:** lezioni T11 (Liste e tuple), T12 (Dizionari e set) e T13 (Funzioni).

Oggi ci sono solo esercizi, in ordine di difficoltà, su liste, tuple, dizionari e set. Per ogni esercizio create un file `.py` con il nome indicato e scrivete il programma da soli. Le funzioni servono solo negli ultimi esercizi.

Ogni esercizio ha la consegna, un esempio di esecuzione e alcuni casi da provare: il programma è corretto quando dà gli stessi risultati. La sfida è per chi finisce prima. Le soluzioni le vediamo all'inizio della lezione T14.

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
| Sfida | `compagni.py` | Compagni di corsi a scelta |

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

## Sfida — Compagni di corsi a scelta (`compagni.py`)

**Consegna**

1. Scrivete il dizionario `scelte: dict[str, set[str]]` con i corsi a scelta di ogni studente (tabella).
2. Scrivete la funzione `jaccard(a, b)` che restituisce la similarità di Jaccard tra due set: elementi in comune diviso elementi totali.
3. Con due cicli annidati sui nomi in ordine alfabetico, con `j` che parte da `i + 1`, confrontate ogni coppia una volta sola e stampate la coppia più simile con la similarità a due decimali.
4. Chiedete il nome di uno studente, trovate il compagno più simile e stampate i corsi che il compagno segue e lui no. Se il nome non c'è, stampate `Studente non trovato`.

| Studente | Corsi a scelta |
|---|---|
| Anna | Serie storiche, Demografia, Marketing, R |
| Bruno | Marketing, Finanza, R, Python |
| Chiara | Serie storiche, Demografia, R, Biostatistica |
| Davide | Finanza, Python, Econometria |
| Elisa | Biostatistica, Demografia, Python |

**Esempio di esecuzione**

```
Coppia più simile: ('Anna', 'Chiara') con 0.60
Studente: Elisa
Più simile: Chiara (0.40)
Corsi consigliati: ['R', 'Serie storiche']
```

**Provate anche**

- `Bruno` → `Davide (0.40)`, consigliato `['Econometria']`
- `Davide` → `Bruno (0.40)`, consigliati `['Marketing', 'R']`
- `Zeno` → `Studente non trovato`

---

## Domande di verifica

1. Che differenza c'è tra `sorted(voti)` e `voti.sort()`? Quale dei due modifica la lista?
2. In `coda_mensa.py`, cosa succede con `coda.remove("Zeno")` se prima non si controlla con `in`?
3. In `sondaggio.py`, perché le risposte vanno pulite prima di passarle a `Counter`?
4. Perché, per stampare un set, conviene usare `sorted()`?
5. In `libretto.py`, quando la media ponderata coincide con la media aritmetica?
6. In `contingenza.py` le chiavi del `Counter` sono tuple. Si potrebbero usare liste? Perché?
7. In `descrittive.py` la funzione restituisce tre valori: che tipo ha il risultato e come si separa in tre variabili?
