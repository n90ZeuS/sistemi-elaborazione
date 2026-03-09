# Laboratorio 3 — Strutture dati

## Informazioni

- **Prerequisiti:** Lezioni frontali T11 (Liste e tuple) e T12 (Dizionari e insiemi)
- **Durata stimata:** 2 ore
- **Obiettivi:** Saper creare, modificare e interrogare liste, tuple, dizionari e set. Capire la differenza tra alias e copia. Usare `Counter` per analisi di frequenza.

---

## Esercizio guidato 1 — Liste: gestire misurazioni

Immaginate di raccogliere le temperature giornaliere di una settimana. Le liste sono lo strumento naturale per questo tipo di dato: una sequenza ordinata e modificabile.

### Passo 1: Creare e popolare una lista

```python
# Creiamo una lista vuota e aggiungiamo misurazioni una alla volta
temperature: list[float] = []

temperature.append(18.5)
temperature.append(21.0)
temperature.append(19.3)
temperature.append(22.1)
temperature.append(20.7)

print(f"Misurazioni raccolte: {temperature}")
print(f"Numero di misurazioni: {len(temperature)}")
```

Possiamo anche creare la lista direttamente:

```python
temperature: list[float] = [18.5, 21.0, 19.3, 22.1, 20.7]
```

### Passo 2: Leggere (Read)

```python
# Accesso per indice
prima: float = temperature[0]
ultima: float = temperature[-1]
print(f"Prima misurazione: {prima}")
print(f"Ultima misurazione: {ultima}")

# Slicing: sottoinsieme di misurazioni
prime_tre: list[float] = temperature[:3]
print(f"Prime tre: {prime_tre}")

# Cercare un valore
if 21.0 in temperature:
    posizione: int = temperature.index(21.0)
    print(f"21.0 trovato alla posizione {posizione}")
```

### Passo 3: Aggiornare (Update)

```python
# Correggere una misurazione errata
print(f"Prima della correzione: {temperature}")
temperature[2] = 19.8  # la terza misurazione era sbagliata
print(f"Dopo la correzione:    {temperature}")

# Inserire una misurazione dimenticata in posizione specifica
temperature.insert(1, 20.0)  # inserisci 20.0 alla posizione 1
print(f"Dopo l'inserimento:    {temperature}")
```

### Passo 4: Cancellare (Delete)

```python
# Rimuovere l'ultima misurazione
rimossa: float = temperature.pop()
print(f"Rimossa l'ultima: {rimossa}, lista: {temperature}")

# Rimuovere per valore
temperature.remove(20.0)
print(f"Dopo remove(20.0): {temperature}")

# Rimuovere per indice
del temperature[0]
print(f"Dopo del [0]: {temperature}")
```

### Passo 5: Operazioni statistiche di base

```python
temperature: list[float] = [18.5, 21.0, 19.3, 22.1, 20.7, 17.9, 23.4]

media: float = sum(temperature) / len(temperature)
minima: float = min(temperature)
massima: float = max(temperature)

print(f"Media:   {media:.2f}")
print(f"Minima:  {minima}")
print(f"Massima: {massima}")

# Ordinamento (crea una nuova lista)
ordinate: list[float] = sorted(temperature)
print(f"Ordinate: {ordinate}")

# Ordinamento in-place (modifica la lista originale)
temperature.sort()
print(f"Originale dopo sort(): {temperature}")
```

---

## Esercizio guidato 2 — Alias vs copia: un esperimento fondamentale

Questo esperimento chiarisce una delle trappole più comuni per i principianti.

### Passo 1: Alias (due nomi, stesso oggetto)

```python
originale: list[int] = [1, 2, 3, 4, 5]
alias: list[int] = originale  # NON è una copia!

# Modifichiamo tramite alias
alias[0] = 999

print(f"alias:     {alias}")
print(f"originale: {originale}")  # Anche originale è cambiato!
print(f"Stesso oggetto? {originale is alias}")  # True
```

L'assegnamento `alias = originale` non crea una nuova lista: entrambi i nomi puntano allo stesso oggetto in memoria. Modificare l'uno significa modificare l'altro.

### Passo 2: Copia superficiale

