# Glossario Python

Tutti i termini chiave del corso, organizzati per argomento. Per ogni termine trovi una definizione semplice, la lezione di riferimento e un esempio minimale.

---

## 1. Concetti base

### Variabile
**Definizione:** Un nome che fa riferimento a un valore memorizzato in memoria. In Python le variabili non hanno un tipo fisso: il tipo dipende dal valore assegnato.
**Lezione:** F07
**Esempio:**
```python
eta = 25
nome = "Luca"
```

### Tipo
**Definizione:** La categoria di un dato che determina quali operazioni si possono fare su di esso. I tipi principali sono int, float, str, bool.
**Lezione:** F07
**Esempio:**
```python
type(42)      # <class 'int'>
type("ciao")  # <class 'str'>
```

### Oggetto
**Definizione:** In Python tutto e' un oggetto: ogni dato ha un tipo, un valore e un'identita' (indirizzo in memoria). Anche numeri e stringhe sono oggetti.
**Lezione:** F07
**Esempio:**
```python
x = 42
id(x)     # identita' univoca dell'oggetto
type(x)   # tipo dell'oggetto
```

### Riferimento
**Definizione:** Il collegamento tra un nome (variabile) e l'oggetto a cui punta. In Python l'assegnamento crea un riferimento, non una copia.
**Lezione:** F07
**Esempio:**
```python
a = [1, 2, 3]
b = a          # b punta allo STESSO oggetto di a
b.append(4)    # modifica visibile anche tramite a
```

### Assegnamento
**Definizione:** L'operazione che associa un nome a un valore tramite l'operatore `=`. Non e' un confronto (quello si fa con `==`).
**Lezione:** F07
**Esempio:**
```python
x = 10       # assegnamento
x = x + 1    # riassegnamento (x ora vale 11)
```

### Espressione
**Definizione:** Una combinazione di valori, variabili e operatori che Python valuta producendo un risultato. Ogni espressione ha un valore.
**Lezione:** F07
**Esempio:**
```python
3 + 4 * 2     # espressione che vale 11
x > 0         # espressione booleana
```

### Istruzione
**Definizione:** Un comando completo che Python puo' eseguire. A differenza dell'espressione, un'istruzione non necessariamente produce un valore.
**Lezione:** F07
**Esempio:**
```python
x = 5            # istruzione di assegnamento
print("ciao")    # istruzione di chiamata
if x > 0:        # istruzione condizionale
    pass
```

### Valore
**Definizione:** Un dato concreto come un numero, una stringa o un booleano. E' cio' che le espressioni producono e le variabili contengono.
**Lezione:** F07
**Esempio:**
```python
42          # valore intero
"ciao"      # valore stringa
True        # valore booleano
```

### Letterale
**Definizione:** Un valore scritto direttamente nel codice sorgente (un numero, una stringa tra virgolette, True/False, None).
**Lezione:** F07
**Esempio:**
```python
3.14        # letterale float
"hello"     # letterale stringa
[1, 2, 3]   # letterale lista
```

### Identificatore
**Definizione:** Il nome dato a una variabile, funzione, classe o modulo. Deve iniziare con una lettera o underscore, puo' contenere lettere, cifre e underscore.
**Lezione:** F07
**Esempio:**
```python
mia_variabile = 10    # identificatore valido
_privato = 5          # valido (inizia con _)
# 2nome = "no"        # ERRORE: non puo' iniziare con una cifra
```

### Parola chiave
**Definizione:** Un nome riservato da Python che non puo' essere usato come identificatore. Esempi: if, else, for, while, def, class, return, import.
**Lezione:** F07
**Esempio:**
```python
import keyword
print(keyword.kwlist)   # lista di tutte le parole chiave
# ['False', 'None', 'True', 'and', 'as', 'assert', ...]
```

### Commento
**Definizione:** Testo nel codice ignorato da Python, usato per spiegare il codice ai lettori umani. Si scrive con `#` per una riga, oppure con triple virgolette per commenti multi-riga (docstring).
**Lezione:** F07
**Esempio:**
```python
# Questo e' un commento su una riga
x = 5  # commento a fine riga

"""Questo e' una docstring,
usata per documentare funzioni e classi."""
```

