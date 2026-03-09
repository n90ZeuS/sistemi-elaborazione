# Metodi delle Stringhe in Python

Scheda di riferimento rapido con tutti i principali metodi stringa, raggruppati per funzione.

> Le stringhe in Python sono **immutabili**: ogni metodo restituisce una **nuova** stringa, l'originale non cambia.

---

## Ricerca

| Metodo | Sintassi | Descrizione | Esempio | Risultato |
|--------|----------|-------------|---------|-----------|
| `find` | `s.find(sub[, start, end])` | Trova la prima posizione di `sub`, restituisce -1 se assente | `"ciao mondo".find("mondo")` | `5` |
| `rfind` | `s.rfind(sub)` | Come find, ma cerca da destra | `"abcabc".rfind("abc")` | `3` |
| `index` | `s.index(sub)` | Come find, ma lancia ValueError se assente | `"ciao".index("ia")` | `1` |
| `rindex` | `s.rindex(sub)` | Come index, ma cerca da destra | `"abcabc".rindex("a")` | `3` |
| `count` | `s.count(sub)` | Conta le occorrenze non sovrapposte | `"banana".count("an")` | `2` |
| `startswith` | `s.startswith(prefix)` | Verifica se inizia con il prefisso | `"ciao".startswith("ci")` | `True` |
| `endswith` | `s.endswith(suffix)` | Verifica se finisce con il suffisso | `"dati.csv".endswith(".csv")` | `True` |
| `in` | `sub in s` | Verifica se la sottostringa e' presente | `"mondo" in "ciao mondo"` | `True` |

---

## Trasformazione (maiuscole/minuscole)

| Metodo | Descrizione | Esempio | Risultato |
|--------|-------------|---------|-----------|
| `upper()` | Tutto maiuscolo | `"ciao".upper()` | `"CIAO"` |
| `lower()` | Tutto minuscolo | `"CIAO".lower()` | `"ciao"` |
| `title()` | Iniziale maiuscola per ogni parola | `"ciao mondo".title()` | `"Ciao Mondo"` |
| `capitalize()` | Solo la prima lettera maiuscola | `"ciao mondo".capitalize()` | `"Ciao mondo"` |
| `swapcase()` | Inverte maiuscole/minuscole | `"Ciao".swapcase()` | `"cIAO"` |
| `casefold()` | Minuscolo aggressivo (per confronti) | `"Strasse".casefold()` | `"strasse"` |

---

## Trasformazione (spazi e caratteri)

| Metodo | Descrizione | Esempio | Risultato |
|--------|-------------|---------|-----------|
| `strip()` | Rimuove spazi (e \n, \t) da inizio e fine | `"  ciao  \n".strip()` | `"ciao"` |
| `lstrip()` | Rimuove spazi solo a sinistra | `"  ciao  ".lstrip()` | `"ciao  "` |
| `rstrip()` | Rimuove spazi solo a destra | `"  ciao  ".rstrip()` | `"  ciao"` |
| `strip(chars)` | Rimuove i caratteri specificati | `"***ciao***".strip("*")` | `"ciao"` |

---

## Verifica (restituiscono True/False)

| Metodo | Descrizione | Esempio `True` | Esempio `False` |
|--------|-------------|----------------|-----------------|
| `isalpha()` | Solo lettere? | `"ciao".isalpha()` | `"ciao2".isalpha()` |
| `isdigit()` | Solo cifre? | `"123".isdigit()` | `"12.3".isdigit()` |
| `isalnum()` | Solo lettere e cifre? | `"abc123".isalnum()` | `"abc 123".isalnum()` |
| `isspace()` | Solo spazi bianchi? | `"  \t\n".isspace()` | `"  a".isspace()` |
| `isupper()` | Tutto maiuscolo? | `"CIAO".isupper()` | `"Ciao".isupper()` |
| `islower()` | Tutto minuscolo? | `"ciao".islower()` | `"Ciao".islower()` |
| `isnumeric()` | Solo caratteri numerici? | `"123".isnumeric()` | `"1.5".isnumeric()` |
| `isdecimal()` | Solo cifre decimali? | `"42".isdecimal()` | `"IV".isdecimal()` |

> **Nota per studenti di statistica:** `isdigit()` e `isnumeric()` NON funzionano con numeri decimali (`"3.14"` restituisce `False`). Per verificare se una stringa rappresenta un numero con la virgola, servono altre strategie.

---

## Divisione e Unione

