# Laboratorio 6 — Classi e oggetti

**Prerequisiti:** lezioni T16 (Programmazione a oggetti).

Oggi ci sono solo esercizi, in ordine di difficoltà, su classi e oggetti. Per ogni esercizio create un file `.py` con il nome indicato: dentro definite le classi richieste, con type hints su attributi e metodi, e poi usatele sui dati della consegna stampando i risultati. Non serve `input()`: i dati sono già scritti nella consegna. Tutto il codice di un esercizio sta in un solo file. Alla fine c'è una challenge a scelta tra 5 temi: sceglietene uno.

Ogni esercizio ha la consegna, un esempio di esecuzione e alcuni casi da provare: il programma è corretto quando dà gli stessi risultati. Alla fine c'è una challenge a scelta tra 5 temi. Le soluzioni le vediamo all'inizio del laboratorio L07.

| # | File | Esercizio |
|---|---|---|
| 1 | `esame.py` | Un esame del libretto |
| 2 | `tessera_mensa.py` | La tessera della mensa |
| 3 | `segreteria.py` | La coda in segreteria |
| 4 | `erasmus.py` | La graduatoria Erasmus |
| 5 | `campione.py` | Un campione di misure |
| 6 | `libretto.py` | Il libretto: un oggetto che contiene oggetti |
| 7 | `abbonamenti.py` | Abbonamenti ai mezzi pubblici |
| 8 | `biblioteca.py` | La biblioteca di dipartimento |
| Challenge | a scelta | Mercati e finanza · Sport · Imprese e marketing · Salute e scienza · Caso e probabilità |

---

## Promemoria

Gli strumenti che servono oggi. `__init__` riceve i dati e li salva negli attributi con `self.`; ogni metodo ha `self` come primo parametro, ma quando lo chiamate non lo scrivete. `__str__` decide cosa stampa `print`, `__lt__` dice a `sorted` quale oggetto viene prima. Se i dati non sono validi, `__init__` solleva un errore con `raise ValueError(...)`.

```python
class Studente:
    def __init__(self, nome: str, voti: list[int]) -> None:
        self.nome: str = nome                       # attributi
        self.voti: list[int] = voti
    def media(self) -> float:                       # metodo
        return sum(self.voti) / len(self.voti)
    def __str__(self) -> str:                       # usato da print
        return f"{self.nome}: {self.media():.1f}"
    def __lt__(self, altro: "Studente") -> bool:    # usato da sorted
        return self.media() < altro.media()

gruppo: list[Studente] = [Studente("Anna", [28, 30]),
                          Studente("Luca", [24, 26])]
for s in sorted(gruppo):
    print(s)                                        # Luca: 25.0 ...
```

---

## Esercizio 1 — Un esame del libretto (`esame.py`)

**Consegna**

1. Definite una classe `Esame` con `__init__(self, nome: str, cfu: int, voto: int)` che salva i tre valori in tre attributi.
2. Aggiungete un metodo `punti(self) -> int` che restituisce il voto moltiplicato per i crediti.
3. Create una lista con tre esami: Analisi 1 (12 CFU, 26), Statistica 1 (9 CFU, 29), Informatica (6 CFU, 30).
4. Con un ciclo stampate ogni esame, usando gli attributi, e sommate crediti e punti. Alla fine stampate i CFU totali e la media ponderata con due decimali.

**Esempio di esecuzione**

```
Analisi 1: 26 (12 CFU)
Statistica 1: 29 (9 CFU)
Informatica: 30 (6 CFU)
CFU: 27, media ponderata: 27.89
```

**Provate anche**

- aggiungete `Esame("Algebra lineare", 9, 24)` → `CFU: 36, media ponderata: 26.92`
- prima del ciclo scrivete `esami[0].voto = 28` → `Analisi 1: 28 (12 CFU)`, `media ponderata: 28.78`
- `print(esami[0])` → `<__main__.Esame object at 0x...>`: per una stampa leggibile serve `__str__` (esercizio 2)

---

## Esercizio 2 — La tessera della mensa (`tessera_mensa.py`)

**Consegna**

1. Definite una classe `Tessera` con titolare e saldo. Se il saldo iniziale è negativo, `__init__` solleva `ValueError("Il saldo iniziale è negativo")`.
2. Aggiungete `ricarica(self, importo: float)`, che solleva `ValueError` se l'importo non è positivo, e `paga(self, prezzo: float)`, che solleva `ValueError` se il saldo non basta. Nel messaggio scrivete il saldo con due decimali.
3. Aggiungete `__str__` che restituisce titolare e saldo, come nell'esempio.
4. Create la tessera di Anna Rossi con 10 EUR e provate a pagare tre pasti da 4.50 EUR, ognuno in un `try`. Poi ricaricate 20 EUR e stampate la tessera.

