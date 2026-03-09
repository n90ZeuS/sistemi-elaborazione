# Errori comuni — F11: Liste e tuple

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione F11.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

---

### Errore 1: `lista2 = lista1` non crea una copia — crea un alias

**Codice errato:**
```python
voti_esame1 = [28, 30, 25]
voti_esame2 = voti_esame1  # Lo studente pensa di copiare la lista
voti_esame2.append(27)
print(voti_esame1)
```

**Cosa succede:**
```
[28, 30, 25, 27]
```

Anche `voti_esame1` è stato modificato, anche se lo studente ha aggiunto l'elemento solo a `voti_esame2`.

**Perché è sbagliato:** L'assegnamento `voti_esame2 = voti_esame1` non crea una nuova lista: crea un secondo nome (alias) che punta alla stessa lista in memoria. Qualsiasi modifica fatta tramite un nome si riflette anche sull'altro, perché la lista sottostante è una sola. Per creare una copia indipendente bisogna usare `.copy()`, `list()` o lo slicing `[:]`.

**Codice corretto:**
```python
voti_esame1 = [28, 30, 25]
voti_esame2 = voti_esame1.copy()  # Crea una copia indipendente
voti_esame2.append(27)
print(voti_esame1)  # [28, 30, 25] — non modificata
print(voti_esame2)  # [28, 30, 25, 27]

# Alternative equivalenti:
# voti_esame2 = list(voti_esame1)
# voti_esame2 = voti_esame1[:]
```

**Regola da ricordare:** Per copiare una lista usa `.copy()` o `lista[:]` — l'assegnamento `=` crea solo un alias, non una copia.

---

### Errore 2: `sort()` restituisce `None` — il risultato non va assegnato

**Codice errato:**
```python
voti = [28, 30, 25, 27]
voti_ordinati = voti.sort()
print(voti_ordinati)
```

**Cosa succede:**
```
None
```

**Perché è sbagliato:** Il metodo `.sort()` ordina la lista sul posto (modifica la lista originale) e restituisce `None`, non la lista ordinata. Assegnando il risultato a una variabile, si ottiene `None`. Se si vuole una nuova lista ordinata senza modificare l'originale, bisogna usare la funzione `sorted()`. Se invece va bene modificare la lista originale, basta chiamare `.sort()` senza assegnare il risultato.

**Codice corretto:**
```python
# Opzione 1: ordinare la lista originale (la modifica sul posto)
voti = [28, 30, 25, 27]
voti.sort()
print(voti)  # [25, 27, 28, 30]

# Opzione 2: creare una nuova lista ordinata (l'originale resta intatta)
voti = [28, 30, 25, 27]
voti_ordinati = sorted(voti)
print(voti)            # [28, 30, 25, 27] — invariata
print(voti_ordinati)   # [25, 27, 28, 30]
```

**Regola da ricordare:** `.sort()` modifica la lista e restituisce `None`; usa `sorted(lista)` se vuoi ottenere una nuova lista ordinata.

---

### Errore 3: `IndexError` — accedere a un indice che non esiste

**Codice errato:**
```python
studenti = ["Anna", "Marco", "Giulia"]
print(studenti[3])
```

**Cosa succede:**
```
IndexError: list index out of range
```

**Perché è sbagliato:** Gli indici delle liste in Python partono da 0, non da 1. Una lista con 3 elementi ha indici 0, 1 e 2. L'indice 3 non esiste e Python genera un `IndexError`. Questo errore è molto comune quando si usa `len(lista)` come indice: l'ultimo elemento ha indice `len(lista) - 1`.

**Codice corretto:**
```python
studenti = ["Anna", "Marco", "Giulia"]
print(studenti[2])   # Giulia — ultimo elemento
print(studenti[-1])  # Giulia — indice negativo per l'ultimo elemento

# Accesso sicuro con controllo
indice = 3
if indice < len(studenti):
    print(studenti[indice])
else:
    print(f"Indice {indice} non valido, la lista ha {len(studenti)} elementi")
```

**Regola da ricordare:** Gli indici partono da 0: una lista di `n` elementi ha indici da 0 a `n-1` — usa `lista[-1]` per accedere all'ultimo elemento.

---

### Errore 4: Modificare una lista durante l'iterazione con `for`

**Codice errato:**
```python
# Rimuovere gli studenti con voto insufficiente
studenti = [("Anna", 28), ("Marco", 15), ("Giulia", 12), ("Luca", 22)]
for studente in studenti:
    if studente[1] < 18:
        studenti.remove(studente)
print(studenti)
```

