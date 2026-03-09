# Errori comuni — F09: Cicli

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione F09.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

---

### Errore 1: Off-by-one in `range()` — il valore finale è escluso

**Codice errato:**
```python
# Lo studente vuole stampare i numeri da 1 a 10
for i in range(1, 10):
    print(i)
```

**Cosa succede:**
```
1
2
3
4
5
6
7
8
9
```

Viene stampato fino a 9, non fino a 10.

**Perché è sbagliato:** La funzione `range(a, b)` genera i numeri da `a` fino a `b - 1`: il valore finale `b` è sempre escluso. Questo è uno degli errori più insidiosi perché il codice funziona senza segnalare errori, ma produce un risultato diverso da quello atteso. Per includere il 10, bisogna scrivere `range(1, 11)`.

**Codice corretto:**
```python
# Per stampare i numeri da 1 a 10 (incluso)
for i in range(1, 11):
    print(i)
```

**Regola da ricordare:** `range(a, b)` genera numeri da `a` a `b-1`: se vuoi includere `b`, scrivi `range(a, b + 1)`.

---

### Errore 2: Modificare una lista durante l'iterazione con `for`

**Codice errato:**
```python
# Rimuovere i numeri negativi dalla lista
numeri = [3, -1, 5, -2, 8, -4]
for n in numeri:
    if n < 0:
        numeri.remove(n)
print(numeri)
```

**Cosa succede:**
```
[3, 5, -2, 8]
```

Il valore `-2` non viene rimosso! Il risultato è incompleto.

**Perché è sbagliato:** Quando rimuovi un elemento da una lista mentre la stai percorrendo con un `for`, gli indici degli elementi successivi si spostano. Dopo aver rimosso `-1` (posizione 1), `-2` si sposta dalla posizione 3 alla posizione 2, ma il ciclo passa alla posizione 3, saltando `-2`. È un errore subdolo perché non genera eccezioni.

**Codice corretto:**
```python
# Soluzione 1: creare una nuova lista con list comprehension
numeri = [3, -1, 5, -2, 8, -4]
numeri_positivi = [n for n in numeri if n >= 0]
print(numeri_positivi)  # [3, 5, 8]

# Soluzione 2: iterare su una copia della lista
numeri = [3, -1, 5, -2, 8, -4]
for n in numeri[:]:  # numeri[:] crea una copia
    if n < 0:
        numeri.remove(n)
print(numeri)  # [3, 5, 8]
```

**Regola da ricordare:** Non modificare mai una lista mentre la stai percorrendo con un `for` — crea una nuova lista o itera su una copia.

---

### Errore 3: Ciclo `while` infinito — dimenticare di aggiornare la variabile di controllo

**Codice errato:**
```python
# Stampare i numeri da 1 a 5
i = 1
while i <= 5:
    print(i)
```

**Cosa succede:**
```
1
1
1
1
1
... (all'infinito, bisogna premere Ctrl+C per fermare il programma)
```

**Perché è sbagliato:** La variabile `i` viene inizializzata a 1 ma non viene mai incrementata all'interno del ciclo. La condizione `i <= 5` rimane sempre vera e il ciclo non termina mai. In un ciclo `while` è fondamentale che il corpo del ciclo modifichi la variabile di controllo in modo che prima o poi la condizione diventi falsa.

**Codice corretto:**
```python
i = 1
while i <= 5:
    print(i)
    i = i + 1  # oppure: i += 1
```

**Regola da ricordare:** In ogni ciclo `while`, assicurati che qualcosa nel corpo del ciclo modifichi la condizione, altrimenti il ciclo non terminerà mai.

---

### Errore 4: Dimenticare di inizializzare l'accumulatore prima del ciclo

**Codice errato:**
```python
# Calcolare la somma dei voti
voti = [28, 30, 25, 27, 30]
for voto in voti:
    somma = somma + voto
print(f"Somma: {somma}")
```

**Cosa succede:**
```
NameError: name 'somma' is not defined
```

**Perché è sbagliato:** La variabile `somma` viene usata nell'espressione `somma + voto` prima di essere stata creata. Alla prima iterazione, Python cerca il valore di `somma` per sommarci `voto`, ma `somma` non esiste ancora. È necessario inizializzare la variabile accumulatore a `0` (per le somme) o al valore iniziale appropriato prima di entrare nel ciclo.

**Codice corretto:**
```python
voti = [28, 30, 25, 27, 30]
somma = 0  # Inizializzazione dell'accumulatore
for voto in voti:
    somma = somma + voto
print(f"Somma: {somma}")  # Somma: 140
```

**Regola da ricordare:** Prima di un ciclo che accumula un risultato, inizializza sempre la variabile accumulatore (a `0` per somme, a `""` per stringhe, a `[]` per liste).

---

### Errore 5: `range()` con argomenti sbagliati o nell'ordine errato

**Codice errato:**
```python
# Contare alla rovescia da 5 a 1
for i in range(5, 1):
    print(i)
```

**Cosa succede:**
```
(nessun output — il ciclo non viene eseguito)
```

**Perché è sbagliato:** `range(5, 1)` genera una sequenza vuota perché il valore iniziale (5) è già maggiore del valore finale (1) e il passo predefinito è `+1`. Per contare alla rovescia bisogna specificare un passo negativo con il terzo argomento: `range(5, 0, -1)`. Nota: il valore finale è 0 (non 1) perché l'estremo destro è escluso.

**Codice corretto:**
```python
# Contare alla rovescia da 5 a 1
for i in range(5, 0, -1):
    print(i)
# Output: 5, 4, 3, 2, 1
```

**Regola da ricordare:** Per contare alla rovescia usa `range(inizio, fine, -1)` — senza il passo negativo, `range` non conta all'indietro.

---

### Errore 6: Confondere `break` e `continue`

**Codice errato:**
```python
# Lo studente vuole saltare i numeri pari e stampare solo i dispari
for i in range(1, 11):
    if i % 2 == 0:
        break  # Lo studente voleva usare continue
    print(i)
```

**Cosa succede:**
```
1
```

Viene stampato solo `1`, poi il ciclo si interrompe.

**Perché è sbagliato:** `break` interrompe completamente il ciclo e ne esce, mentre `continue` salta solo l'iterazione corrente e passa alla successiva. Quando `i` vale 2 (il primo numero pari), `break` termina l'intero ciclo invece di saltare quell'iterazione. Lo studente voleva usare `continue` per saltare i numeri pari e proseguire con i dispari.

**Codice corretto:**
```python
# Saltare i numeri pari e stampare solo i dispari
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Salta questa iterazione
    print(i)
# Output: 1, 3, 5, 7, 9
```

**Regola da ricordare:** `break` esce dal ciclo definitivamente, `continue` salta solo l'iterazione corrente e prosegue con la prossima.