**Esempio di esecuzione**

```
Tessera di Anna Rossi: 10.00 EUR
Pagato 4.50 EUR, restano 5.50
Pagato 4.50 EUR, restano 1.00
Saldo insufficiente: 1.00
Tessera di Anna Rossi: 21.00 EUR
```

**Provate anche**

- saldo iniziale `15.0` → tre pagamenti riusciti e alla fine `Tessera di Anna Rossi: 21.50 EUR`
- `Tessera("Marco Bianchi", -5.0)` → `ValueError: Il saldo iniziale è negativo`
- `tessera.ricarica(0)` → `ValueError: La ricarica deve essere positiva`

---

## Esercizio 3 — La coda in segreteria (`segreteria.py`)

**Consegna**

1. Definite una classe `Ticket` con due attributi di classe: la tupla `SERVIZI = ("iscrizioni", "tasse", "esami")` e il contatore `emessi = 0`.
2. `__init__(self, servizio: str)` solleva `ValueError` se il servizio non è in `SERVIZI`; altrimenti aumenta `Ticket.emessi` di 1 e lo salva nell'attributo di istanza `numero`.
3. Aggiungete `__str__` (`Numero 1 (esami)`) e `__repr__` (`Ticket(1, 'esami')`).
4. Create i biglietti per esami, tasse, esami, iscrizioni, esami e metteteli in una lista. Stampate la lista, il primo biglietto, il numero di biglietti emessi e quanti ce ne sono per ogni servizio.

**Esempio di esecuzione**

```
[Ticket(1, 'esami'), Ticket(2, 'tasse'), Ticket(3, 'esami'), Ticket(4, 'iscrizioni'), Ticket(5, 'esami')]
Prossimo: Numero 1 (esami)
Biglietti emessi: 5
iscrizioni: 1
tasse: 1
esami: 3
```

**Provate anche**

- `Ticket("mensa")` → `ValueError: Servizio sconosciuto: mensa`, e `Ticket.emessi` resta 5
- `print(coda[3].numero, coda[3].emessi)` → `4 5`: l'attributo di classe si legge anche dall'oggetto
- togliete `__repr__`: la lista si stampa come `[<__main__.Ticket object at 0x...>, ...]`

---

## Esercizio 4 — La graduatoria Erasmus (`erasmus.py`)

**Consegna**

1. Definite una classe `Candidato` con nome, media e CFU sostenuti, e un `__str__` come nell'esempio.
2. Aggiungete `__eq__`: due candidati sono a pari merito se hanno la stessa media e gli stessi CFU. Se l'altro oggetto non è un `Candidato` restituite `NotImplemented`.
3. Aggiungete `__lt__`: viene prima chi ha la media più alta e, a parità di media, chi ha più CFU.
4. Ordinate i candidati con `sorted`, stampate la graduatoria numerata con `enumerate` e controllate con `==` se il primo e il secondo, e il terzo e il quarto, sono a pari merito.

| Candidato | Media, CFU |
|---|---|
| Luca | 27.4, 90 |
| Sara | 28.1, 84 |
| Paolo | 27.4, 102 |
| Elena | 26.9, 120 |
| Davide | 28.1, 84 |

**Esempio di esecuzione**

```
1. Sara (media 28.10, 84 CFU)
2. Davide (media 28.10, 84 CFU)
3. Paolo (media 27.40, 102 CFU)
4. Luca (media 27.40, 90 CFU)
5. Elena (media 26.90, 120 CFU)
Pari merito tra 1 e 2: True
Pari merito tra 3 e 4: False
```

**Provate anche**

- aggiungete `Candidato("Marta", 29.0, 60)` → `1. Marta (media 29.00, 60 CFU)`
- `print(classifica[0] == "Sara")` → `False`: una stringa non è un `Candidato`
- togliete `__lt__` → `TypeError: '<' not supported between instances of 'Candidato' and 'Candidato'`

---

## Esercizio 5 — Un campione di misure (`campione.py`)

**Consegna**

