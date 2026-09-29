# Progetto 2: Rubrica contatti

## Introduzione

In questo progetto costruirai una rubrica contatti completa in Python. Partirai da una versione procedurale (con funzioni) e poi la convertirai in una versione orientata agli oggetti (con classi). Imparerai a:

- Leggere e scrivere file JSON (**T07** - Input/Output su file)
- Gestire input utente con cicli (**T08** - Input/Output interattivo)
- Usare dizionari e liste per strutturare i dati (**T09** - Strutture dati)
- Definire e usare funzioni (**T12** - Funzioni base, **T15** - Funzioni avanzate)
- Controllare il flusso con menu e condizioni (**T13** - Controllo di flusso)
- Definire classi e oggetti (**T16** - Programmazione orientata agli oggetti)

---

## Passo 1: Definire la struttura dati di un contatto

### Cosa imparerai
- Usare dizionari per rappresentare entita' strutturate
- Definire uno "schema" per i dati
- Validare input

### Spiegazione

Ogni contatto nella rubrica avra' queste informazioni:
- **nome**: nome completo della persona
- **telefono**: numero di telefono
- **email**: indirizzo email
- **categoria**: tipo di contatto (amico, lavoro, famiglia, altro)

Iniziamo rappresentando ogni contatto come un dizionario e la rubrica come una lista di dizionari.

### Suggerimenti
- Le categorie valide sono: "amico", "lavoro", "famiglia", "altro"
- Usa una funzione per creare un nuovo contatto con validazione
- Un contatto vuoto puo' servire come template

### Scheletro di codice

```python
# Categorie valide per i contatti
CATEGORIE_VALIDE = ["amico", "lavoro", "famiglia", "altro"]

def crea_contatto(nome, telefono, email, categoria):
    """Crea un nuovo dizionario contatto con validazione."""
    # TODO: verifica che la categoria sia valida
    # TODO: verifica che nome e telefono non siano vuoti
    # TODO: restituisci un dizionario con i dati del contatto
    pass

# Esempio
contatto = crea_contatto("Mario Rossi", "333-1234567", "mario@email.it", "amico")
print(contatto)
```

<details>
<summary>Soluzione Passo 1</summary>

```python
CATEGORIE_VALIDE = ["amico", "lavoro", "famiglia", "altro"]

def crea_contatto(nome, telefono, email, categoria):
    """Crea un nuovo dizionario contatto con validazione."""
    if not nome.strip():
        raise ValueError("Il nome non puo' essere vuoto")
    if not telefono.strip():
        raise ValueError("Il telefono non puo' essere vuoto")
    if categoria not in CATEGORIE_VALIDE:
        raise ValueError(f"Categoria non valida. Scegli tra: {CATEGORIE_VALIDE}")
    return {
        'nome': nome.strip(),
        'telefono': telefono.strip(),
        'email': email.strip(),
        'categoria': categoria
    }

# Esempio
contatto = crea_contatto("Mario Rossi", "333-1234567", "mario@email.it", "amico")
print(contatto)
```
</details>

---

## Passo 2: Operazioni CRUD (Crea, Cerca, Modifica, Elimina)

### Cosa imparerai
- Implementare le quattro operazioni fondamentali sui dati
- Cercare in una lista di dizionari
- Modificare dizionari in una lista

### Spiegazione

CRUD e' un acronimo che indica le quattro operazioni base su qualsiasi collezione di dati:
- **C**reate (Crea) - aggiungere un nuovo contatto
- **R**ead (Leggi/Cerca) - trovare contatti per nome o categoria
- **U**pdate (Modifica) - aggiornare i dati di un contatto
- **D**elete (Elimina) - rimuovere un contatto

### Suggerimenti
- La funzione di ricerca puo' cercare sia per nome (parziale) che per categoria
- Usa `str.lower()` per ricerche case-insensitive
- La funzione di modifica deve prima trovare il contatto, poi aggiornarlo
- La funzione di eliminazione puo' usare `list.remove()` o ricostruire la lista

### Scheletro di codice

