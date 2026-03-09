# Lezione 11 — Liste e tuple

## Introduzione

Nelle lezioni precedenti avete già incontrato le liste: le avete usate per raccogliere voti, iterare con `for`, accumulare risultati. Ma finora le avete trattate come semplici contenitori, senza indagare come funzionano davvero. Questa lezione cambia prospettiva: le liste diventano l'oggetto di studio, non solo uno strumento.

Capire a fondo le liste significa capire come Python gestisce la memoria, cosa succede quando assegnate una lista a un'altra variabile, e perché certi errori sono così insidiosi. Accanto alle liste, introduciamo le **tuple** — sequenze immutabili che completano il quadro delle strutture dati sequenziali di Python.

Per chi studia statistica, liste e tuple sono il primo passo verso i vettori di dati: serie di osservazioni, campioni, sequenze temporali. Tutto ciò che vedrete in NumPy e Pandas ha le sue radici qui.

---

## Liste: sequenze ordinate e mutabili

Una lista è una **sequenza ordinata e mutabile** di elementi. "Ordinata" significa che gli elementi hanno una posizione (un indice); "mutabile" significa che potete aggiungere, rimuovere o modificare elementi dopo la creazione.

```python
temperature: list[float] = [18.5, 21.3, 19.7, 22.1, 20.4]
nomi: list[str] = ["Anna", "Marco", "Luca"]
mista: list[int | str] = [1, "due", 3]  # possibile, ma sconsigliato
vuota: list[float] = []
```

Le liste possono contenere qualsiasi tipo di oggetto, anche tipi diversi nella stessa lista. Tuttavia, nella pratica statistica lavorerete quasi sempre con liste omogenee — tutti `float`, tutti `int`, tutti `str` — e i type hint lo riflettono.

---

## Indicizzazione: perché si parte da 0

Ogni elemento di una lista ha un **indice** che ne identifica la posizione. In Python (e nella maggioranza dei linguaggi moderni), gli indici partono da **0**:

```python
voti: list[int] = [28, 30, 25, 27, 22]
#                   0   1   2   3   4

primo: int = voti[0]    # 28
secondo: int = voti[1]  # 30
ultimo: int = voti[4]   # 22
```

### Dijkstra e l'offset

Perché si parte da 0 e non da 1? La risposta ha radici profonde nell'informatica. Edsger W. Dijkstra, uno dei padri della disciplina, scrisse nel 1982 un celebre appunto intitolato *"Why numbering should start at zero"*. L'argomento è matematico: quando si vuole rappresentare una sequenza di N elementi naturali consecutivi, ci sono quattro modi di scrivere l'intervallo:

- a) 0 <= i < N
- b) 0 < i <= N
- c) 0 <= i <= N-1
- d) 0 < i < N+1

La convenzione (a) — intervallo semiaperto a sinistra chiuso e a destra aperto — ha due vantaggi decisivi: la **differenza tra gli estremi** dà esattamente il numero di elementi (N - 0 = N), e **due intervalli adiacenti** si concatenano naturalmente ([0, 5) e [5, 10) coprono [0, 10) senza buchi né sovrapposizioni). Questa è la stessa ragione per cui `range(5)` produce 0, 1, 2, 3, 4.

Ma c'è anche una ragione più concreta. L'indice rappresenta un **offset** (spiazzamento) rispetto all'inizio della sequenza in memoria: il primo elemento ha offset 0 (è *all'inizio*), il secondo ha offset 1 (è *spostato di una posizione*), e così via. Se il primo elemento avesse indice 1, il calcolatore dovrebbe sottrarre 1 ogni volta per trovare la posizione in memoria — un'operazione inutile.

All'inizio sembra innaturale, ma dopo poche settimane diventa seconda natura. Un consiglio: pensate agli indici come a "quanti elementi devo saltare per arrivare a quello che voglio". Il primo elemento richiede 0 salti.

### Indici negativi

Python offre una scorciatoia elegante: gli **indici negativi** contano dalla fine della lista:

```python
voti: list[int] = [28, 30, 25, 27, 22]

ultimo: int = voti[-1]       # 22
penultimo: int = voti[-2]    # 27
primo: int = voti[-len(voti)]  # 28 (equivale a voti[0])
```

