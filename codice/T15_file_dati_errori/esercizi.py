# T15 — File, dati, errori
# Esercizi per la lezione frontale 15

import csv
import json
import tempfile
import shutil
from pathlib import Path
from typing import Any

# Creiamo una directory temporanea per tutti gli esercizi
DIR_TEMP: str = tempfile.mkdtemp(prefix="f15_esercizi_")
print(f"Directory temporanea: {DIR_TEMP}\n")

# ============================================================
# ESERCIZIO 1: Calcolatore di statistiche da CSV
# Creare un file CSV programmaticamente, poi leggere i dati e
# calcolare statistiche.
# ============================================================
print("=== Esercizio 1: Statistiche da CSV ===")

# --- Creazione dati di test ---
percorso_voti: Path = Path(DIR_TEMP) / "voti_esame.csv"

dati_voti: list[dict[str, str | int]] = [
    {"studente": "Marco Rossi", "matematica": 28, "fisica": 25, "informatica": 30},
    {"studente": "Laura Bianchi", "matematica": 30, "fisica": 30, "informatica": 29},
    {"studente": "Giulia Verdi", "matematica": 24, "fisica": 22, "informatica": 26},
    {"studente": "Paolo Neri", "matematica": 27, "fisica": 28, "informatica": 27},
    {"studente": "Anna Gialli", "matematica": 30, "fisica": 29, "informatica": 30},
    {"studente": "Luca Blu", "matematica": 22, "fisica": 20, "informatica": 24},
    {"studente": "Sara Rosa", "matematica": 26, "fisica": 27, "informatica": 28},
]

campi: list[str] = ["studente", "matematica", "fisica", "informatica"]
with open(percorso_voti, "w", encoding="utf-8", newline="") as f:
    writer: csv.DictWriter = csv.DictWriter(f, fieldnames=campi)
    writer.writeheader()
    writer.writerows(dati_voti)


# --- Funzioni di analisi ---
def leggi_csv(percorso: Path) -> list[dict[str, str]]:
    """Legge un file CSV e restituisce una lista di dizionari."""
    risultato: list[dict[str, str]] = []
    with open(percorso, "r", encoding="utf-8") as f:
        reader: csv.DictReader = csv.DictReader(f)
        for riga in reader:
            risultato.append(dict(riga))
    return risultato


def statistiche_colonna(
    dati: list[dict[str, str]], colonna: str
) -> dict[str, float]:
    """Calcola statistiche per una colonna numerica."""
    valori: list[float] = [float(riga[colonna]) for riga in dati]
    n: int = len(valori)
    media: float = sum(valori) / n
    varianza: float = sum((x - media) ** 2 for x in valori) / (n - 1)
    return {
        "media": media,
        "minimo": min(valori),
        "massimo": max(valori),
        "varianza": varianza,
        "dev_standard": varianza ** 0.5,
    }


def media_studente(riga: dict[str, str], materie: list[str]) -> float:
    """Calcola la media dei voti di uno studente."""
    voti: list[float] = [float(riga[m]) for m in materie]
    return sum(voti) / len(voti)


# --- Esecuzione ---
dati: list[dict[str, str]] = leggi_csv(percorso_voti)
assert len(dati) == 7

materie: list[str] = ["matematica", "fisica", "informatica"]

print(f"{'Materia':<15} {'Media':>7} {'Min':>5} {'Max':>5} {'Dev.Std':>8}")
print("-" * 42)
for materia in materie:
    stats: dict[str, float] = statistiche_colonna(dati, materia)
    print(f"{materia:<15} {stats['media']:>7.2f} {stats['minimo']:>5.0f} "
          f"{stats['massimo']:>5.0f} {stats['dev_standard']:>8.2f}")

# Verifica
stats_mat: dict[str, float] = statistiche_colonna(dati, "matematica")
assert stats_mat["minimo"] == 22.0
assert stats_mat["massimo"] == 30.0

print(f"\n{'Studente':<20} {'Media':>7}")
print("-" * 29)
for riga in dati:
    m: float = media_studente(riga, materie)
    print(f"{riga['studente']:<20} {m:>7.2f}")

# Migliore studente
migliore: dict[str, str] = max(dati, key=lambda r: media_studente(r, materie))
assert migliore["studente"] == "Laura Bianchi"
print(f"\nMigliore studente: {migliore['studente']} "
      f"(media: {media_studente(migliore, materie):.2f})")

print("Esercizio 1 superato!\n")

# ============================================================
# ESERCIZIO 2: Parser di file di log
# Creare un file di log programmaticamente, poi analizzarlo.
# ============================================================
print("=== Esercizio 2: Parser di log ===")

