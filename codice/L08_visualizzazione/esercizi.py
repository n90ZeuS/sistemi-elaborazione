# L08 — Visualizzazione e progetto
# Esercizi per il laboratorio 08
#
# Esercizi pratici su creazione di grafici con matplotlib e un mini-progetto
# di analisi dati. I grafici vengono salvati su file (plt.savefig).
# Ogni esercizio include assert per verificare la correttezza.

import os
import tempfile
import math
from typing import Any

# ============================================================================
# Importazione sicura delle librerie
# ============================================================================

try:
    import numpy as np
    NUMPY_DISPONIBILE: bool = True
except ImportError:
    NUMPY_DISPONIBILE = False
    print("ATTENZIONE: NumPy non e' installato. Installa con: pip install numpy")

try:
    import matplotlib
    matplotlib.use("Agg")  # Backend non interattivo: salva su file senza aprire finestre
    import matplotlib.pyplot as plt
    MATPLOTLIB_DISPONIBILE: bool = True
except ImportError:
    MATPLOTLIB_DISPONIBILE = False
    print("ATTENZIONE: Matplotlib non e' installato. Installa con: pip install matplotlib")

try:
    import pandas as pd
    PANDAS_DISPONIBILE: bool = True
except ImportError:
    PANDAS_DISPONIBILE = False
    print("ATTENZIONE: Pandas non e' installato. Installa con: pip install pandas")


# ============================================================================
# ESERCIZIO 1: Creazione di diversi tipi di grafici
# ============================================================================

