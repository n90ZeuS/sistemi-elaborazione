# Laboratorio 8 — Visualizzazione e progetto

**Prerequisiti:** lezioni T17 (NumPy, Pandas e visualizzazione) e laboratorio L07.

Ultimo laboratorio, in due parti. Nella prima ci sono sei esercizi brevi sui grafici con Matplotlib, dal più semplice al più articolato: ognuno salva un'immagine PNG e stampa poche righe di controllo. Nella seconda c'è il progetto finale: scegliete uno dei 5 temi e analizzate un file CSV dal caricamento alla conclusione. Per ogni esercizio create un file `.py` con il nome indicato. Le soluzioni iniziano con `matplotlib.use("Agg")`, che salva i grafici senza aprire finestre: a casa potete toglierlo e aggiungere `plt.show()` dopo `plt.savefig(...)` per vedere il grafico.

Ogni esercizio ha la consegna, un esempio di esecuzione e alcuni casi da provare: il programma è corretto quando dà gli stessi risultati. Alla fine c'è una challenge a scelta tra 5 temi. Le soluzioni vengono pubblicate sul portale dopo il laboratorio.

| # | File | Esercizio |
|---|---|---|
| 1 | `immatricolati.py` | Immatricolati e laureati |
| 2 | `voti.py` | I voti dell'appello |
| 3 | `studio.py` | Ore di studio e voto |
| 4 | `mensa.py` | L'attesa in mensa |
| 5 | `tragitto.py` | Il tragitto per l'università |
| 6 | `meteo.py` | Gennaio in due grafici |
| Challenge | a scelta | Mercati e finanza · Sport · Imprese e marketing · Salute e scienza · Caso e probabilità |

---

## Promemoria

Ogni grafico segue gli stessi passi: nuova figura, disegno, titolo, etichette degli assi con l'unità di misura, `tight_layout()` e salvataggio. `plt.savefig` va chiamato prima di `plt.show()`, che alla chiusura della finestra svuota la figura. Per disegnare un risultato di `groupby` si passano `index` (le etichette) e `values` (i numeri).

```python
import matplotlib
matplotlib.use("Agg")                 # a casa si può togliere
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("dati.csv", sep=";")  # carica
df = df.drop_duplicates().dropna()     # pulisce
medie = df.groupby("gruppo")["valore"].mean()
plt.figure(figsize=(7, 4))             # nuova figura
plt.bar(medie.index, medie.values)     # oppure plot, hist, scatter
plt.title("Valore medio per gruppo")   # titolo ed etichette
plt.xlabel("Gruppo")
plt.ylabel("Valore medio")
plt.tight_layout()                     # niente etichette tagliate
plt.savefig("grafico.png")             # prima di plt.show()
```

---

## Esercizio 1 — Immatricolati e laureati (`immatricolati.py`)

**Consegna**

1. Scrivete i dati nel codice: `anni = list(range(2018, 2026))`, `immatricolati = [182, 195, 210, 204, 231, 248, 240, 262]`, `laureati = [118, 126, 131, 140, 137, 152, 160, 171]`.
2. Create la figura con `plt.figure(figsize=(7, 4))` e disegnate le due serie con `plt.plot`: per ognuna un `marker` e una `label` diversi, i laureati con `linestyle="--"`.
3. Aggiungete titolo, etichette degli assi, legenda e una griglia leggera (`plt.grid(True, alpha=0.3)`), poi salvate con `plt.savefig("immatricolati.png")`. A casa potete aggiungere `plt.show()` dopo il salvataggio.
4. Stampate l'anno con più immatricolati (`immatricolati.index(max(immatricolati))`) e la variazione tra il primo e l'ultimo anno.

**Esempio di esecuzione**

```
Anno con più immatricolati: 2025 (262)
Variazione 2018-2025: 44.0%
```

**Provate anche**

- ultimo valore `230` invece di `262` → `Anno con più immatricolati: 2023 (248)`, `Variazione 2018-2025: 26.4%`
- togliete `plt.legend()`: le linee restano, ma non si sa quale serie sia quale

---

## Esercizio 2 — I voti dell'appello (`voti.py`)