1. Definite una classe `Campione` con un nome e una lista `_valori`, vuota all'inizio. L'underscore indica che la lista si usa solo dentro la classe.
2. Aggiungete il metodo `aggiungi(self, x: float)`.
3. Con `@property` definite `n` (numero di valori), `media` e `varianza` (campionaria, con divisore n − 1).
4. Create il campione `Altezze (cm)` con 172, 165, 180, 158, 175 e stampate n, media, varianza e deviazione standard (`** 0.5`) con due decimali. Poi provate ad assegnare `altezze.media = 175.0` in un `try` e catturate `AttributeError`.

**Esempio di esecuzione**

```
Altezze (cm): 5 valori
Media: 170.00, varianza: 74.50
Deviazione standard: 8.63
La media non si assegna: è calcolata dai valori
```

**Provate anche**

- aggiungete 190 → `6 valori`, `Media: 173.33, varianza: 126.27`
- `statistics.variance([172, 165, 180, 158, 175])` → `74.5`, come la vostra
- `print(altezze._valori)` funziona lo stesso: l'underscore è una convenzione, non un divieto

---

## Esercizio 6 — Il libretto: un oggetto che contiene oggetti (`libretto.py`)

**Consegna**

1. Riprendete la classe `Esame` dell'esercizio 1 e aggiungete `__str__` come nell'esempio.
2. Definite una classe `Libretto` con il nome dello studente e una lista `esami`, vuota all'inizio: il libretto contiene degli esami (composizione).
3. Aggiungete `cerca(self, nome: str) -> Esame | None`, che restituisce l'esame con quel nome oppure `None`, e `aggiungi(self, esame: Esame)`, che usa `cerca` e solleva `ValueError` se l'esame è già presente.
4. Aggiungete `media(self) -> float` con la media ponderata. Inserite i tre esami dell'esercizio 1, provate a inserire di nuovo Informatica (con 28) in un `try`, cercate Statistica 1 e stampate numero di esami e media.

**Esempio di esecuzione**

```
Informatica è già nel libretto
Statistica 1: 29 (9 CFU)
Esami: 3, media ponderata 27.89
```

**Provate anche**

- `print(lib.cerca("Algebra"))` → `None`
- aggiungete `Esame("Algebra lineare", 9, 24)` → `Esami: 4, media ponderata 26.92`
- `Libretto("Marco").media()` → `ZeroDivisionError`: un libretto vuoto non ha media

---

## Esercizio 7 — Abbonamenti ai mezzi pubblici (`abbonamenti.py`)

**Consegna**

1. Definite una classe `Abbonamento` con titolare e numero di mesi (da 1 a 12, altrimenti `ValueError`) e l'attributo di classe `PREZZO_MESE = 40.0`.
2. Aggiungete `prezzo(self) -> float` (prezzo al mese per mesi) e `__str__` come nell'esempio.
3. Definite la sottoclasse `AbbonamentoStudente(Abbonamento)` con la matricola in più e l'attributo di classe `SCONTO = 0.3`. Il suo `__init__` chiama `super().__init__(...)`; `prezzo` e `__str__` riusano quelli della classe madre con `super()`.
4. Mettete in una lista gli abbonamenti della tabella, stampateli e stampate l'incasso totale.

| Titolare | Abbonamento |
|---|---|
| Marco Bianchi | 12 mesi |
| Anna Rossi | 10 mesi, studente 2101234 |
| Luca Russo | 3 mesi, studente 2102345 |
| Elena Romano | 2 mesi |

**Esempio di esecuzione**

```
Marco Bianchi, 12 mesi: 480.00 EUR
Anna Rossi, 10 mesi: 280.00 EUR, matricola 2101234
Luca Russo, 3 mesi: 84.00 EUR, matricola 2102345
Elena Romano, 2 mesi: 80.00 EUR
Incasso: 924.00 EUR
```

**Provate anche**

- `AbbonamentoStudente("Sara Ferrari", 13, "2102890")` → `ValueError: Durata non valida: 13 mesi`: il controllo è ereditato
- prima della lista scrivete `AbbonamentoStudente.SCONTO = 0.5` → Anna `200.00 EUR`, Luca `60.00 EUR`, `Incasso: 820.00 EUR`
- contate gli abbonamenti studente con `isinstance(a, AbbonamentoStudente)` → `2`

---

## Esercizio 8 — La biblioteca di dipartimento (`biblioteca.py`)

**Consegna**

