# Lezione Frontale 13 — Funzioni: fondamenti

## Introduzione

Finora avete scritto programmi che scorrono dall'alto verso il basso, con variabili, condizioni e cicli. Ma man mano che i problemi crescono in complessità, il codice scritto in un unico blocco diventa difficile da leggere, da correggere e da riutilizzare. Se dovete calcolare la media in dieci punti diversi del programma, copiate e incollate lo stesso codice dieci volte? E quando scoprite un errore nella formula, lo correggete in tutti e dieci i posti?

Le **funzioni** risolvono esattamente questo problema. Una funzione è un blocco di codice a cui date un nome, che potete richiamare ogni volta che ne avete bisogno. Scrivete la logica una volta sola, la testate una volta sola, e poi la usate ovunque.

---

## Perche le funzioni: riuso, astrazione, decomposizione

Le funzioni servono per tre motivi fondamentali.

### Riuso del codice

Il motivo piu immediato: evitare la duplicazione. Se la stessa operazione serve in piu punti del programma, la si scrive una volta come funzione e la si chiama dove serve. Quando si scopre un bug, si corregge in un solo posto.

### Astrazione

Una funzione nasconde i dettagli implementativi dietro un nome significativo. Quando leggete `calcola_media(voti)`, capite immediatamente *cosa* fa il codice, senza dovervi preoccupare del *come*. Questo e il principio di **astrazione**: separare il "cosa" dal "come". In statistica lavorerete con funzioni come `media()`, `varianza()`, `regressione()`: vi basta sapere cosa calcolano, non come lo fanno internamente.

### Decomposizione

Un problema complesso si risolve spezzandolo in sotto-problemi piu piccoli e gestibili. Ogni sotto-problema diventa una funzione. Questa strategia si chiama **decomposizione funzionale** ed e una delle tecniche piu potenti della programmazione.

Immaginate di dover analizzare un dataset:

1. Leggere i dati dal file
2. Pulire i dati (rimuovere valori mancanti)
3. Calcolare le statistiche descrittive
4. Generare un report

Ognuno di questi passi diventa una funzione separata. Il programma principale diventa una sequenza leggibile di chiamate a funzione.

### Breve storia delle subroutine

L'idea di "sotto-programma riutilizzabile" e antica quasi quanto la programmazione stessa. Gia negli anni '40, i pionieri dell'informatica si accorsero che certi blocchi di istruzioni venivano ripetuti in programmi diversi. Grace Hopper, matematica e informatica americana, fu tra i primi a promuovere l'idea di librerie di subroutine riutilizzabili: pezzi di codice gia scritti e testati che i programmatori potevano incorporare nei propri programmi.

Negli anni '60, con la "crisi del software" — progetti che sforavano tempi e costi — Edsger Dijkstra e altri teorici promossero la **programmazione strutturata**, in cui le funzioni sono il mattone fondamentale per organizzare il codice. Da allora, ogni linguaggio di programmazione ha messo le funzioni al centro della propria struttura.

---

## Definire una funzione con type hints

In Python una funzione si definisce con la parola chiave `def`:

```python
def calcola_media(valori: list[float]) -> float:
    """Calcola la media aritmetica di una lista di numeri."""
    somma: float = sum(valori)
    n: int = len(valori)
    return somma / n
```

Questa funzione:
- si chiama `calcola_media`
- accetta un parametro `valori` di tipo `list[float]`
- restituisce un `float`
- ha una **docstring** che ne descrive lo scopo
- usa `return` per restituire il risultato

Per chiamarla:

```python
voti: list[float] = [28.0, 30.0, 25.0, 27.0, 22.0]
media: float = calcola_media(voti)
print(f"Media: {media}")  # Media: 26.4
```

---

## Anatomia di una funzione

Ogni funzione Python e composta da parti ben definite. Analizziamole una per una:

```python
def nome_funzione(param1: tipo1, param2: tipo2) -> tipo_ritorno:
    """Docstring: descrizione della funzione."""
    # Corpo della funzione
    risultato = ...
    return risultato
```

### `def`

La parola chiave `def` (abbreviazione di *define*) introduce la definizione di una funzione. In Python, `def` e un'istruzione eseguibile: quando l'interprete la incontra, crea un oggetto funzione e lo associa al nome indicato. Questo significa che una funzione deve essere definita *prima* di essere chiamata.

### Nome

Il nome segue le stesse regole delle variabili: lettere minuscole, parole separate da underscore (`snake_case`). Scegliete nomi che descrivano *cosa fa* la funzione, tipicamente con un verbo: `calcola_media`, `leggi_file`, `filtra_outlier`, `conta_valori_mancanti`.

### Parametri tipizzati

Tra le parentesi tonde si elencano i **parametri**: variabili locali che riceveranno i valori passati alla chiamata. Ogni parametro ha un **type hint** che indica il tipo atteso:

```python
def calcola_bmi(peso_kg: float, altezza_m: float) -> float:
    """Calcola l'indice di massa corporea."""
    return peso_kg / (altezza_m ** 2)
```

I type hints non bloccano l'esecuzione se il tipo e sbagliato (Python non li controlla a runtime), ma sono preziosi per tre motivi:
1. **Documentazione**: chi legge la funzione capisce subito cosa passare
2. **Errori precoci**: strumenti come `mypy` verificano i tipi *prima* dell'esecuzione
3. **Autocompletamento**: gli editor suggeriscono metodi e attributi corretti

### `-> tipo_ritorno`

La freccia `->` seguita dal tipo indica cosa restituisce la funzione. Se la funzione non restituisce nulla di significativo, si annota con `-> None`.

```python
def stampa_report(titolo: str, dati: list[float]) -> None:
    """Stampa un report formattato a schermo."""
    print(f"=== {titolo} ===")
    for valore in dati:
        print(f"  {valore:.2f}")
```

### Docstring

La stringa immediatamente dopo la riga `def` e la **docstring** (*documentation string*). Approfondiremo le docstring in una sezione dedicata piu avanti.

### Corpo

Il blocco indentato dopo la riga `def` e il corpo della funzione. Contiene le istruzioni che vengono eseguite ogni volta che la funzione viene chiamata. Puo contenere qualsiasi codice Python: variabili locali, condizioni, cicli, chiamate ad altre funzioni.

### `return`

L'istruzione `return` restituisce un valore al chiamante e termina immediatamente l'esecuzione della funzione. Ne parliamo in dettaglio nella prossima sezione.

---

## Parametro vs argomento

Questi due termini vengono spesso confusi, ma hanno significati distinti:

- **Parametro**: la variabile nella *definizione* della funzione. E un "segnaposto" che aspetta un valore.
- **Argomento**: il valore concreto passato nella *chiamata* della funzione.

```python
# "nome" e "eta" sono PARAMETRI (definizione)
def saluta(nome: str, eta: int) -> str:
    return f"Ciao {nome}, hai {eta} anni!"

# "Anna" e 21 sono ARGOMENTI (chiamata)
messaggio: str = saluta("Anna", 21)
```

Un'analogia: i parametri sono come i campi vuoti di un modulo da compilare (Nome: ___, Eta: ___). Gli argomenti sono i valori che scrivete nei campi quando compilate il modulo.

---

## L'istruzione `return`

`return` svolge due compiti contemporaneamente:

1. **Restituisce un valore** al codice che ha chiamato la funzione
2. **Termina** immediatamente l'esecuzione della funzione

### Return semplice

```python
def quadrato(n: float) -> float:
    return n ** 2

risultato: float = quadrato(5.0)  # risultato = 25.0
```

### Return multipli: terminazione anticipata

Siccome `return` termina la funzione, puo essere usato per uscire in anticipo:

