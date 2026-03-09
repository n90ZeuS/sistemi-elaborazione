# Python Cheatsheet — Sistemi di Elaborazione

> **Come usare questo documento:** ogni sezione corrisponde a una lezione frontale. Dopo la lezione *N*, avete a disposizione tutte le sezioni dalla 7 alla *N*. All'esame potete consultare l'intero cheatsheet (versione finale).

---

## Indice progressivo

| Dopo la lezione | Sezioni disponibili |
|---|---|
| F07 | 1 |
| F08 | 1–2 |
| F09 | 1–3 |
| F10 | 1–4 |
| F11 | 1–5 |
| F12 | 1–6 |
| F13 | 1–7 |
| F14 | 1–8 |
| F15 | 1–9 |
| F16 | 1–10 |
| F17 | 1–11 (versione completa) |

---

## 1. Variabili, tipi e conversioni (F07)

### Tipi fondamentali e type hints

```python
eta: int = 25
altezza: float = 1.75
nome: str = "Anna"
iscritto: bool = True
risultato: None = None
```

### Verificare il tipo

```python
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("ciao"))     # <class 'str'>
print(type(True))       # <class 'bool'>
print(type(None))       # <class 'NoneType'>
```

### Conversioni di tipo (casting)

```python
eta: int = int("25")
altezza: float = float("1.75")
testo: str = str(42)
y: int = int(3.99)       # 3 (tronca, non arrotonda!)
print(bool(0))            # False
print(bool(""))           # False
print(bool(42))           # True
print(bool("ciao"))       # True
```

### Assegnamento e operatori composti

```python
contatore: int = 0
contatore += 1    # contatore = contatore + 1
totale -= 10      # totale = totale - 10
prodotto *= 2     # prodotto = prodotto * 2
```

### Unpacking e scambio

```python
a, b, c = 1, 2, 3
a, b = b, a          # scambio di variabili
```

### Notazioni numeriche

```python
popolazione: int = 59_000_000       # underscore come separatore
grande: int = 2 ** 100              # precisione arbitraria
notazione: float = 6.022e23         # notazione scientifica
```

### Metodi su oggetti

```python
print((42).bit_length())     # 6
print("ciao".upper())        # "CIAO"
```

---

## 2. Operatori, I/O e condizionali (F08)

### Operatori aritmetici

```python
a + b       # somma
a - b       # sottrazione
a * b       # moltiplicazione
a / b       # divisione (sempre float)
a // b      # divisione intera
a % b       # modulo (resto)
a ** b      # potenza
```

### Operatori di confronto

```python
a == b      # uguale
a != b      # diverso
a < b       # minore
a <= b      # minore o uguale
a > b       # maggiore
a >= b      # maggiore o uguale
```

### Operatori logici

```python
a and b     # vero se entrambi veri
a or b      # vero se almeno uno vero
not a       # negazione
```

### Input e output

```python
nome: str = input("Come ti chiami? ")
eta: int = int(input("Quanti anni hai? "))
```

### f-string

```python
print(f"Ciao, {nome}! Hai {eta} anni.")
print(f"Pi greco: {3.14159:.2f}")      # 3.14
```

### Condizionali

```python
if voto >= 28:
    print("Ottimo")
elif voto >= 18:
    print("Sufficiente")
else:
    print("Insufficiente")
```

### Operatore ternario

```python
esito: str = "promosso" if voto >= 18 else "bocciato"
```

### Confronti concatenati

```python
if 18 <= voto <= 30:
    print("Voto valido")
```

---

## 3. Cicli (F09)

### Ciclo `for`

```python
voti: list[int] = [28, 30, 25, 27, 22]
for voto in voti:
    print(f"Voto: {voto}")
```

### `range()`

```python
for i in range(5):            # 0, 1, 2, 3, 4
for i in range(1, 6):         # 1, 2, 3, 4, 5
for i in range(0, 10, 2):     # 0, 2, 4, 6, 8
for i in range(10, 0, -1):    # 10, 9, ..., 1
```

### `enumerate()` — indice e valore

```python
nomi: list[str] = ["Anna", "Marco", "Luca"]
for i, nome in enumerate(nomi):
    print(f"{i}: {nome}")

for i, nome in enumerate(nomi, start=1):
    print(f"{i}. {nome}")
```

### `zip()` — iterare in parallelo

```python
nomi: list[str] = ["Anna", "Marco", "Luca"]
voti: list[int] = [28, 30, 25]
for nome, voto in zip(nomi, voti):
    print(f"{nome}: {voto}")
```

### Ciclo `while`

```python
risposta: str = ""
while risposta != "esci":
    risposta = input("Comando: ")
```

### `break` e `continue`

```python
# break: esce dal ciclo
for dato in dati:
    if dato == obiettivo:
        print(f"Trovato: {dato}")
        break

# continue: salta al prossimo ciclo
for valore in valori:
    if valore < 0:
        continue
    print(f"Elaboro: {valore}")
```