```python
originale: list[int] = [1, 2, 3, 4, 5]
copia: list[int] = originale.copy()  # oppure list(originale) oppure originale[:]

copia[0] = 999

print(f"copia:     {copia}")
print(f"originale: {originale}")  # Originale NON è cambiato
print(f"Stesso oggetto? {originale is copia}")  # False
```

### Passo 3: Attenzione alle liste di liste

```python
matrice: list[list[int]] = [[1, 2], [3, 4]]
copia_superficiale: list[list[int]] = matrice.copy()

copia_superficiale[0][0] = 999

print(f"copia:    {copia_superficiale}")  # [[999, 2], [3, 4]]
print(f"matrice:  {matrice}")              # [[999, 2], [3, 4]] — anche qui!
```

La copia superficiale copia la lista esterna, ma le liste interne restano condivise. Per una copia completa servono `import copy` e `copy.deepcopy()`, ma per ora è sufficiente essere consapevoli del problema.

---

## Esercizio guidato 3 — Tuple: punti geografici e distanze

Le tuple sono come le liste, ma **immutabili**: una volta create, non si possono modificare. Sono perfette per dati che non devono cambiare, come coordinate geografiche.

### Passo 1: Creare tuple e fare unpacking

```python
import math

# Una tupla di coordinate (latitudine, longitudine)
roma: tuple[float, float] = (41.9028, 12.4964)
milano: tuple[float, float] = (45.4642, 9.1900)
napoli: tuple[float, float] = (40.8518, 14.2681)

# Unpacking: estrarre i valori in variabili separate
lat_roma, lon_roma = roma
print(f"Roma: lat={lat_roma}, lon={lon_roma}")

# Accesso per indice (come le liste)
print(f"Latitudine di Milano: {milano[0]}")
```

### Passo 2: Calcolare la distanza tra due punti

