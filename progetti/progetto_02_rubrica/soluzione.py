"""
Progetto 2: Rubrica contatti
==============================
Questo programma implementa una rubrica contatti con operazioni CRUD,
persistenza su file JSON e interfaccia a menu.
Include sia una versione procedurale che una versione orientata agli oggetti.

Argomenti trattati: F07, F08, F09, F12, F13, F15, F16
"""

import json
from pathlib import Path


# ===========================================================================
# PARTE A: VERSIONE PROCEDURALE (con funzioni)
# ===========================================================================

# Costanti
CATEGORIE_VALIDE = ["amico", "lavoro", "famiglia", "altro"]
PERCORSO_FILE = Path(__file__).parent / "rubrica.json"


# ---------------------------------------------------------------------------
# Passo 1: Struttura dati del contatto
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Passo 2: Operazioni CRUD
# ---------------------------------------------------------------------------

def aggiungi_contatto(rubrica, contatto):
    """Aggiunge un contatto alla rubrica. Restituisce True se aggiunto."""
    for c in rubrica:
        if c['nome'].lower() == contatto['nome'].lower():
            print(f"  Errore: il contatto '{contatto['nome']}' esiste gia'.")
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
        print(f"  Errore: campo '{campo}' non valido. Campi: {campi_validi}")
        return False
    if campo == 'categoria' and nuovo_valore not in CATEGORIE_VALIDE:
        print(f"  Errore: categoria '{nuovo_valore}' non valida.")
        return False
    for c in rubrica:
        if c['nome'].lower() == nome.lower():
            c[campo] = nuovo_valore
            return True
    print(f"  Contatto '{nome}' non trovato.")
    return False


def elimina_contatto(rubrica, nome):
    """Elimina un contatto dalla rubrica. Restituisce True se eliminato."""
    for i, c in enumerate(rubrica):
        if c['nome'].lower() == nome.lower():
            rubrica.pop(i)
            return True
    print(f"  Contatto '{nome}' non trovato.")
    return False


# ---------------------------------------------------------------------------
# Passo 3: Formattazione e stampa
# ---------------------------------------------------------------------------

def formatta_contatto(contatto):
    """Formatta un contatto per la stampa."""
    return (f"  Nome:  {contatto['nome']}\n"
            f"  Tel:   {contatto['telefono']}\n"
            f"  Email: {contatto['email']}\n"
            f"  Cat:   {contatto['categoria']}")


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
            nome = input("  Nome: ")
            telefono = input("  Telefono: ")
            email = input("  Email: ")
            print(f"  Categorie: {CATEGORIE_VALIDE}")
            categoria = input("  Categoria: ")
            try:
                contatto = crea_contatto(nome, telefono, email, categoria)
                if aggiungi_contatto(rubrica, contatto):
                    print(f"  Contatto '{nome}' aggiunto!")
            except ValueError as e:
                print(f"  Errore: {e}")

        elif scelta == "2":
            termine = input("  Cerca per nome: ")
            risultati = cerca_contatti(rubrica, termine)
            if risultati:
                print(f"\n  Trovati {len(risultati)} contatti:")
                for c in risultati:
                    print(formatta_contatto(c))
                    print()
            else:
                print("  Nessun contatto trovato.")

        elif scelta == "3":
            if not rubrica:
                print("  La rubrica e' vuota.")
            else:
                print(f"\n--- Tutti i contatti ({len(rubrica)}) ---")
                for c in rubrica:
                    print(formatta_contatto(c))
                    print()

        elif scelta == "4":
            nome = input("  Nome del contatto da modificare: ")
            campo = input("  Campo (nome/telefono/email/categoria): ")
            nuovo = input(f"  Nuovo valore per '{campo}': ")
            if modifica_contatto(rubrica, nome, campo, nuovo):
                print("  Contatto aggiornato!")

        elif scelta == "5":
            nome = input("  Nome del contatto da eliminare: ")
            if elimina_contatto(rubrica, nome):
                print(f"  Contatto '{nome}' eliminato.")

        elif scelta == "6":
            stampa_statistiche(rubrica)

        elif scelta == "7":
            salva_rubrica(rubrica)
            print("  Arrivederci!")
            break

        else:
            print("  Opzione non valida. Riprova.")


