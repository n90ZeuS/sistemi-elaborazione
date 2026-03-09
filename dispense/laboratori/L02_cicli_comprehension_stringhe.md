# Laboratorio 2 — Cicli, comprehension e stringhe

**Prerequisiti:** Lezioni frontali F9 (*Cicli*) e T10 (*Comprehension e stringhe*).

**Obiettivo:** padroneggiare i cicli `for` e `while` con i pattern fondamentali (accumulatore, contatore, min/max), riscrivere cicli come comprehension, manipolare dati testuali con i metodi delle stringhe.

---

## Parte 1 — Cicli e statistiche base

### Esercizio guidato 1.1: media, minimo e massimo con `while`

Un caso comune in statistica: l'utente inserisce valori uno alla volta (non sappiamo quanti saranno in anticipo) e alla fine vogliamo le statistiche. Il ciclo `while` e lo strumento giusto.

Create un file `statistiche_input.py`:

```python
# statistiche_input.py — Media, minimo e massimo da input variabile

print("Inserisci valori numerici uno per riga.")
print("Scrivi 'fine' per terminare.\n")

conteggio: int = 0
somma: float = 0.0
minimo: float = float("inf")   # +infinito: qualsiasi valore sara minore
massimo: float = float("-inf") # -infinito: qualsiasi valore sara maggiore

while True:
    testo: str = input(f"Valore {conteggio + 1}: ")

    if testo.lower().strip() == "fine":
        break

    valore: float = float(testo)
    conteggio += 1
    somma += valore

    if valore < minimo:
        minimo = valore
    if valore > massimo:
        massimo = valore

if conteggio == 0:
    print("\nNessun valore inserito.")
else:
    media: float = somma / conteggio
    print(f"\n--- Statistiche su {conteggio} valori ---")
    print(f"Somma:   {somma:>10.2f}")
    print(f"Media:   {media:>10.2f}")
    print(f"Minimo:  {minimo:>10.2f}")
    print(f"Massimo: {massimo:>10.2f}")
```

Esecuzione di esempio:

```
Inserisci valori numerici uno per riga.
Scrivi 'fine' per terminare.

Valore 1: 23.5
Valore 2: 19.8
Valore 3: 31.2
Valore 4: 25.0
Valore 5: fine

--- Statistiche su 4 valori ---
Somma:      99.50
Media:      24.88
Minimo:     19.80
Massimo:    31.20
```

Osservate:
- `float("inf")` e `float("-inf")` sono valori speciali che garantiscono che il primo valore inserito diventi sia minimo che massimo. Questa e una tecnica standard.
- `.lower().strip()` rende robusto il confronto: l'utente puo scrivere "Fine", "FINE", " fine " e il programma funziona comunque.
- Il pattern accumulatore (`somma += valore`) e il pattern min/max lavorano insieme nello stesso ciclo.

### Esercizio guidato 1.2: tavola pitagorica con cicli annidati

Create un file `tavola_pitagorica.py`:

```python
# tavola_pitagorica.py — Tavola pitagorica con formattazione allineata

DIMENSIONE: int = 10

# Intestazione
print(f"{'':>4}", end="")
for j in range(1, DIMENSIONE + 1):
    print(f"{j:>4}", end="")
print()

# Linea separatrice
print(f"{'':>4}" + "-" * (DIMENSIONE * 4))

# Corpo della tavola
for i in range(1, DIMENSIONE + 1):
    print(f"{i:>3}|", end="")
    for j in range(1, DIMENSIONE + 1):
        prodotto: int = i * j
        print(f"{prodotto:>4}", end="")
    print()
```

Output:

```
       1   2   3   4   5   6   7   8   9  10
    ----------------------------------------
  1|   1   2   3   4   5   6   7   8   9  10
  2|   2   4   6   8  10  12  14  16  18  20
  3|   3   6   9  12  15  18  21  24  27  30
  ...
```

Osservate: il ciclo esterno (`i`) scorre le righe, quello interno (`j`) le colonne. Il formato `>4` allinea ogni numero a destra in 4 caratteri, producendo colonne ordinate. `end=""` impedisce l'a capo automatico di `print`, cosi i numeri si accumulano sulla stessa riga.

### Esercizio guidato 1.3: contare valori sopra e sotto la media

