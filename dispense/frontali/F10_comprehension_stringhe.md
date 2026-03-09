# Lezione Frontale 10 — Comprehension e stringhe

## Introduzione

Nella lezione precedente abbiamo visto i cicli `for` e `while`, e abbiamo identificato una serie di pattern ricorrenti: accumulatore, contatore, filtro, trasformazione. Se li guardate con attenzione, noterete che molti di questi pattern condividono la stessa struttura: scorrere una sequenza, applicare una trasformazione o un filtro, e raccogliere i risultati in una nuova collezione.

Python offre una sintassi dedicata per esprimere questi pattern in modo compatto e dichiarativo: le **comprehension**. Invece di dire *come* costruire la lista passo per passo (approccio imperativo), con una comprehension descrivete *cosa* deve contenere la lista (approccio dichiarativo). Il risultato e un codice piu leggibile, piu breve e spesso piu efficiente.

Nella seconda parte della lezione ci occuperemo delle **stringhe** come struttura dati. Finora le abbiamo usate soprattutto per stampare messaggi, ma le stringhe sono sequenze a tutti gli effetti: si indicizzano, si affettano, si iterano. In statistica, lavorare con dati testuali e una necessita quotidiana: nomi di variabili, etichette di categorie, dati importati da file CSV che arrivano "sporchi" e vanno ripuliti. Conoscere i metodi delle stringhe vi risparmiera ore di lavoro.

---

## List comprehension

### Sintassi di base

Una list comprehension ha questa forma:

```python
[espressione for variabile in iterabile]
```

Dove `espressione` e il valore che finisce nella lista risultante, `variabile` assume a turno ogni valore dell'`iterabile`. Vediamo un esempio concreto. Supponiamo di voler calcolare il quadrato di ogni numero in una lista:

```python
numeri: list[int] = [1, 2, 3, 4, 5]
quadrati: list[int] = [n ** 2 for n in numeri]
print(quadrati)  # [1, 4, 9, 16, 25]
```

Confrontiamo con il ciclo `for` equivalente:

```python
numeri: list[int] = [1, 2, 3, 4, 5]
quadrati: list[int] = []
for n in numeri:
    quadrati.append(n ** 2)
print(quadrati)  # [1, 4, 9, 16, 25]
```

Il risultato e identico. La comprehension comprime quattro righe in una, rendendo immediatamente visibile l'intenzione: "voglio una lista dei quadrati di `numeri`". Il ciclo `for`, invece, richiede di leggere il corpo per capire cosa sta accadendo.

### Comprehension con filtro

Si puo aggiungere una clausola `if` per selezionare solo alcuni elementi:

```python
[espressione for variabile in iterabile if condizione]
```

Esempio: dai voti, estrarre solo quelli sufficienti e convertirli in trentesimi normalizzati:

```python
voti: list[int] = [28, 15, 30, 22, 12, 27, 18]
sufficienti: list[int] = [v for v in voti if v >= 18]
print(sufficienti)  # [28, 30, 22, 27, 18]
```

L'equivalente con ciclo `for`:

```python
voti: list[int] = [28, 15, 30, 22, 12, 27, 18]
sufficienti: list[int] = []
for v in voti:
    if v >= 18:
        sufficienti.append(v)
```

Anche qui, la comprehension esprime lo stesso concetto in modo piu diretto: "prendi i voti che sono >= 18".

### Trasformazione e filtro insieme

Si possono combinare trasformazione e filtro nella stessa comprehension:

```python
temperature_fahrenheit: list[float] = [32.0, 68.0, 95.0, 14.0, 77.0, 50.0]

# Converti in Celsius solo le temperature sopra lo zero Fahrenheit,
# arrotondando a una cifra decimale
temperature_celsius: list[float] = [
    round((f - 32) * 5 / 9, 1)
    for f in temperature_fahrenheit
    if f > 0
]
print(temperature_celsius)  # [0.0, 20.0, 35.0, -10.0, 25.0, 10.0]
```

### Perche le comprehension esistono

