# Laboratorio 1 — Ambiente, variabili e condizionali

**Prerequisiti:** lezioni T07 (Primi passi in Python) e T08 (Operatori, I/O e condizionali).

Oggi ci sono solo esercizi, in ordine di difficoltà. Per ogni esercizio create un file `.py` con il nome indicato e scrivete il programma da soli.

Ogni esercizio ha la consegna, un esempio di esecuzione e alcuni casi da provare: il programma è corretto quando dà gli stessi risultati. La sfida è per chi finisce prima. Le soluzioni le vediamo all'inizio della lezione T10.

| # | File | Esercizio |
|---|---|---|
| 0 | `saluto.py` | Preparazione |
| 1 | `operatori.py` | Operatori aritmetici |
| 2 | `temperatura.py` | Conversione di temperatura |
| 3 | `iva.py` | Prezzo con IVA |
| 4 | `imc.py` | Indice di massa corporea |
| 5 | `bancomat.py` | Bancomat |
| Sfida | `sfida_temperatura.py` | Report di temperatura |

---

## Esercizio 0 — Preparazione (`saluto.py`)

1. Aprite il terminale e controllate la versione di Python: `python3 --version` (su Windows: `python --version`).
2. Create una cartella `lab01` e apritela in VS Code (File → Apri cartella).
3. Create il file `saluto.py` con il codice qui accanto.
4. Eseguitelo dal terminale di VS Code: `python3 saluto.py`.

```python
nome: str = "Mondo"
print(f"Ciao, {nome}!")
```

Output:

```
Ciao, Mondo!
```

---

## Promemoria

Questo è tutto quello che serve per gli esercizi di oggi. Per la formattazione dei numeri bastano due formati: `.2f` (numero di decimali) e `.0%` (percentuale).

```python
prezzo: float = float(input("Prezzo: "))   # input() restituisce una stringa

print(f"{prezzo:.2f}")      # due decimali:    12.5  -> 12.50
print(f"{prezzo:.1f}")      # un decimale:     12.5  -> 12.5
print(f"{0.22:.0%}")        # percentuale:     0.22  -> 22%
print(f"{0.125:.1%}")       # con un decimale: 0.125 -> 12.5%

if prezzo < 0:
    print("Errore: prezzo negativo")
elif prezzo < 100:
    print("Economico")
else:
    print("Caro")
```

---

## Esercizio 1 — Operatori aritmetici (`operatori.py`)

**Consegna**

1. Assegnate `a = 17` e `b = 5` (due variabili `int`, senza `input()`).
2. Stampate il risultato di `+`, `-`, `*`, `/`, `//`, `%` e `**`, una riga per operazione.
3. Cambiate i valori di `a` e `b` e controllate a mano i risultati.

**Esempio di esecuzione**

```
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.4
17 // 5 = 3
17 % 5 = 2
17 ** 5 = 1419857
```

**Provate anche**

- `a = 20`, `b = 4`: `20 / 4 = 5.0` e `20 // 4 = 5`
- `a = 7`, `b = 2`: `7 % 2 = 1` (7 è dispari)

---

## Esercizio 2 — Conversione di temperatura (`temperatura.py`)

**Consegna**

1. Chiedete all'utente una temperatura in gradi Celsius.
2. Convertitela in Fahrenheit: `F = C * 9 / 5 + 32`.
3. Stampate le due temperature con un decimale.

**Esempio di esecuzione**

```
Temperatura in Celsius: 25
25.0°C = 77.0°F
```

**Provate anche**

- `0` → `32.0°F`
- `100` → `212.0°F`
- `37.5` → `99.5°F`
- `-40` → `-40.0°F`

---

## Esercizio 3 — Prezzo con IVA (`iva.py`)

**Consegna**

1. Scrivete l'aliquota in una costante: `ALIQUOTA_IVA: float = 0.22`.
2. Chiedete il prezzo di un prodotto senza IVA.
3. Calcolate l'IVA e il totale.
4. Stampate prezzo, IVA e totale con due decimali e l'aliquota come percentuale.

