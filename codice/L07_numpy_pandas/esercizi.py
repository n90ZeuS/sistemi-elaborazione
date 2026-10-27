# L07 — NumPy e Pandas
# Soluzioni degli esercizi del laboratorio 07
#
# Ogni esercizio corrisponde a un file della traccia (nome tra parentesi).
# Per provarne uno solo, copiatelo in un file a parte.
# I file di dati usati dagli esercizi sono in questa stessa cartella.


# ============================================================================
# ESERCIZIO 1: i voti in un array — voti_numpy.py
# ============================================================================
print("--- Esercizio 1: I voti in un array ---")
import numpy as np

voti: np.ndarray = np.array([28, 17, 30, 24, 15, 21, 27, 19, 30, 23])

print(f"Forma: {voti.shape}, tipo: {voti.dtype}")
media: float = np.mean(voti)
print(f"Media: {media:.1f}, mediana: {np.median(voti):.1f}")
print(f"Dev. std campionaria: {np.std(voti, ddof=1):.2f}")

promossi: np.ndarray = voti[voti >= 18]       # filtro booleano
quota: float = np.sum(voti >= 18) / voti.size  # True conta 1
print(f"Promossi: {promossi.size} su {voti.size} ({quota:.1%})")
print(f"Voti dei promossi: {promossi}")
print(f"Media dei promossi: {np.mean(promossi):.1f}")

scarti: np.ndarray = voti - media              # senza cicli
print(f"Scarti dalla media: {np.round(scarti, 1)}")
print(f"Somma degli scarti: {np.sum(scarti):.1f}")
print()


# ============================================================================
# ESERCIZIO 2: le ore di studio — ore_studio.py
# ============================================================================
print("--- Esercizio 2: Le ore di studio ---")
import numpy as np

corsi: list[str] = ["Statistica", "Analisi", "Informatica"]
# righe = settimane, colonne = corsi
ore: np.ndarray = np.array([[6, 4, 3],
                            [8, 5, 2],
                            [5, 7, 4],
                            [10, 6, 5]])

print(f"Forma: {ore.shape}, ore totali: {np.sum(ore)}")
per_corso: np.ndarray = np.sum(ore, axis=0)
per_settimana: np.ndarray = np.sum(ore, axis=1)
print(f"Ore per corso: {per_corso}")
print(f"Ore per settimana: {per_settimana}")

quote: np.ndarray = per_corso / np.sum(ore)    # array / scalare
for corso, q in zip(corsi, quote):
    print(f"{corso}: {q:.1%}")

settimane: np.ndarray = np.arange(1, ore.shape[0] + 1)
print(f"Settimane oltre 15 ore: {settimane[per_settimana > 15]}")

medie: np.ndarray = np.mean(ore, axis=0)
print(f"Medie per corso: {medie}")
print("Scarti dalla media del corso:")
print(ore - medie)                             # broadcasting
print()


# ============================================================================
# ESERCIZIO 3: altezze simulate — altezze.py
# ============================================================================
print("--- Esercizio 3: Altezze simulate ---")
import numpy as np

SEED: int = 42
N: int = 500

rng = np.random.default_rng(SEED)
altezze: np.ndarray = rng.normal(loc=170, scale=10, size=N)
print(f"Prime 5 altezze: {np.round(altezze[:5], 1)}")

media: float = np.mean(altezze)
dev: float = np.std(altezze, ddof=1)
print(f"Media: {media:.1f} cm, dev. std: {dev:.1f} cm")
print(f"Minimo: {np.min(altezze):.1f}, "
      f"massimo: {np.max(altezze):.1f}")

z: np.ndarray = (altezze - media) / dev        # z-score
print(f"Dev. std degli z: {np.std(z, ddof=1):.2f}")

entro_1: float = np.mean(np.abs(z) <= 1)       # quota di True
oltre_2: float = np.mean(np.abs(z) > 2)
print(f"Entro 1 dev. std: {entro_1:.1%} (teorica 68.3%)")
print(f"Oltre 2 dev. std: {oltre_2:.1%} (teorica 4.6%)")

alti: np.ndarray = altezze[(altezze >= 185) & (altezze < 195)]
print(f"Tra 185 e 195 cm: {alti.size}")
print()