Le comprehension non sono solo "zucchero sintattico" (un modo piu breve di scrivere la stessa cosa). Esistono perche rendono esplicito un pattern che altrimenti sarebbe nascosto nel corpo di un ciclo. Quando un programmatore legge `[f(x) for x in lista if p(x)]`, riconosce immediatamente: "si sta costruendo una nuova lista applicando `f` agli elementi di `lista` che soddisfano `p`". Con un ciclo `for`, deve leggere tre o quattro righe per arrivare alla stessa conclusione.

In termini di prestazioni, le list comprehension sono generalmente piu veloci del ciclo equivalente, perche Python ottimizza internamente l'operazione di append.

---

## Dict comprehension

La stessa idea si applica ai dizionari. La sintassi e:

```python
{chiave: valore for variabile in iterabile}
```

Esempio: creare un dizionario che associa ogni nome alla sua lunghezza:

```python
nomi: list[str] = ["Anna", "Marco", "Luca", "Francesca"]
lunghezze: dict[str, int] = {nome: len(nome) for nome in nomi}
print(lunghezze)  # {'Anna': 4, 'Marco': 5, 'Luca': 4, 'Francesca': 9}
```

Si puo anche partire da coppie chiave-valore. Supponiamo di avere un dizionario di voti e di voler tenere solo quelli sufficienti:

```python
registro: dict[str, int] = {
    "Anna": 28, "Marco": 15, "Luca": 30, "Sara": 12, "Paolo": 22
}

promossi: dict[str, int] = {
    nome: voto for nome, voto in registro.items() if voto >= 18
}
print(promossi)  # {'Anna': 28, 'Luca': 30, 'Paolo': 22}
```

Un altro uso comune: invertire un dizionario (scambiare chiavi e valori):

```python
codici: dict[str, int] = {"Milano": 2, "Roma": 6, "Napoli": 81}
inverso: dict[int, str] = {v: k for k, v in codici.items()}
print(inverso)  # {2: 'Milano', 6: 'Roma', 81: 'Napoli'}
```

---

## Set comprehension

I set (insiemi) supportano la stessa sintassi, con le parentesi graffe ma senza la struttura chiave-valore:

```python
{espressione for variabile in iterabile}
```

Esempio: estrarre i valori unici delle prime lettere di una lista di nomi:

```python
nomi: list[str] = ["Anna", "Andrea", "Marco", "Maria", "Luca"]
iniziali: set[str] = {nome[0] for nome in nomi}
print(iniziali)  # {'A', 'M', 'L'}
```

Le set comprehension sono utili quando volete eliminare i duplicati dal risultato di una trasformazione.

---

## Generator expression

Le generator expression hanno la stessa sintassi delle list comprehension, ma con parentesi tonde:

```python
(espressione for variabile in iterabile)
```

La differenza fondamentale e che un generatore **non costruisce tutta la lista in memoria**. Produce i valori uno alla volta, su richiesta. Questo si chiama **lazy evaluation** (valutazione pigra): il lavoro viene fatto solo quando il risultato serve davvero.

```python
numeri: list[int] = [1, 2, 3, 4, 5]

# List comprehension: crea tutta la lista in memoria
quadrati_lista: list[int] = [n ** 2 for n in numeri]

# Generator expression: non crea nulla finché non lo chiedi
quadrati_gen = (n ** 2 for n in numeri)
print(type(quadrati_gen))  # <class 'generator'>
```

Il generatore si consuma iterandolo:

```python
for q in quadrati_gen:
    print(q)  # 1, 4, 9, 16, 25
```

### Quando usare i generatori

I generatori brillano quando lavorate con grandi quantita di dati e non avete bisogno di tutti i risultati contemporaneamente. Ad esempio, per sommare i quadrati di un milione di numeri:

```python
# MALE: crea una lista di 1 milione di elementi solo per sommarla
totale: int = sum([n ** 2 for n in range(1_000_000)])

# BENE: il generatore produce i valori uno alla volta, senza occupare memoria
totale: int = sum(n ** 2 for n in range(1_000_000))
```