L'indice `-1` è l'ultimo elemento, `-2` il penultimo, e così via. Questo è molto comodo quando vi serve l'ultimo elemento senza sapere la lunghezza della lista. Internamente, Python calcola `voti[-1]` come `voti[len(voti) - 1]`, cioè `voti[4]`.

Se provate ad accedere a un indice che non esiste, Python solleva un errore:

```python
voti: list[int] = [28, 30, 25]
voti[10]   # IndexError: list index out of range
voti[-10]  # IndexError: list index out of range
```

---

## Slicing: estrarre sottoliste

Lo **slicing** (affettamento) permette di estrarre una porzione di lista specificando un intervallo di indici. La sintassi è `lista[start:stop:step]`:

```python
dati: list[int] = [10, 20, 30, 40, 50, 60, 70, 80]
#                   0   1   2   3   4   5   6   7

dati[2:5]      # [30, 40, 50]  — da indice 2 a 4 (stop escluso!)
dati[:3]       # [10, 20, 30]  — dall'inizio a indice 2
dati[5:]       # [60, 70, 80]  — da indice 5 alla fine
dati[:]        # [10, 20, 30, 40, 50, 60, 70, 80]  — copia completa
dati[::2]      # [10, 30, 50, 70]  — un elemento ogni due
dati[1::2]     # [20, 40, 60, 80]  — gli elementi in posizione dispari
dati[::-1]     # [80, 70, 60, 50, 40, 30, 20, 10]  — lista invertita
```

Notate che `stop` è sempre **escluso**, coerentemente con la convenzione dell'intervallo semiaperto vista per `range()`. Se `start` è omesso vale 0 (inizio); se `stop` è omesso vale la lunghezza della lista (fine); se `step` è omesso vale 1.

Una proprietà utile dello slicing: **non solleva mai `IndexError`**, anche se gli indici sono fuori range. Python li "taglia" silenziosamente:

```python
dati: list[int] = [10, 20, 30]
dati[1:100]   # [20, 30]  — nessun errore
dati[100:200] # []         — lista vuota
```

---

## Operazioni sulle liste

### Concatenazione e ripetizione

```python
a: list[int] = [1, 2, 3]
b: list[int] = [4, 5, 6]

c: list[int] = a + b        # [1, 2, 3, 4, 5, 6] — concatenazione
d: list[int] = a * 3        # [1, 2, 3, 1, 2, 3, 1, 2, 3] — ripetizione
```

La concatenazione crea una **nuova lista**; le liste originali restano invariate. Lo stesso vale per la ripetizione.

### Appartenenza e lunghezza

```python
voti: list[int] = [28, 30, 25, 27]

30 in voti      # True
18 in voti      # False
18 not in voti  # True
len(voti)       # 4
```

L'operatore `in` controlla se un valore è presente nella lista. `len()` restituisce il numero di elementi.

---

## Metodi delle liste

Le liste sono **oggetti**, e come tali hanno **metodi** — funzioni associate all'oggetto che ne modificano il contenuto o ne restituiscono informazioni. Ecco i principali.

### Aggiungere elementi

```python
voti: list[int] = [28, 30, 25]

voti.append(27)          # [28, 30, 25, 27] — aggiunge in fondo
voti.insert(1, 29)       # [28, 29, 30, 25, 27] — inserisce alla posizione 1
voti.extend([22, 24])    # [28, 29, 30, 25, 27, 22, 24] — aggiunge più elementi
```

`append()` aggiunge **un** elemento in coda. `insert(i, x)` inserisce `x` alla posizione `i`, spostando gli elementi successivi. `extend()` aggiunge **tutti** gli elementi di un'altra sequenza (equivale a `+=`).

Attenzione a non confondere `append()` con `extend()`:

```python
a: list[int] = [1, 2, 3]
a.append([4, 5])   # [1, 2, 3, [4, 5]] — ha aggiunto UNA lista come elemento!

b: list[int] = [1, 2, 3]
b.extend([4, 5])   # [1, 2, 3, 4, 5] — ha aggiunto DUE elementi
```

### Rimuovere elementi

```python
voti: list[int] = [28, 30, 25, 27, 30]

voti.remove(30)     # [28, 25, 27, 30] — rimuove la PRIMA occorrenza
ultimo: int = voti.pop()     # ultimo = 30, voti = [28, 25, 27]
secondo: int = voti.pop(1)   # secondo = 25, voti = [28, 27]
```