```python
def calcola_media_sicura(valori: list[float]) -> float:
    """Calcola la media, restituendo 0.0 se la lista e vuota."""
    if len(valori) == 0:
        return 0.0  # esce subito, il codice sotto non viene eseguito
    return sum(valori) / len(valori)
```

### Senza `return`: il valore `None`

Se una funzione termina senza incontrare un'istruzione `return` (oppure esegue un `return` senza valore), restituisce automaticamente `None`:

```python
def saluta(nome: str) -> None:
    print(f"Ciao, {nome}!")
    # nessun return esplicito → restituisce None

risultato = saluta("Marco")
print(risultato)  # None
```

`None` e un valore speciale di Python che rappresenta "nessun valore". E l'equivalente di un foglio bianco: non e zero, non e la stringa vuota, e proprio l'assenza di valore.

### Restituire piu valori con le tuple

Python permette di restituire piu valori contemporaneamente impacchettandoli in una **tupla**:

```python
def statistiche_base(valori: list[float]) -> tuple[float, float, float]:
    """Restituisce media, minimo e massimo."""
    media: float = sum(valori) / len(valori)
    minimo: float = min(valori)
    massimo: float = max(valori)
    return media, minimo, massimo  # restituisce una tupla
```

Al momento della chiamata, potete "spacchettare" i valori in variabili separate:

```python
dati: list[float] = [12.5, 18.3, 9.1, 22.0, 15.7]
m, lo, hi = statistiche_base(dati)
print(f"Media: {m:.1f}, Min: {lo:.1f}, Max: {hi:.1f}")
# Media: 15.5, Min: 9.1, Max: 22.0
```

Questo e estremamente comodo per le funzioni statistiche, dove spesso si vogliono calcolare piu indicatori in un unico passaggio sui dati.

---

## Docstring: documentare le funzioni

Una **docstring** e una stringa posta come prima istruzione di una funzione, che ne documenta lo scopo, i parametri e il valore di ritorno. Python la rende accessibile tramite l'attributo `__doc__` e la funzione built-in `help()`.

### Formato consigliato

Esistono diversi stili di docstring. Per questo corso, adottiamo il formato "Google style", chiaro e leggibile:

```python
def deviazione_standard(valori: list[float], campione: bool = True) -> float:
    """Calcola la deviazione standard di una lista di valori.

    Implementa la formula della deviazione standard, utilizzando
    n-1 al denominatore per la versione campionaria (default)
    oppure n per la versione della popolazione.

    Args:
        valori: lista di valori numerici (almeno 2 elementi).
        campione: se True usa n-1 (Bessel), se False usa n.

    Returns:
        La deviazione standard come float.

    Raises:
        ValueError: se la lista contiene meno di 2 elementi.
    """
    n: int = len(valori)
    if n < 2:
        raise ValueError("Servono almeno 2 valori")
    media: float = sum(valori) / n
    scarti_quadratici: list[float] = [(x - media) ** 2 for x in valori]
    divisore: int = n - 1 if campione else n
    return (sum(scarti_quadratici) / divisore) ** 0.5
```

Le quattro sezioni della docstring sono:

1. **Descrizione breve** (prima riga): una frase che dice *cosa fa* la funzione
2. **Descrizione estesa** (opzionale): dettagli, algoritmo, formule, note
3. **Args**: un parametro per riga, con descrizione
4. **Returns**: cosa viene restituito
5. **Raises**: quali eccezioni puo sollevare e quando

### Usare `help()`

La funzione built-in `help()` mostra la docstring in modo formattato:

```python
help(deviazione_standard)
```

Output:
```
Help on function deviazione_standard in module __main__:

deviazione_standard(valori: list[float], campione: bool = True) -> float
    Calcola la deviazione standard di una lista di valori.

    Implementa la formula della deviazione standard, utilizzando
    n-1 al denominatore per la versione campionaria (default)
    oppure n per la versione della popolazione.
    ...
```

