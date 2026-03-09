# L07 — NumPy e Pandas
# Esercizi per il laboratorio 07
#
# Esercizi pratici di calcolo numerico con NumPy e manipolazione dati con Pandas.
# Le importazioni sono protette da try/except per gestire ambienti senza le librerie.
# Ogni esercizio include assert per verificare la correttezza.

import math

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
    import pandas as pd
    PANDAS_DISPONIBILE: bool = True
except ImportError:
    PANDAS_DISPONIBILE = False
    print("ATTENZIONE: Pandas non e' installato. Installa con: pip install pandas")


# ============================================================================
# ESERCIZIO 1: Operazioni su matrici con NumPy
# ============================================================================

if NUMPY_DISPONIBILE:

    def crea_matrice_identita(n: int) -> np.ndarray:
        """Crea una matrice identita' n x n."""
        return np.eye(n)

    def somma_matrici_np(a: np.ndarray, b: np.ndarray) -> np.ndarray:
        """Somma elemento per elemento di due matrici."""
        if a.shape != b.shape:
            raise ValueError(f"Dimensioni incompatibili: {a.shape} vs {b.shape}")
        return a + b

    def prodotto_matrici_np(a: np.ndarray, b: np.ndarray) -> np.ndarray:
        """Prodotto matriciale (dot product)."""
        if a.shape[1] != b.shape[0]:
            raise ValueError(
                f"Colonne di A ({a.shape[1]}) != Righe di B ({b.shape[0]})"
            )
        return a @ b  # equivalente a np.dot(a, b)

    def trasposta_np(matrice: np.ndarray) -> np.ndarray:
        """Calcola la trasposta di una matrice."""
        return matrice.T

    def determinante_np(matrice: np.ndarray) -> float:
        """Calcola il determinante di una matrice quadrata."""
        if matrice.shape[0] != matrice.shape[1]:
            raise ValueError("Il determinante e' definito solo per matrici quadrate")
        return float(np.linalg.det(matrice))

    def inversa_np(matrice: np.ndarray) -> np.ndarray:
        """Calcola l'inversa di una matrice quadrata."""
        det: float = determinante_np(matrice)
        if abs(det) < 1e-10:
            raise ValueError("La matrice e' singolare (determinante = 0)")
        return np.linalg.inv(matrice)

    def risolvi_sistema(a: np.ndarray, b: np.ndarray) -> np.ndarray:
        """
        Risolve il sistema lineare Ax = b.
        Restituisce il vettore x.
        """
        return np.linalg.solve(a, b)

    # --- Test operazioni matrici NumPy ---
    m1: np.ndarray = np.array([[1, 2], [3, 4]], dtype=float)
    m2: np.ndarray = np.array([[5, 6], [7, 8]], dtype=float)

    # Somma
    somma: np.ndarray = somma_matrici_np(m1, m2)
    assert np.array_equal(somma, np.array([[6, 8], [10, 12]]))

    # Prodotto: [[1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]] = [[19, 22], [43, 50]]
    prodotto: np.ndarray = prodotto_matrici_np(m1, m2)
    assert np.array_equal(prodotto, np.array([[19, 22], [43, 50]]))

    # Trasposta
    t: np.ndarray = trasposta_np(m1)
    assert np.array_equal(t, np.array([[1, 3], [2, 4]]))

    # Determinante di m1: 1*4 - 2*3 = -2
    det: float = determinante_np(m1)
    assert abs(det - (-2.0)) < 1e-9

    # Inversa: A * A^(-1) = I
    inv_m1: np.ndarray = inversa_np(m1)
    identita_calcolata: np.ndarray = prodotto_matrici_np(m1, inv_m1)
    identita_attesa: np.ndarray = crea_matrice_identita(2)
    assert np.allclose(identita_calcolata, identita_attesa)

    # Risolvi sistema: 2x + y = 5, x + 3y = 7 -> x = 1.6, y = 1.8
    a_sist: np.ndarray = np.array([[2, 1], [1, 3]], dtype=float)
    b_sist: np.ndarray = np.array([5, 7], dtype=float)
    x_sist: np.ndarray = risolvi_sistema(a_sist, b_sist)
    assert abs(x_sist[0] - 1.6) < 1e-9
    assert abs(x_sist[1] - 1.8) < 1e-9

    print("Esercizio 1 (Matrici NumPy): SUPERATO")
