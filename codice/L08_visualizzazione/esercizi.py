# L08 — Visualizzazione e progetto
# Soluzioni degli esercizi del laboratorio 08
#
# Ogni esercizio corrisponde a un file della traccia (nome tra parentesi).
# Per provarne uno solo, copiatelo in un file a parte.
# I file di dati usati dagli esercizi sono in questa stessa cartella.


# ============================================================================
# ESERCIZIO 1: immatricolati e laureati — immatricolati.py
# ============================================================================
print("--- Esercizio 1: Immatricolati e laureati ---")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

anni: list[int] = list(range(2018, 2026))
immatricolati: list[int] = [182, 195, 210, 204, 231, 248, 240, 262]
laureati: list[int] = [118, 126, 131, 140, 137, 152, 160, 171]

plt.figure(figsize=(7, 4))
plt.plot(anni, immatricolati, marker="o", label="Immatricolati")
plt.plot(anni, laureati, marker="s", linestyle="--", label="Laureati")
plt.title("Corso di laurea in Statistica")
plt.xlabel("Anno accademico (inizio)")
plt.ylabel("Studenti")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("immatricolati.png")

i: int = immatricolati.index(max(immatricolati))
print(f"Anno con più immatricolati: {anni[i]} ({immatricolati[i]})")
crescita: float = immatricolati[-1] / immatricolati[0] - 1
print(f"Variazione {anni[0]}-{anni[-1]}: {crescita:.1%}")
print()


# ============================================================================
# ESERCIZIO 2: i voti dell'appello — voti.py
# ============================================================================
print("--- Esercizio 2: I voti dell'appello ---")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(14)
tutti: np.ndarray = rng.normal(23.5, 4, 250).round().clip(max=30)
voti: np.ndarray = tutti[tutti >= 18]
media: float = voti.mean()

plt.figure(figsize=(7, 4))
plt.hist(voti, bins=np.arange(17.5, 31), color="steelblue",
         edgecolor="white")
plt.axvline(media, color="red", linestyle="--", label="Media")
plt.title("Voti dei promossi all'appello di Statistica")
plt.xlabel("Voto")
plt.ylabel("Studenti")
plt.legend()
plt.tight_layout()
plt.savefig("voti.png")

print(f"Promossi: {len(voti)} su {len(tutti)}")
print(f"Media dei promossi: {media:.1f}")
print(f"Voti da 27 in su: {(voti >= 27).mean():.1%}")
print()


# ============================================================================
# ESERCIZIO 3: ore di studio e voto — studio.py
# ============================================================================
print("--- Esercizio 3: Ore di studio e voto ---")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(7)
ore: np.ndarray = rng.uniform(20, 120, 80).round()
voto: np.ndarray = (17 + 0.09 * ore + rng.normal(0, 2.5, 80)).round()
voto = voto.clip(18, 30)

plt.figure(figsize=(7, 4))
plt.scatter(ore, voto, alpha=0.6, color="steelblue")
plt.title("Ore di studio e voto all'esame")
plt.xlabel("Ore di studio")
plt.ylabel("Voto")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("studio.png")

r: float = np.corrcoef(ore, voto)[0, 1]
print(f"Studenti: {len(ore)}, correlazione: {r:.2f}")
print(f"Voto medio con più di 80 ore: {voto[ore > 80].mean():.1f}")
print(f"Voto medio con 80 ore o meno: {voto[ore <= 80].mean():.1f}")
print()


# ============================================================================
# ESERCIZIO 4: l'attesa in mensa — mensa.py
# ============================================================================
print("--- Esercizio 4: L'attesa in mensa ---")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rng = np.random.default_rng(3)
giorni: list[str] = ["lun", "mar", "mer", "gio", "ven"]
attesa_tipica: list[float] = [12, 15, 14, 16, 8]
df: pd.DataFrame = pd.DataFrame({
    "giorno": giorni * 20,
    "attesa": np.tile(attesa_tipica, 20) + rng.normal(0, 3, 100)})

medie: pd.Series = df.groupby("giorno", sort=False)["attesa"].mean()
plt.figure(figsize=(7, 4))
plt.bar(medie.index, medie.values, color="steelblue")
plt.title("Attesa media alla mensa")
plt.xlabel("Giorno")
plt.ylabel("Minuti")
plt.tight_layout()
plt.savefig("mensa.png")

print(f"Rilevazioni: {len(df)}, media: {df['attesa'].mean():.1f} min")
print(f"Giorno peggiore: {medie.idxmax()} ({medie.max():.1f} min)")
print(f"Giorno migliore: {medie.idxmin()} ({medie.min():.1f} min)")
print()