Scrivere docstring e un investimento: chi usera la vostra funzione (incluso il "voi del futuro") vi ringraziera.

---

## Parametri: posizionali, con default e keyword

Python offre diversi modi per passare argomenti a una funzione.

### Parametri posizionali

L'ordine degli argomenti corrisponde all'ordine dei parametri nella definizione:

```python
def intervallo_confidenza(media: float, errore: float) -> tuple[float, float]:
    """Calcola estremi dell'intervallo di confidenza."""
    return media - errore, media + errore

# Gli argomenti sono associati per POSIZIONE
limiti: tuple[float, float] = intervallo_confidenza(25.3, 1.2)
# media=25.3, errore=1.2
```

### Parametri con valore di default

Un parametro puo avere un valore predefinito, che viene usato se il chiamante non fornisce un argomento:

```python
def formatta_numero(valore: float, decimali: int = 2, prefisso: str = "") -> str:
    """Formatta un numero con il numero di decimali specificato."""
    return f"{prefisso}{valore:.{decimali}f}"

# Usa tutti i default
print(formatta_numero(3.14159))          # "3.14"

# Sovrascrive il primo default
print(formatta_numero(3.14159, 4))       # "3.1416"

# Sovrascrive entrambi i default
print(formatta_numero(3.14159, 3, "€"))  # "€3.142"
```

**Regola importante:** i parametri con default devono venire *dopo* quelli senza default. Questo non e valido:

```python
# ERRORE: parametro senza default dopo uno con default
def sbagliata(a: int = 0, b: int) -> int:  # SyntaxError!
    return a + b
```

### Argomenti keyword

Potete specificare gli argomenti per *nome*, indipendentemente dall'ordine:

```python
# Argomenti keyword: l'ordine non conta
print(formatta_numero(valore=3.14159, prefisso="€", decimali=3))  # "€3.142"

# Misto: posizionali prima, keyword dopo
print(formatta_numero(3.14159, prefisso="$"))  # "$3.14"
```

Gli argomenti keyword rendono le chiamate piu leggibili, specialmente quando ci sono molti parametri o parametri booleani:

```python
# Poco chiaro: cosa significa True?
risultato: float = deviazione_standard(dati, True)

# Chiaro: si capisce il significato
risultato: float = deviazione_standard(dati, campione=True)
```

### Cenni su `*args` e `**kwargs`

Python permette di definire funzioni che accettano un numero variabile di argomenti. Non li userete spesso in questo corso, ma e bene sapere che esistono:

```python
def somma_tutti(*args: float) -> float:
    """Somma un numero qualsiasi di valori."""
    totale: float = 0.0
    for valore in args:
        totale += valore
    return totale

print(somma_tutti(1.0, 2.0, 3.0))       # 6.0
print(somma_tutti(10.0, 20.0))           # 30.0
print(somma_tutti(5.0))                  # 5.0
```

`*args` raccoglie tutti gli argomenti posizionali "in piu" in una tupla. Analogamente, `**kwargs` raccoglie argomenti keyword aggiuntivi in un dizionario:

```python
def stampa_info(nome: str, **kwargs: str) -> None:
    """Stampa informazioni su uno studente."""
    print(f"Nome: {nome}")
    for chiave, valore in kwargs.items():
        print(f"  {chiave}: {valore}")

stampa_info("Anna", corso="Statistica", anno="primo")
# Nome: Anna
#   corso: Statistica
#   anno: primo
```

Troverete `*args` e `**kwargs` usati internamente in molte librerie Python. Per ora, concentratevi sui parametri posizionali, con default e keyword.

---

## Il pericolo del default mutabile

Questa sezione descrive uno dei bug piu insidiosi di Python, che ha colto di sorpresa generazioni di programmatori. Leggetela con attenzione.

### Il problema

Osservate questa funzione, apparentemente innocua:

```python
def aggiungi_voto(voto: int, lista: list[int] = []) -> list[int]:
    """Aggiunge un voto alla lista e la restituisce."""
    lista.append(voto)
    return lista
```