# ============================================================================
# ESERCIZIO 4: rispondere a caso — test_crocette.py
# ============================================================================
print("--- Esercizio 4: Rispondere a caso ---")
import math
import numpy as np

DOMANDE: int = 10
P: float = 0.25          # 4 opzioni, una giusta
SOGLIA: int = 6          # risposte giuste per superare il test
N: int = 100_000         # studenti simulati

rng = np.random.default_rng(2027)
# l'opzione 0 è quella giusta: ogni riga è uno studente
risposte: np.ndarray = rng.integers(0, 4, size=(N, DOMANDE))
giuste: np.ndarray = np.sum(risposte == 0, axis=1)
print(f"Giuste dei primi 5 studenti: {giuste[:5]}")
print(f"Media di risposte giuste: {np.mean(giuste):.2f} "
      f"(teorica {DOMANDE * P:.2f})")
print(f"Nessuna risposta giusta: {np.mean(giuste == 0):.1%}")
print(f"Test superato (simulato): {np.mean(giuste >= SOGLIA):.2%}")

binom: np.ndarray = rng.binomial(n=DOMANDE, p=P, size=N)
print(f"Test superato (binomiale): {np.mean(binom >= SOGLIA):.2%}")
esatta: float = sum([math.comb(DOMANDE, k) * P**k
                     * (1 - P)**(DOMANDE - k)
                     for k in range(SOGLIA, DOMANDE + 1)])
print(f"Test superato (esatta): {esatta:.2%}")

punteggio: np.ndarray = giuste - (DOMANDE - giuste) / 3
print(f"Punteggio medio con penalità: {np.mean(punteggio):.2f}")
print(f"Punteggio negativo: {np.mean(punteggio < 0):.1%}")
print()


# ============================================================================
# ESERCIZIO 5: il libretto in un dataframe — libretto.py
# ============================================================================
print("--- Esercizio 5: Il libretto in un DataFrame ---")
import pandas as pd

libretto: pd.DataFrame = pd.DataFrame({
    "esame": ["Analisi I", "Statistica I", "Informatica",
              "Economia", "Probabilità", "Demografia"],
    "anno": [1, 1, 1, 1, 2, 2],
    "crediti": [9, 9, 6, 9, 9, 6],
    "voto": [24, 28, 30, 22, 26, 27],
})
print(libretto)
print(f"Righe e colonne: {libretto.shape}")

libretto["pesato"] = libretto["voto"] * libretto["crediti"]
crediti: int = libretto["crediti"].sum()
media: float = libretto["voto"].mean()
ponderata: float = libretto["pesato"].sum() / crediti
print(f"Crediti: {crediti}")
print(f"Media aritmetica: {media:.2f}, ponderata: {ponderata:.2f}")
print(f"Base di laurea: {ponderata / 30 * 110:.1f}")

migliori: pd.DataFrame = libretto[libretto["voto"] >= 26]
migliori = migliori.sort_values("voto", ascending=False)
print(migliori[["esame", "voto"]])
primo: pd.DataFrame = libretto[(libretto["anno"] == 1)
                               & (libretto["crediti"] == 9)]
print(f"Esami da 9 crediti del primo anno: {len(primo)}")
print()


# ============================================================================
# ESERCIZIO 6: esplorare un csv — esami_csv.py
# ============================================================================
print("--- Esercizio 6: Esplorare un CSV ---")
import pandas as pd

esami: pd.DataFrame = pd.read_csv("esami.csv", sep=";")
print(esami.head(3))
print(f"Righe e colonne: {esami.shape}")
print(f"Colonne: {esami.columns.tolist()}")
print(esami["voto"].describe().round(1))
print(esami["corso"].value_counts())

promossi: pd.DataFrame = esami[esami["voto"] >= 18]
print(f"Promossi: {len(promossi)} su {len(esami)}")
stat_2: pd.DataFrame = esami[(esami["corso"] == "Statistica")
                             & (esami["anno"] == 2)]
print(f"Statistica, secondo anno: {stat_2['matricola'].tolist()}")
print(esami.groupby("corso")["voto"].mean().round(1))
print()