```python
def aggiungi_contatto(rubrica, contatto):
    """Aggiunge un contatto alla rubrica."""
    # TODO: controlla se esiste gia' un contatto con lo stesso nome
    # TODO: aggiungi il contatto alla lista
    pass

def cerca_contatti(rubrica, termine):
    """Cerca contatti per nome (ricerca parziale, case-insensitive)."""
    # TODO: restituisci i contatti il cui nome contiene il termine
    pass

def cerca_per_categoria(rubrica, categoria):
    """Cerca contatti per categoria."""
    # TODO: restituisci i contatti della categoria specificata
    pass

def modifica_contatto(rubrica, nome, campo, nuovo_valore):
    """Modifica un campo di un contatto identificato per nome."""
    # TODO: trova il contatto e aggiorna il campo specificato
    pass

def elimina_contatto(rubrica, nome):
    """Elimina un contatto dalla rubrica."""
    # TODO: trova e rimuovi il contatto
    pass
```

<details>
<summary>Soluzione Passo 2</summary>

```python
def aggiungi_contatto(rubrica, contatto):
    """Aggiunge un contatto alla rubrica. Restituisce True se aggiunto."""
    # Controlla duplicati
    for c in rubrica:
        if c['nome'].lower() == contatto['nome'].lower():
            print(f"Errore: il contatto '{contatto['nome']}' esiste gia'.")
            return False
    rubrica.append(contatto)
    return True

def cerca_contatti(rubrica, termine):
    """Cerca contatti per nome (ricerca parziale, case-insensitive)."""
    termine = termine.lower()
    return [c for c in rubrica if termine in c['nome'].lower()]

def cerca_per_categoria(rubrica, categoria):
    """Cerca contatti per categoria."""
    return [c for c in rubrica if c['categoria'] == categoria]

def modifica_contatto(rubrica, nome, campo, nuovo_valore):
    """Modifica un campo di un contatto identificato per nome."""
    campi_validi = ['nome', 'telefono', 'email', 'categoria']
    if campo not in campi_validi:
        print(f"Errore: campo '{campo}' non valido. Campi: {campi_validi}")
        return False
    if campo == 'categoria' and nuovo_valore not in CATEGORIE_VALIDE:
        print(f"Errore: categoria non valida.")
        return False
    for c in rubrica:
        if c['nome'].lower() == nome.lower():
            c[campo] = nuovo_valore
            return True
    print(f"Contatto '{nome}' non trovato.")
    return False

def elimina_contatto(rubrica, nome):
    """Elimina un contatto dalla rubrica. Restituisce True se eliminato."""
    for i, c in enumerate(rubrica):
        if c['nome'].lower() == nome.lower():
            rubrica.pop(i)
            return True
    print(f"Contatto '{nome}' non trovato.")
    return False
```
</details>

---

## Passo 3: Menu interattivo

### Cosa imparerai
- Creare un ciclo `while` per un menu interattivo
- Gestire l'input dell'utente con validazione
- Usare `if/elif/else` per instradare le scelte

### Spiegazione

Il menu permette all'utente di scegliere quale operazione eseguire. Il programma continua a mostrare il menu finche' l'utente non sceglie di uscire. Questo e' un pattern molto comune nelle applicazioni da terminale.

### Suggerimenti
- Usa un ciclo `while True` con `break` per uscire
- Mostra le opzioni numerate per semplicita'
- Gestisci input non validi con messaggi di errore chiari
- Usa una funzione separata per stampare il menu

### Scheletro di codice

```python
def mostra_menu():
    """Mostra il menu delle opzioni."""
    print("\n=== RUBRICA CONTATTI ===")
    print("1. Aggiungi contatto")
    print("2. Cerca contatto")
    print("3. Mostra tutti i contatti")
    print("4. Modifica contatto")
    print("5. Elimina contatto")
    print("6. Statistiche")
    print("7. Salva ed esci")
    print("========================")

def menu_interattivo(rubrica):
    """Gestisce il menu interattivo della rubrica."""
    while True:
        mostra_menu()
        scelta = input("Scegli un'opzione (1-7): ").strip()

        if scelta == "1":
            # TODO: chiedi i dati e aggiungi il contatto
            pass
        elif scelta == "2":
            # TODO: chiedi il termine di ricerca e mostra i risultati
            pass
        # TODO: gestisci le altre opzioni
        elif scelta == "7":
            print("Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")
```

<details>
<summary>Soluzione Passo 3</summary>