### Pattern `while True + break`

```python
while True:
    risposta: str = input("Numero (0 per uscire): ")
    numero: int = int(risposta)
    if numero == 0:
        break
    print(f"Il quadrato è {numero ** 2}")
```

### Pattern accumulatore

```python
somma: int = 0
for voto in voti:
    somma += voto
media: float = somma / len(voti)
```

### Pattern contatore

```python
sufficienze: int = 0
for voto in voti:
    if voto >= 18:
        sufficienze += 1
```

### Pattern ricerca

```python
def contiene(lista: list[int], obiettivo: int) -> bool:
    for elemento in lista:
        if elemento == obiettivo:
            return True
    return False
```

### Pattern filtro

```python
sufficienti: list[int] = []
for voto in voti:
    if voto >= 18:
        sufficienti.append(voto)
```

### Pattern min/max

```python
massimo: float = valori[0]
for valore in valori[1:]:
    if valore > massimo:
        massimo = valore
```

### Statistiche descrittive (esempio completo)

```python
def statistiche(valori: list[float]) -> dict[str, float]:
    n: int = len(valori)
    somma: float = sum(v for v in valori)
    media: float = somma / n
    somma_scarti: float = sum((v - media) ** 2 for v in valori)
    varianza: float = somma_scarti / n
    minimo: float = min(valori)
    massimo: float = max(valori)
    return {"n": n, "media": media, "varianza": varianza,
            "minimo": minimo, "massimo": massimo}
```

---

## 4. Comprehension, stringhe e formattazione (F10)

### List comprehension

```python
# Sintassi base
quadrati: list[int] = [n ** 2 for n in numeri]

# Con filtro
sufficienti: list[int] = [v for v in voti if v >= 18]

# Trasformazione + filtro
celsius: list[float] = [round((f - 32) * 5 / 9, 1)
                        for f in fahrenheit if f > 0]
```

### Dict comprehension

```python
lunghezze: dict[str, int] = {nome: len(nome) for nome in nomi}

# Filtrare un dizionario
promossi: dict[str, int] = {n: v for n, v in registro.items() if v >= 18}

# Invertire un dizionario
inverso: dict[int, str] = {v: k for k, v in codici.items()}
```

### Set comprehension

```python
iniziali: set[str] = {nome[0] for nome in nomi}
```

### Generator expression (memoria efficiente)

```python
totale: int = sum(n ** 2 for n in range(1_000_000))
```

### Stringhe — indicizzazione e slicing

```python
testo: str = "Statistica"
testo[0]       # 'S'
testo[-1]      # 'a'
testo[0:4]     # 'Stat'
testo[4:]      # 'istica'
testo[::-1]    # 'acitsitats' (invertita)
len(testo)     # 10
"ist" in testo # True
```

### Metodi stringa principali

```python
# Pulizia
" 42.5 \n".strip()          # '42.5'

# Divisione e unione
"Anna,28,Eco".split(",")    # ['Anna', '28', 'Eco']
", ".join(["a", "b", "c"])  # 'a, b, c'

# Sostituzione
"N/A".replace("N/A", "0")   # '0'

# Ricerca
testo.find("media")          # posizione o -1
testo.startswith("dati")     # True/False
testo.endswith(".csv")       # True/False

# Maiuscole/minuscole
testo.upper()                # tutto maiuscolo
testo.lower()                # tutto minuscolo
testo.title()                # Prima Lettera Maiuscola
testo.capitalize()           # Solo prima maiuscola

# Test contenuto
"42".isdigit()               # True
"abc".isalpha()              # True
"abc123".isalnum()           # True
```

### Pattern pulizia dati stringa

```python
campi: list[str] = [c.strip() for c in riga.strip().split(",")]
```

### f-string — formattazione avanzata

```python
# Decimali
f"{pi:.2f}"                  # '3.14'
f"{pi:.4f}"                  # '3.1416'

# Notazione scientifica
f"{6.022e23:.2e}"            # '6.02e+23'

# Percentuale
f"{0.0325:.1%}"              # '3.2%'

# Separatore migliaia
f"{59_641_488:,}"            # '59,641,488'

# Allineamento
f"|{'Anna':<15}|"            # '|Anna           |'  (sinistra)
f"|{'Anna':>15}|"            # '|           Anna|'  (destra)
f"|{'Anna':^15}|"            # '|     Anna      |'  (centro)

# Numeri allineati
f"{voto:>5d}"                # allinea a destra su 5 caratteri
```

### Espressioni regolari (cenni)

```python
import re

numeri: list[str] = re.findall(r"\d+\.?\d*", testo)
if re.match(r"^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$", cf):
    print("Codice fiscale valido")
```

---

## 5. Liste e tuple (F11)

