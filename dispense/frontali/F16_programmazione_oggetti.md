# Lezione Frontale 16 — Programmazione orientata agli oggetti

## Introduzione: il problema della crescita del codice

Nei programmi che abbiamo scritto finora, i dati e le funzioni che li manipolano vivono separati. Abbiamo dizionari che rappresentano studenti, funzioni che calcolano medie, altre funzioni che formattano output. Finché il programma è piccolo, questo approccio funziona. Ma cosa succede quando il codice cresce?

Immaginiamo di lavorare con dati su studenti universitari. Con l'approccio procedurale, potremmo avere qualcosa del genere:

```python
studente_1: dict[str, str | int | list[int]] = {
    "nome": "Anna",
    "cognome": "Rossi",
    "matricola": 12345,
    "voti": [28, 30, 25, 27]
}

def calcola_media(studente: dict[str, str | int | list[int]]) -> float:
    voti: list[int] = studente["voti"]  # type: ignore
    return sum(voti) / len(voti)

def aggiungi_voto(studente: dict[str, str | int | list[int]], voto: int) -> None:
    if not 18 <= voto <= 30:
        raise ValueError(f"Voto {voto} non valido")
    studente["voti"].append(voto)  # type: ignore

def descrizione_studente(studente: dict[str, str | int | list[int]]) -> str:
    return f"{studente['nome']} {studente['cognome']} (mat. {studente['matricola']})"
```

Questo codice presenta diversi problemi concreti:

- **Nessuna garanzia di struttura.** Nulla impedisce di creare un dizionario senza la chiave `"voti"`, e il programma si accorgerebbe dell'errore solo a runtime.
- **Le funzioni sono scollegate dai dati.** `calcola_media` potrebbe ricevere per errore un dizionario che rappresenta un libro, non uno studente. Il type checker non può aiutarci.
- **Il tipo è illeggibile.** Scrivere `dict[str, str | int | list[int]]` ovunque è faticoso e poco informativo. Non dice "questo è uno studente", dice solo "questo è un dizionario eterogeneo".
- **Mancanza di validazione centralizzata.** Se vogliamo garantire che la matricola sia sempre un numero positivo, dobbiamo ricordarci di controllare in ogni funzione che crea o modifica studenti.

La programmazione orientata agli oggetti (OOP, *Object-Oriented Programming*) risolve questi problemi unendo **stato** (i dati) e **comportamento** (le funzioni che operano su quei dati) in un'unica entità chiamata *oggetto*. L'oggetto "sa" quali dati contiene e "sa" cosa può fare con essi.

---

## 1. Già usate oggetti (senza saperlo)

Prima di imparare a creare i nostri oggetti, è importante rendersi conto che li abbiamo usati fin dalla prima lezione. In Python, **tutto è un oggetto**. Non è una metafora: è un fatto tecnico.

```python
# Le stringhe sono oggetti
nome: str = "ciao"
print(nome.upper())       # "CIAO" — upper() è un metodo dell'oggetto stringa
print(nome.replace("c", "C"))  # "Ciao"

# Le liste sono oggetti
voti: list[int] = [28, 30, 25]
voti.append(27)            # append() è un metodo dell'oggetto lista
voti.sort()                # sort() è un altro metodo

# Anche i numeri sono oggetti
n: int = 42
print(n.bit_length())     # 6 — quanti bit servono per rappresentare 42
print((3.14).is_integer()) # False
```

Quando scriviamo `nome.upper()`, stiamo chiedendo all'oggetto `nome` di eseguire il suo metodo `upper`. Il punto (`.`) è l'operatore che ci permette di accedere ai metodi e agli attributi di un oggetto. Questa è la sintassi fondamentale della programmazione a oggetti, e la usate da settimane.

Anche i tipi stessi sono oggetti:

```python
print(type(42))        # <class 'int'>
print(type("ciao"))    # <class 'str'>
print(type([1, 2, 3])) # <class 'list'>
```

La parola `class` che compare nell'output non è casuale: ci dice che `int`, `str` e `list` sono *classi*. Ogni valore concreto (42, "ciao", [1, 2, 3]) è un'*istanza* di quella classe. Vediamo cosa significano questi termini.

---

## 2. Un po' di storia

La programmazione orientata agli oggetti non è nata con Python, e non è nemmeno un'idea recente. Le sue radici risalgono agli anni Sessanta.