---

## 2. Tipi di dato

### Intero (int)
**Definizione:** Tipo numerico che rappresenta numeri interi senza limite di dimensione. Supporta le operazioni aritmetiche standard.
**Lezione:** F07
**Esempio:**
```python
eta = 20
grande = 10 ** 100    # Python gestisce numeri grandi senza problemi
```

### Numero in virgola mobile (float)
**Definizione:** Tipo numerico che rappresenta numeri con la virgola (decimali). Ha precisione limitata (~15-17 cifre significative) a causa della rappresentazione binaria.
**Lezione:** F07
**Esempio:**
```python
media = 27.5
pi = 3.14159
# Attenzione: 0.1 + 0.2 != 0.3 (errore di rappresentazione)
```

### Stringa (str)
**Definizione:** Tipo che rappresenta testo, cioe' una sequenza immutabile di caratteri. Si delimita con apici singoli o doppi.
**Lezione:** F07
**Esempio:**
```python
nome = "Luca"
frase = 'Ciao mondo'
multi = """Testo
su piu' righe"""
```

### Booleano (bool)
**Definizione:** Tipo con solo due valori possibili: `True` e `False`. Usato nelle condizioni e nei confronti. In Python bool e' un sottotipo di int (True=1, False=0).
**Lezione:** F08
**Esempio:**
```python
superato = voto >= 18     # True o False
print(True + True)        # 2 (perche' True vale 1)
```

### None
**Definizione:** Valore speciale che rappresenta l'assenza di valore. E' l'unico valore del tipo `NoneType`. Le funzioni senza return esplicito restituiscono None.
**Lezione:** F08
**Esempio:**
```python
risultato = print("ciao")   # print restituisce None
x = None                    # variabile senza valore
if x is None:
    print("Nessun valore")
```

### Tipo dinamico
**Definizione:** In Python il tipo di una variabile e' determinato a runtime dal valore assegnato e puo' cambiare durante l'esecuzione. Non serve dichiarare il tipo in anticipo.
**Lezione:** F07
**Esempio:**
```python
x = 42        # x e' int
x = "ciao"    # ora x e' str (nessun errore)
x = [1, 2]    # ora x e' list
```

### Casting / Conversione
**Definizione:** L'operazione di trasformare un valore da un tipo a un altro usando funzioni come int(), float(), str(), bool().
**Lezione:** F08
**Esempio:**
```python
int("42")       # 42 (str -> int)
float("3.14")   # 3.14 (str -> float)
str(42)         # "42" (int -> str)
int(3.9)        # 3 (tronca, NON arrotonda)
```

### f-string
**Definizione:** Stringa formattata (preceduta da `f`) che permette di inserire espressioni Python direttamente dentro le parentesi graffe. Introdotta in Python 3.6.
**Lezione:** F10
**Esempio:**
```python
nome = "Luca"
media = 27.5
print(f"Studente: {nome}, media: {media:.1f}")
# Studente: Luca, media: 27.5
```

---

## 3. Strutture dati

### Lista
**Definizione:** Collezione ordinata e mutabile di elementi, delimitata da parentesi quadre. Puo' contenere elementi di tipi diversi e ammette duplicati.
**Lezione:** F11
**Esempio:**
```python
voti = [28, 30, 25, 27]
voti.append(26)      # aggiunge in fondo
voti[0] = 29         # modifica il primo elemento
```

### Tupla
**Definizione:** Collezione ordinata e immutabile di elementi, delimitata da parentesi tonde. Una volta creata non puo' essere modificata. Usata per dati fissi.
**Lezione:** F11
**Esempio:**
```python
coordinate = (45.07, 7.69)
x, y = coordinate    # unpacking
# coordinate[0] = 0  # ERRORE: le tuple sono immutabili
```