Create un file `sopra_sotto_media.py`:

```python
# sopra_sotto_media.py — Analisi distribuzione rispetto alla media

temperature: list[float] = [
    18.5, 22.3, 15.7, 28.1, 20.0,
    31.4, 17.2, 24.8, 19.5, 26.3,
    14.0, 23.7, 29.5, 16.8, 21.1,
]

# Primo passo: calcolare la media
n: int = len(temperature)
somma: float = 0.0
for temp in temperature:
    somma += temp
media: float = somma / n

# Secondo passo: contare sopra, sotto e uguali alla media
sopra: int = 0
sotto: int = 0
uguali: int = 0

for temp in temperature:
    if temp > media:
        sopra += 1
    elif temp < media:
        sotto += 1
    else:
        uguali += 1

# Report
print(f"--- Analisi di {n} temperature ---")
print(f"Media: {media:.2f}°C\n")
print(f"Sopra la media: {sopra:>3} ({sopra / n:.1%})")
print(f"Sotto la media: {sotto:>3} ({sotto / n:.1%})")
print(f"Uguali:         {uguali:>3} ({uguali / n:.1%})")

# Dettaglio: quali sono sopra la media?
print(f"\nValori sopra la media ({media:.2f}°C):")
for i, temp in enumerate(temperature, start=1):
    if temp > media:
        print(f"  Osservazione {i:>2}: {temp:.1f}°C  (+{temp - media:.1f})")
```

Osservate: servono **due passaggi** sui dati. Nel primo calcoliamo la media; nel secondo la usiamo per classificare. Non possiamo fare tutto in un solo ciclo perche la media dipende da *tutti* i valori. Questo pattern a due passaggi e molto comune nell'analisi dei dati.

---

## Parte 2 — Dalle comprehension ai cicli e ritorno

### Esercizio guidato 2.1: riscrivere cicli come comprehension

Le comprehension sono un modo conciso di creare liste (e altri contenitori) a partire da un iterabile, applicando opzionalmente una trasformazione e un filtro. Vediamo come tradurre i pattern visti nei cicli.

Create un file `comprehension.py`:

```python
# comprehension.py — Da cicli a comprehension

temperature: list[float] = [
    18.5, 22.3, 15.7, 28.1, 20.0,
    31.4, 17.2, 24.8, 19.5, 26.3,
]

# --- Pattern FILTRO ---
# Con ciclo:
calde_ciclo: list[float] = []
for temp in temperature:
    if temp > 25.0:
        calde_ciclo.append(temp)
print(f"Calde (ciclo):         {calde_ciclo}")

# Con comprehension:
calde_comp: list[float] = [temp for temp in temperature if temp > 25.0]
print(f"Calde (comprehension): {calde_comp}")

# --- Pattern TRASFORMAZIONE ---
# Con ciclo:
fahrenheit_ciclo: list[float] = []
for temp in temperature:
    fahrenheit_ciclo.append(temp * 9 / 5 + 32)
print(f"\nFahrenheit (ciclo):         {fahrenheit_ciclo}")

# Con comprehension:
fahrenheit_comp: list[float] = [temp * 9 / 5 + 32 for temp in temperature]
print(f"Fahrenheit (comprehension): {fahrenheit_comp}")

# --- Pattern FILTRO + TRASFORMAZIONE ---
# Solo le temperature sopra 25°C, convertite in Fahrenheit
# Con ciclo:
calde_f_ciclo: list[float] = []
for temp in temperature:
    if temp > 25.0:
        calde_f_ciclo.append(temp * 9 / 5 + 32)

# Con comprehension:
calde_f_comp: list[float] = [
    temp * 9 / 5 + 32
    for temp in temperature
    if temp > 25.0
]
print(f"\nCalde in °F (ciclo):         {calde_f_ciclo}")
print(f"Calde in °F (comprehension): {calde_f_comp}")

# --- Quando NON usare una comprehension ---
# Se la logica e complessa o ha effetti collaterali, il ciclo e piu chiaro.
# Regola pratica: se la comprehension non sta su 1-2 righe leggibili,
# usate un ciclo.
```

### Esercizio guidato 2.2: comprehension per stringhe e formattazione

