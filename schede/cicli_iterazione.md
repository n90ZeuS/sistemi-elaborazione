# Cicli e Iterazione a Confronto

Scheda di riferimento rapido su cicli `for` e `while`, funzioni di iterazione e pattern comuni.

---

## for vs while: quando usare quale

| Caratteristica         | `for`                              | `while`                             |
|------------------------|------------------------------------|-------------------------------------|
| **Quando usare**       | Numero di iterazioni noto o iterabile disponibile | Numero di iterazioni non noto a priori |
| **Itera su**           | Qualsiasi iterabile (lista, stringa, range...) | Finche' una condizione e' vera     |
| **Rischio loop infinito** | No (iterabile finito)           | Si, se la condizione non diventa mai falsa |
| **Contatore**          | Automatico (la variabile del for)  | Da gestire manualmente              |
| **Uso tipico**         | Scorrere una collezione, ripetere N volte | Input utente, convergenza, ricerca  |

### Sintassi `for`

```python
# Itera su una lista
voti = [28, 30, 25, 27]
for voto in voti:
    print(voto)

# Ripeti N volte
for i in range(5):
    print(f"Iterazione {i}")

# Itera su una stringa
for carattere in "ciao":
    print(carattere)

# Itera su un dizionario
studente = {"nome": "Luca", "eta": 20}
for chiave, valore in studente.items():
    print(f"{chiave}: {valore}")
```

### Sintassi `while`

```python
# Ripeti finche' condizione vera
risposta = ""
while risposta != "si":
    risposta = input("Vuoi continuare? (si/no): ")

# Contatore manuale
i = 0
while i < 5:
    print(f"Iterazione {i}")
    i += 1  # NON dimenticare di aggiornare!

# Convergenza (esempio statistico)
errore = 100.0
while errore > 0.001:
    errore = errore / 2
    print(f"Errore: {errore}")
```

---

## range() vs enumerate() vs zip()

### range() -- genera sequenze di numeri

```python
range(5)           # 0, 1, 2, 3, 4
range(2, 7)        # 2, 3, 4, 5, 6
range(0, 10, 2)    # 0, 2, 4, 6, 8
range(10, 0, -1)   # 10, 9, 8, ..., 1

# Uso: ripetere N volte o generare indici
for i in range(len(voti)):     # funziona, ma vedi enumerate
    print(f"Voto {i}: {voti[i]}")
```

### enumerate() -- indice + valore insieme

```python
frutti = ["mela", "banana", "ciliegia"]

# SENZA enumerate (brutto)
for i in range(len(frutti)):
    print(f"{i}: {frutti[i]}")

# CON enumerate (pythonic)
for i, frutto in enumerate(frutti):
    print(f"{i}: {frutto}")

# Con indice di partenza personalizzato
for num, frutto in enumerate(frutti, start=1):
    print(f"{num}. {frutto}")
# 1. mela
# 2. banana
# 3. ciliegia
```

### zip() -- iterare su piu' sequenze in parallelo

```python
nomi = ["Luca", "Anna", "Marco"]
voti = [28, 30, 25]

# Itera su entrambe contemporaneamente
for nome, voto in zip(nomi, voti):
    print(f"{nome}: {voto}")

# zip si ferma alla sequenza piu' corta!
# Per continuare fino alla piu' lunga: itertools.zip_longest

# Creare un dizionario con zip
registro = dict(zip(nomi, voti))
# {"Luca": 28, "Anna": 30, "Marco": 25}
```

### Confronto rapido

| Funzione      | Input                    | Output per iterazione        | Uso tipico                  |
|---------------|--------------------------|-----------------------------|-----------------------------|
| `range(n)`    | Numero intero            | Un numero                   | Ripetere N volte            |
| `enumerate(x)`| Un iterabile             | `(indice, elemento)`        | Indice + valore             |
| `zip(a, b)`  | Due+ iterabili           | `(elem_a, elem_b)`          | Iterare in parallelo        |

---

## List Comprehension vs Ciclo Esplicito

### Sintassi a confronto

```python
# CICLO ESPLICITO
quadrati = []
for x in range(10):
    quadrati.append(x ** 2)

# LIST COMPREHENSION (equivalente)
quadrati = [x ** 2 for x in range(10)]
```

### Con condizione (filtro)