Nota: quando una generator expression e l'unico argomento di una funzione, si possono omettere le parentesi esterne. Quindi `sum((n ** 2 for n in range(1_000_000)))` si semplifica in `sum(n ** 2 for n in range(1_000_000))`.

Funzioni come `sum()`, `min()`, `max()`, `any()`, `all()` accettano tutte un iterabile, e i generatori sono perfetti per questo scopo.

---

## Best practice sulle comprehension

### Quando usarle

Le comprehension sono ideali per:
- **Trasformazioni semplici**: `[f(x) for x in lista]`
- **Filtri semplici**: `[x for x in lista if condizione]`
- **Combinazione trasformazione + filtro**: `[f(x) for x in lista if condizione]`

### Quando evitarle

**Comprehension annidate complesse.** Tecnicamente Python permette comprehension dentro comprehension, ma il risultato e spesso illeggibile:

```python
# MALE: difficile da leggere
matrice: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
piatta: list[int] = [x for riga in matrice for x in riga]
# Funziona, ma chi legge deve fermarsi a pensare
```

Meglio un ciclo esplicito o una funzione dedicata quando la logica diventa complessa.

**Mai per side effect.** Una comprehension deve *produrre un valore*, non *fare qualcosa*. Questo e un anti-pattern grave:

```python
# MALE: comprehension usata per side effect
nomi: list[str] = ["Anna", "Marco", "Luca"]
[print(nome) for nome in nomi]  # crea una lista di None inutile!
```

Si sta costruendo una lista di valori `None` (il valore di ritorno di `print()`) solo per il side effect della stampa. Usate un ciclo `for` normale:

```python
# BENE: ciclo for per side effect
nomi: list[str] = ["Anna", "Marco", "Luca"]
for nome in nomi:
    print(nome)
```

La regola e: **se il risultato della comprehension non vi interessa, non usate una comprehension**.

---

## Stringhe come struttura dati

### Sequenze immutabili di caratteri

Le stringhe in Python sono **sequenze immutabili di caratteri**. "Sequenza" significa che supportano indicizzazione e slicing, esattamente come le liste. "Immutabile" significa che, una volta creata, una stringa non puo essere modificata: ogni operazione che sembra "modificare" una stringa in realta ne crea una nuova.

```python
testo: str = "Statistica"

# Indicizzazione
print(testo[0])    # 'S'
print(testo[-1])   # 'a'

# Slicing
print(testo[0:4])  # 'Stat'
print(testo[4:])   # 'istica'
print(testo[::-1]) # 'acitsitats' (stringa al contrario)

# Iterazione
for carattere in testo:
    print(carattere, end=" ")  # S t a t i s t i c a

# Lunghezza
print(len(testo))  # 10

# Appartenenza
print("ist" in testo)  # True
```

L'immutabilita significa che questo e un errore:

```python
testo: str = "Statistica"
testo[0] = "s"  # TypeError: 'str' object does not support item assignment
```

Per "modificare" una stringa, dovete crearne una nuova:

```python
testo: str = "Statistica"
testo_minuscolo: str = "s" + testo[1:]
print(testo_minuscolo)  # "statistica"
```

---

## Metodi fondamentali delle stringhe

Ogni metodo delle stringhe **restituisce una nuova stringa** (o un altro valore), senza modificare l'originale. Questo e una conseguenza dell'immutabilita.

### `strip()`, `lstrip()`, `rstrip()` — rimozione spazi

```python
dato: str = "  42.5  \n"
pulito: str = dato.strip()
print(repr(pulito))  # '42.5'

# strip() rimuove spazi, tab, newline da entrambi i lati
# lstrip() solo a sinistra, rstrip() solo a destra
```

Nella pulizia di dati importati da file, `strip()` e quasi sempre il primo metodo da chiamare.

### `split()` e `join()` — dividere e ricomporre

`split()` divide una stringa in una lista di sottostringhe, usando un separatore:

```python
riga: str = "Anna,28,Economia"
campi: list[str] = riga.split(",")
print(campi)  # ['Anna', '28', 'Economia']

# Senza argomento, split() divide su qualsiasi spazio bianco
frase: str = "la  statistica   e   bella"
parole: list[str] = frase.split()
print(parole)  # ['la', 'statistica', 'e', 'bella']
```

`join()` fa l'operazione inversa — unisce una lista di stringhe con un separatore:

```python
parole: list[str] = ["media", "varianza", "deviazione"]
risultato: str = ", ".join(parole)
print(risultato)  # 'media, varianza, deviazione'

# Il separatore puo essere qualsiasi stringa
percorso: str = "/".join(["home", "utente", "dati"])
print(percorso)  # 'home/utente/dati'
```

### `replace()` — sostituzione

```python
testo: str = "valore: N/A"
pulito: str = testo.replace("N/A", "0")
print(pulito)  # 'valore: 0'

# Sostituisce TUTTE le occorrenze
dati: str = "1,2,,4,,6"
dati_puliti: str = dati.replace(",,", ",0,")
print(dati_puliti)  # '1,2,0,4,0,6'
```

### `find()` e `index()` — ricerca

```python
testo: str = "La media campionaria"

# find() restituisce la posizione, o -1 se non trovato
pos: int = testo.find("media")
print(pos)  # 3

pos_assente: int = testo.find("varianza")
print(pos_assente)  # -1

# index() fa lo stesso, ma lancia ValueError se non trovato
# pos: int = testo.index("varianza")  # ValueError!
```

### `startswith()` e `endswith()` — prefisso e suffisso

```python
nome_file: str = "dati_2024.csv"

print(nome_file.startswith("dati"))  # True
print(nome_file.endswith(".csv"))    # True
print(nome_file.endswith(".xlsx"))   # False
```

Utile per filtrare nomi di file, controllare formati, validare input.

### `upper()`, `lower()`, `title()`, `capitalize()` — maiuscole e minuscole

```python
testo: str = "statistica Descrittiva"

print(testo.upper())       # 'STATISTICA DESCRITTIVA'
print(testo.lower())       # 'statistica descrittiva'
print(testo.title())       # 'Statistica Descrittiva'
print(testo.capitalize())  # 'Statistica descrittiva'
```

La conversione a `lower()` e fondamentale per confronti case-insensitive:

```python
risposta: str = "Si"
if risposta.lower() == "si":
    print("Confermato")
```

### `isdigit()`, `isalpha()`, `isalnum()` — test sul contenuto

```python
print("42".isdigit())      # True
print("3.14".isdigit())    # False (il punto non e una cifra)
print("abc".isalpha())     # True
print("abc123".isalnum())  # True
print("abc 123".isalnum()) # False (lo spazio non e alfanumerico)
```

Questi metodi sono utili per validare l'input dell'utente prima di convertirlo.

---

## Pattern di pulizia dati: split + strip

Un pattern estremamente comune in statistica e il parsing manuale di righe CSV. I dati arrivano spesso con spazi extra, newline a fine riga, campi vuoti:

```python
riga_grezza: str = "  Anna , 28 , Economia , 105  \n"

# Step 1: strip della riga intera
riga: str = riga_grezza.strip()

# Step 2: split sul separatore
campi_grezzi: list[str] = riga.split(",")
# ['  Anna ', ' 28 ', ' Economia ', ' 105  ']

# Step 3: strip di ogni campo — ecco la comprehension!
campi: list[str] = [campo.strip() for campo in campi_grezzi]
# ['Anna', '28', 'Economia', '105']
```

In una riga sola:

```python
campi: list[str] = [c.strip() for c in riga_grezza.strip().split(",")]
```

Questo pattern combina tutto cio che abbiamo visto: metodi delle stringhe e list comprehension. Vedrete una variante di questo codice ogni volta che lavorerete con dati testuali.

Un esempio piu completo — leggere un "mini-CSV" e convertirlo in una lista di dizionari:

