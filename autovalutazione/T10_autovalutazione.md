# Autovalutazione — T10: Stringhe

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
s = "Statistica"
print(s[0:4])
print(s[-3:])
print(s[::2])
print(len(s))
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
Stat
ica
Saitc
10
```

**Spiegazione:** `s[0:4]` prende i caratteri dalla posizione 0 alla 3: il 4 è escluso, come in `range()`. `s[-3:]` parte dal terzultimo carattere e arriva in fondo. `s[::2]` prende un carattere sì e uno no partendo dal primo: posizioni 0, 2, 4, 6, 8, cioè `S`, `a`, `i`, `t`, `c`. `len(s)` conta i caratteri: 10.
</details>

---

### Esercizio 2

```python
frase = "Ciao Mondo"
print(frase.lower())
print(frase.upper())
print(frase.replace("Mondo", "Python"))
print(frase)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
ciao mondo
CIAO MONDO
Ciao Python
Ciao Mondo
```

**Spiegazione:** I metodi delle stringhe (`lower()`, `upper()`, `replace()`) restituiscono una **nuova stringa** e non modificano l'originale. Le stringhe in Python sono **immutabili**: non possono essere cambiate dopo la creazione. L'ultima riga lo mostra: `frase` vale ancora `"Ciao Mondo"` dopo le operazioni precedenti.
</details>

---

### Esercizio 3

```python
parola = "statistica"
risultato = ""
for c in parola:
    if c != "t":
        risultato = risultato + c.upper()
print(risultato)
print(parola.count("t"), parola.find("i"))
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
SAISICA
3 4
```

**Spiegazione:** Il ciclo scorre i caratteri di `"statistica"` uno alla volta. Le `t` vengono saltate, gli altri caratteri (`s`, `a`, `i`, `s`, `i`, `c`, `a`) vengono aggiunti in maiuscolo a `risultato`, che parte dalla stringa vuota. `count("t")` conta le `t` (3); `find("i")` restituisce la posizione della prima `i`, cioè 4 (si conta da 0).
</details>

---

### Esercizio 4

```python
quota = 0.1573
media = 27.456
print(f"{quota:.1%}")
print(f"{media:.1f}")
print("3.14".isdigit(), "314".isdigit())
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
15.7%
27.5
False True
```

**Spiegazione:** Il formato `.1%` moltiplica il valore per 100, aggiunge il simbolo `%` e tiene un decimale: `0.1573` diventa `15.7%`. Il formato `.1f` arrotonda a un decimale: `27.456` diventa `27.5`. `isdigit()` restituisce `True` solo se tutti i caratteri sono cifre: in `"3.14"` il punto non è una cifra.
</details>

---

## Trova l'errore

### Esercizio 5

Il codice dovrebbe mettere in maiuscolo la prima lettera di una stringa, ma genera un errore.

```python
nome = "alice"
nome[0] = "A"
print(nome)
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `TypeError: 'str' object does not support item assignment`

**Problema:** Le stringhe sono **immutabili** in Python: non si possono modificare i singoli caratteri. L'operazione `nome[0] = "A"` tenta di cambiare il primo carattere, ma Python non lo permette.

**Soluzione:**
```python
nome = "alice"
nome = "A" + nome[1:]     # creiamo una NUOVA stringa
print(nome)                # stampa: Alice

# Oppure, più semplice:
nome = "alice"
nome = nome.capitalize()   # metodo che mette in maiuscolo la prima lettera
print(nome)                # stampa: Alice
```

Con le stringhe si crea sempre una **nuova** stringa invece di modificare quella esistente.
</details>

---

### Esercizio 6

Il codice dovrebbe stampare l'estensione di un nome di file, oppure un messaggio se l'estensione manca. Con `"relazione"` stampa un risultato sbagliato.

```python
nome_file = "relazione"
punto = nome_file.find(".")
estensione = nome_file[punto + 1:]
print("Estensione:", estensione)
```

<details>
<summary>Mostra la risposta</summary>

**Output:** `Estensione: relazione`

**Problema:** Il nome non contiene il punto, quindi `find(".")` restituisce `-1`. Allora `punto + 1` vale `0` e `nome_file[0:]` è tutta la stringa. Python non segnala nessun errore: il valore `-1` va controllato prima di usarlo come indice.

**Soluzione:**
```python
nome_file = "relazione"
punto = nome_file.find(".")
if punto == -1:
    print("Il file non ha estensione")
else:
    print("Estensione:", nome_file[punto + 1:])
# stampa: Il file non ha estensione
```