else:
    print("Esercizio 1 (Matrici NumPy): SALTATO (NumPy non disponibile)")


# ============================================================================
# ESERCIZIO 2: Analisi statistica con NumPy
# ============================================================================

if NUMPY_DISPONIBILE:

    def statistiche_numpy(dati: np.ndarray) -> dict[str, float]:
        """
        Calcola statistiche descrittive di un array con NumPy.
        Piu' efficiente e preciso delle implementazioni manuali.
        """
        return {
            "n": float(len(dati)),
            "media": float(np.mean(dati)),
            "mediana": float(np.median(dati)),
            "dev_std": float(np.std(dati, ddof=1)),     # campionaria
            "varianza": float(np.var(dati, ddof=1)),     # campionaria
            "minimo": float(np.min(dati)),
            "massimo": float(np.max(dati)),
            "q1": float(np.percentile(dati, 25)),
            "q3": float(np.percentile(dati, 75)),
        }

    def genera_dati_normali(
        media: float, dev_std: float, n: int, seed: int = 42
    ) -> np.ndarray:
        """Genera n dati da una distribuzione normale."""
        rng: np.random.Generator = np.random.default_rng(seed)
        return rng.normal(media, dev_std, n)

    def normalizza(dati: np.ndarray) -> np.ndarray:
        """Normalizzazione z-score: (x - media) / dev_std."""
        m: float = float(np.mean(dati))
        s: float = float(np.std(dati))
        if s == 0:
            raise ValueError("Deviazione standard zero: impossibile normalizzare")
        return (dati - m) / s

    def correlazione(x: np.ndarray, y: np.ndarray) -> float:
        """Calcola il coefficiente di correlazione di Pearson tra x e y."""
        if len(x) != len(y):
            raise ValueError("Le serie devono avere la stessa lunghezza")
        matrice_corr: np.ndarray = np.corrcoef(x, y)
        return float(matrice_corr[0, 1])

    # --- Test analisi statistica ---
    # Genera dati con seed per riproducibilita'
    dati_norm: np.ndarray = genera_dati_normali(100.0, 15.0, 1000, seed=42)

    stats: dict[str, float] = statistiche_numpy(dati_norm)
    assert stats["n"] == 1000.0
    # Con 1000 campioni, la media dovrebbe essere vicina a 100
    assert abs(stats["media"] - 100.0) < 2.0, f"Media troppo lontana da 100: {stats['media']}"
    # La dev_std dovrebbe essere vicina a 15
    assert abs(stats["dev_std"] - 15.0) < 2.0, f"Dev std troppo lontana da 15: {stats['dev_std']}"

    # Normalizzazione: i dati normalizzati devono avere media ~0 e std ~1
    dati_normalizzati: np.ndarray = normalizza(dati_norm)
    assert abs(float(np.mean(dati_normalizzati))) < 1e-10
    assert abs(float(np.std(dati_normalizzati)) - 1.0) < 1e-10

    # Correlazione: dati perfettamente correlati
    x_test: np.ndarray = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y_test: np.ndarray = np.array([2.0, 4.0, 6.0, 8.0, 10.0])  # y = 2x
    assert abs(correlazione(x_test, y_test) - 1.0) < 1e-9  # correlazione perfetta

    # Correlazione negativa
    y_neg: np.ndarray = np.array([10.0, 8.0, 6.0, 4.0, 2.0])
    assert abs(correlazione(x_test, y_neg) - (-1.0)) < 1e-9

    print("Esercizio 2 (Statistiche NumPy): SUPERATO")
else:
    print("Esercizio 2 (Statistiche NumPy): SALTATO (NumPy non disponibile)")


# ============================================================================
# ESERCIZIO 3: Manipolazione DataFrame con Pandas
# ============================================================================

