# Operatori e Precedenza in Python

Scheda di riferimento rapido: tabella completa della precedenza, esempi ed errori comuni.

---

## Tabella di precedenza (dall'alto = priorita' maggiore)

| Priorita' | Operatore | Descrizione | Esempio |
|-----------|-----------|-------------|---------|
| 1 (max) | `()` | Parentesi (raggruppamento) | `(2 + 3) * 4` |
| 2 | `**` | Esponenziazione | `2 ** 3` = 8 |
| 3 | `+x`, `-x`, `~x` | Operatori unari (segno, NOT bit) | `-5`, `~0` |
| 4 | `*`, `/`, `//`, `%` | Moltiplicazione, divisione, div. intera, modulo | `7 // 2` = 3 |
| 5 | `+`, `-` | Addizione, sottrazione | `3 + 4` = 7 |
| 6 | `<<`, `>>` | Shift bit a bit | `1 << 3` = 8 |
| 7 | `&` | AND bit a bit | `5 & 3` = 1 |
| 8 | `^` | XOR bit a bit | `5 ^ 3` = 6 |
| 9 | `\|` | OR bit a bit | `5 \| 3` = 7 |
| 10 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in`, `not in` | Confronto, identita', appartenenza | `x == 5` |
| 11 | `not` | NOT logico | `not True` = False |
| 12 | `and` | AND logico | `True and False` = False |
| 13 (min) | `or` | OR logico | `False or True` = True |

> **Regola pratica:** la precedenza segue grosso modo l'ordine della matematica: prima le potenze, poi moltiplicazione/divisione, poi addizione/sottrazione, poi i confronti, infine la logica.

---

## Operatori aritmetici in dettaglio

| Operatore | Nome | Esempio | Risultato | Note |
|-----------|------|---------|-----------|------|
| `+` | Addizione | `7 + 3` | `10` | |
| `-` | Sottrazione | `7 - 3` | `4` | |
| `*` | Moltiplicazione | `7 * 3` | `21` | Anche per stringhe: `"ab" * 3` = `"ababab"` |
| `/` | Divisione | `7 / 3` | `2.3333...` | Restituisce **sempre** float |
| `//` | Divisione intera | `7 // 3` | `2` | Arrotonda verso il basso |
| `%` | Modulo (resto) | `7 % 3` | `1` | Utile per pari/dispari: `n % 2` |
| `**` | Esponenziazione | `2 ** 10` | `1024` | Associativo a destra: `2**3**2` = `2**(3**2)` = 512 |

### Divisione: `/` vs `//`

```python
7 / 2       # 3.5  (divisione reale, sempre float)
7 // 2      # 3    (divisione intera, arrotonda in basso)
-7 // 2     # -4   (!) arrotonda verso -infinito, NON verso zero
7 / 2.0     # 3.5
7 // 2.0    # 3.0  (divisione intera ma risultato float)
```

---

## Operatori di confronto