`remove(x)` cerca il valore `x` e rimuove la prima occorrenza; se non lo trova, solleva `ValueError`. `pop()` rimuove e **restituisce** l'ultimo elemento (o quello all'indice specificato).

### Ordinare e invertire

```python
voti: list[int] = [28, 30, 25, 27, 22]

voti.sort()              # [22, 25, 27, 28, 30] — ordina IN PLACE
voti.sort(reverse=True)  # [30, 28, 27, 25, 22] — ordine decrescente
voti.reverse()           # [22, 25, 27, 28, 30] — inverte l'ordine
```

**Attenzione**: `sort()` e `reverse()` modificano la lista **in place** e restituiscono `None`. Non scrivete `voti = voti.sort()` — perdereste la lista e otterreste `None`. Se volete una nuova lista ordinata senza modificare l'originale, usate la funzione built-in `sorted()`:

```python
voti: list[int] = [28, 30, 25, 27, 22]
voti_ordinati: list[int] = sorted(voti)  # voti resta invariata
```

### Cercare e contare

```python
voti: list[int] = [28, 30, 25, 27, 30]

voti.index(30)    # 1 — posizione della PRIMA occorrenza
voti.count(30)    # 2 — quante volte appare 30
```

`index(x)` restituisce la posizione della prima occorrenza di `x`; se non lo trova, solleva `ValueError`. `count(x)` restituisce quante volte `x` appare nella lista.

---

## Riferimenti e copie: il concetto cruciale

Questa è la sezione più importante della lezione. Se non la capite bene, vi ritroverete con bug misteriosi che corrompono i vostri dati senza che ve ne accorgiate.

### L'assegnamento crea un alias, non una copia

Quando scrivete `b = a` con una lista, **non** state creando una copia. State creando un **alias**: un secondo nome per lo stesso oggetto in memoria.

```python
a: list[int] = [1, 2, 3]
b: list[int] = a           # b è un ALIAS di a, non una copia

b.append(4)
print(a)  # [1, 2, 3, 4] — SORPRESA! Anche a è cambiata!
```

Per capire cosa succede, bisogna pensare a come Python gestisce la memoria. Immaginate la memoria del computer come un grande magazzino con scaffali numerati. Quando create `a = [1, 2, 3]`, Python:

1. Costruisce la lista `[1, 2, 3]` da qualche parte nel magazzino.
2. Attacca l'etichetta `a` a quello scaffale.

Quando poi scrivete `b = a`, Python:

3. Attacca una **seconda etichetta** `b` allo **stesso scaffale**.

Non c'è nessuna copia. C'è un solo oggetto con due nomi. Qualsiasi modifica attraverso `b` è visibile anche attraverso `a`, perché puntano allo stesso posto.

Potete verificarlo con `id()`, che restituisce l'indirizzo dell'oggetto in memoria, e con `is`, che confronta le identità (non i valori):

```python
a: list[int] = [1, 2, 3]
b: list[int] = a

print(id(a))       # es. 140234567890
print(id(b))       # 140234567890 — stesso indirizzo!
print(a is b)      # True — stesso oggetto
```

Ecco un diagramma in memoria (ASCII art) che mostra la situazione:

```
 Variabile     Memoria
 ┌───┐        ┌───────────┐
 │ a │───────>│ [1, 2, 3] │
 └───┘   ┌──>│           │
 ┌───┐   │   └───────────┘
 │ b │───┘
 └───┘
```

Entrambe le frecce puntano allo stesso oggetto. Se modificate l'oggetto tramite `b`, vedrete la modifica anche da `a`.

### Shallow copy: copiare il primo livello

Per creare una vera copia, avete diverse opzioni:

```python
a: list[int] = [1, 2, 3]

b: list[int] = a.copy()    # metodo copy()
c: list[int] = a[:]        # slicing completo
d: list[int] = list(a)     # costruttore list()
```

Ora `b`, `c` e `d` sono **oggetti indipendenti**: modificarli non modifica `a`.

```python
a: list[int] = [1, 2, 3]
b: list[int] = a.copy()

b.append(4)
print(a)  # [1, 2, 3] — a è rimasta invariata
print(b)  # [1, 2, 3, 4]

print(a is b)  # False — oggetti diversi
```

