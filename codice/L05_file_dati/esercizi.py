# L05 — File e gestione dati
# Esercizi per il laboratorio 05
#
# Esercizi pratici su lettura/scrittura file, CSV, JSON e analisi log.
# I dati di test vengono creati programmaticamente con tempfile.
# Ogni esercizio include assert per verificare la correttezza.

import tempfile
import os
import csv
import json
from typing import Any

# ============================================================================
# ESERCIZIO 1: Contatore di parole da file di testo
# ============================================================================

def conta_parole_file(percorso: str) -> dict[str, int]:
    """
    Legge un file di testo e conta le occorrenze di ogni parola.
    Le parole sono convertite in minuscolo; la punteggiatura viene rimossa.
    """
    frequenze: dict[str, int] = {}

    with open(percorso, "r", encoding="utf-8") as f:
        for riga in f:
            # Rimuovi punteggiatura e converti in minuscolo
            pulita: str = ""
            for c in riga.lower():
                if c.isalnum() or c.isspace():
                    pulita += c
                else:
                    pulita += " "
            for parola in pulita.split():
                frequenze[parola] = frequenze.get(parola, 0) + 1

    return frequenze


def top_parole_file(percorso: str, n: int = 10) -> list[tuple[str, int]]:
    """Restituisce le n parole piu' frequenti da un file."""
    freq: dict[str, int] = conta_parole_file(percorso)
    ordinato: list[tuple[str, int]] = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return ordinato[:n]


def statistiche_file(percorso: str) -> dict[str, int]:
    """
    Calcola statistiche su un file di testo:
    - num_righe, num_parole, num_caratteri, righe_vuote
    """
    num_righe: int = 0
    num_parole: int = 0
    num_caratteri: int = 0
    righe_vuote: int = 0

    with open(percorso, "r", encoding="utf-8") as f:
        for riga in f:
            num_righe += 1
            num_caratteri += len(riga)
            parole: list[str] = riga.split()
            num_parole += len(parole)
            if not riga.strip():
                righe_vuote += 1

    return {
        "num_righe": num_righe,
        "num_parole": num_parole,
        "num_caratteri": num_caratteri,
        "righe_vuote": righe_vuote,
    }


# --- Test contatore parole ---
# Creiamo un file di testo temporaneo per i test
testo_test: str = """Il gatto dorme sul divano.
Il cane corre nel giardino.
Il gatto e il cane sono amici.
Il giardino e' grande e bello.
"""

with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as tmp:
    tmp.write(testo_test)
    percorso_testo: str = tmp.name

try:
    freq_parole: dict[str, int] = conta_parole_file(percorso_testo)
    assert freq_parole["il"] == 5
    assert freq_parole["gatto"] == 2
    assert freq_parole["e"] == 3

    top3: list[tuple[str, int]] = top_parole_file(percorso_testo, 3)
    assert top3[0][0] == "il"  # "il" e' la parola piu' frequente

    stats: dict[str, int] = statistiche_file(percorso_testo)
    assert stats["num_righe"] == 4  # 4 righe di testo
    print("Esercizio 1 (Contatore parole da file): SUPERATO")
finally:
    os.unlink(percorso_testo)


# ============================================================================
# ESERCIZIO 2: Lettore e processore CSV
# ============================================================================

