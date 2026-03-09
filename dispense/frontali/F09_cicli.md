# Lezione Frontale 9 — Cicli

## Introduzione

Con variabili, operatori e condizionali, i vostri programmi sanno memorizzare dati, calcolare e decidere. Ma manca ancora un ingrediente fondamentale: la **ripetizione**. Gran parte del lavoro in statistica consiste nel fare la stessa operazione su molti dati: calcolare la media di mille osservazioni, cercare un valore anomalo in un dataset, applicare una trasformazione a ogni riga di una tabella.

I cicli permettono di ripetere un blocco di codice senza doverlo riscrivere. Con variabili, condizioni e cicli avete i tre pilastri della programmazione imperativa — tutto il resto è costruito su questi.

---

## Il ciclo `for`

Il `for` in Python è un **ciclo di iterazione**: scorre gli elementi di una sequenza (lista, stringa, range, qualsiasi *iterabile*), uno alla volta, eseguendo un blocco di codice per ciascun elemento.

```python
voti: list[int] = [28, 30, 25, 27, 22]

for voto in voti:
    print(f"Voto: {voto}")
```

Ad ogni iterazione, la variabile `voto` assume il valore dell'elemento successivo della lista. Quando gli elementi finiscono, il ciclo termina.

### `range()`: generare sequenze di numeri

Quando serve un ciclo che si ripete un certo numero di volte, si usa `range()`:

```python
# range(stop): da 0 a stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop): da start a stop-1
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# range(start, stop, step): con passo
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Contare all'indietro
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

**Perché `stop` è escluso?** Per due motivi:
1. **Coerenza con l'indicizzazione da 0:** `range(n)` produce esattamente `n` elementi (da 0 a n-1), come gli indici di una lista di lunghezza `n`.
2. **Intervalli concatenabili:** `range(0, 5)` e `range(5, 10)` coprono insieme `range(0, 10)` senza sovrapposizioni.

È una convenzione matematica (intervallo semiaperto [start, stop)) che all'inizio sembra innaturale, ma diventa rapidamente intuitiva.

### `enumerate()`: indice e valore insieme

Spesso serve sia l'indice che il valore. Il modo sbagliato:

```python
# MALE: anti-pattern C-style
nomi: list[str] = ["Anna", "Marco", "Luca"]
for i in range(len(nomi)):
    print(f"{i}: {nomi[i]}")
```

Il modo pythonic:

```python
# BENE: enumerate
nomi: list[str] = ["Anna", "Marco", "Luca"]
for i, nome in enumerate(nomi):
    print(f"{i}: {nome}")

# Con indice iniziale diverso
for i, nome in enumerate(nomi, start=1):
    print(f"{i}. {nome}")  # 1. Anna, 2. Marco, 3. Luca
```

### `zip()`: iterare su più sequenze in parallelo

```python
nomi: list[str] = ["Anna", "Marco", "Luca"]
voti: list[int] = [28, 30, 25]

for nome, voto in zip(nomi, voti):
    print(f"{nome}: {voto}")
# Anna: 28
# Marco: 30
# Luca: 25
```

`zip()` si ferma alla sequenza più corta. Se le lunghezze sono diverse e non volete perdere dati, usate `itertools.zip_longest`.

---

## Il ciclo `while`

Il `while` ripete un blocco **finché una condizione è vera**. Si usa quando non si sa in anticipo quante iterazioni servono.

```python
risposta: str = ""
while risposta != "esci":
    risposta = input("Inserisci un comando (o 'esci'): ")
    print(f"Hai scritto: {risposta}")
```

### Il pericolo del ciclo infinito

Se la condizione non diventa mai falsa, il ciclo non termina mai:

```python
# ATTENZIONE: ciclo infinito!
x: int = 1
while x > 0:
    x += 1  # x cresce sempre, la condizione è sempre vera
```

Per interrompere un ciclo infinito: `Ctrl+C` nel terminale. Ma meglio: progettate correttamente la condizione di uscita.

### `break` e `continue`

**`break`**: esce immediatamente dal ciclo.

```python
# Cercare un valore
dati: list[int] = [4, 7, 2, 9, 1, 8]
obiettivo: int = 9

for dato in dati:
    if dato == obiettivo:
        print(f"Trovato: {dato}")
        break