Sembra ragionevole: se non si passa una lista, ne crea una vuota. Ma guardate cosa succede:

```python
print(aggiungi_voto(28))  # [28]        — fin qui tutto bene
print(aggiungi_voto(30))  # [28, 30]    — aspettavamo [30]!
print(aggiungi_voto(25))  # [28, 30, 25] — la lista "vuota" non è vuota!
```

Ogni chiamata modifica la *stessa* lista! Il valore di default `[]` viene creato **una sola volta**, nel momento in cui Python esegue la riga `def`. Da quel momento, tutte le chiamate che non forniscono una lista condividono lo stesso oggetto.

### Perche succede

Quando Python incontra `def aggiungi_voto(voto: int, lista: list[int] = [])`, valuta l'espressione `[]` e crea un oggetto lista vuota. Questo oggetto viene conservato come attributo della funzione stessa (in `aggiungi_voto.__defaults__`). Ad ogni chiamata senza argomento `lista`, il parametro punta a *quello stesso oggetto*, che nel frattempo e stato modificato dalle chiamate precedenti.

Potete verificare:

```python
print(aggiungi_voto.__defaults__)
# ([28, 30, 25],)  — il default NON è più una lista vuota!
```

### La soluzione: usare `None` come default

Il pattern corretto e usare `None` come valore di default e creare una nuova lista all'interno della funzione:

```python
def aggiungi_voto(voto: int, lista: list[int] | None = None) -> list[int]:
    """Aggiunge un voto alla lista e la restituisce."""
    if lista is None:
        lista = []  # nuova lista ad ogni chiamata
    lista.append(voto)
    return lista
```

Ora ogni chiamata senza argomento `lista` crea una lista vuota *fresca*:

```python
print(aggiungi_voto(28))  # [28]
print(aggiungi_voto(30))  # [30]  — corretto!
print(aggiungi_voto(25))  # [25]  — corretto!
```

### La regola d'oro

> **Non usate mai un oggetto mutabile (lista, dizionario, set) come valore di default di un parametro.** Usate `None` e create l'oggetto dentro la funzione.

Questo vale per `list`, `dict`, `set` e qualsiasi altro oggetto modificabile. I tipi immutabili (`int`, `float`, `str`, `bool`, `tuple`, `None`) sono sicuri come default perche non possono essere modificati.

---

## Scope e namespace

Quando definite una variabile, dove e accessibile? La risposta dipende dallo **scope** (ambito di visibilita) e dal **namespace** (spazio dei nomi) in cui si trova.

### Scope locale

Le variabili create dentro una funzione esistono solo dentro quella funzione:

```python
def calcola_area(base: float, altezza: float) -> float:
    area: float = base * altezza  # variabile LOCALE
    return area

risultato: float = calcola_area(5.0, 3.0)
print(risultato)  # 15.0
print(area)       # NameError: name 'area' is not defined
```

La variabile `area` nasce quando la funzione viene chiamata e muore quando la funzione termina. Questo e il **scope locale**: le variabili locali sono invisibili dall'esterno.

Questo e un vantaggio, non un limite. Significa che potete usare gli stessi nomi di variabile in funzioni diverse senza conflitti:

```python
def media(valori: list[float]) -> float:
    n: int = len(valori)  # questa n è locale a media()
    return sum(valori) / n

def varianza(valori: list[float]) -> float:
    n: int = len(valori)  # questa è un'ALTRA n, locale a varianza()
    m: float = media(valori)
    return sum((x - m) ** 2 for x in valori) / (n - 1)
```

### Scope globale

Le variabili definite fuori da qualsiasi funzione, al livello principale del modulo, hanno **scope globale**:

```python
PI: float = 3.14159265  # variabile GLOBALE

def area_cerchio(raggio: float) -> float:
    return PI * raggio ** 2  # può LEGGERE PI

print(area_cerchio(5.0))  # 78.5398...
```