### Dizionario
**Definizione:** Collezione di coppie chiave-valore, delimitata da parentesi graffe. Le chiavi devono essere uniche e immutabili. Accesso per chiave in tempo O(1).
**Lezione:** F12
**Esempio:**
```python
studente = {"nome": "Luca", "eta": 20, "media": 27.5}
print(studente["nome"])     # "Luca"
studente["corso"] = "Stat"  # aggiunge nuova coppia
```

### Set
**Definizione:** Collezione non ordinata di elementi unici, delimitata da parentesi graffe. Non ammette duplicati. Supporta operazioni insiemistiche (unione, intersezione).
**Lezione:** F12
**Esempio:**
```python
numeri = {1, 2, 3, 2, 1}   # {1, 2, 3} (duplicati rimossi)
numeri.add(4)
pari = {2, 4, 6}
print(numeri & pari)        # intersezione: {2, 4}
```

### Array (NumPy)
**Definizione:** Struttura dati di NumPy ottimizzata per calcoli numerici su collezioni omogenee (tutti dello stesso tipo). Supporta operazioni vettoriali molto efficienti.
**Lezione:** F17
**Esempio:**
```python
import numpy as np
dati = np.array([1, 2, 3, 4, 5])
print(dati.mean())    # 3.0
print(dati * 2)       # [2, 4, 6, 8, 10] (operazione vettoriale)
```

### DataFrame (Pandas)
**Definizione:** Tabella bidimensionale di Pandas con righe e colonne etichettate. E' la struttura fondamentale per l'analisi dati in Python, simile a un foglio di calcolo.
**Lezione:** F17
**Esempio:**
```python
import pandas as pd
df = pd.DataFrame({"nome": ["Luca", "Anna"], "voto": [28, 30]})
print(df["voto"].mean())    # 29.0
```

### Indice
**Definizione:** Numero intero che indica la posizione di un elemento in una sequenza. In Python gli indici partono da 0. Indici negativi contano dalla fine (-1 = ultimo).
**Lezione:** F11
**Esempio:**
```python
lista = ["a", "b", "c", "d"]
lista[0]     # "a" (primo elemento)
lista[-1]    # "d" (ultimo elemento)
lista[-2]    # "c" (penultimo)
```

### Slicing
**Definizione:** Operazione che estrae una sotto-sequenza da una lista, tupla o stringa usando la sintassi `[inizio:fine:passo]`. L'elemento a posizione `fine` e' escluso.
**Lezione:** F11
**Esempio:**
```python
numeri = [0, 1, 2, 3, 4, 5]
numeri[1:4]     # [1, 2, 3]
numeri[::2]     # [0, 2, 4] (ogni 2)
numeri[::-1]    # [5, 4, 3, 2, 1, 0] (invertita)
```

### Mutabilita'
**Definizione:** Proprieta' di un oggetto che puo' essere modificato dopo la creazione. Liste, dizionari e set sono mutabili.
**Lezione:** F11
**Esempio:**
```python
lista = [1, 2, 3]
lista[0] = 99       # OK: le liste sono mutabili
lista.append(4)     # OK: aggiunge un elemento
```

### Immutabilita'
**Definizione:** Proprieta' di un oggetto che NON puo' essere modificato dopo la creazione. Stringhe, tuple, interi e float sono immutabili.
**Lezione:** F11
**Esempio:**
```python
s = "ciao"
# s[0] = "C"        # ERRORE: le stringhe sono immutabili
s = "C" + s[1:]     # OK: crea una NUOVA stringa "Ciao"
```

---

## 4. Flusso di controllo

### Condizionale (if/elif/else)
**Definizione:** Istruzione che esegue blocchi di codice diversi in base a condizioni booleane. `if` verifica la prima condizione, `elif` le successive, `else` il caso residuo.
**Lezione:** F08
**Esempio:**
```python
voto = 28
if voto >= 30:
    print("Ottimo")
elif voto >= 24:
    print("Buono")
elif voto >= 18:
    print("Sufficiente")
else:
    print("Insufficiente")
```