| Metodo | Sintassi | Descrizione | Esempio | Risultato |
|--------|----------|-------------|---------|-----------|
| `split()` | `s.split(sep)` | Divide in lista di sottostringhe | `"a,b,c".split(",")` | `["a", "b", "c"]` |
| `split()` | `s.split()` | Divide per spazi (qualsiasi quantita') | `"ciao   mondo".split()` | `["ciao", "mondo"]` |
| `rsplit()` | `s.rsplit(sep, maxsplit)` | Come split, ma da destra | `"a.b.c".rsplit(".", 1)` | `["a.b", "c"]` |
| `splitlines()` | `s.splitlines()` | Divide per righe | `"a\nb\nc".splitlines()` | `["a", "b", "c"]` |
| `join()` | `sep.join(lista)` | Unisce una lista con il separatore | `", ".join(["a","b","c"])` | `"a, b, c"` |
| `partition()` | `s.partition(sep)` | Divide in 3: prima, sep, dopo | `"nome=Luca".partition("=")` | `("nome", "=", "Luca")` |
| `rpartition()` | `s.rpartition(sep)` | Come partition, ma da destra | `"a.b.c".rpartition(".")` | `("a.b", ".", "c")` |

### Esempio pratico: elaborare un CSV semplice

```python
riga = "Rossi,Marco,28,Statistica"
campi = riga.split(",")
# ["Rossi", "Marco", "28", "Statistica"]

cognome, nome, voto, corso = riga.split(",")
voto = int(voto)  # "28" -> 28
```

---

## Sostituzione

| Metodo | Sintassi | Descrizione | Esempio | Risultato |
|--------|----------|-------------|---------|-----------|
| `replace()` | `s.replace(old, new[, count])` | Sostituisce tutte le occorrenze | `"ciao ciao".replace("ciao", "hello")` | `"hello hello"` |
| `replace()` | `s.replace(old, new, 1)` | Sostituisce solo la prima | `"aaa".replace("a", "b", 1)` | `"baa"` |
| `translate()` | `s.translate(table)` | Traduce caratteri secondo una tabella | vedi sotto | vedi sotto |

### translate() con maketrans()

```python
# Sostituire singoli caratteri (utile per pulizia dati)
tabella = str.maketrans("aeiou", "AEIOU")
"ciao mondo".translate(tabella)
# "cIAO mOndO"

# Rimuovere caratteri
tabella = str.maketrans("", "", ",.;:!?")
"Ciao, come stai?".translate(tabella)
# "Ciao come stai"
```

---

## Formattazione

### f-string (raccomandato, Python 3.6+)

```python
nome = "Luca"
media = 27.333333

f"Studente: {nome}"                    # "Studente: Luca"
f"Media: {media:.2f}"                  # "Media: 27.33"
f"Media: {media:.1f}"                  # "Media: 27.3"
f"{'Titolo':^20}"                      # "      Titolo       "  (centrato)
f"{'Voto':<10}{'Nome':>10}"            # "Voto            Nome"
f"Percentuale: {0.856:.1%}"            # "Percentuale: 85.6%"
f"Grande: {1000000:,}"                 # "Grande: 1,000,000"
f"Binario: {42:b}"                     # "Binario: 101010"
```

### Specifiche di formato comuni

| Specifica | Significato | Esempio | Risultato |
|-----------|-------------|---------|-----------|
| `:.2f` | 2 decimali | `f"{3.14159:.2f}"` | `"3.14"` |
| `:.0f` | Nessun decimale | `f"{3.7:.0f}"` | `"4"` |
| `:.1%` | Percentuale 1 dec | `f"{0.856:.1%}"` | `"85.6%"` |
| `:>10` | Allinea a destra (10 car.) | `f"{'abc':>10}"` | `"       abc"` |
| `:<10` | Allinea a sinistra | `f"{'abc':<10}"` | `"abc       "` |
| `:^10` | Centra | `f"{'abc':^10}"` | `"   abc    "` |
| `:06` | Padding con zeri | `f"{42:06}"` | `"000042"` |
| `:,` | Separatore migliaia | `f"{1234567:,}"` | `"1,234,567"` |
| `:+` | Mostra sempre segno | `f"{42:+}"` | `"+42"` |

### Metodo format() (alternativa)

```python
"Studente: {}, Media: {:.2f}".format(nome, media)
"Studente: {nome}, Media: {media:.2f}".format(nome="Luca", media=27.3)
```

### Allineamento e riempimento

| Metodo | Descrizione | Esempio | Risultato |
|--------|-------------|---------|-----------|
| `center(n)` | Centra in n caratteri | `"abc".center(9)` | `"   abc   "` |
| `center(n, c)` | Centra con riempimento | `"abc".center(9, "-")` | `"---abc---"` |
| `ljust(n)` | Allinea a sinistra | `"abc".ljust(9)` | `"abc      "` |
| `rjust(n)` | Allinea a destra | `"abc".rjust(9)` | `"      abc"` |
| `zfill(n)` | Riempie con zeri | `"42".zfill(5)` | `"00042"` |

---

## Suggerimenti rapidi

```python
# Invertire una stringa
"ciao"[::-1]                    # "oaic"

# Ripetere una stringa
"ab" * 3                        # "ababab"

# Controllare se una stringa e' vuota
if not s:       # s == "" oppure s e' vuota
if s.strip():   # contiene qualcosa oltre a spazi

# Rimuovere newline alla fine
riga = riga.rstrip("\n")

# Concatenazione efficiente di molte stringhe
parti = []
for x in range(1000):
    parti.append(str(x))
risultato = ",".join(parti)     # meglio di += ripetuti
```