```python
# comprehension_stringhe.py — Comprehension applicate a stringhe

nomi: list[str] = ["anna rossi", "marco bianchi", "luca verdi", "sara neri"]

# Capitalizzare ogni nome
nomi_formattati: list[str] = [nome.title() for nome in nomi]
print(f"Formattati: {nomi_formattati}")
# ['Anna Rossi', 'Marco Bianchi', 'Luca Verdi', 'Sara Neri']

# Estrarre solo i cognomi
cognomi: list[str] = [nome.split()[-1].title() for nome in nomi]
print(f"Cognomi: {cognomi}")
# ['Rossi', 'Bianchi', 'Verdi', 'Neri']

# Filtrare nomi che contengono la lettera 'a'
con_a: list[str] = [nome.title() for nome in nomi if "a" in nome]
print(f"Con 'a': {con_a}")

# Lunghezza di ogni nome
lunghezze: list[int] = [len(nome) for nome in nomi]
print(f"Lunghezze: {lunghezze}")
```

---

## Parte 3 — Stringhe come struttura dati

### Esercizio guidato 3.1: pulire dati testuali

I dati reali sono quasi sempre "sporchi": spazi in eccesso, maiuscole/minuscole miste, caratteri inattesi. I metodi delle stringhe sono lo strumento base per la pulizia.

Create un file `pulizia_dati.py`:

```python
# pulizia_dati.py — Pulizia dati testuali con metodi stringa

# Dati "sporchi" come arriverebbero da un file o un form
dati_grezzi: list[str] = [
    "  Mario ROSSI  ",
    "anna   bianchi",
    "LUCA  Verdi ",
    " Sara   NERI",
    "  marco   De Luca  ",
]

print("--- Dati grezzi ---")
for i, dato in enumerate(dati_grezzi):
    print(f"  {i}: {dato!r}")

# Passo 1: rimuovere spazi iniziali e finali
puliti: list[str] = [dato.strip() for dato in dati_grezzi]

# Passo 2: normalizzare gli spazi interni (sostituire spazi multipli con uno)
normalizzati: list[str] = []
for nome in puliti:
    # split() senza argomenti divide su qualsiasi whitespace e ignora i multipli
    parti: list[str] = nome.split()
    normalizzati.append(" ".join(parti))

# Passo 3: uniformare la capitalizzazione
formattati: list[str] = [nome.title() for nome in normalizzati]

print("\n--- Dati puliti ---")
for i, dato in enumerate(formattati):
    print(f"  {i}: {dato!r}")

# Passo 4: estrarre iniziali
print("\n--- Iniziali ---")
for nome in formattati:
    parti = nome.split()
    iniziali: str = "".join(p[0] for p in parti)
    print(f"  {nome:<25} -> {iniziali}")
```

Output atteso:

```
--- Dati grezzi ---
  0: '  Mario ROSSI  '
  1: 'anna   bianchi'
  2: 'LUCA  Verdi '
  3: ' Sara   NERI'
  4: '  marco   De Luca  '

--- Dati puliti ---
  0: 'Mario Rossi'
  1: 'Anna Bianchi'
  2: 'Luca Verdi'
  3: 'Sara Neri'
  4: 'Marco De Luca'

--- Iniziali ---
  Mario Rossi               -> MR
  Anna Bianchi              -> AB
  Luca Verdi                -> LV
  Sara Neri                 -> SN
  Marco De Luca             -> MDL
```

Osservate la pipeline di pulizia: `strip()` -> `split()` + `join()` -> `title()`. Questa sequenza risolve la maggior parte dei problemi di formattazione nei dati testuali. Il trucco `" ".join(nome.split())` e un idioma Python fondamentale: normalizza qualsiasi sequenza di spazi bianchi (spazi, tab, a capo) in un singolo spazio.

---

## Parte 4 — Esercizi autonomi

Svolgete i seguenti esercizi in autonomia. Usate type hints in tutte le variabili.

### Esercizio base: statistiche temperature settimanali

Create un file `temperature_settimana.py`.

**Traccia:** data la lista seguente che rappresenta le temperature massime giornaliere di una settimana:

```python
temperature: list[float] = [18.5, 22.3, 15.7, 28.1, 20.0, 31.4, 17.2]
giorni: list[str] = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]
```