def leggi_csv(percorso: str) -> list[dict[str, str]]:
    """
    Legge un file CSV e restituisce una lista di dizionari.
    Ogni riga diventa un dizionario con le intestazioni come chiavi.
    """
    righe: list[dict[str, str]] = []
    with open(percorso, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for riga in reader:
            righe.append(dict(riga))
    return righe


def filtra_csv(dati: list[dict[str, str]], campo: str, valore: str) -> list[dict[str, str]]:
    """Filtra le righe del CSV dove campo == valore."""
    return [riga for riga in dati if riga.get(campo, "") == valore]


def media_colonna_csv(dati: list[dict[str, str]], colonna: str) -> float:
    """Calcola la media di una colonna numerica del CSV."""
    valori: list[float] = []
    for riga in dati:
        if colonna in riga and riga[colonna]:
            valori.append(float(riga[colonna]))
    if not valori:
        raise ValueError(f"Nessun valore numerico nella colonna '{colonna}'")
    return round(sum(valori) / len(valori), 2)


def scrivi_csv(percorso: str, dati: list[dict[str, str]], intestazioni: list[str]) -> None:
    """Scrive dati in formato CSV."""
    with open(percorso, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=intestazioni)
        writer.writeheader()
        writer.writerows(dati)


# --- Test CSV ---
# Creiamo un file CSV temporaneo con dati studenti
csv_contenuto: str = """nome,cognome,voto,materia
Alice,Rossi,28,Matematica
Bob,Bianchi,22,Informatica
Carla,Verdi,30,Matematica
Davide,Neri,25,Informatica
Eva,Gialli,18,Matematica
Fabio,Blu,27,Informatica
"""

with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as tmp:
    tmp.write(csv_contenuto)
    percorso_csv: str = tmp.name

try:
    dati_csv: list[dict[str, str]] = leggi_csv(percorso_csv)
    assert len(dati_csv) == 6
    assert dati_csv[0]["nome"] == "Alice"
    assert dati_csv[0]["voto"] == "28"

    # Filtra per materia
    matematica: list[dict[str, str]] = filtra_csv(dati_csv, "materia", "Matematica")
    assert len(matematica) == 3
    assert all(r["materia"] == "Matematica" for r in matematica)

    # Media voti
    media_voti: float = media_colonna_csv(dati_csv, "voto")
    assert media_voti == 25.0  # (28+22+30+25+18+27)/6 = 150/6 = 25.0

    media_mat: float = media_colonna_csv(matematica, "voto")
    assert abs(media_mat - 25.33) < 0.01  # (28+30+18)/3

    # Scrivi e rileggi CSV
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as tmp2:
        percorso_csv_out: str = tmp2.name

    scrivi_csv(percorso_csv_out, dati_csv, ["nome", "cognome", "voto", "materia"])
    dati_riletti: list[dict[str, str]] = leggi_csv(percorso_csv_out)
    assert len(dati_riletti) == 6
    assert dati_riletti[0]["nome"] == "Alice"
    os.unlink(percorso_csv_out)

    print("Esercizio 2 (CSV): SUPERATO")
finally:
    os.unlink(percorso_csv)


# ============================================================================
# ESERCIZIO 3: Loader/Saver di configurazione JSON
# ============================================================================

def carica_json(percorso: str) -> dict[str, Any]:
    """
    Carica un file JSON e restituisce il dizionario corrispondente.
    Gestisce errori di file non trovato e JSON malformato.
    """
    try:
        with open(percorso, "r", encoding="utf-8") as f:
            dati: dict[str, Any] = json.load(f)
        return dati
    except FileNotFoundError:
        raise FileNotFoundError(f"File non trovato: {percorso}")
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON malformato in {percorso}: {e}")


def salva_json(percorso: str, dati: dict[str, Any], indentazione: int = 2) -> None:
    """Salva un dizionario in formato JSON con indentazione leggibile."""
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=indentazione, ensure_ascii=False)


def aggiorna_config(
    percorso: str, chiave: str, valore: Any
) -> dict[str, Any]:
    """
    Carica una configurazione JSON, aggiorna un campo e salva.
    Supporta chiavi annidate con notazione puntata (es. "database.host").
    """
    config: dict[str, Any] = carica_json(percorso)

    # Supporto per chiavi annidate
    parti: list[str] = chiave.split(".")
    d: dict[str, Any] = config
    for parte in parti[:-1]:
        if parte not in d or not isinstance(d[parte], dict):
            d[parte] = {}
        d = d[parte]
    d[parti[-1]] = valore

    salva_json(percorso, config)
    return config


# --- Test JSON ---
config_test: dict[str, Any] = {
    "app": {
        "nome": "MioProgetto",
        "versione": "1.0.0",
        "debug": False,
    },
    "database": {
        "host": "localhost",
        "porta": 5432,
        "nome_db": "test_db",
    },
    "utenti_max": 100,
}

with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as tmp:
    json.dump(config_test, tmp, indent=2)
    percorso_json: str = tmp.name

try:
    # Carica
    config_caricata: dict[str, Any] = carica_json(percorso_json)
    assert config_caricata["app"]["nome"] == "MioProgetto"
    assert config_caricata["database"]["porta"] == 5432
    assert config_caricata["utenti_max"] == 100

    # Aggiorna campo semplice
    aggiorna_config(percorso_json, "utenti_max", 200)
    config_aggiornata: dict[str, Any] = carica_json(percorso_json)
    assert config_aggiornata["utenti_max"] == 200

    # Aggiorna campo annidato
    aggiorna_config(percorso_json, "database.host", "192.168.1.1")
    config_aggiornata = carica_json(percorso_json)
    assert config_aggiornata["database"]["host"] == "192.168.1.1"

    # Salva e ricarica
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as tmp2:
        percorso_json_out: str = tmp2.name

    salva_json(percorso_json_out, config_caricata)
    ricaricato: dict[str, Any] = carica_json(percorso_json_out)
    assert ricaricato["app"]["versione"] == "1.0.0"
    os.unlink(percorso_json_out)

    # Test file non trovato
    errore_file: bool = False
    try:
        carica_json("/percorso/inesistente.json")
    except FileNotFoundError:
        errore_file = True
    assert errore_file

    print("Esercizio 3 (JSON): SUPERATO")