In memoria:

```
 Variabile     Memoria
 ┌───┐        ┌───────────┐
 │ a │───────>│ [1, 2, 3] │
 └───┘        └───────────┘
 ┌───┐        ┌───────────┐
 │ b │───────>│ [1, 2, 3] │  (copia indipendente)
 └───┘        └───────────┘
```

### Deep copy: il caso delle strutture annidate

Ma c'è un tranello. La `copy()` è una **shallow copy** (copia superficiale): copia i riferimenti agli elementi, non gli elementi stessi. Con una lista di interi non è un problema, perché gli interi sono immutabili. Ma con una **lista di liste**:

```python
matrice: list[list[int]] = [[1, 2], [3, 4], [5, 6]]
copia: list[list[int]] = matrice.copy()  # shallow copy

copia[0][0] = 99
print(matrice)  # [[99, 2], [3, 4], [5, 6]] — MODIFICATA!
```

La shallow copy ha creato una nuova lista esterna, ma le liste interne sono ancora **condivise**:

```
 Variabile       Memoria
 ┌─────────┐    ┌────────────────────┐
 │ matrice  │──> │ [ ref0, ref1, ref2 ] │
 └─────────┘    └──┬──────┬──────┬───┘
                   │      │      │
 ┌─────────┐    ┌──┼──────┼──────┼───┐
 │ copia    │──> │ [ ref0, ref1, ref2 ] │  (stessi riferimenti interni!)
 └─────────┘    └──┬──────┬──────┬───┘
                   │      │      │
                   v      v      v
                [1,2]  [3,4]  [5,6]
```

Per copiare **tutto**, compresi gli oggetti annidati, serve `copy.deepcopy()`:

```python
import copy

matrice: list[list[int]] = [[1, 2], [3, 4], [5, 6]]
copia_profonda: list[list[int]] = copy.deepcopy(matrice)

copia_profonda[0][0] = 99
print(matrice)  # [[1, 2], [3, 4], [5, 6]] — intatta!
```

### Perché è importante per la statistica

Immaginate di avere un dataset (rappresentato come lista di liste) e di voler "provare" una trasformazione senza alterare i dati originali:

```python
import copy

dati_originali: list[list[float]] = [
    [1.2, 3.4, 5.6],
    [7.8, 9.0, 1.2],
]

# SBAGLIATO: modifica anche dati_originali
dati_lavoro: list[list[float]] = dati_originali
dati_lavoro[0][0] = 0.0  # dati_originali[0][0] è ora 0.0!

# ANCORA SBAGLIATO con liste annidate: shallow copy
dati_lavoro = dati_originali.copy()
dati_lavoro[0][0] = 0.0  # dati_originali[0][0] è ancora modificato!

# CORRETTO
dati_lavoro = copy.deepcopy(dati_originali)
dati_lavoro[0][0] = 0.0  # dati_originali resta intatta
```

Regola pratica: se la lista contiene solo tipi immutabili (int, float, str, tuple), basta `copy()`. Se contiene oggetti mutabili (altre liste, dizionari), serve `deepcopy()`.

---

## Tuple: sequenze ordinate e immutabili

Le **tuple** sono simili alle liste, ma con una differenza fondamentale: sono **immutabili**. Una volta create, non potete aggiungere, rimuovere o modificare i loro elementi.

```python
coordinate: tuple[float, float] = (45.4642, 9.1900)  # Milano
giorni: tuple[str, ...] = ("lun", "mar", "mer", "gio", "ven", "sab", "dom")
singolo: tuple[int] = (42,)   # la virgola è necessaria per tuple con un elemento!
vuota: tuple[()] = ()
```

Notate i type hint: `tuple[float, float]` indica una tupla di esattamente due float (posizione fissa); `tuple[str, ...]` indica una tupla di lunghezza arbitraria con tutti elementi `str`.

L'indicizzazione e lo slicing funzionano come per le liste:

```python
coordinate: tuple[float, float] = (45.4642, 9.1900)
lat: float = coordinate[0]     # 45.4642
lon: float = coordinate[-1]    # 9.1900
```

Ma il tentativo di modifica fallisce:

```python
coordinate[0] = 41.9028  # TypeError: 'tuple' object does not support item assignment
```

### Perché esistono le tuple?

