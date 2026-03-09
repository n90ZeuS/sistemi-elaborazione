# F17 — NumPy, Pandas, visualizzazione
# Esercizi per la lezione frontale 17

from __future__ import annotations
import os
import tempfile

# ============================================================
# Importazione condizionale
# ============================================================
try:
    import numpy as np
    HAS_NUMPY: bool = True
except ImportError:
    HAS_NUMPY = False
    print("ATTENZIONE: NumPy non installato. Installare con: pip install numpy")
    print("  Gli esercizi NumPy verranno saltati.\n")

try:
    import pandas as pd
    HAS_PANDAS: bool = True
except ImportError:
    HAS_PANDAS = False
    print("ATTENZIONE: Pandas non installato. Installare con: pip install pandas")
    print("  Gli esercizi Pandas verranno saltati.\n")

try:
    import matplotlib
    matplotlib.use("Agg")  # backend non interattivo
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB: bool = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("ATTENZIONE: Matplotlib non installato. Installare con: pip install matplotlib")
    print("  I grafici verranno saltati.\n")

DIR_TEMP: str = tempfile.mkdtemp(prefix="f17_esercizi_")

# ============================================================
# ESERCIZIO 1: Pipeline di analisi dati con NumPy
# Analisi statistica completa di un dataset simulato.
# ============================================================
if HAS_NUMPY:
    print("=== Esercizio 1: Analisi dati con NumPy ===")

    # Simulazione dati: voti di 100 studenti in 3 materie
    np.random.seed(42)
    n_studenti: int = 100
    n_materie: int = 3

    # Genera voti realistici (distribuzione normale troncata tra 18 e 30)
    voti_raw: np.ndarray = np.random.normal(loc=25, scale=3, size=(n_studenti, n_materie))
    voti: np.ndarray = np.clip(np.round(voti_raw), 18, 30).astype(int)
    materie: list[str] = ["Matematica", "Fisica", "Informatica"]

    print(f"Dataset: {voti.shape[0]} studenti x {voti.shape[1]} materie")
    print(f"Prime 5 righe:\n{voti[:5]}\n")

    # --- Analisi per materia ---
    print("Statistiche per materia:")
    print(f"{'Materia':<15} {'Media':>7} {'Mediana':>8} {'Std':>7} {'Min':>5} {'Max':>5}")
    print("-" * 50)
    for i, materia in enumerate(materie):
        col: np.ndarray = voti[:, i]
        media: float = float(np.mean(col))
        mediana: float = float(np.median(col))
        std: float = float(np.std(col, ddof=1))
        minimo: int = int(np.min(col))
        massimo: int = int(np.max(col))
        print(f"{materia:<15} {media:>7.2f} {mediana:>8.1f} {std:>7.2f} {minimo:>5} {massimo:>5}")

    # --- Analisi per studente ---
    medie_studenti: np.ndarray = np.mean(voti, axis=1)
    assert medie_studenti.shape == (n_studenti,)

    print(f"\nMedia delle medie degli studenti: {np.mean(medie_studenti):.2f}")
    print(f"Studente con media più alta: #{np.argmax(medie_studenti)} "
          f"(media={np.max(medie_studenti):.2f})")
    print(f"Studente con media più bassa: #{np.argmin(medie_studenti)} "
          f"(media={np.min(medie_studenti):.2f})")

    # --- Correlazione tra materie ---
    print("\nMatrice di correlazione:")
    corr: np.ndarray = np.corrcoef(voti.T)
    assert corr.shape == (3, 3)
    for i, m1 in enumerate(materie):
        valori_str: str = "  ".join(f"{corr[i, j]:>6.3f}" for j in range(n_materie))
        print(f"  {m1:<15} {valori_str}")

    # --- Distribuzione voti ---
    print("\nDistribuzione voti (tutte le materie):")
    tutti_voti: np.ndarray = voti.flatten()
    valori_unici: np.ndarray
    conteggi: np.ndarray
    valori_unici, conteggi = np.unique(tutti_voti, return_counts=True)
    for voto, conteggio in zip(valori_unici, conteggi):
        barra: str = "#" * conteggio
        print(f"  {voto:>2}: {barra} ({conteggio})")

    # --- Percentuale di sufficienze (>= 18) e lodi (30) ---
    totale_voti: int = voti.size
    n_lodi: int = int(np.sum(voti == 30))
    percentuale_lodi: float = n_lodi / totale_voti * 100
    print(f"\nVoti totali: {totale_voti}")
    print(f"Lodi (30): {n_lodi} ({percentuale_lodi:.1f}%)")

    # Studenti con tutti 30
    tutti_trenta: np.ndarray = np.all(voti == 30, axis=1)
    n_tutti_trenta: int = int(np.sum(tutti_trenta))
    print(f"Studenti con tutti 30: {n_tutti_trenta}")

    # Verifica: nessun voto fuori range
    assert np.all(voti >= 18)
    assert np.all(voti <= 30)

    print("\nEsercizio 1 superato!\n")

