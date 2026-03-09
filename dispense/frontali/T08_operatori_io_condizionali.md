# Lezione 8 — Operatori, I/O e strutture condizionali

## Introduzione

Nella lezione precedente abbiamo imparato a creare variabili e a dare loro un tipo. Ma un programma che si limita a memorizzare valori non è molto utile. Oggi aggiungiamo tre capacità fondamentali: **calcolare** (operatori), **comunicare** (input/output) e **decidere** (condizionali). Alla fine di questa lezione, i vostri programmi saranno in grado di interagire con l'utente e prendere decisioni basate sui dati.

---

## Operatori

### Operatori aritmetici

```python
a: int = 17
b: int = 5

print(a + b)    # 22  — addizione
print(a - b)    # 12  — sottrazione
print(a * b)    # 85  — moltiplicazione
print(a / b)    # 3.4 — divisione vera (restituisce SEMPRE un float)
print(a // b)   # 3   — divisione intera (tronca verso il basso)
print(a % b)    # 2   — modulo (resto della divisione)
print(a ** b)   # 1419857 — potenza (17⁵)
```

**Nota storica importante:** in Python 2, la divisione `/` tra due interi restituiva un intero (`17 / 5` dava `3`, non `3.4`). Questa scelta era fonte di bug insidiosi — immaginate di calcolare una media: `somma / n` dava un intero troncato se entrambi erano `int`. Python 3 ha corretto questo comportamento: `/` restituisce sempre un `float`. Se volete la divisione intera, usate esplicitamente `//`.

Il modulo (`%`) è più utile di quanto sembri: serve per verificare la divisibilità (`n % 2 == 0` → n è pari), per ciclare tra valori (`i % n` riporta l'indice nell'intervallo 0..n-1), per estrarre cifre.

### Operatori di confronto

```python
x: int = 10
y: int = 20

print(x == y)   # False — uguaglianza (valore)
print(x != y)   # True  — diverso
print(x < y)    # True  — minore
print(x > y)    # False — maggiore
print(x <= y)   # True  — minore o uguale
print(x >= y)   # False — maggiore o uguale
```

Gli operatori di confronto restituiscono un `bool` (`True` o `False`).

**`==` vs `is`:** una distinzione fondamentale.

```python
a: list[int] = [1, 2, 3]
b: list[int] = [1, 2, 3]
c: list[int] = a

print(a == b)   # True  — stesso VALORE
print(a is b)   # False — oggetti DIVERSI in memoria
print(a is c)   # True  — stesso OGGETTO (c è un alias di a)
```

`==` confronta il **valore**: "contengono la stessa cosa?". `is` confronta l'**identità**: "sono lo stesso oggetto in memoria?". Per i confronti di valore, usate sempre `==`. L'unica eccezione idiomatica è il confronto con `None`: `if x is None:` (non `if x == None:`).

### Operatori logici

```python
eta: int = 20
reddito: float = 15000.0

print(eta >= 18 and reddito < 20000)   # True — entrambe vere
print(eta < 18 or reddito > 50000)     # False — nessuna vera
print(not (eta >= 18))                 # False — negazione
```

Questi sono gli stessi AND, OR, NOT dell'algebra booleana che avete studiato nella Lezione 2. Ogni `if` che scriverete è un'applicazione pratica di Boole.

**Short-circuit evaluation:** Python è "pigro" — smette di valutare appena conosce il risultato:

```python
# Se la prima condizione è False, and non valuta la seconda
# (tanto il risultato sarà False comunque)
x: int = 0
if x != 0 and 10 / x > 2:  # la divisione per zero NON viene eseguita
    print("OK")
```

Questo non è solo un'ottimizzazione — è una garanzia di sicurezza che potete sfruttare.

### Operatori di appartenenza

```python
vocali: str = "aeiou"
print("a" in vocali)       # True
print("b" not in vocali)   # True

numeri: list[int] = [1, 2, 3, 4, 5]
print(3 in numeri)          # True
```

`in` è un operatore potentissimo che useremo costantemente. Funziona con stringhe, liste, tuple, set, dizionari.