# --- Creazione dati di test ---
percorso_log: Path = Path(DIR_TEMP) / "applicazione.log"

righe_log: list[str] = [
    "2024-01-15 08:30:00 INFO Applicazione avviata",
    "2024-01-15 08:30:05 INFO Utente marco ha effettuato il login",
    "2024-01-15 08:31:10 WARNING Memoria oltre l'80%",
    "2024-01-15 08:32:00 ERROR Connessione al database fallita",
    "2024-01-15 08:32:05 INFO Riconnessione al database riuscita",
    "2024-01-15 08:45:00 INFO Utente laura ha effettuato il login",
    "2024-01-15 09:00:00 WARNING CPU oltre il 90%",
    "2024-01-15 09:15:00 ERROR Timeout nella richiesta API",
    "2024-01-15 09:15:05 INFO Richiesta API riprovata con successo",
    "2024-01-15 09:30:00 INFO Utente marco ha effettuato il logout",
    "2024-01-15 10:00:00 ERROR Disco quasi pieno",
    "2024-01-15 10:00:05 WARNING Pulizia automatica avviata",
    "2024-01-15 10:05:00 INFO Pulizia completata",
]

with open(percorso_log, "w", encoding="utf-8") as f:
    for riga in righe_log:
        f.write(riga + "\n")


# --- Funzioni di analisi ---
def parse_riga_log(riga: str) -> dict[str, str]:
    """
    Analizza una riga di log nel formato:
    'DATA ORA LIVELLO MESSAGGIO'
    """
    parti: list[str] = riga.strip().split(" ", 3)
    return {
        "data": parti[0],
        "ora": parti[1],
        "livello": parti[2],
        "messaggio": parti[3] if len(parti) > 3 else "",
    }


