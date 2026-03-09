# F17 — NumPy, Pandas, visualizzazione
# Esempi per la lezione frontale 17

from __future__ import annotations
import os
import tempfile

# ============================================================
# Importazione condizionale di numpy, pandas, matplotlib
# ============================================================
try:
    import numpy as np
    HAS_NUMPY: bool = True
except ImportError:
    HAS_NUMPY = False
    print("ATTENZIONE: NumPy non installato. Installare con: pip install numpy")

try:
    import pandas as pd
    HAS_PANDAS: bool = True
except ImportError:
    HAS_PANDAS = False
    print("ATTENZIONE: Pandas non installato. Installare con: pip install pandas")

try:
    import matplotlib
    matplotlib.use("Agg")  # backend non interattivo
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB: bool = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("ATTENZIONE: Matplotlib non installato. Installare con: pip install matplotlib")

DIR_TEMP: str = tempfile.mkdtemp(prefix="f17_esempi_")

# ============================================================
# PARTE 1: NUMPY
# ============================================================
if HAS_NUMPY:
    print("\n" + "=" * 60)
    print("PARTE 1: NUMPY")
    print("=" * 60)

    # --- 1.1 Creazione di array ---
    print("\n=== Creazione di array ===")

    # Da lista
    arr1: np.ndarray = np.array([1, 2, 3, 4, 5])
    print(f"Da lista: {arr1}, dtype={arr1.dtype}")

    # Da lista 2D
    matrice: np.ndarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Matrice 3x3:\n{matrice}")
    print(f"  Shape: {matrice.shape}, ndim: {matrice.ndim}")

    # Funzioni di creazione
    zeri: np.ndarray = np.zeros((2, 3))
    uni: np.ndarray = np.ones((3, 2))
    intervallo: np.ndarray = np.arange(0, 10, 2)
    lineare: np.ndarray = np.linspace(0, 1, 5)

    print(f"\nzeros(2,3):\n{zeri}")
    print(f"ones(3,2):\n{uni}")
    print(f"arange(0,10,2): {intervallo}")
    print(f"linspace(0,1,5): {lineare}")

    assert zeri.shape == (2, 3)
    assert np.all(intervallo == np.array([0, 2, 4, 6, 8]))
    assert len(lineare) == 5

    # --- 1.2 Indicizzazione e slicing ---
    print("\n=== Indicizzazione e slicing ===")

    arr: np.ndarray = np.array([10, 20, 30, 40, 50, 60])
    print(f"Array: {arr}")
    print(f"arr[0] = {arr[0]}, arr[-1] = {arr[-1]}")
    print(f"arr[1:4] = {arr[1:4]}")
    print(f"arr[::2] = {arr[::2]}")  # ogni 2 elementi

    # Indicizzazione booleana (fondamentale!)
    mask: np.ndarray = arr > 30
    print(f"\narr > 30: {mask}")
    print(f"arr[arr > 30] = {arr[mask]}")
    assert np.all(arr[mask] == np.array([40, 50, 60]))

    # Indicizzazione matrice
    m: np.ndarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\nMatrice:\n{m}")
    print(f"m[0, 0] = {m[0, 0]}")
    print(f"m[1, :] = {m[1, :]} (seconda riga)")
    print(f"m[:, 2] = {m[:, 2]} (terza colonna)")

    # --- 1.3 Operazioni vettorizzate ---
    print("\n=== Operazioni vettorizzate ===")

    a: np.ndarray = np.array([1.0, 2.0, 3.0, 4.0])
    b: np.ndarray = np.array([10.0, 20.0, 30.0, 40.0])

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"a + b = {a + b}")
    print(f"a * b = {a * b}")  # elemento per elemento!
    print(f"a ** 2 = {a ** 2}")
    print(f"np.sqrt(a) = {np.sqrt(a)}")

    assert np.all(a + b == np.array([11, 22, 33, 44]))

    # Broadcasting: scalare + array
    print(f"\na + 100 = {a + 100}")
    print(f"a * 3 = {a * 3}")

    # --- 1.4 Funzioni statistiche ---
    print("\n=== Funzioni statistiche NumPy ===")

    voti: np.ndarray = np.array([18, 22, 24, 25, 27, 28, 28, 30, 30, 30], dtype=float)
    print(f"Voti: {voti}")
    print(f"  Media:    {np.mean(voti):.2f}")
    print(f"  Mediana:  {np.median(voti):.2f}")
    print(f"  Dev.std:  {np.std(voti, ddof=1):.2f}")  # ddof=1 per campionaria
    print(f"  Varianza: {np.var(voti, ddof=1):.2f}")
    print(f"  Min:      {np.min(voti):.2f}")
    print(f"  Max:      {np.max(voti):.2f}")
    print(f"  Somma:    {np.sum(voti):.2f}")

    assert np.mean(voti) == 26.2
    assert np.min(voti) == 18.0
    assert np.max(voti) == 30.0

    # Percentili
    q1: float = float(np.percentile(voti, 25))
    q3: float = float(np.percentile(voti, 75))
    print(f"  Q1 (25%): {q1:.2f}")
    print(f"  Q3 (75%): {q3:.2f}")
    print(f"  IQR:      {q3 - q1:.2f}")

    # Statistiche per asse (su matrici)
    print("\nStatistiche per asse:")
    voti_matrice: np.ndarray = np.array([
        [28, 30, 25],  # Marco
        [30, 29, 27],  # Laura
        [24, 22, 26],  # Giulia
    ])
    materie: list[str] = ["Mat", "Fis", "Inf"]
    nomi: list[str] = ["Marco", "Laura", "Giulia"]

    medie_studenti: np.ndarray = np.mean(voti_matrice, axis=1)  # media per riga
    medie_materie: np.ndarray = np.mean(voti_matrice, axis=0)   # media per colonna

    for nome, media in zip(nomi, medie_studenti):
        print(f"  Media {nome}: {media:.2f}")
    for materia, media in zip(materie, medie_materie):
        print(f"  Media {materia}: {media:.2f}")