**Simula 67** (1967), creato dai norvegesi Ole-Johan Dahl e Kristen Nygaard, è considerato il primo linguaggio orientato agli oggetti. Fu progettato per simulare sistemi complessi (code in un ufficio postale, traffico stradale, reti di telecomunicazioni). L'idea chiave era modellare ogni entità della simulazione come un oggetto autonomo, con il proprio stato interno e il proprio comportamento. Questa intuizione — rappresentare il mondo come una collezione di oggetti che interagiscono — si rivelò potentissima ben oltre il campo delle simulazioni.

**Smalltalk** (anni Settanta), sviluppato da Alan Kay e il suo gruppo allo Xerox PARC, portò l'idea alle sue conseguenze estreme: in Smalltalk *tutto* è un oggetto, perfino i numeri, i blocchi di codice e le classi stesse. Python ha ereditato questa filosofia. Alan Kay è anche l'autore di una frase celebre:

> *"Il miglior modo di predire il futuro è inventarlo."*

Questa frase non riguarda solo la tecnologia: riguarda il modo di pensare. Invece di adattarsi agli strumenti esistenti, Kay e il suo gruppo inventarono strumenti nuovi — e con essi un modo completamente nuovo di progettare il software.

Da Simula e Smalltalk, l'OOP si è diffusa in C++ (anni Ottanta), Java (anni Novanta) e infine in Python, che la integra in modo particolarmente elegante e pragmatico.

---

## 3. Classi e istanze

Una **classe** è un modello, uno stampo, un progetto. Descrive *quali* attributi e *quali* metodi avranno gli oggetti di quel tipo, ma non contiene dati concreti.

Un'**istanza** (o oggetto) è una realizzazione concreta di quel modello. Contiene dati specifici e può eseguire i metodi definiti dalla classe.

L'analogia più immediata: la classe è il *progetto architettonico* di una casa; l'istanza è una *casa costruita* seguendo quel progetto. Da un unico progetto posso costruire cento case, ciascuna con i propri abitanti e il proprio colore delle pareti.

```python
# La classe è il progetto
class Punto:
    """Rappresenta un punto nel piano cartesiano."""

    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

# Le istanze sono i punti concreti
origine: Punto = Punto(0.0, 0.0)
p1: Punto = Punto(3.0, 4.0)
p2: Punto = Punto(-1.5, 2.7)

print(p1.x)  # 3.0 — accediamo all'attributo x dell'istanza p1
```

Ogni istanza ha i propri valori per `x` e `y`. Modificare `p1.x` non cambia `p2.x`. Le istanze sono indipendenti.

---

## 4. Un esempio completo: la classe `Studente`

Riprendiamo il problema iniziale e risolviamolo con una classe ben progettata.

```python
class Studente:
    """Rappresenta uno studente universitario con i suoi esami."""

    # Attributo di CLASSE: condiviso da tutte le istanze
    universita: str = "Università degli Studi"

    def __init__(self, nome: str, cognome: str, matricola: int) -> None:
        """Inizializza un nuovo studente con una lista di voti vuota."""
        if not nome.strip():
            raise ValueError("Il nome non può essere vuoto")
        if not cognome.strip():
            raise ValueError("Il cognome non può essere vuoto")
        if matricola <= 0:
            raise ValueError(f"Matricola non valida: {matricola}")

        # Attributi di ISTANZA: specifici di ogni singolo studente
        self.nome: str = nome.strip()
        self.cognome: str = cognome.strip()
        self.matricola: int = matricola
        self.voti: list[int] = []

    def aggiungi_voto(self, voto: int) -> None:
        """Aggiunge un voto alla carriera dello studente."""
        if not 18 <= voto <= 30:
            raise ValueError(f"Voto {voto} fuori dall'intervallo 18-30")
        self.voti.append(voto)

    def media(self) -> float:
        """Calcola la media aritmetica dei voti."""
        if not self.voti:
            raise ValueError("Nessun voto registrato")
        return sum(self.voti) / len(self.voti)

    def numero_esami(self) -> int:
        """Restituisce il numero di esami sostenuti."""
        return len(self.voti)

    def descrizione(self) -> str:
        """Restituisce una descrizione leggibile dello studente."""
        stato: str = f"media {self.media():.1f}" if self.voti else "nessun esame"
        return f"{self.nome} {self.cognome} (mat. {self.matricola}) — {stato}"
```

Usiamola:

```python
# Creazione di istanze
anna: Studente = Studente("Anna", "Rossi", 12345)
marco: Studente = Studente("Marco", "Bianchi", 67890)

# Aggiunta di voti
anna.aggiungi_voto(28)
anna.aggiungi_voto(30)
anna.aggiungi_voto(25)

marco.aggiungi_voto(24)
marco.aggiungi_voto(27)

# Uso dei metodi
print(anna.descrizione())  # Anna Rossi (mat. 12345) — media 27.7
print(marco.media())       # 25.5
print(anna.numero_esami()) # 3

# La validazione funziona
try:
    anna.aggiungi_voto(35)  # ValueError: Voto 35 fuori dall'intervallo 18-30
except ValueError as e:
    print(e)

# Anche alla creazione
try:
    errore: Studente = Studente("", "Verdi", 0)  # ValueError
except ValueError as e:
    print(e)
```

Confrontate questo codice con la versione procedurale dell'introduzione. I vantaggi sono evidenti:

- **Il tipo è chiaro.** `anna: Studente` dice esattamente cosa contiene quella variabile.
- **La validazione è centralizzata.** Avviene in `__init__` e in `aggiungi_voto`. Non è possibile creare uno studente malformato.
- **Dati e comportamento sono uniti.** `anna.media()` è più naturale di `calcola_media(anna)`.
- **Il type checker può aiutarci.** Se scriviamo `anna.media` senza parentesi, l'IDE ci avvisa.

---

## 5. `__init__` e `self`: due concetti fondamentali

### `__init__`: inizializzazione, non costruzione

Il metodo `__init__` viene chiamato automaticamente da Python subito dopo la creazione dell'oggetto. Il suo compito è *inizializzare* l'oggetto, cioè assegnare valori iniziali ai suoi attributi.

Una precisazione importante: `__init__` **non è il costruttore**. Il vero costruttore in Python è `__new__`, che crea l'oggetto in memoria. `__init__` riceve l'oggetto già creato e lo *configura*. In pratica, la distinzione raramente conta, ma è bene saperlo per non usare il termine sbagliato.

Quando scriviamo `Studente("Anna", "Rossi", 12345)`, Python esegue due passi:
1. Crea un nuovo oggetto di tipo `Studente` (tramite `__new__`).
2. Chiama `__init__` passandogli quell'oggetto come primo argomento (`self`).

### `self`: il riferimento esplicito all'istanza

