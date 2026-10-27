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
# CHALLENGE MERCATI E FINANZA: rischio e rendimento — ch_mercati.py
# ============================================================================
print("--- Challenge Mercati e finanza: Rischio e rendimento ---")
import statistics


def rendimenti(prezzi: list[float]) -> list[float]:
    """Rendimenti giornalieri, saltando i prezzi non positivi."""
    p: list[float] = [x for x in prezzi if x > 0]
    return [(p[i] - p[i - 1]) / p[i - 1] for i in range(1, len(p))]


def rischio(rend: list[float]) -> tuple[float, float]:
    """Restituisce media e deviazione standard dei rendimenti."""
    media: float = sum(rend) / len(rend)
    scarti: list[float] = [(r - media) ** 2 for r in rend]
    return media, (sum(scarti) / (len(rend) - 1)) ** 0.5


def valore(azioni: dict[str, int], prezzi: dict[str, list[float]],
           giorno: int = -1) -> float:
    """Valore del portafoglio in un giorno (di default l'ultimo)."""
    return sum([azioni[t] * prezzi[t][giorno] for t in azioni])


portafoglio: dict[str, int] = {"ENRG": 40, "BANK": 20, "TECH": 20}
prezzi: dict[str, list[float]] = {
    "ENRG": [12.40, 12.10, 12.55, 12.80, 0.0, 13.05, 12.90, 13.20],
    "BANK": [8.15, 8.30, 8.60, 8.45, 8.75, 8.70, 8.90, 8.85],
    "TECH": [45.20, 47.80, 44.90, 46.30, 48.10, 45.60, 49.20, 50.10],
}
for titolo, serie in prezzi.items():
    rend: list[float] = rendimenti(serie)
    media, vol = rischio(rend)
    print(f"{titolo}: media {media:.2%}, volatilità {vol:.2%} "
          f"(statistics: {statistics.stdev(rend):.2%})")


print("Più volatile:",
      max(prezzi, key=lambda t: rischio(rendimenti(prezzi[t]))[1]))


primo: float = valore(portafoglio, prezzi, giorno=0)
ultimo: float = valore(portafoglio, prezzi)
print(f"Valore il primo giorno: {primo:.2f} euro")
print(f"Valore l'ultimo giorno: {ultimo:.2f} euro")
print()


# ============================================================================
# CHALLENGE SPORT: il passo gara — ch_sport.py
# ============================================================================
print("--- Challenge Sport: Il passo gara ---")
import statistics


def validi(tempi: list[float], limite: float = 100.0) -> list[float]:
    """Tempi positivi e sotto il limite: niente pit stop."""
    return [t for t in tempi if 0 < t < limite]


def passo(tempi: list[float]) -> tuple[float, float]:
    """Restituisce media e deviazione standard dei tempi."""
    media: float = sum(tempi) / len(tempi)
    scarti: list[float] = [(t - media) ** 2 for t in tempi]
    return media, (sum(scarti) / (len(tempi) - 1)) ** 0.5


def piu_veloce(tempi: dict[str, list[float]]) -> str:
    """Pilota con il passo medio più basso sui giri validi."""
    return min(tempi, key=lambda p: passo(validi(tempi[p]))[0])


tempi: dict[str, list[float]] = {
    "Ferri": [92.8, 92.4, 92.1, 113.6, 92.6, 92.3, 92.9, 93.1],
    "Lanza": [93.2, 92.9, 93.4, 93.0, 114.8, 93.3, 93.6, 93.8],
    "Moro": [92.5, 92.0, 91.8, 92.2, 112.9, 92.1, 92.4, 92.7],
    "Neri": [93.5, 93.9, 115.2, 93.4, 93.7, 94.1, 0.0, 94.3],
}
for pilota, giri in tempi.items():
    buoni: list[float] = validi(giri)
    media, dev = passo(buoni)
    print(f"{pilota}: {len(buoni)} giri validi, "
          f"passo {media:.2f} s, dev. std {dev:.2f} "
          f"(statistics: {statistics.stdev(buoni):.2f})")


print(f"Passo migliore: {piu_veloce(tempi)}")
sotto: dict[str, int] = {p: len(validi(g, limite=93.0))
                         for p, g in tempi.items()}


print(f"Giri sotto 93 secondi: {sotto}")
print()


# ============================================================================
# CHALLENGE IMPRESE E MARKETING: margini e sconti — ch_negozio.py
# ============================================================================
print("--- Challenge Imprese e marketing: Margini e sconti ---")
import statistics

CATALOGO: dict[str, tuple[float, float]] = {
    "zaino": (39.90, 22.00), "borraccia": (12.50, 5.20),
    "quaderno": (3.20, 1.10), "cuffie": (24.90, 14.50),
    "lampada": (18.00, 9.80)}


def valido(prodotto: str, pezzi: int) -> bool:
    """True se il prodotto è in catalogo e i pezzi sono positivi."""
    return prodotto in CATALOGO and pezzi > 0


def bilancio(prodotto: str, pezzi: int,
             sconto: float = 0.0) -> tuple[float, float]:
    """Incasso e margine di un prodotto, con lo sconto sul prezzo."""
    prezzo, costo = CATALOGO[prodotto]
    incasso: float = prezzo * (1 - sconto) * pezzi
    return incasso, incasso - costo * pezzi


