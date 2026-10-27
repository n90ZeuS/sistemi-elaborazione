# L05 — File e gestione dati
# Soluzioni degli esercizi del laboratorio 05
#
# Ogni esercizio corrisponde a un file della traccia (nome tra parentesi).
# Per provarne uno solo, copiatelo in un file a parte.
# I file di dati usati dagli esercizi sono in questa stessa cartella.
# Alcuni programmi leggono i dati con input(): eseguendo il file vengono chiesti uno dopo l'altro.


# ============================================================================
# ESERCIZIO 1: commenti al corso — conta_righe.py
# ============================================================================
print("--- Esercizio 1: Commenti al corso ---")
from pathlib import Path

percorso: Path = Path("commenti.txt")
righe: int = 0
vuote: int = 0
parole: int = 0
max_parole: int = 0
riga_max: int = 0

with open(percorso, "r", encoding="utf-8") as f:
    for riga in f:
        righe += 1
        n: int = len(riga.split())   # split() ignora anche "\n"
        if n == 0:
            vuote += 1
        parole += n
        if n > max_parole:
            max_parole = n
            riga_max = righe

commenti: int = righe - vuote
print(f"File: {percorso.name}")
print(f"Righe: {righe}, di cui vuote: {vuote}")
print(f"Parole: {parole}")
print(f"Parole per commento: {parole / commenti:.1f}")
print(f"Commento più lungo: riga {riga_max}, {max_parole} parole")
print()


# ============================================================================
# ESERCIZIO 2: le parole più usate — parole_frequenti.py
# ============================================================================
print("--- Esercizio 2: Le parole più usate ---")
from collections import Counter
from pathlib import Path

PUNTEGGIATURA: str = ".,;:!?"
LUNGHEZZA_MINIMA: int = 5

def parole_del_file(percorso: Path) -> list[str]:
    """Parole del file in minuscolo, senza punteggiatura."""
    parole: list[str] = []
    with open(percorso, "r", encoding="utf-8") as f:
        for riga in f:
            for parola in riga.lower().split():
                parole.append(parola.strip(PUNTEGGIATURA))
    return parole

tutte: list[str] = parole_del_file(Path("commenti.txt"))
lunghe: list[str] = [p for p in tutte
                     if len(p) >= LUNGHEZZA_MINIMA]
conteggi: Counter[str] = Counter(lunghe)

print(f"Parole: {len(tutte)}, distinte: {len(set(tutte))}")
print(f"Parole di almeno {LUNGHEZZA_MINIMA} lettere: {len(lunghe)}")
for parola, volte in conteggi.most_common(3):
    print(f"{parola}: {volte}")
print()


# ============================================================================
# ESERCIZIO 3: gli esiti dell'appello — esiti_appello.py
# ============================================================================
print("--- Esercizio 3: Gli esiti dell'appello ---")
import csv
from pathlib import Path

VOTO_MINIMO: int = 18

def leggi_appello(percorso: Path) -> list[dict[str, str]]:
    """Righe del CSV come dizionari (separatore ;)."""
    with open(percorso, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=";"))

studenti: list[dict[str, str]] = leggi_appello(Path("appello.csv"))
voti: list[int] = [int(s["voto"]) for s in studenti]
promossi: list[int] = [v for v in voti if v >= VOTO_MINIMO]
migliore: dict[str, str] = max(studenti,
                               key=lambda s: int(s["voto"]))

print(f"Iscritti: {len(studenti)}")
print(f"Promossi: {len(promossi)} "
      f"({len(promossi) / len(studenti):.1%})")
print(f"Media di tutti: {sum(voti) / len(voti):.1f}")
print(f"Media dei promossi: {sum(promossi) / len(promossi):.1f}")
print(f"Voto più alto: {migliore['voto']} "
      f"({migliore['cognome']} {migliore['nome']})")
print()