Una funzione puo *leggere* le variabili globali, ma non puo *modificarle* senza una dichiarazione esplicita:

```python
contatore: int = 0

def incrementa() -> None:
    contatore = contatore + 1  # UnboundLocalError!

incrementa()
```

Python vede che `contatore` appare a sinistra di un `=` dentro la funzione e la tratta come variabile locale. Ma quando tenta di leggere `contatore + 1`, la variabile locale non e ancora stata assegnata.

### La parola chiave `global` (e perche evitarla)

Tecnicamente, potete usare `global` per modificare una variabile globale dall'interno di una funzione:

```python
contatore: int = 0

def incrementa() -> None:
    global contatore
    contatore = contatore + 1

incrementa()
print(contatore)  # 1
```

Ma questo e quasi sempre una **cattiva pratica**. Perche?

- Crea **dipendenze nascoste**: la funzione modifica qualcosa che non e tra i suoi parametri ne tra i suoi valori di ritorno. Chi legge la chiamata `incrementa()` non sospetta che una variabile globale sia stata modificata.
- Rende il codice **difficile da testare**: il risultato della funzione dipende dallo stato globale, non solo dai suoi input.
- Causa **bug sottili**: in un programma grande, piu funzioni che modificano la stessa variabile globale creano interazioni imprevedibili.

Il modo corretto e passare il valore come parametro e restituirlo come risultato:

```python
def incrementa(contatore: int) -> int:
    return contatore + 1

contatore: int = 0
contatore = incrementa(contatore)
print(contatore)  # 1
```

### Scope built-in

Oltre allo scope locale e globale, esiste lo scope **built-in**: i nomi predefiniti di Python come `print`, `len`, `sum`, `range`, `int`, `float`, ecc. Questi sono sempre disponibili senza importazioni.

### La regola LEGB

Quando Python incontra un nome, lo cerca in quest'ordine:

1. **L** — **Local**: lo scope della funzione corrente
2. **E** — **Enclosing**: gli scope delle funzioni che racchiudono quella corrente (per le funzioni annidate, che vedremo piu avanti)
3. **G** — **Global**: lo scope del modulo
4. **B** — **Built-in**: i nomi predefiniti di Python

La ricerca si ferma al primo livello in cui il nome viene trovato. Se non viene trovato in nessun livello, Python solleva un `NameError`.

```python
x: str = "globale"

def esterna() -> None:
    x: str = "enclosing"

    def interna() -> None:
        x: str = "locale"
        print(x)  # "locale" — trovata in L

    interna()

esterna()
```

Se rimuovete `x = "locale"` dalla funzione `interna`, Python troverebbe `x` nello scope enclosing ("enclosing"). Se rimuovete anche quello, troverebbe quello globale ("globale"). Se rimuovete tutti e tre, cercherebbe `x` tra i built-in e, non trovandolo, solleverebbe un `NameError`.

---

## Best practice per le funzioni

Ecco un riepilogo delle buone abitudini da seguire quando scrivete funzioni.

### Funzioni brevi e focalizzate

Ogni funzione dovrebbe fare **una cosa sola** e farla bene. Se la vostra funzione supera le 20-30 righe, probabilmente sta facendo troppo e andrebbe spezzata in sotto-funzioni. Una funzione breve e piu facile da capire, da testare e da riutilizzare.

### Comunicare via parametri e return

Le funzioni dovrebbero ricevere i dati necessari tramite i **parametri** e restituire i risultati tramite **return**. Evitate di leggere o modificare variabili globali dall'interno delle funzioni. Questo rende la funzione **pura**: il suo output dipende solo dai suoi input, senza effetti collaterali.

```python
# MALE: usa variabile globale
dati: list[float] = [1.0, 2.0, 3.0]

def media_brutta() -> float:
    return sum(dati) / len(dati)  # dipende dalla variabile globale "dati"

# BENE: riceve i dati come parametro
def media_buona(valori: list[float]) -> float:
    return sum(valori) / len(valori)  # dipende solo dal parametro
```