```python
def formatta_contatto(contatto):
    """Formatta un contatto per la stampa."""
    return (f"  Nome: {contatto['nome']}\n"
            f"  Tel:  {contatto['telefono']}\n"
            f"  Email:{contatto['email']}\n"
            f"  Cat:  {contatto['categoria']}")

def mostra_menu():
    """Mostra il menu delle opzioni."""
    print("\n=== RUBRICA CONTATTI ===")
    print("1. Aggiungi contatto")
    print("2. Cerca contatto")
    print("3. Mostra tutti i contatti")
    print("4. Modifica contatto")
    print("5. Elimina contatto")
    print("6. Statistiche")
    print("7. Salva ed esci")
    print("========================")

def menu_interattivo(rubrica):
    """Gestisce il menu interattivo della rubrica."""
    while True:
        mostra_menu()
        scelta = input("Scegli un'opzione (1-7): ").strip()

        if scelta == "1":
            print("\n--- Nuovo contatto ---")
            nome = input("Nome: ")
            telefono = input("Telefono: ")
            email = input("Email: ")
            print(f"Categorie: {CATEGORIE_VALIDE}")
            categoria = input("Categoria: ")
            try:
                contatto = crea_contatto(nome, telefono, email, categoria)
                if aggiungi_contatto(rubrica, contatto):
                    print(f"Contatto '{nome}' aggiunto!")
            except ValueError as e:
                print(f"Errore: {e}")

        elif scelta == "2":
            termine = input("Cerca per nome: ")
            risultati = cerca_contatti(rubrica, termine)
            if risultati:
                print(f"\nTrovati {len(risultati)} contatti:")
                for c in risultati:
                    print(formatta_contatto(c))
                    print()
            else:
                print("Nessun contatto trovato.")

        elif scelta == "3":
            if not rubrica:
                print("La rubrica e' vuota.")
            else:
                print(f"\n--- Tutti i contatti ({len(rubrica)}) ---")
                for c in rubrica:
                    print(formatta_contatto(c))
                    print()

        elif scelta == "4":
            nome = input("Nome del contatto da modificare: ")
            campo = input("Campo da modificare (nome/telefono/email/categoria): ")
            nuovo = input(f"Nuovo valore per '{campo}': ")
            if modifica_contatto(rubrica, nome, campo, nuovo):
                print("Contatto aggiornato!")

        elif scelta == "5":
            nome = input("Nome del contatto da eliminare: ")
            if elimina_contatto(rubrica, nome):
                print(f"Contatto '{nome}' eliminato.")

        elif scelta == "6":
            stampa_statistiche(rubrica)

        elif scelta == "7":
            print("Arrivederci!")
            break

        else:
            print("Opzione non valida. Riprova.")
```
</details>

---

## Passo 4: Salvataggio e caricamento con JSON

### Cosa imparerai
- Usare il modulo `json` per salvare dati strutturati
- Caricare dati da file JSON
- Gestire il caso in cui il file non esiste

### Spiegazione

JSON (JavaScript Object Notation) e' un formato di testo per memorizzare dati strutturati. E' molto usato perche' e' leggibile sia dagli umani che dai computer. Python ha un modulo built-in `json` che converte facilmente liste e dizionari in JSON e viceversa.

### Suggerimenti
- `json.dump()` scrive su file, `json.dumps()` restituisce una stringa
- `json.load()` legge da file, `json.loads()` legge da una stringa
- Usa `ensure_ascii=False` per mantenere i caratteri accentati
- Usa `indent=2` per un formato leggibile
- Gestisci `FileNotFoundError` per il primo avvio (quando il file non esiste)

### Scheletro di codice

```python
import json

PERCORSO_FILE = Path(__file__).parent / "rubrica.json"

def salva_rubrica(rubrica, percorso=PERCORSO_FILE):
    """Salva la rubrica su file JSON."""
    # TODO: apri il file in scrittura e usa json.dump()
    pass

def carica_rubrica(percorso=PERCORSO_FILE):
    """Carica la rubrica da file JSON. Restituisce lista vuota se non esiste."""
    # TODO: prova a leggere il file, se non esiste restituisci []
    pass
```

<details>
<summary>Soluzione Passo 4</summary>

```python
import json
from pathlib import Path

PERCORSO_FILE = Path(__file__).parent / "rubrica.json"

def salva_rubrica(rubrica, percorso=PERCORSO_FILE):
    """Salva la rubrica su file JSON."""
    with open(percorso, 'w', encoding='utf-8') as file:
        json.dump(rubrica, file, ensure_ascii=False, indent=2)
    print(f"Rubrica salvata ({len(rubrica)} contatti)")

def carica_rubrica(percorso=PERCORSO_FILE):
    """Carica la rubrica da file JSON. Restituisce lista vuota se non esiste."""
    try:
        with open(percorso, 'r', encoding='utf-8') as file:
            rubrica = json.load(file)
        print(f"Rubrica caricata ({len(rubrica)} contatti)")
        return rubrica
    except FileNotFoundError:
        print("Nessuna rubrica trovata, ne creo una nuova.")
        return []
    except json.JSONDecodeError:
        print("Errore nel file rubrica. Creo una nuova rubrica.")
        return []
```
</details>