# ============================================================================
# ESERCIZIO 4: il verbale d'esame — verbale.py
# ============================================================================
print("--- Esercizio 4: Il verbale d'esame ---")
import csv
from pathlib import Path

VOTO_MINIMO: int = 18

with open(Path("appello.csv"), "r", encoding="utf-8") as f:
    studenti: list[dict[str, str]] = list(
        csv.DictReader(f, delimiter=";"))

ordinati: list[dict[str, str]] = sorted(
    studenti, key=lambda s: s["cognome"])
promossi: int = 0

verbale: Path = Path("verbale.txt")
with open(verbale, "w", encoding="utf-8") as f:
    f.write("Verbale dell'appello\n")
    for s in ordinati:
        voto: int = int(s["voto"])
        esito: str = "respinto"
        if voto >= VOTO_MINIMO:
            esito = "promosso"
            promossi += 1
        f.write(f"{s['matricola']} {s['cognome']} {s['nome']}: "
                f"{voto}, {esito}\n")
    f.write(f"Promossi: {promossi} su {len(studenti)}\n")

print(verbale.read_text(encoding="utf-8"), end="")
print()


# ============================================================================
# ESERCIZIO 5: il registro delle spese — spese.py
# ============================================================================
print("--- Esercizio 5: Il registro delle spese ---")
import csv
from collections import defaultdict
from pathlib import Path

SPESE: Path = Path("spese.csv")

data: str = input("Data (aaaa-mm-gg): ")
categoria: str = input("Categoria: ").strip().lower()
try:
    importo: float = float(input("Importo: "))
except ValueError:
    print("Importo non valido: spesa non registrata")
else:
    with open(SPESE, "a", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter=";").writerow(
            [data, categoria, f"{importo:.2f}"])

totali: defaultdict[str, float] = defaultdict(float)
with open(SPESE, "r", encoding="utf-8") as f:
    for riga in csv.DictReader(f, delimiter=";"):
        totali[riga["categoria"]] += float(riga["importo"])

for cat, totale in sorted(totali.items(),
                          key=lambda c: c[1], reverse=True):
    print(f"{cat}: {totale:.2f} EUR")
print(f"Totale: {sum(totali.values()):.2f} EUR")
print()


# ============================================================================
# ESERCIZIO 6: il sondaggio in json — sondaggio.py
# ============================================================================
print("--- Esercizio 6: Il sondaggio in JSON ---")
import json
from pathlib import Path

def media(valori: list[int]) -> float:
    """Media aritmetica arrotondata a due decimali."""
    return round(sum(valori) / len(valori), 2)

with open(Path("sondaggio.json"), "r", encoding="utf-8") as f:
    dati: dict = json.load(f)

risposte: list[dict] = dati["risposte"]
tutti: list[int] = [r["voto"] for r in risposte]
freq: list[int] = [r["voto"] for r in risposte if r["frequenta"]]
non_freq: list[int] = [r["voto"] for r in risposte
                       if not r["frequenta"]]

riepilogo: dict[str, str | int | float] = {
    "corso": dati["corso"],
    "risposte": len(risposte),
    "media": media(tutti),
    "media_frequentanti": media(freq),
    "media_non_frequentanti": media(non_freq),
    "quota_frequentanti": round(len(freq) / len(risposte), 3),
}
with open(Path("riepilogo.json"), "w", encoding="utf-8") as f:
    json.dump(riepilogo, f, indent=2, ensure_ascii=False)

print(f"{dati['corso']} ({dati['anno']})")
print(f"Risposte: {len(risposte)}")
print("Salvato riepilogo.json:")
print(json.dumps(riepilogo, indent=2, ensure_ascii=False))
print()


# ============================================================================
# ESERCIZIO 7: un appello con errori — appello_robusto.py
# ============================================================================
print("--- Esercizio 7: Un appello con errori ---")
import csv
from pathlib import Path

nome: str = input("File da leggere: ")
voti: list[int] = []
scartate: int = 0