### Creare liste

```python
temperature: list[float] = [18.5, 21.3, 19.7]
vuota: list[float] = []
```

### Indicizzazione e slicing

```python
voti: list[int] = [28, 30, 25, 27, 22]
voti[0]        # 28 (primo)
voti[-1]       # 22 (ultimo)
voti[2:5]      # [25, 27, 22]
voti[:3]       # [28, 30, 25]
voti[::2]      # [28, 25, 22]
voti[::-1]     # [22, 27, 25, 30, 28]
```

### Operazioni su liste

```python
a + b          # concatenazione
a * 3          # ripetizione
30 in voti     # appartenenza → True
len(voti)      # lunghezza → 5
```

### Metodi lista — aggiungere

```python
voti.append(27)          # aggiunge in fondo
voti.insert(1, 29)       # inserisce alla posizione 1
voti.extend([22, 24])    # aggiunge più elementi
```

### Metodi lista — rimuovere

```python
voti.remove(30)          # rimuove la prima occorrenza
ultimo: int = voti.pop()       # rimuove e restituisce l'ultimo
secondo: int = voti.pop(1)     # rimuove e restituisce alla posizione 1
```

### Metodi lista — ordinare e cercare

```python
voti.sort()                    # ordina in place (crescente)
voti.sort(reverse=True)        # ordina in place (decrescente)
voti_ord: list[int] = sorted(voti)  # restituisce nuova lista ordinata
voti.reverse()                 # inverte in place
voti.index(30)                 # posizione della prima occorrenza
voti.count(30)                 # quante volte appare
```

### Alias vs copia

```python
# ALIAS (stesso oggetto!)
b: list[int] = a              # b e a puntano alla stessa lista

# COPIA SUPERFICIALE (shallow copy)
b: list[int] = a.copy()       # oppure a[:] oppure list(a)

# COPIA PROFONDA (per liste annidate)
import copy
b: list[list[int]] = copy.deepcopy(a)
```

### Tuple

```python
coordinate: tuple[float, float] = (45.4642, 9.1900)
giorni: tuple[str, ...] = ("lun", "mar", "mer", "gio", "ven")
singolo: tuple[int] = (42,)    # virgola obbligatoria!
```

### Unpacking

```python
lat, lon = coordinate
a, b = b, a                   # scambio

# Return multipli da funzione
def stats(valori: list[float]) -> tuple[float, float, float]:
    return sum(valori) / len(valori), min(valori), max(valori)

media, minimo, massimo = stats(dati)
```

### Tuple come chiavi di dizionario

```python
posizioni: dict[tuple[int, int], str] = {
    (0, 0): "origine",
    (1, 0): "destra",
}
```

### Named tuple

```python
from typing import NamedTuple

class Osservazione(NamedTuple):
    valore: float
    unita: str
    timestamp: str

o: Osservazione = Osservazione(valore=23.5, unita="°C", timestamp="2025-01-15")
print(o.valore)    # 23.5
```

### Calcolo della mediana

```python
campione_ordinato: list[float] = sorted(campione)
n: int = len(campione_ordinato)
if n % 2 == 1:
    mediana: float = campione_ordinato[n // 2]
else:
    mediana = (campione_ordinato[n // 2 - 1] + campione_ordinato[n // 2]) / 2
```

---

## 6. Dizionari, set e mutabilità (F12)

### Creare dizionari

```python
voti: dict[str, int] = {"analisi": 28, "informatica": 30}
vuoto: dict[str, str] = {}
config: dict[str, int] = dict(larghezza=800, altezza=600)
da_coppie: dict[str, int] = dict([("a", 1), ("b", 2)])
```

### Accesso, modifica, aggiunta, rimozione

```python
voti["analisi"]            # 28 (accesso)
voti["analisi"] = 29       # modifica
voti["statistica"] = 27    # aggiunta
del voti["informatica"]    # rimozione
```

### Accesso sicuro con `get()`

```python
voto: int | None = voti.get("algebra")         # None se assente
voto: int = voti.get("algebra", 0)              # 0 se assente
```

### Pattern conteggio con `get()`

```python
conteggi: dict[str, int] = {}
for parola in parole:
    conteggi[parola] = conteggi.get(parola, 0) + 1
```

### Iterare su un dizionario

```python
for chiave in diz:                    # solo chiavi
for chiave, valore in diz.items():    # chiave e valore
list(diz.keys())                      # lista delle chiavi
list(diz.values())                    # lista dei valori
```

### Metodi dizionario

```python
base.update(nuovi)                    # aggiorna/unisce
unione: dict = base | nuovi           # unione (Python 3.9+)
rimosso: int = voti.pop("info")       # rimuove e restituisce
assente: int = voti.pop("alg", -1)    # con default se assente
```

### `Counter` — contare frequenze