Se le liste possono fare tutto ciò che fanno le tuple (e di più), perché esistono le tuple? Tre motivi.

**1. Garanzia di immutabilità.** Quando passate una tupla a una funzione, avete la certezza che la funzione non potrà modificare i dati. Questo rende il codice più sicuro e facile da ragionare. È un contratto: "questi dati non cambieranno".

```python
def distanza_da_origine(punto: tuple[float, float]) -> float:
    """Non può modificare il punto — è una tupla."""
    return (punto[0] ** 2 + punto[1] ** 2) ** 0.5
```

**2. Hashabilità.** Le tuple (purché contengano solo elementi immutabili) sono *hashable*, cioè possono essere usate come chiavi di dizionario o elementi di un insieme (`set`). Le liste no.

```python
# Le tuple possono essere chiavi di dizionario
posizioni: dict[tuple[int, int], str] = {
    (0, 0): "origine",
    (1, 0): "destra",
    (0, 1): "sopra",
}

# Le liste NO
# {[0, 0]: "origine"}  # TypeError: unhashable type: 'list'
```

Questo è fondamentale quando dovrete contare combinazioni, creare tabelle di contingenza, o usare coordinate come chiavi.

**3. Efficienza.** Le tuple occupano meno memoria delle liste e sono leggermente più veloci da creare e accedere. Per dati che non devono cambiare, sono la scelta appropriata.

---

## Unpacking: assegnamento multiplo

L'**unpacking** (spacchettamento) permette di assegnare gli elementi di una tupla (o lista) a variabili separate in un'unica istruzione:

```python
coordinate: tuple[float, float] = (45.4642, 9.1900)
lat, lon = coordinate  # lat = 45.4642, lon = 9.1900

# Funziona anche con le liste
valori: list[int] = [10, 20, 30]
a, b, c = valori  # a = 10, b = 20, c = 30
```

Il numero di variabili a sinistra deve corrispondere al numero di elementi a destra, altrimenti si ottiene un `ValueError`.

### Return multipli dalle funzioni

L'unpacking è particolarmente utile con le funzioni che restituiscono più valori. In Python, una funzione può restituire una tupla, e il chiamante la spacchetta:

```python
def statistiche_base(valori: list[float]) -> tuple[float, float, float]:
    """Restituisce media, minimo e massimo."""
    n: int = len(valori)
    media: float = sum(valori) / n
    minimo: float = min(valori)
    massimo: float = max(valori)
    return media, minimo, massimo  # Python crea automaticamente una tupla

# Unpacking del risultato
dati: list[float] = [23.5, 21.0, 25.3, 19.8, 22.1]
media, minimo, massimo = statistiche_base(dati)
print(f"Media: {media:.1f}, Range: [{minimo}, {massimo}]")
# Media: 22.3, Range: [19.8, 25.3]
```

Notate che `return media, minimo, massimo` crea implicitamente la tupla `(media, minimo, massimo)`. Le parentesi sono opzionali nella maggior parte dei contesti.

### Scambio di variabili

L'unpacking rende elegante lo scambio di due variabili, che in molti linguaggi richiede una variabile temporanea:

```python
a: int = 10
b: int = 20

# In C: temp = a; a = b; b = temp;
# In Python:
a, b = b, a  # a = 20, b = 10
```

Python crea la tupla `(b, a)` = `(20, 10)` a destra, poi la spacchetta nelle variabili a sinistra. Semplice ed elegante.

---

## Named tuple (cenni)

Quando le tuple hanno molti elementi, ricordare quale posizione corrisponde a quale dato diventa difficile. Le **named tuple** risolvono questo problema aggiungendo nomi ai campi:

```python
from collections import namedtuple

Studente = namedtuple("Studente", ["nome", "matricola", "media"])

s: Studente = Studente(nome="Anna Rossi", matricola=123456, media=27.5)

# Accesso per nome (più leggibile)
print(s.nome)      # Anna Rossi
print(s.media)     # 27.5

# Accesso per indice (ancora possibile)
print(s[0])        # Anna Rossi

# Immutabile come una tupla normale
# s.media = 28.0   # AttributeError!
```

