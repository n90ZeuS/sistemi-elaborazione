# L04 — Funzioni e modularità
# Soluzioni degli esercizi del laboratorio 04
#
# Ogni esercizio corrisponde a un file della traccia (nome tra parentesi).
# Per provarne uno solo, copiatelo in un file a parte.


# ============================================================================
# ESERCIZIO 1: esito dell'esame — esito.py
# ============================================================================
print("--- Esercizio 1: Esito dell'esame ---")
def esito(voto: int, lode: bool = False) -> str:
    """Restituisce l'esito di un esame dato il voto in trentesimi."""
    if voto < 0 or voto > 30:
        return "voto non valido"
    if voto < 18:
        return "respinto"
    if voto == 30 and lode:
        return "30 e lode"
    return f"promosso con {voto}"


print(esito(28))
print(esito(30, lode=True))

appello: list[tuple[str, int, bool]] = [
    ("Anna", 27, False),
    ("Marco", 15, False),
    ("Giulia", 30, True),
    ("Luca", 30, False),
]
for nome, voto, lode in appello:
    print(f"{nome}: {esito(voto, lode)}")
print()


# ============================================================================
# ESERCIZIO 2: media ponderata — media_ponderata.py
# ============================================================================
print("--- Esercizio 2: Media ponderata ---")
def media_ponderata(voti: list[int], cfu: list[int]) -> float:
    """Media pesata con i crediti; 0.0 se i dati non vanno bene."""
    if len(voti) == 0 or len(voti) != len(cfu):
        return 0.0
    somma: int = 0
    for voto, crediti in zip(voti, cfu):
        somma += voto * crediti
    return somma / sum(cfu)


def base_laurea(media: float) -> float:
    """Converte una media in trentesimi in centodecimi."""
    return media * 110 / 30


voti: list[int] = [28, 30, 25, 27, 30, 24]
cfu: list[int] = [9, 6, 12, 6, 9, 6]

ponderata: float = media_ponderata(voti, cfu)
print(f"Media aritmetica: {sum(voti) / len(voti):.2f}")
print(f"Media ponderata: {ponderata:.2f}")
print(f"Base di laurea: {base_laurea(ponderata):.1f}/110")
print()


# ============================================================================
# ESERCIZIO 3: media e varianza a mano — descrittive.py
# ============================================================================
print("--- Esercizio 3: Media e varianza a mano ---")
import statistics


def media(valori: list[float]) -> float:
    """Media aritmetica."""
    return sum(valori) / len(valori)


def varianza(valori: list[float], campionaria: bool = True) -> float:
    """Varianza: divide per n - 1 se campionaria, altrimenti per n."""
    m: float = media(valori)
    somma: float = 0.0
    for x in valori:
        somma += (x - m) ** 2
    if campionaria:
        return somma / (len(valori) - 1)
    return somma / len(valori)


altezze: list[float] = [172.0, 165.5, 180.2, 158.0,
                        175.3, 169.8, 183.1, 162.4]

m: float = media(altezze)
s2: float = varianza(altezze)
p2: float = varianza(altezze, campionaria=False)
print(f"Media: {m:.2f} (statistics: {statistics.mean(altezze):.2f})")
print(f"Varianza campionaria: {s2:.2f} "
      f"(statistics: {statistics.variance(altezze):.2f})")
print(f"Varianza di popolazione: {p2:.2f} "
      f"(statistics: {statistics.pvariance(altezze):.2f})")
print(f"Deviazione standard: {s2 ** 0.5:.2f} "
      f"(statistics: {statistics.stdev(altezze):.2f})")
print()


# ============================================================================
# ESERCIZIO 4: tempi di viaggio — riassunto.py
# ============================================================================
print("--- Esercizio 4: Tempi di viaggio ---")
def mediana(valori: list[float]) -> float:
    """Valore centrale dei dati ordinati."""
    ordinati: list[float] = sorted(valori)
    n: int = len(ordinati)
    meta: int = n // 2
    if n % 2 == 1:
        return ordinati[meta]
    return (ordinati[meta - 1] + ordinati[meta]) / 2