**Consegna**

1. Generate i voti con `rng = np.random.default_rng(14)` e `tutti = rng.normal(23.5, 4, 250).round().clip(max=30)`: 250 voti interi, al massimo 30.
2. Tenete i promossi con un filtro booleano: `voti = tutti[tutti >= 18]`.
3. Disegnate l'istogramma con una barra per ogni voto (`bins=np.arange(17.5, 31)`) e `edgecolor="white"`. Aggiungete una linea verticale tratteggiata sulla media con `plt.axvline` e la legenda.
4. Salvate `voti.png` e stampate promossi, media dei promossi e quota di voti da 27 in su.

**Esempio di esecuzione**

```
Promossi: 233 su 250
Media dei promossi: 24.1
Voti da 27 in su: 26.2%
```

**Provate anche**

- seed `15` → `Promossi: 232 su 250`, `Media dei promossi: 24.2`, `Voti da 27 in su: 28.4%`
- deviazione standard `6` → `Promossi: 211 su 250`: l'istogramma si allarga e la barra del 30 si alza
- `bins=5`: ogni barra raccoglie più voti e la forma cambia

---

## Esercizio 3 — Ore di studio e voto (`studio.py`)

**Consegna**

1. Generate i dati di 80 studenti: `rng = np.random.default_rng(7)`, `ore = rng.uniform(20, 120, 80).round()`, `voto = (17 + 0.09 * ore + rng.normal(0, 2.5, 80)).round().clip(18, 30)`.
2. Disegnate un grafico di dispersione con `plt.scatter(ore, voto, alpha=0.6)`: la trasparenza mostra i punti sovrapposti.
3. Aggiungete titolo, etichette e griglia leggera e salvate `studio.png`.
4. Stampate la correlazione (`np.corrcoef(ore, voto)[0, 1]`) e il voto medio di chi ha studiato più di 80 ore e di chi ne ha studiate 80 o meno.

**Esempio di esecuzione**

```
Studenti: 80, correlazione: 0.67
Voto medio con più di 80 ore: 25.2
Voto medio con 80 ore o meno: 21.6
```

**Provate anche**

- rumore `rng.normal(0, 5, 80)` → `correlazione: 0.28`, medie `24.3` e `22.0`: i punti sono più sparsi
- togliete `alpha=0.6`: dove i punti si sovrappongono non si vede quanti sono

---

## Esercizio 4 — L'attesa in mensa (`mensa.py`)

**Consegna**

1. Costruite un DataFrame con 20 settimane di rilevazioni dell'attesa in mensa (minuti): `rng = np.random.default_rng(3)`, `giorni = ["lun", "mar", "mer", "gio", "ven"]`, attese tipiche `[12, 15, 14, 16, 8]`.
2. Colonne: `"giorno": giorni * 20` e `"attesa": np.tile(attesa_tipica, 20) + rng.normal(0, 3, 100)`.
3. Calcolate l'attesa media per giorno con `df.groupby("giorno", sort=False)["attesa"].mean()`: `sort=False` mantiene i giorni nell'ordine della settimana.
4. Disegnate le barre con `plt.bar(medie.index, medie.values)`, aggiungete titolo ed etichette, salvate `mensa.png` e stampate le rilevazioni, la media generale e i giorni con l'attesa più lunga e più corta (`idxmax`, `idxmin`).

**Esempio di esecuzione**

```
Rilevazioni: 100, media: 12.8 min
Giorno peggiore: gio (15.8 min)
Giorno migliore: ven (7.4 min)
```

**Provate anche**

- senza `sort=False` le righe stampate non cambiano, ma le barre sono in ordine alfabetico: `gio`, `lun`, `mar`, `mer`, `ven`
- aggiungete `plt.axhline(df["attesa"].mean(), color="red", linestyle="--")`: si vedono i giorni sopra la media

---

## Esercizio 5 — Il tragitto per l'università (`tragitto.py`)

**Consegna**