Usiamo la formula di Haversine semplificata (distanza in linea d'aria approssimata):

```python
def distanza_gradi(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """Calcola la distanza euclidea approssimata tra due punti in gradi."""
    lat1, lon1 = p1
    lat2, lon2 = p2
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)


citta: list[tuple[str, tuple[float, float]]] = [
    ("Roma", roma),
    ("Milano", milano),
    ("Napoli", napoli),
]

# Calcolare le distanze tra tutte le coppie
for i in range(len(citta)):
    for j in range(i + 1, len(citta)):
        nome_a, coord_a = citta[i]
        nome_b, coord_b = citta[j]
        d: float = distanza_gradi(coord_a, coord_b)
        print(f"{nome_a} — {nome_b}: {d:.4f} gradi")
```

### Passo 3: Tuple come chiavi di dizionario

Le tuple, essendo immutabili, possono essere usate come chiavi di dizionario (le liste no):

```python
# Distanze pre-calcolate tra coppie di città
distanze: dict[tuple[str, str], float] = {}
distanze[("Roma", "Milano")] = 4.77
distanze[("Roma", "Napoli")] = 2.10
distanze[("Milano", "Napoli")] = 6.52

coppia: tuple[str, str] = ("Roma", "Milano")
print(f"Distanza {coppia[0]}—{coppia[1]}: {distanze[coppia]:.2f} gradi")
```

---

## Esercizio guidato 4 — Dizionari: registro studenti

I dizionari associano **chiavi** a **valori**. Sono la struttura dati più usata quando serve un accesso rapido per nome o identificativo.

### Passo 1: Creare un registro

```python
# Ogni studente è identificato dalla matricola
registro: dict[str, dict[str, object]] = {
    "MAT001": {
        "nome": "Anna Rossi",
        "anno": 1,
        "voti": [28, 30, 25],
    },
    "MAT002": {
        "nome": "Marco Bianchi",
        "anno": 1,
        "voti": [24, 27, 30],
    },
    "MAT003": {
        "nome": "Luca Verdi",
        "anno": 2,
        "voti": [30, 30, 28],
    },
}
```

### Passo 2: Accesso e ricerca

```python
# Accesso diretto per matricola
studente: dict[str, object] = registro["MAT001"]
print(f"Nome: {studente['nome']}")

# Accesso sicuro con get (nessun errore se la chiave non esiste)
risultato: dict[str, object] | None = registro.get("MAT999")
print(f"MAT999 esiste? {risultato is not None}")

# Iterare su tutti gli studenti
for matricola, dati in registro.items():
    voti: list[int] = dati["voti"]
    media: float = sum(voti) / len(voti)
    print(f"{matricola} — {dati['nome']}: media {media:.1f}")
```

### Passo 3: Inserimento e aggiornamento

```python
# Aggiungere un nuovo studente
registro["MAT004"] = {
    "nome": "Sara Neri",
    "anno": 1,
    "voti": [26, 29],
}

# Aggiungere un voto a uno studente esistente
registro["MAT001"]["voti"].append(27)
print(f"Voti aggiornati di MAT001: {registro['MAT001']['voti']}")

# Aggiornare l'anno
registro["MAT003"]["anno"] = 3
```

### Passo 4: Cancellazione

```python
# Rimuovere uno studente
rimosso: dict[str, object] = registro.pop("MAT004")
print(f"Rimosso: {rimosso['nome']}")

# Verificare le chiavi rimaste
print(f"Matricole nel registro: {list(registro.keys())}")
```

### Passo 5: Statistiche sul registro

```python
# Trovare lo studente con la media più alta
migliore_matricola: str = ""
migliore_media: float = 0.0

for matricola, dati in registro.items():
    voti: list[int] = dati["voti"]
    media: float = sum(voti) / len(voti)
    if media > migliore_media:
        migliore_media = media
        migliore_matricola = matricola

print(f"Miglior studente: {registro[migliore_matricola]['nome']} "
      f"(media: {migliore_media:.1f})")
```

---

## Esercizio guidato 5 — Set: confronto iscritti tra anni accademici

I set sono insiemi matematici: collezioni **non ordinate** di elementi **unici**. Sono perfetti per operazioni come unione, intersezione e differenza.

### Passo 1: Creare set di iscritti

```python
iscritti_2024: set[str] = {"Anna", "Marco", "Luca", "Sara", "Elena"}
iscritti_2025: set[str] = {"Marco", "Sara", "Elena", "Paolo", "Giulia"}
```

### Passo 2: Operazioni insiemistiche

```python
# Studenti confermati (presenti in entrambi gli anni)
confermati: set[str] = iscritti_2024 & iscritti_2025  # intersezione
print(f"Confermati:  {confermati}")

# Nuovi iscritti (presenti nel 2025 ma non nel 2024)
nuovi: set[str] = iscritti_2025 - iscritti_2024  # differenza
print(f"Nuovi:       {nuovi}")

# Abbandoni (presenti nel 2024 ma non nel 2025)
abbandoni: set[str] = iscritti_2024 - iscritti_2025  # differenza
print(f"Abbandoni:   {abbandoni}")

# Tutti gli studenti che sono passati per il corso
tutti: set[str] = iscritti_2024 | iscritti_2025  # unione
print(f"Tutti:       {tutti}")

# Studenti che hanno cambiato stato (presenti in uno solo dei due anni)
cambiati: set[str] = iscritti_2024 ^ iscritti_2025  # differenza simmetrica
print(f"Cambiati:    {cambiati}")
```

### Passo 3: Verifiche di appartenenza

```python
print(f"Marco è iscritto nel 2025? {'Marco' in iscritti_2025}")
print(f"Anna è iscritto nel 2025?  {'Anna' in iscritti_2025}")

# I confermati sono un sottoinsieme di tutti?
print(f"Confermati ⊆ Tutti? {confermati <= tutti}")  # True, sempre
```

### Passo 4: Eliminare duplicati da una lista

```python
# Caso pratico: risposte a un sondaggio con duplicati
risposte: list[str] = ["pizza", "pasta", "pizza", "sushi", "pasta", "pizza", "sushi"]
piatti_unici: set[str] = set(risposte)
print(f"Piatti unici: {piatti_unici}")
print(f"Quanti piatti diversi: {len(piatti_unici)}")
```

---

## Esercizio guidato 6 — Counter: frequenza delle parole

`Counter` del modulo `collections` è un dizionario specializzato per contare elementi.

### Passo 1: Contare le parole in un testo

```python
from collections import Counter

testo: str = """
La statistica è la scienza che studia i fenomeni collettivi.
La statistica descrittiva riassume i dati osservati.
La statistica inferenziale generalizza i risultati al di là dei dati osservati.
"""

# Pulizia e tokenizzazione
parole: list[str] = testo.lower().split()
conteggio: Counter[str] = Counter(parole)

print("Tutte le frequenze:")
for parola, freq in conteggio.most_common():
    print(f"  {parola:20s} → {freq}")
```

### Passo 2: Le parole più frequenti

```python
# Le 5 parole più comuni
top_5: list[tuple[str, int]] = conteggio.most_common(5)
print("\nTop 5:")
for parola, freq in top_5:
    print(f"  {parola}: {freq}")

# Quante parole uniche?
print(f"\nParole totali: {sum(conteggio.values())}")
print(f"Parole uniche: {len(conteggio)}")
```

### Passo 3: Confronto tra due testi

```python
testo_a: str = "il gatto e il cane giocano nel giardino"
testo_b: str = "il cane e il gatto dormono in giardino"

freq_a: Counter[str] = Counter(testo_a.split())
freq_b: Counter[str] = Counter(testo_b.split())

# Parole in comune
comuni: set[str] = set(freq_a.keys()) & set(freq_b.keys())
print(f"Parole in comune: {comuni}")

# Combinare i conteggi
combinato: Counter[str] = freq_a + freq_b
print(f"Frequenze combinate: {combinato.most_common()}")
```

---

## Esercizi autonomi

Per ciascun esercizio, scrivi il codice completo con type hints. Non vengono fornite le soluzioni: verifica il funzionamento eseguendo il codice e ragionando sull'output.

### Esercizio A1 — Rubrica telefonica (base)

Crea una rubrica telefonica usando un dizionario che associa nomi (`str`) a numeri di telefono (`str`).

1. Crea la rubrica con almeno 5 contatti.
2. Implementa queste operazioni:
   - Cerca un contatto per nome e stampa il numero.
   - Aggiungi un nuovo contatto.
   - Modifica il numero di un contatto esistente.
   - Elimina un contatto.
   - Stampa tutti i contatti in ordine alfabetico (usa `sorted()` sulle chiavi).
3. Gestisci il caso in cui si cerca un contatto inesistente (usa `.get()`).

### Esercizio A2 — Analisi dataset con lista di dizionari (intermedio)

Hai un dataset di studenti rappresentato come lista di dizionari:

```python
studenti: list[dict[str, object]] = [
    {"nome": "Anna", "corso": "Statistica I", "voto": 28},
    {"nome": "Marco", "corso": "Statistica I", "voto": 24},
    {"nome": "Anna", "corso": "Analisi", "voto": 30},
    {"nome": "Luca", "corso": "Statistica I", "voto": 26},
    {"nome": "Marco", "corso": "Analisi", "voto": 22},
    {"nome": "Luca", "corso": "Analisi", "voto": 27},
    {"nome": "Sara", "corso": "Statistica I", "voto": 30},
    {"nome": "Sara", "corso": "Analisi", "voto": 25},
]
```

Scrivi codice che:

1. Calcola la media dei voti per ciascun corso.
2. Trova lo studente con la media complessiva più alta.
3. Per ogni studente, stampa tutti i voti sostenuti e la media.
4. Conta quanti studenti hanno una media superiore a 26.

**Suggerimento:** usa un dizionario per raggruppare i voti per corso, e un altro per raggruppare i voti per studente.

### Esercizio A3 — Sistema di raccomandazione con set (avanzato)

Hai un dizionario che associa ogni utente ai film che ha visto:

```python
catalogo: dict[str, set[str]] = {
    "Alice": {"Matrix", "Inception", "Interstellar", "Dune"},
    "Bob": {"Matrix", "Inception", "Avatar", "Titanic"},
    "Carla": {"Interstellar", "Dune", "Avatar", "Arrival"},
    "David": {"Matrix", "Dune", "Arrival", "Titanic"},
}
```

Scrivi codice che:

1. Dato un utente, trova l'utente con cui ha più film in comune (usa l'intersezione dei set).
2. Raccomanda all'utente i film visti dal suo "utente più simile" ma non ancora visti da lui (usa la differenza).
3. Trova i film visti da tutti gli utenti (intersezione di tutti i set).
4. Trova i film visti da almeno un utente (unione di tutti i set).
5. Trova i film "di nicchia" visti da un solo utente.

