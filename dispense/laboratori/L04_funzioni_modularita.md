# Laboratorio 4 — Funzioni e modularità

## Informazioni

- **Prerequisiti:** Lezioni frontali T13 (Funzioni) e T14 (Modularità e buone pratiche)
- **Durata stimata:** 2 ore
- **Obiettivi:** Definire funzioni con type hints e docstring. Usare `assert` per verificare la correttezza. Fare refactoring di codice monolitico. Usare `sorted()` con `key`. Creare e importare moduli.

---

## Esercizio guidato 1 — Implementare funzioni statistiche

### Passo 1: La funzione `media()`

```python
def media(valori: list[float]) -> float:
    """Calcola la media aritmetica di una lista di numeri.

    Args:
        valori: lista non vuota di numeri.

    Returns:
        La media aritmetica dei valori.

    Raises:
        ValueError: se la lista è vuota.
    """
    if len(valori) == 0:
        raise ValueError("Impossibile calcolare la media di una lista vuota")
    return sum(valori) / len(valori)


# Test con assert
assert media([10, 20, 30]) == 20.0
assert media([5]) == 5.0
assert media([1, 2, 3, 4, 5]) == 3.0
print("media(): tutti i test superati")
```

Osservate la struttura:

- **Type hints** nei parametri (`valori: list[float]`) e nel valore di ritorno (`-> float`).
- **Docstring** che spiega cosa fa la funzione, cosa accetta e cosa restituisce.
- **Validazione** dell'input: se la lista è vuota, solleviamo un errore esplicito.
- **Assert** come test: se l'asserzione fallisce, Python solleva `AssertionError` e sappiamo che qualcosa non funziona.

### Passo 2: La funzione `varianza()`

La varianza misura quanto i dati si disperdono intorno alla media. Usiamo la varianza campionaria (dividiamo per n-1):

```python
def varianza(valori: list[float]) -> float:
    """Calcola la varianza campionaria di una lista di numeri.

    Usa il denominatore n-1 (correzione di Bessel).

    Args:
        valori: lista con almeno 2 elementi.

    Returns:
        La varianza campionaria.

    Raises:
        ValueError: se la lista ha meno di 2 elementi.
    """
    n: int = len(valori)
    if n < 2:
        raise ValueError("Servono almeno 2 valori per calcolare la varianza")
    m: float = media(valori)  # riusiamo la funzione definita prima!
    somma_scarti_quadrati: float = sum((x - m) ** 2 for x in valori)
    return somma_scarti_quadrati / (n - 1)


# Test
assert abs(varianza([2, 4, 4, 4, 5, 5, 7, 9]) - 4.571428571428571) < 1e-10
assert abs(varianza([10, 10, 10]) - 0.0) < 1e-10
print("varianza(): tutti i test superati")
```

Notate come `varianza()` chiama `media()`: le funzioni si possono comporre, evitando di duplicare codice.

### Passo 3: La funzione `mediana()`

```python
def mediana(valori: list[float]) -> float:
    """Calcola la mediana di una lista di numeri.

    Args:
        valori: lista non vuota di numeri.

    Returns:
        Il valore mediano.

    Raises:
        ValueError: se la lista è vuota.
    """
    if len(valori) == 0:
        raise ValueError("Impossibile calcolare la mediana di una lista vuota")
    ordinati: list[float] = sorted(valori)
    n: int = len(ordinati)
    centro: int = n // 2
    if n % 2 == 1:
        # Numero dispari di elementi: il mediano è quello centrale
        return ordinati[centro]
    else:
        # Numero pari: media dei due centrali
        return (ordinati[centro - 1] + ordinati[centro]) / 2


# Test
assert mediana([3, 1, 2]) == 2
assert mediana([1, 2, 3, 4]) == 2.5
assert mediana([5]) == 5
assert mediana([7, 1]) == 4.0
print("mediana(): tutti i test superati")
```

---

## Esercizio guidato 2 — Assert come strumento di testing

Gli `assert` non sono solo per controllare i test: servono anche per documentare le aspettative sul codice.