def riassunto(valori: list[float]) -> tuple[float, float, float]:
    """Restituisce minimo, mediana e massimo."""
    return min(valori), mediana(valori), max(valori)


tempi: list[float] = [35, 12, 50, 20, 75, 18, 40, 25]

minimo, centro, massimo = riassunto(tempi)
print(f"Minimo: {minimo:.1f} minuti")
print(f"Mediana: {centro:.1f} minuti")
print(f"Massimo: {massimo:.1f} minuti")
print(f"Campo di variazione: {massimo - minimo:.1f} minuti")
print()


# ============================================================================
# ESERCIZIO 5: quanto manca all'esame — esami_date.py
# ============================================================================
print("--- Esercizio 5: Quanto manca all'esame ---")
from datetime import date

GIORNI: list[str] = ["lunedì", "martedì", "mercoledì", "giovedì",
                     "venerdì", "sabato", "domenica"]


def giorni_mancanti(esame: date, oggi: date) -> int:
    """Giorni tra oggi e la data dell'esame."""
    return (esame - oggi).days


def settimane_e_giorni(giorni: int) -> tuple[int, int]:
    """Divide un numero di giorni in settimane e giorni."""
    return giorni // 7, giorni % 7


def nome_giorno(giorno: date) -> str:
    """Nome italiano del giorno della settimana."""
    return GIORNI[giorno.weekday()]


oggi: date = date(2026, 11, 19)
esami: dict[str, date] = {
    "Analisi 1": date(2027, 1, 18),
    "Statistica 1": date(2027, 1, 28),
    "Sistemi di elaborazione": date(2027, 2, 10),
}
for corso, giorno in esami.items():
    mancano: int = giorni_mancanti(giorno, oggi)
    print(f"{corso}: {nome_giorno(giorno)} {giorno}")
    if mancano < 0:
        print("  esame già passato")
    else:
        s, g = settimane_e_giorni(mancano)
        print(f"  tra {mancano} giorni: {s} settimane e {g} giorni")
print()


# ============================================================================
# ESERCIZIO 6: classifica del corso — classifica.py
# ============================================================================
print("--- Esercizio 6: Classifica del corso ---")
def classifica(
    studenti: list[tuple[str, float, int]],
) -> list[tuple[str, float, int]]:
    """Ordina per media decrescente; a parità di media, per nome."""
    return sorted(studenti, key=lambda s: (-s[1], s[0]))


def in_regola(studenti: list[tuple[str, float, int]],
              cfu_minimi: int = 60) -> list[str]:
    """Nomi di chi ha almeno cfu_minimi crediti."""
    return [s[0] for s in studenti if s[2] >= cfu_minimi]


studenti: list[tuple[str, float, int]] = [
    ("Marco", 26.4, 66),
    ("Anna", 28.1, 54),
    ("Sara", 26.4, 72),
    ("Luca", 24.9, 48),
    ("Giulia", 29.3, 60),
]

for posto, (nome, media, cfu) in enumerate(classifica(studenti), 1):
    print(f"{posto}. {nome}: {media:.1f} ({cfu} CFU)")

piu_cfu: tuple[str, float, int] = max(studenti, key=lambda s: s[2])
print(f"Più crediti: {piu_cfu[0]} con {piu_cfu[2]}")
print(f"In regola con 60 CFU: {in_regola(studenti)}")
print(f"In regola con 70 CFU: {in_regola(studenti, cfu_minimi=70)}")
print()


# ============================================================================
# ESERCIZIO 7: come arrivate in università — questionario.py
# ============================================================================
print("--- Esercizio 7: Come arrivate in università ---")
from collections import Counter