### Ciclo for
**Definizione:** Istruzione che ripete un blocco di codice per ogni elemento di un iterabile (lista, stringa, range, ecc.). Il numero di iterazioni e' determinato dalla lunghezza dell'iterabile.
**Lezione:** F09
**Esempio:**
```python
for voto in [28, 30, 25]:
    print(voto)

for i in range(5):
    print(i)    # stampa 0, 1, 2, 3, 4
```

### Ciclo while
**Definizione:** Istruzione che ripete un blocco di codice finche' una condizione e' vera. Richiede che la condizione diventi falsa a un certo punto, altrimenti si crea un ciclo infinito.
**Lezione:** F09
**Esempio:**
```python
contatore = 0
while contatore < 5:
    print(contatore)
    contatore += 1
```

### Iterazione
**Definizione:** Il processo di scorrere uno a uno gli elementi di una collezione o sequenza. In Python si realizza tipicamente con il ciclo for.
**Lezione:** F09
**Esempio:**
```python
for carattere in "Python":
    print(carattere)    # stampa P, y, t, h, o, n
```

### break
**Definizione:** Istruzione che interrompe immediatamente il ciclo (for o while) piu' interno in cui si trova. L'esecuzione prosegue con la prima istruzione dopo il ciclo.
**Lezione:** F09
**Esempio:**
```python
for n in [3, 7, -2, 5]:
    if n < 0:
        print(f"Trovato negativo: {n}")
        break
```

### continue
**Definizione:** Istruzione che salta il resto del corpo del ciclo e passa direttamente all'iterazione successiva.
**Lezione:** F09
**Esempio:**
```python
for n in [1, -2, 3, -4, 5]:
    if n < 0:
        continue      # salta i negativi
    print(n)           # stampa solo 1, 3, 5
```

### range
**Definizione:** Funzione built-in che genera una sequenza immutabile di numeri interi. Usata principalmente nei cicli for per ripetere un'azione N volte.
**Lezione:** F09
**Esempio:**
```python
range(5)          # 0, 1, 2, 3, 4
range(2, 8)       # 2, 3, 4, 5, 6, 7
range(0, 10, 2)   # 0, 2, 4, 6, 8
```

### Comprehension
**Definizione:** Sintassi compatta per creare liste, dizionari o set a partire da un iterabile, opzionalmente con filtro. Alternativa concisa al ciclo for esplicito.
**Lezione:** F10
**Esempio:**
```python
quadrati = [x**2 for x in range(10)]
pari = [x for x in range(20) if x % 2 == 0]
dizionario = {x: x**2 for x in range(5)}
```

---

## 5. Funzioni

### Funzione
**Definizione:** Blocco di codice riutilizzabile, definito con `def`, che accetta parametri in input e puo' restituire un valore. Permette di organizzare il codice ed evitare ripetizioni.
**Lezione:** F13
**Esempio:**
```python
def media(valori):
    return sum(valori) / len(valori)

risultato = media([28, 30, 25])   # 27.666...
```

### Parametro
**Definizione:** Variabile elencata nella definizione di una funzione che ricevera' un valore quando la funzione viene chiamata. Si distingue dall'argomento (il valore effettivo passato).
**Lezione:** F13
**Esempio:**
```python
def saluta(nome, titolo="Sig."):   # nome e titolo sono parametri
    print(f"Buongiorno {titolo} {nome}")
```

### Argomento
**Definizione:** Il valore effettivo passato a una funzione quando viene chiamata. Puo' essere posizionale (in ordine) o con nome (keyword).
**Lezione:** F13
**Esempio:**
```python
saluta("Rossi")                # "Rossi" e' l'argomento posizionale
saluta("Rossi", titolo="Dr.")  # titolo="Dr." e' un argomento keyword
```

### return
**Definizione:** Istruzione che termina l'esecuzione di una funzione e restituisce un valore al chiamante. Senza return, la funzione restituisce None.
**Lezione:** F13
**Esempio:**
```python
def quadrato(n):
    return n ** 2

def senza_return(n):
    print(n ** 2)       # stampa ma non restituisce

x = quadrato(5)        # x = 25
y = senza_return(5)    # stampa 25, ma y = None
```