### Passo 1: Test di casi limite

```python
# Testare che le funzioni gestiscano correttamente gli errori
errore_sollevato: bool = False
try:
    media([])
except ValueError:
    errore_sollevato = True
assert errore_sollevato, "media([]) dovrebbe sollevare ValueError"

errore_sollevato = False
try:
    varianza([5])
except ValueError:
    errore_sollevato = True
assert errore_sollevato, "varianza([5]) dovrebbe sollevare ValueError"

print("Test sui casi limite: tutti superati")
```

### Passo 2: Test con valori noti

Quando si testano funzioni numeriche, bisogna fare attenzione ai confronti tra float. Non si scrive `assert varianza(dati) == 4.5` perché l'aritmetica in virgola mobile può introdurre piccoli errori. Si usa un confronto con tolleranza:

```python
def quasi_uguale(a: float, b: float, tolleranza: float = 1e-9) -> bool:
    """Verifica se due float sono approssimativamente uguali."""
    return abs(a - b) < tolleranza


# Test con dataset noto
dati: list[float] = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
assert quasi_uguale(media(dati), 5.0)
assert quasi_uguale(varianza(dati), 4.571428571428571)
assert quasi_uguale(mediana(dati), 4.5)
print("Test con valori noti: tutti superati")
```

---

## Esercizio guidato 3 — Refactoring: da monolitico a modulare

Il refactoring consiste nel migliorare la struttura del codice senza cambiarne il comportamento. Partiamo da un blocco di codice tutto in un unico pezzo e lo trasformiamo in funzioni.

### Il codice monolitico (prima)

```python
# Questo codice funziona, ma è un unico blocco non riutilizzabile
voti_stat: list[int] = [28, 24, 30, 26, 22, 27, 30, 25]
voti_anal: list[int] = [30, 22, 27, 25, 20, 28, 26, 24]

# Media statistica
somma_stat: int = 0
for v in voti_stat:
    somma_stat += v
media_stat: float = somma_stat / len(voti_stat)

# Media analisi
somma_anal: int = 0
for v in voti_anal:
    somma_anal += v
media_anal: float = somma_anal / len(voti_anal)

# Trova il voto massimo in statistica
max_stat: int = voti_stat[0]
for v in voti_stat[1:]:
    if v > max_stat:
        max_stat = v

# Trova il voto massimo in analisi
max_anal: int = voti_anal[0]
for v in voti_anal[1:]:
    if v > max_anal:
        max_anal = v

print(f"Statistica: media={media_stat:.1f}, max={max_stat}")
print(f"Analisi:    media={media_anal:.1f}, max={max_anal}")
```

Il problema è evidente: il codice per calcolare media e massimo è **duplicato**. Se avessimo dieci corsi, dovremmo copiare e incollare lo stesso blocco dieci volte.

### Il codice ristrutturato (dopo)

```python
def calcola_media(voti: list[int]) -> float:
    """Calcola la media di una lista di voti."""
    if len(voti) == 0:
        raise ValueError("Lista vuota")
    return sum(voti) / len(voti)


def trova_massimo(voti: list[int]) -> int:
    """Trova il voto massimo in una lista."""
    if len(voti) == 0:
        raise ValueError("Lista vuota")
    massimo: int = voti[0]
    for v in voti[1:]:
        if v > massimo:
            massimo = v
    return massimo


def stampa_report(nome_corso: str, voti: list[int]) -> None:
    """Stampa un report con media e massimo per un corso."""
    m: float = calcola_media(voti)
    mx: int = trova_massimo(voti)
    print(f"{nome_corso}: media={m:.1f}, max={mx}")


# Il codice principale diventa chiarissimo
corsi: dict[str, list[int]] = {
    "Statistica": [28, 24, 30, 26, 22, 27, 30, 25],
    "Analisi":    [30, 22, 27, 25, 20, 28, 26, 24],
}

for nome, voti in corsi.items():
    stampa_report(nome, voti)
```

Vantaggi del refactoring:

- **Nessuna duplicazione:** ogni operazione è definita una volta sola.
- **Riutilizzabilità:** possiamo aggiungere un corso con una sola riga.
- **Testabilità:** possiamo testare `calcola_media` e `trova_massimo` separatamente.
- **Leggibilità:** il codice principale è quasi pseudocodice.

---

## Esercizio guidato 4 — `sorted()` con `key=lambda`

La funzione `sorted()` accetta un parametro `key` che specifica come confrontare gli elementi. `lambda` permette di definire piccole funzioni anonime al volo.

### Passo 1: Ordinare stringhe per lunghezza

```python
parole: list[str] = ["statistica", "media", "varianza", "moda", "quartile"]

# Ordine alfabetico (default)
print(f"Alfabetico: {sorted(parole)}")

# Per lunghezza
print(f"Per lunghezza: {sorted(parole, key=lambda p: len(p))}")

# Per lunghezza decrescente
print(f"Per lunghezza (desc): {sorted(parole, key=lambda p: -len(p))}")
```

### Passo 2: Ordinare dizionari per un campo

```python
studenti: list[dict[str, object]] = [
    {"nome": "Anna",  "media": 28.5},
    {"nome": "Marco", "media": 24.0},
    {"nome": "Luca",  "media": 29.3},
    {"nome": "Sara",  "media": 27.1},
]

# Ordinare per media decrescente
classifica: list[dict[str, object]] = sorted(
    studenti, key=lambda s: s["media"], reverse=True
)

print("Classifica:")
for i, s in enumerate(classifica, start=1):
    print(f"  {i}. {s['nome']} — media: {s['media']}")
```

### Passo 3: Ordinare tuple per un elemento specifico

```python
risultati: list[tuple[str, int, float]] = [
    ("Anna",  3, 28.5),
    ("Marco", 2, 24.0),
    ("Luca",  3, 29.3),
    ("Sara",  2, 27.1),
]

# Ordinare per media (terzo elemento, indice 2)
per_media: list[tuple[str, int, float]] = sorted(
    risultati, key=lambda r: r[2], reverse=True
)

# Ordinare per numero di esami (secondo elemento), poi per media
per_esami_e_media: list[tuple[str, int, float]] = sorted(
    risultati, key=lambda r: (-r[1], -r[2])
)

print("Per media:")
for nome, esami, med in per_media:
    print(f"  {nome}: {esami} esami, media {med}")

print("Per esami (desc) e media (desc):")
for nome, esami, med in per_esami_e_media:
    print(f"  {nome}: {esami} esami, media {med}")
```

---

## Esercizio guidato 5 — Creare un modulo e importarlo

Un modulo è semplicemente un file `.py` che contiene definizioni di funzioni, variabili e classi. Creare moduli è il primo passo verso il codice riutilizzabile.

### Passo 1: Creare il file `statistiche.py`

Crea un file chiamato `statistiche.py` nella stessa cartella del tuo script, con il seguente contenuto:

```python
"""Modulo con funzioni statistiche di base.

Questo modulo fornisce implementazioni semplici di media,
varianza e mediana per liste di numeri.
"""


def media(valori: list[float]) -> float:
    """Calcola la media aritmetica."""
    if len(valori) == 0:
        raise ValueError("Lista vuota")
    return sum(valori) / len(valori)


def varianza(valori: list[float]) -> float:
    """Calcola la varianza campionaria (denominatore n-1)."""
    n: int = len(valori)
    if n < 2:
        raise ValueError("Servono almeno 2 valori")
    m: float = media(valori)
    return sum((x - m) ** 2 for x in valori) / (n - 1)


def deviazione_standard(valori: list[float]) -> float:
    """Calcola la deviazione standard campionaria."""
    return varianza(valori) ** 0.5


def mediana(valori: list[float]) -> float:
    """Calcola la mediana."""
    if len(valori) == 0:
        raise ValueError("Lista vuota")
    ordinati: list[float] = sorted(valori)
    n: int = len(ordinati)
    centro: int = n // 2
    if n % 2 == 1:
        return ordinati[centro]
    return (ordinati[centro - 1] + ordinati[centro]) / 2
```