Con `nome_file = "dati.csv"` lo stesso codice stampa `Estensione: csv`.
</details>

---

### Esercizio 7

Il codice dovrebbe stampare `Confermato` quando l'utente risponde «sì», scritto in qualunque modo. Con la risposta `"  Si "` stampa il messaggio sbagliato.

```python
risposta = "  Si "
if risposta == "si":
    print("Confermato")
else:
    print("Risposta non riconosciuta")
```

<details>
<summary>Mostra la risposta</summary>

**Output:** `Risposta non riconosciuta`

**Problema:** Il confronto `==` tra stringhe tiene conto di ogni carattere: gli spazi ai bordi e la `S` maiuscola rendono `"  Si "` diversa da `"si"`.

**Soluzione:**
```python
risposta = "  Si "
if risposta.strip().lower() == "si":
    print("Confermato")
else:
    print("Risposta non riconosciuta")
# stampa: Confermato
```

`strip()` toglie gli spazi ai bordi e `lower()` porta tutto in minuscolo. Prima di confrontare un testo scritto da un utente conviene sempre pulirlo così.
</details>

---

## Completa il codice

### Esercizio 8

Completa il codice che conta le vocali (a, e, i, o, u) in una stringa, senza distinguere tra maiuscole e minuscole.

```python
testo = "Ciao Mondo"
vocali = "aeiou"
conta = 0
for c in testo.__________:
    if c ____ vocali:
        conta ________
print(conta)    # deve stampare 5
```

<details>
<summary>Mostra la risposta</summary>

```python
testo = "Ciao Mondo"
vocali = "aeiou"
conta = 0
for c in testo.lower():
    if c in vocali:
        conta += 1
print(conta)    # 5
```

**Spiegazione:** Prima si porta il testo in minuscolo, così le vocali maiuscole vengono riconosciute. Il ciclo scorre ogni carattere e `c in vocali` controlla se il carattere compare nella stringa `"aeiou"`. È il pattern contatore: `conta` parte da 0 e cresce di 1 a ogni vocale. In `"ciao mondo"` le vocali sono `i`, `a`, `o`, `o`, `o`.
</details>

---

### Esercizio 9

Completa il codice che riceve un nome scritto come «cognome nome», con spazi e maiuscole a caso, e stampa `Mario Rossi`.

```python
dato = "  rossi MARIO  "
pulito = dato.__________.__________     # "Rossi Mario"
spazio = pulito.__________
cognome = pulito[__________]
nome = pulito[__________]
print(nome + " " + cognome)            # deve stampare: Mario Rossi
```

<details>
<summary>Mostra la risposta</summary>

```python
dato = "  rossi MARIO  "
pulito = dato.strip().title()     # "Rossi Mario"
spazio = pulito.find(" ")         # 5
cognome = pulito[:spazio]         # "Rossi"
nome = pulito[spazio + 1:]        # "Mario"
print(nome + " " + cognome)       # Mario Rossi
```

**Spiegazione:** `strip()` toglie gli spazi ai bordi e `title()` mette la maiuscola all'inizio di ogni parola e le altre lettere in minuscolo. `find(" ")` dà la posizione dello spazio che separa le due parole. Il cognome va dall'inizio fino allo spazio escluso; il nome parte dal carattere dopo lo spazio e arriva in fondo.
</details>

---

### Esercizio 10

Completa il codice che controlla se una frase è palindroma, cioè se si legge uguale nei due versi senza contare spazi e maiuscole.

```python
frase = "I topi non avevano nipoti"
pulita = frase.__________.__________(" ", "")
if pulita == pulita[__________]:
    print("Palindroma")
else:
    print("Non palindroma")
# deve stampare: Palindroma
```

<details>
<summary>Mostra la risposta</summary>

```python
frase = "I topi non avevano nipoti"
pulita = frase.lower().replace(" ", "")
if pulita == pulita[::-1]:
    print("Palindroma")
else:
    print("Non palindroma")
# Palindroma
```

**Spiegazione:** `lower()` porta tutto in minuscolo e `replace(" ", "")` toglie gli spazi sostituendoli con la stringa vuota: si ottiene `"itopinonavevanonipoti"`. Lo slicing `[::-1]` legge la stringa dalla fine all'inizio. Se la stringa rovesciata è uguale all'originale, la frase è palindroma.
</details>