### Scope (ambito)
**Definizione:** La regione del codice in cui un nome (variabile) e' accessibile. Python segue la regola LEGB: Local, Enclosing, Global, Built-in.
**Lezione:** F14
**Esempio:**
```python
x = "globale"           # scope globale

def funzione():
    x = "locale"        # scope locale (non modifica la globale)
    print(x)            # "locale"

funzione()
print(x)                # "globale"
```

### Variabile locale
**Definizione:** Variabile definita all'interno di una funzione, accessibile solo dentro quella funzione. Viene creata alla chiamata e distrutta al termine.
**Lezione:** F14
**Esempio:**
```python
def calcola():
    risultato = 42      # variabile locale
    return risultato

# print(risultato)      # ERRORE: risultato non esiste fuori dalla funzione
```

### Variabile globale
**Definizione:** Variabile definita al livello principale del modulo, accessibile ovunque nel file. Per modificarla dentro una funzione serve la keyword `global` (sconsigliato).
**Lezione:** F14
**Esempio:**
```python
contatore = 0           # variabile globale

def incrementa():
    global contatore    # necessario per MODIFICARE la globale
    contatore += 1
```

### Closure
**Definizione:** Funzione interna che "ricorda" le variabili della funzione esterna in cui e' stata definita, anche dopo che quest'ultima ha terminato l'esecuzione.
**Lezione:** F14
**Esempio:**
```python
def crea_moltiplicatore(fattore):
    def moltiplica(x):
        return x * fattore    # fattore viene "ricordato"
    return moltiplica

doppio = crea_moltiplicatore(2)
doppio(5)    # 10
```

### Lambda
**Definizione:** Funzione anonima (senza nome) definita in una sola riga con la keyword `lambda`. Utile per funzioni semplici passate come argomento a sorted(), map(), filter().
**Lezione:** F14
**Esempio:**
```python
quadrato = lambda x: x ** 2
quadrato(5)   # 25

# Uso tipico: ordinamento personalizzato
studenti = [("Luca", 28), ("Anna", 30)]
sorted(studenti, key=lambda s: s[1])
```

### Decoratore
**Definizione:** Funzione che modifica il comportamento di un'altra funzione senza cambiarne il codice. Si applica con la sintassi `@nome_decoratore` sopra la definizione della funzione.
**Lezione:** F14
**Esempio:**
```python
def registra(func):
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@registra
def somma(a, b):
    return a + b

somma(3, 4)    # stampa "Chiamata a somma", restituisce 7
```

---

## 6. OOP (Programmazione orientata agli oggetti)

### Classe
**Definizione:** Un modello (template) che definisce la struttura e il comportamento di un tipo di oggetto. Contiene attributi (dati) e metodi (funzioni).
**Lezione:** F16
**Esempio:**
```python
class Studente:
    def __init__(self, nome, matricola):
        self.nome = nome
        self.matricola = matricola
```

### Istanza (oggetto)
**Definizione:** Un oggetto concreto creato a partire da una classe. Ogni istanza ha i propri valori per gli attributi definiti dalla classe.
**Lezione:** F16
**Esempio:**
```python
s1 = Studente("Luca", "S12345")    # s1 e' un'istanza di Studente
s2 = Studente("Anna", "S67890")    # s2 e' un'altra istanza
```

### Attributo
**Definizione:** Una variabile associata a un oggetto o a una classe. Gli attributi di istanza sono specifici di ogni oggetto, quelli di classe sono condivisi da tutte le istanze.
**Lezione:** F16
**Esempio:**
```python
class Cerchio:
    pi = 3.14159             # attributo di classe

    def __init__(self, raggio):
        self.raggio = raggio  # attributo di istanza
```

### Metodo
**Definizione:** Una funzione definita all'interno di una classe che opera sull'istanza. Il primo parametro e' sempre `self`, che rappresenta l'istanza su cui il metodo e' chiamato.
**Lezione:** F16
**Esempio:**
```python
class Studente:
    def __init__(self, nome, voti):
        self.nome = nome
        self.voti = voti

    def media(self):       # metodo
        return sum(self.voti) / len(self.voti)
```

