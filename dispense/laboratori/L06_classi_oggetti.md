# Laboratorio 6 --- Classi e oggetti

**Prerequisiti**: Frontale T16 (Classi e programmazione orientata agli oggetti)

**Obiettivo**: mettere in pratica la definizione di classi in Python, con attributi, metodi, metodi speciali (`__str__`, `__repr__`, `__eq__`, `__lt__`), validazione dei dati e composizione di oggetti.

---

## Esercizio guidato 1 --- `Punto2D`: coordinate, distanza, `__str__`

Iniziamo con una classe semplice che rappresenta un punto nel piano cartesiano.

### Passo 1: definire la classe base

```python
import math


class Punto2D:
    """Rappresenta un punto nel piano cartesiano."""

    def __init__(self, x: float, y: float) -> None:
        """Inizializza un punto con coordinate x e y.

        Args:
            x: Coordinata orizzontale.
            y: Coordinata verticale.
        """
        self.x: float = x
        self.y: float = y

    def distanza_da(self, altro: "Punto2D") -> float:
        """Calcola la distanza euclidea da un altro punto.

        Args:
            altro: Un altro punto nel piano.

        Returns:
            La distanza euclidea tra i due punti.
        """
        dx: float = self.x - altro.x
        dy: float = self.y - altro.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def distanza_da_origine(self) -> float:
        """Calcola la distanza dall'origine (0, 0).

        Returns:
            La distanza euclidea dall'origine.
        """
        return self.distanza_da(Punto2D(0.0, 0.0))

    def __str__(self) -> str:
        """Restituisce una rappresentazione leggibile del punto."""
        return f"({self.x}, {self.y})"


# --- Prova ---
if __name__ == "__main__":
    p1: Punto2D = Punto2D(3.0, 4.0)
    p2: Punto2D = Punto2D(0.0, 0.0)

    print(f"Punto 1: {p1}")             # Usa __str__
    print(f"Punto 2: {p2}")
    print(f"Distanza p1-p2: {p1.distanza_da(p2):.2f}")
    print(f"Distanza p1 dall'origine: {p1.distanza_da_origine():.2f}")
```

**Output atteso**:

```
Punto 1: (3.0, 4.0)
Punto 2: (0.0, 0.0)
Distanza p1-p2: 5.00
Distanza p1 dall'origine: 5.00
```

**Cosa notiamo**:

- `__init__` e' il costruttore: viene chiamato automaticamente quando scriviamo `Punto2D(3.0, 4.0)`.
- `self` e' il riferimento all'oggetto corrente: ogni metodo lo riceve come primo parametro.
- `__str__` viene invocato automaticamente da `print()` e dalle f-string.
- `distanza_da_origine` riusa `distanza_da` --- un metodo puo' chiamare altri metodi dello stesso oggetto.

### Passo 2: aggiungere `__repr__`

```python
    def __repr__(self) -> str:
        """Restituisce una rappresentazione tecnica del punto.

        La convenzione e' che repr() produca una stringa che,
        incollata nell'interprete, ricrei l'oggetto.
        """
        return f"Punto2D({self.x}, {self.y})"
```

La differenza: `__str__` e' per gli umani (`print`), `__repr__` e' per i programmatori (debug, interprete interattivo, rappresentazione nelle liste).

```python
    punti: list[Punto2D] = [Punto2D(1, 2), Punto2D(3, 4)]
    print(punti)  # Usa __repr__ per ogni elemento: [Punto2D(1, 2), Punto2D(3, 4)]
    print(punti[0])  # Usa __str__: (1, 2)
```

---

## Esercizio guidato 2 --- `Studente`: nome, cognome, matricola, voti, `aggiungi_voto`

Costruiamo una classe piu' ricca, con validazione dei dati.

