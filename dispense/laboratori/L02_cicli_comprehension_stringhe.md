# Laboratorio 2 — Cicli e stringhe

*Esercizi di Halloween*

**Prerequisiti:** lezioni T09 (Cicli) e T10 (Stringhe).

Oggi ci sono solo esercizi, in ordine di difficoltà, a tema Halloween. Per ogni esercizio create un file `.py` con il nome indicato e scrivete il programma da soli. Le liste non servono: bastano `for`, `while`, `range()` e le stringhe.

Ogni esercizio ha la consegna, un esempio di esecuzione e alcuni casi da provare: il programma è corretto quando dà gli stessi risultati. La sfida è per chi finisce prima. Le soluzioni le vediamo all'inizio della lezione T11.

| # | File | Esercizio |
|---|---|---|
| 1 | `epidemia.py` | Epidemia zombie |
| 2 | `apocalisse.py` | Quando cade la città |
| 3 | `venerdi17.py` | Venerdì 17 |
| 4 | `cena_dracula.py` | La cena di Dracula |
| 5 | `epitaffio.py` | L'epitaffio |
| 6 | `anagrammi.py` | Anagrammi maledetti |
| 7 | `bottino.py` | Il bottino della notte |
| 8 | `login_dracula.py` | Il login di Dracula |
| Sfida | `apocalisse_esercito.py` | Apocalisse con esercito |

---

## Promemoria

Gli strumenti che servono oggi. Non usate `sum()`, `min()` e `max()`: i calcoli si fanno con i cicli. `str()` trasforma un numero in stringa.

```python
for i in range(5, 0, -1):    # 5, 4, 3, 2, 1
    print(i, end=" ")         # end=" ": resta sulla stessa riga
print()

conta: int = 0
for carattere in "abracadabra":   # una stringa si scorre carattere per carattere
    if carattere == "a":
        conta += 1                  # alla fine conta vale 5

parola: str = "Python"
print(parola[0], parola[-1], len(parola))   # P n 6
print(parola[::-1])                         # nohtyP
print(parola.upper(), "y" in parola)        # PYTHON True
print("17" in str(2017), "7".isdigit())     # True True
print(12 // 5, 12 % 5)                      # 2 2  (quoziente e resto)
```

---

## Esercizio 1 — Epidemia zombie (`epidemia.py`)

**Consegna**

1. Il giorno 1 c'è un solo infetto e ogni giorno gli infetti raddoppiano.
2. Chiedete il numero di giorni.
3. Con un ciclo `for` stampate una riga per giorno con il numero di infetti.

**Esempio di esecuzione**

```
Giorni: 10
Giorno 1: 1 infetti
Giorno 2: 2 infetti
Giorno 3: 4 infetti
...
Giorno 10: 512 infetti
```

**Provate anche**

- `1` → solo `Giorno 1: 1 infetti`
- `20` → giorno 20: `524288` infetti

---

## Esercizio 2 — Quando cade la città (`apocalisse.py`)

**Consegna**

1. Stesso contagio: il giorno 1 c'è un infetto, poi gli infetti raddoppiano ogni giorno.
2. Chiedete il numero di abitanti della città.
3. Con un `while` trovate il primo giorno in cui gli infetti superano gli abitanti e stampatelo con il numero di infetti.

**Esempio di esecuzione**

```
Abitanti: 210000
La città cade il giorno 19: 262144 infetti
```

**Provate anche**

- Italia, `59000000` → giorno `27`
- `1` → giorno `2`

---

## Esercizio 3 — Venerdì 17 (`venerdi17.py`)

**Consegna**

1. Chiedete un intero `n`.
2. Tra 1 e `n`, un numero porta sfortuna se è divisibile per 17 oppure se contiene "17" (`"17" in str(i)`).
3. Stampate quanti sono e la loro percentuale con un decimale.

**Esempio di esecuzione**

```
Controlla i numeri fino a: 1000
Numeri sfortunati: 76
Percentuale: 7.6%
```

**Provate anche**

- `100` → `5`, `5.0%`
- `2026` → `250`, `12.3%`

---

## Esercizio 4 — La cena di Dracula (`cena_dracula.py`)

**Consegna**

1. Il conte ha un certo numero di sacche di sangue e vuole dividerle tra i commensali: tutti devono averne lo stesso numero e non deve avanzare niente.
2. Chiedete il numero di sacche; se non è positivo stampate un errore.
3. Per ogni numero di commensali da 1 al numero di sacche, se la divisione è esatta (`%`) stampate quante sacche riceve ognuno (`//`). Contate le possibilità.
4. Se le possibilità sono esattamente due, il numero di sacche è primo: stampatelo.

**Esempio di esecuzione**

```
Sacche di sangue: 12
Commensali 1, sacche a testa 12
Commensali 2, sacche a testa 6
Commensali 3, sacche a testa 4
Commensali 4, sacche a testa 3
Commensali 6, sacche a testa 2
Commensali 12, sacche a testa 1
Possibilità: 6
```

**Provate anche**

- `13` → solo 1 o 13 commensali: 13 è primo
- `1` → una sola possibilità (1 non è primo)
- `0` → errore

---

## Esercizio 5 — L'epitaffio (`epitaffio.py`)

**Consegna**

1. L'incisore del cimitero si fa pagare a carattere: lettere 2 EUR, cifre 3 EUR, punteggiatura e simboli 1 EUR, spazi gratis. Scrivete i prezzi in costanti.
2. Chiedete il testo dell'epitaffio e scorretelo carattere per carattere, contando lettere, cifre, spazi e altri caratteri (`isalpha()`, `isdigit()`).
3. Stampate i quattro conteggi, il costo totale e la percentuale di lettere sul totale dei caratteri, con un decimale.

**Esempio di esecuzione**