### Costruttore (__init__)
**Definizione:** Metodo speciale chiamato automaticamente quando si crea una nuova istanza della classe. Serve per inizializzare gli attributi dell'oggetto.
**Lezione:** F16
**Esempio:**
```python
class Punto:
    def __init__(self, x, y):   # costruttore
        self.x = x
        self.y = y

p = Punto(3, 4)    # __init__ viene chiamato automaticamente
```

### Ereditarieta'
**Definizione:** Meccanismo per cui una classe (figlia) puo' ereditare attributi e metodi da un'altra classe (genitore), estendendola o modificandola.
**Lezione:** F16
**Esempio:**
```python
class Persona:
    def __init__(self, nome):
        self.nome = nome

class Studente(Persona):          # eredita da Persona
    def __init__(self, nome, matricola):
        super().__init__(nome)    # chiama il costruttore del genitore
        self.matricola = matricola
```

### self
**Definizione:** Riferimento all'istanza corrente della classe. E' il primo parametro di ogni metodo e permette di accedere agli attributi e altri metodi dell'oggetto.
**Lezione:** F16
**Esempio:**
```python
class Contatore:
    def __init__(self):
        self.valore = 0     # self si riferisce all'istanza

    def incrementa(self):
        self.valore += 1    # modifica l'attributo dell'istanza
```

### Incapsulamento
**Definizione:** Principio OOP che consiste nel nascondere i dettagli interni di un oggetto e esporre solo un'interfaccia pubblica. In Python e' una convenzione (underscore), non un vincolo rigido.
**Lezione:** F16
**Esempio:**
```python
class ContoBancario:
    def __init__(self, saldo):
        self._saldo = saldo      # _ = "privato" per convenzione

    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo

    def get_saldo(self):
        return self._saldo
```

---

## 7. File e gestione errori

### File handle
**Definizione:** Oggetto restituito dalla funzione `open()` che rappresenta un file aperto. Attraverso di esso si possono leggere o scrivere dati nel file.
**Lezione:** F15
**Esempio:**
```python
f = open("dati.txt", "r")     # f e' il file handle
contenuto = f.read()
f.close()                      # sempre chiudere il file!
```

### Encoding (codifica)
**Definizione:** Il sistema usato per rappresentare i caratteri come sequenze di byte. UTF-8 e' lo standard raccomandato e supporta tutti i caratteri (incluse lettere accentate).
**Lezione:** F15
**Esempio:**
```python
# Specificare sempre l'encoding per evitare problemi con le lettere accentate
f = open("dati.txt", "r", encoding="utf-8")
```

### Eccezione
**Definizione:** Un errore che si verifica durante l'esecuzione del programma. Se non gestita, interrompe il programma. Esempi comuni: ValueError, TypeError, FileNotFoundError, KeyError.
**Lezione:** F15
**Esempio:**
```python
int("abc")      # ValueError: invalid literal for int()
lista = [1, 2]
lista[5]        # IndexError: list index out of range
```

### try/except
**Definizione:** Struttura per gestire le eccezioni. Il codice nel blocco `try` viene eseguito; se si verifica un'eccezione del tipo specificato in `except`, viene eseguito il blocco except anziche' interrompere il programma.
**Lezione:** F15
**Esempio:**
```python
try:
    numero = int(input("Numero: "))
    risultato = 10 / numero
except ValueError:
    print("Input non valido")
except ZeroDivisionError:
    print("Divisione per zero!")
finally:
    print("Eseguito sempre")
```

### Context manager (with)
**Definizione:** Costrutto che garantisce la corretta gestione delle risorse (apertura/chiusura). Con `with`, il file viene chiuso automaticamente alla fine del blocco, anche in caso di errore.
**Lezione:** F15
**Esempio:**
```python
with open("dati.txt", "r", encoding="utf-8") as f:
    contenuto = f.read()
# qui il file e' gia' stato chiuso automaticamente
```