```python
class Studente:
    """Rappresenta uno studente universitario con i suoi voti."""

    def __init__(
        self,
        nome: str,
        cognome: str,
        matricola: str,
    ) -> None:
        """Inizializza uno studente.

        Args:
            nome: Nome dello studente.
            cognome: Cognome dello studente.
            matricola: Codice matricola univoco.

        Raises:
            ValueError: Se nome, cognome o matricola sono vuoti.
        """
        if not nome.strip():
            raise ValueError("Il nome non puo' essere vuoto")
        if not cognome.strip():
            raise ValueError("Il cognome non puo' essere vuoto")
        if not matricola.strip():
            raise ValueError("La matricola non puo' essere vuota")

        self.nome: str = nome.strip()
        self.cognome: str = cognome.strip()
        self.matricola: str = matricola.strip()
        self.voti: list[int] = []

    def aggiungi_voto(self, voto: int) -> None:
        """Aggiunge un voto alla lista dei voti dello studente.

        Args:
            voto: Un voto tra 18 e 30 (inclusi).

        Raises:
            ValueError: Se il voto non e' nell'intervallo 18-30.
            TypeError: Se il voto non e' un intero.
        """
        if not isinstance(voto, int):
            raise TypeError(f"Il voto deve essere un intero, ricevuto {type(voto).__name__}")
        if voto < 18 or voto > 30:
            raise ValueError(f"Il voto deve essere tra 18 e 30, ricevuto {voto}")
        self.voti.append(voto)

    def media(self) -> float:
        """Calcola la media aritmetica dei voti.

        Returns:
            La media dei voti.

        Raises:
            ValueError: Se non ci sono voti registrati.
        """
        if not self.voti:
            raise ValueError(
                f"Nessun voto registrato per {self.nome} {self.cognome}"
            )
        return sum(self.voti) / len(self.voti)

    def numero_esami(self) -> int:
        """Restituisce il numero di esami sostenuti."""
        return len(self.voti)

    def __str__(self) -> str:
        """Rappresentazione leggibile dello studente."""
        n_esami: int = self.numero_esami()
        if n_esami > 0:
            return (
                f"{self.nome} {self.cognome} ({self.matricola}) "
                f"- {n_esami} esami, media: {self.media():.2f}"
            )
        return f"{self.nome} {self.cognome} ({self.matricola}) - nessun esame"


# --- Prova ---
if __name__ == "__main__":
    s: Studente = Studente("Anna", "Rossi", "MAT001")
    print(s)  # Nessun esame

    s.aggiungi_voto(28)
    s.aggiungi_voto(25)
    s.aggiungi_voto(30)
    print(s)  # Con media

    # Test validazione
    try:
        s.aggiungi_voto(15)  # Troppo basso
    except ValueError as e:
        print(f"Errore catturato: {e}")

    try:
        s.aggiungi_voto(25.5)  # Non intero
    except TypeError as e:
        print(f"Errore catturato: {e}")
```

**Output atteso**:

```
Anna Rossi (MAT001) - nessun esame
Anna Rossi (MAT001) - 3 esami, media: 27.67
Errore catturato: Il voto deve essere tra 18 e 30, ricevuto 15
Errore catturato: Il voto deve essere un intero, ricevuto float
```

**Punto chiave**: la validazione nel metodo `aggiungi_voto` garantisce che l'oggetto sia sempre in uno stato coerente. Non e' possibile inserire un voto di 15 o un valore decimale. Questa e' la potenza dell'incapsulamento: la classe protegge i propri dati.

---

## Esercizio guidato 3 --- `__repr__`, `__eq__`, `__lt__` su `Studente`

Aggiungiamo i metodi speciali che permettono di confrontare e ordinare gli studenti.