| Operatore | Significato | Esempio |
|-----------|-------------|---------|
| `==` | Uguale a (valore) | `5 == 5.0` -> `True` |
| `!=` | Diverso da | `5 != 3` -> `True` |
| `<` | Minore di | `3 < 5` -> `True` |
| `>` | Maggiore di | `5 > 3` -> `True` |
| `<=` | Minore o uguale | `5 <= 5` -> `True` |
| `>=` | Maggiore o uguale | `5 >= 6` -> `False` |
| `is` | Stesso oggetto (identita') | `x is None` |
| `is not` | Oggetto diverso | `x is not None` |
| `in` | Appartiene a | `3 in [1, 2, 3]` -> `True` |
| `not in` | Non appartiene a | `4 not in [1, 2, 3]` -> `True` |

### Confronti a catena (feature di Python!)

```python
# Python permette i confronti a catena
1 < x < 10          # equivale a: 1 < x and x < 10
a <= b <= c         # equivale a: a <= b and b <= c

# Molto utile per intervalli statistici
18 <= voto <= 30    # voto e' tra 18 e 30?
```

---

## Operatori logici

| Operatore | Significato | Esempio | Risultato |
|-----------|-------------|---------|-----------|
| `not x` | Negazione | `not True` | `False` |
| `x and y` | Congiunzione (entrambi veri) | `True and False` | `False` |
| `x or y` | Disgiunzione (almeno uno vero) | `True or False` | `True` |

### Cortocircuito (short-circuit evaluation)

```python
# and: se il primo e' False, il secondo NON viene valutato
False and funzione_costosa()    # funzione_costosa() non viene chiamata

# or: se il primo e' True, il secondo NON viene valutato
True or funzione_costosa()      # funzione_costosa() non viene chiamata

# Uso pratico: evitare errori
lista = []
if lista and lista[0] > 5:     # lista vuota -> False -> non accede a lista[0]
    print("ok")

# Valore di default con or
nome = input("Nome: ") or "Anonimo"  # se input vuoto (""), usa "Anonimo"
```

---

## Operatori di assegnamento composto

| Operatore | Equivalente a | Esempio |
|-----------|---------------|---------|
| `+=` | `x = x + valore` | `x += 5` |
| `-=` | `x = x - valore` | `x -= 3` |
| `*=` | `x = x * valore` | `x *= 2` |
| `/=` | `x = x / valore` | `x /= 4` |
| `//=` | `x = x // valore` | `x //= 3` |
| `%=` | `x = x % valore` | `x %= 2` |
| `**=` | `x = x ** valore` | `x **= 2` |

> **Attenzione:** Python NON ha gli operatori `++` e `--`. Usare `x += 1` e `x -= 1`.

---

## Espressioni ambigue risolte dalla precedenza

### Esempio 1: Aritmetica mista

```python
2 + 3 * 4       # = 2 + 12 = 14      (* ha precedenza su +)
(2 + 3) * 4     # = 5 * 4 = 20       (parentesi forzano l'ordine)
```

### Esempio 2: Esponenziazione e segno

```python
-2 ** 2          # = -(2**2) = -4     (** ha precedenza su - unario!)
(-2) ** 2        # = 4                (parentesi: prima il segno)
```

> Questo e' un errore **molto comune**! In Python `-2**2` vale **-4**, non 4.

### Esempio 3: Confronti e logica

```python
x = 5
not x == 5       # = not (x == 5) = not True = False
                  # (== ha precedenza su not)

x != 5           # False (modo diretto per confrontare)
```

### Esempio 4: and vs or

```python
True or False and False
# = True or (False and False)    (and ha precedenza su or)
# = True or False
# = True

(True or False) and False
# = True and False
# = False
```

### Esempio 5: Confronto e in

```python
x = 3
1 < x and x < 10       # True (modo esplicito)
1 < x < 10              # True (confronto a catena, piu' leggibile)
```

### Esempio 6: Assegnamento (NON e' un operatore di confronto!)

```python
x = 5       # assegnamento: x riceve il valore 5
x == 5      # confronto: x e' uguale a 5? -> True

# Errore comune nei condizionali:
if x == 5:  # CORRETTO: confronto
    pass
# if x = 5:  # ERRORE DI SINTASSI! (Python lo impedisce)
```

---

## Errori comuni (trappole da evitare)

### 1. `-x**n` non fa quello che pensi

```python
-3 ** 2     # -9, NON 9!  Equivale a -(3**2)
(-3) ** 2   # 9            Usa le parentesi!
```

### 2. `==` vs `is`

```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b      # True  (stesso VALORE)
a is b      # False (OGGETTI diversi in memoria)

# Usa 'is' SOLO con None, True, False
x is None   # corretto
x == None   # funziona ma non e' pythonico
```

### 3. Divisione intera con numeri negativi

```python
7 // 2      #  3  (ok, arrotonda verso il basso)
-7 // 2     # -4  (!) NON -3! Arrotonda verso -infinito
```

### 4. Uguaglianza tra float

```python
0.1 + 0.2 == 0.3               # False (!)
abs(0.1 + 0.2 - 0.3) < 1e-9    # True (confronto con tolleranza)

# In NumPy:
# numpy.isclose(0.1 + 0.2, 0.3)  # True
```

### 5. Operatori logici su valori non booleani

```python
# and restituisce il primo valore falsy, o l'ultimo
0 and 5         # 0
3 and 5         # 5

# or restituisce il primo valore truthy, o l'ultimo
0 or 5          # 5
3 or 5          # 3
"" or "default" # "default"
```

---

## Consiglio finale

> **Nel dubbio, usa le parentesi!**
> Le parentesi rendono il codice piu' leggibile e prevengono errori.
> Non costano nulla e salvano da bug insidiosi.

```python
# Poco chiaro
risultato = a + b * c > d and not e or f

# Chiaro!
risultato = ((a + (b * c)) > d) and (not e) or f
```