def pulisci(risposte: list[str]) -> list[str]:
    """Toglie spazi e maiuscole e scarta le risposte vuote."""
    return [r.strip().lower() for r in risposte if r.strip() != ""]


def frequenze_relative(risposte: list[str]) -> dict[str, float]:
    """Frequenza relativa di ogni risposta, dalla più comune."""
    conteggi: Counter = Counter(risposte)
    n: int = len(risposte)
    return {r: c / n for r, c in conteggi.most_common()}


def mode(risposte: list[str]) -> list[str]:
    """Risposte più frequenti in ordine alfabetico; [] se vuota."""
    if len(risposte) == 0:
        return []
    conteggi: Counter = Counter(risposte)
    massimo: int = max(conteggi.values())
    return sorted([r for r in conteggi if conteggi[r] == massimo])


grezze: list[str] = ["Bici", " autobus", "treno ", "BICI", "",
                     "a piedi", "Treno", "bici", "Autobus ",
                     "treno", "autobus", "  "]

risposte: list[str] = pulisci(grezze)
print(f"Risposte valide: {len(risposte)} su {len(grezze)}")
for mezzo, quota in frequenze_relative(risposte).items():
    print(f"{mezzo}: {quota:.1%}")
print(f"Moda: {mode(risposte)}")
print()


# ============================================================================
# ESERCIZIO 8: frequentanti e non frequentanti — confronto_gruppi.py
# ============================================================================
print("--- Esercizio 8: Frequentanti e non frequentanti ---")
import statistics


def confronta(a: list[float], b: list[float],
              statistica: callable) -> tuple[float, float, float]:
    """Applica statistica ai gruppi; dà i valori e la differenza."""
    valore_a: float = statistica(a)
    valore_b: float = statistica(b)
    return valore_a, valore_b, valore_a - valore_b


def campo(valori: list[float]) -> float:
    """Campo di variazione: massimo meno minimo."""
    return max(valori) - min(valori)


frequentanti: list[float] = [27, 24, 30, 22, 28, 19, 26, 25, 29, 16]
non_frequentanti: list[float] = [21, 18, 30, 14, 23, 25, 13, 20]

misure: dict[str, callable] = {
    "Media": statistics.mean,
    "Mediana": statistics.median,
    "Deviazione standard": statistics.stdev,
    "Campo di variazione": campo,
    "Minimo": min,
}
for nome, funzione in misure.items():
    f, nf, diff = confronta(frequentanti, non_frequentanti, funzione)
    print(f"{nome}: {f:.2f} contro {nf:.2f} (differenza {diff:.2f})")
print()


# ============================================================================
# SFIDA: compleanni in aula — compleanni.py
# ============================================================================
print("--- Sfida: Compleanni in aula ---")
import random


def compleanno_comune(n: int) -> bool:
    """Estrae n compleanni a caso; True se almeno due coincidono."""
    giorni: list[int] = [random.randint(1, 365) for i in range(n)]
    return len(set(giorni)) < n


def stima(n_studenti: int, prove: int = 10000) -> float:
    """Quota di aule simulate con almeno un compleanno comune."""
    successi: int = 0
    for i in range(prove):
        if compleanno_comune(n_studenti):
            successi += 1
    return successi / prove


def esatta(n_studenti: int) -> float:
    """Probabilità esatta di almeno un compleanno in comune."""
    tutti_diversi: float = 1.0
    for i in range(n_studenti):
        tutti_diversi *= (365 - i) / 365
    return 1 - tutti_diversi


random.seed(2026)
for n in [10, 23, 30, 50]:
    print(f"{n} studenti: simulata {stima(n):.1%}, "
          f"esatta {esatta(n):.1%}")

n_minimo: int = 1
while esatta(n_minimo) < 0.5:
    n_minimo += 1
print(f"Si supera il 50% con {n_minimo} studenti")
print()


# ============================================================================
print("=" * 60)
print("Fine degli esercizi del laboratorio 04")
print("=" * 60)
