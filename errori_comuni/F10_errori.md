# Errori comuni — F10: Comprehension e stringhe

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione F10.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

---

### Errore 1: Comprehension troppo complesse — sacrificare la leggibilità

**Codice errato:**
```python
# Trovare la somma dei quadrati dei numeri pari in una matrice
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
risultato = sum([x**2 for riga in matrice for x in riga if x % 2 == 0])
print(risultato)
```

**Cosa succede:**
```
120
```

Il risultato è corretto, ma il codice è difficile da leggere e da correggere in caso di errore.

**Perché è sbagliato:** Anche se Python permette comprehension con più cicli e condizioni, una comprehension troppo complessa diventa illeggibile. Per studenti alle prime armi è facile confondere l'ordine dei `for` e delle condizioni `if`. Quando una comprehension richiede più di un `for` o diventa lunga, è meglio usare cicli espliciti che sono più chiari.

**Codice corretto:**
```python
# Versione chiara con cicli espliciti
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
somma = 0
for riga in matrice:
    for x in riga:
        if x % 2 == 0:
            somma += x ** 2
print(somma)  # 120
```

**Regola da ricordare:** Se una list comprehension richiede più di un `for` o non si capisce al primo sguardo, riscrivila con cicli espliciti.

---

### Errore 2: Comportamento inatteso di `.split()` su stringa vuota

**Codice errato:**
```python
# Lo studente si aspetta una lista con un elemento vuoto
testo = ""
parole = testo.split()
print(parole)
print(len(parole))  # Lo studente si aspetta 1
```

**Cosa succede:**
```
[]
0
```

La lista è vuota, non contiene una stringa vuota.

**Perché è sbagliato:** Il metodo `.split()` senza argomenti divide per spazi bianchi e rimuove automaticamente le stringhe vuote dal risultato. Chiamato su una stringa vuota, restituisce una lista vuota `[]`, non `[""]`. Questo è diverso da `.split(",")` con un separatore esplicito, che su una stringa vuota restituisce `[""]`. La differenza è sottile ma importante quando si contano le parole di un testo.

**Codice corretto:**
```python
# Se vuoi gestire il caso di stringa vuota
testo = ""
if testo:
    parole = testo.split()
    print(f"Ci sono {len(parole)} parole")
else:
    print("Il testo è vuoto, 0 parole")

# Nota la differenza con un separatore esplicito:
print("".split())     # []    — lista vuota
print("".split(","))  # ['']  — lista con una stringa vuota
```

**Regola da ricordare:** `.split()` senza argomenti su stringa vuota restituisce `[]` (lista vuota), non `[""]` — controlla sempre se la stringa è vuota prima di contare le parole.

---

### Errore 3: Confondere `in` su stringa e `in` su lista

**Codice errato:**
```python
# Lo studente vuole cercare la parola "anno" nel testo
testo = "il mio compleanno è domani"
if "anno" in testo:
    print("Trovata la parola 'anno'!")
```

**Cosa succede:**
```
Trovata la parola 'anno'!
```

Il messaggio viene stampato, ma la parola "anno" come parola a sé non è nel testo: è contenuta dentro "compleanno".

**Perché è sbagliato:** L'operatore `in` su una stringa cerca una sottostringa, non una parola intera. `"anno" in "compleanno"` è `True` perché i caratteri "anno" appaiono dentro "compleanno". Se si vogliono cercare parole intere, bisogna prima dividere il testo in parole con `.split()` e cercare nella lista risultante.

**Codice corretto:**
```python
# Cercare una parola intera nel testo
testo = "il mio compleanno è domani"

# Metodo corretto: cercare nella lista di parole
parole = testo.split()
if "anno" in parole:
    print("Trovata la parola 'anno'!")
else:
    print("La parola 'anno' non è presente")
# Output: La parola 'anno' non è presente
```

**Regola da ricordare:** `in` su una stringa cerca sottostringhe, `in` su una lista cerca elementi esatti — per cercare parole intere, usa `.split()` e cerca nella lista.

---

### Errore 4: Tentare di modificare una stringa tramite indice

**Codice errato:**
```python
nome = "Marko"
nome[3] = "c"  # Correggere il typo: Marko → Marco
print(nome)
```

**Cosa succede:**
```
TypeError: 'str' object does not support item assignment
```

**Perché è sbagliato:** In Python le stringhe sono immutabili: una volta create, non si possono modificare i singoli caratteri. Non è possibile assegnare un nuovo valore a una posizione specifica della stringa come si farebbe con una lista. Per "modificare" una stringa, bisogna crearne una nuova usando metodi come `.replace()` o lo slicing.

**Codice corretto:**
```python
nome = "Marko"

# Metodo 1: usare .replace()
nome = nome.replace("k", "c")
print(nome)  # Marco

# Metodo 2: usare lo slicing
nome = "Marko"
nome = nome[:3] + "c" + nome[4:]
print(nome)  # Marco
```

**Regola da ricordare:** Le stringhe in Python sono immutabili: per modificarle devi crearne una nuova, ad esempio con `.replace()` o con lo slicing.

---

### Errore 5: Errori con le espressioni dentro le f-string

**Codice errato:**
```python
voti = [28, 30, 25]
print(f"La media è: {sum(voti) / len(voti):.2f}")
# Fin qui tutto bene, ma poi:

studente = {"nome": "Luca", "voto": 28}
print(f"Voto di {studente["nome"]}")
```

**Cosa succede:**
```
SyntaxError: f-string: unmatched '['
```

**Perché è sbagliato:** Dentro le parentesi graffe di una f-string delimitata da virgolette doppie `"`, non si possono usare altre virgolette doppie `"` per le chiavi del dizionario. Python si confonde perché la seconda `"` chiude la f-string. Bisogna usare virgolette di tipo diverso all'interno (singole) rispetto a quelle esterne (doppie), oppure viceversa.

**Codice corretto:**
```python
studente = {"nome": "Luca", "voto": 28}

# Soluzione 1: virgolette singole dentro la f-string
print(f"Voto di {studente['nome']}")

# Soluzione 2: variabile di appoggio
nome = studente["nome"]
print(f"Voto di {nome}")
```

**Regola da ricordare:** Dentro una f-string, usa virgolette di tipo diverso da quelle che delimitano la stringa — se la stringa è tra `"..."`, usa `'...'` all'interno delle graffe.

---

### Errore 6: Pensare che `.replace()` modifichi la stringa originale

**Codice errato:**
```python
frase = "Ciao Mondo Ciao"
frase.replace("Ciao", "Salve")
print(frase)
```

**Cosa succede:**
```
Ciao Mondo Ciao
```

La stringa non è cambiata.

**Perché è sbagliato:** Il metodo `.replace()` non modifica la stringa originale (le stringhe sono immutabili). Restituisce invece una nuova stringa con le sostituzioni applicate. Se non si assegna il risultato a una variabile, la nuova stringa viene creata e immediatamente persa. È un errore che non genera eccezioni, il che lo rende difficile da individuare.

**Codice corretto:**
```python
frase = "Ciao Mondo Ciao"
frase = frase.replace("Ciao", "Salve")  # Riassegna il risultato
print(frase)  # Salve Mondo Salve
```

**Regola da ricordare:** I metodi delle stringhe (`.replace()`, `.upper()`, `.strip()`, ecc.) restituiscono una nuova stringa — assegna sempre il risultato a una variabile.
