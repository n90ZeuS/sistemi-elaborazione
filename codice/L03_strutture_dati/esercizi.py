# L03 — Strutture dati
# Soluzioni degli esercizi del laboratorio 03
#
# Ogni esercizio corrisponde a un file della traccia (nome tra parentesi).
# Per provarne uno solo, copiatelo in un file a parte.
# Alcuni programmi leggono i dati con input(): eseguendo il file vengono chiesti uno dopo l'altro.


# ============================================================================
# ESERCIZIO 1: l'appello di statistica — voti_appello.py
# ============================================================================
print("--- Esercizio 1: L'appello di Statistica ---")
SOGLIA: int = 18

testo: str = input("Voti separati da spazi: ")
voti: list[int] = [int(v) for v in testo.split()]
promossi: list[int] = [v for v in voti if v >= SOGLIA]

print(f"Voti ordinati: {sorted(voti)}")
print(f"Presenti: {len(voti)}")
print(f"Media: {sum(voti) / len(voti):.1f}")
print(f"Minimo: {min(voti)}  Massimo: {max(voti)}")
print(f"Promossi: {len(promossi)} ({len(promossi) / len(voti):.1%})")
if len(promossi) > 0:
    media_p: float = sum(promossi) / len(promossi)
    print(f"Media dei promossi: {media_p:.1f}")
print()


# ============================================================================
# ESERCIZIO 2: la coda in mensa — coda_mensa.py
# ============================================================================
print("--- Esercizio 2: La coda in mensa ---")
coda: list[str] = ["Anna", "Bruno", "Carla"]
eventi: list[str] = ["arriva Davide", "servito", "arriva Elena",
                     "esce Bruno", "davanti Franco Elena",
                     "servito", "esce Zeno"]
serviti: list[str] = []

for evento in eventi:
    parti: list[str] = evento.split()
    azione: str = parti[0]
    if azione == "arriva":
        coda.append(parti[1])
    elif azione == "servito":
        if len(coda) > 0:
            serviti.append(coda.pop(0))
        else:
            print("Nessuno da servire")
    elif azione == "esce" and parti[1] in coda:
        coda.remove(parti[1])
    elif azione == "davanti" and parti[2] in coda:
        coda.insert(coda.index(parti[2]), parti[1])
    else:
        print(f"Evento non valido: {evento}")
    print(f"{evento} -> {coda}")

print(f"Serviti: {serviti}")
print(f"Ancora in coda: {len(coda)}")
print()


# ============================================================================
# ESERCIZIO 3: come arrivate in aula — sondaggio.py
# ============================================================================
print("--- Esercizio 3: Come arrivate in aula ---")
from collections import Counter

testo: str = input("Risposte separate da virgole: ")
risposte: list[str] = [r.strip().lower() for r in testo.split(",")]
risposte = [r for r in risposte if r != ""]
conteggio: Counter[str] = Counter(risposte)
totale: int = len(risposte)

print(f"Risposte: {totale}, mezzi diversi: {len(conteggio)}")
for mezzo, n in conteggio.most_common():
    print(f"{mezzo}: {n} ({n / totale:.1%})")
moda: str = conteggio.most_common(1)[0][0]
print(f"Mezzo più usato: {moda}")
print()


# ============================================================================
# ESERCIZIO 4: chi segue cosa — tre_corsi.py
# ============================================================================
print("--- Esercizio 4: Chi segue cosa ---")
from collections import Counter

statistica: set[str] = {"Anna", "Bruno", "Chiara", "Davide",
                        "Elisa", "Fabio", "Giulia"}
analisi: set[str] = {"Anna", "Chiara", "Davide", "Hana",
                     "Ivan", "Giulia"}
informatica: set[str] = {"Bruno", "Chiara", "Giulia", "Ivan",
                         "Luca"}

almeno_uno: set[str] = statistica | analisi | informatica
tutti_tre: set[str] = statistica & analisi & informatica
solo_stat: set[str] = statistica - analisi - informatica
stat_an: set[str] = (statistica & analisi) - informatica

presenze: Counter[str] = Counter(
    list(statistica) + list(analisi) + list(informatica))
un_corso: list[str] = [n for n in presenze if presenze[n] == 1]

print(f"Studenti diversi: {len(almeno_uno)}")
print(f"Tutti e tre i corsi: {sorted(tutti_tre)}")
print(f"Solo Statistica: {sorted(solo_stat)}")
print(f"Statistica e Analisi, non Informatica: {sorted(stat_an)}")
print(f"Un corso soltanto: {sorted(un_corso)}")
print()


