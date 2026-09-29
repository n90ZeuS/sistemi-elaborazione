# T08 — Operatori, I/O e condizionali
# Esercizi per la lezione frontale 8
# Calcolatrice, classificatore voti, anno bisestile, discriminante

# =============================================================================
# Esercizio 1: Calcolatrice con quattro operazioni
# Implementare una funzione che esegue le quattro operazioni base
# e gestisce la divisione per zero.
# =============================================================================
print("--- Esercizio 1: Calcolatrice ---")


def calcolatrice(a: float, b: float, operazione: str) -> float | str:
    """
    Esegue un'operazione aritmetica tra due numeri.
    Restituisce il risultato come float, oppure un messaggio di errore (str)
    in caso di operazione non valida o divisione per zero.
    """
    if operazione == "+":
        risultato: float = a + b
    elif operazione == "-":
        risultato = a - b
    elif operazione == "*":
        risultato = a * b
    elif operazione == "/":
        if b == 0:
            return "Errore: divisione per zero"
        risultato = a / b
    elif operazione == "//":
        if b == 0:
            return "Errore: divisione per zero"
        risultato = a // b
    elif operazione == "%":
        if b == 0:
            return "Errore: divisione per zero"
        risultato = a % b
    elif operazione == "**":
        risultato = a ** b
    else:
        return f"Errore: operazione '{operazione}' non riconosciuta"
    return risultato


# Test operazioni base
assert calcolatrice(10, 3, "+") == 13
assert calcolatrice(10, 3, "-") == 7
assert calcolatrice(10, 3, "*") == 30
assert abs(calcolatrice(10, 3, "/") - 3.3333333) < 1e-5
assert calcolatrice(10, 3, "//") == 3
assert calcolatrice(10, 3, "%") == 1
assert calcolatrice(2, 10, "**") == 1024

# Test divisione per zero
assert calcolatrice(5, 0, "/") == "Errore: divisione per zero"
assert calcolatrice(5, 0, "//") == "Errore: divisione per zero"
assert calcolatrice(5, 0, "%") == "Errore: divisione per zero"

# Test operazione non valida
assert "Errore" in str(calcolatrice(5, 3, "§"))

# Dimostrazione
operazioni: list[str] = ["+", "-", "*", "/", "//", "%", "**"]
for op in operazioni:
    risultato = calcolatrice(10, 3, op)
    print(f"  10 {op:>2} 3 = {risultato}")

print("  Esercizio 1 superato!\n")


# =============================================================================
# Esercizio 2: Classificatore di voti con statistiche
# Data una lista di voti, classificare ciascuno e produrre statistiche.
# =============================================================================
print("--- Esercizio 2: Classificatore di voti ---")


def classifica_voto(voto: int) -> str:
    """Classifica un voto in scala 0-30 (sistema universitario italiano)."""
    if voto < 0 or voto > 30:
        return "Non valido"
    elif voto < 18:
        return "Insufficiente"
    elif voto < 22:
        return "Sufficiente"
    elif voto < 26:
        return "Discreto"
    elif voto < 29:
        return "Buono"
    elif voto <= 30:
        return "Ottimo"
    return "Non valido"  # Non raggiungibile, ma per completezza


def statistiche_classe(voti: list[int]) -> dict[str, float | int]:
    """Calcola statistiche aggregate di una lista di voti."""
    validi: list[int] = [v for v in voti if 0 <= v <= 30]
    sufficienti: list[int] = [v for v in validi if v >= 18]

    n_totali: int = len(validi)
    n_sufficienti: int = len(sufficienti)
    media: float = sum(validi) / n_totali if n_totali > 0 else 0.0
    tasso_promozione: float = n_sufficienti / n_totali * 100 if n_totali > 0 else 0.0

    return {
        "n_totali": n_totali,
        "n_sufficienti": n_sufficienti,
        "media": round(media, 2),
        "min": min(validi),
        "max": max(validi),
        "tasso_promozione": round(tasso_promozione, 1),
    }


# Test classificazione singola
assert classifica_voto(30) == "Ottimo"
assert classifica_voto(28) == "Buono"
assert classifica_voto(24) == "Discreto"
assert classifica_voto(19) == "Sufficiente"
assert classifica_voto(10) == "Insufficiente"
assert classifica_voto(-1) == "Non valido"
assert classifica_voto(31) == "Non valido"

# Test statistiche
voti_classe: list[int] = [28, 30, 18, 15, 22, 27, 30, 10, 25, 20, 19, 24]
stats: dict[str, float | int] = statistiche_classe(voti_classe)

assert stats["n_totali"] == 12
assert stats["n_sufficienti"] == 10  # 15 e 10 sono insufficienti
assert stats["min"] == 10
assert stats["max"] == 30
assert stats["media"] == 22.33

print(f"  Voti: {voti_classe}")
print(f"  Statistiche: {stats}")

# Distribuzione per categoria
categorie: dict[str, int] = {}
for v in voti_classe:
    cat: str = classifica_voto(v)
    categorie[cat] = categorie.get(cat, 0) + 1

print(f"  Distribuzione: {categorie}")
print("  Esercizio 2 superato!\n")