try:
    with open(Path(nome), "r", encoding="utf-8") as f:
        lettore = csv.DictReader(f, delimiter=";")
        for numero, riga in enumerate(lettore, start=2):
            testo: str = riga["voto"]
            try:
                voto: int = int(testo)
            except ValueError:
                print(f"Riga {numero}: voto non valido '{testo}'")
                scartate += 1
                continue
            if voto < 0 or voto > 30:
                print(f"Riga {numero}: voto fuori scala {voto}")
                scartate += 1
            else:
                voti.append(voto)
except FileNotFoundError:
    print(f"Il file {nome} non esiste")
except KeyError:
    print(f"Il file {nome} non ha la colonna voto")
else:
    print(f"Voti validi: {len(voti)}, righe scartate: {scartate}")
    if len(voti) > 0:
        print(f"Media: {sum(voti) / len(voti):.1f}")
print()


# ============================================================================
# ESERCIZIO 8: configurazione in json — config_soglia.py
# ============================================================================
print("--- Esercizio 8: Configurazione in JSON ---")
import csv
import json
from pathlib import Path

def sopra_soglia(file: str, colonna: str,
                 soglia: int) -> list[str]:
    """Cognomi degli studenti con valore >= soglia."""
    cognomi: list[str] = []
    with open(Path(file), "r", encoding="utf-8") as f:
        for riga in csv.DictReader(f, delimiter=";"):
            if int(riga[colonna]) >= soglia:
                cognomi.append(riga["cognome"])
    return cognomi

try:
    with open(Path("config.json"), "r", encoding="utf-8") as f:
        config: dict = json.load(f)
    cognomi: list[str] = sopra_soglia(
        config["file"], config["colonna"], config["soglia"])
except FileNotFoundError as e:
    print(f"File non trovato: {e.filename}")
except json.JSONDecodeError as e:
    print(f"config.json non valido alla riga {e.lineno}")
except KeyError as e:
    print(f"Chiave mancante: {e}")
except ValueError:
    print("La colonna scelta non contiene numeri interi")
else:
    print(f"File: {config['file']}, soglia: {config['soglia']}")
    print(f"Sopra soglia: {len(cognomi)}")
    print(", ".join(sorted(cognomi)))
print()


# ============================================================================
# SFIDA: pm10 a padova — pipeline_pm10.py
# ============================================================================
print("--- Sfida: PM10 a Padova ---")
import csv
import json
from collections import defaultdict
from pathlib import Path

LIMITE: float = 50.0     # limite giornaliero PM10 in µg/m³

def pulisci(percorso: Path) -> tuple[dict[str, list[float]], int]:
    misure: defaultdict[str, list[float]] = defaultdict(list)
    scartate: int = 0
    with open(percorso, "r", encoding="utf-8") as f:
        for riga in csv.DictReader(f, delimiter=";"):
            stazione: str = riga["stazione"].strip().title()
            try:
                pm10: float = float(riga["pm10"].replace(",", "."))
            except ValueError:
                pm10 = -1.0      # illeggibile: verrà scartata
            if stazione == "" or pm10 < 0:
                scartate += 1
            else:
                misure[stazione].append(pm10)
    return misure, scartate

if __name__ == "__main__":
    misure, scartate = pulisci(Path("rilevazioni.csv"))
    report: dict[str, dict[str, float]] = {}
    for stazione, valori in sorted(misure.items()):
        report[stazione] = {
            "media": round(sum(valori) / len(valori), 1),
            "massimo": max(valori),
            "giorni_oltre": len([v for v in valori if v > LIMITE])}
        print(f"{stazione}: {report[stazione]}")
    with open(Path("pm10.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Righe scartate: {scartate}. Salvato pm10.json")
print()


# ============================================================================
print("=" * 60)
print("Fine degli esercizi del laboratorio 05")
print("=" * 60)