# ============================================================================
# ESERCIZIO 5: il libretto — libretto.py
# ============================================================================
print("--- Esercizio 5: Il libretto ---")
libretto: dict[str, tuple[int, int]] = {
    "Analisi 1": (24, 9),
    "Statistica 1": (28, 9),
    "Informatica": (30, 6),
    "Economia politica": (22, 9),
    "Algebra lineare": (27, 6),
}

somma_voti: int = 0
somma_pesata: int = 0
cfu_totali: int = 0
for esame, (voto, cfu) in libretto.items():
    print(f"{esame}: {voto} ({cfu} CFU)")
    somma_voti += voto
    somma_pesata += voto * cfu
    cfu_totali += cfu

media: float = somma_voti / len(libretto)
ponderata: float = somma_pesata / cfu_totali
print(f"CFU totali: {cfu_totali}")
print(f"Media aritmetica: {media:.2f}")
print(f"Media ponderata: {ponderata:.2f}")
print(f"Base di laurea: {ponderata * 110 / 30:.1f}")
print()


# ============================================================================
# ESERCIZIO 6: la sessione invernale — sessione.py
# ============================================================================
print("--- Esercizio 6: La sessione invernale ---")
from collections import defaultdict

esiti: list[tuple[str, str, int]] = [
    ("Anna", "Statistica", 28), ("Anna", "Analisi", 30),
    ("Bruno", "Statistica", 16), ("Bruno", "Analisi", 17),
    ("Bruno", "Informatica", 23), ("Chiara", "Analisi", 25),
    ("Chiara", "Statistica", 30), ("Davide", "Statistica", 21),
    ("Davide", "Informatica", 26), ("Elisa", "Analisi", 12),
]

voti_esame: defaultdict[str, list[int]] = defaultdict(list)
superati: defaultdict[str, list[str]] = defaultdict(list)
studenti: set[str] = set()
for nome, esame, voto in esiti:
    voti_esame[esame].append(voto)
    studenti.add(nome)
    if voto >= 18:
        superati[nome].append(esame)

for esame, voti in voti_esame.items():
    promossi: int = len([v for v in voti if v >= 18])
    print(f"{esame}: {len(voti)} prove, media "
          f"{sum(voti) / len(voti):.1f}, promossi {promossi}")
for nome in sorted(superati):
    print(f"{nome} ha superato {superati[nome]}")
print(f"Nessun esame superato: {sorted(studenti - set(superati))}")
print()


# ============================================================================
# ESERCIZIO 7: scuola di provenienza ed esito — contingenza.py
# ============================================================================
print("--- Esercizio 7: Scuola di provenienza ed esito ---")
from collections import Counter

scuola: list[str] = ["liceo", "tecnico", "liceo", "altro", "liceo",
                     "tecnico", "tecnico", "liceo", "altro",
                     "tecnico", "liceo", "tecnico"]
superato: list[bool] = [True, False, True, False, True, True,
                        False, False, True, False, True, True]

tabella: Counter[tuple[str, bool]] = Counter(zip(scuola, superato))
per_scuola: Counter[str] = Counter(scuola)

for s in sorted(per_scuola):
    si: int = tabella[(s, True)]
    no: int = tabella[(s, False)]
    print(f"{s}: superato {si}, non superato {no}, "
          f"percentuale {si / per_scuola[s]:.1%}")

totale_si: int = superato.count(True)
print(f"Totale: {totale_si} su {len(superato)} "
      f"({totale_si / len(superato):.1%})")
print()