1. Generate i tempi (minuti) di 40 tragitti per mezzo con `rng = np.random.default_rng(11)` e un dizionario: `"bici": rng.normal(22, 3, 40).round()`, `"autobus": rng.normal(28, 7, 40).round()`, `"treno": rng.normal(35, 4, 40).round()`.
2. Disegnate un boxplot con `plt.boxplot(list(tempi.values()), tick_labels=list(tempi.keys()))`. Con Matplotlib precedente alla 3.9 il parametro si chiama `labels`.
3. Aggiungete titolo ed etichette e salvate `tragitto.png`.
4. Per ogni mezzo stampate la mediana (`np.median`) e la quota di tragitti oltre 30 minuti.

**Esempio di esecuzione**

```
bici: mediana 22 min, oltre 30 min 0.0%
autobus: mediana 30 min, oltre 30 min 47.5%
treno: mediana 35 min, oltre 30 min 82.5%
```

**Provate anche**

- autobus con `rng.normal(28, 2, 40)` → `autobus: mediana 29 min, oltre 30 min 7.5%`: la scatola si stringe
- il treno ha la mediana più alta ma una scatola più stretta dell'autobus: è più lento ma più regolare

---

## Esercizio 6 — Gennaio in due grafici (`meteo.py`)

**Consegna**

1. Generate le temperature di 31 giorni: `rng = np.random.default_rng(1)`, `minime = rng.normal(0, 2.5, 31).round(1)`, `massime = (minime + rng.normal(7, 1.8, 31)).round(1)`.
2. Create due grafici affiancati con `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))`. Sugli assi si usano `ax1.plot(...)`, `ax1.set_title(...)`, `ax1.set_xlabel(...)`.
3. A sinistra le linee delle massime e delle minime giorno per giorno, con legenda; a destra l'istogramma dell'escursione termica (`massime - minime`, `bins=8`).
4. Chiudete con `fig.tight_layout()` e `fig.savefig("meteo.png")`, poi stampate i giorni con la minima sotto zero e l'escursione media.

**Esempio di esecuzione**

```
Giorni con la minima sotto zero: 13
Escursione media: 6.8 °C
```

**Provate anche**

- seed `2` → `Giorni con la minima sotto zero: 15`, `Escursione media: 7.4 °C`
- `plt.subplots(2, 1, figsize=(7, 7))`: i due grafici uno sopra l'altro

---

## Challenge a scelta

Scegliete un tema. Le cinque challenge hanno la stessa difficoltà e usano gli stessi strumenti: cambiano la storia e i dati. Ogni tema continua nei laboratori successivi.

| Tema | Challenge | File |
|---|---|---|
| Mercati e finanza | Due mesi di borsa | `ch_mercati.py` |
| Sport | Il passo gara | `ch_sport.py` |
| Imprese e marketing | Quattro mesi di ordini | `ch_negozio.py` |
| Salute e scienza | L'effetto dell'integratore | `ch_salute.py` |
| Caso e probabilità | Il dado sospetto | `ch_probabilita.py` |

**Tutte le challenge chiedono:**

- Scaricate dal portale il file CSV del vostro tema e mettetelo nella cartella del programma. Il separatore è `;`.
- Caricate: `grezzo = pd.read_csv(..., sep=";")`. Tenete il DataFrame originale per contare le righe lette.
- Pulite: togliete le righe doppie (`drop_duplicates()`), quelle con valori mancanti (`dropna()`) e quelle con valori impossibili, con un filtro booleano. Aggiungete `.copy()` all'ultimo filtro, prima di creare nuove colonne. Stampate righe lette e righe rimaste.
- Calcolate le colonne e le 3 statistiche indicate nel vostro tema: almeno una con `groupby`.
- Disegnate 3 grafici con titolo ed etichette degli assi e salvateli in PNG: un istogramma o boxplot, un grafico a linee o di dispersione, un grafico a barre per gruppo. Conviene una funzione `salva(nome: str, titolo: str, x: str, y: str) -> None` che mette titolo ed etichette, chiama `tight_layout()` e `savefig` e chiude la figura con `plt.close()`.
- Concludete con 3 righe stampate che commentano i risultati. I numeri vengono dalle variabili calcolate, non scritti a mano: se cambiano i dati, la conclusione si aggiorna.

---