def analizza_log(percorso: Path) -> dict[str, Any]:
    """Analizza un file di log e produce un riepilogo."""
    conteggio_livelli: dict[str, int] = {}
    eventi: list[dict[str, str]] = []

    with open(percorso, "r", encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if not riga:
                continue
            evento: dict[str, str] = parse_riga_log(riga)
            eventi.append(evento)
            livello: str = evento["livello"]
            conteggio_livelli[livello] = conteggio_livelli.get(livello, 0) + 1

    errori: list[dict[str, str]] = [e for e in eventi if e["livello"] == "ERROR"]
    warnings: list[dict[str, str]] = [e for e in eventi if e["livello"] == "WARNING"]

    return {
        "totale_eventi": len(eventi),
        "conteggio_livelli": conteggio_livelli,
        "errori": errori,
        "warnings": warnings,
    }


# --- Esecuzione ---
analisi: dict[str, Any] = analizza_log(percorso_log)

assert analisi["totale_eventi"] == 13
assert analisi["conteggio_livelli"]["INFO"] == 7
assert analisi["conteggio_livelli"]["WARNING"] == 3
assert analisi["conteggio_livelli"]["ERROR"] == 3

print(f"Totale eventi: {analisi['totale_eventi']}")
print("Conteggio per livello:")
for livello, conteggio in analisi["conteggio_livelli"].items():
    print(f"  {livello}: {conteggio}")

print("\nErrori trovati:")
for errore in analisi["errori"]:
    print(f"  [{errore['ora']}] {errore['messaggio']}")

print("Esercizio 2 superato!\n")

# ============================================================
# ESERCIZIO 3: Pipeline di pulizia dati
# Leggere dati JSON "sporchi", pulirli, e salvarli come CSV pulito.
# ============================================================
print("=== Esercizio 3: Pipeline di pulizia dati ===")

# --- Creazione dati di test (JSON con dati "sporchi") ---
percorso_json_sporco: Path = Path(DIR_TEMP) / "dati_sporchi.json"

dati_sporchi: list[dict[str, Any]] = [
    {"nome": "Marco", "eta": 22, "voto": 28, "email": "marco@uni.it"},
    {"nome": "  Laura  ", "eta": -5, "voto": 30, "email": "laura@uni.it"},
    {"nome": "Giulia", "eta": 21, "voto": 35, "email": "giulia@uni.it"},
    {"nome": "", "eta": 23, "voto": 27, "email": "anonimo@uni.it"},
    {"nome": "Paolo", "eta": 25, "voto": 25, "email": ""},
    {"nome": "Anna", "eta": 20, "voto": 30, "email": "anna@uni.it"},
    {"nome": "Luca", "eta": None, "voto": 28, "email": "luca@uni.it"},
    {"nome": "Sara", "eta": 22, "voto": None, "email": "sara@uni.it"},
    {"nome": "Marco", "eta": 22, "voto": 28, "email": "marco@uni.it"},  # duplicato
]

with open(percorso_json_sporco, "w", encoding="utf-8") as f:
    json.dump(dati_sporchi, f, indent=2, ensure_ascii=False)


# --- Funzioni di pulizia ---
class DatoPulitoError(Exception):
    """Eccezione per dati che non possono essere puliti."""
    pass


def pulisci_stringa(valore: str | None) -> str:
    """Rimuove spazi e verifica che la stringa non sia vuota."""
    if valore is None:
        raise DatoPulitoError("Valore nullo")
    pulito: str = valore.strip()
    if not pulito:
        raise DatoPulitoError("Stringa vuota dopo la pulizia")
    return pulito


def valida_eta(eta: int | None) -> int:
    """Valida che l'età sia un intero positivo ragionevole."""
    if eta is None:
        raise DatoPulitoError("Età mancante")
    if not isinstance(eta, int) or eta < 16 or eta > 100:
        raise DatoPulitoError(f"Età non valida: {eta}")
    return eta


def valida_voto(voto: int | None) -> int:
    """Valida che il voto sia nel range 18-30."""
    if voto is None:
        raise DatoPulitoError("Voto mancante")
    if not isinstance(voto, int) or voto < 18 or voto > 30:
        raise DatoPulitoError(f"Voto non valido: {voto}")
    return voto


def pipeline_pulizia(
    dati: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    """
    Pulisce i dati e restituisce (dati_puliti, log_errori).
    Rimuove anche i duplicati.
    """
    puliti: list[dict[str, Any]] = []
    errori: list[dict[str, str]] = []
    visti: set[str] = set()  # per deduplicazione

    for i, record in enumerate(dati):
        try:
            nome: str = pulisci_stringa(record.get("nome"))
            eta: int = valida_eta(record.get("eta"))
            voto: int = valida_voto(record.get("voto"))
            email: str = pulisci_stringa(record.get("email"))

            # Deduplicazione basata su nome + email
            chiave: str = f"{nome.lower()}_{email.lower()}"
            if chiave in visti:
                errori.append({
                    "riga": str(i),
                    "errore": f"Duplicato: {nome}",
                })
                continue
            visti.add(chiave)

            puliti.append({
                "nome": nome,
                "eta": eta,
                "voto": voto,
                "email": email,
            })
        except DatoPulitoError as e:
            errori.append({
                "riga": str(i),
                "errore": str(e),
            })

    return puliti, errori


# --- Esecuzione ---

# Leggi JSON
with open(percorso_json_sporco, "r", encoding="utf-8") as f:
    dati_letti: list[dict[str, Any]] = json.load(f)

assert len(dati_letti) == 9

# Pulizia
dati_puliti, log_errori = pipeline_pulizia(dati_letti)

print(f"Record originali: {len(dati_letti)}")
print(f"Record puliti: {len(dati_puliti)}")
print(f"Record scartati: {len(log_errori)}")

assert len(dati_puliti) == 2  # Marco(22,28) e Anna(20,30) sono gli unici puliti

print("\nRecord puliti:")
for record in dati_puliti:
    print(f"  {record}")

print("\nErrori di pulizia:")
for errore in log_errori:
    print(f"  Riga {errore['riga']}: {errore['errore']}")

# Salva come CSV pulito
percorso_csv_pulito: Path = Path(DIR_TEMP) / "dati_puliti.csv"
if dati_puliti:
    with open(percorso_csv_pulito, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(dati_puliti[0].keys()))
        writer.writeheader()
        writer.writerows(dati_puliti)
    print(f"\nCSV pulito salvato: {percorso_csv_pulito}")

# Salva log errori
percorso_log_errori: Path = Path(DIR_TEMP) / "errori_pulizia.json"
with open(percorso_log_errori, "w", encoding="utf-8") as f:
    json.dump(log_errori, f, indent=2, ensure_ascii=False)
print(f"Log errori salvato: {percorso_log_errori}")

# Verifica che i dati puliti siano validi
for record in dati_puliti:
    assert isinstance(record["nome"], str) and len(record["nome"]) > 0
    assert isinstance(record["eta"], int) and 16 <= record["eta"] <= 100
    assert isinstance(record["voto"], int) and 18 <= record["voto"] <= 30
    assert isinstance(record["email"], str) and len(record["email"]) > 0

print("Esercizio 3 superato!\n")

# ============================================================
# Pulizia directory temporanea
# ============================================================
shutil.rmtree(DIR_TEMP)
print(f"Directory temporanea rimossa: {DIR_TEMP}")
print("\n=== Tutti gli esercizi T15 completati! ===")
