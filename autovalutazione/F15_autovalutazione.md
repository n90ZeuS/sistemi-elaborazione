# Autovalutazione — F15: File, Eccezioni e CSV

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
try:
    print("A")
    x = 10 / 2
    print("B")
except ZeroDivisionError:
    print("C")
else:
    print("D")
finally:
    print("E")
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
A
B
D
E
```

**Spiegazione:** Passo per passo:
1. `print("A")` viene eseguito normalmente.
2. `x = 10 / 2` non causa errore (risultato: `5.0`).
3. `print("B")` viene eseguito normalmente.
4. Nessuna eccezione, quindi `except` viene saltato (`"C"` non appare).
5. Il blocco `else` viene eseguito **solo se non ci sono state eccezioni**: stampa `"D"`.
6. Il blocco `finally` viene eseguito **sempre**, con o senza eccezione: stampa `"E"`.
</details>

---

### Esercizio 2

```python
try:
    print("inizio")
    risultato = int("abc")
    print("conversione riuscita")
except ValueError:
    print("errore di conversione")
except TypeError:
    print("errore di tipo")
finally:
    print("fine")
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
inizio
errore di conversione
fine
```

**Spiegazione:**
1. `print("inizio")` viene eseguito.
2. `int("abc")` causa un `ValueError` perche' `"abc"` non e' convertibile in intero.
3. L'esecuzione salta **immediatamente** al blocco `except ValueError`. La riga `print("conversione riuscita")` non viene mai raggiunta.
4. Viene stampato `"errore di conversione"`.
5. `finally` viene eseguito sempre: stampa `"fine"`.
</details>

---

### Esercizio 3

```python
def leggi_numero(testo):
    try:
        return int(testo)
    except ValueError:
        return -1
    finally:
        print("tentativo completato")

valore = leggi_numero("42")
print(f"Risultato: {valore}")
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
tentativo completato
Risultato: 42
```

**Spiegazione:** Anche quando c'e' un `return` nel blocco `try`, il blocco `finally` viene eseguito **prima** che la funzione restituisca il valore. Quindi `"tentativo completato"` appare per primo. Poi la funzione restituisce `42` (la conversione ha successo) e viene stampato `"Risultato: 42"`.
</details>

---

## Trova l'errore

### Esercizio 4

```python
# Leggiamo un file e contiamo le righe
f = open("dati.txt", "r")
righe = f.readlines()
print(f"Il file ha {len(righe)} righe")
# ...altro codice qui...
# Ops! Se c'e' un errore sopra, il file non viene mai chiuso
```

<details>
<summary>Mostra la risposta</summary>

**Problema:** Il file viene aperto ma non viene mai chiuso esplicitamente. Se si verifica un errore tra `open()` e la fine del programma, il file rimane aperto, occupando risorse del sistema.

**Correzione:**
```python
# Usare il context manager 'with' che chiude il file automaticamente
with open("dati.txt", "r") as f:
    righe = f.readlines()
    print(f"Il file ha {len(righe)} righe")
# Il file e' automaticamente chiuso qui, anche in caso di errore
```

**Lezione:** Usate **sempre** `with open(...) as f:` per aprire i file. Il context manager garantisce che il file venga chiuso automaticamente, anche se si verifica un'eccezione.
</details>

---

### Esercizio 5

```python
# Leggiamo un file CSV con dati in italiano (nomi con accenti)
with open("studenti.csv", "r") as f:
    contenuto = f.read()
    print(contenuto)
```

<details>
<summary>Mostra la risposta</summary>

**Problema potenziale:** Su alcuni sistemi operativi (specialmente Windows), l'encoding di default potrebbe non essere UTF-8. Se il file contiene caratteri accentati (come e', a', ecc.), la lettura potrebbe produrre caratteri errati o causare un `UnicodeDecodeError`.

**Correzione:**
```python
# Specificare sempre l'encoding esplicitamente
with open("studenti.csv", "r", encoding="utf-8") as f:
    contenuto = f.read()
    print(contenuto)
```

**Lezione:** Specificate sempre `encoding="utf-8"` quando aprite file di testo, soprattutto se contengono caratteri non ASCII (accenti, simboli speciali). Questo rende il codice portabile su tutti i sistemi operativi.
</details>

---

### Esercizio 6

```python
# Calcoliamo la media dei voti da un file
with open("voti.txt", "r", encoding="utf-8") as f:
    righe = f.readlines()

somma = 0
for riga in righe:
    somma += int(riga)

media = somma / len(righe)
print(f"Media: {media}")
```

<details>
<summary>Mostra la risposta</summary>

**Problemi multipli:**
1. Se il file `"voti.txt"` non esiste, si ottiene `FileNotFoundError` senza alcun messaggio utile.
2. Se una riga contiene testo non numerico (intestazione, riga vuota), `int(riga)` causa un `ValueError`.
3. Se il file e' vuoto, `len(righe)` e' 0 e si ottiene `ZeroDivisionError`.

**Correzione:**
```python
try:
    with open("voti.txt", "r", encoding="utf-8") as f:
        righe = f.readlines()
