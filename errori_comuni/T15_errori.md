# Errori comuni — T15: File, dati e gestione errori

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione T15.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

---

### Errore 1: File non chiuso senza il costrutto `with`

**Codice errato:**
```python
f = open("dati.txt", "r")
contenuto = f.read()
# lo studente dimentica f.close()
# se si verifica un errore prima di close(), il file resta aperto
```

**Cosa succede:**
```
Nessun errore immediato, ma il file resta aperto in memoria. Con molti file aperti
contemporaneamente si rischia: ResourceWarning: unclosed file <_io.TextIOWrapper ...>
```

**Perché è sbagliato:** Se non si chiude il file con `f.close()`, le risorse del sistema operativo non vengono rilasciate. Peggio ancora, se si verifica un'eccezione tra `open()` e `close()`, il file non verrà mai chiuso. Il costrutto `with` garantisce la chiusura automatica anche in caso di errore.

**Codice corretto:**
```python
with open("dati.txt", "r") as f:
    contenuto = f.read()
# il file viene chiuso automaticamente all'uscita dal blocco with
```

**Regola da ricordare:** Usa sempre `with open(...) as f:` per aprire i file: garantisce la chiusura automatica anche in caso di errore.

---

### Errore 2: Encoding sbagliato nella lettura di un file

**Codice errato:**
```python
with open("dati_italiani.csv", "r") as f:
    contenuto = f.read()
    print(contenuto)
```

**Cosa succede:**
```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe0 in position 42: invalid continuation byte
```
Oppure i caratteri accentati (à, è, ù) appaiono come simboli incomprensibili.

**Perché è sbagliato:** Molti file creati su Windows con programmi italiani usano la codifica `latin-1` (ISO-8859-1) o `cp1252`, non `utf-8`. Se non si specifica l'encoding corretto, Python (che usa `utf-8` di default) non riesce a decodificare i byte dei caratteri accentati.

**Codice corretto:**
```python
# Specifica l'encoding corretto
with open("dati_italiani.csv", "r", encoding="utf-8") as f:
    contenuto = f.read()

# Se il file è stato creato su Windows con Excel:
with open("dati_italiani.csv", "r", encoding="latin-1") as f:
    contenuto = f.read()

# Se non si conosce l'encoding, si può provare:
with open("dati_italiani.csv", "r", encoding="utf-8", errors="replace") as f:
    contenuto = f.read()  # i caratteri non decodificabili diventano '�'
```