```python
from collections import Counter

frequenze: Counter[str] = Counter(parole)
print(frequenze["casa"])           # 3
print(frequenze["drago"])          # 0 (nessun errore)
print(frequenze.most_common(2))    # [("casa", 3), ("albero", 2)]
```

### `defaultdict` — dizionario con default

```python
from collections import defaultdict

conteggi: defaultdict[str, int] = defaultdict(int)       # default: 0
gruppi: defaultdict[str, list[str]] = defaultdict(list)  # default: []

for parola in parole:
    conteggi[parola] += 1

for cognome, corso in studenti:
    gruppi[corso].append(cognome)
```

### Set — creare e operare

```python
numeri: set[int] = {1, 2, 3, 4, 5}
vuoto: set[int] = set()                # {} crea un dict!
unici: set[str] = set(lista)           # rimuove duplicati
```

### Operazioni insiemistiche

```python
a | b      # unione
a & b      # intersezione
a - b      # differenza
a ^ b      # differenza simmetrica
a <= b     # sottoinsieme
```

### Metodi set

```python
colori.add("giallo")       # aggiunge
colori.discard("verde")    # rimuove (nessun errore se assente)
colori.remove("rosso")     # rimuove (KeyError se assente)
```

### Appartenenza — set vs lista

```python
# Set: O(1) — praticamente istantaneo
999_999 in grande_set

# Lista: O(n) — lento per grandi collezioni
999_999 in grande_lista
```

### Tabella mutabilità

| Tipo | Mutabile | Hashable | Uso come chiave dict |
|---|---|---|---|
| `int`, `float`, `str`, `bool` | No | Sì | Sì |
| `tuple` | No | Sì* | Sì* |
| `frozenset` | No | Sì | Sì |
| `list` | Sì | No | No |
| `dict` | Sì | No | No |
| `set` | Sì | No | No |

*Solo se contiene elementi hashable.

### Alias e copie — effetti collaterali

```python
# Alias: modifica condivisa!
lista_b: list[int] = lista_a
lista_a.append(4)    # lista_b è cambiata!

# Copia: indipendente
lista_c: list[int] = lista_a.copy()
lista_a.append(5)    # lista_c NON è cambiata
```

---

## 7. Funzioni — fondamenti (F13)

### Definire e chiamare una funzione

```python
def calcola_media(valori: list[float]) -> float:
    """Calcola la media aritmetica."""
    return sum(valori) / len(valori)

media: float = calcola_media([28.0, 30.0, 25.0])
```

### Funzione che restituisce `None`

```python
def stampa_report(titolo: str, dati: list[float]) -> None:
    print(f"=== {titolo} ===")
    for valore in dati:
        print(f"  {valore:.2f}")
```

### Return multipli con tuple

```python
def statistiche_base(valori: list[float]) -> tuple[float, float, float]:
    return sum(valori) / len(valori), min(valori), max(valori)

media, minimo, massimo = statistiche_base(dati)
```

### Parametri con valori di default

```python
def formatta(valore: float, decimali: int = 2, prefisso: str = "") -> str:
    return f"{prefisso}{valore:.{decimali}f}"

formatta(3.14)                 # "3.14"
formatta(3.14, 4)              # "3.1416"
formatta(3.14, 3, "€")        # "€3.142"
```

### Argomenti keyword

```python
formatta(valore=3.14, prefisso="€", decimali=3)
deviazione_standard(dati, campione=True)    # più leggibile
```

### `*args` e `**kwargs`

```python
def somma_tutti(*args: float) -> float:
    totale: float = 0.0
    for valore in args:
        totale += valore
    return totale

def stampa_info(nome: str, **kwargs: str) -> None:
    print(f"Nome: {nome}")
    for chiave, valore in kwargs.items():
        print(f"  {chiave}: {valore}")
```

### Default mutabile — il problema e la soluzione

```python
# MALE: il default mutabile è condiviso tra le chiamate!
def aggiungi(voto: int, lista: list[int] = []) -> list[int]:  # BUG!
    lista.append(voto)
    return lista

# BENE: usare None come default
def aggiungi(voto: int, lista: list[int] | None = None) -> list[int]:
    if lista is None:
        lista = []
    lista.append(voto)
    return lista
```

### Scope — regole fondamentali

```python
PI: float = 3.14159265  # variabile globale: leggibile ovunque

def area_cerchio(raggio: float) -> float:
    return PI * raggio ** 2     # OK: legge la globale

# Per modificare una globale (SCONSIGLIATO):
# global contatore
```

### Docstring — formato Google