# ============================================================================
# ESERCIZIO 7: pulire un questionario — pulizia_questionario.py
# ============================================================================
print("--- Esercizio 7: Pulire un questionario ---")
import pandas as pd

q: pd.DataFrame = pd.read_csv("questionario.csv", sep=";",
                              na_values=["", "NA", "?"])
print(f"Righe lette: {len(q)}")
print("Valori mancanti per colonna:")
print(q.isna().sum())

doppi: int = q.duplicated().sum()
q = q.drop_duplicates()
print(f"Righe duplicate tolte: {doppi}")

senza_voto: int = q["voto"].isna().sum()
q = q.dropna(subset=["voto"])
print(f"Righe senza voto tolte: {senza_voto}")

media_ore: float = q["ore_studio"].mean()
q = q.fillna({"ore_studio": round(media_ore, 1)})
q["voto"] = q["voto"].astype(int)
print(f"Ore mancanti sostituite con la media: {media_ore:.1f}")

print(f"Righe pulite: {len(q)}, mancanti: {q.isna().sum().sum()}")
print(f"Voto medio: {q['voto'].mean():.2f}")
print(f"Ore medie: {q['ore_studio'].mean():.2f}")
print(q.groupby("corso")[["ore_studio", "voto"]].mean().round(1))
print()


# ============================================================================
# ESERCIZIO 8: gli esami del primo anno — esami_primo_anno.py
# ============================================================================
print("--- Esercizio 8: Gli esami del primo anno ---")
import numpy as np
import pandas as pd

N: int = 150
CORSI: list[str] = ["Analisi", "Statistica", "Informatica"]

rng = np.random.default_rng(2026)
voti: np.ndarray = np.round(rng.normal(23, 5, size=N))
esami: pd.DataFrame = pd.DataFrame({
    "corso": rng.choice(CORSI, size=N),
    "voto": np.minimum(voti, 30).astype(int),
})
corsi: pd.DataFrame = pd.DataFrame({
    "corso": ["Analisi", "Statistica", "Informatica", "Economia"],
    "crediti": [9, 9, 6, 9],
})
print(f"Esami: {len(esami)}, voti 30: {np.sum(esami['voto'] == 30)}")

esami["promosso"] = esami["voto"] >= 18
for corso, quota in esami.groupby("corso")["promosso"].mean().items():
    print(f"{corso}: promossi {quota:.1%}")

promossi: pd.DataFrame = (
    esami
    .merge(corsi, on="corso", how="left")
    .query("promosso")
)
print(f"Crediti acquisiti: {promossi['crediti'].sum()}")
riepilogo: pd.DataFrame = (
    promossi
    .groupby("corso")["voto"]
    .agg(["count", "mean", "min", "max"])
    .round(1)
)
print(riepilogo)
print()


# ============================================================================
# CHALLENGE MERCATI E FINANZA: il portafoglio simulato — ch_mercati.py
# ============================================================================
print("--- Challenge Mercati e finanza: Il portafoglio simulato ---")
import numpy as np
import pandas as pd

TITOLI: list[str] = ["ENRG", "BANK", "TECH"]
MEDIE: np.ndarray = np.array([0.001, 0.0005, 0.002])
VOL: np.ndarray = np.array([0.012, 0.009, 0.025])
PESI: np.ndarray = np.array([0.3, 0.5, 0.2])
GIORNI: int = 20
N: int = 10_000

rng = np.random.default_rng(7)
# righe = giorni, colonne = titoli
rend: np.ndarray = rng.normal(MEDIE, VOL, size=(GIORNI, 3))
vol: np.ndarray = np.std(rend, axis=0, ddof=1)
for titolo, v in zip(TITOLI, vol):
    print(f"Volatilità {titolo}: {v:.2%}")
port: np.ndarray = np.sum(rend * PESI, axis=1)   # broadcasting
valore: float = 10_000 * np.prod(1 + port)
print(f"Valore finale di 10000 EUR: {valore:.2f} EUR")
print(f"Giorni in perdita: {np.sum(port < 0)} su {GIORNI}")
print(f"Peggior giorno: {np.min(port):.2%}")

sim: np.ndarray = rng.normal(MEDIE[2], VOL[2], size=(N, GIORNI))
mese: np.ndarray = np.sum(sim, axis=1)
perdita: float = np.mean(mese < -0.05)
print(f"P(TECH perde più del 5% in un mese): {perdita:.1%}")