```python
class Studente:
    """Rappresenta uno studente universitario con i suoi voti."""

    def __init__(
        self,
        nome: str,
        cognome: str,
        matricola: str,
    ) -> None:
        if not nome.strip():
            raise ValueError("Il nome non puo' essere vuoto")
        if not cognome.strip():
            raise ValueError("Il cognome non puo' essere vuoto")
        if not matricola.strip():
            raise ValueError("La matricola non puo' essere vuota")

        self.nome: str = nome.strip()
        self.cognome: str = cognome.strip()
        self.matricola: str = matricola.strip()
        self.voti: list[int] = []

    def aggiungi_voto(self, voto: int) -> None:
        if not isinstance(voto, int):
            raise TypeError(
                f"Il voto deve essere un intero, ricevuto {type(voto).__name__}"
            )
        if voto < 18 or voto > 30:
            raise ValueError(
                f"Il voto deve essere tra 18 e 30, ricevuto {voto}"
            )
        self.voti.append(voto)

    def media(self) -> float:
        if not self.voti:
            raise ValueError(
                f"Nessun voto registrato per {self.nome} {self.cognome}"
            )
        return sum(self.voti) / len(self.voti)

    def numero_esami(self) -> int:
        return len(self.voti)

    def __str__(self) -> str:
        n_esami: int = self.numero_esami()
        if n_esami > 0:
            return (
                f"{self.nome} {self.cognome} ({self.matricola}) "
                f"- {n_esami} esami, media: {self.media():.2f}"
            )
        return f"{self.nome} {self.cognome} ({self.matricola}) - nessun esame"

    def __repr__(self) -> str:
        """Rappresentazione tecnica: permette di ricreare l'oggetto."""
        return f"Studente('{self.nome}', '{self.cognome}', '{self.matricola}')"

    def __eq__(self, altro: object) -> bool:
        """Due studenti sono uguali se hanno la stessa matricola.

        La matricola e' l'identificatore univoco: due studenti con
        la stessa matricola sono la stessa persona, indipendentemente
        da eventuali differenze nei campi nome/cognome (errori di battitura).
        """
        if not isinstance(altro, Studente):
            return NotImplemented
        return self.matricola == altro.matricola

    def __lt__(self, altro: "Studente") -> bool:
        """Ordinamento per cognome, poi per nome.

        Questo permette di usare sorted() su liste di studenti.
        """
        if not isinstance(altro, Studente):
            return NotImplemented
        if self.cognome == altro.cognome:
            return self.nome < altro.nome
        return self.cognome < altro.cognome


# --- Prova ---
if __name__ == "__main__":
    s1: Studente = Studente("Anna", "Rossi", "MAT001")
    s2: Studente = Studente("Marco", "Bianchi", "MAT002")
    s3: Studente = Studente("Anna", "Rossi", "MAT001")  # Stessa matricola di s1
    s4: Studente = Studente("Lucia", "Bianchi", "MAT004")

    # __repr__
    print(repr(s1))  # Studente('Anna', 'Rossi', 'MAT001')

    # __eq__
    print(f"s1 == s3? {s1 == s3}")  # True (stessa matricola)
    print(f"s1 == s2? {s1 == s2}")  # False

    # __lt__ e ordinamento
    print(f"s2 < s1? {s2 < s1}")   # True (Bianchi < Rossi)

    # sorted() funziona grazie a __lt__
    studenti: list[Studente] = [s1, s2, s4]
    ordinati: list[Studente] = sorted(studenti)
    print("\nStudenti ordinati per cognome e nome:")
    for s in ordinati:
        print(f"  {s}")
```

**Output atteso**:

```
Studente('Anna', 'Rossi', 'MAT001')
s1 == s3? True
s1 == s2? False
s2 < s1? True

Studenti ordinati per cognome e nome:
  Lucia Bianchi (MAT004) - nessun esame
  Marco Bianchi (MAT002) - nessun esame
  Anna Rossi (MAT001) - nessun esame
```

**Dettagli importanti**:

- `__eq__` restituisce `NotImplemented` (non `False`) quando il tipo e' sbagliato: questo permette a Python di provare il confronto nell'altro senso.
- `__lt__` e' sufficiente per far funzionare `sorted()`: Python usa internamente solo `<` per l'ordinamento.
- Definire l'uguaglianza sulla matricola e' una scelta di modellazione: due record con la stessa matricola sono lo stesso studente.

---

## Esercizio guidato 4 --- `sorted()` su lista di studenti

Approfondiamo l'ordinamento con criteri diversi, usando sia `__lt__` sia il parametro `key` di `sorted()`.