else:
    print("[SKIP] Esercizio 1 saltato (numpy non installato)\n")

# ============================================================
# ESERCIZIO 2: Analisi con Pandas e GroupBy
# Creare un DataFrame, analizzare con groupby e aggregazioni.
# ============================================================
if HAS_PANDAS:
    print("=== Esercizio 2: Pandas GroupBy e aggregazioni ===")

    # Creazione dataset
    dati: dict[str, list] = {
        "studente": [
            "Marco", "Laura", "Giulia", "Paolo", "Anna",
            "Luca", "Sara", "Davide", "Elena", "Matteo",
            "Chiara", "Fabio", "Valentina", "Andrea", "Silvia",
        ],
        "corso": [
            "Informatica", "Matematica", "Informatica", "Fisica", "Matematica",
            "Informatica", "Fisica", "Matematica", "Informatica", "Fisica",
            "Matematica", "Informatica", "Fisica", "Matematica", "Informatica",
        ],
        "anno": [1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1],
        "voto_mat": [28, 30, 24, 27, 30, 22, 26, 29, 25, 28, 30, 20, 27, 28, 26],
        "voto_fis": [25, 30, 22, 28, 29, 20, 27, 27, 23, 30, 28, 18, 29, 26, 24],
        "voto_inf": [30, 29, 26, 27, 30, 24, 28, 28, 27, 25, 29, 22, 26, 27, 30],
    }

    df: pd.DataFrame = pd.DataFrame(dati)
    print(f"DataFrame:\n{df}\n")

    # --- Colonna media calcolata ---
    df["media"] = (df["voto_mat"] + df["voto_fis"] + df["voto_inf"]) / 3
    df["media"] = df["media"].round(2)

    # --- GroupBy per corso ---
    print("=== Statistiche per corso ===")
    stats_corso: pd.DataFrame = df.groupby("corso").agg(
        n_studenti=("studente", "count"),
        media_mat=("voto_mat", "mean"),
        media_fis=("voto_fis", "mean"),
        media_inf=("voto_inf", "mean"),
        media_globale=("media", "mean"),
    ).round(2)
    print(f"{stats_corso}\n")

    assert stats_corso.loc["Informatica", "n_studenti"] == 6
    assert stats_corso.loc["Matematica", "n_studenti"] == 5
    assert stats_corso.loc["Fisica", "n_studenti"] == 4

    # --- GroupBy per anno ---
    print("=== Statistiche per anno ===")
    stats_anno: pd.DataFrame = df.groupby("anno").agg(
        n_studenti=("studente", "count"),
        media_globale=("media", "mean"),
        voto_max=("media", "max"),
        voto_min=("media", "min"),
    ).round(2)
    print(f"{stats_anno}\n")

    # --- GroupBy multiplo (corso x anno) ---
    print("=== Studenti per corso e anno ===")
    pivot: pd.DataFrame = df.pivot_table(
        values="media",
        index="corso",
        columns="anno",
        aggfunc="mean"
    ).round(2)
    print(f"{pivot}\n")

    # --- Top studenti per corso ---
    print("=== Miglior studente per corso ===")
    for corso, gruppo in df.groupby("corso"):
        migliore: pd.Series = gruppo.loc[gruppo["media"].idxmax()]
        print(f"  {corso}: {migliore['studente']} (media: {migliore['media']:.2f})")

    # --- Filtri combinati ---
    eccellenti: pd.DataFrame = df[
        (df["media"] >= 28) & (df["anno"] >= 2)
    ].sort_values("media", ascending=False)
    print(f"\nEccellenti (media >= 28, anno >= 2):")
    print(f"{eccellenti[['studente', 'corso', 'anno', 'media']]}\n")

    # --- Esportazione CSV ---
    csv_output: str = os.path.join(DIR_TEMP, "analisi_studenti.csv")
    df.to_csv(csv_output, index=False)
    print(f"CSV esportato: {csv_output}")

    # Verifica rileggendo
    df_riletto: pd.DataFrame = pd.read_csv(csv_output)
    assert df_riletto.shape == df.shape

    print("\nEsercizio 2 superato!\n")

else:
    print("[SKIP] Esercizio 2 saltato (pandas non installato)\n")