```python
righe: list[str] = [
    "nome, eta, voto",
    "Anna, 22, 28",
    "Marco, 21, 25",
    "Sara, 23, 30",
]

intestazione: list[str] = [c.strip() for c in righe[0].split(",")]
dati: list[dict[str, str]] = []

for riga in righe[1:]:
    valori: list[str] = [c.strip() for c in riga.split(",")]
    record: dict[str, str] = {
        intestazione[i]: valori[i] for i in range(len(intestazione))
    }
    dati.append(record)

print(dati)
# [{'nome': 'Anna', 'eta': '22', 'voto': '28'},
#  {'nome': 'Marco', 'eta': '21', 'voto': '25'},
#  {'nome': 'Sara', 'eta': '23', 'voto': '30'}]
```

---

## f-string avanzate

Abbiamo gia usato le f-string per inserire variabili nelle stringhe. Ma le f-string supportano anche la **formattazione avanzata** tramite un mini-linguaggio dopo i due punti `:`.

### Formattazione di numeri

```python
pi: float = 3.141592653589793

# Cifre decimali
print(f"Pi greco: {pi:.2f}")    # Pi greco: 3.14
print(f"Pi greco: {pi:.4f}")    # Pi greco: 3.1416

# Notazione scientifica
grande: float = 6.022e23
print(f"Avogadro: {grande:.2e}")  # Avogadro: 6.02e+23

# Percentuale
tasso: float = 0.0325
print(f"Tasso: {tasso:.1%}")  # Tasso: 3.2%

# Separatore delle migliaia
popolazione: int = 59_641_488
print(f"Popolazione: {popolazione:,}")  # Popolazione: 59,641,488
# Con separatore italiano (punto):
print(f"Popolazione: {popolazione:_}".replace("_", "."))
```

### Allineamento e larghezza

```python
# Allineamento a destra (default per numeri)
for i in range(1, 13):
    print(f"Mese {i:2d}: {'*' * i}")
# Mese  1: *
# Mese  2: **
# ...
# Mese 12: ************

# Allineamento esplicito
nome: str = "Anna"
print(f"|{nome:<15}|")  # |Anna           |  (sinistra)
print(f"|{nome:>15}|")  # |           Anna|  (destra)
print(f"|{nome:^15}|")  # |     Anna      |  (centro)

# Tabella formattata
studenti: list[tuple[str, int]] = [
    ("Anna", 28), ("Marco", 30), ("Francesca", 25)
]
print(f"{'Nome':<15} {'Voto':>5}")
print("-" * 21)
for nome, voto in studenti:
    print(f"{nome:<15} {voto:>5d}")
# Nome              Voto
# ---------------------
# Anna                28
# Marco               30
# Francesca           25
```

Le f-string formattate sono indispensabili per produrre output leggibili: tabelle di statistiche, report, log.

---

## Cenni su espressioni regolari

Le espressioni regolari (regex) sono un linguaggio per descrivere **pattern** nelle stringhe. Python le supporta tramite il modulo `re` della libreria standard. Non le tratteremo in dettaglio, ma e utile sapere che esistono e vedere un paio di esempi.

```python
import re

testo: str = "Il reddito medio e 32.500 euro, con deviazione standard 8.200 euro."

# Trovare tutti i numeri (anche con punto separatore)
numeri: list[str] = re.findall(r"\d+\.?\d*", testo)
print(numeri)  # ['32.500', '8.200']

# Verificare se una stringa e un codice fiscale valido (pattern semplificato)
cf: str = "RSSMRA85M01H501Z"
if re.match(r"^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$", cf):
    print("Formato codice fiscale valido")
```

I simboli principali:
- `\d` = una cifra, `\w` = un carattere alfanumerico, `\s` = uno spazio
- `+` = una o piu ripetizioni, `*` = zero o piu, `?` = zero o una
- `^` = inizio stringa, `$` = fine stringa
- `[A-Z]` = un carattere nell'intervallo A-Z

Le regex sono potenti ma complesse. Per la pulizia di dati semplice, i metodi `split()`, `strip()`, `replace()` sono sufficienti. Le regex diventano necessarie quando i pattern sono variabili o complessi (estrarre date in formati diversi, validare email, analizzare log).