In molti linguaggi (Java, C#, C++), l'istanza corrente è disponibile tramite una parola chiave implicita (`this`). Python segue una filosofia diversa, espressa dallo Zen di Python:

> *"Explicit is better than implicit."*

Per questo motivo, ogni metodo di istanza riceve come primo parametro un riferimento all'oggetto su cui viene chiamato. Per convenzione universale, questo parametro si chiama `self`. Non è una parola riservata — potremmo chiamarlo `pippo` e funzionerebbe — ma usare un nome diverso da `self` è considerato un errore di stile grave.

```python
class Esempio:
    def saluta(self) -> str:
        return f"Sono l'oggetto {id(self)}"

e: Esempio = Esempio()
print(e.saluta())  # Sono l'oggetto 140234567890

# Quando chiamiamo e.saluta(), Python traduce internamente in:
# Esempio.saluta(e)
```

L'esplicitazione di `self` ha anche un vantaggio pratico: dentro un metodo è sempre chiaro cosa è un attributo dell'oggetto (`self.nome`) e cosa è una variabile locale (`nome`).

---

## 6. Attributi di istanza vs attributi di classe

Esistono due tipi di attributi, ed è importante non confonderli.

### Attributi di istanza

Sono definiti dentro `__init__` (o in altri metodi) usando `self.nome_attributo`. Ogni istanza ha la propria copia indipendente.

```python
class Contatore:
    def __init__(self) -> None:
        self.valore: int = 0  # Attributo di istanza

    def incrementa(self) -> None:
        self.valore += 1

c1: Contatore = Contatore()
c2: Contatore = Contatore()
c1.incrementa()
c1.incrementa()

print(c1.valore)  # 2
print(c2.valore)  # 0 — c2 è indipendente da c1
```

### Attributi di classe

Sono definiti nel corpo della classe, fuori da qualsiasi metodo. Sono condivisi da tutte le istanze.

```python
class Studente:
    universita: str = "Università degli Studi"  # Attributo di classe
    _contatore: int = 0  # Quanti studenti sono stati creati

    def __init__(self, nome: str) -> None:
        self.nome: str = nome       # Attributo di istanza
        Studente._contatore += 1    # Modifichiamo l'attributo di classe
        self.numero: int = Studente._contatore

s1: Studente = Studente("Anna")
s2: Studente = Studente("Marco")

print(s1.universita)      # "Università degli Studi"
print(s2.universita)      # "Università degli Studi" — stesso valore
print(Studente.universita) # "Università degli Studi" — accessibile anche dalla classe

print(s1.numero)  # 1
print(s2.numero)  # 2
print(Studente._contatore)  # 2
```

Gli attributi di classe sono utili per valori costanti condivisi (come `universita`) o per tenere traccia di informazioni globali alla classe (come il contatore). Usateli con parsimonia: nella maggior parte dei casi, gli attributi di istanza sono la scelta giusta.

---

## 7. Metodi speciali (dunder methods)

Python utilizza un sistema elegante di **metodi speciali** per definire come gli oggetti interagiscono con il linguaggio stesso. Questi metodi hanno nomi circondati da doppi underscore (`__nome__`), per questo sono chiamati *dunder methods* (da *double underscore*).

Non vengono chiamati direttamente: Python li invoca automaticamente in risposta a operatori e funzioni built-in.

### `__str__` e `__repr__`: rappresentazione testuale

```python
class Punto:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

p: Punto = Punto(3.0, 4.0)
print(p)  # <__main__.Punto object at 0x...> — poco utile!
```

Senza `__str__`, stampare un oggetto produce un messaggio poco informativo. Definiamo le rappresentazioni:

```python
class Punto:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __str__(self) -> str:
        """Rappresentazione leggibile, per gli utenti."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Rappresentazione tecnica, per i programmatori."""
        return f"Punto(x={self.x}, y={self.y})"

p: Punto = Punto(3.0, 4.0)
print(p)       # (3.0, 4.0) — usa __str__
print(repr(p)) # Punto(x=3.0, y=4.0) — usa __repr__
print([p])     # [Punto(x=3.0, y=4.0)] — nelle collezioni Python usa __repr__
```

La regola pratica: `__str__` deve essere leggibile per un essere umano; `__repr__` deve essere una stringa da cui, idealmente, si possa ricostruire l'oggetto. Se definite un solo metodo, definite `__repr__`: Python lo usa come fallback per `__str__`.

### `__len__`: lunghezza

```python
class Classe:
    """Rappresenta una classe scolastica con i suoi studenti."""

    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.studenti: list[str] = []

    def aggiungi(self, studente: str) -> None:
        self.studenti.append(studente)

    def __len__(self) -> int:
        return len(self.studenti)

prima_a: Classe = Classe("1A")
prima_a.aggiungi("Anna")
prima_a.aggiungi("Marco")
prima_a.aggiungi("Luca")

print(len(prima_a))  # 3 — funziona grazie a __len__
```

### `__eq__` e `__lt__`: confronti

Per default, due oggetti sono uguali solo se sono lo *stesso* oggetto in memoria. Spesso vogliamo un comportamento diverso:

```python
class Punto:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __eq__(self, altro: object) -> bool:
        if not isinstance(altro, Punto):
            return NotImplemented
        return self.x == altro.x and self.y == altro.y

    def __lt__(self, altro: "Punto") -> bool:
        """Ordina per distanza dall'origine."""
        return (self.x ** 2 + self.y ** 2) < (altro.x ** 2 + altro.y ** 2)

    def __repr__(self) -> str:
        return f"Punto({self.x}, {self.y})"

p1: Punto = Punto(3.0, 4.0)
p2: Punto = Punto(3.0, 4.0)
p3: Punto = Punto(1.0, 1.0)

print(p1 == p2)  # True — stesse coordinate
print(p1 is p2)  # False — oggetti diversi in memoria

# Con __lt__ definito, possiamo anche ordinare
punti: list[Punto] = [p1, p3]
punti.sort()
print(punti)  # [Punto(1.0, 1.0), Punto(3.0, 4.0)]
```

Notate il pattern in `__eq__`: controlliamo che `altro` sia effettivamente un `Punto` con `isinstance`, e restituiamo `NotImplemented` (non `NotImplementedError`) se non lo è. Questo permette a Python di provare il confronto nell'altro senso.

### `__getitem__`: accesso con indice

```python
class SerieStorica:
    """Una serie di valori indicizzati nel tempo."""

    def __init__(self, valori: list[float]) -> None:
        self.valori: list[float] = valori

    def __getitem__(self, indice: int) -> float:
        return self.valori[indice]

    def __len__(self) -> int:
        return len(self.valori)

serie: SerieStorica = SerieStorica([100.0, 102.5, 98.3, 105.1])
print(serie[0])   # 100.0 — usa __getitem__
print(serie[-1])  # 105.1
print(len(serie)) # 4
```

### Riepilogo dei metodi speciali più comuni

| Metodo | Invocato da | Scopo |
|--------|-------------|-------|
| `__init__` | `Classe(...)` | Inizializzazione |
| `__str__` | `str(obj)`, `print(obj)` | Rappresentazione leggibile |
| `__repr__` | `repr(obj)`, nel REPL | Rappresentazione tecnica |
| `__len__` | `len(obj)` | Lunghezza |
| `__eq__` | `obj1 == obj2` | Uguaglianza |
| `__lt__` | `obj1 < obj2`, `sorted()` | Confronto "minore di" |
| `__getitem__` | `obj[i]` | Accesso per indice |
| `__contains__` | `x in obj` | Appartenenza |
| `__add__` | `obj1 + obj2` | Somma |
| `__bool__` | `if obj:` | Valore di verità |

Questa è una delle caratteristiche più potenti di Python: definendo pochi metodi speciali, i nostri oggetti si integrano perfettamente con la sintassi del linguaggio. `len()`, `print()`, `sorted()`, gli operatori `==`, `<`, `+`, l'accesso con `[]` — funzionano tutti con oggetti personalizzati, esattamente come con i tipi built-in.

---

## 8. Ereditarietà

L'**ereditarietà** permette di creare una nuova classe basata su una classe esistente. La nuova classe (chiamata *sottoclasse* o *classe figlia*) eredita tutti gli attributi e i metodi della classe originale (la *superclasse* o *classe madre*), e può aggiungerne di nuovi o modificare quelli ereditati.

### La relazione "è un"

L'ereditarietà modella la relazione **"è un"** (*is-a*). Uno `StudenteLavoratore` *è uno* `Studente`, con qualche caratteristica in più. Un `Cerchio` *è una* `Forma`. Un `Gatto` *è un* `Animale`.

```python
class Studente:
    """Studente universitario."""

    def __init__(self, nome: str, cognome: str, matricola: int) -> None:
        self.nome: str = nome
        self.cognome: str = cognome
        self.matricola: int = matricola
        self.voti: list[int] = []

    def aggiungi_voto(self, voto: int) -> None:
        if not 18 <= voto <= 30:
            raise ValueError(f"Voto {voto} fuori dall'intervallo 18-30")
        self.voti.append(voto)

    def media(self) -> float:
        if not self.voti:
            raise ValueError("Nessun voto registrato")
        return sum(self.voti) / len(self.voti)

    def __str__(self) -> str:
        return f"{self.nome} {self.cognome} (mat. {self.matricola})"

    def __repr__(self) -> str:
        return f"Studente({self.nome!r}, {self.cognome!r}, {self.matricola})"


class StudenteLavoratore(Studente):
    """Studente che lavora part-time. È uno Studente con attributi aggiuntivi."""

    def __init__(self, nome: str, cognome: str, matricola: int,
                 azienda: str, ore_settimanali: int) -> None:
        # super() chiama il __init__ della classe madre
        super().__init__(nome, cognome, matricola)
        self.azienda: str = azienda
        self.ore_settimanali: int = ore_settimanali

    def è_part_time(self) -> bool:
        """Un lavoratore è part-time se lavora meno di 20 ore a settimana."""
        return self.ore_settimanali < 20

    def __str__(self) -> str:
        base: str = super().__str__()
        return f"{base} — lavora presso {self.azienda} ({self.ore_settimanali}h/sett.)"

    def __repr__(self) -> str:
        return (f"StudenteLavoratore({self.nome!r}, {self.cognome!r}, "
                f"{self.matricola}, {self.azienda!r}, {self.ore_settimanali})")
```

Usiamo la sottoclasse:

```python
sl: StudenteLavoratore = StudenteLavoratore(
    "Giulia", "Verdi", 11111, "DataCorp", 16
)

# Metodi ereditati da Studente
sl.aggiungi_voto(28)
sl.aggiungi_voto(30)
print(sl.media())       # 29.0

# Metodi propri di StudenteLavoratore
print(sl.è_part_time()) # True

# __str__ ridefinito
print(sl)  # Giulia Verdi (mat. 11111) — lavora presso DataCorp (16h/sett.)

# isinstance funziona con l'ereditarietà
print(isinstance(sl, StudenteLavoratore))  # True
print(isinstance(sl, Studente))            # True — è anche uno Studente
```

### `super()`: chiamare la classe madre

La funzione `super()` restituisce un riferimento alla superclasse. Si usa tipicamente in `__init__` per non duplicare il codice di inizializzazione, e nei metodi ridefiniti per estendere (anziché sostituire) il comportamento originale.

### "È un" vs "ha un": preferire la composizione

Non tutte le relazioni tra classi sono relazioni "è un". Spesso la relazione corretta è **"ha un"** (*has-a*), e in quel caso si usa la **composizione**: un oggetto contiene un altro oggetto come attributo.

```python
# SBAGLIATO: un Dipartimento NON è una lista di docenti
class Dipartimento(list):  # Non fate questo!
    pass

# CORRETTO: un Dipartimento HA una lista di docenti
class Docente:
    def __init__(self, nome: str, settore: str) -> None:
        self.nome: str = nome
        self.settore: str = settore

    def __repr__(self) -> str:
        return f"Docente({self.nome!r}, {self.settore!r})"

class Dipartimento:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.docenti: list[Docente] = []  # Composizione: HA dei docenti

    def aggiungi_docente(self, docente: Docente) -> None:
        self.docenti.append(docente)

    def __len__(self) -> int:
        return len(self.docenti)
```

Una regola pratica molto citata nel mondo della programmazione:

> *Preferire la composizione all'ereditarietà.*

L'ereditarietà crea un accoppiamento forte tra le classi: ogni modifica alla classe madre si ripercuote su tutte le figlie. La composizione è più flessibile. Usate l'ereditarietà quando la relazione "è un" è genuina e stabile; usate la composizione in tutti gli altri casi.

---

## 9. Incapsulamento e `@property`

### La convenzione dell'underscore

In Python non esistono veri attributi "privati" come in Java o C++. La protezione si basa su una **convenzione**: un attributo il cui nome inizia con un singolo underscore (`_`) è considerato *interno*, cioè non destinato all'uso esterno. Non è un divieto tecnico — è un accordo tra programmatori.

```python
class ContoBancario:
    def __init__(self, titolare: str, saldo_iniziale: float = 0.0) -> None:
        self.titolare: str = titolare
        self._saldo: float = saldo_iniziale  # Convenzione: uso interno

    def deposita(self, importo: float) -> None:
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        self._saldo += importo

    def preleva(self, importo: float) -> None:
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        if importo > self._saldo:
            raise ValueError("Saldo insufficiente")
        self._saldo -= importo

    def get_saldo(self) -> float:
        return self._saldo
```

L'underscore dice: "non accedere direttamente a `_saldo` da fuori la classe; usa i metodi `deposita`, `preleva` e `get_saldo`". Chi lo fa comunque non riceve un errore tecnico, ma viola il contratto implicito e rischia che il codice si rompa in futuro.

### Il decoratore `@property`

Python offre un modo più elegante per controllare l'accesso agli attributi: il decoratore `@property`. Permette di definire metodi che si usano *come se fossero attributi*.

```python
class ContoBancario:
    def __init__(self, titolare: str, saldo_iniziale: float = 0.0) -> None:
        self.titolare: str = titolare
        self._saldo: float = saldo_iniziale

    @property
    def saldo(self) -> float:
        """Il saldo corrente (sola lettura)."""
        return self._saldo

    def deposita(self, importo: float) -> None:
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        self._saldo += importo

    def preleva(self, importo: float) -> None:
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        if importo > self._saldo:
            raise ValueError("Saldo insufficiente")
        self._saldo -= importo

conto: ContoBancario = ContoBancario("Anna Rossi", 1000.0)
print(conto.saldo)   # 1000.0 — sembra un attributo, ma è un metodo
conto.deposita(500)
print(conto.saldo)   # 1500.0

# Tentare di assegnare direttamente produce un errore
# conto.saldo = 9999  # AttributeError: property 'saldo' has no setter
```

Il vantaggio di `@property` è che il codice esterno non deve cambiare se in futuro decidiamo di aggiungere logica all'accesso (ad esempio, arrotondare il saldo, registrare ogni lettura in un log, o convertire la valuta). L'interfaccia resta `conto.saldo`.

---

## 10. Collegamento con il mondo dei dati

Se studiate Scienze Statistiche, vi chiederete: "a cosa mi serve tutto questo nella pratica?" La risposta è: lo state già usando.

### pandas DataFrame

Un `DataFrame` di pandas è un oggetto. Quando scrivete:

```python
import pandas as pd

df: pd.DataFrame = pd.DataFrame({"età": [22, 25, 21], "voto": [28, 30, 25]})
print(df.shape)       # (3, 2) — attributo
print(df.describe())  # metodo
print(df["età"])       # __getitem__
print(len(df))         # __len__
```

State usando esattamente i concetti di questa lezione: attributi (`shape`), metodi (`describe()`), metodi speciali (`__getitem__` per l'accesso con `[]`, `__len__` per `len()`).

### Modelli scikit-learn

Anche i modelli di machine learning sono oggetti con un'interfaccia comune:

```python
from sklearn.linear_model import LinearRegression
import numpy as np

modello: LinearRegression = LinearRegression()  # Istanza
X: np.ndarray = np.array([[1], [2], [3], [4]])
y: np.ndarray = np.array([2.1, 3.9, 6.2, 7.8])

modello.fit(X, y)                    # Metodo: addestra il modello
previsioni: np.ndarray = modello.predict(X)  # Metodo: genera previsioni
print(modello.coef_)                 # Attributo: coefficienti stimati
print(modello.intercept_)            # Attributo: intercetta
```

La bellezza di questo design è la **consistenza**: tutti i modelli di scikit-learn (regressione lineare, alberi decisionali, reti neurali) seguono la stessa interfaccia `.fit()` / `.predict()`. Questo è possibile proprio grazie alla programmazione a oggetti e all'ereditarietà: tutti i modelli ereditano da classi base comuni.

---

## Domande di verifica

1. Qual è la differenza tra una classe e un'istanza? Fate un'analogia con un esempio della vita quotidiana diverso da quelli visti a lezione.

2. Perché `__init__` si chiama "inizializzatore" e non "costruttore"? Cosa succede prima che `__init__` venga eseguito?

3. Spiegate il ruolo di `self` nei metodi di istanza. Perché Python richiede che sia esplicito, a differenza di altri linguaggi?

4. Qual è la differenza tra un attributo di istanza e un attributo di classe? In quale situazione usereste un attributo di classe?

5. Spiegate la differenza tra `__str__` e `__repr__`. Se poteste definire un solo metodo tra i due, quale scegliereste e perché?

6. Cosa significa la regola "preferire la composizione all'ereditarietà"? Fate un esempio di una relazione tra classi che dovrebbe usare la composizione e non l'ereditarietà.

7. Perché in Python gli attributi "privati" usano una semplice convenzione (l'underscore) invece di un meccanismo di protezione reale? Quale principio dello Zen di Python giustifica questa scelta?

8. Quando scriviamo `len(df)` su un DataFrame di pandas, quale metodo speciale viene invocato? E quando scriviamo `df["colonna"]`?

---

## Esercizi

### Base

**Esercizio 1 — Rettangolo**

Scrivete una classe `Rettangolo` con attributi `larghezza: float` e `altezza: float` (entrambi devono essere positivi, altrimenti `ValueError`). Implementate i metodi `area() -> float`, `perimetro() -> float` e `__str__` (che deve restituire qualcosa come `"Rettangolo 5.0 × 3.0"`). Usate sempre i type hints.

**Esercizio 2 — Contatore con limiti**

Scrivete una classe `Contatore` con un attributo `_valore: int` inizializzato a zero e un attributo `massimo: int` passato al costruttore. Implementate i metodi `incrementa() -> None` (che alza un `ValueError` se il contatore ha raggiunto il massimo), `reset() -> None` (che riporta il valore a zero) e una `@property` chiamata `valore` che restituisce il valore corrente in sola lettura. Implementate anche `__str__` e `__repr__`.

**Esercizio 3 — Dado**

Scrivete una classe `Dado` con un attributo `facce: int` (default 6). Implementate un metodo `lancia() -> int` che restituisce un valore casuale tra 1 e `facce` (usate `random.randint`). Aggiungete un attributo `_storico: list[int]` che tiene traccia di tutti i lanci e un metodo `media_lanci() -> float` che restituisce la media dei lanci effettuati.

### Intermedio

**Esercizio 4 — Registro esami**

Scrivete una classe `Esame` con attributi `materia: str`, `voto: int` e `data: str`. Poi scrivete una classe `RegistroEsami` che contiene una lista di esami e implementa:
- `aggiungi(esame: Esame) -> None` con validazione del voto.
- `media() -> float` che calcola la media dei voti.
- `__len__` che restituisce il numero di esami.
- `__getitem__` che permette di accedere agli esami per indice.
- `migliore() -> Esame` che restituisce l'esame con il voto più alto. Implementate `__lt__` su `Esame` per poter usare `max()`.

**Esercizio 5 — Statistiche descrittive**

Scrivete una classe `CampioneStatistico` che riceve una lista di `float` nel costruttore (deve contenere almeno un elemento). Implementate come `@property`: `media`, `varianza` (della popolazione), `deviazione_standard`. Implementate `__len__`, `__getitem__`, `__str__` (che stampa `"Campione(n=10, media=5.32, std=1.41)"`) e `__eq__` (due campioni sono uguali se contengono gli stessi valori nello stesso ordine).

### Avanzato

**Esercizio 6 — Matrice semplice**

Scrivete una classe `Matrice` che rappresenta una matrice di numeri reali. Il costruttore riceve una lista di liste di `float` e verifica che tutte le righe abbiano la stessa lunghezza. Implementate:
- `righe` e `colonne` come `@property`.
- `__getitem__` che accetta una tupla `(riga, colonna)` e restituisce l'elemento.
- `__add__` per la somma tra matrici (stesse dimensioni, altrimenti `ValueError`).
- `__str__` per una rappresentazione leggibile.
- Un metodo `trasposta() -> "Matrice"` che restituisce una nuova matrice trasposta.

**Esercizio 7 — Gerarchia di forme**

Create una classe base `Forma` con un metodo astratto (basta alzare `NotImplementedError`) `area() -> float` e un metodo `descrizione() -> str` che restituisce `"Forma con area X.XX"`. Derivate le classi `Cerchio` (attributo `raggio`), `Rettangolo` (attributi `larghezza` e `altezza`) e `Quadrato` che eredita da `Rettangolo` (un quadrato *è un* rettangolo con lato uguale). Ogni sottoclasse implementa `area()` e `__repr__`. Scrivete una funzione `area_totale(forme: list[Forma]) -> float` che somma le aree di una lista di forme qualsiasi.

---

## Osservazioni finali

La programmazione orientata agli oggetti è, prima di tutto, uno strumento per *organizzare il pensiero*. Quando rappresentiamo un concetto come una classe, siamo costretti a rispondere a domande precise: quali dati lo definiscono? Quali operazioni ha senso compiere su di esso? Quali garanzie devono valere sempre? Queste domande rendono il codice più chiaro, più robusto e più facile da estendere.

Non tutto deve essere una classe. Python è un linguaggio *multi-paradigma*: potete mescolare funzioni, classi e moduli a seconda di ciò che serve. Una regola semplice: se avete dati e comportamento che vanno insieme, una classe è probabilmente la scelta giusta; se avete una funzione che non ha bisogno di stato, lasciatela come funzione.

I concetti fondamentali da portare con sé:

1. **Classe = modello, istanza = oggetto concreto.** La classe definisce la struttura; le istanze contengono i dati.
2. **`self` è esplicito.** Ogni metodo riceve il riferimento all'istanza come primo argomento.
3. **I metodi speciali integrano i vostri oggetti nel linguaggio.** Definite `__str__`, `__repr__`, `__len__`, `__eq__` per rendere i vostri oggetti cittadini di prima classe in Python.
4. **Preferite la composizione all'ereditarietà.** Usate l'ereditarietà per le vere relazioni "è un"; usate la composizione per le relazioni "ha un".
5. **Tutto in Python è un oggetto.** Le stringhe, le liste, i DataFrame, i modelli di machine learning — tutto segue gli stessi principi che avete imparato oggi.

Nelle prossime lezioni vedremo come questi concetti si applicano nella pratica dell'analisi dei dati, dove librerie come pandas e scikit-learn sfruttano intensamente la programmazione a oggetti per offrire interfacce potenti e coerenti.