---

## Passo 5: Statistiche sulla rubrica

### Cosa imparerai
- Contare elementi per categoria usando dizionari
- Calcolare percentuali
- Formattare output statistici

### Spiegazione

Aggiungiamo una funzione che mostra statistiche sulla rubrica: quanti contatti per categoria, la categoria piu' numerosa, ecc.

### Suggerimenti
- Usa un dizionario per contare i contatti per categoria
- Puoi usare `dict.get(chiave, 0)` per inizializzare i conteggi
- Calcola la percentuale come `(conteggio / totale) * 100`

### Scheletro di codice

```python
def calcola_statistiche(rubrica):
    """Calcola e restituisce statistiche sulla rubrica."""
    # TODO: conta contatti per categoria
    # TODO: trova la categoria piu' numerosa
    # TODO: restituisci un dizionario con le statistiche
    pass

def stampa_statistiche(rubrica):
    """Stampa le statistiche della rubrica in modo formattato."""
    # TODO: usa calcola_statistiche e formatta l'output
    pass
```

<details>
<summary>Soluzione Passo 5</summary>

```python
def calcola_statistiche(rubrica):
    """Calcola e restituisce statistiche sulla rubrica."""
    if not rubrica:
        return {'totale': 0, 'per_categoria': {}}

    conteggio = {}
    for c in rubrica:
        cat = c['categoria']
        conteggio[cat] = conteggio.get(cat, 0) + 1

    totale = len(rubrica)
    categoria_max = max(conteggio, key=conteggio.get) if conteggio else None

    return {
        'totale': totale,
        'per_categoria': conteggio,
        'categoria_piu_numerosa': categoria_max,
    }

def stampa_statistiche(rubrica):
    """Stampa le statistiche della rubrica in modo formattato."""
    stats = calcola_statistiche(rubrica)

    print("\n--- STATISTICHE RUBRICA ---")
    print(f"  Contatti totali: {stats['totale']}")

    if stats['totale'] > 0:
        print("  Per categoria:")
        for cat, num in stats['per_categoria'].items():
            perc = num / stats['totale'] * 100
            barra = "#" * int(perc / 5)
            print(f"    {cat:<12} {num:>3} ({perc:5.1f}%) {barra}")
        print(f"  Categoria piu' numerosa: {stats['categoria_piu_numerosa']}")
    else:
        print("  Rubrica vuota.")
```
</details>

---

## Passo 6: Versione ad oggetti (OOP)

### Cosa imparerai
- Definire classi con `class`
- Usare `__init__`, `__str__`, `__repr__`
- Incapsulare dati e comportamento in oggetti
- Convertire codice procedurale in codice orientato agli oggetti

### Spiegazione

La Programmazione Orientata agli Oggetti (OOP) organizza il codice in "classi" che raggruppano dati (attributi) e funzioni (metodi). Convertiamo la rubrica procedurale in due classi:

- **Contatto**: rappresenta un singolo contatto
- **Rubrica**: gestisce la collezione di contatti

### Suggerimenti
- `__init__` e' il costruttore: viene chiamato quando crei un nuovo oggetto
- `__str__` definisce come l'oggetto viene stampato con `print()`
- `self` si riferisce all'oggetto corrente
- I metodi della classe `Rubrica` corrispondono alle funzioni del Passo 2

### Scheletro di codice

```python
class Contatto:
    """Rappresenta un singolo contatto nella rubrica."""

    CATEGORIE_VALIDE = ["amico", "lavoro", "famiglia", "altro"]

    def __init__(self, nome, telefono, email, categoria):
        # TODO: valida e assegna gli attributi
        pass

    def __str__(self):
        # TODO: restituisci una rappresentazione leggibile
        pass

    def to_dict(self):
        # TODO: converti in dizionario (utile per JSON)
        pass

    @classmethod
    def from_dict(cls, dati):
        # TODO: crea un Contatto da un dizionario
        pass


class Rubrica:
    """Gestisce una collezione di contatti."""

    def __init__(self, percorso_file=None):
        # TODO: inizializza la lista contatti e il percorso file
        pass

    def aggiungi(self, contatto):
        # TODO: aggiungi un contatto (controlla duplicati)
        pass

    def cerca(self, termine):
        # TODO: cerca per nome
        pass

    def modifica(self, nome, campo, nuovo_valore):
        # TODO: modifica un contatto
        pass

    def elimina(self, nome):
        # TODO: elimina un contatto
        pass

    def salva(self):
        # TODO: salva su file JSON
        pass

    def carica(self):
        # TODO: carica da file JSON
        pass

    def statistiche(self):
        # TODO: restituisci statistiche
        pass
```