```python
def crea_classe_esempio() -> list[Studente]:
    """Crea una lista di studenti di esempio con voti."""
    dati: list[tuple[str, str, str, list[int]]] = [
        ("Anna", "Rossi", "MAT001", [28, 25, 30]),
        ("Marco", "Bianchi", "MAT002", [22, 24, 26]),
        ("Lucia", "Verdi", "MAT003", [30, 30, 28]),
        ("Giuseppe", "Neri", "MAT004", [18, 20, 22]),
        ("Francesca", "Rossi", "MAT005", [27, 29]),
    ]

    studenti: list[Studente] = []
    for nome, cognome, matricola, voti in dati:
        s: Studente = Studente(nome, cognome, matricola)
        for voto in voti:
            s.aggiungi_voto(voto)
        studenti.append(s)

    return studenti


def stampa_classifica(studenti: list[Studente], titolo: str) -> None:
    """Stampa una lista numerata di studenti."""
    print(f"\n{titolo}")
    print("=" * 60)
    for i, s in enumerate(studenti, start=1):
        print(f"  {i}. {s}")


if __name__ == "__main__":
    classe: list[Studente] = crea_classe_esempio()

    # Ordinamento predefinito: per cognome e nome (usa __lt__)
    stampa_classifica(
        sorted(classe),
        "Ordine alfabetico (cognome, nome)"
    )

    # Ordinamento per media (decrescente)
    per_media: list[Studente] = sorted(
        classe,
        key=lambda s: s.media(),
        reverse=True,
    )
    stampa_classifica(per_media, "Classifica per media (decrescente)")

    # Ordinamento per numero di esami
    per_esami: list[Studente] = sorted(
        classe,
        key=lambda s: s.numero_esami(),
    )
    stampa_classifica(per_esami, "Per numero di esami (crescente)")

    # Ordinamento per matricola
    per_matricola: list[Studente] = sorted(
        classe,
        key=lambda s: s.matricola,
    )
    stampa_classifica(per_matricola, "Per matricola")
```

**Punto chiave**: `sorted()` usa `__lt__` come criterio predefinito, ma il parametro `key` permette di ordinare per qualsiasi attributo o calcolo. La funzione passata a `key` viene chiamata una volta per ogni elemento e il risultato viene usato per il confronto.

---

## Esercizi autonomi

### Base

**Esercizio 1 --- Classe `Rettangolo`**

Definite una classe `Rettangolo` con:

- `__init__(self, base: float, altezza: float) -> None` --- validare che base e altezza siano positive.
- `area(self) -> float` --- restituisce l'area.
- `perimetro(self) -> float` --- restituisce il perimetro.
- `e_quadrato(self) -> bool` --- restituisce `True` se base e altezza sono uguali.
- `__str__(self) -> str` --- es. `"Rettangolo(base=5.0, altezza=3.0)"`.
- `__repr__(self) -> str` --- es. `"Rettangolo(5.0, 3.0)"`.
- `__eq__(self, altro: object) -> bool` --- due rettangoli sono uguali se hanno stessa area.
- `__lt__(self, altro: "Rettangolo") -> bool` --- confronto per area.

Testate la classe creando una lista di rettangoli e ordinandoli con `sorted()`.

---

### Base

**Esercizio 2 --- Classe `ContoCorrente`**

Definite una classe `ContoCorrente` con:

- `__init__(self, titolare: str, saldo_iniziale: float = 0.0) -> None` --- validare che il saldo iniziale non sia negativo.
- `deposita(self, importo: float) -> None` --- aggiunge al saldo; l'importo deve essere positivo.
- `preleva(self, importo: float) -> None` --- sottrae dal saldo; l'importo deve essere positivo e non deve superare il saldo disponibile (`ValueError` altrimenti).
- `saldo(self) -> float` --- restituisce il saldo corrente (proprieta' o metodo, a scelta).
- `storico(self) -> list[str]` --- restituisce la lista delle operazioni nel formato `"DEPOSITO: +100.00"` oppure `"PRELIEVO: -50.00"`.
- `__str__(self) -> str` --- es. `"Conto di Mario Rossi: saldo 1250.00 EUR"`.

Testate la classe simulando una sequenza di operazioni e stampando lo storico.

---

### Intermedio

**Esercizio 3 --- Classe `Corso`**

Definite una classe `Corso` che gestisce una lista di studenti (usando la classe `Studente` costruita negli esercizi guidati). La classe deve avere:

- `__init__(self, nome: str, codice: str) -> None`.
- `iscrivi(self, studente: Studente) -> None` --- aggiunge lo studente al corso; se la matricola e' gia' presente, solleva `ValueError`.
- `cerca_studente(self, matricola: str) -> Studente | None` --- restituisce lo studente con quella matricola, o `None`.
- `media_corso(self) -> float` --- media di tutte le medie degli studenti che hanno almeno un voto.
- `migliore(self) -> Studente` --- restituisce lo studente con la media piu' alta.
- `classifica(self) -> list[Studente]` --- restituisce gli studenti ordinati per media decrescente.
- `__len__(self) -> int` --- numero di studenti iscritti (permette di scrivere `len(corso)`).
- `__str__(self) -> str` --- riepilogo del corso.

---

### Intermedio

**Esercizio 4 --- Classe `Temperatura`**

Definite una classe `Temperatura` che rappresenta una temperatura e permette conversioni tra scale.

- `__init__(self, gradi: float, scala: str = "C") -> None` --- la scala puo' essere `"C"` (Celsius), `"F"` (Fahrenheit) o `"K"` (Kelvin). Validare la scala e verificare che la temperatura non sia sotto lo zero assoluto.
- `in_celsius(self) -> float`, `in_fahrenheit(self) -> float`, `in_kelvin(self) -> float`.
- `__str__(self) -> str` --- es. `"20.0 C"`.
- `__eq__(self, altro: object) -> bool` --- due temperature sono uguali se rappresentano lo stesso valore fisico (confronto in Kelvin).
- `__lt__(self, altro: "Temperatura") -> bool` --- confronto in Kelvin.

Testate creando temperature in scale diverse e verificando che `sorted()` le ordini correttamente.

---

### Avanzato

**Esercizio 5 --- Classe `Inventario`**

Definite una classe `Prodotto` con `codice: str`, `nome: str`, `prezzo: float`, `quantita: int`. Poi definite una classe `Inventario` con:

- `aggiungi(self, prodotto: Prodotto) -> None` --- aggiunge o aggiorna la quantita' se il codice esiste gia'.
- `rimuovi(self, codice: str, quantita: int) -> None` --- riduce la quantita'; solleva `ValueError` se la quantita' e' insufficiente.
- `cerca(self, nome: str) -> list[Prodotto]` --- cerca prodotti il cui nome contiene la stringa (case-insensitive).
- `valore_totale(self) -> float` --- somma di (prezzo * quantita) per tutti i prodotti.
- `sotto_scorta(self, soglia: int = 5) -> list[Prodotto]` --- prodotti con quantita' inferiore alla soglia.
- `__len__(self) -> int` --- numero di prodotti distinti.
- `__str__(self) -> str` --- riepilogo dell'inventario.

---

## Sfida finale --- Classe `Dataset`: un mini-Pandas

Costruite una classe `Dataset` che imita (in modo molto semplificato) il comportamento di un DataFrame Pandas. La classe deve permettere di caricare dati da CSV, filtrarli, raggrupparli e calcolare statistiche.

### Specifiche

La classe `Dataset` deve avere i seguenti metodi:

- `__init__(self, intestazione: list[str], righe: list[dict[str, str]]) -> None` --- inizializza con nomi di colonne e dati.

- `carica_da_csv(percorso: Path, delimiter: str = ",") -> "Dataset"` --- metodo statico (`@staticmethod`) che crea un `Dataset` leggendo un file CSV. Gestire `FileNotFoundError` e encoding.

- `n_righe(self) -> int` --- numero di righe.

- `n_colonne(self) -> int` --- numero di colonne.

- `colonna(self, nome: str) -> list[str]` --- restituisce tutti i valori di una colonna come lista di stringhe. Solleva `KeyError` se la colonna non esiste.

- `colonna_numerica(self, nome: str) -> list[float | None]` --- come `colonna`, ma converte i valori in `float` (i non convertibili diventano `None`).

- `filtra(self, colonna: str, valore: str) -> "Dataset"` --- restituisce un *nuovo* `Dataset` contenente solo le righe in cui la colonna ha il valore specificato.

- `raggruppa(self, colonna: str) -> dict[str, "Dataset"]` --- restituisce un dizionario che associa ogni valore distinto della colonna a un `Dataset` contenente le righe corrispondenti.

- `statistiche(self, colonna: str) -> dict[str, float | int | None]` --- per una colonna numerica, calcola e restituisce: `conteggio`, `media`, `minimo`, `massimo`, `somma`. Ignora i valori `None`.

- `salva_csv(self, percorso: Path, delimiter: str = ",") -> None` --- salva il dataset in un file CSV.

- `__str__(self) -> str` --- mostra le prime 5 righe in formato tabellare.

- `__len__(self) -> int` --- numero di righe.

### Esempio d'uso atteso

```python
from pathlib import Path

# Caricamento
ds: Dataset = Dataset.carica_da_csv(Path("vendite.csv"), delimiter=";")
print(f"Dataset: {ds.n_righe()} righe, {ds.n_colonne()} colonne")
print(ds)

# Filtraggio
roma: Dataset = ds.filtra("citta", "Roma")
print(f"\nVendite a Roma: {roma.n_righe()} righe")

# Raggruppamento e statistiche
per_citta: dict[str, Dataset] = ds.raggruppa("citta")
for citta, sottoinsieme in per_citta.items():
    stats: dict[str, float | int | None] = sottoinsieme.statistiche("importo")
    print(f"{citta}: media={stats['media']:.2f}, totale={stats['somma']:.2f}")

# Salvataggio
roma.salva_csv(Path("output") / "vendite_roma.csv", delimiter=";")
```

### Suggerimenti

- Internamente, memorizzate i dati come `list[dict[str, str]]`: ogni dizionario e' una riga con chiavi = nomi di colonna.
- `filtra` e `raggruppa` devono restituire *nuovi* oggetti `Dataset`, senza modificare l'originale.
- Per `statistiche`, convertite la colonna con `colonna_numerica` e poi calcolate le metriche ignorando i `None`.
- Per `__str__`, formattate le prime 5 righe in colonne allineate.

---

## Domande di verifica

1. Qual e' la differenza tra `__str__` e `__repr__`? Quando viene chiamato ciascuno? Se definite solo uno dei due, quale scegliete e perche'?

2. Perche' il metodo `__eq__` deve restituire `NotImplemented` (e non `False`) quando il tipo dell'altro oggetto e' sbagliato?

3. Spiegate perche' basta definire `__lt__` per far funzionare `sorted()` su una lista di oggetti. Quali altri metodi di confronto potremmo definire?

4. Nel metodo `aggiungi_voto` della classe `Studente`, perche' usiamo `isinstance(voto, int)` per il controllo del tipo invece di `type(voto) == int`?

5. Cosa significa che `self` e' "implicito" nelle chiamate ai metodi? Scrivete l'equivalente esplicito di `s.aggiungi_voto(28)`.

6. Nella classe `Dataset` della sfida, perche' e' importante che `filtra()` restituisca un nuovo oggetto invece di modificare quello esistente?

7. Qual e' la differenza tra un metodo normale e un metodo statico (`@staticmethod`)? Perche' `carica_da_csv` e' un buon candidato per essere statico?

---

## Osservazioni finali

In questo laboratorio avete costruito le vostre prime classi da zero, partendo da un semplice `Punto2D` fino alla sfida di un `Dataset` che imita il comportamento di Pandas. Il percorso e' stato pensato per farvi toccare con mano i concetti chiave della programmazione orientata agli oggetti:

- **Incapsulamento**: i dati (attributi) e le operazioni su di essi (metodi) vivono insieme. La validazione in `aggiungi_voto` protegge l'integrita' dell'oggetto.
- **Metodi speciali**: `__str__`, `__repr__`, `__eq__`, `__lt__` permettono ai vostri oggetti di integrarsi con il linguaggio --- potete stamparli, confrontarli, ordinarli come se fossero tipi built-in.
- **Composizione**: un `Corso` contiene una lista di `Studente`, un `Dataset` contiene righe e colonne. Costruire sistemi complessi componendo oggetti semplici e' il cuore della progettazione orientata agli oggetti.

I punti da portare con se':

- **Validazione nel costruttore e nei metodi**: non fidatevi mai dei dati in ingresso. Un oggetto deve essere sempre in uno stato coerente.
- **`__repr__` per il debug**: quando qualcosa non funziona, `repr()` vi mostra esattamente cosa contiene un oggetto.
- **`__eq__` e `__lt__` per i confronti**: definirli permette di usare `==`, `sorted()`, `min()`, `max()` sui vostri oggetti.
- **Restituire nuovi oggetti** (come in `filtra`): non modificate l'originale, create una copia filtrata. Questo rende il codice piu' prevedibile e meno soggetto a bug.

Nelle prossime lezioni vedrete come Pandas usa esattamente questi principi --- metodi che restituiscono nuovi DataFrame, operatori sovraccaricati, composizione di strutture --- per costruire uno strumento di analisi dati potentissimo.