df: pd.DataFrame = pd.DataFrame(rend, columns=TITOLI)
df["settimana"] = np.arange(GIORNI) // 5 + 1
df["portafoglio"] = port
medie_sett: pd.Series = df.groupby("settimana")["portafoglio"].mean()
for sett, m in medie_sett.items():
    print(f"Settimana {sett}: rendimento medio {m:.2%}")
print()


# ============================================================================
# CHALLENGE SPORT: la gara simulata — ch_sport.py
# ============================================================================
print("--- Challenge Sport: La gara simulata ---")
import numpy as np
import pandas as pd

PILOTI: list[str] = ["Ferri", "Lanza", "Moro", "Neri"]
SCUDERIE: list[str] = ["Scuderia Rossa"] * 2 + ["Scuderia Blu"] * 2
BASE: np.ndarray = np.array([92.0, 92.4, 92.2, 92.6])
GIRI: int = 15
N: int = 10_000

rng = np.random.default_rng(15)
# righe = giri, colonne = piloti
tempi: np.ndarray = rng.normal(BASE, 0.6, size=(GIRI, 4))
tempi[7] = tempi[7] + 20               # pit stop al giro 8
print(f"Giri anomali (oltre 100 s): {np.sum(tempi > 100)}")
sotto_92: np.ndarray = np.sum(tempi < 92, axis=0)
for pilota, n in zip(PILOTI, sotto_92):
    print(f"{pilota}, giri sotto i 92 s: {n}")

ferri: np.ndarray = rng.normal(92.0, 0.6, size=(N, GIRI))
moro: np.ndarray = rng.normal(92.2, 0.6, size=(N, GIRI))
vince: np.ndarray = np.sum(moro, axis=1) < np.sum(ferri, axis=1)
print(f"P(Moro batte Ferri): {np.mean(vince):.1%}")

gara: pd.DataFrame = pd.DataFrame({
    "pilota": PILOTI, "scuderia": SCUDERIE,
    "totale": np.sum(tempi, axis=0),
    "migliore": np.min(tempi, axis=0),
})
gara["distacco"] = gara["totale"] - gara["totale"].min()
print(gara.sort_values("totale").round(1))
print(gara.groupby("scuderia")["totale"].mean().round(1))
print()


# ============================================================================
# CHALLENGE IMPRESE E MARKETING: un mese di vendite — ch_negozio.py
# ============================================================================
print("--- Challenge Imprese e marketing: Un mese di vendite ---")
import numpy as np
import pandas as pd

PRODOTTI: list[str] = ["zaino", "borraccia", "quaderno",
                       "cuffie", "lampada"]
CATEGORIE: list[str] = ["scuola", "casa", "scuola", "tech", "casa"]
PREZZI: np.ndarray = np.array([39.9, 14.5, 3.2, 59.0, 24.9])
COSTI: np.ndarray = np.array([22.0, 6.0, 1.1, 38.0, 13.5])
GIORNI: int = 30
N: int = 10_000

rng = np.random.default_rng(30)
# righe = giorni, colonne = prodotti: pezzi venduti
pezzi: np.ndarray = rng.integers(0, 6, size=(GIORNI, 5))
incasso: np.ndarray = np.sum(pezzi * PREZZI, axis=1)  # broadcasting
print(f"Fatturato del mese: {np.sum(incasso):.2f} EUR")
print(f"Incasso medio giornaliero: {np.mean(incasso):.2f} EUR")
print(f"Giorni sopra 300 EUR: {np.sum(incasso > 300)} su {GIORNI}")

conv_a: np.ndarray = rng.binomial(n=1000, p=0.04, size=N)
conv_b: np.ndarray = rng.binomial(n=1000, p=0.05, size=N)
print(f"P(la pagina B vende più della A): "
      f"{np.mean(conv_b > conv_a):.1%}")

negozio: pd.DataFrame = pd.DataFrame({
    "prodotto": PRODOTTI, "categoria": CATEGORIE,
    "pezzi": np.sum(pezzi, axis=0), "prezzo": PREZZI, "costo": COSTI,
})
negozio["margine"] = negozio["pezzi"] * (
    negozio["prezzo"] - negozio["costo"])