```

**`continue`**: salta il resto del corpo e passa all'iterazione successiva.

```python
# Elaborare solo i valori positivi
valori: list[float] = [3.5, -1.2, 4.0, -0.5, 2.1]

for valore in valori:
    if valore < 0:
        continue  # salta i negativi
    print(f"Elaboro: {valore}")
```

### Il pattern `while True + break`

Quando la condizione di uscita è nel mezzo del ciclo, non all'inizio:

```python
while True:
    risposta: str = input("Inserisci un numero positivo (0 per uscire): ")
    numero: int = int(risposta)
    if numero == 0:
        break
    print(f"Il quadrato è {numero ** 2}")
```

### `for` vs `while`: quando usare quale

- **`for`**: quando iterate su una collezione (lista, stringa, range) o sapete quante iterazioni servono. Nel **90% dei casi** in Python, `for` è la scelta giusta.
- **`while`**: quando la terminazione dipende da una condizione che cambia durante l'esecuzione (input utente, convergenza di un algoritmo, ricerca).

---

## Cicli annidati

Un ciclo dentro un altro ciclo:

```python
# Tavola pitagorica
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4d}", end="")
    print()  # a capo dopo ogni riga
```

I cicli annidati sono necessari per lavorare con strutture bidimensionali (matrici, tabelle). Ma **attenzione alla complessità**: un ciclo annidato con n iterazioni ciascuno esegue n² operazioni. Con tre cicli, n³. Se n è grande, il tempo di esecuzione esplode.

---

## Pattern comuni

### Pattern accumulatore

Accumulare un valore (somma, prodotto, concatenazione):

```python
voti: list[int] = [28, 30, 25, 27, 22]

somma: int = 0
for voto in voti:
    somma += voto

media: float = somma / len(voti)
print(f"Media: {media:.2f}")
```

### Pattern contatore

Contare gli elementi che soddisfano una condizione:

```python
voti: list[int] = [28, 30, 25, 27, 22, 15, 12]

sufficienze: int = 0
for voto in voti:
    if voto >= 18:
        sufficienze += 1

print(f"Sufficienze: {sufficienze} su {len(voti)}")
```

### Pattern ricerca

Trovare un elemento specifico:

```python
def contiene(lista: list[int], obiettivo: int) -> bool:
    """Verifica se obiettivo è presente nella lista."""
    for elemento in lista:
        if elemento == obiettivo:
            return True
    return False
```

### Pattern filtro

Selezionare gli elementi che soddisfano un criterio:

```python
voti: list[int] = [28, 30, 25, 27, 22, 15, 12]

sufficienti: list[int] = []
for voto in voti:
    if voto >= 18:
        sufficienti.append(voto)

print(f"Voti sufficienti: {sufficienti}")
```

### Pattern min/max

Trovare il minimo o il massimo:

```python
def trova_massimo(valori: list[float]) -> float:
    """Trova il valore massimo nella lista."""
    if not valori:
        raise ValueError("Lista vuota")

    massimo: float = valori[0]  # inizializza col primo elemento
    for valore in valori[1:]:   # scorre dal secondo in poi
        if valore > massimo:
            massimo = valore
    return massimo
```

(Python ha `max()` e `min()` built-in, ma è istruttivo capire come funzionano.)

### Esempio completo: statistiche descrittive

```python
def statistiche(valori: list[float]) -> dict[str, float]:
    """Calcola statistiche descrittive base."""
    n: int = len(valori)
    if n == 0:
        raise ValueError("Lista vuota")

    # Media
    somma: float = 0.0
    for v in valori:
        somma += v
    media: float = somma / n

    # Varianza
    somma_scarti_quadrati: float = 0.0
    for v in valori:
        somma_scarti_quadrati += (v - media) ** 2
    varianza: float = somma_scarti_quadrati / n

    # Min e max
    minimo: float = valori[0]
    massimo: float = valori[0]
    for v in valori[1:]:
        if v < minimo:
            minimo = v
        if v > massimo:
            massimo = v

    return {
        "n": n,
        "media": media,
        "varianza": varianza,
        "minimo": minimo,
        "massimo": massimo
    }