**Esempio di esecuzione**

```
Prezzo senza IVA (euro): 49.99
Prezzo: 49.99 EUR
IVA: 11.00 EUR (22%)
Totale: 60.99 EUR
```

**Provate anche**

- `100` → IVA `22.00`, totale `122.00`
- `10` → IVA `2.20`, totale `12.20`
- con `ALIQUOTA_IVA = 0.10` e `49.99` → IVA `5.00 EUR (10%)`

---

## Esercizio 4 — Indice di massa corporea (`imc.py`)

**Consegna**

1. Chiedete peso (kg) e altezza (m).
2. Se peso o altezza non sono positivi, o l'altezza supera 2.50 m, stampate un errore.
3. Altrimenti calcolate `imc = peso / altezza ** 2` e stampatelo con un decimale insieme alla classe.

| IMC | Classe |
|---|---|
| minore di 18.5 | Sottopeso |
| da 18.5 a meno di 25 | Normopeso |
| da 25 a meno di 30 | Sovrappeso |
| 30 o più | Obesità |

**Esempio di esecuzione**

```
Peso (kg): 72
Altezza (m): 1.75
IMC: 23.5 — Normopeso
```

**Provate anche**

- `50`, `1.80` → `15.4 — Sottopeso`
- `95`, `1.75` → `31.0 — Obesità`
- `70`, `0` → errore
- `70`, `2.60` → errore

---

## Esercizio 5 — Bancomat (`bancomat.py`)

**Consegna**

1. Il saldo iniziale è `1000.00` EUR, scritto nel codice. Stampatelo.
2. Chiedete l'operazione: `D` deposito, `P` prelievo, `S` saldo. Accettate anche le minuscole con `.upper()`.
3. Con `S` stampate il saldo. Con `D` e `P` chiedete l'importo, aggiornate il saldo e stampatelo.
4. Gestite tre errori: operazione sconosciuta, importo minore o uguale a zero, prelievo maggiore del saldo.

**Esempio di esecuzione**

```
=== BANCOMAT ===
Saldo attuale: 1000.00 EUR
Operazione (D=Deposito, P=Prelievo, S=Saldo): P
Importo: 250
Prelievo di 250.00 EUR effettuato.
Nuovo saldo: 750.00 EUR
```

**Provate anche**

- `d`, `500` → nuovo saldo `1500.00`
- `P`, `2000` → saldo insufficiente
- `P`, `-10` → importo non valido
- `X` → operazione non riconosciuta

---

## Sfida — Report di temperatura (`sfida_temperatura.py`)

**Consegna**

1. Chiedete una temperatura in gradi Celsius.
2. Se è sotto lo zero assoluto (−273.15 °C) stampate un errore e non fate altro.
3. Altrimenti convertitela in Fahrenheit, classificatela con la tabella e stampate il report.

| Celsius | Percezione |
|---|---|
| fino a −10 | Gelido |
| fino a 5 | Freddo |
| fino a 18 | Mite |
| fino a 30 | Caldo |
| oltre 30 | Torrido |

**Esempio di esecuzione**

```
Temperatura in Celsius: 22
=== REPORT TEMPERATURA ===
Celsius:    22.0°C
Fahrenheit: 71.6°F
Percezione: Caldo
```

**Provate anche**

- `-15` → Gelido
- `18` → Mite (18 è compreso)
- `35` → Torrido
- `-300` → errore

---

## Domande di verifica

1. Cosa succede se il programma esegue `int(input("Età: "))` e l'utente scrive `venti`?
2. Quanto valgono `10 / 2` e `10 // 2`? Perché i due risultati hanno tipo diverso?
3. In `imc.py`, perché basta scrivere `elif imc < 25` senza controllare anche `imc >= 18.5`?
4. Cosa stampano `f"{0.075:.1%}"` e `f"{2 / 3:.2f}"`?
5. In `bancomat.py`, cosa succede con `P` e importo `-10` se manca il controllo sull'importo?