Scrivete un programma che:
1. Calcola media, minimo e massimo delle temperature (senza usare `sum()`, `min()`, `max()` -- usate i pattern visti nei guidati).
2. Stampa una tabella formattata con giorno, temperatura e scostamento dalla media.
3. Indica qual e il giorno piu caldo e quale il piu freddo.
4. Usando una comprehension, crea una lista dei giorni con temperatura sopra la media e stampala.

Esempio parziale di output:

```
Giorno | Temp (°C) | Scostamento
-------|-----------|------------
Lun    |     18.5  |      -3.4
Mar    |     22.3  |      +0.4
...

Giorno piu caldo: Sab (31.4°C)
Giorno piu freddo: Mer (15.7°C)
Giorni sopra la media: Mar, Gio, Sab
```

### Esercizio intermedio: frequenza dei caratteri

Create un file `frequenza_caratteri.py`.

**Traccia:** scrivete un programma che:
1. Chiede all'utente di inserire una frase.
2. Conta la frequenza di ogni carattere (convertito in minuscolo), ignorando gli spazi.
3. Stampa i risultati ordinati per frequenza decrescente.
4. Calcola e stampa la percentuale di vocali e consonanti (considerare solo le lettere dell'alfabeto, ignorando numeri e punteggiatura; usate `char.isalpha()` per verificare se un carattere e una lettera).

Suggerimenti:
- Usate un dizionario `dict[str, int]` per contare le occorrenze.
- Per ordinare: `sorted(dizionario.items(), key=lambda coppia: coppia[1], reverse=True)`.
- Le vocali sono `"aeiou"`.

Esempio di output:

```
Frase: Il sole splende nel cielo azzurro

--- Frequenza caratteri ---
l : 5 (17.9%)
e : 4 (14.3%)
o : 3 (10.7%)
...

Vocali:     10 (35.7%)
Consonanti: 18 (64.3%)
```

### Esercizio avanzato: validatore codice fiscale (formato)

Create un file `validatore_cf.py`.

**Traccia:** scrivete un programma che verifica se una stringa rispetta il **formato** di un codice fiscale italiano. Non serve calcolare il codice fiscale corretto: verificate solo la struttura.

Un codice fiscale valido ha 16 caratteri con questo schema:
- Posizioni 1-3: tre lettere (cognome)
- Posizioni 4-6: tre lettere (nome)
- Posizioni 7-8: due cifre (anno)
- Posizione 9: una lettera (mese)
- Posizioni 10-11: due cifre (giorno)
- Posizione 12: una lettera (codice catastale, prima lettera)
- Posizioni 13-15: tre cifre (codice catastale, parte numerica)
- Posizione 16: una lettera (carattere di controllo)

Il programma deve:
1. Verificare che la lunghezza sia 16.
2. Verificare che ogni posizione contenga il tipo di carattere atteso (lettera o cifra), usando `char.isalpha()` e `char.isdigit()`.
3. Stampare un report dettagliato indicando se ogni sezione e valida.
4. Convertire l'input in maiuscolo prima della validazione.

Suggerimenti:
- Definite lo schema atteso come stringa di `L` (lettera) e `N` (numero): `"LLLLLLNNLNNLNNNL"`.
- Usate `zip()` o `enumerate()` per confrontare ogni carattere con lo schema.

---

## Parte 5 — Sfida

### Sfida: analisi e pulizia dati da stringa multi-riga

Create un file `sfida_analisi_dati.py`.

**Traccia:** avete ricevuto dati di vendite in un formato testuale disordinato. I dati sono in una stringa multi-riga, con campi separati da `";"`. I dati sono sporchi: spazi in eccesso, maiuscole miste, valori mancanti o non numerici.

```python
dati_grezzi: str = """
  prodotto ; quantita ; prezzo_unitario
  Mele     ; 50       ; 1.20
  BANANE   ;  30      ; 0.85
  Arance   ; 25       ; 1.50
  mele     ; 15       ;  1.20
  Pere     ;          ; 2.00
  BANANE   ; 20       ; abc
  kiwi     ; 40       ; 3.50
  Arance   ; 10       ; 1.50
  Mele     ; errore   ; 1.20
"""
```

Il programma deve:

1. **Parsare i dati:** dividere la stringa in righe, e ogni riga in campi separati da `";"`. Saltare la riga di intestazione e le righe vuote.

2. **Pulire ogni campo:** rimuovere spazi, uniformare i nomi dei prodotti in formato `title()`.

3. **Validare:** scartare le righe in cui quantita o prezzo non sono numerici, oppure la quantita e vuota. Stampare un avviso per ogni riga scartata, indicando il motivo.

4. **Aggregare per prodotto:** per ogni prodotto, calcolare:
   - Quantita totale venduta
   - Ricavo totale (quantita * prezzo per ogni riga valida)
   - Prezzo medio ponderato (ricavo totale / quantita totale)

5. **Stampare un report formattato:**

```
=== REPORT VENDITE ===

Righe elaborate: 6 su 8 (2 scartate)

Prodotto     | Quantita | Ricavo (EUR) | Prezzo medio
-------------|----------|--------------|-------------
Mele         |       65 |        78.00 |         1.20
Banane       |       30 |        25.50 |         0.85
Arance       |       35 |        52.50 |         1.50
Kiwi         |       40 |       140.00 |         3.50

TOTALE       |      170 |       296.00 |         1.74
```

Suggerimenti:
- Usate `stringa.split("\n")` per le righe e `riga.split(";")` per i campi.
- Per verificare se una stringa rappresenta un numero (anche decimale), una strategia semplice: provate a convertire con `float()` e controllate se `stringa.strip()` non e vuoto. Per ora, potete usare un approccio con `try/except` oppure verificare con `stringa.replace(".", "", 1).isdigit()`.
- Usate un dizionario `dict[str, dict[str, float]]` per aggregare per prodotto.

---

## Domande di verifica

Rispondete brevemente a ciascuna domanda.

1. Perche nell'esercizio guidato 1.1 inizializziamo `minimo` con `float("inf")` e `massimo` con `float("-inf")`? Cosa succederebbe se inizializzassimo entrambi a `0`?

2. Nel conteggio sopra/sotto media, perche servono due passaggi separati sui dati? Sarebbe possibile farlo in un solo passaggio?

3. Qual e la differenza tra `nome.split()` (senza argomenti) e `nome.split(" ")` (con argomento spazio)? Provate con la stringa `"  anna   rossi  "`.

4. Riscrivete questa comprehension come ciclo `for` equivalente:
   ```python
   pari: list[int] = [n ** 2 for n in range(20) if n % 2 == 0]
   ```

5. Quando e preferibile usare un ciclo `for` tradizionale invece di una comprehension?

6. Nel validatore del codice fiscale, perche e importante convertire l'input in maiuscolo prima della validazione?

---

## Osservazioni finali

In questo laboratorio avete lavorato con i tre strumenti che, combinati, risolvono la maggior parte dei problemi di manipolazione dati in Python:

- **I cicli** vi permettono di elaborare collezioni di dimensione arbitraria, applicando pattern ricorrenti (accumulatore, contatore, min/max, filtro). La scelta tra `for` e `while` dipende da una domanda semplice: sapete in anticipo quante iterazioni servono?

- **Le comprehension** condensano i pattern filtro e trasformazione in espressioni compatte. Non sono una scorciatoia: sono un modo diverso di pensare, piu dichiarativo. Pero hanno un limite: quando la logica diventa complessa, il ciclo esplicito e piu chiaro. La regola pratica e: se la comprehension non e immediatamente leggibile, tornate al ciclo.

- **I metodi delle stringhe** sono il coltellino svizzero della pulizia dati. La pipeline `strip()` -> `split()` -> `join()` -> `title()`/`lower()`/`upper()` risolve la stragrande maggioranza dei problemi di formattazione. In un corso di statistica, la pulizia dei dati e spesso la parte piu lunga e ingrata del lavoro: meglio padroneggiarla fin da subito.

La sfida finale vi ha fatto lavorare con un problema realistico: dati sporchi, formati misti, valori mancanti. Questo e il pane quotidiano di chi lavora con i dati. Le tecniche di oggi sono le stesse che userete con pandas e NumPy -- solo che li avrete funzioni di piu alto livello che fanno il lavoro pesante. Ma capire cosa succede sotto e la differenza tra usare uno strumento e padroneggiarlo.
