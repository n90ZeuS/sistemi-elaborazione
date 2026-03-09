# Laboratorio 1 — Ambiente Python, variabili, tipi e condizionali

**Prerequisiti:** Lezioni frontali F7 (*Primi passi in Python*) e F8 (*Operatori, I/O e strutture condizionali*).

**Obiettivo:** configurare l'ambiente di lavoro, scrivere programmi con variabili tipizzate, I/O formattato e strutture condizionali.

---

## Parte 1 — Setup dell'ambiente

### Esercizio guidato 1.1: verifica dell'installazione

Aprite un terminale (su macOS: *Terminale* o *iTerm*; su Windows: *PowerShell*) e verificate che Python sia installato:

```bash
python3 --version
```

Dovreste vedere qualcosa come `Python 3.12.x` (o superiore). Se il comando non viene riconosciuto, installate Python da [python.org](https://www.python.org/downloads/).

Verificate anche che VS Code sia installato:

```bash
code --version
```

Se VS Code non si apre da terminale, aprite VS Code, premete `Cmd+Shift+P` (macOS) o `Ctrl+Shift+P` (Windows/Linux), cercate "Shell Command: Install 'code' command in PATH" e confermate.

### Esercizio guidato 1.2: il REPL

Avviate il REPL (Read-Eval-Print Loop) di Python digitando:

```bash
python3
```

Il prompt cambia in `>>>`. Siete dentro l'interprete interattivo. Provate:

```python
>>> 2 + 3
5
>>> "ciao" * 3
'ciaociaociao'
>>> type(42)
<class 'int'>
>>> exit()
```

Il REPL e utile per esperimenti rapidi. Per programmi veri, useremo file `.py`.

### Esercizio guidato 1.3: il primo file Python

Create una cartella per il laboratorio e apritela in VS Code:

```bash
mkdir -p ~/lab_python/lab01
code ~/lab_python/lab01
```

Create un file `saluto.py` con il seguente contenuto:

```python
# saluto.py — Il mio primo programma Python
nome: str = "Mondo"
print(f"Ciao, {nome}!")
```

Eseguitelo dal terminale integrato di VS Code (`Ctrl+ò` o `Ctrl+`` per aprirlo):

```bash
python3 saluto.py
```

Output atteso:

```
Ciao, Mondo!
```

---

## Parte 2 — Variabili tipizzate e operatori

### Esercizio guidato 2.1: variabili, type hints e `type()`

Create un file `variabili.py`:

```python
# variabili.py — Esplorazione dei tipi fondamentali

# Dichiarazione con type hints
nome: str = "Maria"
eta: int = 21
altezza: float = 1.68
iscritta: bool = True

# Verifica dei tipi
print(f"nome     = {nome!r:>15}  tipo: {type(nome).__name__}")
print(f"eta      = {eta!r:>15}  tipo: {type(eta).__name__}")
print(f"altezza  = {altezza!r:>15}  tipo: {type(altezza).__name__}")
print(f"iscritta = {iscritta!r:>15}  tipo: {type(iscritta).__name__}")
```

Output atteso:

```
nome     =         'Maria'  tipo: str
eta      =              21  tipo: int
altezza  =            1.68  tipo: float
iscritta =            True  tipo: bool
```

Osservate: `!r` dentro la f-string mostra la rappresentazione "grezza" del valore (le stringhe appaiono con le virgolette). Il formato `>15` allinea a destra in 15 caratteri. I type hints (`str`, `int`, ecc.) non cambiano il comportamento del programma, ma documentano le vostre intenzioni.

### Esercizio guidato 2.2: operatori aritmetici

Create un file `operatori.py`:

```python
# operatori.py — Operatori aritmetici e conversioni

a: int = 17
b: int = 5

print("--- Operatori aritmetici ---")
print(f"{a} + {b}  = {a + b}")
print(f"{a} - {b}  = {a - b}")
print(f"{a} * {b}  = {a * b}")
print(f"{a} / {b}  = {a / b}")       # divisione vera -> float
print(f"{a} // {b} = {a // b}")      # divisione intera
print(f"{a} % {b}  = {a % b}")       # modulo (resto)
print(f"{a} ** {b} = {a ** b}")      # potenza

print("\n--- Conversioni ---")
prezzo_stringa: str = "49.99"
prezzo: float = float(prezzo_stringa)
iva: float = prezzo * 0.22
totale: float = prezzo + iva
print(f"Prezzo: {prezzo:.2f} EUR")
print(f"IVA 22%: {iva:.2f} EUR")
print(f"Totale: {totale:.2f} EUR")
```

Eseguite e verificate che l'output corrisponda ai calcoli manuali.

---

## Parte 3 — Input/Output formattato

### Esercizio guidato 3.1: calcolo interattivo con f-string

Create un file `area_cerchio.py`:

```python
# area_cerchio.py — Calcolo dell'area di un cerchio con input utente

import math

raggio_str: str = input("Inserisci il raggio del cerchio (in cm): ")
raggio: float = float(raggio_str)

area: float = math.pi * raggio ** 2
circonferenza: float = 2 * math.pi * raggio

print(f"\n--- Risultati ---")
print(f"Raggio:        {raggio:>10.2f} cm")
print(f"Area:          {area:>10.2f} cm²")
print(f"Circonferenza: {circonferenza:>10.2f} cm")
```

Esecuzione di esempio:

```
Inserisci il raggio del cerchio (in cm): 5

--- Risultati ---
Raggio:              5.00 cm
Area:             78.54 cm²
Circonferenza:       31.42 cm
```

Osservate il formato `>10.2f`: allinea a destra in un campo di 10 caratteri con 2 decimali. Questo rende l'output ordinato e leggibile.

---

## Parte 4 — Condizionali

### Esercizio guidato 4.1: classificatore fascia ISEE

L'ISEE (Indicatore della Situazione Economica Equivalente) determina l'accesso a servizi e agevolazioni. Scrivete un programma che classifica un reddito in fasce.

Create un file `classificatore_isee.py`:

```python
# classificatore_isee.py — Classificazione fascia ISEE

SOGLIA_1: float = 6_000.00
SOGLIA_2: float = 15_000.00
SOGLIA_3: float = 25_000.00
SOGLIA_4: float = 40_000.00

reddito_str: str = input("Inserisci il reddito ISEE (in euro): ")
reddito: float = float(reddito_str)

if reddito < 0:
    print("Errore: il reddito non puo essere negativo.")
elif reddito <= SOGLIA_1:
    fascia: str = "Fascia 1 — Esenzione totale"
    aliquota: float = 0.0
elif reddito <= SOGLIA_2:
    fascia = "Fascia 2 — Agevolazione alta"
    aliquota = 0.05
elif reddito <= SOGLIA_3:
    fascia = "Fascia 3 — Agevolazione media"
    aliquota = 0.10
elif reddito <= SOGLIA_4:
    fascia = "Fascia 4 — Agevolazione ridotta"
    aliquota = 0.15
else:
    fascia = "Fascia 5 — Nessuna agevolazione"
    aliquota = 0.22

if reddito >= 0:
    contributo: float = reddito * aliquota
    print(f"\n--- Risultato ---")
    print(f"Reddito ISEE:  {reddito:>12,.2f} EUR")
    print(f"Classificazione: {fascia}")
    print(f"Aliquota:      {aliquota:>12.0%}")
    print(f"Contributo:    {contributo:>12,.2f} EUR")
```

Esecuzione di esempio:

```
Inserisci il reddito ISEE (in euro): 18500

--- Risultato ---
Reddito ISEE:    18,500.00 EUR
Classificazione: Fascia 3 — Agevolazione media
Aliquota:              10%
Contributo:      1,850.00 EUR
```

Osservate:
- Le costanti (`SOGLIA_1`, ecc.) sono in `UPPER_SNAKE_CASE`, come richiede PEP 8.
- L'underscore nelle costanti numeriche (`6_000.00`) migliora la leggibilita senza cambiare il valore.
- Il formato `,.2f` aggiunge il separatore delle migliaia.
- Il formato `.0%` mostra il valore come percentuale senza decimali.
- La catena `if/elif/else` garantisce che ogni reddito cada in una sola fascia.

### Esercizio guidato 4.2: calcolatrice con scelta operazione

Create un file `calcolatrice.py`:

```python
# calcolatrice.py — Calcolatrice interattiva con validazione

print("=== CALCOLATRICE ===")
print("Operazioni: +  -  *  /  //  %  **")
print()

primo_str: str = input("Primo numero: ")
primo: float = float(primo_str)

operazione: str = input("Operazione: ")

secondo_str: str = input("Secondo numero: ")
secondo: float = float(secondo_str)

errore: bool = False
risultato: float = 0.0

if operazione == "+":
    risultato = primo + secondo
elif operazione == "-":
    risultato = primo - secondo
elif operazione == "*":
    risultato = primo * secondo
elif operazione == "/":
    if secondo == 0:
        print("Errore: divisione per zero!")
        errore = True
    else:
        risultato = primo / secondo
elif operazione == "//":
    if secondo == 0:
        print("Errore: divisione per zero!")
        errore = True
    else:
        risultato = primo // secondo
elif operazione == "%":
    if secondo == 0:
        print("Errore: divisione per zero!")
        errore = True
    else:
        risultato = primo % secondo
elif operazione == "**":
    risultato = primo ** secondo
else:
    print(f"Errore: operazione '{operazione}' non riconosciuta.")
    errore = True

if not errore:
    print(f"\n{primo} {operazione} {secondo} = {risultato:.4f}")
```

Provate diversi casi:
- `10 / 3` (verifica decimali)
- `10 / 0` (verifica gestione errore)
- `2 ** 10` (potenza)
- `17 % 5` (modulo)
- `10 @ 3` (operazione non valida)

---

## Parte 5 — Esercizi autonomi

Svolgete i seguenti esercizi in autonomia. Ogni esercizio ha una traccia con indicazioni, ma **non la soluzione**. Usate type hints in tutte le variabili.

### Esercizio base: conversione di temperatura

Create un file `temperatura.py`.

**Traccia:** scrivete un programma che chiede all'utente una temperatura in Celsius e la converte in Fahrenheit. La formula e: `F = C * 9/5 + 32`. Stampate il risultato con una cifra decimale, usando una f-string formattata.

Esempio di output atteso:

```
Temperatura in Celsius: 25
25.0°C = 77.0°F
```

### Esercizio intermedio: calcolo IMC con classificazione

Create un file `imc.py`.

**Traccia:** scrivete un programma che:
1. Chiede all'utente peso (in kg) e altezza (in metri).
2. Calcola l'IMC (Indice di Massa Corporea): `peso / altezza ** 2`.
3. Classifica il risultato secondo le fasce OMS:
   - IMC < 18.5: "Sottopeso"
   - 18.5 <= IMC < 25.0: "Normopeso"
   - 25.0 <= IMC < 30.0: "Sovrappeso"
   - IMC >= 30.0: "Obesita"
4. Valida l'input: peso e altezza devono essere positivi; l'altezza non puo superare 2.50 m.
5. Stampa il risultato formattato con 1 decimale.

Esempio di output atteso:

```
Peso (kg): 72
Altezza (m): 1.75

IMC: 23.5 — Normopeso
```

### Esercizio avanzato: simulazione bancomat

Create un file `bancomat.py`.

**Traccia:** scrivete un programma che simula un'operazione al bancomat:
1. Il saldo iniziale e 1000.00 EUR (costante nel codice, non chiesto all'utente).
2. Mostra il menu: `D` = deposito, `P` = prelievo, `S` = saldo.
3. Chiede all'utente l'operazione (accettate sia maiuscole che minuscole: usate `.upper()`).
4. Per deposito e prelievo, chiede l'importo.
5. Gestite i seguenti errori con messaggi appropriati:
   - Operazione non riconosciuta.
   - Importo negativo o zero.
   - Prelievo superiore al saldo disponibile.
6. Stampate il saldo aggiornato con 2 decimali e il separatore delle migliaia.

Esempio di output atteso:

```
=== BANCOMAT ===
Saldo attuale: 1,000.00 EUR

Operazione (D=Deposito, P=Prelievo, S=Saldo): P
Importo: 250

Prelievo di 250.00 EUR effettuato.
Nuovo saldo: 750.00 EUR
```

---

## Parte 6 — Sfida

### Sfida: convertitore e classificatore di temperatura

Create un file `sfida_temperatura.py`.

**Traccia:** scrivete un programma che:
1. Chiede all'utente una temperatura in gradi Celsius.
2. La converte in Fahrenheit (`F = C * 9/5 + 32`).
3. Classifica la percezione secondo questa tabella:

| Intervallo Celsius | Classificazione |
|---|---|
| C <= -10 | Gelido |
| -10 < C <= 5 | Freddo |
| 5 < C <= 18 | Mite |
| 18 < C <= 30 | Caldo |
| C > 30 | Torrido |

4. Stampa un report formattato come il seguente:

```
Temperatura in Celsius: 22

=== REPORT TEMPERATURA ===
Celsius:       22.0°C
Fahrenheit:    71.6°F
Percezione:    Caldo
```

5. Validazione: se la temperatura e inferiore a -273.15 (zero assoluto), stampate un messaggio di errore e non procedete con la conversione.

---

## Domande di verifica

Rispondete brevemente a ciascuna domanda.

1. Qual e la differenza tra eseguire codice nel REPL e da un file `.py`? In quali situazioni e preferibile usare l'uno o l'altro?

2. Cosa succede se scrivete `eta: int = int(input("Eta: "))` e l'utente inserisce `"venti"`? Quale tipo di errore si verifica?

3. Nel programma della calcolatrice, perche controlliamo `secondo == 0` solo per le operazioni `/`, `//` e `%`, ma non per `+`, `-`, `*`?

4. Perche usiamo `elif` invece di una sequenza di `if` indipendenti nel classificatore ISEE? Cosa cambierebbe se usassimo solo `if`?

5. Spiegate cosa fa il formato `{valore:>12,.2f}` in una f-string. Cosa significano `>`, `12`, `,` e `.2f`?

6. Perche le soglie ISEE sono definite come costanti (`SOGLIA_1`, ecc.) all'inizio del programma invece che come numeri direttamente nei confronti?

---

## Osservazioni finali

In questo laboratorio avete:

- **Configurato l'ambiente di lavoro:** terminale, Python, VS Code. Questi strumenti vi accompagneranno per tutto il corso e oltre. Investire tempo nel padroneggiarli non e un lusso, e una necessita.

- **Scritto programmi completi con type hints:** non solo frammenti, ma programmi che leggono input, calcolano e stampano risultati formattati. I type hints sono stati usati ovunque: non rallentano, non complicano, e rendono il codice piu chiaro.

- **Praticato le strutture condizionali su problemi reali:** classificare un reddito ISEE, gestire la divisione per zero, validare un input. Queste non sono astrazioni accademiche: ogni programma che scriverete nella vostra carriera dovra gestire dati inattesi e prendere decisioni.

Un consiglio: riscrivete da zero gli esercizi guidati senza guardare il codice. Se riuscite a ricostruirli dalla memoria e dalla comprensione, avete davvero imparato. Se dovete sbirciare, tornate indietro e rileggete la parte corrispondente.
