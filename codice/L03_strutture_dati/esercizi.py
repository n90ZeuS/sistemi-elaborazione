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
# SFIDA: compagni di corsi a scelta — compagni.py
# ============================================================================
print("--- Sfida: Compagni di corsi a scelta ---")
def jaccard(a: set[str], b: set[str]) -> float:
    """Elementi in comune diviso elementi totali."""
    return len(a & b) / len(a | b)

scelte: dict[str, set[str]] = {
    "Anna": {"Serie storiche", "Demografia", "Marketing", "R"},
    "Bruno": {"Marketing", "Finanza", "R", "Python"},
    "Chiara": {"Serie storiche", "Demografia", "R", "Biostatistica"},
    "Davide": {"Finanza", "Python", "Econometria"},
    "Elisa": {"Biostatistica", "Demografia", "Python"},
}

nomi: list[str] = sorted(scelte)
coppia: tuple[str, str] = ("", "")
massimo: float = -1.0
for i in range(len(nomi)):
    for j in range(i + 1, len(nomi)):
        s: float = jaccard(scelte[nomi[i]], scelte[nomi[j]])
        if s > massimo:
            massimo, coppia = s, (nomi[i], nomi[j])
print(f"Coppia più simile: {coppia} con {massimo:.2f}")

nome: str = input("Studente: ")
if nome not in scelte:
    print("Studente non trovato")
else:
    simile: str = ""
    massimo = -1.0
    for altro in nomi:
        s = jaccard(scelte[nome], scelte[altro])
        if altro != nome and s > massimo:
            massimo, simile = s, altro
    consigli: set[str] = scelte[simile] - scelte[nome]
    print(f"Più simile: {simile} ({massimo:.2f})")
    print(f"Corsi consigliati: {sorted(consigli)}")
print()


# ============================================================================
print("=" * 60)
print("Fine degli esercizi del laboratorio 03")
print("=" * 60)