Il consiglio e: **sapete che esistono**, e quando i metodi stringa non bastano, cercate "python regex" e troverete la soluzione.

---

## Applicazioni statistiche: pulizia di dati testuali

Nella pratica statistica, i dati raramente arrivano puliti. Ecco alcuni scenari comuni e come affrontarli con gli strumenti di questa lezione.

### Normalizzazione di categorie

```python
risposte: list[str] = [
    "si", "Si", "SI", " si ", "no", "No", "  NO", "forse"
]

# Normalizzare: strip + lower
normalizzate: list[str] = [r.strip().lower() for r in risposte]
print(normalizzate)
# ['si', 'si', 'si', 'si', 'no', 'no', 'no', 'forse']

# Contare le frequenze con una dict comprehension
valori_unici: set[str] = set(normalizzate)
frequenze: dict[str, int] = {
    valore: normalizzate.count(valore) for valore in valori_unici
}
print(frequenze)  # {'si': 4, 'no': 3, 'forse': 1}
```

### Estrazione di valori numerici da testo

```python
celle: list[str] = ["42", "  38.5 ", "N/A", "27", "", "31.2", "-"]

valori_validi: list[float] = []
for cella in celle:
    pulita: str = cella.strip()
    # Proviamo a verificare se e un numero
    try:
        valori_validi.append(float(pulita))
    except ValueError:
        pass  # saltiamo i valori non numerici

print(valori_validi)  # [42.0, 38.5, 27.0, 31.2]
```

### Costruire un report formattato

```python
def report_statistiche(nome_variabile: str, valori: list[float]) -> str:
    """Genera un report testuale per una variabile numerica."""
    n: int = len(valori)
    media: float = sum(valori) / n
    minimo: float = min(valori)
    massimo: float = max(valori)

    righe: list[str] = [
        f"{'=' * 40}",
        f"{'Statistiche descrittive':^40}",
        f"{'=' * 40}",
        f"{'Variabile:':<20} {nome_variabile}",
        f"{'N. osservazioni:':<20} {n}",
        f"{'Media:':<20} {media:>10.2f}",
        f"{'Minimo:':<20} {minimo:>10.2f}",
        f"{'Massimo:':<20} {massimo:>10.2f}",
        f"{'=' * 40}",
    ]
    return "\n".join(righe)

dati: list[float] = [23.5, 21.0, 25.3, 19.8, 22.1, 24.7, 20.5]
print(report_statistiche("Temperatura", dati))
```

Output:

```
========================================
         Statistiche descrittive
========================================
Variabile:           Temperatura
N. osservazioni:     7
Media:                    22.41
Minimo:                   19.80
Massimo:                  25.30
========================================
```

Questo esempio combina `join()`, f-string con allineamento, e una funzione che restituisce una stringa — tutti strumenti di questa lezione.

---

## Domande di verifica

1. **Qual e la differenza tra una list comprehension e un ciclo `for` con `append()`?** Il risultato e diverso o solo la forma?

2. **Scrivete la list comprehension equivalente al seguente codice:**
   ```python
   risultato: list[str] = []
   for nome in nomi:
       if len(nome) > 4:
           risultato.append(nome.upper())
   ```

3. **Qual e la differenza tra una list comprehension `[...]` e una generator expression `(...)`?** Quando conviene usare l'una o l'altra?

4. **Perche `[print(x) for x in lista]` e considerato un anti-pattern?** Cosa c'e di sbagliato?

5. **Cosa significa che le stringhe sono "immutabili"?** Cosa succede quando chiamate `testo.upper()`?

6. **Spiegate la differenza tra `find()` e `index()` applicati a una stringa.**

7. **Descrivete il pattern "split + strip" per la pulizia di dati testuali.** Perche e utile?

8. **Cosa fa l'espressione `f"{valore:.2%}"`?** Che output produce se `valore` e `0.1573`?

---

## Esercizi

### Base