def classifica(venduti: dict[str, int]) -> list[str]:
    """Prodotti dal margine più alto al più basso."""
    return sorted(venduti, key=lambda p: -bilancio(p, venduti[p])[1])


venduti: dict[str, int] = {"zaino": 2, "borraccia": 5, "quaderno": 12,
                           "cuffie": 2, "lampada": 3, "penna": 4}


validi: dict[str, int] = {p: n for p, n in venduti.items()
                          if valido(p, n)}


for prodotto in classifica(validi):
    incasso, margine = bilancio(prodotto, validi[prodotto])
    print(f"{prodotto}: incasso {incasso:.2f}, margine {margine:.2f}")


incassi: list[float] = [bilancio(p, n)[0] for p, n in validi.items()]
print(f"Incasso medio: {sum(incassi) / len(incassi):.2f} "
      f"(statistics: {statistics.mean(incassi):.2f})")


incasso, margine = bilancio("zaino", validi["zaino"], sconto=0.2)
print(f"Zaini con lo sconto del 20%: incasso {incasso:.2f}, "
      f"margine {margine:.2f}")
print()


# ============================================================================
# CHALLENGE SALUTE E SCIENZA: le variazioni di pressione — ch_salute.py
# ============================================================================
print("--- Challenge Salute e scienza: Le variazioni di pressione ---")
import statistics


def valido(riga: tuple[str, int, int]) -> bool:
    """True se le due pressioni sono tra 60 e 250 mmHg."""
    return 60 <= riga[1] <= 250 and 60 <= riga[2] <= 250


def descrivi(diff: list[int]) -> tuple[float, float]:
    """Restituisce media e deviazione standard delle variazioni."""
    media: float = sum(diff) / len(diff)
    scarti: list[float] = [(d - media) ** 2 for d in diff]
    return media, (sum(scarti) / (len(diff) - 1)) ** 0.5


def migliorati(diff: list[int], soglia: int = 10) -> float:
    """Quota di pazienti con un calo di almeno soglia mmHg."""
    return len([d for d in diff if d <= -soglia]) / len(diff)


studio: dict[str, list[tuple[str, int, int]]] = {
    "trattamento": [("P01", 152, 138), ("P03", 160, 147),
                    ("P05", 145, 140), ("P07", 158, 0),
                    ("P09", 162, 148), ("P11", 154, 139)],
    "controllo": [("P02", 148, 145), ("P04", 155, 150),
                  ("P06", 150, 152), ("P08", 149, 138),
                  ("P10", 157, 155), ("P12", 15, 146)]}


for gruppo, righe in studio.items():
    ok: list[tuple[str, int, int]] = [r for r in righe if valido(r)]
    diff: list[int] = [d - p for c, p, d in ok]
    media, dev = descrivi(diff)
    print(f"{gruppo}: media {media:.1f} mmHg, dev. std {dev:.2f} "
          f"(statistics: {statistics.stdev(diff):.2f})")
    print(f"  {len(ok)} validi, migliorati {migliorati(diff):.1%}, "
          f"con soglia 5: {migliorati(diff, soglia=5):.1%}")
    print("  calo maggiore:", min(ok, key=lambda r: r[2] - r[1])[0])
print()


# ============================================================================
# CHALLENGE CASO E PROBABILITÀ: tanti lanci — ch_probabilita.py
# ============================================================================
print("--- Challenge Caso e probabilità: Tanti lanci ---")
import random
import statistics


def simula(n: int) -> list[int]:
    """Somme di n lanci di due dadi."""
    return [random.randint(1, 6) + random.randint(1, 6)
            for i in range(n)]


def riassunto(somme: list[int]) -> tuple[float, float]:
    """Restituisce media e deviazione standard delle somme."""
    media: float = sum(somme) / len(somme)
    scarti: list[float] = [(s - media) ** 2 for s in somme]
    return media, (sum(scarti) / (len(somme) - 1)) ** 0.5


def esatta(somma: int, facce: int = 6) -> float:
    """Probabilità esatta di una somma; 0.0 se è impossibile."""
    if somma < 2 or somma > 2 * facce:
        return 0.0
    valori: range = range(1, facce + 1)
    casi: list[tuple[int, int]] = [(a, b) for a in valori
                                   for b in valori if a + b == somma]
    return len(casi) / facce ** 2


random.seed(2026)
for n in [10, 100, 1000, 10000]:
    somme: list[int] = simula(n)
    media, dev = riassunto(somme)
    print(f"{n} lanci: media {media:.2f}, dev. std {dev:.2f} "
          f"(statistics: {statistics.stdev(somme):.2f})")


piu: int = max(range(2, 13), key=lambda s: somme.count(s))
print(f"Somma più frequente: {piu}, "
      f"{somme.count(piu) / len(somme):.1%} dei lanci "
      f"(esatta {esatta(piu):.1%})")


print(f"Somma 5 con due dadi da 4 facce: {esatta(5, facce=4):.1%}")
print()


# ============================================================================
print("=" * 60)
print("Fine degli esercizi del laboratorio 04")
print("=" * 60)