### Challenge · Mercati e finanza — Due mesi di borsa (`ch_mercati.py`)

**Consegna**

1. `prezzi.csv` contiene i prezzi di chiusura di ENRG, BANK, TECH e dell'indice MIB, giorno per giorno, a settembre e ottobre 2026. Colonne: `data`, `titolo`, `prezzo`. Ci sono giorni ripetuti, prezzi mancanti e prezzi non positivi da scartare.
2. Dopo la pulizia aggiungete la colonna `rendimento` con `df.groupby("titolo")["prezzo"].pct_change()`: per ogni titolo calcola (p_oggi − p_ieri) / p_ieri. Il primo giorno di ogni titolo resta vuoto.
3. Statistiche: per ogni titolo il rendimento nel periodo (con `g = df.groupby("titolo")["prezzo"]`, `g.last() / g.first() - 1`) e la volatilità (deviazione standard dei rendimenti); i giorni in cui il MIB perde più dell'1%.
4. Grafici: `rendimenti.png`, istogramma dei rendimenti (con `dropna()`); `prezzi.png`, linee dei prezzi di ENRG, BANK e TECH con legenda (il MIB ha un'altra scala); `volatilita.png`, barre della volatilità per titolo.
5. Conclusione: titolo migliore e peggiore escluso il MIB (`rend.drop("MIB")`, `idxmax`, `idxmin`); il più volatile a confronto con il MIB; quanti titoli hanno reso più dell'indice.

**File di dati:** `prezzi.csv`, da scaricare dal portale (cartella del codice di L08).

**Esempio di esecuzione**

```
Righe lette: 179, dopo la pulizia: 172
BANK: rendimento 14.6%, volatilità 1.6%
ENRG: rendimento -10.6%, volatilità 1.2%
MIB: rendimento 1.9%, volatilità 0.9%
TECH: rendimento 21.6%, volatilità 2.2%
Giorni con il MIB in calo oltre l'1%: 4
Il migliore è TECH (21.6%), il peggiore ENRG (-10.6%).
Il più volatile è TECH, con 2.2% al giorno; il MIB si ferma a 0.9%.
Il MIB rende 1.9%: 2 titoli su 3 fanno meglio.
```

**Provate anche**

- senza `drop_duplicates()` → `dopo la pulizia: 175`; un giorno ripetuto dà rendimento 0 e le statistiche cambiano di poco
- senza il filtro sui prezzi → volatilità di ENRG `nan%` e di MIB `154.2%`, poi l'istogramma si ferma con `ValueError`: un prezzo 0 produce un rendimento infinito

---

### Challenge · Sport — Il passo gara (`ch_sport.py`)

**Consegna**

1. `tempi_giro.csv` contiene i tempi sul giro (secondi) di Ferri, Lanza, Moro e Neri in 3 gare da 15 giri. Colonne: `gara`, `pilota`, `giro`, `tempo`. Ci sono righe doppie, tempi mancanti e tempi impossibili: tenete solo quelli tra 60 e 180 secondi.
2. Aggiungete la colonna `lento` (`True` se il tempo supera 100 s: pit stop o safety car) e create `normali = df[~df["lento"]]`; `~` inverte i valori booleani.
3. Statistiche: il giro più veloce con pilota, gara e giro (`df.loc[df["tempo"].idxmin()]`); la quota di giri lenti; la media sui giri normali per pilota.
4. Grafici: `hist_tempi.png`, istogramma di tutti i tempi; `gara1.png`, linee dei giri normali della gara 1, una per pilota, con `marker="o"` e legenda; `distacchi.png`, barre del distacco di ogni pilota dal più veloce (media − media minima).
5. Conclusione: il più veloce sul passo gara e quanto perde al giro il più lento; quanti secondi costa in media un giro lento rispetto ai giri normali; cosa mostra il grafico della gara 1.

**File di dati:** `tempi_giro.csv`, da scaricare dal portale (cartella del codice di L08).

**Esempio di esecuzione**

```
Righe lette: 183, dopo la pulizia: 176
Giro più veloce: Moro, gara 2, giro 12, 88.3 s
Giri lenti (pit stop e safety car): 11.4%
Ferri: media sui giri normali 92.46 s
Lanza: media sui giri normali 93.01 s
Moro: media sui giri normali 92.68 s
Neri: media sui giri normali 93.22 s
Sul passo gara il più veloce è Ferri; Neri perde 0.76 s al giro.
Un giro lento costa 16.3 s in più e va escluso.
Gara 1: i tempi crescono fino al pit stop (usura gomme).
```

**Provate anche**

- senza il filtro sui tempi → `Giro più veloce: Lanza, gara 3, giro 13, 0.0 s` e Lanza risulta il più veloce sul passo gara
- senza `drop_duplicates()` → `dopo la pulizia: 179`, `Giri lenti (pit stop e safety car): 11.7%`

---

### Challenge · Imprese e marketing — Quattro mesi di ordini (`ch_negozio.py`)

**Consegna**

1. `ordini.csv` contiene gli ordini del negozio online da settembre a dicembre 2026. Colonne: `ordine`, `data`, `cliente`, `citta`, `prodotto`, `quantita`, `prezzo`. Ci sono ordini registrati due volte, quantità mancanti e quantità non positive da scartare.
2. Aggiungete le colonne `importo` (quantità × prezzo) e `mese`, i primi 7 caratteri della data (`df["data"].str[:7]`, per esempio `2026-09`).
3. Statistiche: fatturato totale e importo medio per ordine; fatturato per città con la quota sul totale; prodotto più venduto per numero di pezzi.
4. Grafici: `hist_importi.png`, istogramma degli importi; `mesi.png`, linea del fatturato per mese con `marker="o"`; `citta.png`, barre del fatturato per città.
5. Conclusione: città con la quota più alta e più bassa; mese migliore e peggiore; per il prodotto più venduto, quota dei pezzi e quota del fatturato.

**File di dati:** `ordini.csv`, da scaricare dal portale (cartella del codice di L08).

**Esempio di esecuzione**

```
Righe lette: 154, dopo la pulizia: 146
Fatturato: 5438.80 EUR, ordine medio: 37.25 EUR
Padova: 1639.10 EUR (30.1%)
Venezia: 1466.00 EUR (27.0%)
Verona: 1934.00 EUR (35.6%)
Vicenza: 399.70 EUR (7.3%)
Prodotto più venduto: quaderno, 124 pezzi
Verona vale 35.6% del fatturato, Vicenza solo 7.3%.
Il mese migliore è 2026-09 (1871.90 EUR), il peggiore 2026-11 (806.70 EUR).
Prodotto quaderno: 41.6% dei pezzi, ma 11.2% del fatturato.
```

**Provate anche**

- senza il filtro sulle quantità → `dopo la pulizia: 148`, `Fatturato: 5389.00 EUR`: l'ordine con quantità -2 toglie fatturato
- senza `drop_duplicates()` → `dopo la pulizia: 150`, `Fatturato: 5572.50 EUR`

---

### Challenge · Salute e scienza — L'effetto dell'integratore (`ch_salute.py`)

**Consegna**

1. `pazienti.csv` contiene i dati dello studio sull'integratore: `codice`, `sesso`, `eta`, `gruppo` (`trattamento` o `controllo`), `pressione_prima` e `pressione_dopo` in mmHg. Ci sono pazienti registrati due volte, pressioni mancanti (pazienti usciti dallo studio) e pressioni impossibili: tenete solo i valori tra 80 e 250 (`between(80, 250)`), sia prima sia dopo.
2. Aggiungete le colonne `differenza` (dopo − prima) e `migliorato` (`True` se la pressione è scesa di almeno 10 mmHg).
3. Statistiche: per gruppo la variazione media e la quota di migliorati (media della colonna booleana); il rischio relativo, cioè la quota di migliorati con il trattamento divisa per quella del controllo.
4. Grafici: `variazione.png`, boxplot della differenza per gruppo (`tick_labels=`); `prima_dopo.png`, dispersione della pressione prima e dopo, un colore per gruppo e legenda; `migliorati.png`, barre della quota di migliorati per gruppo.
5. Conclusione: variazione media nei due gruppi; rischio relativo; perché serve il gruppo di controllo.

**File di dati:** `pazienti.csv`, da scaricare dal portale (cartella del codice di L08).

**Esempio di esecuzione**

```
Righe lette: 123, dopo la pulizia: 115
controllo: variazione media -5.4 mmHg, migliorati 27.3%
trattamento: variazione media -10.2 mmHg, migliorati 51.7%
Rischio relativo di miglioramento: 1.89
La pressione cambia di -10.2 mmHg con l'integratore e di -5.4 senza.
I migliorati sono 1.89 volte quelli del controllo.
Anche il controllo migliora: per questo serve un confronto.
```

**Provate anche**

- senza il filtro sulle pressioni → `controllo: variazione media -31.4 mmHg`: due valori sbagliati ribaltano il confronto
- soglia di miglioramento a 5 mmHg → migliorati `50.9%` e `83.3%`, rischio relativo `1.64`
- solo pazienti da 60 anni in su (`df[df["eta"] >= 60]`) → `dopo la pulizia: 46`, rischio relativo `2.18`

---

### Challenge · Caso e probabilità — Il dado sospetto (`ch_probabilita.py`)

**Consegna**

1. `lanci.csv` è il registro di 180 lanci di due dadi, fatti a turno da Ada, Bruno, Carla e Dario. Colonne: `lancio`, `giocatore`, `dado1`, `dado2`. Ci sono lanci copiati due volte, valori mancanti e valori impossibili del secondo dado: tenete solo quelli tra 1 e 6 (`between(1, 6)`).
2. Aggiungete le colonne `somma` (dado1 + dado2) e `sei` (`True` se il secondo dado vale 6).
3. Statistiche: media della somma (teorica 7); quota di lanci con somma 7 (teorica 6/36); per giocatore, media della somma e quota di 6 sul secondo dado.
4. Grafici: `somme.png`, istogramma della somma con una barra per valore (`bins=np.arange(1.5, 13)`); `media_cumulata.png`, linea della media dopo ogni lancio (`df["somma"].cumsum()` diviso per `np.arange(1, len(df) + 1)`) con una linea orizzontale a 7 (`plt.axhline`); `sei.png`, barre della quota di 6 per giocatore con una linea a 1/6.
5. Conclusione: media finale a confronto con 7; il giocatore con più 6 sul secondo dado e la sua somma media; il confronto con 1/6.

**File di dati:** `lanci.csv`, da scaricare dal portale (cartella del codice di L08).

**Esempio di esecuzione**

```
Righe lette: 183, dopo la pulizia: 176
Media della somma: 7.20 (teorica 7.00)
Somma 7: 18.2% dei lanci (teorica 16.7%)
Ada: media 6.73, sei sul dado 2 6.7%
Bruno: media 7.24, sei sul dado 2 15.6%
Carla: media 6.95, sei sul dado 2 21.4%
Dario: media 7.86, sei sul dado 2 43.2%
Dopo 176 lanci la media cumulata è 7.20; il valore teorico è 7.
Dario fa 6 sul dado 2 nel 43.2% dei lanci e la sua somma media è 7.86.
Con un dado regolare sarebbe 16.7%: va controllato.
```

**Provate anche**

- senza il filtro sul secondo dado → `dopo la pulizia: 178`, `Media della somma: 7.18 (teorica 7.00)`
- togliete i lanci di Dario prima dei calcoli → `Media della somma: 6.98`; ora la conclusione indica Carla, con 21.4% su 42 lanci: uno scarto così piccolo può dipendere dal caso

---

## Domande di verifica

1. Perché `plt.savefig` va chiamato prima di `plt.show()`? Cosa contiene il PNG se si inverte l'ordine?
2. Quando si usa un istogramma e quando un grafico a barre? Fate un esempio per ciascuno con i dati di oggi.
3. In `mensa.py` le barre partono da 0. Come cambierebbe l'impressione se l'asse verticale partisse da 7 minuti?
4. In `studio.py` la correlazione è 0.67. Basta per dire che studiare di più fa prendere voti più alti?
5. Nel vostro progetto, quale statistica cambia di più se togliete il filtro sui valori impossibili? Perché?