### Precedenza degli operatori

Come in matematica, gli operatori hanno una precedenza: `**` prima di `*`, `/`, `//`, `%`, che vengono prima di `+` e `-`. I confronti vengono dopo le operazioni aritmetiche, e gli operatori logici per ultimi.

```python
risultato: bool = 3 + 5 * 2 > 10 and not False
# Equivale a: ((3 + (5 * 2)) > 10) and (not False)
# Cioè:       (3 + 10 > 10) and True
# Cioè:       (13 > 10) and True
# Cioè:       True and True → True
```

**Best practice:** non affidatevi alla memorizzazione della precedenza. Usate le **parentesi** per rendere esplicite le vostre intenzioni:

```python
# Chiaro: le parentesi esplicitano l'ordine
risultato: bool = ((3 + (5 * 2)) > 10) and (not False)
```

---

## Input e Output

### `print()`: comunicare con l'utente

Abbiamo già usato `print()`, ma ha opzioni utili:

```python
nome: str = "Anna"
eta: int = 22

# Argomenti multipli (separati da spazio per default)
print("Nome:", nome, "Età:", eta)  # Nome: Anna Età: 22

# Cambiare il separatore
print("2024", "01", "15", sep="-")  # 2024-01-15

# Cambiare il carattere finale (default: a capo)
print("Caricamento", end="...")
print("fatto!")  # Caricamento...fatto!
```

### f-string: il modo moderno di formattare

Le **f-string** (formatted string literals), introdotte in Python 3.6, sono il modo più leggibile e potente per formattare l'output:

```python
nome: str = "Anna"
media: float = 28.6667
esami: int = 12

# Sintassi base: f"testo {espressione}"
print(f"Studentessa: {nome}")
print(f"Media: {media}")
print(f"Esami sostenuti: {esami}")

# Formattazione dei numeri
print(f"Media: {media:.2f}")        # 28.67 (2 decimali)
print(f"Media: {media:.1f}")        # 28.7 (1 decimale)
print(f"Percentuale: {0.856:.1%}")  # 85.6%

# Allineamento
print(f"{'Nome':<15}{'Voto':>5}")   # allineato a sinistra/destra
print(f"{'Anna':<15}{28:>5}")
print(f"{'Marco':<15}{30:>5}")

# Espressioni dentro le graffe
print(f"Il doppio è {eta * 2}")
print(f"Tra 5 anni avrà {eta + 5} anni")
```

Le f-string sono preferite a tutti gli altri metodi di formattazione (`.format()`, `%`) per la loro leggibilità.

### `input()`: leggere dall'utente

```python
nome: str = input("Come ti chiami? ")
print(f"Ciao, {nome}!")
```

**Attenzione fondamentale:** `input()` restituisce **sempre una stringa**, anche se l'utente inserisce un numero:

```python
# ERRORE COMUNE:
eta = input("Quanti anni hai? ")
print(eta + 1)  # TypeError! "25" + 1 non ha senso

# CORRETTO:
eta: int = int(input("Quanti anni hai? "))
print(eta + 1)  # 26
```

La conversione può fallire se l'utente inserisce qualcosa di non numerico:

```python
eta: int = int(input("Quanti anni hai? "))
# Se l'utente scrive "venticinque" → ValueError!
```

Impareremo a gestire questi errori con `try/except` più avanti. Per ora, assumiamo che l'utente sia collaborativo.

---

## Strutture condizionali

### Il flusso sequenziale

Normalmente, Python esegue le istruzioni una dopo l'altra, dall'alto verso il basso:

```python
a: int = 5
b: int = 3
c: int = a + b
print(c)  # 8
```

Ma i programmi reali devono **prendere decisioni**. L'istruzione `if` permette di eseguire un blocco di codice solo se una condizione è vera.

### `if`

```python
voto: int = 25

if voto >= 18:
    print("Esame superato!")
```