else:
    print("\n[SKIP] Parte NumPy saltata (numpy non installato)")

# ============================================================
# PARTE 2: PANDAS
# ============================================================
if HAS_PANDAS:
    print("\n" + "=" * 60)
    print("PARTE 2: PANDAS")
    print("=" * 60)

    # --- 2.1 Series ---
    print("\n=== Pandas Series ===")

    voti_series: pd.Series = pd.Series(
        [28, 30, 25, 27, 30],
        index=["Marco", "Laura", "Giulia", "Paolo", "Anna"],
        name="voto"
    )
    print(f"Series:\n{voti_series}\n")
    print(f"Media: {voti_series.mean():.2f}")
    print(f"Laura: {voti_series['Laura']}")
    assert voti_series["Laura"] == 30

    # --- 2.2 DataFrame ---
    print("\n=== Pandas DataFrame ===")

    dati: dict[str, list] = {
        "nome": ["Marco", "Laura", "Giulia", "Paolo", "Anna", "Luca", "Sara"],
        "corso": ["Informatica", "Matematica", "Informatica", "Fisica",
                   "Matematica", "Informatica", "Fisica"],
        "voto_mat": [28, 30, 24, 27, 30, 22, 26],
        "voto_fis": [25, 30, 22, 28, 29, 20, 27],
        "voto_inf": [30, 29, 26, 27, 30, 24, 28],
    }
    df: pd.DataFrame = pd.DataFrame(dati)
    print(f"DataFrame:\n{df}\n")
    print(f"Shape: {df.shape}")
    print(f"Colonne: {list(df.columns)}")
    print(f"Tipi:\n{df.dtypes}\n")

    # Statistiche descrittive
    print(f"Describe:\n{df.describe()}\n")

    # --- 2.3 Selezione e filtro ---
    print("=== Selezione e filtro ===")

    # Selezione colonne
    nomi_col: pd.Series = df["nome"]
    print(f"Colonna 'nome':\n{nomi_col.values}\n")

    # Selezione righe con condizione
    voti_alti: pd.DataFrame = df[df["voto_mat"] >= 28]
    print(f"Studenti con voto_mat >= 28:\n{voti_alti}\n")
    assert len(voti_alti) == 3

    # Selezione con .loc (label) e .iloc (posizione)
    prima_riga: pd.Series = df.iloc[0]
    print(f"Prima riga (iloc[0]):\n{prima_riga}\n")

    # --- 2.4 Colonne calcolate ---
    print("=== Colonne calcolate ===")

    df["media"] = (df["voto_mat"] + df["voto_fis"] + df["voto_inf"]) / 3
    print(f"DataFrame con media:\n{df[['nome', 'media']]}\n")

    # --- 2.5 GroupBy ---
    print("=== GroupBy ===")

    grouped: pd.DataFrame = df.groupby("corso")[["voto_mat", "voto_fis", "voto_inf"]].mean()
    print(f"Media voti per corso:\n{grouped}\n")

    conteggio: pd.Series = df.groupby("corso")["nome"].count()
    print(f"Studenti per corso:\n{conteggio}\n")

    # --- 2.6 Ordinamento ---
    print("=== Ordinamento ===")

    df_ordinato: pd.DataFrame = df.sort_values("media", ascending=False)
    print(f"Ordinati per media (decrescente):\n{df_ordinato[['nome', 'media']]}\n")
    assert df_ordinato.iloc[0]["nome"] == "Laura"  # o Anna

    # --- 2.7 Lettura/scrittura CSV ---
    print("=== Lettura/scrittura CSV ===")

    csv_path: str = os.path.join(DIR_TEMP, "studenti_pandas.csv")
    df.to_csv(csv_path, index=False)
    print(f"CSV salvato: {csv_path}")

    df_letto: pd.DataFrame = pd.read_csv(csv_path)
    assert df_letto.shape == df.shape
    print(f"CSV letto: {df_letto.shape[0]} righe, {df_letto.shape[1]} colonne")