1. Data la lista `numeri: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, scrivete una list comprehension che produca la lista dei numeri pari moltiplicati per 3. Risultato atteso: `[6, 12, 18, 24, 30]`.

2. Data la lista `parole: list[str] = ["casa", "albero", "sole", "mare", "acqua"]`, create una dict comprehension che associ ogni parola al numero di vocali che contiene. (Suggerimento: usate `sum()` con una generator expression per contare le vocali.)

3. Data la stringa `riga: str = "  Mario Rossi , 25 , Roma  "`, usate `strip()` e `split(",")` per estrarre i tre campi puliti in una lista.

4. Scrivete un programma che chiede all'utente un nome di file e stampa `True` se il nome finisce con `.csv` o `.txt`, `False` altrimenti.

### Intermedio

5. Data una lista di stringhe che rappresentano righe CSV:
   ```python
   righe: list[str] = [
       "prodotto, prezzo, quantita",
       " Mele, 2.50, 100 ",
       "Banane , 1.80 , 150",
       " Arance,  3.20, 80 ",
   ]
   ```
   Scrivete un programma che le converte in una lista di dizionari con chiavi dall'intestazione e valori puliti (stringhe senza spazi). Poi calcolate il ricavo totale (prezzo * quantita) per ogni prodotto.

6. Scrivete una funzione `conta_frequenze(testo: str) -> dict[str, int]` che, dato un testo, restituisce un dizionario con la frequenza di ogni parola (convertita in minuscolo). Usate `split()`, `lower()` e una dict comprehension o un ciclo.

7. Scrivete una funzione `formatta_tabella(intestazioni: list[str], righe: list[list[str]]) -> str` che produce una tabella formattata con colonne allineate. La larghezza di ogni colonna deve adattarsi al contenuto piu lungo.

### Avanzato

8. Scrivete una funzione `pulisci_dataset(righe: list[str], separatore: str = ",") -> list[dict[str, float]]` che:
   - prende una lista di righe CSV (la prima e l'intestazione);
   - pulisce ogni campo con strip;
   - converte i valori numerici in `float`, sostituendo i valori non convertibili con `0.0`;
   - restituisce una lista di dizionari.

   Testatela con dati che contengono spazi, valori mancanti e valori non numerici.

9. Usando le espressioni regolari (`re.findall()`), scrivete una funzione `estrai_numeri(testo: str) -> list[float]` che estrae tutti i numeri (interi e decimali, anche negativi) da una stringa di testo e li restituisce come lista di float.

   ```python
   testo: str = "La temperatura e variata da -3.5 a 12.8 gradi in 24 ore."
   print(estrai_numeri(testo))  # [-3.5, 12.8, 24.0]
   ```

---

## Osservazioni finali

In questa lezione abbiamo introdotto due strumenti che lavorano in sinergia. Le **comprehension** forniscono un modo dichiarativo per trasformare e filtrare dati: sono piu concise di un ciclo `for` equivalente e rendono immediatamente leggibile l'intenzione del codice. Le **stringhe**, con i loro metodi, sono lo strumento fondamentale per manipolare dati testuali — e nel lavoro statistico, una quantita sorprendente di tempo viene spesa a pulire, formattare e interpretare testo.

Tre punti da ricordare:

1. **Comprehension semplici, cicli per il resto.** Se una comprehension diventa difficile da leggere, tornate al ciclo `for`. Non c'e nulla di sbagliato in un ciclo esplicito — la leggibilita e piu importante della concisione.

2. **Le stringhe sono immutabili.** Ogni metodo (`strip()`, `replace()`, `upper()`, ...) restituisce una **nuova** stringa. L'originale non viene mai modificata. Questo e un principio che ritroverete in molte strutture dati di Python e delle librerie scientifiche.

3. **Il pattern split + strip e il vostro coltellino svizzero.** Quando lavorerete con dati reali — CSV mal formattati, log di sistema, output di strumenti esterni — la combinazione di `split()`, `strip()` e list comprehension risolvera la maggior parte dei problemi di parsing. Per i casi piu complessi, le espressioni regolari vi aspettano.

Nella prossima lezione introdurremo le **funzioni** in modo piu approfondito: come definirle, come organizzare il codice, e il concetto di scope delle variabili.