```python
def deviazione_standard(valori: list[float], campione: bool = True) -> float:
    """Calcola la deviazione standard.

    Args:
        valori: lista di valori numerici (almeno 2).
        campione: se True usa n-1, se False usa n.

    Returns:
        La deviazione standard come float.

    Raises:
        ValueError: se la lista contiene meno di 2 elementi.
    """
    n: int = len(valori)
    if n < 2:
        raise ValueError("Servono almeno 2 valori")
    media: float = sum(valori) / n
    scarti: list[float] = [(x - media) ** 2 for x in valori]
    divisore: int = n - 1 if campione else n
    return (sum(scarti) / divisore) ** 0.5
```

---

## 8. Funzioni avanzate e moduli (F14)

### Funzioni come oggetti

```python
operazione = quadrato     # assegnare una funzione a una variabile
print(operazione(5))      # 25
```

### Lambda

```python
quadrato = lambda x: x ** 2
somma = lambda a, b: a + b
```

### `sorted()` con `key=`

```python
# Ordinare per lunghezza
sorted(parole, key=lambda s: len(s))

# Ordinare dizionari per un campo
sorted(studenti, key=lambda s: s["media"])
sorted(studenti, key=lambda s: s["media"], reverse=True)

# Ordinare per più criteri
sorted(esami, key=lambda e: (-e["voto"], e["data"]))

# min/max con key
migliore: dict = max(studenti, key=lambda s: s["media"])
```

### `map()` e `filter()` vs comprehension

```python
# map: applica funzione a ogni elemento
list(map(int, ["1", "2", "3"]))          # [1, 2, 3]
[int(s) for s in ["1", "2", "3"]]        # equivalente

# filter: seleziona elementi
list(filter(lambda v: v >= 18, voti))    # solo sufficienti
[v for v in voti if v >= 18]              # equivalente (preferito)
```

### Importare moduli

```python
import statistiche                        # modulo intero
from statistiche import media, varianza   # nomi specifici
import statistiche as stat                # con alias
```

### Libreria standard — `math`

```python
import math

math.sqrt(16)          # 4.0
math.log(100, 10)      # 2.0
math.log(math.e)       # 1.0
math.pi                # 3.14159...
math.factorial(5)      # 120
math.ceil(3.2)         # 4
math.floor(3.8)        # 3
```

### Libreria standard — `statistics`

```python
import statistics

statistics.mean(dati)       # media
statistics.median(dati)     # mediana
statistics.stdev(dati)      # deviazione standard campionaria
statistics.variance(dati)   # varianza campionaria
statistics.mode(dati)       # moda
```

### Libreria standard — `random`

```python
import random

random.seed(42)                   # riproducibilità
random.random()                   # float in [0, 1)
random.randint(1, 100)            # intero in [1, 100]
random.uniform(0.0, 10.0)        # float in [0, 10]
random.choice(lista)              # elemento casuale
random.sample(lista, 2)           # 2 elementi senza ripetizione
random.shuffle(lista)             # mescola in-place
```

### Libreria standard — `json`

```python
import json

dati: dict = json.loads('{"nome": "Anna"}')  # da stringa JSON a dict
testo: str = json.dumps(dati, indent=2)      # da dict a stringa JSON
```

### Libreria standard — `datetime`

```python
from datetime import date, timedelta

oggi: date = date.today()
tra_7_giorni: date = oggi + timedelta(days=7)
nascita: date = date(2005, 6, 15)
eta_giorni: int = (oggi - nascita).days
```

### Ordine degli import (PEP 8)

```python
# 1. Libreria standard
import math
import statistics

# 2. Pacchetti terze parti
import numpy as np
import pandas as pd

# 3. Moduli propri
from mio_progetto.utils import pulisci_dati
```

---

## 9. File, dati e gestione errori (F15)

### Leggere un file di testo

```python
# Leggere tutto il contenuto
with open("dati.txt", "r", encoding="utf-8") as f:
    contenuto: str = f.read()

# Leggere riga per riga (memoria efficiente)
with open("dati.txt", "r", encoding="utf-8") as f:
    for riga in f:
        print(riga.strip())

# Leggere tutte le righe in una lista
with open("dati.txt", "r", encoding="utf-8") as f:
    righe: list[str] = f.readlines()
```

### Scrivere un file di testo

```python
# Scrittura (sovrascrive)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f"Media: {media:.4f}\n")

# Append (aggiunge in fondo)
with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"{evento}\n")
```

### `pathlib` — gestione percorsi

```python
from pathlib import Path

percorso: Path = Path("dati") / "2024" / "risultati.csv"
print(percorso.name)       # "risultati.csv"
print(percorso.stem)       # "risultati"
print(percorso.suffix)     # ".csv"
print(percorso.parent)     # dati/2024

percorso.exists()          # True/False
percorso.is_file()         # True/False

# Creare directory
Path("output/grafici").mkdir(parents=True, exist_ok=True)

# Elencare file
for f in Path("dati").glob("*.csv"):
    print(f.name)

# Leggere direttamente
contenuto: str = percorso.read_text(encoding="utf-8")
```

### Leggere CSV