else:
    print("\n[SKIP] Parte Pandas saltata (pandas non installato)")

# ============================================================
# PARTE 3: MATPLOTLIB (visualizzazione base)
# ============================================================
if HAS_MATPLOTLIB and HAS_NUMPY:
    print("\n" + "=" * 60)
    print("PARTE 3: MATPLOTLIB")
    print("=" * 60)

    # --- 3.1 Grafico a linee ---
    print("\n=== Grafico a linee ===")

    x: np.ndarray = np.linspace(0, 2 * np.pi, 100)
    y_sin: np.ndarray = np.sin(x)
    y_cos: np.ndarray = np.cos(x)

    fig1, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(x, y_sin, label="sin(x)", color="blue")
    ax1.plot(x, y_cos, label="cos(x)", color="red", linestyle="--")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_title("Funzioni trigonometriche")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    path_linee: str = os.path.join(DIR_TEMP, "grafico_linee.png")
    fig1.savefig(path_linee, dpi=100, bbox_inches="tight")
    plt.close(fig1)
    print(f"Grafico salvato: {path_linee}")

    # --- 3.2 Istogramma ---
    print("\n=== Istogramma ===")

    np.random.seed(42)
    dati_norm: np.ndarray = np.random.normal(loc=26, scale=3, size=200)

    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.hist(dati_norm, bins=20, edgecolor="black", alpha=0.7, color="steelblue")
    ax2.axvline(np.mean(dati_norm), color="red", linestyle="--", label=f"Media: {np.mean(dati_norm):.1f}")
    ax2.set_xlabel("Voto")
    ax2.set_ylabel("Frequenza")
    ax2.set_title("Distribuzione dei voti (simulata)")
    ax2.legend()

    path_isto: str = os.path.join(DIR_TEMP, "istogramma.png")
    fig2.savefig(path_isto, dpi=100, bbox_inches="tight")
    plt.close(fig2)
    print(f"Istogramma salvato: {path_isto}")

    # --- 3.3 Grafico a barre ---
    print("\n=== Grafico a barre ===")

    materie_nomi: list[str] = ["Matematica", "Fisica", "Informatica"]
    medie_val: list[float] = [26.7, 25.9, 27.7]

    fig3, ax3 = plt.subplots(figsize=(8, 5))
    barre = ax3.bar(materie_nomi, medie_val, color=["#4CAF50", "#2196F3", "#FF9800"])
    ax3.set_ylabel("Media voto")
    ax3.set_title("Media voti per materia")
    ax3.set_ylim(20, 31)
    for barra, valore in zip(barre, medie_val):
        ax3.text(barra.get_x() + barra.get_width() / 2, barra.get_height() + 0.2,
                 f"{valore:.1f}", ha="center", va="bottom")

    path_barre: str = os.path.join(DIR_TEMP, "grafico_barre.png")
    fig3.savefig(path_barre, dpi=100, bbox_inches="tight")
    plt.close(fig3)
    print(f"Grafico a barre salvato: {path_barre}")

    # --- 3.4 Scatter plot ---
    print("\n=== Scatter plot ===")

    np.random.seed(42)
    ore_studio: np.ndarray = np.random.uniform(1, 10, 50)
    voti_sim: np.ndarray = 18 + ore_studio * 1.3 + np.random.normal(0, 1.5, 50)
    voti_sim = np.clip(voti_sim, 18, 30)

    fig4, ax4 = plt.subplots(figsize=(8, 5))
    ax4.scatter(ore_studio, voti_sim, alpha=0.6, color="steelblue")
    # Retta di tendenza
    coefficienti: np.ndarray = np.polyfit(ore_studio, voti_sim, 1)
    x_retta: np.ndarray = np.linspace(1, 10, 100)
    y_retta: np.ndarray = np.polyval(coefficienti, x_retta)
    ax4.plot(x_retta, y_retta, color="red", linestyle="--",
             label=f"y = {coefficienti[0]:.2f}x + {coefficienti[1]:.2f}")
    ax4.set_xlabel("Ore di studio")
    ax4.set_ylabel("Voto")
    ax4.set_title("Ore di studio vs Voto")
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    path_scatter: str = os.path.join(DIR_TEMP, "scatter.png")
    fig4.savefig(path_scatter, dpi=100, bbox_inches="tight")
    plt.close(fig4)
    print(f"Scatter plot salvato: {path_scatter}")

else:
    if not HAS_MATPLOTLIB:
        print("\n[SKIP] Parte Matplotlib saltata (matplotlib non installato)")
    elif not HAS_NUMPY:
        print("\n[SKIP] Parte Matplotlib saltata (numpy non installato)")

# ============================================================
# Pulizia
# ============================================================
import shutil
shutil.rmtree(DIR_TEMP)
print(f"\nDirectory temporanea rimossa: {DIR_TEMP}")
print("\n=== Fine esempi F17 ===")