if MATPLOTLIB_DISPONIBILE and NUMPY_DISPONIBILE:

    # Cartella temporanea per salvare i grafici
    dir_grafici: str = tempfile.mkdtemp(prefix="grafici_lab08_")

    # --- 1a) Grafico a barre ---
    def crea_grafico_barre(
        categorie: list[str],
        valori: list[float],
        titolo: str,
        etichetta_x: str,
        etichetta_y: str,
        percorso_file: str,
    ) -> str:
        """
        Crea un grafico a barre e lo salva su file.
        Restituisce il percorso del file creato.
        """
        fig, ax = plt.subplots(figsize=(10, 6))

        # Colori diversi per ogni barra
        colori: list[str] = ["#2196F3", "#4CAF50", "#FF9800", "#E91E63",
                             "#9C27B0", "#00BCD4", "#FF5722", "#607D8B"]
        colori_barre: list[str] = [colori[i % len(colori)] for i in range(len(categorie))]

        barre = ax.bar(categorie, valori, color=colori_barre, edgecolor="black", linewidth=0.5)

        # Aggiungi etichette sopra le barre
        for barra, valore in zip(barre, valori):
            ax.text(
                barra.get_x() + barra.get_width() / 2.0,
                barra.get_height() + max(valori) * 0.01,
                f"{valore:.1f}",
                ha="center", va="bottom", fontsize=9,
            )

        ax.set_title(titolo, fontsize=14, fontweight="bold")
        ax.set_xlabel(etichetta_x, fontsize=12)
        ax.set_ylabel(etichetta_y, fontsize=12)
        ax.grid(axis="y", alpha=0.3)

        plt.tight_layout()
        plt.savefig(percorso_file, dpi=150)
        plt.close(fig)
        return percorso_file

    # --- 1b) Grafico a dispersione (scatter) ---
    def crea_grafico_scatter(
        x: np.ndarray,
        y: np.ndarray,
        titolo: str,
        etichetta_x: str,
        etichetta_y: str,
        percorso_file: str,
    ) -> str:
        """Crea un grafico a dispersione e lo salva su file."""
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.scatter(x, y, alpha=0.6, c=y, cmap="viridis", edgecolors="black", linewidth=0.3, s=40)

        # Linea di tendenza (regressione lineare)
        coefficienti: np.ndarray = np.polyfit(x, y, 1)
        linea_tendenza: np.ndarray = np.polyval(coefficienti, x)
        pendenza: float = float(coefficienti[0])
        intercetta: float = float(coefficienti[1])
        ax.plot(
            np.sort(x), np.polyval(coefficienti, np.sort(x)),
            color="red", linewidth=2, linestyle="--",
            label=f"Tendenza: y = {pendenza:.2f}x + {intercetta:.2f}",
        )

        ax.set_title(titolo, fontsize=14, fontweight="bold")
        ax.set_xlabel(etichetta_x, fontsize=12)
        ax.set_ylabel(etichetta_y, fontsize=12)
        ax.legend(fontsize=10)
        ax.grid(alpha=0.3)

        plt.tight_layout()
        plt.savefig(percorso_file, dpi=150)
        plt.close(fig)
        return percorso_file

    # --- 1c) Istogramma ---
    def crea_istogramma(
        dati: np.ndarray,
        n_bins: int,
        titolo: str,
        etichetta_x: str,
        percorso_file: str,
    ) -> str:
        """Crea un istogramma con curva di densita' e lo salva su file."""
        fig, ax = plt.subplots(figsize=(10, 6))

        # Istogramma normalizzato
        conteggi, bordi, patches = ax.hist(
            dati, bins=n_bins, density=True, alpha=0.7,
            color="#2196F3", edgecolor="black", linewidth=0.5,
        )

        # Curva di densita' gaussiana sovrapposta
        media_dati: float = float(np.mean(dati))
        std_dati: float = float(np.std(dati))
        x_curva: np.ndarray = np.linspace(float(np.min(dati)), float(np.max(dati)), 200)
        y_curva: np.ndarray = (
            1 / (std_dati * np.sqrt(2 * np.pi))
            * np.exp(-0.5 * ((x_curva - media_dati) / std_dati) ** 2)
        )
        ax.plot(x_curva, y_curva, color="red", linewidth=2,
                label=f"Gaussiana (mu={media_dati:.1f}, sigma={std_dati:.1f})")

        # Linea verticale per la media
        ax.axvline(media_dati, color="green", linewidth=1.5, linestyle="--",
                   label=f"Media = {media_dati:.1f}")

        ax.set_title(titolo, fontsize=14, fontweight="bold")
        ax.set_xlabel(etichetta_x, fontsize=12)
        ax.set_ylabel("Densita'", fontsize=12)
        ax.legend(fontsize=10)
        ax.grid(alpha=0.3)

        plt.tight_layout()
        plt.savefig(percorso_file, dpi=150)
        plt.close(fig)
        return percorso_file

    # --- 1d) Boxplot ---
    def crea_boxplot(
        dati_gruppi: list[np.ndarray],
        etichette_gruppi: list[str],
        titolo: str,
        percorso_file: str,
    ) -> str:
        """Crea un boxplot comparativo e lo salva su file."""
        fig, ax = plt.subplots(figsize=(10, 6))

        bp = ax.boxplot(
            dati_gruppi, tick_labels=etichette_gruppi, patch_artist=True,
            medianprops=dict(color="red", linewidth=2),
        )

        # Colori diversi per ogni box
        colori: list[str] = ["#2196F3", "#4CAF50", "#FF9800", "#E91E63"]
        for patch, colore in zip(bp["boxes"], colori):
            patch.set_facecolor(colore)
            patch.set_alpha(0.6)

        ax.set_title(titolo, fontsize=14, fontweight="bold")
        ax.set_ylabel("Valori", fontsize=12)
        ax.grid(axis="y", alpha=0.3)

        plt.tight_layout()
        plt.savefig(percorso_file, dpi=150)
        plt.close(fig)
        return percorso_file

    # --- Test grafici ---
    # 1a) Grafico a barre: voti medi per materia
    materie: list[str] = ["Analisi", "Algebra", "Fisica", "Informatica", "Chimica"]
    voti_medi: list[float] = [25.3, 23.8, 26.1, 28.5, 24.0]
    path_barre: str = crea_grafico_barre(
        materie, voti_medi,
        "Voto medio per materia", "Materia", "Voto medio",
        os.path.join(dir_grafici, "barre.png"),
    )
    assert os.path.exists(path_barre), "Il file del grafico a barre non e' stato creato"
    assert os.path.getsize(path_barre) > 0, "Il file del grafico a barre e' vuoto"

    # 1b) Scatter: relazione ore studio / voto
    rng: np.random.Generator = np.random.default_rng(42)
    ore_studio: np.ndarray = rng.uniform(1, 10, 100)
    voti_scatter: np.ndarray = 18 + ore_studio * 1.2 + rng.normal(0, 2, 100)
    path_scatter: str = crea_grafico_scatter(
        ore_studio, voti_scatter,
        "Relazione ore di studio - Voto", "Ore di studio", "Voto",
        os.path.join(dir_grafici, "scatter.png"),
    )
    assert os.path.exists(path_scatter)

    # 1c) Istogramma: distribuzione altezze
    altezze: np.ndarray = rng.normal(170, 10, 500)
    path_isto: str = crea_istogramma(
        altezze, 30,
        "Distribuzione delle altezze", "Altezza (cm)",
        os.path.join(dir_grafici, "istogramma.png"),
    )
    assert os.path.exists(path_isto)

    # 1d) Boxplot: confronto voti tra corsi
    voti_info: np.ndarray = rng.normal(27, 3, 50)
    voti_mat: np.ndarray = rng.normal(24, 4, 50)
    voti_fis: np.ndarray = rng.normal(25, 3.5, 50)
    voti_chim: np.ndarray = rng.normal(23, 5, 50)
    path_box: str = crea_boxplot(
        [voti_info, voti_mat, voti_fis, voti_chim],
        ["Informatica", "Matematica", "Fisica", "Chimica"],
        "Distribuzione voti per corso di laurea",
        os.path.join(dir_grafici, "boxplot.png"),
    )
    assert os.path.exists(path_box)

    print(f"Esercizio 1 (Grafici): SUPERATO")
    print(f"  Grafici salvati in: {dir_grafici}")

    # Pulizia file temporanei dei grafici
    for nome_file in os.listdir(dir_grafici):
        os.unlink(os.path.join(dir_grafici, nome_file))
    os.rmdir(dir_grafici)