### Type hints sempre

In questo corso annotiamo *sempre* i parametri e il tipo di ritorno. I type hints sono documentazione vivente, verificabile con strumenti automatici. Non e un capriccio stilistico: in un contesto professionale, il codice senza type hints e piu difficile da mantenere e piu soggetto a errori.

### Nomi significativi

Il nome della funzione deve descrivere *cosa fa*. Usate verbi: `calcola_`, `leggi_`, `filtra_`, `conta_`, `valida_`. Evitate nomi generici come `funzione1`, `fai_cose`, `f`.

### Docstring per ogni funzione

Ogni funzione pubblica (cioe usata da altri, non solo come dettaglio interno) dovrebbe avere una docstring. Anche una sola riga e meglio di niente.

### Un esempio completo

Mettiamo insieme tutto quello che abbiamo visto con un esempio realistico per un corso di statistica:

```python
def analisi_descrittiva(
    valori: list[float],
    nome_variabile: str = "x",
    decimali: int = 2
) -> None:
    """Stampa un'analisi descrittiva di base per una variabile numerica.

    Args:
        valori: lista non vuota di valori numerici.
        nome_variabile: nome della variabile per l'intestazione.
        decimali: numero di cifre decimali nel report.

    Raises:
        ValueError: se la lista e vuota.
    """
    if len(valori) == 0:
        raise ValueError("La lista non puo essere vuota")

    n: int = len(valori)
    media: float = sum(valori) / n
    minimo: float = min(valori)
    massimo: float = max(valori)
    ampiezza: float = massimo - minimo

    print(f"=== Analisi descrittiva: {nome_variabile} ===")
    print(f"  n:         {n}")
    print(f"  Media:     {media:.{decimali}f}")
    print(f"  Minimo:    {minimo:.{decimali}f}")
    print(f"  Massimo:   {massimo:.{decimali}f}")
    print(f"  Ampiezza:  {ampiezza:.{decimali}f}")


# Uso della funzione
altezze: list[float] = [175.2, 168.0, 182.5, 170.3, 178.9, 165.1, 190.0]
analisi_descrittiva(altezze, nome_variabile="altezza (cm)", decimali=1)
```

Output:
```
=== Analisi descrittiva: altezza (cm) ===
  n:         7
  Media:     175.7
  Minimo:    165.1
  Massimo:   190.0
  Ampiezza:  24.9
```

---

## Domande di verifica

1. Quali sono i tre motivi principali per cui si usano le funzioni? Spiegate brevemente ciascuno.

2. Qual e la differenza tra *parametro* e *argomento*? Fate un esempio.

3. Cosa restituisce una funzione che non ha istruzione `return`?

4. Perche `def f(lista: list[int] = [])` e pericoloso? Qual e il pattern corretto?

5. Spiegate la regola LEGB con un esempio. In quale ordine Python cerca un nome?

6. Perche si sconsiglia l'uso della parola chiave `global`? Quale alternativa e preferibile?

7. Cosa succede se una funzione contiene piu istruzioni `return`? Quale viene eseguita?

8. Data la seguente funzione, quali sono i parametri e quali i type hints?
   ```python
   def calcola_iqr(dati: list[float], ordinati: bool = False) -> float:
   ```

---

## Esercizi

### Esercizi base

**Esercizio 1 — Funzione di benvenuto.**
Scrivete una funzione `benvenuto(nome: str, corso: str = "Statistica") -> str` che restituisca la stringa `"Benvenuto/a, {nome}! Corso: {corso}"`. Testatela con e senza il secondo argomento.

**Esercizio 2 — Area del rettangolo.**
Scrivete una funzione `area_rettangolo(base: float, altezza: float) -> float` che calcola e restituisce l'area. Aggiungete una docstring completa (con Args e Returns). Verificate con `help()`.