# ============================================================================
# ESERCIZIO 5: il tragitto per l'università — tragitto.py
# ============================================================================
print("--- Esercizio 5: Il tragitto per l'università ---")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(11)
tempi: dict[str, np.ndarray] = {
    "bici": rng.normal(22, 3, 40).round(),
    "autobus": rng.normal(28, 7, 40).round(),
    "treno": rng.normal(35, 4, 40).round()}

plt.figure(figsize=(7, 4))
plt.boxplot(list(tempi.values()), tick_labels=list(tempi.keys()))
plt.title("Tempo per arrivare in università")
plt.xlabel("Mezzo")
plt.ylabel("Minuti")
plt.tight_layout()
plt.savefig("tragitto.png")

for mezzo, t in tempi.items():
    print(f"{mezzo}: mediana {np.median(t):.0f} min, "
          f"oltre 30 min {(t > 30).mean():.1%}")
print()


# ============================================================================
# ESERCIZIO 6: gennaio in due grafici — meteo.py
# ============================================================================
print("--- Esercizio 6: Gennaio in due grafici ---")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(1)
giorni: np.ndarray = np.arange(1, 32)
minime: np.ndarray = rng.normal(0, 2.5, 31).round(1)
massime: np.ndarray = (minime + rng.normal(7, 1.8, 31)).round(1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(giorni, massime, color="tomato", label="Massima")
ax1.plot(giorni, minime, color="steelblue", label="Minima")
ax1.set_title("Temperature di gennaio a Padova")
ax1.set_xlabel("Giorno")
ax1.set_ylabel("°C")
ax1.legend()
ax2.hist(massime - minime, bins=8, color="gray", edgecolor="white")
ax2.set_title("Escursione termica")
ax2.set_xlabel("Massima - minima (°C)")
ax2.set_ylabel("Giorni")
fig.tight_layout()
fig.savefig("meteo.png")
print(f"Giorni con la minima sotto zero: {(minime < 0).sum()}")
print(f"Escursione media: {(massime - minime).mean():.1f} °C")
print()


# ============================================================================
# CHALLENGE MERCATI E FINANZA: due mesi di borsa — ch_mercati.py
# ============================================================================
print("--- Challenge Mercati e finanza: Due mesi di borsa ---")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def salva(nome: str, titolo: str, x: str, y: str) -> None:
    """Mette titolo ed etichette al grafico e lo salva in PNG."""
    plt.title(titolo)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.savefig(nome)
    plt.close()


grezzo: pd.DataFrame = pd.read_csv("prezzi.csv", sep=";")
df: pd.DataFrame = grezzo.drop_duplicates().dropna()
df = df[df["prezzo"] > 0].copy()
print(f"Righe lette: {len(grezzo)}, dopo la pulizia: {len(df)}")
df["rendimento"] = df.groupby("titolo")["prezzo"].pct_change()
prezzi = df.groupby("titolo")["prezzo"]
rend: pd.Series = prezzi.last() / prezzi.first() - 1
vol: pd.Series = df.groupby("titolo")["rendimento"].std()
mib: pd.DataFrame = df[df["titolo"] == "MIB"]
for t in rend.index:
    print(f"{t}: rendimento {rend[t]:.1%}, volatilità {vol[t]:.1%}")
print("Giorni con il MIB in calo oltre l'1%:",
      (mib["rendimento"] < -0.01).sum())
plt.hist(df["rendimento"].dropna(), bins=20, edgecolor="white")
salva("rendimenti.png", "Rendimenti giornalieri", "Rendimento",
      "Giorni")
for t in ["ENRG", "BANK", "TECH"]:
    plt.plot(df[df["titolo"] == t]["prezzo"].values, label=t)
plt.legend()
salva("prezzi.png", "Prezzi di chiusura", "Giorno", "Prezzo (EUR)")
plt.bar(vol.index, vol.values, color="steelblue")
salva("volatilita.png", "Volatilità", "Titolo", "Deviazione std")
titoli: pd.Series = rend.drop("MIB")
print(f"Il migliore è {titoli.idxmax()} ({titoli.max():.1%}), "
      f"il peggiore {titoli.idxmin()} ({titoli.min():.1%}).")
print(f"Il più volatile è {vol.idxmax()}, con {vol.max():.1%} al "
      f"giorno; il MIB si ferma a {vol['MIB']:.1%}.")
print(f"Il MIB rende {rend['MIB']:.1%}: "
      f"{(titoli > rend['MIB']).sum()} titoli su 3 fanno meglio.")
print()


# ============================================================================
# CHALLENGE SPORT: il passo gara — ch_sport.py
# ============================================================================
print("--- Challenge Sport: Il passo gara ---")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def salva(nome: str, titolo: str, x: str, y: str) -> None:
    """Mette titolo ed etichette al grafico e lo salva in PNG."""
    plt.title(titolo)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.savefig(nome)
    plt.close()


grezzo: pd.DataFrame = pd.read_csv("tempi_giro.csv", sep=";")
df: pd.DataFrame = grezzo.drop_duplicates().dropna()
df = df[(df["tempo"] > 60) & (df["tempo"] < 180)].copy()
print(f"Righe lette: {len(grezzo)}, dopo la pulizia: {len(df)}")
df["lento"] = df["tempo"] > 100
normali: pd.DataFrame = df[~df["lento"]]
media: pd.Series = normali.groupby("pilota")["tempo"].mean()
distacco: pd.Series = media - media.min()
top: pd.Series = df.loc[df["tempo"].idxmin()]
print(f"Giro più veloce: {top['pilota']}, gara {top['gara']}, "
      f"giro {top['giro']}, {top['tempo']:.1f} s")
print(f"Giri lenti (pit stop e safety car): {df['lento'].mean():.1%}")
for p in media.index:
    print(f"{p}: media sui giri normali {media[p]:.2f} s")
plt.hist(df["tempo"], bins=25, edgecolor="white")
salva("hist_tempi.png", "Tempi sul giro", "Tempo (s)", "Giri")
gara1: pd.DataFrame = normali[normali["gara"] == 1]
for p in media.index:
    s: pd.DataFrame = gara1[gara1["pilota"] == p]
    plt.plot(s["giro"], s["tempo"], marker="o", label=p)
plt.legend()
salva("gara1.png", "Gara 1, giri normali", "Giro", "Tempo (s)")
plt.bar(distacco.index, distacco.values, color="steelblue")
salva("distacchi.png", "Distacco dal più veloce", "Pilota", "s")
costo: float = df[df["lento"]]["tempo"].mean() - media.mean()
print(f"Sul passo gara il più veloce è {media.idxmin()}; "
      f"{media.idxmax()} perde {distacco.max():.2f} s al giro.")
print(f"Un giro lento costa {costo:.1f} s in più e va escluso.")
print("Gara 1: i tempi crescono fino al pit stop (usura gomme).")
print()


# ============================================================================
# CHALLENGE IMPRESE E MARKETING: quattro mesi di ordini — ch_negozio.py
# ============================================================================
print("--- Challenge Imprese e marketing: Quattro mesi di ordini ---")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def salva(nome: str, titolo: str, x: str, y: str) -> None:
    """Mette titolo ed etichette al grafico e lo salva in PNG."""
    plt.title(titolo)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.savefig(nome)
    plt.close()


grezzo: pd.DataFrame = pd.read_csv("ordini.csv", sep=";")
df: pd.DataFrame = grezzo.drop_duplicates().dropna()
df = df[df["quantita"] > 0].copy()
print(f"Righe lette: {len(grezzo)}, dopo la pulizia: {len(df)}")
df["importo"] = df["quantita"] * df["prezzo"]
df["mese"] = df["data"].str[:7]
citta: pd.Series = df.groupby("citta")["importo"].sum()
mesi: pd.Series = df.groupby("mese")["importo"].sum()
pezzi: pd.Series = df.groupby("prodotto")["quantita"].sum()
ricavi: pd.Series = df.groupby("prodotto")["importo"].sum()
top: str = pezzi.idxmax()
print(f"Fatturato: {df['importo'].sum():.2f} EUR, "
      f"ordine medio: {df['importo'].mean():.2f} EUR")
for c in citta.index:
    print(f"{c}: {citta[c]:.2f} EUR ({citta[c] / citta.sum():.1%})")
print(f"Prodotto più venduto: {top}, {pezzi[top]:.0f} pezzi")
plt.hist(df["importo"], bins=15, edgecolor="white")
salva("hist_importi.png", "Importo degli ordini", "Euro", "Ordini")
plt.plot(mesi.index, mesi.values, marker="o")
salva("mesi.png", "Fatturato mensile", "Mese", "Euro")
plt.bar(citta.index, citta.values, color="steelblue")
salva("citta.png", "Fatturato per città", "Città", "Euro")
tot: float = citta.sum()
print(f"{citta.idxmax()} vale {citta.max() / tot:.1%} del fatturato, "
      f"{citta.idxmin()} solo {citta.min() / tot:.1%}.")
print(f"Il mese migliore è {mesi.idxmax()} ({mesi.max():.2f} EUR), "
      f"il peggiore {mesi.idxmin()} ({mesi.min():.2f} EUR).")
print(f"Prodotto {top}: {pezzi[top] / pezzi.sum():.1%} dei pezzi, "
      f"ma {ricavi[top] / ricavi.sum():.1%} del fatturato.")
print()


# ============================================================================
# CHALLENGE SALUTE E SCIENZA: l'effetto dell'integratore — ch_salute.py
# ============================================================================
print("--- Challenge Salute e scienza: L'effetto dell'integratore ---")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def salva(nome: str, titolo: str, x: str, y: str) -> None:
    """Mette titolo ed etichette al grafico e lo salva in PNG."""
    plt.title(titolo)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.savefig(nome)
    plt.close()


grezzo: pd.DataFrame = pd.read_csv("pazienti.csv", sep=";")
df: pd.DataFrame = grezzo.drop_duplicates().dropna()
df = df[df["pressione_prima"].between(80, 250)
        & df["pressione_dopo"].between(80, 250)].copy()
print(f"Righe lette: {len(grezzo)}, dopo la pulizia: {len(df)}")
df["differenza"] = df["pressione_dopo"] - df["pressione_prima"]
df["migliorato"] = df["differenza"] <= -10
calo: pd.Series = df.groupby("gruppo")["differenza"].mean()
quota: pd.Series = df.groupby("gruppo")["migliorato"].mean()
rr: float = quota["trattamento"] / quota["controllo"]
for g in calo.index:
    print(f"{g}: variazione media {calo[g]:.1f} mmHg, "
          f"migliorati {quota[g]:.1%}")
print(f"Rischio relativo di miglioramento: {rr:.2f}")
plt.boxplot([df[df["gruppo"] == g]["differenza"] for g in calo.index],
            tick_labels=calo.index)
salva("variazione.png", "Dopo meno prima", "Gruppo", "mmHg")
for g in calo.index:
    s: pd.DataFrame = df[df["gruppo"] == g]
    plt.scatter(s["pressione_prima"], s["pressione_dopo"], label=g)
plt.legend()
salva("prima_dopo.png", "Pressione sistolica", "Prima (mmHg)",
      "Dopo (mmHg)")
plt.bar(quota.index, quota.values, color="steelblue")
salva("migliorati.png", "Quota di migliorati", "Gruppo", "Quota")
print(f"La pressione cambia di {calo['trattamento']:.1f} mmHg con "
      f"l'integratore e di {calo['controllo']:.1f} senza.")
print(f"I migliorati sono {rr:.2f} volte quelli del controllo.")
print("Anche il controllo migliora: per questo serve un confronto.")
print()


# ============================================================================
# CHALLENGE CASO E PROBABILITÀ: il dado sospetto — ch_probabilita.py
# ============================================================================
print("--- Challenge Caso e probabilità: Il dado sospetto ---")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def salva(nome: str, titolo: str, x: str, y: str) -> None:
    """Mette titolo ed etichette al grafico e lo salva in PNG."""
    plt.title(titolo)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.savefig(nome)
    plt.close()


grezzo: pd.DataFrame = pd.read_csv("lanci.csv", sep=";")
df: pd.DataFrame = grezzo.drop_duplicates().dropna()
df = df[df["dado2"].between(1, 6)].copy()
print(f"Righe lette: {len(grezzo)}, dopo la pulizia: {len(df)}")
df["somma"] = df["dado1"] + df["dado2"]
df["sei"] = df["dado2"] == 6
media: pd.Series = df.groupby("giocatore")["somma"].mean()
sei: pd.Series = df.groupby("giocatore")["sei"].mean()
print(f"Media della somma: {df['somma'].mean():.2f} (teorica 7.00)")
print(f"Somma 7: {(df['somma'] == 7).mean():.1%} dei lanci "
      f"(teorica {6 / 36:.1%})")
for g in media.index:
    print(f"{g}: media {media[g]:.2f}, sei sul dado 2 {sei[g]:.1%}")
plt.hist(df["somma"], bins=np.arange(1.5, 13), edgecolor="white")
salva("somme.png", "Somma dei due dadi", "Somma", "Lanci")
lanci: np.ndarray = np.arange(1, len(df) + 1)
plt.plot(lanci, df["somma"].cumsum() / lanci)
plt.axhline(7, color="red", linestyle="--", label="valore teorico")
plt.legend()
salva("media_cumulata.png", "Media della somma", "Lanci", "Media")
plt.bar(sei.index, sei.values, color="steelblue")
plt.axhline(1 / 6, color="red", linestyle="--")
salva("sei.png", "Quota di 6 sul dado 2", "Giocatore", "Quota")
print(f"Dopo {len(df)} lanci la media cumulata è "
      f"{df['somma'].mean():.2f}; il valore teorico è 7.")
print(f"{sei.idxmax()} fa 6 sul dado 2 nel {sei.max():.1%} dei lanci "
      f"e la sua somma media è {media[sei.idxmax()]:.2f}.")
print(f"Con un dado regolare sarebbe {1 / 6:.1%}: va controllato.")
print()


# ============================================================================
print("=" * 60)
print("Fine degli esercizi del laboratorio 08")
print("=" * 60)