# ---------------------------------------------------------------------------
# Passo 4: Persistenza JSON
# ---------------------------------------------------------------------------

def salva_rubrica(rubrica, percorso=PERCORSO_FILE):
    """Salva la rubrica su file JSON."""
    with open(percorso, 'w', encoding='utf-8') as file:
        json.dump(rubrica, file, ensure_ascii=False, indent=2)
    print(f"  Rubrica salvata ({len(rubrica)} contatti) in {percorso.name}")


def carica_rubrica(percorso=PERCORSO_FILE):
    """Carica la rubrica da file JSON. Restituisce lista vuota se non esiste."""
    try:
        with open(percorso, 'r', encoding='utf-8') as file:
            rubrica = json.load(file)
        print(f"  Rubrica caricata ({len(rubrica)} contatti)")
        return rubrica
    except FileNotFoundError:
        print("  Nessuna rubrica salvata trovata, ne creo una nuova.")
        return []
    except json.JSONDecodeError:
        print("  Errore nel file rubrica. Creo una nuova rubrica.")
        return []


# ---------------------------------------------------------------------------
# Passo 5: Statistiche
# ---------------------------------------------------------------------------

def calcola_statistiche(rubrica):
    """Calcola statistiche sulla rubrica."""
    if not rubrica:
        return {'totale': 0, 'per_categoria': {}}

    conteggio = {}
    for c in rubrica:
        cat = c['categoria']
        conteggio[cat] = conteggio.get(cat, 0) + 1

    categoria_max = max(conteggio, key=conteggio.get) if conteggio else None

    return {
        'totale': len(rubrica),
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


# ===========================================================================
# PARTE B: VERSIONE ORIENTATA AGLI OGGETTI (OOP)
# ===========================================================================

class Contatto:
    """Rappresenta un singolo contatto nella rubrica."""

    CATEGORIE_VALIDE = ["amico", "lavoro", "famiglia", "altro"]

    def __init__(self, nome, telefono, email, categoria):
        """Inizializza un nuovo contatto con validazione dei dati."""
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
        """Rappresentazione leggibile del contatto."""
        return (f"{self.nome} | Tel: {self.telefono} | "
                f"Email: {self.email} | Cat: {self.categoria}")

    def __repr__(self):
        """Rappresentazione tecnica del contatto."""
        return (f"Contatto('{self.nome}', '{self.telefono}', "
                f"'{self.email}', '{self.categoria}')")

    def to_dict(self):
        """Converte il contatto in dizionario (utile per JSON)."""
        return {
            'nome': self.nome,
            'telefono': self.telefono,
            'email': self.email,
            'categoria': self.categoria
        }

    @classmethod
    def from_dict(cls, dati):
        """Crea un Contatto da un dizionario."""
        return cls(
            dati['nome'],
            dati['telefono'],
            dati['email'],
            dati['categoria']
        )


class Rubrica:
    """Gestisce una collezione di contatti con persistenza JSON."""

    def __init__(self, percorso_file=None):
        """Inizializza la rubrica con una lista vuota."""
        self.contatti = []
        self.percorso_file = percorso_file

    def aggiungi(self, contatto):
        """Aggiunge un contatto. Restituisce True se aggiunto, False se duplicato."""
        for c in self.contatti:
            if c.nome.lower() == contatto.nome.lower():
                return False
        self.contatti.append(contatto)
        return True

    def cerca(self, termine):
        """Cerca contatti per nome (parziale, case-insensitive)."""
        termine = termine.lower()
        return [c for c in self.contatti if termine in c.nome.lower()]

    def cerca_per_categoria(self, categoria):
        """Restituisce tutti i contatti di una data categoria."""
        return [c for c in self.contatti if c.categoria == categoria]

    def modifica(self, nome, campo, nuovo_valore):
        """Modifica un campo di un contatto. Restituisce True se trovato."""
        for c in self.contatti:
            if c.nome.lower() == nome.lower():
                if hasattr(c, campo):
                    setattr(c, campo, nuovo_valore)
                    return True
                return False
        return False

    def elimina(self, nome):
        """Elimina un contatto per nome. Restituisce True se eliminato."""
        for i, c in enumerate(self.contatti):
            if c.nome.lower() == nome.lower():
                self.contatti.pop(i)
                return True
        return False

    def salva(self):
        """Salva la rubrica su file JSON."""
        if not self.percorso_file:
            print("  Nessun percorso file specificato.")
            return
        dati = [c.to_dict() for c in self.contatti]
        with open(self.percorso_file, 'w', encoding='utf-8') as f:
            json.dump(dati, f, ensure_ascii=False, indent=2)

    def carica(self):
        """Carica la rubrica da file JSON."""
        if not self.percorso_file:
            return
        try:
            with open(self.percorso_file, 'r', encoding='utf-8') as f:
                dati = json.load(f)
            self.contatti = [Contatto.from_dict(d) for d in dati]
        except (FileNotFoundError, json.JSONDecodeError):
            self.contatti = []

    def statistiche(self):
        """Restituisce un dizionario con le statistiche della rubrica."""
        conteggio = {}
        for c in self.contatti:
            conteggio[c.categoria] = conteggio.get(c.categoria, 0) + 1
        return {
            'totale': len(self.contatti),
            'per_categoria': conteggio
        }

    def __len__(self):
        """Restituisce il numero di contatti."""
        return len(self.contatti)

    def __str__(self):
        """Rappresentazione leggibile della rubrica."""
        if not self.contatti:
            return "Rubrica vuota."
        righe = [f"Rubrica ({len(self.contatti)} contatti):"]
        for c in self.contatti:
            righe.append(f"  - {c}")
        return '\n'.join(righe)


# ===========================================================================
# DEMO: dimostrazione di tutte le funzionalita'
# ===========================================================================

def demo_procedurale():
    """Dimostra tutte le operazioni della versione procedurale."""
    print("=" * 60)
    print("  DEMO: VERSIONE PROCEDURALE")
    print("=" * 60)

    # Crea una rubrica vuota
    rubrica = []

    # --- Aggiunta contatti ---
    print("\n--- Aggiunta contatti ---")
    contatti_da_aggiungere = [
        ("Maria Rossi", "333-1111111", "maria.rossi@email.it", "amico"),
        ("Luca Bianchi", "333-2222222", "luca.bianchi@lavoro.it", "lavoro"),
        ("Anna Verdi", "333-3333333", "anna.verdi@email.it", "famiglia"),
        ("Marco Ferrari", "333-4444444", "marco.ferrari@lavoro.it", "lavoro"),
        ("Giulia Russo", "333-5555555", "giulia.russo@email.it", "amico"),
        ("Paolo Colombo", "333-6666666", "paolo.colombo@email.it", "famiglia"),
        ("Sara Greco", "333-7777777", "sara.greco@email.it", "altro"),
        ("Andrea Conti", "333-8888888", "andrea.conti@lavoro.it", "lavoro"),
    ]
    for nome, tel, email, cat in contatti_da_aggiungere:
        contatto = crea_contatto(nome, tel, email, cat)
        if aggiungi_contatto(rubrica, contatto):
            print(f"  + Aggiunto: {nome} [{cat}]")

    # --- Test duplicato ---
    print("\n--- Test duplicato ---")
    dup = crea_contatto("Maria Rossi", "333-9999999", "dup@email.it", "altro")
    aggiungi_contatto(rubrica, dup)

    # --- Ricerca ---
    print("\n--- Ricerca per nome 'ros' ---")
    risultati = cerca_contatti(rubrica, "ros")
    for c in risultati:
        print(f"  Trovato: {c['nome']} ({c['telefono']})")

    print("\n--- Ricerca per categoria 'lavoro' ---")
    lavoratori = cerca_per_categoria(rubrica, "lavoro")
    for c in lavoratori:
        print(f"  {c['nome']}")

    # --- Modifica ---
    print("\n--- Modifica telefono di Luca Bianchi ---")
    if modifica_contatto(rubrica, "Luca Bianchi", "telefono", "333-0000000"):
        trovato = cerca_contatti(rubrica, "Luca Bianchi")[0]
        print(f"  Nuovo telefono: {trovato['telefono']}")

    # --- Eliminazione ---
    print("\n--- Eliminazione di Sara Greco ---")
    if elimina_contatto(rubrica, "Sara Greco"):
        print(f"  Contatti rimasti: {len(rubrica)}")

    # --- Statistiche ---
    stampa_statistiche(rubrica)

    # --- Salvataggio ---
    percorso_demo = Path(__file__).parent / "rubrica_demo.json"
    print(f"\n--- Salvataggio ---")
    salva_rubrica(rubrica, percorso_demo)

    # --- Ricaricamento ---
    print("\n--- Ricaricamento da file ---")
    rubrica_ricaricata = carica_rubrica(percorso_demo)
    print(f"  Contatti ricaricati: {len(rubrica_ricaricata)}")
    for c in rubrica_ricaricata:
        print(f"  - {c['nome']} ({c['categoria']})")

    return rubrica


def demo_oop():
    """Dimostra tutte le operazioni della versione OOP."""
    print("\n\n" + "=" * 60)
    print("  DEMO: VERSIONE ORIENTATA AGLI OGGETTI (OOP)")
    print("=" * 60)

    # Crea la rubrica con percorso file
    percorso = Path(__file__).parent / "rubrica_oop_demo.json"
    rubrica = Rubrica(percorso_file=percorso)

    # --- Aggiunta contatti ---
    print("\n--- Aggiunta contatti ---")
    contatti = [
        Contatto("Maria Rossi", "333-1111111", "maria.rossi@email.it", "amico"),
        Contatto("Luca Bianchi", "333-2222222", "luca.bianchi@lavoro.it", "lavoro"),
        Contatto("Anna Verdi", "333-3333333", "anna.verdi@email.it", "famiglia"),
        Contatto("Marco Ferrari", "333-4444444", "marco.ferrari@lavoro.it", "lavoro"),
        Contatto("Giulia Russo", "333-5555555", "giulia.russo@email.it", "amico"),
    ]
    for c in contatti:
        if rubrica.aggiungi(c):
            print(f"  + {c}")

    # --- Stampa rubrica (usa __str__) ---
    print(f"\n--- Contenuto rubrica ---")
    print(rubrica)

    # --- Ricerca ---
    print("\n--- Ricerca 'ros' ---")
    for c in rubrica.cerca("ros"):
        print(f"  Trovato: {c}")

    # --- Modifica ---
    print("\n--- Modifica email di Marco Ferrari ---")
    rubrica.modifica("Marco Ferrari", "email", "nuova.email@lavoro.it")
    trovati = rubrica.cerca("Marco Ferrari")
    if trovati:
        print(f"  Aggiornato: {trovati[0]}")

    # --- Eliminazione ---
    print("\n--- Eliminazione di Giulia Russo ---")
    rubrica.elimina("Giulia Russo")
    print(f"  Contatti rimasti: {len(rubrica)}")

    # --- Statistiche ---
    print("\n--- Statistiche ---")
    stats = rubrica.statistiche()
    print(f"  Totale: {stats['totale']}")
    for cat, num in stats['per_categoria'].items():
        print(f"  {cat}: {num}")

    # --- Salvataggio e ricaricamento ---
    print("\n--- Salvataggio su file ---")
    rubrica.salva()
    print(f"  Salvata in: {percorso.name}")

    rubrica2 = Rubrica(percorso_file=percorso)
    rubrica2.carica()
    print(f"\n--- Ricaricamento ---")
    print(rubrica2)

    # --- Dimostrazione __repr__ ---
    print("\n--- Rappresentazione tecnica (repr) ---")
    for c in rubrica2.contatti:
        print(f"  {repr(c)}")


def main():
    """
    Funzione principale.
    Esegue le demo procedurali e OOP.
    Per la versione interattiva, decommentare le righe sotto.
    """
    print("Rubrica Contatti - Progetto 2")
    print("Esecuzione in modalita' demo (senza input interattivo)\n")

    # Demo della versione procedurale
    demo_procedurale()

    # Demo della versione OOP
    demo_oop()

    print("\n" + "=" * 60)
    print("  Demo completata!")
    print("=" * 60)

    # Per usare la versione interattiva con menu, decommentare:
    # rubrica = carica_rubrica()
    # menu_interattivo(rubrica)


if __name__ == "__main__":
    main()