1. Definite una classe `Pubblicazione` con titolo e anno, l'attributo di classe `GIORNI = 30` (durata del prestito), un `__str__` come nell'esempio e un `__lt__` che ordina per anno.
2. Definite la sottoclasse `Rivista(Pubblicazione)`, che cambia solo `GIORNI = 7`. Nel `__str__` usate `self.GIORNI`: così ogni oggetto prende il valore della sua classe.
3. Definite una classe `Biblioteca` con una lista `_catalogo` e i metodi `aggiungi`, `cerca(self, parola: str)`, che restituisce le pubblicazioni con quella parola nel titolo (senza distinguere maiuscole e minuscole), e `in_ordine`, che restituisce il catalogo ordinato con `sorted`.
4. Inserite le pubblicazioni della tabella, stampate il catalogo in ordine e il numero di titoli che contengono `statistica`.

| Titolo | Tipo, anno |
|---|---|
| Statistica di base | libro, 2019 |
| Rivista di statistica applicata | rivista, 2024 |
| Probabilità e inferenza | libro, 2015 |
| Bollettino di demografia | rivista, 2023 |

**Esempio di esecuzione**

```
2015 Probabilità e inferenza: 30 giorni
2019 Statistica di base: 30 giorni
2023 Bollettino di demografia: 7 giorni
2024 Rivista di statistica applicata: 7 giorni
Titoli con 'statistica': 2
```

**Provate anche**

- aggiungete `Rivista("Statistica in medicina", 2021)` → compare `2021 Statistica in medicina: 7 giorni` e `Titoli con 'statistica': 3`
- `Rivista.GIORNI = 14` prima delle stampe → le riviste hanno 14 giorni, i libri restano a 30
- `bib.cerca("STATISTICA")` → gli stessi 2 risultati

---

## Challenge a scelta

Scegliete un tema. Le cinque challenge hanno la stessa difficoltà e usano gli stessi strumenti: cambiano la storia e i dati. Ogni tema continua nei laboratori successivi.

| Tema | Challenge | File |
|---|---|---|
| Mercati e finanza | Il portafoglio a oggetti | `ch_mercati.py` |
| Sport | Il campionato a oggetti | `ch_sport.py` |
| Imprese e marketing | Il negozio online a oggetti | `ch_negozio.py` |
| Salute e scienza | Lo studio clinico a oggetti | `ch_salute.py` |
| Caso e probabilità | Il tavolo da gioco a oggetti | `ch_probabilita.py` |

**Tutte le challenge chiedono:**