**Esercizio 3 — Pari o dispari.**
Scrivete una funzione `e_pari(n: int) -> bool` che restituisce `True` se `n` e pari, `False` altrimenti. Usatela in un ciclo `for` per classificare i numeri da 1 a 10.

### Esercizi intermedi

**Esercizio 4 — Statistiche di base.**
Scrivete una funzione `statistiche(valori: list[float]) -> tuple[float, float, float]` che restituisce la media, il valore minimo e il massimo. Gestite il caso della lista vuota restituendo `(0.0, 0.0, 0.0)`. Utilizzate lo spacchettamento della tupla per stampare i risultati.

**Esercizio 5 — Contatore di occorrenze.**
Scrivete una funzione `conta_occorrenze(testo: str, carattere: str) -> int` che conta quante volte `carattere` appare in `testo`, *senza* usare il metodo `.count()`. Aggiungete una docstring completa.

**Esercizio 6 — Formattazione condizionale.**
Scrivete una funzione `formatta_voto(voto: int, lode: bool = False, scala: int = 30) -> str` che restituisce:
- `"INSUFFICIENTE"` se il voto e inferiore a 18
- `"{voto}/{scala}"` normalmente
- `"{voto}/{scala} e lode"` se `lode` e `True` e il voto e uguale a `scala`
- `"Errore: lode non valida"` se `lode` e `True` ma il voto non e uguale a `scala`

### Esercizi avanzati

**Esercizio 7 — Il default mutabile.**
Considerate questa funzione:
```python
def registra_esame(nome: str, esami: list[str] = []) -> list[str]:
    esami.append(nome)
    return esami
```
a) Senza eseguirla, prevedete cosa stampa il seguente codice:
```python
print(registra_esame("Analisi"))
print(registra_esame("Statistica"))
print(registra_esame("Informatica"))
```
b) Riscrivete la funzione in modo corretto.
c) Verificate la vostra previsione eseguendo entrambe le versioni.

**Esercizio 8 — Calcolatrice statistica.**
Create un mini-programma che definisca le seguenti funzioni:
- `media(valori: list[float]) -> float`
- `varianza_campionaria(valori: list[float]) -> float` (che internamente chiama `media()`)
- `deviazione_standard(valori: list[float]) -> float` (che internamente chiama `varianza_campionaria()`)
- `coefficiente_variazione(valori: list[float]) -> float` (che internamente chiama `media()` e `deviazione_standard()`)

Ogni funzione deve avere type hints completi e una docstring. Il programma principale chiede all'utente di inserire una serie di numeri separati da virgola e stampa tutte le statistiche calcolate.

---

## Osservazioni finali

Le funzioni sono il primo vero strumento di *ingegneria del software* che incontrate in questo corso. Fino a oggi avete scritto codice che risolve problemi piccoli e autocontenuti. Con le funzioni, potete iniziare a costruire programmi piu grandi, piu leggibili e piu affidabili.

I concetti chiave di questa lezione sono:

- **Definire funzioni** con `def`, parametri tipizzati e `return`.
- **Documentarle** con docstring complete.
- **Distinguere** parametri e argomenti, scope locale e globale.
- **Evitare** i default mutabili e le variabili globali.
- **Seguire** le best practice: funzioni brevi, nomi significativi, type hints sempre.

Nelle prossime lezioni costruiremo su queste fondamenta, esplorando concetti piu avanzati come le funzioni come oggetti, le funzioni lambda, la ricorsione e l'uso delle funzioni nella manipolazione di file e dati. Per ora, assicuratevi di aver interiorizzato i fondamenti: la vostra produttivita come programmatori dipendera in larga misura dalla vostra capacita di progettare buone funzioni.

Un ultimo consiglio pratico: quando vi trovate a copiare e incollare codice, fermatevi. Probabilmente quel codice dovrebbe essere una funzione.