```
Epitaffio: Qui giace Dracula, morto il 31/10/1897. R.I.P.
Lettere: 25  Cifre: 8
Spazi: 6  Altri: 7
Costo dell'incisione: 81 EUR
Lettere sul totale: 54.3%
```

**Provate anche**

- `R.I.P.` → 3 lettere e 3 simboli: `9 EUR`, `50.0%`
- testo vuoto → `0 EUR`, niente percentuale (si dividerebbe per zero)

---

## Esercizio 6 — Anagrammi maledetti (`anagrammi.py`)

**Consegna**

1. Due parole sono anagrammi se contengono le stesse lettere, ognuna lo stesso numero di volte.
2. Chiedete due parole, passatele in minuscolo e togliete gli spazi.
3. Usate la costante `ALFABETO = "abcdefghijklmnopqrstuvwxyz"`: per ogni lettera confrontate `count()` nelle due parole.
4. Alla prima lettera che non torna stampate i due conteggi; alla fine dite se sono anagrammi.

**Esempio di esecuzione**

```
Prima parola: Satan
Seconda parola: Santa
Sono anagrammi
```

**Provate anche**

- `mostro` / `stormo` → anagrammi
- `lapide` / `pedali` → anagrammi
- `vampiro` / `zombie` → `Lettera a: 1 nella prima, 0 nella seconda`

---

## Esercizio 7 — Il bottino della notte (`bottino.py`)

**Consegna**

1. Leggete con un `while`, casa per casa, quante caramelle avete preso, finché l'utente scrive `fine` (anche in maiuscolo). I valori negativi vanno segnalati e ignorati.
2. Una casa che dà 0 caramelle ha chiuso la porta.
3. Alla fine stampate: case visitate, caramelle totali, media per casa con un decimale, casa più generosa (numero e caramelle), percentuale di porte chiuse.
4. Se non avete visitato nessuna casa, stampate un messaggio. Il testo letto va convertito con `int()` solo dopo aver controllato che non sia `fine`.

**Esempio di esecuzione**

```
Casa 1, caramelle (fine per finire): 5
Casa 2, caramelle (fine per finire): 0
Casa 3, caramelle (fine per finire): 12
Casa 4, caramelle (fine per finire): -2
Valore non valido, ignorato
Casa 4, caramelle (fine per finire): 3
Casa 5, caramelle (fine per finire): 0
Casa 6, caramelle (fine per finire): fine
Case visitate: 5
Caramelle totali: 20
Media per casa: 4.0
Casa più generosa: la 3, con 12 caramelle
Porte chiuse: 40.0%
```

**Provate anche**

- subito `fine` → nessuna casa visitata
- `0`, `0`, `FINE` → porte chiuse `100.0%`, nessuna casa generosa

---

## Esercizio 8 — Il login di Dracula (`login_dracula.py`)

**Consegna**

1. Chiedete una password e controllate i requisiti: almeno 8 caratteri, almeno una maiuscola e una cifra, nessuno spazio.
2. Il conte non accetta password che contengono "aglio" o "croce", anche scritte in maiuscolo: usate `lower()` e `in`.
3. Per ogni requisito mancante stampate un messaggio.
4. Richiedete la password finché non è valida.

**Esempio di esecuzione**

```
Password: ciao
- servono almeno 8 caratteri
- manca una lettera maiuscola
- manca una cifra
Password: Aglio2026x
- parola proibita: il conte non gradisce
Password: Nosferatu1922
Benvenuto nel castello
```

**Provate anche**

- `Conte Dracula1` → niente spazi
- `SantaCROCE99` → parola proibita

---

## Sfida — Apocalisse con esercito (`apocalisse_esercito.py`)

**Consegna**

1. Chiedete gli zombie e i soldati iniziali.
2. Ogni giorno, partendo dai valori di inizio giornata: ogni 10 zombie infettano un soldato, che diventa zombie; ogni soldato elimina 2 zombie. Né gli infettati né gli eliminati possono superare quelli che ci sono.
3. Gli zombie sopravvissuti contagiano i civili e crescono del 50% (parte intera).
4. Stampate una riga per giorno, dal giorno 0. Fermatevi se gli zombie arrivano a 0 (vittoria), se i soldati arrivano a 0 (sconfitta) o dopo 30 giorni, poi stampate l'esito.

**Esempio di esecuzione**

```
Zombie iniziali: 100
Soldati iniziali: 31
Giorno 0: 100 zombie, 31 soldati
Giorno 1: 67 zombie, 21 soldati
Giorno 2: 43 zombie, 15 soldati
Giorno 3: 23 zombie, 11 soldati
Giorno 4: 3 zombie, 9 soldati
Giorno 5: 0 zombie, 9 soldati
Vittoria il giorno 5, restano 9 soldati
```

**Provate anche**

- `100`, `30` → `Sconfitta il giorno 5, restano 61 zombie`
- `6`, `1` → 6 zombie ogni giorno, dopo 30 giorni la guerra continua
- Con 200 zombie, trovate il numero minimo di soldati per vincere.

---

## Domande di verifica

1. Quali numeri produce `range(1, 10)`? E `range(10, 0, -2)`?
2. In `apocalisse.py` serve un `while` e non un `for`: perché?
3. In `venerdi17.py`, perché il 17 viene contato una volta sola anche se soddisfa entrambe le condizioni?
4. In `cena_dracula.py`, che differenza c'è tra `12 % 5` e `12 // 5`?
5. In `anagrammi.py`, perché si scorre l'alfabeto e non le lettere della prima parola?
6. In `bottino.py` il massimo può partire da 0, mentre il minimo non potrebbe. Perché?
7. Nella sfida, perché infettati ed eliminati vanno calcolati prima di aggiornare zombie e soldati?