- Definite una classe per l'elemento del tema. `__init__` riceve i dati e li controlla: se non sono validi solleva `ValueError` con un messaggio che contiene il nome dell'elemento; altrimenti li salva in attributi con type hints.
- La classe ha due metodi che calcolano qualcosa dai dati, un `__str__` per la stampa e un `__lt__` per ordinare gli oggetti con `sorted`.
- Definite una classe contenitore che ha come attributo una lista di oggetti della prima classe (composizione), con i metodi `aggiungi`, `cerca` (restituisce l'oggetto oppure `None`) e un metodo che calcola una statistica su tutti gli oggetti.
- Create gli oggetti con i dati della consegna in un ciclo e aggiungeteli al contenitore. Uno dei dati è sbagliato: catturate il `ValueError` con `try/except` e stampatene il messaggio.
- Stampate gli oggetti in ordine con `sorted`, il risultato di due ricerche (una riuscita e una no) e la statistica.

---

### Challenge · Mercati e finanza — Il portafoglio a oggetti (`ch_mercati.py`)

**Consegna**

1. Classe `Titolo` con sigla, numero di azioni e lista dei prezzi di chiusura. Se le azioni non sono positive o un prezzo non è positivo (o ci sono meno di due prezzi), `ValueError("MIB: azioni o prezzi non validi")`.
2. Metodi `rendimento()`, dal primo all'ultimo prezzo, e `valore()`, azioni per ultimo prezzo. `__lt__` confronta i rendimenti.
3. Classe `Portafoglio` con il titolare e una lista di titoli; metodi `aggiungi`, `cerca(sigla)` e `valore_totale()`.
4. Create il portafoglio di Giulia con i titoli della tabella e stampate i titoli dal rendimento più alto (`reverse=True`), le ricerche di `BANK` e `MIB` e il valore totale.

| Titolo, azioni | Prezzi 01/12 – 04/12 |
|---|---|
| ENRG, 20 | 24.10, 24.60, 25.30, 25.10 |
| BANK, 50 | 12.40, 12.20, 12.70, 12.90 |
| TECH, 10 | 48.00, 49.20, 50.40, 51.20 |
| MIB, 0 | 33.50, 33.90, 34.20, 34.10 |

**Esempio di esecuzione**

```
MIB: azioni o prezzi non validi
TECH: valore 512.00, rendimento 6.7%
ENRG: valore 502.00, rendimento 4.1%
BANK: valore 645.00, rendimento 4.0%
BANK: valore 645.00, rendimento 4.0%
None
Valore totale: 1659.00
```

**Provate anche**

- MIB con 5 azioni → `MIB: valore 170.50, rendimento 1.8%` in fondo, `Valore totale: 1829.50`
- ENRG con 40 azioni → `ENRG: valore 1004.00, rendimento 4.1%`, `Valore totale: 2161.00`
- `print(port.cerca("ENRG") < port.cerca("TECH"))` → `True`

---

### Challenge · Sport — Il campionato a oggetti (`ch_sport.py`)

**Consegna**

1. Classe `Pilota` con nome, scuderia e lista dei tempi sul giro. Se la lista è vuota o un tempo non è positivo, `ValueError("Neri: tempi non validi")`.
2. Metodi `media()` e `migliore()` (il tempo minimo). `__lt__` confronta le medie: viene prima il pilota più veloce.
3. Classe `Gara` con il circuito e una lista di piloti; metodi `aggiungi`, `cerca(nome)` e `giro_veloce()`, il miglior tempo tra tutti i piloti.
4. Create la gara di Monza con i piloti della tabella e stampate i piloti in ordine, le ricerche di `Lanza` e `Neri` e il giro più veloce.

| Pilota, scuderia | Tempi dei giri 1-3 |
|---|---|
| Ferri, Scuderia Rossa | 92.4, 92.1, 92.6 |
| Lanza, Scuderia Rossa | 92.9, 92.7, 92.5 |
| Moro, Scuderia Blu | 93.1, 92.8, 92.3 |
| Neri, Scuderia Blu | 93.6, 93.0, 0.0 |

**Esempio di esecuzione**

```
Neri: tempi non validi
Ferri: media 92.37, migliore 92.10
Lanza: media 92.70, migliore 92.50
Moro: media 92.73, migliore 92.30
Lanza: media 92.70, migliore 92.50
None
Giro più veloce: 92.10
```

**Provate anche**

- terzo giro di Neri `93.4` → `Neri: media 93.33, migliore 93.00` in fondo
- terzo giro di Moro `91.9` → `Giro più veloce: 91.90` e Moro passa davanti a Lanza
- `print(gara.cerca("Ferri") < gara.cerca("Moro"))` → `True`

---

### Challenge · Imprese e marketing — Il negozio online a oggetti (`ch_negozio.py`)

**Consegna**

1. Classe `Prodotto` con nome, prezzo e lista dei pezzi venduti ogni settimana. Se il prezzo non è positivo o una vendita è negativa (o la lista è vuota), `ValueError("lampada: prezzo o vendite non validi")`.
2. Metodi `pezzi()`, il totale venduto, e `fatturato()`, prezzo per pezzi. `__lt__` confronta i fatturati.
3. Classe `Negozio` con il nome e una lista di prodotti; metodi `aggiungi`, `cerca(nome)` e `fatturato_totale()`.
4. Create il negozio con i prodotti della tabella e stampate i prodotti dal fatturato più alto (`reverse=True`), le ricerche di `cuffie` e `lampada` e il fatturato totale.

| Prodotto, prezzo | Vendite settimana 1-3 |
|---|---|
| zaino, 39.90 | 3, 5, 4 |
| borraccia, 14.50 | 10, 8, 12 |
| quaderno, 3.20 | 30, 25, 30 |
| cuffie, 59.00 | 2, 4, 2 |
| lampada, 24.90 | 2, −1, 3 |

**Esempio di esecuzione**

```
lampada: prezzo o vendite non validi
zaino: 12 pezzi, fatturato 478.80
cuffie: 8 pezzi, fatturato 472.00
borraccia: 30 pezzi, fatturato 435.00
quaderno: 85 pezzi, fatturato 272.00
cuffie: 8 pezzi, fatturato 472.00
None
Fatturato totale: 1657.80
```

**Provate anche**

- vendite della lampada `[2, 1, 3]` → `lampada: 6 pezzi, fatturato 149.40` in fondo, `Fatturato totale: 1807.20`
- cuffie a `49.00` → `cuffie: 8 pezzi, fatturato 392.00`, dopo la borraccia
- `print(negozio.cerca("quaderno") < negozio.cerca("zaino"))` → `True`

---

### Challenge · Salute e scienza — Lo studio clinico a oggetti (`ch_salute.py`)

**Consegna**

1. Classe `Paziente` con codice, gruppo e lista delle pressioni sistoliche misurate a ogni visita. Se ci sono meno di due misure o una misura è fuori da 60–250 mmHg, `ValueError("P05: misure non valide")`.
2. Metodi `variazione()`, ultima misura meno prima, e `migliorato()`, vero se la pressione è scesa di almeno 10 mmHg. `__lt__` confronta le variazioni: viene prima chi è sceso di più.
3. Classe `Studio` con il nome e una lista di pazienti; metodi `aggiungi`, `cerca(codice)` e `quota_migliorati()`.
4. Create lo studio con i pazienti della tabella e stampate i pazienti in ordine, le ricerche di `P02` e `P05` e la quota di migliorati.

| Paziente, gruppo | Misure (mmHg) |
|---|---|
| P01, trattamento | 152, 146, 138 |
| P02, controllo | 148, 147, 145 |
| P03, trattamento | 160, 151, 149 |
| P04, controllo | 155, 150, 144 |
| P05, trattamento | 145, 0, 139 |

**Esempio di esecuzione**

```
P05: misure non valide
P01 (trattamento): variazione -14.0 mmHg
P03 (trattamento): variazione -11.0 mmHg
P04 (controllo): variazione -11.0 mmHg
P02 (controllo): variazione -3.0 mmHg
P02 (controllo): variazione -3.0 mmHg
None
Migliorati: 75.0%
```

**Provate anche**

- seconda misura di P05 `141` → `P05 (trattamento): variazione -6.0 mmHg` prima di P02, `Migliorati: 60.0%`
- `print(studio.cerca("P03").migliorato())` → `True`
- `print(studio.cerca("P01") < studio.cerca("P02"))` → `True`

---

### Challenge · Caso e probabilità — Il tavolo da gioco a oggetti (`ch_probabilita.py`)

**Consegna**

1. Classe `Dado` con il colore e la lista dei risultati dei lanci, registrati a mano. Se la lista è vuota o un risultato è fuori da 1–6, `ValueError("bianco: lanci non validi")`.
2. Metodi `media()` e `quota(faccia)`, la frequenza relativa di una faccia. `__lt__` confronta le medie.
3. Classe `Tavolo` con il nome e una lista di dadi; metodi `aggiungi`, `cerca(colore)` e `media_generale()`, la media di tutti i lanci di tutti i dadi.
4. Create il tavolo con i dadi della tabella e stampate i dadi dalla media più alta (`reverse=True`), con la quota di 6, le ricerche di `blu` e `bianco` e la media generale.

| Dado | Lanci |
|---|---|
| rosso | 4, 6, 1, 6, 3, 6 |
| blu | 2, 5, 3, 1, 4, 6 |
| verde | 6, 2, 5, 3, 3, 1 |
| bianco | 1, 4, 7, 2, 5, 3 |

**Esempio di esecuzione**

```
bianco: lanci non validi
rosso: media 4.33, quota di 6: 50.0%
blu: media 3.50, quota di 6: 16.7%
verde: media 3.33, quota di 6: 16.7%
blu: media 3.50, quota di 6: 16.7%
None
Media di tutti i lanci: 3.72
```

**Provate anche**

- terzo lancio del bianco `6` → `bianco: media 3.50, quota di 6: 16.7%` dopo il blu, `Media di tutti i lanci: 3.67`
- `print(tavolo.cerca("verde").quota(3))` → `0.3333333333333333`
- `print(tavolo.cerca("verde") < tavolo.cerca("rosso"))` → `True`

---

## Domande di verifica

1. Che differenza c'è tra la classe `Esame` e l'oggetto `Esame("Analisi 1", 12, 26)`? Quanti oggetti crea `esame.py`?
2. Ogni metodo ha `self` come primo parametro, ma in `e.punti()` non lo scrivete. Chi lo passa?
3. In `segreteria.py` il contatore si aggiorna con `Ticket.emessi += 1`. Cosa succederebbe scrivendo `self.emessi += 1`?
4. Che differenza c'è tra `__str__` e `__repr__`? Quale usa `print(coda)` per gli elementi della lista?
5. In `erasmus.py`, perché `__lt__` confronta con `>` (`self.media > altro.media`)?
6. In `campione.py`, perché `media` è una `@property` e non un attributo calcolato una volta in `__init__`?
7. Il libretto contiene esami (composizione); un abbonamento studente è un abbonamento (ereditarietà). Fate un altro esempio per ciascuna.