Le named tuple sono un ponte tra le tuple e le classi: offrono la chiarezza di campi con nome mantenendo l'immutabilità e l'efficienza delle tuple. Le approfondiremo quando parleremo di classi e oggetti; per ora, sappiate che esistono e che sono utili quando una tupla ha più di due o tre elementi.

Una versione moderna è `typing.NamedTuple`, che si integra meglio con i type hint:

```python
from typing import NamedTuple

class Osservazione(NamedTuple):
    valore: float
    unita: str
    timestamp: str

o: Osservazione = Osservazione(valore=23.5, unita="°C", timestamp="2025-01-15")
print(o.valore)  # 23.5
```

---

## Applicazioni statistiche

### Liste di osservazioni

La struttura dati più naturale per un campione statistico è una lista di numeri:

```python
campione: list[float] = [23.5, 21.0, 25.3, 19.8, 22.1, 24.7, 20.5]

n: int = len(campione)
media: float = sum(campione) / n

# Varianza campionaria (con n-1 al denominatore)
somma_scarti_quadrati: float = sum((x - media) ** 2 for x in campione)
varianza: float = somma_scarti_quadrati / (n - 1)

# Ordinamento per calcolare la mediana
campione_ordinato: list[float] = sorted(campione)
if n % 2 == 1:
    mediana: float = campione_ordinato[n // 2]
else:
    mediana = (campione_ordinato[n // 2 - 1] + campione_ordinato[n // 2]) / 2

print(f"n = {n}")
print(f"Media = {media:.2f}")
print(f"Varianza campionaria = {varianza:.2f}")
print(f"Mediana = {mediana:.2f}")
```

Notate l'uso di `sorted()` (che crea una nuova lista) anziché `sort()` (che modifica l'originale). Preservare i dati originali nell'ordine di raccolta è una buona pratica.

### Serie di misurazioni con tuple

Quando ogni osservazione ha più attributi (valore, momento, condizioni), le tuple sono la scelta naturale:

```python
from typing import NamedTuple

class Misurazione(NamedTuple):
    temperatura: float
    umidita: float
    ora: str

rilevamenti: list[Misurazione] = [
    Misurazione(18.5, 65.0, "08:00"),
    Misurazione(22.3, 55.0, "12:00"),
    Misurazione(25.1, 48.0, "15:00"),
    Misurazione(20.7, 62.0, "18:00"),
]

# Estrarre solo le temperature
temperature: list[float] = [m.temperatura for m in rilevamenti]
media_temp: float = sum(temperature) / len(temperature)
print(f"Temperatura media: {media_temp:.1f}°C")

# Trovare il rilevamento con temperatura massima
piu_caldo: Misurazione = max(rilevamenti, key=lambda m: m.temperatura)
print(f"Picco: {piu_caldo.temperatura}°C alle {piu_caldo.ora}")
```

### Frequenze con liste e conteggio

```python
def distribuzione_frequenze(dati: list[int]) -> list[tuple[int, int]]:
    """Restituisce coppie (valore, frequenza) ordinate per valore."""
    valori_unici: list[int] = sorted(set(dati))
    frequenze: list[tuple[int, int]] = []
    for valore in valori_unici:
        freq: int = dati.count(valore)
        frequenze.append((valore, freq))
    return frequenze

voti_esame: list[int] = [25, 28, 30, 28, 27, 25, 30, 30, 28, 22, 25, 27]
for voto, freq in distribuzione_frequenze(voti_esame):
    print(f"Voto {voto}: {'█' * freq} ({freq})")
```

---

## Domande di verifica

1. **Perché in Python gli indici partono da 0?** Spiegate sia la motivazione matematica (Dijkstra) sia quella pratica (offset in memoria).

2. **Cosa restituisce `lista[2:2]`?** E `lista[2:3]`? Perché?

3. **Qual è la differenza tra `append()` e `extend()`?** Cosa succede se scrivete `a.append([4, 5])` invece di `a.extend([4, 5])`?

4. **Perché `voti = voti.sort()` è un errore logico?** Cosa contiene `voti` dopo questa istruzione?

5. **Dopo `a = [1, 2, 3]` e `b = a`, la modifica `b[0] = 99` cambia anche `a`?** Perché? Disegnate un diagramma in memoria.

6. **Quando serve `copy.deepcopy()` invece di `copy()` o slicing?** Fate un esempio con una lista di liste.