```python
# CICLO ESPLICITO
pari = []
for x in range(20):
    if x % 2 == 0:
        pari.append(x)

# LIST COMPREHENSION
pari = [x for x in range(20) if x % 2 == 0]
```

### Con if-else (trasformazione)

```python
# CICLO ESPLICITO
risultati = []
for voto in voti:
    if voto >= 18:
        risultati.append("promosso")
    else:
        risultati.append("bocciato")

# LIST COMPREHENSION (nota: if-else PRIMA del for)
risultati = ["promosso" if voto >= 18 else "bocciato" for voto in voti]
```

### Quando usare quale?

```
Usa la LIST COMPREHENSION quando:
  - L'operazione e' semplice (una riga logica)
  - Vuoi creare una nuova lista trasformando/filtrando
  - La leggibilita' non ne risente

Usa il CICLO ESPLICITO quando:
  - L'operazione e' complessa (piu' righe di logica)
  - Hai bisogno di effetti collaterali (print, modificare altro)
  - Devi usare try/except dentro il ciclo
  - La comprehension diventerebbe illeggibile
```

### Funziona anche per dict e set

```python
# Dict comprehension
quadrati = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
iniziali = {nome[0] for nome in nomi}
# {'L', 'A', 'M'}
```

---

## break, continue, else nei cicli

### break -- interrompe il ciclo

```python
# Cerca il primo numero negativo
numeri = [3, 7, -2, 5, -1]
for n in numeri:
    if n < 0:
        print(f"Trovato negativo: {n}")
        break
# Stampa: Trovato negativo: -2
# Il ciclo si ferma, non controlla 5 e -1
```

### continue -- salta all'iterazione successiva

```python
# Stampa solo i numeri positivi
for n in numeri:
    if n < 0:
        continue  # salta questo elemento
    print(n)
# Stampa: 3, 7, 5
```

### else nei cicli -- eseguito se il ciclo termina SENZA break

```python
# Cerca un valore: else si esegue se NON trovato
numeri = [3, 7, 5, 2]
cercato = 10

for n in numeri:
    if n == cercato:
        print(f"Trovato {cercato}!")
        break
else:
    # Eseguito SOLO se il for finisce senza break
    print(f"{cercato} non trovato nella lista")
# Stampa: 10 non trovato nella lista
```

### Tabella riassuntiva

| Istruzione | Effetto                                        | Funziona in |
|------------|------------------------------------------------|-------------|
| `break`    | Esce dal ciclo immediatamente                  | for, while  |
| `continue` | Salta al prossimo giro del ciclo               | for, while  |
| `else`     | Eseguito se il ciclo finisce senza `break`     | for, while  |

---

## Pattern di iterazione comuni

### 1. Accumulatore (somma, prodotto, conteggio)

```python
# Somma
totale = 0
for voto in voti:
    totale += voto
media = totale / len(voti)

# Conteggio con condizione
sufficienti = 0
for voto in voti:
    if voto >= 18:
        sufficienti += 1
```

### 2. Ricerca (trovare un elemento)

```python
# Trova il primo che soddisfa una condizione
trovato = None
for voto in voti:
    if voto == 30:
        trovato = voto
        break

# Verificare se almeno uno soddisfa la condizione
ha_lode = any(voto == 30 for voto in voti)      # True/False
tutti_sufficienti = all(voto >= 18 for voto in voti)
```

### 3. Trasformazione (creare nuova lista)

```python
# Converti tutti i voti in trentesimi a percentuale
percentuali = [voto / 30 * 100 for voto in voti]
```

### 4. Filtraggio (selezionare elementi)

```python
# Solo i voti sufficienti
sufficienti = [v for v in voti if v >= 18]
```

### 5. Massimo/Minimo con posizione

```python
voti = [28, 30, 25, 27]
indice_max = 0
for i, voto in enumerate(voti):
    if voto > voti[indice_max]:
        indice_max = i
print(f"Voto max: {voti[indice_max]} alla posizione {indice_max}")

# Oppure, piu' semplice:
indice_max = voti.index(max(voti))
```

### 6. Iterazione su file (riga per riga)

```python
with open("dati.txt") as f:
    for riga in f:
        riga = riga.strip()  # rimuovi \n
        print(riga)
```

### 7. Cicli annidati (combinazioni)

```python
# Tabellina pitagorica
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()  # vai a capo dopo ogni riga
```