print(negozio[["prodotto", "pezzi", "margine"]].round(2))
print(negozio.groupby("categoria")["margine"].sum().round(2))
print()


# ============================================================================
# CHALLENGE SALUTE E SCIENZA: lo studio simulato — ch_salute.py
# ============================================================================
print("--- Challenge Salute e scienza: Lo studio simulato ---")
import numpy as np
import pandas as pd

SOGLIA: int = 5          # calo minimo in mmHg per dire "migliorato"
N: int = 10_000

codici: list[str] = ["P" + str(i).zfill(2) for i in range(1, 21)]
gruppo: np.ndarray = np.array(["trattamento"] * 10
                              + ["controllo"] * 10)
rng = np.random.default_rng(11)
eta: np.ndarray = rng.integers(35, 71, size=20)
prima: np.ndarray = np.round(rng.normal(150, 12, size=20))
calo: np.ndarray = rng.normal(2 + 6 * (gruppo == "trattamento"), 5)
dopo: np.ndarray = np.round(prima - calo)

diff: np.ndarray = prima - dopo                   # vettorizzato
migliorato: np.ndarray = diff >= SOGLIA
tratt: np.ndarray = gruppo == "trattamento"
k: int = np.sum(migliorato[tratt])
p0: float = np.mean(migliorato)                  # quota complessiva
print(f"Calo medio: {np.mean(diff):.1f} mmHg")
print(f"Migliorati trattamento: {k} su 10")
print(f"Migliorati controllo: {np.sum(migliorato[~tratt])} su 10")
print(f"Migliorati in tutto: {p0:.0%}")

sim: np.ndarray = rng.binomial(n=10, p=p0, size=N)
print(f"P(almeno {k} su 10 senza effetto): {np.mean(sim >= k):.1%}")

studio: pd.DataFrame = pd.DataFrame({
    "codice": codici, "eta": eta, "gruppo": gruppo,
    "prima": prima, "dopo": dopo,
})
studio["differenza"] = studio["prima"] - studio["dopo"]
print(studio.head(3))
print(studio.groupby("gruppo")[["eta", "differenza"]].mean().round(1))
print()


# ============================================================================
# CHALLENGE CASO E PROBABILITÀ: dadi e porte — ch_probabilita.py
# ============================================================================
print("--- Challenge Caso e probabilità: Dadi e porte ---")
import numpy as np
import pandas as pd

LANCI: int = 1000
N: int = 10_000

rng = np.random.default_rng(6)
dado1: np.ndarray = rng.integers(1, 7, size=LANCI)
dado2: np.ndarray = rng.integers(1, 7, size=LANCI)
somma: np.ndarray = dado1 + dado2                 # vettorizzato
print(f"Somma media: {np.mean(somma):.2f} (teorica 7.00)")
print(f"Somma 7: {np.mean(somma == 7):.1%} (esatta {6 / 36:.1%})")
alte: np.ndarray = somma[somma >= 10]
print(f"Somma almeno 10: {alte.size} lanci "
      f"({alte.size / LANCI:.1%}, esatta {6 / 36:.1%})")
print(f"Doppi: {np.mean(dado1 == dado2):.1%} (esatta {1 / 6:.1%})")

auto: np.ndarray = rng.integers(0, 3, size=N)    # porta dell'auto
scelta: np.ndarray = rng.integers(0, 3, size=N)  # prima scelta
resta: float = np.mean(auto == scelta)
print(f"Monty Hall, vince chi resta: {resta:.1%}")
print(f"Monty Hall, vince chi cambia: {1 - resta:.1%}")

tavolo: pd.DataFrame = pd.DataFrame({"dado1": dado1, "dado2": dado2})
tavolo["somma"] = tavolo["dado1"] + tavolo["dado2"]
medie: pd.Series = tavolo.groupby("dado1")["somma"].mean()
for faccia, m in medie.items():
    print(f"Primo dado {faccia}: somma media {m:.2f} "
          f"(teorica {faccia + 3.5:.2f})")
print()


# ============================================================================
print("=" * 60)
print("Fine degli esercizi del laboratorio 07")
print("=" * 60)