La struttura è:
1. La parola chiave `if`
2. Una **condizione** (un'espressione che produce un `bool`)
3. I due punti `:`
4. Il **corpo** (le istruzioni indentate che vengono eseguite se la condizione è vera)

### `if/else`

```python
voto: int = 15

if voto >= 18:
    print("Esame superato!")
else:
    print("Esame non superato.")
```

Due strade: una sola viene percorsa. Non è possibile che vengano eseguite entrambe.

### `if/elif/else`

```python
def valuta_voto(voto: int) -> str:
    """Restituisce una valutazione testuale del voto."""
    if voto >= 28:
        return "Ottimo"
    elif voto >= 24:
        return "Buono"
    elif voto >= 18:
        return "Sufficiente"
    else:
        return "Insufficiente"
```

`elif` (*else if*) permette di valutare condizioni multiple. Le condizioni vengono valutate **in ordine**, e si esegue il blocco della **prima** condizione vera. Se nessuna è vera, si esegue `else`.

**Perché `elif` e non una catena di `if`?** Perché con `elif` le condizioni sono **mutuamente esclusive**: appena una è vera, le altre non vengono nemmeno valutate. Con `if` multipli indipendenti, ogni condizione viene valutata sempre.

### L'operatore ternario

Per condizioni semplici con assegnamento:

```python
# Forma estesa
if voto >= 18:
    esito: str = "Promosso"
else:
    esito = "Bocciato"

# Forma compatta (operatore ternario)
esito: str = "Promosso" if voto >= 18 else "Bocciato"
```

Usatelo solo quando rende il codice **più leggibile**, non per ogni `if/else`.

### Condizioni composte

```python
eta: int = 25
reddito: float = 18000.0
residente: bool = True

# AND: entrambe devono essere vere
if eta >= 18 and reddito < 20000:
    print("Ha diritto alla borsa di studio")

# OR: almeno una deve essere vera
if eta < 18 or not residente:
    print("Non può iscriversi")

# Condizioni concatenate (Python le supporta nativamente!)
voto: int = 25
if 18 <= voto <= 30:  # elegante! In altri linguaggi: voto >= 18 and voto <= 30
    print("Voto valido")
```

---

## Best practice per le condizioni

### Truthy e falsy

In Python, molti valori possono essere interpretati come `True` o `False` in un contesto booleano:

**Falsy** (valutati come `False`):
- `False`
- `0`, `0.0`
- `""` (stringa vuota)
- `[]` (lista vuota), `()` (tupla vuota), `{}` (dizionario vuoto), `set()` (set vuoto)
- `None`

**Truthy** (valutati come `True`): **tutto il resto**.

```python
lista: list[int] = []

# MALE: confronto esplicito inutile
if len(lista) == 0:
    print("Lista vuota")

# BENE: pythonic, sfrutta truthy/falsy
if not lista:
    print("Lista vuota")
```

### Non confrontare con `True`/`False`

```python
attivo: bool = True

# MALE:
if attivo == True:
    print("È attivo")

# BENE:
if attivo:
    print("È attivo")

# MALE:
if attivo == False:
    print("Non è attivo")

# BENE:
if not attivo:
    print("Non è attivo")
```

### Early return

Quando una funzione ha molte condizioni, gestite i casi anomali all'inizio e uscite subito, lasciando il caso principale non indentato:

```python
# MALE: nesting profondo
def calcola_media(voti: list[int]) -> float:
    if len(voti) > 0:
        if all(0 <= v <= 30 for v in voti):
            return sum(voti) / len(voti)
        else:
            raise ValueError("Voti non validi")
    else:
        raise ValueError("Lista vuota")

# BENE: early return, logica piatta
def calcola_media(voti: list[int]) -> float:
    if not voti:
        raise ValueError("Lista vuota")
    if not all(0 <= v <= 30 for v in voti):
        raise ValueError("Voti non validi")
    return sum(voti) / len(voti)
```

### Validazione dell'input

Non fidatevi mai dei dati che vengono dall'esterno. L'utente può inserire qualsiasi cosa:

```python
# Validazione semplice
eta_str: str = input("Età: ")
if not eta_str.isdigit():
    print("Errore: inserisci un numero intero positivo")
else:
    eta: int = int(eta_str)
    if eta < 0 or eta > 150:
        print("Errore: età non realistica")
    else:
        print(f"Hai {eta} anni")
```

---

## Domande di verifica

1. **Qual è la differenza tra `/` e `//` in Python?** Perché Python 3 ha cambiato il comportamento di `/`?

2. **Qual è la differenza tra `==` e `is`?** Quando si usa `is`?

3. **Cos'è la short-circuit evaluation?** Fate un esempio pratico.

4. **`input()` restituisce sempre una stringa.** Perché questa scelta? Cosa dovete fare se volete leggere un numero?

5. **Cosa sono i valori truthy e falsy?** Elencate almeno tre valori falsy.

6. **Cos'è l'early return e perché migliora la leggibilità del codice?**

7. **Quando è appropriato usare l'operatore ternario?** Quando è meglio evitarlo?

8. **Perché è importante validare l'input dell'utente?**

---

## Esercizi

### Base

1. Scrivete un programma che legge due numeri dall'utente e stampa la somma, la differenza, il prodotto e il quoziente, formattati con 2 decimali.

2. Scrivete un programma che legge un voto (intero) e stampa:
   - "Insufficiente" se < 18
   - "Sufficiente" se tra 18 e 23
   - "Buono" se tra 24 e 27
   - "Ottimo" se tra 28 e 30

3. Scrivete un programma che legge un anno e determina se è bisestile. Un anno è bisestile se è divisibile per 4, **tranne** se è divisibile per 100, **a meno che** non sia divisibile per 400.

### Intermedio

4. Scrivete una **calcolatrice** interattiva che:
   - Legge due numeri e un'operazione (+, -, *, /)
   - Esegue l'operazione e stampa il risultato formattato
   - Gestisce la divisione per zero con un messaggio di errore

5. Scrivete un programma che calcola l'**IMC** (Indice di Massa Corporea: peso/altezza²) e classifica il risultato:
   - < 18.5: Sottopeso
   - 18.5-24.9: Normopeso
   - 25.0-29.9: Sovrappeso
   - ≥ 30.0: Obeso

   Usate type hints, f-string e validazione dell'input.

6. Scrivete un programma che, dato un importo e un'aliquota fiscale, calcola:
   - L'imposta
   - Il netto
   - Se l'imposta supera una certa soglia, applica una detrazione

### Avanzato

7. Scrivete un programma che simula un **bancomat semplificato**:
   ```
   Saldo attuale: €1000.00
   Operazione (D=deposito, P=prelievo, S=saldo): P
   Importo: 200
   Prelievo di €200.00 effettuato.
   Nuovo saldo: €800.00
   ```
   Gestite: saldo insufficiente, importi negativi, operazione non valida.

8. Scrivete una funzione `classifica_triangolo(a: float, b: float, c: float) -> str` che, dati i tre lati di un triangolo:
   - Verifica che i lati formino un triangolo valido (disuguaglianza triangolare)
   - Classifica il triangolo come equilatero, isoscele o scaleno
   - Usate type hints e docstring

---

## Osservazioni finali

Oggi avete aggiunto tre capacità fondamentali ai vostri programmi:

- **Calcolare** con gli operatori — e avete visto che gli operatori logici sono esattamente l'algebra di Boole della Lezione 2, applicata al codice.
- **Comunicare** con l'utente — e avete imparato che l'input dall'esterno è sempre inaffidabile e va validato.
- **Decidere** con le condizioni — e il vostro codice ha iniziato a comportarsi diversamente in base ai dati.

Le best practice introdotte oggi — truthy/falsy, early return, validazione dell'input — non sono regole arbitrarie. Sono il risultato di decenni di esperienza collettiva su cosa rende il codice leggibile, manutenibile e corretto.

Nella prossima lezione aggiungeremo la **ripetizione**: i cicli `for` e `while`. Con variabili, condizioni e cicli, avrete i tre mattoni fondamentali di qualsiasi programma.