# ============================================================
# ESERCIZIO 3: Visualizzazione dati
# Creare grafici riepilogativi dei dati analizzati.
# ============================================================
if HAS_MATPLOTLIB and HAS_PANDAS and HAS_NUMPY:
    print("=== Esercizio 3: Visualizzazione ===")

    # Usiamo il DataFrame dall'esercizio 2 (già creato sopra)

    # --- 3.1 Grafico a barre: media per corso ---
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    medie_corso: pd.Series = df.groupby("corso")["media"].mean()
    colori: list[str] = ["#4CAF50", "#2196F3", "#FF9800"]
    barre = ax1.bar(medie_corso.index, medie_corso.values, color=colori)
    ax1.set_ylabel("Media voto")
    ax1.set_title("Media voti per corso di laurea")
    ax1.set_ylim(20, 31)
    for barra, valore in zip(barre, medie_corso.values):
        ax1.text(barra.get_x() + barra.get_width() / 2, barra.get_height() + 0.2,
                 f"{valore:.1f}", ha="center", va="bottom", fontweight="bold")

    path_barre: str = os.path.join(DIR_TEMP, "media_per_corso.png")
    fig1.savefig(path_barre, dpi=100, bbox_inches="tight")
    plt.close(fig1)
    print(f"Grafico barre salvato: {path_barre}")

    # --- 3.2 Box plot: distribuzione voti per materia ---
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    dati_box: list[pd.Series] = [df["voto_mat"], df["voto_fis"], df["voto_inf"]]
    bp = ax2.boxplot(dati_box, labels=["Matematica", "Fisica", "Informatica"],
                     patch_artist=True)
    colors_box: list[str] = ["#81C784", "#64B5F6", "#FFB74D"]
    for patch, color in zip(bp["boxes"], colors_box):
        patch.set_facecolor(color)
    ax2.set_ylabel("Voto")
    ax2.set_title("Distribuzione voti per materia")
    ax2.grid(True, alpha=0.3, axis="y")

    path_box: str = os.path.join(DIR_TEMP, "boxplot_materie.png")
    fig2.savefig(path_box, dpi=100, bbox_inches="tight")
    plt.close(fig2)
    print(f"Box plot salvato: {path_box}")

    # --- 3.3 Scatter: relazione tra voti matematica e informatica ---
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    for corso, gruppo in df.groupby("corso"):
        ax3.scatter(gruppo["voto_mat"], gruppo["voto_inf"],
                    label=corso, alpha=0.7, s=80)
    ax3.set_xlabel("Voto Matematica")
    ax3.set_ylabel("Voto Informatica")
    ax3.set_title("Voto Matematica vs Informatica")
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # Retta di tendenza
    coeffs: np.ndarray = np.polyfit(df["voto_mat"].values, df["voto_inf"].values, 1)
    x_line: np.ndarray = np.linspace(df["voto_mat"].min(), df["voto_mat"].max(), 100)
    y_line: np.ndarray = np.polyval(coeffs, x_line)
    ax3.plot(x_line, y_line, "r--", alpha=0.5,
             label=f"Tendenza (r={np.corrcoef(df['voto_mat'], df['voto_inf'])[0,1]:.2f})")
    ax3.legend()

    path_scatter: str = os.path.join(DIR_TEMP, "scatter_mat_inf.png")
    fig3.savefig(path_scatter, dpi=100, bbox_inches="tight")
    plt.close(fig3)
    print(f"Scatter plot salvato: {path_scatter}")

    # --- 3.4 Subplot multipli ---
    fig4, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig4.suptitle("Istogrammi dei voti per materia", fontsize=14)

    materie_plot: list[tuple[str, str]] = [
        ("voto_mat", "Matematica"),
        ("voto_fis", "Fisica"),
        ("voto_inf", "Informatica"),
    ]

    for ax, (col, titolo) in zip(axes, materie_plot):
        ax.hist(df[col], bins=range(18, 32), edgecolor="black", alpha=0.7,
                color="steelblue")
        media_val: float = df[col].mean()
        ax.axvline(media_val, color="red", linestyle="--",
                   label=f"Media: {media_val:.1f}")
        ax.set_xlabel("Voto")
        ax.set_ylabel("Frequenza")
        ax.set_title(titolo)
        ax.legend()

    fig4.tight_layout()
    path_subplots: str = os.path.join(DIR_TEMP, "istogrammi_materie.png")
    fig4.savefig(path_subplots, dpi=100, bbox_inches="tight")
    plt.close(fig4)
    print(f"Subplots salvati: {path_subplots}")

    print("\nEsercizio 3 superato!")

elif not HAS_MATPLOTLIB:
    print("[SKIP] Esercizio 3 saltato (matplotlib non installato)")
elif not HAS_PANDAS:
    print("[SKIP] Esercizio 3 saltato (pandas non installato)")
else:
    print("[SKIP] Esercizio 3 saltato (numpy non installato)")

# ============================================================
# Pulizia
# ============================================================
import shutil
shutil.rmtree(DIR_TEMP)
print(f"\nDirectory temporanea rimossa: {DIR_TEMP}")
print("\n=== Tutti gli esercizi F17 completati! ===")