7. **Elencate tre motivi per cui esistono le tuple, nonostante le liste sembrino più versatili.**

8. **Cos'è l'unpacking e perché è utile quando una funzione restituisce più valori?**

---

## Esercizi

### Base

1. Create una lista con i primi 10 numeri naturali (da 0 a 9). Usando lo slicing, estraete: i numeri pari, i numeri dispari, la lista invertita, i primi 5 elementi, gli ultimi 3 elementi.

2. Scrivete una funzione `rimuovi_duplicati(valori: list[int]) -> list[int]` che restituisce una nuova lista senza duplicati, mantenendo l'ordine originale. Non usate `set()`.

3. Data una lista di voti `[28, 30, 25, 18, 27, 30, 22, 15, 28, 26]`, usate i metodi delle liste per: contare quanti 30 ci sono, trovare la posizione del primo 25, ordinare la lista in ordine decrescente (senza modificare l'originale), rimuovere tutti i voti insufficienti (< 18).

### Intermedio

4. Scrivete una funzione `mediana(valori: list[float]) -> float` che calcola la mediana di una lista. Attenzione: non modificate la lista originale.

5. Scrivete una funzione `quartili(valori: list[float]) -> tuple[float, float, float]` che restituisce il primo quartile (Q1), la mediana (Q2) e il terzo quartile (Q3). Usate l'unpacking per assegnare i risultati.

6. Dimostrate la differenza tra alias, shallow copy e deep copy con un programma che:
   - crea una lista di liste (es. `[[1, 2], [3, 4]]`)
   - crea un alias, una shallow copy e una deep copy
   - modifica un elemento della lista interna nella deep copy
   - stampa tutte e quattro le versioni mostrando quale è stata modificata e quale no

### Avanzato

7. Scrivete una funzione `normalizza(valori: list[float]) -> list[float]` che restituisce una nuova lista in cui ogni valore e' stato trasformato con la normalizzazione z-score: z = (x - media) / deviazione_standard. Calcolate media e deviazione standard manualmente (senza librerie).

8. Implementate una funzione `tabella_contingenza(var1: list[str], var2: list[str]) -> dict[tuple[str, str], int]` che, date due liste di variabili categoriali della stessa lunghezza, restituisce un dizionario dove le chiavi sono tuple `(valore_var1, valore_var2)` e i valori sono le frequenze congiunte. Testatela con dati inventati (es. genere e preferenza).

   ```python
   genere: list[str] = ["M", "F", "F", "M", "F", "M", "M", "F"]
   sport: list[str] = ["calcio", "tennis", "tennis", "calcio", "nuoto", "nuoto", "calcio", "tennis"]

   tabella: dict[tuple[str, str], int] = tabella_contingenza(genere, sport)
   # Dovrebbe produrre: {("M", "calcio"): 2, ("F", "tennis"): 3, ...}
   ```

---

## Osservazioni finali

Liste e tuple sono i mattoni fondamentali per gestire collezioni di dati in Python. La distinzione tra le due non e' un dettaglio sintattico: riflette una scelta progettuale precisa. Usate le liste quando i dati devono crescere, ridursi o cambiare; usate le tuple quando i dati rappresentano un record fisso (una coordinata, una data, un risultato di funzione).

Il concetto di **riferimento** e **alias** e' probabilmente l'idea piu' importante di questa lezione. Quasi tutti i bug piu' difficili da trovare nei programmi di analisi dati derivano da modifiche accidentali a strutture condivise. La regola e' semplice: se dovete lavorare su una copia, createla esplicitamente.

Due osservazioni per il futuro:

1. **NumPy e Pandas** sostituiranno le liste per il lavoro numerico serio. Ma capire come funzionano le liste vi permette di capire cosa succede "sotto il cofano" di quelle librerie — e di riconoscere quando un bug dipende dalla struttura dati e quando dal calcolo.

2. **L'unpacking e le tuple** diventeranno ancora piu' utili quando vedrete le funzioni in dettaglio. Restituire piu' valori come tupla e spacchettarli nel chiamante e' un idioma Python cosi' frequente che diventa seconda natura.

Nella prossima lezione esploreremo i **dizionari e gli insiemi** — strutture dati che non si basano sull'ordine posizionale ma su chiavi e appartenenza, aprendo la porta a un modo completamente diverso di organizzare i dati.
