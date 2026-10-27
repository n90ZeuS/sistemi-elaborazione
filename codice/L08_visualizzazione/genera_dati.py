"""Genera i 5 CSV dei progetti finali di L08 (seed fisso).

Ogni file usa il separatore ";" e contiene qualche riga da
pulire: duplicati, valori mancanti, valori impossibili.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(2027)


def difetti(df: pd.DataFrame, col: str, mancanti: int,
            impossibili: list, duplicati: int) -> pd.DataFrame:
    """Inserisce mancanti, valori impossibili e righe doppie."""
    df = df.copy()
    righe = rng.choice(len(df), mancanti + len(impossibili),
                       replace=False)
    df[col] = df[col].astype(object)
    for i, r in enumerate(righe):
        valore = np.nan if i < mancanti else impossibili[i - mancanti]
        df.loc[r, col] = valore
    doppie = np.sort(rng.choice(len(df), duplicati, replace=False))
    pezzi = []
    for i in range(len(df)):
        pezzi.append(df.iloc[[i]])
        if i in doppie:
            pezzi.append(df.iloc[[i]])
    return pd.concat(pezzi, ignore_index=True)


def mercati() -> pd.DataFrame:
    """Prezzi di chiusura di settembre e ottobre 2026."""
    giorni = pd.bdate_range("2026-09-01", "2026-10-30")
    n = len(giorni)
    mib = rng.normal(0.0004, 0.008, n)
    titoli = {"ENRG": (18.40, 0.7, -0.0003, 0.009),
              "BANK": (11.20, 1.2, 0.0002, 0.010),
              "TECH": (26.50, 1.4, 0.0020, 0.016)}
    serie = {"MIB": 100 * np.cumprod(1 + mib)}
    for t, (p0, beta, mu, sd) in titoli.items():
        r = mu + beta * mib + rng.normal(0, sd, n)
        serie[t] = p0 * np.cumprod(1 + r)
    righe = []
    for i, g in enumerate(giorni):
        for t in ["ENRG", "BANK", "TECH", "MIB"]:
            righe.append((g.strftime("%Y-%m-%d"), t,
                          round(float(serie[t][i]), 2)))
    df = pd.DataFrame(righe, columns=["data", "titolo", "prezzo"])
    return difetti(df, "prezzo", 2, [0.0, -11.35], 3)


def sport() -> pd.DataFrame:
    """Tempi sul giro dei 4 piloti in 3 gare da 15 giri."""
    base = {1: 92.0, 2: 88.5, 3: 95.2}
    passo = {"Ferri": -0.35, "Lanza": 0.15,
             "Moro": -0.10, "Neri": 0.45}
    righe = []
    for gara, t0 in base.items():
        for pilota, delta in passo.items():
            pit = int(rng.integers(7, 11))
            for giro in range(1, 16):
                usura = 0.22 * ((giro - 1) if giro < pit
                                else (giro - pit))
                t = t0 + delta + usura + rng.normal(0, 0.3)
                if giro == pit:
                    t += 21.0
                if gara == 2 and giro in (5, 6):
                    t += 14.0
                righe.append((gara, pilota, giro, round(t, 1)))
    df = pd.DataFrame(righe,
                      columns=["gara", "pilota", "giro", "tempo"])
    return difetti(df, "tempo", 2, [0.0, 921.4], 3)


def negozio() -> pd.DataFrame:
    """Ordini del negozio online da settembre a dicembre 2026."""
    clienti = {"Bianchi Laura": "Padova", "Rossi Marco": "Padova",
               "Conte Elisa": "Padova", "Ferro Luca": "Padova",
               "Galli Sara": "Padova", "Marin Davide": "Venezia",
               "Zanon Giulia": "Venezia", "Pavan Matteo": "Venezia",
               "Basso Chiara": "Venezia", "Carraro Paolo": "Verona",
               "Fabbri Anna": "Verona", "Riva Stefano": "Verona",
               "Tosi Marta": "Verona", "Dal Bo Irene": "Vicenza",
               "Sartori Luca": "Vicenza", "Zen Alice": "Vicenza"}
    prezzi = {"zaino": 39.90, "borraccia": 14.50, "quaderno": 4.90,
              "cuffie": 59.00, "lampada": 24.90}
    pesi_prod = [0.20, 0.25, 0.30, 0.10, 0.15]
    mesi = {9: 0.30, 10: 0.20, 11: 0.20, 12: 0.30}
    nomi = list(clienti)
    pesi_cli = rng.dirichlet(np.ones(len(nomi)) * 1.5)
    righe = []
    for _ in range(150):
        mese = int(rng.choice(list(mesi), p=list(mesi.values())))
        giorno = int(rng.integers(1, 31 if mese != 10 else 32))
        cliente = str(rng.choice(nomi, p=pesi_cli))
        prodotto = str(rng.choice(list(prezzi), p=pesi_prod))
        alto = 7 if prodotto == "quaderno" else 3
        q = int(rng.integers(1, alto))
        righe.append((f"2026-{mese:02d}-{giorno:02d}", cliente,
                      clienti[cliente], prodotto, q,
                      prezzi[prodotto]))
    df = pd.DataFrame(righe, columns=["data", "cliente", "citta",
                                      "prodotto", "quantita",
                                      "prezzo"])
    df = df.sort_values("data", kind="stable")
    df = df.reset_index(drop=True)
    df.insert(0, "ordine", range(1001, 1001 + len(df)))
    return difetti(df, "quantita", 2, [0, -2], 4)


def salute() -> pd.DataFrame:
    """Pazienti dello studio sull'integratore per la pressione."""
    n = 120
    gruppo = np.array(["trattamento", "controllo"] * (n // 2))
    eta = rng.integers(40, 76, n)
    sesso = rng.choice(["F", "M"], n)
    prima = rng.normal(152, 11, n) + 0.2 * (eta - 57)
    effetto = np.where(gruppo == "trattamento", -11.0, -4.0)
    dopo = prima + effetto + rng.normal(0, 7, n)
    df = pd.DataFrame({
        "codice": [f"P{i:03d}" for i in range(1, n + 1)],
        "sesso": sesso, "eta": eta, "gruppo": gruppo,
        "pressione_prima": prima.round().astype(int),
        "pressione_dopo": dopo.round().astype(int)})
    df = difetti(df, "pressione_dopo", 3, [0], 3)
    df["pressione_prima"] = df["pressione_prima"].astype(object)
    df.loc[17, "pressione_prima"] = 1480
    return df


def probabilita() -> pd.DataFrame:
    """Registro di 180 lanci di due dadi; il dado di Dario è
    truccato e dà 6 più spesso."""
    giocatori = ["Ada", "Bruno", "Carla", "Dario"]
    giusto = np.full(6, 1 / 6)
    truccato = np.array([0.12, 0.12, 0.12, 0.12, 0.12, 0.40])
    righe = []
    for lancio in range(1, 181):
        g = giocatori[(lancio - 1) % 4]
        p = truccato if g == "Dario" else giusto
        d1 = int(rng.integers(1, 7))
        d2 = int(rng.choice(np.arange(1, 7), p=p))
        righe.append((lancio, g, d1, d2))
    df = pd.DataFrame(righe, columns=["lancio", "giocatore",
                                      "dado1", "dado2"])
    return difetti(df, "dado2", 2, [7, 0], 3)


if __name__ == "__main__":
    file: dict = {"prezzi.csv": mercati(), "tempi_giro.csv": sport(),
                  "ordini.csv": negozio(), "pazienti.csv": salute(),
                  "lanci.csv": probabilita()}
    for nome, df in file.items():
        df.to_csv(nome, sep=";", index=False)
        print(f"{nome}: {len(df)} righe")
