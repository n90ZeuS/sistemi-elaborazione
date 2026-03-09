# F15 — File, dati, errori
# Esempi per la lezione frontale 15

import os
import csv
import json
import tempfile
from pathlib import Path

# Creiamo una directory temporanea per tutti gli esempi
DIR_TEMP: str = tempfile.mkdtemp(prefix="f15_esempi_")
print(f"Directory temporanea: {DIR_TEMP}\n")

# ============================================================
# 1. OPEN() CON CONTEXT MANAGER (with)
# ============================================================
print("=== open() con context manager ===")

# Scrittura di un file di testo
percorso_testo: Path = Path(DIR_TEMP) / "saluto.txt"
with open(percorso_testo, "w", encoding="utf-8") as f:
    f.write("Ciao, mondo!\n")
    f.write("Questa è la seconda riga.\n")
    f.write("E questa è la terza.\n")

print(f"File scritto: {percorso_testo}")

# Lettura completa
with open(percorso_testo, "r", encoding="utf-8") as f:
    contenuto: str = f.read()

assert "Ciao, mondo!" in contenuto
print(f"Contenuto:\n{contenuto}")

# ============================================================
# 2. MODALITÀ DI APERTURA: read, write, append
# ============================================================
print("=== Modalità di apertura ===")

# Append — aggiunge alla fine del file
with open(percorso_testo, "a", encoding="utf-8") as f:
    f.write("Riga aggiunta con append.\n")

with open(percorso_testo, "r", encoding="utf-8") as f:
    righe: list[str] = f.readlines()

assert len(righe) == 4
print(f"Numero di righe dopo append: {len(righe)}")

# ============================================================
# 3. LETTURA RIGA PER RIGA
# ============================================================
print("\n=== Lettura riga per riga ===")

# Metodo 1: iterazione diretta sul file (più efficiente per file grandi)
print("Metodo 1 — iterazione diretta:")
with open(percorso_testo, "r", encoding="utf-8") as f:
    for numero, riga in enumerate(f, start=1):
        print(f"  Riga {numero}: {riga.rstrip()}")

# Metodo 2: readline()
print("Metodo 2 — readline():")
with open(percorso_testo, "r", encoding="utf-8") as f:
    prima_riga: str = f.readline().rstrip()
    seconda_riga: str = f.readline().rstrip()
    print(f"  Prima: {prima_riga}")
    print(f"  Seconda: {seconda_riga}")

# ============================================================
# 4. SCRITTURA E LETTURA CSV
# ============================================================
print("\n=== CSV: scrittura e lettura ===")

# Creiamo un file CSV con dati di studenti
percorso_csv: Path = Path(DIR_TEMP) / "studenti.csv"

studenti: list[dict[str, str | int]] = [
    {"nome": "Marco", "cognome": "Rossi", "voto": 28, "corso": "Informatica"},
    {"nome": "Laura", "cognome": "Bianchi", "voto": 30, "corso": "Matematica"},
    {"nome": "Giulia", "cognome": "Verdi", "voto": 25, "corso": "Informatica"},
    {"nome": "Paolo", "cognome": "Neri", "voto": 27, "corso": "Fisica"},
    {"nome": "Anna", "cognome": "Gialli", "voto": 30, "corso": "Matematica"},
]

# Scrittura CSV con DictWriter
intestazioni: list[str] = ["nome", "cognome", "voto", "corso"]
with open(percorso_csv, "w", encoding="utf-8", newline="") as f:
    writer: csv.DictWriter = csv.DictWriter(f, fieldnames=intestazioni)
    writer.writeheader()
    writer.writerows(studenti)

print(f"CSV scritto: {percorso_csv}")

# Lettura CSV con DictReader
studenti_letti: list[dict[str, str]] = []
with open(percorso_csv, "r", encoding="utf-8") as f:
    reader: csv.DictReader = csv.DictReader(f)
    for riga in reader:
        studenti_letti.append(dict(riga))

assert len(studenti_letti) == 5
assert studenti_letti[0]["nome"] == "Marco"
print(f"Studenti letti dal CSV: {len(studenti_letti)}")
for s in studenti_letti:
    print(f"  {s['nome']} {s['cognome']}: voto={s['voto']}, corso={s['corso']}")

# ============================================================
# 5. JSON: LETTURA E SCRITTURA
# ============================================================
print("\n=== JSON: scrittura e lettura ===")

# Dati da salvare in JSON
configurazione: dict[str, str | int | list[str] | dict[str, bool]] = {
    "app_nome": "StudenteManager",
    "versione": 1,
    "lingue": ["italiano", "inglese"],
    "opzioni": {
        "debug": False,
        "verbose": True,
    },
}

percorso_json: Path = Path(DIR_TEMP) / "config.json"