### CSV
**Definizione:** Formato di file testuale (Comma-Separated Values) in cui ogni riga rappresenta un record e i campi sono separati da virgole (o punto e virgola). Molto usato per dati tabulari.
**Lezione:** F15
**Esempio:**
```python
import csv
with open("dati.csv", "r") as f:
    lettore = csv.reader(f)
    for riga in lettore:
        print(riga)    # riga e' una lista di stringhe
```

### JSON
**Definizione:** Formato di file testuale (JavaScript Object Notation) per dati strutturati, basato su coppie chiave-valore e liste. Molto usato per scambio dati e API web.
**Lezione:** F15
**Esempio:**
```python
import json
with open("config.json", "r") as f:
    dati = json.load(f)        # legge JSON -> dict Python

with open("output.json", "w") as f:
    json.dump(dati, f, indent=2)  # dict Python -> JSON
```

### Percorso (path)
**Definizione:** La posizione di un file o cartella nel file system. Puo' essere assoluto (dalla radice: `/home/utente/file.txt`) o relativo (dalla posizione corrente: `dati/file.txt`).
**Lezione:** F15
**Esempio:**
```python
from pathlib import Path

percorso = Path("dati") / "risultati" / "output.csv"
print(percorso.exists())      # True se il file esiste
print(percorso.suffix)        # ".csv"
print(percorso.stem)          # "output"
```

---

## 8. Ecosistema Python

### Modulo
**Definizione:** Un file Python (`.py`) che contiene definizioni di funzioni, classi e variabili. Puo' essere importato in altri file per riutilizzare il codice.
**Lezione:** F14
**Esempio:**
```python
# File: utilita.py
def saluta(nome):
    return f"Ciao {nome}"

# File: main.py
import utilita
print(utilita.saluta("Luca"))
```

### Pacchetto
**Definizione:** Una cartella contenente piu' moduli Python e un file `__init__.py`. Permette di organizzare il codice in gerarchie logiche (es. `numpy.random`).
**Lezione:** F14
**Esempio:**
```python
# Struttura:
# mio_pacchetto/
#   __init__.py
#   analisi.py
#   grafici.py

from mio_pacchetto import analisi
```

### Libreria
**Definizione:** Termine generico per un insieme di moduli e pacchetti che forniscono funzionalita' aggiuntive. Esempi: NumPy (calcolo numerico), Pandas (analisi dati), Matplotlib (grafici).
**Lezione:** F14
**Esempio:**
```python
import numpy as np         # libreria per calcolo numerico
import pandas as pd        # libreria per analisi dati
import matplotlib.pyplot as plt  # libreria per grafici
```

### import
**Definizione:** Istruzione che rende disponibile nel file corrente il codice definito in un modulo esterno. Diverse forme: `import modulo`, `from modulo import funzione`, `import modulo as alias`.
**Lezione:** F14
**Esempio:**
```python
import math                     # tutto il modulo
from math import sqrt, pi       # solo specifiche funzioni
import numpy as np              # con alias (abbreviazione)
from os.path import join        # da sotto-modulo
```

### pip
**Definizione:** Il gestore di pacchetti di Python. Permette di installare, aggiornare e rimuovere librerie esterne dal Python Package Index (PyPI).
**Lezione:** F14
**Esempio:**
```python
# Da terminale (non da Python):
# pip install numpy
# pip install pandas matplotlib
# pip list                  (mostra pacchetti installati)
# pip install --upgrade numpy
```

### Ambiente virtuale
**Definizione:** Una copia isolata dell'ambiente Python con le proprie librerie installate. Permette a progetti diversi di usare versioni diverse delle stesse librerie senza conflitti.
**Lezione:** F14
**Esempio:**
```python
# Da terminale:
# python -m venv mio_ambiente        (crea l'ambiente)
# source mio_ambiente/bin/activate   (attiva - macOS/Linux)
# mio_ambiente\Scripts\activate      (attiva - Windows)
# pip install numpy pandas           (installa nel venv)
# deactivate                         (disattiva)
```