### Passo 2: Importare e usare il modulo

Crea un secondo file, ad esempio `analisi.py`, nella stessa cartella:

```python
"""Script che usa il modulo statistiche per analizzare dati."""
import statistiche

dati_temperatura: list[float] = [18.5, 21.0, 19.3, 22.1, 20.7, 17.9, 23.4]

m: float = statistiche.media(dati_temperatura)
v: float = statistiche.varianza(dati_temperatura)
ds: float = statistiche.deviazione_standard(dati_temperatura)
med: float = statistiche.mediana(dati_temperatura)

print(f"Media:     {m:.2f}")
print(f"Varianza:  {v:.2f}")
print(f"Dev. std.: {ds:.2f}")
print(f"Mediana:   {med:.2f}")
```

### Passo 3: Importazione selettiva

```python
# Importare solo le funzioni che servono
from statistiche import media, mediana

dati: list[float] = [10, 20, 30, 40, 50]
print(f"Media: {media(dati)}")
print(f"Mediana: {mediana(dati)}")
```

### Passo 4: Il blocco `if __name__ == "__main__"`

Aggiungi alla fine di `statistiche.py`:

```python
if __name__ == "__main__":
    # Questo codice viene eseguito SOLO se si lancia direttamente
    # statistiche.py, NON quando viene importato come modulo.
    print("=== Test del modulo statistiche ===")

    dati_test: list[float] = [2, 4, 4, 4, 5, 5, 7, 9]
    print(f"Dati: {dati_test}")
    print(f"Media:    {media(dati_test):.2f}")
    print(f"Varianza: {varianza(dati_test):.2f}")
    print(f"Dev.std.: {deviazione_standard(dati_test):.2f}")
    print(f"Mediana:  {mediana(dati_test):.2f}")
    print("Test completati.")
```

Se lanci `python statistiche.py`, vedrai i test. Se lo importi con `import statistiche`, i test non verranno eseguiti.

---

## Esercizi autonomi

Per ciascun esercizio, scrivi il codice completo con type hints e docstring. Testa ogni funzione con almeno 3 `assert`.

### Esercizio A1 — Funzione moda (base)

Implementa una funzione `moda()` che restituisce il valore piu frequente in una lista.

```python
def moda(valori: list[float]) -> float:
    ...
```

Specifiche:

1. Se la lista e vuota, solleva `ValueError`.
2. Se ci sono piu valori con la stessa frequenza massima, restituisci il primo incontrato.
3. Puoi usare `Counter` oppure risolvere il problema con un dizionario manuale.
4. Testa con: `moda([1, 2, 2, 3])` deve restituire `2`; `moda([5])` deve restituire `5`.

### Esercizio A2 — Normalizzazione z-score (intermedio)

Lo z-score trasforma ogni valore sottraendo la media e dividendo per la deviazione standard: `z = (x - media) / dev_std`.

Implementa:

```python
def z_score(valori: list[float]) -> list[float]:
    ...
```

Specifiche:

1. Se la lista ha meno di 2 elementi, solleva `ValueError`.
2. Se la deviazione standard e zero (tutti i valori uguali), solleva `ValueError` con un messaggio appropriato.
3. Riusa le funzioni `media()` e `deviazione_standard()` definite in precedenza o nel modulo `statistiche`.
4. Verifica che la media degli z-score sia circa 0 e la deviazione standard sia circa 1.

### Esercizio A3 — Decoratore timer (avanzato)

Un decoratore e una funzione che "avvolge" un'altra funzione per aggiungere comportamento. Implementa un decoratore che misura il tempo di esecuzione:

```python
import time
from typing import Callable, Any


def timer(funzione: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Registra il tempo prima dell'esecuzione
        # Chiama la funzione originale
        # Registra il tempo dopo l'esecuzione
        # Stampa il tempo impiegato
        # Restituisci il risultato della funzione originale
        ...
    return wrapper
```

Specifiche:

1. Usa `time.perf_counter()` per misurare il tempo.
2. Applica il decoratore alla funzione `media()` con la sintassi `@timer`.
3. Testa con una lista molto lunga: `list(range(1_000_000))`.
4. Verifica che il risultato della funzione decorata sia identico a quello della funzione originale.

**Nota:** i decoratori non sono nel programma d'esame, ma capire il concetto aiuta a comprendere come le funzioni siano oggetti di prima classe in Python.

---

## Sfida finale — Mini-toolkit statistico completo

Crea un modulo `toolkit.py` che contenga un toolkit statistico completo. Il modulo deve includere tutte le seguenti funzioni, ciascuna con type hints, docstring e validazione dell'input:

### Funzioni richieste

```python
def media(valori: list[float]) -> float: ...
def mediana(valori: list[float]) -> float: ...
def moda(valori: list[float]) -> float: ...
def varianza(valori: list[float]) -> float: ...
def deviazione_standard(valori: list[float]) -> float: ...
def z_score(valori: list[float]) -> list[float]: ...
def riepilogo(valori: list[float]) -> dict[str, float]: ...
```

### Requisiti

1. **Validazione:** ogni funzione deve controllare che l'input sia valido (lista non vuota, lunghezza sufficiente) e sollevare `ValueError` con un messaggio chiaro.
2. **Composizione:** le funzioni devono riutilizzarsi tra loro (la varianza deve usare la media, la deviazione standard deve usare la varianza, e cosi via).
3. **`riepilogo()`** deve restituire un dizionario con tutte le statistiche:

   ```python
   {
       "media": ...,
       "mediana": ...,
       "moda": ...,
       "varianza": ...,
       "dev_standard": ...,
       "minimo": ...,
       "massimo": ...,
       "n": ...,
   }
   ```

4. **Testing:** aggiungi un blocco `if __name__ == "__main__"` con almeno 10 `assert` che verificano la correttezza di tutte le funzioni.
5. **Report finale:** nel blocco principale, applica `riepilogo()` a questo dataset e stampa i risultati formattati:

   ```python
   voti: list[float] = [28, 24, 30, 26, 22, 27, 30, 25, 29, 23,
                         30, 18, 26, 28, 24, 27, 30, 22, 25, 29]
   ```

---

## Domande di verifica

1. Qual e la differenza tra parametri e argomenti di una funzione?
2. Cosa succede se una funzione non ha un'istruzione `return`? Quale valore restituisce?
3. Perche e importante validare l'input di una funzione invece di lasciare che Python generi un errore generico?
4. Che differenza c'e tra `import statistiche` e `from statistiche import media`? Quando preferiresti l'uno o l'altro?
5. Cosa fa il blocco `if __name__ == "__main__"` e perche e utile?
6. Nell'espressione `sorted(dati, key=lambda x: x["voto"])`, cosa rappresenta la lambda? Potresti riscriverla come funzione normale?
7. Perche `assert` e utile durante lo sviluppo ma non deve essere usato per la validazione dell'input in produzione?

---

## Osservazioni finali

In questo laboratorio avete fatto un salto di qualita nel vostro modo di programmare: dal codice come sequenza di istruzioni al codice come **insieme di funzioni componibili e testabili**.

I tre principi chiave emersi sono:

1. **DRY (Don't Repeat Yourself):** se copiate e incollate codice, probabilmente vi serve una funzione.
2. **Testabilita:** una funzione ben scritta puo essere testata in isolamento con `assert`. Se non riuscite a testarla, probabilmente fa troppe cose.
3. **Modularita:** separare il codice in moduli rende il progetto gestibile anche quando cresce. Oggi avete un solo modulo con poche funzioni; in un progetto reale potreste averne decine.

La combinazione di type hints e docstring rende il codice auto-documentante: chi legge la firma della funzione capisce immediatamente cosa entra e cosa esce, senza dover leggere il corpo.

Nel prossimo laboratorio applicherete queste competenze alla lettura e scrittura di file, lavorando finalmente con dati esterni.