# Scrittura JSON
with open(percorso_json, "w", encoding="utf-8") as f:
    json.dump(configurazione, f, indent=2, ensure_ascii=False)

print(f"JSON scritto: {percorso_json}")

# Lettura JSON
with open(percorso_json, "r", encoding="utf-8") as f:
    config_letta: dict = json.load(f)

assert config_letta["app_nome"] == "StudenteManager"
assert config_letta["versione"] == 1
assert "italiano" in config_letta["lingue"]
print(f"Configurazione letta: {json.dumps(config_letta, indent=2, ensure_ascii=False)}")

# JSON da/a stringa
dati_json: str = json.dumps({"pi": 3.14159, "e": 2.71828}, indent=2)
print(f"\nJSON come stringa:\n{dati_json}")
dati_parsed: dict[str, float] = json.loads(dati_json)
assert abs(dati_parsed["pi"] - 3.14159) < 1e-5

# ============================================================
# 6. TRY/EXCEPT/ELSE/FINALLY
# ============================================================
print("\n=== try/except/else/finally ===")


def dividi(a: float, b: float) -> float:
    """Divide a per b con gestione degli errori."""
    try:
        risultato: float = a / b
    except ZeroDivisionError:
        print("  ERRORE: divisione per zero!")
        return 0.0
    except TypeError as e:
        print(f"  ERRORE: tipo non valido — {e}")
        return 0.0
    else:
        # Eseguito solo se NON ci sono eccezioni
        print(f"  {a} / {b} = {risultato}")
        return risultato
    finally:
        # Eseguito SEMPRE
        print("  (blocco finally eseguito)")


r1: float = dividi(10, 3)
assert abs(r1 - 10 / 3) < 1e-9

r2: float = dividi(10, 0)
assert r2 == 0.0

# Gestione di file non trovato
print("\nGestione FileNotFoundError:")
try:
    with open("/percorso/inesistente.txt", "r") as f:
        contenuto = f.read()
except FileNotFoundError:
    print("  File non trovato — gestito correttamente!")

# Gestione multipla
print("\nGestione multipla:")


def converti_a_intero(valore: str) -> int | None:
    """Converte una stringa in intero, restituisce None se impossibile."""
    try:
        return int(valore)
    except ValueError:
        print(f"  '{valore}' non è un intero valido")
        return None


assert converti_a_intero("42") == 42
assert converti_a_intero("abc") is None
assert converti_a_intero("3.14") is None

# ============================================================
# 7. ECCEZIONI PERSONALIZZATE
# ============================================================
print("\n=== Eccezioni personalizzate ===")


class VotoNonValidoError(Exception):
    """Eccezione per voti non validi (fuori range 18-30)."""

    def __init__(self, voto: int, messaggio: str = ""):
        self.voto: int = voto
        if not messaggio:
            messaggio = f"Voto {voto} non valido (deve essere tra 18 e 30)"
        super().__init__(messaggio)


def registra_voto(studente: str, voto: int) -> str:
    """Registra un voto, validandolo."""
    if not 18 <= voto <= 30:
        raise VotoNonValidoError(voto)
    return f"Voto {voto} registrato per {studente}"


# Test: voto valido
msg: str = registra_voto("Marco", 28)
assert "28" in msg
print(f"  {msg}")

# Test: voto non valido
try:
    registra_voto("Laura", 15)
except VotoNonValidoError as e:
    print(f"  Errore catturato: {e}")
    assert e.voto == 15

# ============================================================
# 8. PATHLIB — BASI
# ============================================================
print("\n=== pathlib ===")

# Creazione di percorsi
home: Path = Path.home()
print(f"Home: {home}")

percorso: Path = Path(DIR_TEMP) / "sottocartella" / "file.txt"
print(f"Percorso composto: {percorso}")
print(f"  Nome file: {percorso.name}")
print(f"  Estensione: {percorso.suffix}")
print(f"  Directory padre: {percorso.parent}")
print(f"  Esiste? {percorso.exists()}")

# Creazione directory con parents=True
percorso.parent.mkdir(parents=True, exist_ok=True)
percorso.write_text("Contenuto scritto con pathlib.\n", encoding="utf-8")
assert percorso.exists()
assert percorso.read_text(encoding="utf-8") == "Contenuto scritto con pathlib.\n"
print(f"  File creato e verificato con pathlib!")

# Elenco file nella directory temporanea
print(f"\nFile in {DIR_TEMP}:")
for file_path in Path(DIR_TEMP).rglob("*"):
    if file_path.is_file():
        dimensione: int = file_path.stat().st_size
        print(f"  {file_path.name} ({dimensione} bytes)")

# ============================================================
# Pulizia
# ============================================================
import shutil
shutil.rmtree(DIR_TEMP)
print(f"\nDirectory temporanea rimossa: {DIR_TEMP}")

print("\n=== Fine esempi F15 ===")