```python
import csv

# Con csv.reader
with open("voti.csv", "r", encoding="utf-8") as f:
    lettore = csv.reader(f)
    intestazione = next(lettore)     # salta l'intestazione
    for riga in lettore:
        nome, voto = riga[0], int(riga[2])

# Con csv.DictReader (più leggibile)
with open("voti.csv", "r", encoding="utf-8") as f:
    lettore = csv.DictReader(f)
    for riga in lettore:
        print(f"{riga['nome']}: {riga['voto']}")

# Separatore europeo (punto e virgola)
csv.DictReader(f, delimiter=";")
```

### Scrivere CSV

```python
import csv

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    scrittore = csv.DictWriter(f, fieldnames=["nome", "voto"])
    scrittore.writeheader()
    scrittore.writerows(dati)
```

### Leggere e scrivere JSON

```python
import json

# Leggere
with open("config.json", "r", encoding="utf-8") as f:
    config: dict = json.load(f)

# Scrivere
with open("risultati.json", "w", encoding="utf-8") as f:
    json.dump(risultati, f, indent=2, ensure_ascii=False)
```

### Gestione eccezioni — `try/except`

```python
try:
    valore: int = int(input("Numero: "))
except ValueError:
    print("Non è un numero valido")
```

### Catturare eccezioni specifiche

```python
try:
    risultato = operazione(dati)
except ValueError as e:
    print(f"Valore non valido: {e}")
except ZeroDivisionError:
    print("Divisione per zero")
except FileNotFoundError:
    print("File non trovato")
```

### `else` e `finally`

```python
try:
    f = open(percorso, "r", encoding="utf-8")
except FileNotFoundError:
    print("File non trovato")
else:
    contenuto = f.readlines()    # eseguito solo se try ha successo
finally:
    print("Operazione completata")  # eseguito SEMPRE
```

### Sollevare eccezioni con `raise`

```python
def calcola_media(voti: list[int]) -> float:
    if not voti:
        raise ValueError("Lista vuota")
    for voto in voti:
        if not 0 <= voto <= 30:
            raise ValueError(f"Voto fuori range: {voto}")
    return sum(voti) / len(voti)
```

---

## 10. Programmazione a oggetti (F16)

### Definire una classe

```python
class Punto:
    """Rappresenta un punto nel piano cartesiano."""

    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y
```

### Classe completa con metodi

```python
class Studente:
    universita: str = "Università degli Studi"  # attributo di classe

    def __init__(self, nome: str, cognome: str, matricola: int) -> None:
        self.nome: str = nome
        self.cognome: str = cognome
        self.matricola: int = matricola
        self.voti: list[int] = []

    def aggiungi_voto(self, voto: int) -> None:
        if not 18 <= voto <= 30:
            raise ValueError(f"Voto {voto} fuori range")
        self.voti.append(voto)

    def media(self) -> float:
        if not self.voti:
            raise ValueError("Nessun voto")
        return sum(self.voti) / len(self.voti)

    def __str__(self) -> str:
        return f"{self.nome} {self.cognome} (mat. {self.matricola})"

    def __repr__(self) -> str:
        return f"Studente({self.nome!r}, {self.cognome!r}, {self.matricola})"
```

### Usare una classe

```python
anna: Studente = Studente("Anna", "Rossi", 12345)
anna.aggiungi_voto(28)
anna.aggiungi_voto(30)
print(anna.media())    # 29.0
print(anna)            # Anna Rossi (mat. 12345)
```

### Metodi speciali (dunder methods)

| Metodo | Invocato da | Scopo |
|---|---|---|
| `__init__` | `Classe(...)` | Inizializzazione |
| `__str__` | `str(obj)`, `print(obj)` | Rappresentazione leggibile |
| `__repr__` | `repr(obj)` | Rappresentazione tecnica |
| `__len__` | `len(obj)` | Lunghezza |
| `__eq__` | `obj1 == obj2` | Uguaglianza |
| `__lt__` | `obj1 < obj2` | Confronto "minore di" |
| `__getitem__` | `obj[i]` | Accesso per indice |
| `__contains__` | `x in obj` | Appartenenza |

### `__eq__` e `__lt__`

```python
class Punto:
    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    def __eq__(self, altro: object) -> bool:
        if not isinstance(altro, Punto):
            return NotImplemented
        return self.x == altro.x and self.y == altro.y

    def __lt__(self, altro: "Punto") -> bool:
        return (self.x**2 + self.y**2) < (altro.x**2 + altro.y**2)
```

### Ereditarietà

```python
class StudenteLavoratore(Studente):
    def __init__(self, nome: str, cognome: str, matricola: int,
                 azienda: str, ore: int) -> None:
        super().__init__(nome, cognome, matricola)
        self.azienda: str = azienda
        self.ore: int = ore

    def è_part_time(self) -> bool:
        return self.ore < 20

    def __str__(self) -> str:
        return f"{super().__str__()} — {self.azienda} ({self.ore}h/sett.)"
```