# Test
dati: list[float] = [23.5, 21.0, 25.3, 19.8, 22.1]
risultati: dict[str, float] = statistiche(dati)
for chiave, valore in risultati.items():
    print(f"{chiave}: {valore:.2f}")
```

Più avanti vedremo che NumPy fa tutto questo in una riga (`np.mean()`, `np.var()`, ecc.) — ma è fondamentale capire cosa succede *sotto*.

---

## Domande di verifica

1. **Qual è la differenza tra `for` e `while`?** Quando usare l'uno o l'altro?

2. **Perché `range(5)` produce i numeri da 0 a 4 e non da 0 a 5?**

3. **Cos'è `enumerate()` e perché è preferibile a `range(len(lista))`?**

4. **Cosa fanno `break` e `continue`?** Quale interrompe il ciclo e quale salta un'iterazione?

5. **Cos'è un ciclo infinito?** Come si evita? Come si interrompe se si verifica?

6. **Spiegate il pattern accumulatore con un esempio diverso da quelli del testo.**

7. **Perché i cicli annidati possono essere un "segnale di allarme"?**

8. **Nell'esempio della funzione `statistiche()`, perché si inizializza `minimo` con `valori[0]` e non con `0`?**

---

## Esercizi

### Base

1. Scrivete un programma che stampa i numeri da 1 a 100. Accanto a ogni multiplo di 3, stampate "Fizz"; accanto a ogni multiplo di 5, "Buzz"; accanto a ogni multiplo di 15, "FizzBuzz".

2. Scrivete un programma che legge numeri dall'utente (con `while`) fino a quando l'utente inserisce 0, e poi stampa la somma di tutti i numeri inseriti.

3. Usate `enumerate()` per stampare una lista di nomi numerata:
   ```
   1. Anna
   2. Marco
   3. Luca
   ```

### Intermedio

4. Scrivete una funzione `calcola_media_mobile(valori: list[float], finestra: int) -> list[float]` che calcola la media mobile di una lista con una data finestra temporale.

5. Scrivete un programma che legge voti dall'utente uno alla volta (0 per terminare) e alla fine stampa: media, voto massimo, voto minimo, numero di sufficienze.

6. Scrivete una funzione che, data una lista di numeri, restituisce una nuova lista contenente solo i numeri primi presenti nella lista originale. (Suggerimento: scrivete prima una funzione `e_primo(n: int) -> bool`.)

### Avanzato

7. Scrivete una funzione `varianza_campionaria(valori: list[float]) -> float` che calcola la varianza campionaria (con n-1 al denominatore) senza usare funzioni built-in diverse da `len()`.

8. Implementate la **ricerca binaria**: data una lista **ordinata** e un valore obiettivo, trovate la posizione dell'obiettivo. Se non è presente, restituite -1. (Suggerimento: usate un `while` che dimezza lo spazio di ricerca ad ogni passo.)

   ```python
   def ricerca_binaria(lista: list[int], obiettivo: int) -> int:
       """Trova la posizione di obiettivo nella lista ordinata. Restituisce -1 se assente."""
       # Completate...

   # Test
   dati: list[int] = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
   assert ricerca_binaria(dati, 23) == 5
   assert ricerca_binaria(dati, 10) == -1
   ```

---

## Osservazioni finali

I cicli completano il trio fondamentale: **sequenza**, **selezione** (condizionali), **iterazione** (cicli). Questi tre costrutti, combinati con le variabili, sono sufficienti per esprimere qualsiasi algoritmo — è un risultato teorico noto come **teorema di Böhm-Jacopini** (1966).

Due lezioni pratiche:

1. **Riconoscete i pattern.** Accumulatore, contatore, ricerca, filtro, min/max — sono mattoni ricorrenti. Quando affrontate un problema, chiedetevi: "quale pattern serve qui?"

2. **La funzione `statistiche()` che abbiamo scritto** usa solo cicli e condizioni, eppure calcola media, varianza, minimo e massimo. Tra qualche lezione, vedremo che NumPy fa lo stesso con `np.mean()`, `np.var()`, `np.min()`, `np.max()`. Ma ora **capite cosa c'è dentro** quelle funzioni — non è magia, è un ciclo con un accumulatore.

Nella prossima lezione vedremo le **comprehension** — un modo elegante e conciso di esprimere i pattern filtro e trasformazione — e le **stringhe** come struttura dati.