# ============================================================================
# ESERCIZIO 8: ore di studio — descrittive.py
# ============================================================================
print("--- Esercizio 8: Ore di studio ---")
def descrittive(valori: list[float]) -> tuple[float, float, float]:
    """Restituisce media, mediana e deviazione standard."""
    n: int = len(valori)
    media: float = sum(valori) / n
    ordinati: list[float] = sorted(valori)
    if n % 2 == 1:
        mediana: float = ordinati[n // 2]
    else:
        mediana = (ordinati[n // 2 - 1] + ordinati[n // 2]) / 2
    scarti: list[float] = [(x - media) ** 2 for x in valori]
    dev_std: float = (sum(scarti) / (n - 1)) ** 0.5
    return media, mediana, dev_std


ore_studio: dict[str, list[float]] = {
    "Primo anno": [12, 15, 8, 20, 10, 14, 9],
    "Secondo anno": [18, 22, 15, 25, 30, 16],
    "Terzo anno": [20, 8, 35, 12, 28, 6, 14, 25],
}

for anno, ore in ore_studio.items():
    media, mediana, dev_std = descrittive(ore)
    print(f"{anno}: media {media:.1f}, mediana {mediana:.1f}, "
          f"dev. std {dev_std:.2f}")
print()


# ============================================================================
# CHALLENGE MERCATI E FINANZA: il portafoglio — ch_mercati.py
# ============================================================================
print("--- Challenge Mercati e finanza: Il portafoglio ---")
from collections import Counter, defaultdict


def escursione(prezzi: list[float]) -> tuple[float, float]:
    """Restituisce il prezzo minimo e il prezzo massimo."""
    return min(prezzi), max(prezzi)


ordini: list[tuple[str, int, float]] = [
    ("ENRG", 30, 12.40), ("BANK", 20, 8.15), ("TECH", 10, 45.20),
    ("ENRG", 20, 12.10), ("BANK", -5, 8.60), ("TECH", 5, 47.80),
    ("ENRG", -10, 13.05), ("BANK", 10, 8.30), ("TECH", 5, 44.90),
    ("BANK", -5, 8.75),
]

prezzi: defaultdict[str, list[float]] = defaultdict(list)
portafoglio: Counter[str] = Counter()
for titolo, quantita, prezzo in ordini:
    prezzi[titolo].append(prezzo)
    portafoglio[titolo] += quantita

for titolo in sorted(prezzi):
    basso, alto = escursione(prezzi[titolo])
    print(f"{titolo}: {len(prezzi[titolo])} ordini, prezzo da "
          f"{basso:.2f} a {alto:.2f}, "
          f"in portafoglio {portafoglio[titolo]}")
primo, azioni = portafoglio.most_common(1)[0]
print(f"Posizione più grande: {primo} con {azioni} azioni")
vendite: list[tuple[str, int, float]] = [
    o for o in ordini if o[1] < 0]
print(f"Vendite: {len(vendite)} su {len(ordini)} "
      f"({len(vendite) / len(ordini):.1%})")
comprati: set[str] = {o[0] for o in ordini if o[1] > 0}
venduti: set[str] = {o[0] for o in vendite}
print(f"Mai venduti: {sorted(comprati - venduti)}")
print()


# ============================================================================
# CHALLENGE SPORT: il campionato — ch_sport.py
# ============================================================================
print("--- Challenge Sport: Il campionato ---")
from collections import Counter, defaultdict

PUNTI: list[int] = [25, 18, 15, 12]


def bilancio(posizioni: list[int]) -> tuple[int, int]:
    """Restituisce i punti totali e il miglior piazzamento."""
    return sum([PUNTI[p - 1] for p in posizioni]), min(posizioni)


rossa: set[str] = {"Ferri", "Lanza"}
gare: list[tuple[str, str, str, str]] = [
    ("Ferri", "Moro", "Lanza", "Neri"),
    ("Moro", "Ferri", "Neri", "Lanza"),
    ("Ferri", "Lanza", "Moro", "Neri"),
    ("Moro", "Lanza", "Ferri", "Neri"),
    ("Moro", "Neri", "Ferri", "Lanza"),
]

posizioni: defaultdict[str, list[int]] = defaultdict(list)
vittorie: Counter[str] = Counter()
for arrivo in gare:
    vittorie[arrivo[0]] += 1
    for i in range(len(arrivo)):
        posizioni[arrivo[i]].append(i + 1)

for pilota in sorted(posizioni):
    punti, migliore = bilancio(posizioni[pilota])
    print(f"{pilota}: {punti} punti, miglior piazzamento {migliore}")
primo, n = vittorie.most_common(1)[0]
print(f"Più vittorie: {primo} con {n}")
vinte: list[str] = [g[0] for g in gare if g[0] in rossa]
print(f"Gare vinte dalla Scuderia Rossa: {len(vinte)} su {len(gare)} "
      f"({len(vinte) / len(gare):.1%})")
print(f"Senza vittorie: {sorted(set(posizioni) - set(vittorie))}")
print()


# ============================================================================
# CHALLENGE IMPRESE E MARKETING: il negozio online — ch_negozio.py
# ============================================================================
print("--- Challenge Imprese e marketing: Il negozio online ---")
from collections import Counter, defaultdict


def vendite(quantita: list[int]) -> tuple[int, int]:
    """Restituisce il numero di ordini e i pezzi venduti."""
    return len(quantita), sum(quantita)


prezzi: dict[str, float] = {"zaino": 39.90, "borraccia": 12.50,
                            "quaderno": 3.20, "cuffie": 24.90,
                            "lampada": 18.00}
ordini: list[tuple[str, str, int]] = [
    ("Irene", "zaino", 1), ("Tommaso", "quaderno", 5),
    ("Giada", "cuffie", 1), ("Pietro", "borraccia", 2),
    ("Irene", "quaderno", 3), ("Noemi", "zaino", 1),
    ("Tommaso", "borraccia", 1), ("Irene", "cuffie", 1),
    ("Giada", "quaderno", 4), ("Noemi", "borraccia", 2),
]

pezzi: defaultdict[str, list[int]] = defaultdict(list)
clienti: Counter[str] = Counter()
for cliente, prodotto, quantita in ordini:
    pezzi[prodotto].append(quantita)
    clienti[cliente] += 1

for prodotto in sorted(pezzi):
    n, tot = vendite(pezzi[prodotto])
    print(f"{prodotto}: {n} ordini, {tot} pezzi, "
          f"incasso {tot * prezzi[prodotto]:.2f} euro")
primo, n = clienti.most_common(1)[0]
print(f"Cliente più assiduo: {primo} con {n} ordini")
multipli: list[tuple[str, str, int]] = [o for o in ordini if o[2] > 1]
print(f"Ordini con più di un pezzo: {len(multipli)} su "
      f"{len(ordini)} ({len(multipli) / len(ordini):.1%})")
print(f"Mai venduti: {sorted(set(prezzi) - set(pezzi))}")
print()


# ============================================================================
# CHALLENGE SALUTE E SCIENZA: lo studio clinico — ch_salute.py
# ============================================================================
print("--- Challenge Salute e scienza: Lo studio clinico ---")
from collections import Counter, defaultdict


def variazione(differenze: list[int]) -> tuple[int, float]:
    """Restituisce il numero di pazienti e la variazione media."""
    return len(differenze), sum(differenze) / len(differenze)


pazienti: list[tuple[str, str, int, int]] = [
    ("P01", "trattamento", 152, 138), ("P02", "controllo", 148, 145),
    ("P03", "trattamento", 160, 147), ("P04", "controllo", 155, 150),
    ("P05", "trattamento", 145, 140), ("P06", "controllo", 150, 152),
    ("P07", "trattamento", 158, 0), ("P08", "controllo", 149, 138),
    ("P09", "trattamento", 162, 148), ("P10", "controllo", 157, 155),
]

validi: list[tuple[str, str, int, int]] = [
    p for p in pazienti if p[3] > 0]
differenze: defaultdict[str, list[int]] = defaultdict(list)
for codice, gruppo, prima, dopo in validi:
    differenze[gruppo].append(dopo - prima)
migliorati: Counter[str] = Counter(
    [p[1] for p in validi if p[3] - p[2] <= -10])

print(f"Misure valide: {len(validi)} su {len(pazienti)} "
      f"({len(validi) / len(pazienti):.1%})")
persi: set[str] = {p[0] for p in pazienti} - {p[0] for p in validi}
print(f"Senza seconda misura: {sorted(persi)}")
for gruppo in sorted(differenze):
    n, media = variazione(differenze[gruppo])
    print(f"{gruppo}: {n} pazienti, variazione media {media:.1f} "
          f"mmHg, migliorati {migliorati[gruppo]}")
print(f"Migliorati: {sum(migliorati.values())} su {len(validi)}")
gruppo, n = migliorati.most_common(1)[0]
print(f"Gruppo con più migliorati: {gruppo} ({n})")
print()


# ============================================================================
# CHALLENGE CASO E PROBABILITÀ: il tavolo da gioco — ch_probabilita.py
# ============================================================================
print("--- Challenge Caso e probabilità: Il tavolo da gioco ---")
from collections import Counter, defaultdict


def riassunto(somme: list[int]) -> tuple[float, int]:
    """Restituisce la somma media e la somma più alta."""
    return sum(somme) / len(somme), max(somme)


lanci: list[tuple[str, int, int]] = [
    ("Ada", 3, 4), ("Bea", 6, 6), ("Ciro", 2, 5), ("Ada", 1, 3),
    ("Bea", 5, 2), ("Ciro", 4, 4), ("Ada", 6, 5), ("Bea", 3, 1),
    ("Ciro", 6, 2), ("Ada", 2, 2), ("Bea", 4, 3), ("Ciro", 5, 3),
]

somme: defaultdict[str, list[int]] = defaultdict(list)
uscite: Counter[int] = Counter()
for giocatore, d1, d2 in lanci:
    somme[giocatore].append(d1 + d2)
    uscite[d1 + d2] += 1

for giocatore in sorted(somme):
    media, alta = riassunto(somme[giocatore])
    print(f"{giocatore}: somma media {media:.2f}, più alta {alta}")
somma, volte = uscite.most_common(1)[0]
print(f"Somma più uscita: {somma} ({volte} volte)")
doppi: list[tuple[str, int, int]] = [x for x in lanci if x[1] == x[2]]
print(f"Doppi: {len(doppi)} su {len(lanci)} "
      f"({len(doppi) / len(lanci):.1%})")
possibili: set[int] = {a + b for a in range(1, 7)
                       for b in range(1, 7)}
print(f"Somme mai uscite: {sorted(possibili - set(uscite))}")
print()


# ============================================================================
print("=" * 60)
print("Fine degli esercizi del laboratorio 03")
print("=" * 60)