### `@property` — accesso controllato

```python
class ContoBancario:
    def __init__(self, titolare: str, saldo: float = 0.0) -> None:
        self.titolare: str = titolare
        self._saldo: float = saldo       # convenzione: uso interno

    @property
    def saldo(self) -> float:
        return self._saldo               # sola lettura

    def deposita(self, importo: float) -> None:
        if importo <= 0:
            raise ValueError("Importo deve essere positivo")
        self._saldo += importo

conto: ContoBancario = ContoBancario("Anna", 1000.0)
print(conto.saldo)       # 1000.0 (sembra attributo, è un metodo)
# conto.saldo = 9999     # AttributeError!
```

### Composizione (HA-un)

```python
class Dipartimento:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.docenti: list[Docente] = []    # composizione

    def aggiungi_docente(self, docente: Docente) -> None:
        self.docenti.append(docente)

    def __len__(self) -> int:
        return len(self.docenti)
```

---

## 11. NumPy, Pandas e visualizzazione (F17)

### NumPy — creare array

```python
import numpy as np

array: np.ndarray = np.array([1.0, 2.0, 3.0])
matrice: np.ndarray = np.array([[1, 2, 3], [4, 5, 6]])

np.zeros(10)                    # 10 zeri
np.zeros((3, 4))                # matrice 3×4 di zeri
np.ones(5)                      # 5 uno
np.arange(0, 10, 0.5)           # sequenza con passo 0.5
np.linspace(0, 1, 100)          # 100 punti equidistanti tra 0 e 1
```

### NumPy — attributi array

```python
dati.shape      # (righe, colonne)
dati.dtype      # tipo degli elementi (es. float64)
dati.ndim       # numero di dimensioni
dati.size       # numero totale di elementi
```

### NumPy — operazioni vettorizzate

```python
a: np.ndarray = np.array([10, 20, 30])
b: np.ndarray = np.array([1, 2, 3])

a + b           # [11, 22, 33]
a * b           # [10, 40, 90]
a / b           # [10.0, 10.0, 10.0]
a > 15          # [False, True, True]
a ** 2          # [100, 400, 900]
```

### NumPy — boolean indexing (filtro)

```python
temperature: np.ndarray = np.array([15.2, 22.1, 31.5, 18.7])
calde: np.ndarray = temperature[temperature > 25]    # [31.5]
```

### NumPy — statistiche

```python
np.mean(voti)              # media
np.median(voti)            # mediana
np.std(voti)               # deviazione standard (popolazione)
np.std(voti, ddof=1)       # deviazione standard campionaria
np.var(voti)               # varianza (popolazione)
np.sum(voti)               # somma
np.min(voti)               # minimo
np.max(voti)               # massimo
```

### NumPy — broadcasting e standardizzazione

```python
# Standardizzazione (z-score)
z_scores: np.ndarray = (dati - np.mean(dati)) / np.std(dati, ddof=1)

# Media per colonna di una matrice
medie_colonne: np.ndarray = np.mean(matrice, axis=0)
centrata: np.ndarray = matrice - medie_colonne
```

### NumPy — numeri casuali

```python
rng: np.random.Generator = np.random.default_rng(seed=42)

rng.uniform(0.0, 1.0, size=1000)        # uniforme
rng.normal(loc=0, scale=1, size=1000)    # normale
rng.binomial(n=10, p=0.5, size=1000)     # binomiale
rng.integers(low=1, high=7, size=100)    # interi casuali
rng.permutation(10)                      # permutazione
```

### Pandas — creare Series e DataFrame

```python
import pandas as pd

# Series
voti: pd.Series = pd.Series([28, 30, 25], index=["Alice", "Bob", "Carla"])

# DataFrame
df: pd.DataFrame = pd.DataFrame({
    "nome": ["Alice", "Bob", "Carla"],
    "voto": [28, 30, 25],
    "corso": ["Stat I", "Stat I", "Stat II"]
})
```

### Pandas — leggere CSV

```python
df: pd.DataFrame = pd.read_csv("dati.csv")

# Con opzioni
df = pd.read_csv("dati.csv", sep=";", encoding="utf-8",
                  decimal=",", na_values=["", "NA", "?"])
```

### Pandas — esplorazione iniziale

```python
df.head()           # prime 5 righe
df.tail()           # ultime 5 righe
df.info()           # struttura e tipi
df.describe()       # statistiche descrittive
df.shape            # (righe, colonne)
df.columns          # nomi colonne
df["corso"].value_counts()              # frequenze assolute
df["corso"].value_counts(normalize=True) # frequenze relative
```

### Pandas — selezione e filtro