**Suggerimento per il punto 5:** per ogni film nell'unione totale, conta in quanti set compare.

---

## Sfida finale — Analisi completa di un dataset studenti

Dato il seguente dataset:

```python
esami: list[dict[str, object]] = [
    {"matricola": "M001", "nome": "Anna",  "corso": "Statistica", "voto": 28, "lode": False},
    {"matricola": "M001", "nome": "Anna",  "corso": "Analisi",    "voto": 30, "lode": True},
    {"matricola": "M001", "nome": "Anna",  "corso": "Informatica","voto": 25, "lode": False},
    {"matricola": "M002", "nome": "Marco", "corso": "Statistica", "voto": 24, "lode": False},
    {"matricola": "M002", "nome": "Marco", "corso": "Analisi",    "voto": 27, "lode": False},
    {"matricola": "M003", "nome": "Luca",  "corso": "Statistica", "voto": 30, "lode": True},
    {"matricola": "M003", "nome": "Luca",  "corso": "Analisi",    "voto": 30, "lode": False},
    {"matricola": "M003", "nome": "Luca",  "corso": "Informatica","voto": 28, "lode": False},
    {"matricola": "M004", "nome": "Sara",  "corso": "Statistica", "voto": 26, "lode": False},
    {"matricola": "M004", "nome": "Sara",  "corso": "Informatica","voto": 30, "lode": True},
    {"matricola": "M005", "nome": "Elena", "corso": "Statistica", "voto": 22, "lode": False},
    {"matricola": "M005", "nome": "Elena", "corso": "Analisi",    "voto": 20, "lode": False},
    {"matricola": "M005", "nome": "Elena", "corso": "Informatica","voto": 24, "lode": False},
]
```