except FileNotFoundError:
    print("Errore: il file 'voti.txt' non esiste.")
else:
    voti = []
    for riga in righe:
        riga = riga.strip()
        if riga:  # ignora righe vuote
            try:
                voti.append(int(riga))
            except ValueError:
                print(f"Attenzione: '{riga}' non e' un numero, ignorato.")

    if voti:
        media = sum(voti) / len(voti)
        print(f"Media: {media}")
    else:
        print("Nessun voto valido trovato.")
```

**Lezione:** Quando lavorate con file, gestite sempre le eccezioni probabili: `FileNotFoundError` per file mancanti, `ValueError` per dati malformati e `ZeroDivisionError` per divisioni per zero.
</details>

---

## Completa il codice

### Esercizio 7

Completa la funzione che legge un file CSV di voti e restituisce la media per studente.

Il file `voti.csv` ha questo formato:
```
nome,voto
Alice,28
Bob,24
Alice,30
Bob,27
Carla,26
```

```python
import csv

def media_per_studente(nome_file):
    """Legge un CSV e restituisce un dizionario {nome: media_voti}.

    Args:
        nome_file: percorso del file CSV.

    Returns:
        Dizionario con la media dei voti per ogni studente.
    """
    registro = {}

    # --- COMPLETA: apri il file e leggi il CSV ---

        # --- COMPLETA: per ogni riga, accumula i voti ---

    # --- COMPLETA: calcola la media per ogni studente ---

    return medie

# Test (supponendo che il file esista)
# risultato = media_per_studente("voti.csv")
# print(risultato)
# Output atteso: {'Alice': 29.0, 'Bob': 25.5, 'Carla': 26.0}
```

<details>
<summary>Mostra la soluzione</summary>

```python
import csv

def media_per_studente(nome_file):
    """Legge un CSV e restituisce un dizionario {nome: media_voti}.

    Args:
        nome_file: percorso del file CSV.

    Returns:
        Dizionario con la media dei voti per ogni studente.
    """
    registro = {}

    with open(nome_file, "r", encoding="utf-8") as f:
        lettore = csv.DictReader(f)
        for riga in lettore:
            nome = riga["nome"]
            voto = int(riga["voto"])
            if nome not in registro:
                registro[nome] = []
            registro[nome].append(voto)

    medie = {}
    for nome, voti in registro.items():
        medie[nome] = sum(voti) / len(voti)

    return medie

# risultato = media_per_studente("voti.csv")
# print(risultato)
# Output: {'Alice': 29.0, 'Bob': 25.5, 'Carla': 26.0}
```

**Spiegazione:** Usiamo `csv.DictReader` che legge automaticamente l'intestazione e permette di accedere ai campi per nome. Per ogni riga, accumuliamo i voti in una lista. Infine calcoliamo la media dividendo la somma per il numero di voti.
</details>

---

### Esercizio 8

Completa la funzione che legge un valore numerico dall'utente con gestione degli errori.

```python
def chiedi_numero(messaggio, minimo=None, massimo=None):
    """Chiede un numero all'utente, ripetendo in caso di input non valido.

    Args:
        messaggio: testo da mostrare all'utente.
        minimo: valore minimo accettato (opzionale).
        massimo: valore massimo accettato (opzionale).

    Returns:
        Il numero inserito dall'utente.
    """
    while True:
        # --- COMPLETA: chiedi input e gestisci gli errori ---
        pass

# Esempio d'uso:
# voto = chiedi_numero("Inserisci il voto (18-30): ", minimo=18, massimo=30)
# print(f"Voto inserito: {voto}")
```

<details>
<summary>Mostra la soluzione</summary>

```python
def chiedi_numero(messaggio, minimo=None, massimo=None):
    """Chiede un numero all'utente, ripetendo in caso di input non valido.

    Args:
        messaggio: testo da mostrare all'utente.
        minimo: valore minimo accettato (opzionale).
        massimo: valore massimo accettato (opzionale).

    Returns:
        Il numero inserito dall'utente (float).
    """
    while True:
        try:
            valore = float(input(messaggio))
        except ValueError:
            print("Errore: inserisci un numero valido.")
            continue

        if minimo is not None and valore < minimo:
            print(f"Errore: il valore deve essere almeno {minimo}.")
            continue
        if massimo is not None and valore > massimo:
            print(f"Errore: il valore deve essere al massimo {massimo}.")
            continue

        return valore

# Esempio d'uso:
# voto = chiedi_numero("Inserisci il voto (18-30): ", minimo=18, massimo=30)
# print(f"Voto inserito: {voto}")
```

**Spiegazione:** Il ciclo `while True` ripete la richiesta finche' l'utente non inserisce un valore valido. `try/except ValueError` cattura input non numerici. I controlli su `minimo` e `massimo` (con `is not None` per permettere il valore `0`) garantiscono che il numero sia nel range desiderato. `continue` torna all'inizio del ciclo, `return` esce dalla funzione.
</details>