<details>
<summary>Soluzione Passo 6</summary>

```python
class Contatto:
    """Rappresenta un singolo contatto nella rubrica."""

    CATEGORIE_VALIDE = ["amico", "lavoro", "famiglia", "altro"]

    def __init__(self, nome, telefono, email, categoria):
        if not nome.strip():
            raise ValueError("Il nome non puo' essere vuoto")
        if not telefono.strip():
            raise ValueError("Il telefono non puo' essere vuoto")
        if categoria not in self.CATEGORIE_VALIDE:
            raise ValueError(f"Categoria non valida: {categoria}")
        self.nome = nome.strip()
        self.telefono = telefono.strip()
        self.email = email.strip()
        self.categoria = categoria

    def __str__(self):
        return (f"{self.nome} | Tel: {self.telefono} | "
                f"Email: {self.email} | Cat: {self.categoria}")

    def __repr__(self):
        return f"Contatto('{self.nome}', '{self.telefono}', '{self.email}', '{self.categoria}')"

    def to_dict(self):
        return {
            'nome': self.nome,
            'telefono': self.telefono,
            'email': self.email,
            'categoria': self.categoria
        }

    @classmethod
    def from_dict(cls, dati):
        return cls(dati['nome'], dati['telefono'], dati['email'], dati['categoria'])


class Rubrica:
    """Gestisce una collezione di contatti."""

    def __init__(self, percorso_file=None):
        self.contatti = []
        self.percorso_file = percorso_file

    def aggiungi(self, contatto):
        for c in self.contatti:
            if c.nome.lower() == contatto.nome.lower():
                print(f"Errore: '{contatto.nome}' esiste gia'.")
                return False
        self.contatti.append(contatto)
        return True

    def cerca(self, termine):
        termine = termine.lower()
        return [c for c in self.contatti if termine in c.nome.lower()]

    def cerca_per_categoria(self, categoria):
        return [c for c in self.contatti if c.categoria == categoria]

    def modifica(self, nome, campo, nuovo_valore):
        for c in self.contatti:
            if c.nome.lower() == nome.lower():
                if hasattr(c, campo):
                    setattr(c, campo, nuovo_valore)
                    return True
        return False

    def elimina(self, nome):
        for i, c in enumerate(self.contatti):
            if c.nome.lower() == nome.lower():
                self.contatti.pop(i)
                return True
        return False

    def salva(self):
        if not self.percorso_file:
            print("Nessun percorso file specificato.")
            return
        dati = [c.to_dict() for c in self.contatti]
        with open(self.percorso_file, 'w', encoding='utf-8') as f:
            json.dump(dati, f, ensure_ascii=False, indent=2)

    def carica(self):
        if not self.percorso_file:
            return
        try:
            with open(self.percorso_file, 'r', encoding='utf-8') as f:
                dati = json.load(f)
            self.contatti = [Contatto.from_dict(d) for d in dati]
        except (FileNotFoundError, json.JSONDecodeError):
            self.contatti = []

    def statistiche(self):
        conteggio = {}
        for c in self.contatti:
            conteggio[c.categoria] = conteggio.get(c.categoria, 0) + 1
        return {'totale': len(self.contatti), 'per_categoria': conteggio}

    def __len__(self):
        return len(self.contatti)

    def __str__(self):
        if not self.contatti:
            return "Rubrica vuota."
        righe = [f"Rubrica ({len(self.contatti)} contatti):"]
        for c in self.contatti:
            righe.append(f"  - {c}")
        return '\n'.join(righe)
```
</details>

---

## Complimenti!

Hai completato il Progetto 2. Ora sai:
- Strutturare dati con dizionari
- Implementare operazioni CRUD
- Creare interfacce a menu con cicli
- Salvare e caricare dati in formato JSON
- Calcolare statistiche su collezioni di dati
- Convertire codice procedurale in classi (OOP)

La soluzione completa e' nel file `soluzione.py`, che include sia la versione procedurale che quella ad oggetti, con una modalita' demo che mostra tutte le funzionalita' senza richiedere input interattivo.