```python
# Una colonna → Series
voti: pd.Series = df["voto"]

# Più colonne → DataFrame
sotto: pd.DataFrame = df[["nome", "voto"]]

# Filtro booleano
promossi: pd.DataFrame = df[df["voto"] >= 18]
eccellenti: pd.DataFrame = df[(df["voto"] >= 28) & (df["corso"] == "Stat I")]

# loc (per etichetta) e iloc (per posizione)
df.loc[0, "nome"]           # riga 0, colonna "nome"
df.iloc[:3]                 # prime 3 righe
```

### Pandas — valori mancanti

```python
df.isna().sum()                         # contare mancanti per colonna
df.dropna()                             # rimuovere righe con mancanti
df.dropna(subset=["voto"])              # solo se manca il voto
df.fillna({"voto": 0, "corso": "?"})    # sostituire con valori
df["voto"].fillna(df["voto"].mean())    # sostituire con la media
```

### Pandas — duplicati

```python
df.duplicated().sum()                   # contare duplicati
df.drop_duplicates()                    # rimuovere duplicati
df.drop_duplicates(subset=["nome"])     # su colonne specifiche
```

### Pandas — aggregazione con `groupby`

```python
df.groupby("corso")["voto"].mean()                  # media per gruppo
df.groupby("corso")["voto"].agg(["mean", "std", "min", "max", "count"])
df.groupby(["corso", "anno"])["voto"].mean()         # gruppi multipli
```

### Pandas — merge (join)

```python
risultato: pd.DataFrame = pd.merge(esami, anagrafica, on="studente_id")
risultato_left: pd.DataFrame = pd.merge(esami, anagrafica,
                                         on="studente_id", how="left")
```

### Pandas — method chaining

```python
risultato = (
    df
    .dropna(subset=["voto"])
    .query("voto >= 18")
    .groupby("corso")["voto"]
    .mean()
    .reset_index()
    .rename(columns={"voto": "media_voto"})
)
```

### Matplotlib — grafico a linee

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
plt.plot(x, y, color="steelblue", linewidth=1.5, label="sin(x)")
plt.title("Titolo")
plt.xlabel("Asse X")
plt.ylabel("Asse Y")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("grafico.png", dpi=150)
plt.show()
```

### Matplotlib — istogramma

```python
plt.figure(figsize=(8, 4))
plt.hist(dati, bins=25, color="steelblue", edgecolor="white", alpha=0.8)
plt.axvline(np.mean(dati), color="red", linestyle="--", label="Media")
plt.title("Distribuzione")
plt.xlabel("Valore")
plt.ylabel("Frequenza")
plt.legend()
plt.tight_layout()
plt.show()
```

### Matplotlib — scatter plot

```python
plt.figure(figsize=(7, 5))
plt.scatter(x, y, alpha=0.6, color="steelblue", edgecolors="white")
plt.title("Relazione tra X e Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.show()
```

### Matplotlib — barre e boxplot

```python
# Barre
plt.bar(categorie, valori, color="steelblue", edgecolor="white")

# Boxplot
plt.boxplot([gruppo1, gruppo2, gruppo3], labels=["A", "B", "C"],
            patch_artist=True, boxprops=dict(facecolor="steelblue", alpha=0.5))
```

### Matplotlib — stile minimale

```python
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(dati, bins=30, color="steelblue", edgecolor="white")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.2)
fig.tight_layout()
plt.show()
```

### Seaborn — grafici statistici

```python
import seaborn as sns

# Boxplot per gruppi
sns.boxplot(data=df, x="corso", y="voto", palette="Set2")

# Heatmap correlazione
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm",
            vmin=-1, vmax=1, center=0)

# Pairplot
sns.pairplot(df, hue="corso", palette="Set2", diag_kind="kde")
```

### SciPy — test statistici

```python
from scipy import stats

# t-test per un campione
risultato = stats.ttest_1samp(campione, popmean=100)
print(f"t = {risultato.statistic:.3f}, p = {risultato.pvalue:.4f}")

# Distribuzione normale
stats.norm.cdf(1.96)       # ~0.975
stats.norm.ppf(0.975)      # ~1.96
```

### scikit-learn — regressione lineare

```python
from sklearn.linear_model import LinearRegression

modello: LinearRegression = LinearRegression()
modello.fit(X, y)                          # addestramento
previsioni: np.ndarray = modello.predict(X_nuovo)
print(modello.coef_)                       # coefficienti
print(modello.intercept_)                  # intercetta
```

---

## Appendice — Comandi terminale utili

```bash
# Ambienti virtuali
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate       # Windows
deactivate

# Gestione pacchetti
pip install numpy pandas matplotlib seaborn scipy scikit-learn
pip install -r requirements.txt
pip freeze > requirements.txt
pip list

# Eseguire script
python script.py

# Linter e formatter
ruff check .
black .
mypy script.py

# Test
pytest
```