**Cosa succede:**
```
[('Anna', 28), ('Giulia', 12), ('Luca', 22)]
```

Giulia (voto 12) non viene rimossa! Dopo la rimozione di Marco, Giulia prende il suo posto nella lista e viene saltata dal ciclo.

**Perché è sbagliato:** Rimuovere elementi da una lista mentre la si percorre con un `for` causa lo spostamento degli indici. Quando Marco viene rimosso, tutti gli elementi successivi si spostano di una posizione indietro. Il ciclo avanza all'indice successivo e salta Giulia. Non si riceve nessun messaggio di errore, il che rende il bug difficile da individuare.

**Codice corretto:**
```python
# Soluzione 1: list comprehension (creare nuova lista)
studenti = [("Anna", 28), ("Marco", 15), ("Giulia", 12), ("Luca", 22)]
promossi = [s for s in studenti if s[1] >= 18]
print(promossi)  # [('Anna', 28), ('Luca', 22)]

# Soluzione 2: iterare su una copia
studenti = [("Anna", 28), ("Marco", 15), ("Giulia", 12), ("Luca", 22)]
for studente in studenti[:]:
    if studente[1] < 18:
        studenti.remove(studente)
print(studenti)  # [('Anna', 28), ('Luca', 22)]
```

**Regola da ricordare:** Non rimuovere mai elementi da una lista mentre la percorri con `for` — usa una list comprehension per filtrare o itera su una copia con `lista[:]`.

---

### Errore 5: Tentare di modificare una tupla

**Codice errato:**
```python
coordinate = (44.4949, 11.3426)  # Bologna
coordinate[0] = 45.4642  # Cambiare a Milano
```

**Cosa succede:**
```
TypeError: 'tuple' object does not support item assignment
```

**Perché è sbagliato:** Le tuple, a differenza delle liste, sono immutabili: una volta create, non è possibile modificare, aggiungere o rimuovere i loro elementi. Le parentesi tonde `()` creano una tupla, le parentesi quadre `[]` creano una lista. Se hai bisogno di modificare i dati, usa una lista. Se i dati non devono cambiare (come delle coordinate fisse), la tupla è la scelta giusta proprio perché protegge da modifiche accidentali.

**Codice corretto:**
```python
# Se devi modificare i dati, usa una lista
coordinate = [44.4949, 11.3426]
coordinate[0] = 45.4642
print(coordinate)  # [45.4642, 11.3426]

# Se vuoi una nuova tupla, devi crearla da zero
bologna = (44.4949, 11.3426)
milano = (45.4642, 9.1900)  # Nuova tupla
```

**Regola da ricordare:** Le tuple sono immutabili (non modificabili); se hai bisogno di modificare i dati, usa una lista con le parentesi quadre `[]`.

---

### Errore 6: Confondere `append()` e `extend()`

**Codice errato:**
```python
# Lo studente vuole unire due liste di voti
voti_primo_semestre = [28, 30, 25]
voti_secondo_semestre = [27, 30, 26]
voti_primo_semestre.append(voti_secondo_semestre)
print(voti_primo_semestre)
```

**Cosa succede:**
```
[28, 30, 25, [27, 30, 26]]
```

La seconda lista viene aggiunta come un unico elemento (una lista dentro la lista), non come singoli elementi.

**Perché è sbagliato:** Il metodo `.append()` aggiunge un singolo elemento alla fine della lista. Se gli si passa una lista, aggiunge l'intera lista come un unico elemento, creando una lista annidata. Per aggiungere tutti gli elementi di una lista a un'altra, bisogna usare `.extend()` o l'operatore `+`.

**Codice corretto:**
```python
voti_primo_semestre = [28, 30, 25]
voti_secondo_semestre = [27, 30, 26]

# Metodo 1: extend() aggiunge ogni elemento singolarmente
voti_primo_semestre.extend(voti_secondo_semestre)
print(voti_primo_semestre)  # [28, 30, 25, 27, 30, 26]

# Metodo 2: operatore + crea una nuova lista
voti_primo_semestre = [28, 30, 25]
tutti_i_voti = voti_primo_semestre + voti_secondo_semestre
print(tutti_i_voti)  # [28, 30, 25, 27, 30, 26]
```

**Regola da ricordare:** `.append(x)` aggiunge `x` come singolo elemento; `.extend(lista)` aggiunge ogni elemento della lista uno per uno — per unire due liste usa `.extend()` o `+`.