Scrivi un programma completo che:

1. **Media per corso:** calcola e stampa la media dei voti per ciascun corso.
2. **Studente migliore per corso:** per ogni corso, identifica lo studente con il voto più alto.
3. **Classifica generale:** ordina gli studenti per media complessiva decrescente e stampa la classifica.
4. **Conteggio lodi:** conta quante lodi ha ottenuto ciascuno studente.
5. **Corsi per studente:** usa un set per mostrare quali corsi ha sostenuto ogni studente e identifica chi non ha ancora sostenuto tutti e tre gli esami.

Usa `Counter`, operazioni su dizionari e set, type hints per tutte le variabili. L'output deve essere chiaro e formattato.

---

## Domande di verifica

1. Qual è la differenza fondamentale tra una lista e una tupla? In quale situazione preferiresti una tupla?
2. Se scrivi `b = a` dove `a` è una lista, e poi modifichi `b[0]`, cosa succede ad `a`? Perché?
3. Cosa restituisce `{"a": 1, "b": 2}.get("c", 0)`? E `{"a": 1, "b": 2}["c"]`?
4. Date due set `A` e `B`, quale operazione produce gli elementi presenti in `A` ma non in `B`? E quelli presenti in uno solo dei due?
5. Qual è la differenza tra `sorted(lista)` e `lista.sort()`? Quale delle due modifica la lista originale?
6. Perché una lista non puo essere usata come chiave di un dizionario, ma una tupla si?
7. Cosa fa `Counter("abracadabra").most_common(3)`?

---

## Osservazioni finali

In questo laboratorio avete lavorato con le quattro strutture dati fondamentali di Python: liste, tuple, dizionari e set. La scelta della struttura giusta dipende dal problema:

- **Lista** quando l'ordine conta e i dati possono cambiare.
- **Tupla** quando i dati sono fissi (coordinate, record immutabili, chiavi composite).
- **Dizionario** quando serve accesso rapido per chiave (registri, lookup, conteggi manuali).
- **Set** quando servono operazioni insiemistiche o eliminare duplicati.

L'esperimento su alias e copia e uno dei concetti piu importanti del laboratorio. In statistica, quando passate un dataset a una funzione e quella funzione lo modifica, volete essere certi di sapere se state lavorando sulla copia o sull'originale. Questo tema tornerà nei prossimi laboratori.

`Counter` meriterà poca attenzione adesso, ma diventerà uno strumento prezioso quando lavorerete con dati testuali o categoriali.

Nel prossimo laboratorio vedremo come organizzare queste operazioni in **funzioni** riutilizzabili e testabili.