else:
    print("Esercizio 1 (Grafici): SALTATO (Matplotlib/NumPy non disponibili)")


# ============================================================================
# ESERCIZIO 2: Mini-progetto di analisi dati
# ============================================================================
# Un progetto completo che legge dati, calcola statistiche, e genera un report.

if MATPLOTLIB_DISPONIBILE and NUMPY_DISPONIBILE and PANDAS_DISPONIBILE:

    def genera_dati_vendite(n_righe: int = 200, seed: int = 42) -> pd.DataFrame:
        """
        Genera un dataset simulato di vendite per il mini-progetto.
        Colonne: data, prodotto, categoria, quantita, prezzo_unitario, citta
        """
        rng_loc: np.random.Generator = np.random.default_rng(seed)

        prodotti_per_cat: dict[str, list[str]] = {
            "Elettronica": ["Laptop", "Smartphone", "Tablet", "Cuffie"],
            "Abbigliamento": ["Maglietta", "Jeans", "Giacca", "Scarpe"],
            "Alimentari": ["Pasta", "Olio", "Caffe", "Biscotti"],
        }

        citta_lista: list[str] = ["Milano", "Roma", "Napoli", "Torino", "Bologna"]

        righe: list[dict[str, Any]] = []
        for _ in range(n_righe):
            categoria: str = rng_loc.choice(list(prodotti_per_cat.keys()))
            prodotto: str = rng_loc.choice(prodotti_per_cat[categoria])
            citta: str = rng_loc.choice(citta_lista)
            quantita: int = int(rng_loc.integers(1, 20))

            # Prezzi dipendono dalla categoria
            prezzi_base: dict[str, tuple[float, float]] = {
                "Elettronica": (100.0, 1500.0),
                "Abbigliamento": (15.0, 200.0),
                "Alimentari": (1.0, 15.0),
            }
            p_min, p_max = prezzi_base[categoria]
            prezzo: float = round(float(rng_loc.uniform(p_min, p_max)), 2)

            # Data casuale nel 2024
            mese: int = int(rng_loc.integers(1, 13))
            giorno: int = int(rng_loc.integers(1, 29))
            data: str = f"2024-{mese:02d}-{giorno:02d}"

            righe.append({
                "data": data,
                "prodotto": prodotto,
                "categoria": categoria,
                "quantita": quantita,
                "prezzo_unitario": prezzo,
                "citta": citta,
            })

        df: pd.DataFrame = pd.DataFrame(righe)
        df["fatturato"] = df["quantita"] * df["prezzo_unitario"]
        df["data"] = pd.to_datetime(df["data"])
        return df

    def analisi_vendite(df: pd.DataFrame) -> dict[str, Any]:
        """
        Esegue un'analisi completa delle vendite:
        - fatturato totale e medio
        - fatturato per categoria
        - fatturato per citta'
        - prodotto piu' venduto (per quantita')
        - mese con piu' fatturato
        """
        fatturato_totale: float = round(float(df["fatturato"].sum()), 2)
        fatturato_medio: float = round(float(df["fatturato"].mean()), 2)

        # Per categoria
        fatt_categoria: pd.Series = df.groupby("categoria")["fatturato"].sum().round(2)

        # Per citta'
        fatt_citta: pd.Series = df.groupby("citta")["fatturato"].sum().round(2)

        # Prodotto piu' venduto per quantita'
        vendite_prodotto: pd.Series = df.groupby("prodotto")["quantita"].sum()
        prodotto_top: str = str(vendite_prodotto.idxmax())
        quantita_top: int = int(vendite_prodotto.max())

        # Mese con piu' fatturato
        df_copia: pd.DataFrame = df.copy()
        df_copia["mese"] = df_copia["data"].dt.month
        fatt_mese: pd.Series = df_copia.groupby("mese")["fatturato"].sum()
        mese_top: int = int(fatt_mese.idxmax())

        return {
            "fatturato_totale": fatturato_totale,
            "fatturato_medio": fatturato_medio,
            "fatturato_per_categoria": fatt_categoria.to_dict(),
            "fatturato_per_citta": fatt_citta.to_dict(),
            "prodotto_piu_venduto": prodotto_top,
            "quantita_prodotto_top": quantita_top,
            "mese_migliore": mese_top,
            "num_transazioni": len(df),
        }

    def genera_report_grafici(df: pd.DataFrame, cartella: str) -> list[str]:
        """
        Genera una serie di grafici per il report e li salva nella cartella.
        Restituisce la lista dei percorsi dei file creati.
        """
        percorsi: list[str] = []

        # --- Grafico 1: Fatturato per categoria (barre) ---
        fig, ax = plt.subplots(figsize=(10, 6))
        fatt_cat: pd.Series = df.groupby("categoria")["fatturato"].sum().sort_values(ascending=False)
        colori_cat: list[str] = ["#2196F3", "#4CAF50", "#FF9800"]
        fatt_cat.plot(kind="bar", ax=ax, color=colori_cat[:len(fatt_cat)], edgecolor="black")
        ax.set_title("Fatturato totale per categoria", fontsize=14, fontweight="bold")
        ax.set_ylabel("Fatturato (EUR)", fontsize=12)
        ax.set_xlabel("Categoria", fontsize=12)
        plt.xticks(rotation=0)
        ax.grid(axis="y", alpha=0.3)
        plt.tight_layout()
        path_1: str = os.path.join(cartella, "fatturato_categoria.png")
        plt.savefig(path_1, dpi=150)
        plt.close(fig)
        percorsi.append(path_1)

        # --- Grafico 2: Fatturato per citta' (barre orizzontali) ---
        fig, ax = plt.subplots(figsize=(10, 6))
        fatt_citta: pd.Series = df.groupby("citta")["fatturato"].sum().sort_values()
        fatt_citta.plot(kind="barh", ax=ax, color="#E91E63", edgecolor="black")
        ax.set_title("Fatturato totale per citta'", fontsize=14, fontweight="bold")
        ax.set_xlabel("Fatturato (EUR)", fontsize=12)
        ax.grid(axis="x", alpha=0.3)
        plt.tight_layout()
        path_2: str = os.path.join(cartella, "fatturato_citta.png")
        plt.savefig(path_2, dpi=150)
        plt.close(fig)
        percorsi.append(path_2)

        # --- Grafico 3: Distribuzione fatturato per transazione (istogramma) ---
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(df["fatturato"], bins=30, color="#9C27B0", alpha=0.7, edgecolor="black")
        media_fatt: float = float(df["fatturato"].mean())
        ax.axvline(media_fatt, color="red", linestyle="--", linewidth=2,
                   label=f"Media = {media_fatt:.0f} EUR")
        ax.set_title("Distribuzione del fatturato per transazione", fontsize=14, fontweight="bold")
        ax.set_xlabel("Fatturato (EUR)", fontsize=12)
        ax.set_ylabel("Frequenza", fontsize=12)
        ax.legend(fontsize=10)
        ax.grid(alpha=0.3)
        plt.tight_layout()
        path_3: str = os.path.join(cartella, "distribuzione_fatturato.png")
        plt.savefig(path_3, dpi=150)
        plt.close(fig)
        percorsi.append(path_3)

        # --- Grafico 4: Boxplot fatturato per categoria ---
        fig, ax = plt.subplots(figsize=(10, 6))
        categorie_uniche: list[str] = sorted(df["categoria"].unique().tolist())
        dati_box: list[np.ndarray] = [
            df[df["categoria"] == cat]["fatturato"].values for cat in categorie_uniche
        ]
        bp = ax.boxplot(dati_box, tick_labels=categorie_uniche, patch_artist=True,
                        medianprops=dict(color="red", linewidth=2))
        colori_box: list[str] = ["#2196F3", "#4CAF50", "#FF9800"]
        for patch, colore in zip(bp["boxes"], colori_box):
            patch.set_facecolor(colore)
            patch.set_alpha(0.6)
        ax.set_title("Distribuzione fatturato per categoria", fontsize=14, fontweight="bold")
        ax.set_ylabel("Fatturato (EUR)", fontsize=12)
        ax.grid(axis="y", alpha=0.3)
        plt.tight_layout()
        path_4: str = os.path.join(cartella, "boxplot_categorie.png")
        plt.savefig(path_4, dpi=150)
        plt.close(fig)
        percorsi.append(path_4)

        # --- Grafico 5: Fatturato mensile (linea) ---
        fig, ax = plt.subplots(figsize=(12, 6))
        df_copia: pd.DataFrame = df.copy()
        df_copia["mese"] = df_copia["data"].dt.month
        fatt_mensile: pd.Series = df_copia.groupby("mese")["fatturato"].sum()
        ax.plot(fatt_mensile.index, fatt_mensile.values, marker="o", linewidth=2,
                color="#2196F3", markersize=8)
        ax.fill_between(fatt_mensile.index, fatt_mensile.values, alpha=0.2, color="#2196F3")
        ax.set_title("Andamento fatturato mensile", fontsize=14, fontweight="bold")
        ax.set_xlabel("Mese", fontsize=12)
        ax.set_ylabel("Fatturato (EUR)", fontsize=12)
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(["Gen", "Feb", "Mar", "Apr", "Mag", "Giu",
                            "Lug", "Ago", "Set", "Ott", "Nov", "Dic"])
        ax.grid(alpha=0.3)
        plt.tight_layout()
        path_5: str = os.path.join(cartella, "fatturato_mensile.png")
        plt.savefig(path_5, dpi=150)
        plt.close(fig)
        percorsi.append(path_5)

        return percorsi

    def genera_report_testuale(analisi: dict[str, Any]) -> str:
        """Genera un report testuale dell'analisi."""
        linee: list[str] = [
            "=" * 60,
            "REPORT ANALISI VENDITE",
            "=" * 60,
            "",
            f"Numero transazioni: {analisi['num_transazioni']}",
            f"Fatturato totale: EUR {analisi['fatturato_totale']:,.2f}",
            f"Fatturato medio per transazione: EUR {analisi['fatturato_medio']:,.2f}",
            "",
            "--- Fatturato per categoria ---",
        ]

        for cat, fatt in analisi["fatturato_per_categoria"].items():
            linee.append(f"  {cat}: EUR {fatt:,.2f}")

        linee.append("")
        linee.append("--- Fatturato per citta' ---")
        for citta, fatt in analisi["fatturato_per_citta"].items():
            linee.append(f"  {citta}: EUR {fatt:,.2f}")

        linee.extend([
            "",
            f"Prodotto piu' venduto: {analisi['prodotto_piu_venduto']} "
            f"({analisi['quantita_prodotto_top']} unita')",
            f"Mese migliore: {analisi['mese_migliore']}",
            "",
            "=" * 60,
        ])

        return "\n".join(linee)

    # --- Test mini-progetto ---
    # Genera dati
    df_vendite: pd.DataFrame = genera_dati_vendite(200, seed=42)
    assert len(df_vendite) == 200
    assert "fatturato" in df_vendite.columns
    assert df_vendite["fatturato"].sum() > 0

    # Analisi
    risultati: dict[str, Any] = analisi_vendite(df_vendite)
    assert risultati["num_transazioni"] == 200
    assert risultati["fatturato_totale"] > 0
    assert risultati["fatturato_medio"] > 0
    assert len(risultati["fatturato_per_categoria"]) == 3
    assert len(risultati["fatturato_per_citta"]) == 5
    assert risultati["prodotto_piu_venduto"] != ""
    assert 1 <= risultati["mese_migliore"] <= 12

    # Report testuale
    report_testo: str = genera_report_testuale(risultati)
    assert "REPORT ANALISI VENDITE" in report_testo
    assert "EUR" in report_testo

    # Genera grafici
    dir_report: str = tempfile.mkdtemp(prefix="report_lab08_")
    percorsi_grafici: list[str] = genera_report_grafici(df_vendite, dir_report)

    assert len(percorsi_grafici) == 5
    for percorso in percorsi_grafici:
        assert os.path.exists(percorso), f"Grafico non trovato: {percorso}"
        assert os.path.getsize(percorso) > 0, f"Grafico vuoto: {percorso}"

    # Stampa il report
    print(report_testo)
    print(f"\nGrafici salvati in: {dir_report}")

    # Pulizia file temporanei
    for nome_file in os.listdir(dir_report):
        os.unlink(os.path.join(dir_report, nome_file))
    os.rmdir(dir_report)

    print("\nEsercizio 2 (Mini-progetto analisi dati): SUPERATO")

else:
    print("Esercizio 2 (Mini-progetto): SALTATO (librerie non disponibili)")


# ============================================================================
esercizi_superati: int = 0
totale: int = 2
if MATPLOTLIB_DISPONIBILE and NUMPY_DISPONIBILE:
    esercizi_superati += 1
if MATPLOTLIB_DISPONIBILE and NUMPY_DISPONIBILE and PANDAS_DISPONIBILE:
    esercizi_superati += 1

print("\n" + "=" * 60)
print(f"LABORATORIO 08: {esercizi_superati}/{totale} ESERCIZI SUPERATI")
if esercizi_superati == totale:
    print("TUTTI GLI ESERCIZI DEL LABORATORIO 08 SUPERATI!")
else:
    print("Installa le librerie mancanti per completare tutti gli esercizi.")
print("=" * 60)