# =============================================================================
# Esercizio 3: Verifica anno bisestile
# Un anno e' bisestile se:
#   - divisibile per 4 E
#   - (NON divisibile per 100 OPPURE divisibile per 400)
# =============================================================================
print("--- Esercizio 3: Anno bisestile ---")


def is_bisestile(anno: int) -> bool:
    """Verifica se un anno e' bisestile."""
    risultato: bool = (anno % 4 == 0) and (anno % 100 != 0 or anno % 400 == 0)
    return risultato


# Test casi noti
assert is_bisestile(2000) is True    # Divisibile per 400
assert is_bisestile(1900) is False   # Divisibile per 100 ma non per 400
assert is_bisestile(2024) is True    # Divisibile per 4 ma non per 100
assert is_bisestile(2023) is False   # Non divisibile per 4
assert is_bisestile(2100) is False   # Divisibile per 100 ma non per 400
assert is_bisestile(2400) is True    # Divisibile per 400
assert is_bisestile(1) is False

# Contare quanti anni bisestili ci sono in un secolo
bisestili_xxi: list[int] = [a for a in range(2000, 2100) if is_bisestile(a)]
assert len(bisestili_xxi) == 25
assert bisestili_xxi[0] == 2000
assert bisestili_xxi[-1] == 2096

print(f"  2000 bisestile? {is_bisestile(2000)}")
print(f"  1900 bisestile? {is_bisestile(1900)}")
print(f"  2024 bisestile? {is_bisestile(2024)}")
print(f"  Anni bisestili nel XXI secolo (2000-2099): {len(bisestili_xxi)}")
print(f"  Primi 5: {bisestili_xxi[:5]}")
print("  Esercizio 3 superato!\n")


# =============================================================================
# Esercizio 4: Discriminante dell'equazione quadratica
# Data ax^2 + bx + c = 0, calcolare il discriminante e classificare le soluzioni.
# Delta = b^2 - 4ac
# =============================================================================
print("--- Esercizio 4: Discriminante equazione quadratica ---")

import math


def analizza_equazione(
    a: float, b: float, c: float
) -> dict[str, float | str | tuple[float, ...] | None]:
    """
    Analizza l'equazione ax^2 + bx + c = 0.
    Restituisce un dizionario con il discriminante, il tipo di soluzione e le soluzioni.
    """
    if a == 0:
        # Non e' un'equazione di secondo grado
        if b == 0:
            tipo: str = "degenere"
            soluzioni: tuple[float, ...] | None = None
        else:
            tipo = "lineare"
            soluzioni = (-c / b,)
        return {"delta": None, "tipo": tipo, "soluzioni": soluzioni}

    delta: float = b ** 2 - 4 * a * c

    if delta > 0:
        tipo = "due reali distinte"
        x1: float = (-b + math.sqrt(delta)) / (2 * a)
        x2: float = (-b - math.sqrt(delta)) / (2 * a)
        soluzioni = (round(x1, 6), round(x2, 6))
    elif delta == 0:
        tipo = "due reali coincidenti"
        x1 = -b / (2 * a)
        soluzioni = (round(x1, 6),)
    else:
        tipo = "complesse coniugate"
        parte_reale: float = -b / (2 * a)
        parte_imm: float = math.sqrt(-delta) / (2 * a)
        # Restituiamo la rappresentazione come stringhe
        soluzioni = None  # Le soluzioni complesse non sono float

    return {"delta": round(delta, 6), "tipo": tipo, "soluzioni": soluzioni}


# Test: x^2 - 5x + 6 = 0 → x = 2, x = 3
r1: dict = analizza_equazione(1, -5, 6)
assert r1["delta"] == 1.0
assert r1["tipo"] == "due reali distinte"
assert r1["soluzioni"] == (3.0, 2.0)

# Test: x^2 - 4x + 4 = 0 → x = 2 (doppia)
r2: dict = analizza_equazione(1, -4, 4)
assert r2["delta"] == 0.0
assert r2["tipo"] == "due reali coincidenti"
assert r2["soluzioni"] == (2.0,)

# Test: x^2 + 1 = 0 → soluzioni complesse
r3: dict = analizza_equazione(1, 0, 1)
assert r3["delta"] == -4.0
assert r3["tipo"] == "complesse coniugate"

# Test: caso lineare (a=0)
r4: dict = analizza_equazione(0, 2, -6)
assert r4["tipo"] == "lineare"
assert r4["soluzioni"] == (3.0,)

# Stampa risultati
equazioni: list[tuple[float, float, float]] = [
    (1, -5, 6),
    (1, -4, 4),
    (1, 0, 1),
    (2, -7, 3),
]

for a_coeff, b_coeff, c_coeff in equazioni:
    ris: dict = analizza_equazione(a_coeff, b_coeff, c_coeff)
    eq_str: str = f"{a_coeff}x^2 + {b_coeff}x + {c_coeff} = 0"
    print(f"  {eq_str:<25} delta={str(ris['delta']):>8}  → {ris['tipo']}")
    if ris["soluzioni"]:
        print(f"  {'':25} soluzioni: {ris['soluzioni']}")

print("  Esercizio 4 superato!\n")


print("Tutti gli esercizi T08 completati con successo!")