finally:
    os.unlink(percorso_json)


# ============================================================================
# ESERCIZIO 4: Analizzatore di log
# ============================================================================

def analizza_log(percorso: str) -> dict[str, Any]:
    """
    Analizza un file di log con formato:
    TIMESTAMP | LIVELLO | MESSAGGIO

    Restituisce statistiche:
    - totale_righe: numero totale di righe
    - per_livello: conteggio per livello (INFO, WARNING, ERROR, DEBUG)
    - errori: lista dei messaggi di errore
    - percentuale_errori: percentuale di righe ERROR sul totale
    """
    totale: int = 0
    per_livello: dict[str, int] = {"INFO": 0, "WARNING": 0, "ERROR": 0, "DEBUG": 0}
    errori: list[str] = []

    with open(percorso, "r", encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if not riga:
                continue

            totale += 1
            parti: list[str] = riga.split(" | ")
            if len(parti) >= 3:
                livello: str = parti[1].strip()
                messaggio: str = parti[2].strip()

                if livello in per_livello:
                    per_livello[livello] += 1

                if livello == "ERROR":
                    errori.append(messaggio)

    percentuale_errori: float = round(
        (per_livello["ERROR"] / totale * 100) if totale > 0 else 0.0, 2
    )

    return {
        "totale_righe": totale,
        "per_livello": per_livello,
        "errori": errori,
        "percentuale_errori": percentuale_errori,
    }


def filtra_log_per_livello(percorso_input: str, percorso_output: str, livello: str) -> int:
    """
    Filtra le righe del log per livello e le scrive in un nuovo file.
    Restituisce il numero di righe filtrate.
    """
    conteggio: int = 0
    with open(percorso_input, "r", encoding="utf-8") as fin:
        with open(percorso_output, "w", encoding="utf-8") as fout:
            for riga in fin:
                parti: list[str] = riga.split(" | ")
                if len(parti) >= 2 and parti[1].strip() == livello:
                    fout.write(riga)
                    conteggio += 1
    return conteggio


# --- Test analizzatore log ---
log_contenuto: str = """2024-01-15 10:00:01 | INFO | Applicazione avviata
2024-01-15 10:00:05 | DEBUG | Connessione al database stabilita
2024-01-15 10:01:12 | INFO | Utente 'admin' ha effettuato il login
2024-01-15 10:02:30 | WARNING | Memoria disponibile sotto il 20%
2024-01-15 10:03:45 | ERROR | Impossibile connettersi al servizio esterno
2024-01-15 10:04:00 | INFO | Retry connessione in corso
2024-01-15 10:04:15 | ERROR | Timeout nella risposta del servizio
2024-01-15 10:05:00 | INFO | Connessione ristabilita
2024-01-15 10:06:30 | WARNING | Disco quasi pieno (90% utilizzato)
2024-01-15 10:10:00 | INFO | Report giornaliero generato
"""

with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False, encoding="utf-8") as tmp:
    tmp.write(log_contenuto)
    percorso_log: str = tmp.name

try:
    risultato_log: dict[str, Any] = analizza_log(percorso_log)

    assert risultato_log["totale_righe"] == 10
    assert risultato_log["per_livello"]["INFO"] == 5
    assert risultato_log["per_livello"]["WARNING"] == 2
    assert risultato_log["per_livello"]["ERROR"] == 2
    assert risultato_log["per_livello"]["DEBUG"] == 1
    assert len(risultato_log["errori"]) == 2
    assert risultato_log["percentuale_errori"] == 20.0

    # Test filtro per livello
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False, encoding="utf-8") as tmp2:
        percorso_errori: str = tmp2.name

    num_filtrate: int = filtra_log_per_livello(percorso_log, percorso_errori, "ERROR")
    assert num_filtrate == 2

    # Verifica che il file filtrato contenga solo errori
    with open(percorso_errori, "r", encoding="utf-8") as f:
        righe_errori: list[str] = f.readlines()
    assert len(righe_errori) == 2
    assert all("ERROR" in r for r in righe_errori)

    os.unlink(percorso_errori)
    print("Esercizio 4 (Analizzatore log): SUPERATO")
finally:
    os.unlink(percorso_log)


# ============================================================================
print("\n" + "=" * 60)
print("TUTTI GLI ESERCIZI DEL LABORATORIO 05 SUPERATI!")
print("=" * 60)