if PANDAS_DISPONIBILE:

    def crea_dataframe_studenti() -> pd.DataFrame:
        """
        Crea un DataFrame di esempio con dati di studenti.
        Colonne: nome, cognome, eta, voto_medio, corso_laurea, anno
        """
        dati: dict[str, list] = {
            "nome": ["Alice", "Bob", "Carla", "Davide", "Eva",
                     "Fabio", "Giulia", "Hasan", "Irene", "Luca"],
            "cognome": ["Rossi", "Bianchi", "Verdi", "Neri", "Gialli",
                        "Blu", "Rosa", "Marroni", "Viola", "Grigi"],
            "eta": [22, 24, 21, 23, 22, 25, 21, 23, 24, 22],
            "voto_medio": [28.5, 24.0, 29.0, 22.5, 27.0,
                           25.5, 30.0, 23.0, 26.5, 28.0],
            "corso_laurea": ["Informatica", "Matematica", "Informatica",
                             "Fisica", "Informatica", "Matematica",
                             "Informatica", "Fisica", "Matematica", "Informatica"],
            "anno": [2, 3, 1, 2, 2, 3, 1, 2, 3, 2],
        }
        return pd.DataFrame(dati)

    def filtra_per_corso(df: pd.DataFrame, corso: str) -> pd.DataFrame:
        """Filtra il DataFrame per corso di laurea."""
        return df[df["corso_laurea"] == corso].reset_index(drop=True)

    def media_per_corso(df: pd.DataFrame) -> pd.Series:
        """Calcola la media del voto_medio raggruppata per corso."""
        return df.groupby("corso_laurea")["voto_medio"].mean().round(2)

    def studenti_migliori(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
        """Restituisce i top n studenti per voto_medio."""
        return df.nlargest(n, "voto_medio")[["nome", "cognome", "voto_medio"]].reset_index(drop=True)

    def aggiungi_colonna_lode(df: pd.DataFrame) -> pd.DataFrame:
        """Aggiunge una colonna 'lode' che e' True se voto_medio >= 28."""
        df_copia: pd.DataFrame = df.copy()
        df_copia["lode"] = df_copia["voto_medio"] >= 28.0
        return df_copia

    def statistiche_per_gruppo(df: pd.DataFrame, colonna_gruppo: str) -> pd.DataFrame:
        """Calcola statistiche aggregate per gruppo."""
        return df.groupby(colonna_gruppo)["voto_medio"].agg(
            ["mean", "std", "min", "max", "count"]
        ).round(2)

    # --- Test DataFrame ---
    df: pd.DataFrame = crea_dataframe_studenti()
    assert len(df) == 10
    assert list(df.columns) == ["nome", "cognome", "eta", "voto_medio", "corso_laurea", "anno"]

    # Filtra per corso
    info: pd.DataFrame = filtra_per_corso(df, "Informatica")
    assert len(info) == 5
    assert all(info["corso_laurea"] == "Informatica")

    # Media per corso
    medie: pd.Series = media_per_corso(df)
    assert "Informatica" in medie.index
    assert "Matematica" in medie.index
    # Informatica: (28.5+29+27+30+28)/5 = 28.5
    assert abs(medie["Informatica"] - 28.5) < 0.01

    # Top studenti
    top: pd.DataFrame = studenti_migliori(df, 3)
    assert len(top) == 3
    assert top.iloc[0]["nome"] == "Giulia"  # voto 30.0

    # Colonna lode
    df_lode: pd.DataFrame = aggiungi_colonna_lode(df)
    assert "lode" in df_lode.columns
    num_con_lode: int = int(df_lode["lode"].sum())
    assert num_con_lode == 4  # Alice(28.5), Carla(29), Giulia(30), Luca(28)

    # Statistiche per gruppo
    stats_gruppo: pd.DataFrame = statistiche_per_gruppo(df, "corso_laurea")
    assert "Informatica" in stats_gruppo.index
    assert "mean" in stats_gruppo.columns

    print("Esercizio 3 (DataFrame Pandas): SUPERATO")
else:
    print("Esercizio 3 (DataFrame Pandas): SALTATO (Pandas non disponibile)")


# ============================================================================
# ESERCIZIO 4: Pulizia dati (Data Cleaning)
# ============================================================================

if PANDAS_DISPONIBILE and NUMPY_DISPONIBILE:

    def crea_dati_sporchi() -> pd.DataFrame:
        """
        Crea un DataFrame con dati 'sporchi' per praticare la pulizia:
        - valori mancanti (NaN)
        - duplicati
        - tipi inconsistenti
        - outlier
        """
        dati: dict[str, list] = {
            "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 5],
            "temperatura": [36.5, 37.0, np.nan, 38.2, 36.8,
                            99.9, 37.1, np.nan, 36.9, 37.5, 36.5, 36.8],
            "pressione": [120, 130, 125, np.nan, 118,
                          122, 135, 128, np.nan, 115, 125, 118],
            "frequenza_cardiaca": [72, 80, 68, 75, np.nan,
                                   85, 90, 73, 78, 65, 68, np.nan],
            "note": ["ok", "ok", "ok", "febbre", "ok",
                     "errore sensore", "ok", "ok", "ok", "ok", "ok", "ok"],
        }
        return pd.DataFrame(dati)

    def rimuovi_duplicati(df: pd.DataFrame, colonna_id: str) -> pd.DataFrame:
        """Rimuove le righe duplicate basandosi sulla colonna ID, tenendo la prima."""
        return df.drop_duplicates(subset=[colonna_id], keep="first").reset_index(drop=True)

    def riempi_mancanti_media(df: pd.DataFrame, colonne: list[str]) -> pd.DataFrame:
        """Riempie i valori mancanti con la media della colonna."""
        df_pulito: pd.DataFrame = df.copy()
        for col in colonne:
            if col in df_pulito.columns:
                media_col: float = df_pulito[col].mean()
                df_pulito[col] = df_pulito[col].fillna(media_col).round(1)
        return df_pulito

    def rimuovi_outlier_iqr(df: pd.DataFrame, colonna: str) -> pd.DataFrame:
        """
        Rimuove outlier usando il metodo IQR (InterQuartile Range).
        Outlier = valori sotto Q1 - 1.5*IQR o sopra Q3 + 1.5*IQR
        """
        q1: float = float(df[colonna].quantile(0.25))
        q3: float = float(df[colonna].quantile(0.75))
        iqr: float = q3 - q1
        limite_inf: float = q1 - 1.5 * iqr
        limite_sup: float = q3 + 1.5 * iqr

        maschera: pd.Series = (df[colonna] >= limite_inf) & (df[colonna] <= limite_sup)
        return df[maschera].reset_index(drop=True)

    def pipeline_pulizia(df: pd.DataFrame) -> pd.DataFrame:
        """
        Pipeline completa di pulizia dati:
        1. Rimuovi duplicati
        2. Rimuovi outlier dalla temperatura
        3. Riempi valori mancanti con la media
        """
        # Passo 1: rimuovi duplicati
        df_clean: pd.DataFrame = rimuovi_duplicati(df, "id")

        # Passo 2: rimuovi outlier dalla temperatura (prima di calcolare la media)
        df_clean = rimuovi_outlier_iqr(df_clean, "temperatura")

        # Passo 3: riempi valori mancanti
        df_clean = riempi_mancanti_media(
            df_clean, ["temperatura", "pressione", "frequenza_cardiaca"]
        )

        return df_clean

    # --- Test pulizia dati ---
    df_sporco: pd.DataFrame = crea_dati_sporchi()
    assert len(df_sporco) == 12  # include duplicati

    # Test rimuovi duplicati
    df_no_dup: pd.DataFrame = rimuovi_duplicati(df_sporco, "id")
    assert len(df_no_dup) == 10  # rimossi 2 duplicati

    # Test pipeline completa
    df_pulito: pd.DataFrame = pipeline_pulizia(df_sporco)

    # Non ci devono essere NaN dopo la pulizia
    assert df_pulito["temperatura"].isna().sum() == 0
    assert df_pulito["pressione"].isna().sum() == 0
    assert df_pulito["frequenza_cardiaca"].isna().sum() == 0

    # L'outlier 99.9 deve essere stato rimosso
    assert (df_pulito["temperatura"] > 50).sum() == 0

    # Non ci devono essere duplicati
    assert df_pulito["id"].is_unique

    print("Esercizio 4 (Pulizia dati): SUPERATO")
else:
    print("Esercizio 4 (Pulizia dati): SALTATO (NumPy/Pandas non disponibili)")


# ============================================================================
esercizi_superati: int = 0
totale: int = 4
if NUMPY_DISPONIBILE:
    esercizi_superati += 2
if PANDAS_DISPONIBILE:
    esercizi_superati += 1
if PANDAS_DISPONIBILE and NUMPY_DISPONIBILE:
    esercizi_superati += 1

print("\n" + "=" * 60)
print(f"LABORATORIO 07: {esercizi_superati}/{totale} ESERCIZI SUPERATI")
if esercizi_superati == totale:
    print("TUTTI GLI ESERCIZI DEL LABORATORIO 07 SUPERATI!")
else:
    print("Installa le librerie mancanti per completare tutti gli esercizi.")
print("=" * 60)
