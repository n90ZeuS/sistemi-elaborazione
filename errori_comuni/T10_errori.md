# Errori comuni — T10: Stringhe

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione T10.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

---

### Errore 1: Tentare di modificare una stringa tramite indice

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

**Perché è sbagliato:** In Python le stringhe sono immutabili: una volta create, non si possono modificare i singoli caratteri. Con l'indice si può leggere un carattere, ma non assegnargli un valore nuovo. Per "modificare" una stringa bisogna crearne una nuova, con un metodo come `.replace()` o con lo slicing.

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

### Errore 2: Pensare che `.replace()` modifichi la stringa originale

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

**Perché è sbagliato:** Il metodo `.replace()` non modifica la stringa originale (le stringhe sono immutabili). Restituisce invece una nuova stringa con le sostituzioni applicate. Se non si assegna il risultato a una variabile, la nuova stringa viene creata e subito persa. Python non segnala nessun errore, quindi il problema è difficile da individuare.

**Codice corretto:**
```python
frase = "Ciao Mondo Ciao"
frase = frase.replace("Ciao", "Salve")  # Riassegna il risultato
print(frase)  # Salve Mondo Salve
```

**Regola da ricordare:** I metodi delle stringhe (`.replace()`, `.upper()`, `.strip()`, ecc.) restituiscono una nuova stringa: assegna sempre il risultato a una variabile.

---

### Errore 3: Usare `in` per cercare una parola intera

**Codice errato:**
```python
# Lo studente vuole sapere se nel testo compare la parola "anno"
testo = "il mio compleanno è domani"
if "anno" in testo:
    print("Trovata la parola 'anno'")
```

**Cosa succede:**
```
Trovata la parola 'anno'
```

Il messaggio viene stampato, ma la parola "anno" non è nel testo: i caratteri "anno" stanno dentro "compleanno".

**Perché è sbagliato:** L'operatore `in` su una stringa cerca una sottostringa, cioè una sequenza di caratteri consecutivi in qualunque punto del testo, anche in mezzo a un'altra parola. Per cercare una parola intera bisogna controllare che sia preceduta e seguita da uno spazio. Aggiungendo uno spazio all'inizio e alla fine del testo, la regola vale anche per la prima e l'ultima parola.

**Codice corretto:**
```python
testo = "il mio compleanno è domani"

# Cerco " anno " in un testo con uno spazio in più ai due bordi
if " anno " in " " + testo + " ":
    print("Trovata la parola 'anno'")
else:
    print("La parola 'anno' non è presente")
# Output: La parola 'anno' non è presente
```

Questo controllo non funziona se la parola è seguita da un segno di punteggiatura (per esempio `"anno,"`): in quel caso la punteggiatura va tolta prima con `replace()`.

**Regola da ricordare:** `in` su una stringa cerca sottostringhe, non parole: `"anno" in "compleanno"` è `True`.

---

### Errore 4: Usare il risultato di `.find()` senza controllare `-1`

**Codice errato:**
```python
# Lo studente vuole il nome del file senza estensione
nome_file = "relazione"
punto = nome_file.find(".")
print(nome_file[:punto])
```

**Cosa succede:**
```
relazion
```

Manca l'ultima lettera e Python non segnala nessun errore.

**Perché è sbagliato:** Quando la sottostringa non c'è, `.find()` restituisce `-1`. Usato come indice, `-1` indica l'ultimo carattere: `nome_file[:-1]` prende tutto tranne l'ultimo carattere. Il programma prosegue con un dato sbagliato. `.index()` invece in questo caso dà `ValueError`, quindi l'errore almeno si vede.

**Codice corretto:**
```python
nome_file = "relazione"
punto = nome_file.find(".")
if punto == -1:
    print(nome_file)               # nessuna estensione: il nome resta intero
else:
    print(nome_file[:punto])
# Output: relazione
```

**Regola da ricordare:** Dopo `.find()` controlla sempre se il risultato è `-1` prima di usarlo in un indice o in uno slicing.

---

### Errore 5: Dimenticare la `f` davanti alla f-string

**Codice errato:**
```python
media = 27.4567
print("Media: {media:.2f}")
```

**Cosa succede:**
```
Media: {media:.2f}
```

Viene stampato il testo così com'è, con le graffe.

**Perché è sbagliato:** Senza la lettera `f` prima delle virgolette, la stringa è una stringa normale e le graffe sono caratteri come gli altri. Python non sostituisce il valore della variabile e non segnala nessun errore.

**Codice corretto:**
```python
media = 27.4567
print(f"Media: {media:.2f}")  # Media: 27.46
```

**Regola da ricordare:** Se nell'output compaiono le parentesi graffe, controlla di aver scritto la `f` prima delle virgolette.

---

### Errore 6: Moltiplicare per 100 prima di usare il formato `%`

**Codice errato:**
```python
promossi = 13
iscritti = 40
quota = promossi / iscritti        # 0.325
print(f"Promossi: {quota * 100:.1%}")
```

**Cosa succede:**
```
Promossi: 3250.0%
```

**Perché è sbagliato:** Il formato `.1%` moltiplica già il valore per 100 e aggiunge il simbolo `%`. Se il valore è già stato moltiplicato per 100, la moltiplicazione avviene due volte. Lo stesso errore al contrario: con `.1f` il simbolo `%` va scritto a mano e il valore va moltiplicato per 100.

**Codice corretto:**
```python
promossi = 13
iscritti = 40
quota = promossi / iscritti

print(f"Promossi: {quota:.1%}")         # Promossi: 32.5%
print(f"Promossi: {quota * 100:.1f}%")  # Promossi: 32.5% (stesso risultato con .1f)
```

**Regola da ricordare:** Con il formato `%` si passa la proporzione (tra 0 e 1), non la percentuale già calcolata.

---

### Errore 7: Usare `.isdigit()` per controllare numeri decimali o negativi

**Codice errato:**
```python
dato = "3.5"
if dato.isdigit():
    valore = float(dato)
    print(f"Valore: {valore:.1f}")
else:
    print("Non è un numero")
```

**Cosa succede:**
```
Non è un numero
```

**Perché è sbagliato:** `.isdigit()` restituisce `True` solo se **tutti** i caratteri sono cifre. Il punto decimale e il segno meno non sono cifre, quindi `"3.5".isdigit()` e `"-2".isdigit()` sono `False`, anche se `float()` li convertirebbe senza problemi.

**Codice corretto:**
```python
dato = "3.5"
# Tolgo un eventuale punto decimale e poi controllo che restino solo cifre
if dato.count(".") <= 1 and dato.replace(".", "").isdigit():
    valore = float(dato)
    print(f"Valore: {valore:.1f}")  # Valore: 3.5
else:
    print("Non è un numero")
```

**Regola da ricordare:** `.isdigit()` va bene per interi senza segno (un CAP, un anno, una matricola); per i decimali bisogna prima togliere il punto.