**Regola da ricordare:** Specifica sempre `encoding="utf-8"` (o l'encoding appropriato) quando apri un file di testo, soprattutto con caratteri accentati.

---

### Errore 3: Leggere un file inesistente senza gestire l'errore

**Codice errato:**
```python
with open("risultati_esame.csv", "r") as f:
    dati = f.read()
```

**Cosa succede:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'risultati_esame.csv'
```
Il programma si interrompe bruscamente.

**Perché è sbagliato:** Se il file non esiste (nome sbagliato, percorso errato, file non ancora creato), Python solleva un `FileNotFoundError`. In un programma reale bisogna prevedere questa eventualità e gestirla con un blocco `try/except`, dando un messaggio utile all'utente.

**Codice corretto:**
```python
import os

# Opzione 1: try/except
try:
    with open("risultati_esame.csv", "r") as f:
        dati = f.read()
except FileNotFoundError:
    print("Errore: il file 'risultati_esame.csv' non è stato trovato.")
    print("Verifica che il nome e il percorso siano corretti.")
    dati = ""

# Opzione 2: controllo preventivo
percorso = "risultati_esame.csv"
if os.path.exists(percorso):
    with open(percorso, "r") as f:
        dati = f.read()
else:
    print(f"Il file '{percorso}' non esiste.")
    dati = ""
```

**Regola da ricordare:** Proteggi sempre la lettura di file con `try/except FileNotFoundError` per evitare che il programma si blocchi se il file non esiste.

---

### Errore 4: CSV con separatore sbagliato

**Codice errato:**
```python
import csv

with open("dati.csv", "r") as f:
    lettore = csv.reader(f)
    for riga in lettore:
        print(riga)
```

**Cosa succede:**
```
['Nome;Cognome;Voto;Data']
['Luca;Rossi;28;15/01/2025']
['Anna;Bianchi;30;16/01/2025']
```
Ogni riga è una lista con un solo elemento (la riga intera come stringa) invece di essere separata nei singoli campi.

**Perché è sbagliato:** `csv.reader` usa la virgola `,` come separatore di default, ma molti file CSV italiani (soprattutto quelli esportati da Excel in Italia) usano il punto e virgola `;` come separatore, perché la virgola è già usata come separatore decimale nei numeri.

**Codice corretto:**
```python
import csv

with open("dati.csv", "r") as f:
    lettore = csv.reader(f, delimiter=";")
    for riga in lettore:
        print(riga)
# ['Nome', 'Cognome', 'Voto', 'Data']
# ['Luca', 'Rossi', '28', '15/01/2025']
# ['Anna', 'Bianchi', '30', '16/01/2025']
```

**Regola da ricordare:** Controlla quale separatore usa il file CSV (virgola, punto e virgola, tabulazione) e specificalo con `delimiter=";"` nel `csv.reader`.

---

### Errore 5: Leggere un file già consumato senza `seek()`

**Codice errato:**
```python
with open("dati.txt", "r") as f:
    prima_lettura = f.read()
    print(f"Lunghezza: {len(prima_lettura)}")

    seconda_lettura = f.read()
    print(f"Contenuto: {seconda_lettura}")
```

**Cosa succede:**
```
Lunghezza: 150
Contenuto:
```
La seconda lettura restituisce una stringa vuota, anche se il file contiene dati.

**Perché è sbagliato:** Un file aperto ha un "cursore" che indica la posizione corrente di lettura. Dopo `f.read()`, il cursore è alla fine del file. Una seconda chiamata a `f.read()` parte dalla posizione attuale (la fine) e non trova più nulla da leggere. Bisogna riportare il cursore all'inizio con `f.seek(0)`.

**Codice corretto:**
```python
with open("dati.txt", "r") as f:
    prima_lettura = f.read()
    print(f"Lunghezza: {len(prima_lettura)}")

    f.seek(0)  # riporta il cursore all'inizio del file
    seconda_lettura = f.read()
    print(f"Contenuto: {seconda_lettura}")
```

**Regola da ricordare:** Dopo aver letto un file con `.read()`, il cursore è alla fine: usa `f.seek(0)` per riportarlo all'inizio prima di leggere di nuovo.

---

### Errore 6: Blocco `except` troppo generico

**Codice errato:**
```python
try:
    valore = int(input("Inserisci un numero: "))
    risultato = 100 / valore
    print(f"Risultato: {risultato}")
except:
    print("Si è verificato un errore")
```

**Cosa succede:**
```
Si è verificato un errore
```
Il messaggio non aiuta a capire cosa è andato storto: era un input non numerico? Una divisione per zero? Un altro problema? Inoltre, un `except` generico cattura anche errori di programmazione come `NameError` o `KeyboardInterrupt`, nascondendo bug.

**Perché è sbagliato:** Un blocco `except:` senza specificare il tipo di eccezione cattura tutto, inclusi errori che non ci si aspetta. Questo rende impossibile distinguere tra errori diversi (input sbagliato, divisione per zero, errore di sistema) e nasconde bug nel codice che andrebbero corretti.

**Codice corretto:**
```python
try:
    valore = int(input("Inserisci un numero: "))
    risultato = 100 / valore
    print(f"Risultato: {risultato}")
except ValueError:
    print("Errore: devi inserire un numero intero valido.")
except ZeroDivisionError:
    print("Errore: non puoi dividere per zero.")
except Exception as e:
    print(f"Errore imprevisto: {e}")
```

**Regola da ricordare:** Specifica sempre il tipo di eccezione nel blocco `except` (es. `except ValueError:`) per gestire ogni errore in modo appropriato e non nascondere bug.

---
