# T13 — Funzioni: fondamenti
# Esempi per la lezione frontale 13

# ============================================================
# 1. DEFINIZIONE DI FUNZIONI CON def, PARAMETRI, RETURN
# ============================================================
print("=== Definizione di funzioni ===")


def saluta(nome: str) -> str:
    """Restituisce un saluto personalizzato."""
    return f"Ciao, {nome}!"


risultato: str = saluta("Marco")
assert risultato == "Ciao, Marco!"
print(risultato)


def somma(a: float, b: float) -> float:
    """Restituisce la somma di due numeri."""
    return a + b


assert somma(3, 4) == 7
assert somma(1.5, 2.5) == 4.0
print(f"somma(3, 4) = {somma(3, 4)}")

# ============================================================
# 2. DOCSTRINGS E TYPE HINTS
# ============================================================
print("\n=== Docstrings e type hints ===")


def calcola_media(valori: list[float]) -> float:
    """
    Calcola la media aritmetica di una lista di valori.

    Args:
        valori: lista di numeri (non vuota)

    Returns:
        la media aritmetica dei valori

    Raises:
        ValueError: se la lista è vuota
    """
    if not valori:
        raise ValueError("La lista non può essere vuota")
    return sum(valori) / len(valori)


voti: list[float] = [28.0, 30.0, 25.0, 27.0, 30.0]
media: float = calcola_media(voti)
assert media == 28.0
print(f"Media dei voti: {media}")

# Accedere alla docstring
print(f"Docstring: {calcola_media.__doc__[:50]}...")

# ============================================================
# 3. ARGOMENTI PREDEFINITI (DEFAULT)
# ============================================================
print("\n=== Argomenti predefiniti ===")


def potenza(base: float, esponente: int = 2) -> float:
    """Calcola base elevato a esponente (default: quadrato)."""
    return base ** esponente


assert potenza(3) == 9       # usa il default
assert potenza(3, 3) == 27   # sovrascrive il default
assert potenza(2, 10) == 1024
print(f"potenza(3) = {potenza(3)}")
print(f"potenza(3, 3) = {potenza(3, 3)}")


def formatta_nome(
    nome: str,
    cognome: str,
    maiuscolo: bool = False,
    ordine_cognome_nome: bool = False
) -> str:
    """Formatta un nome completo con varie opzioni."""
    if ordine_cognome_nome:
        risultato: str = f"{cognome} {nome}"
    else:
        risultato = f"{nome} {cognome}"
    if maiuscolo:
        risultato = risultato.upper()
    return risultato


assert formatta_nome("Marco", "Rossi") == "Marco Rossi"
assert formatta_nome("Marco", "Rossi", maiuscolo=True) == "MARCO ROSSI"
assert formatta_nome("Marco", "Rossi", ordine_cognome_nome=True) == "Rossi Marco"
print(f"Formato base: {formatta_nome('Marco', 'Rossi')}")
print(f"Maiuscolo: {formatta_nome('Marco', 'Rossi', maiuscolo=True)}")

# ============================================================
# 4. ARGOMENTI KEYWORD
# ============================================================
print("\n=== Argomenti keyword ===")


def crea_studente(
    nome: str,
    cognome: str,
    matricola: int,
    corso: str = "Informatica",
    anno: int = 1
) -> dict[str, str | int]:
    """Crea un dizionario studente."""
    return {
        "nome": nome,
        "cognome": cognome,
        "matricola": matricola,
        "corso": corso,
        "anno": anno,
    }


# Tutti i modi di chiamare la funzione
s1: dict[str, str | int] = crea_studente("Marco", "Rossi", 12345)
s2: dict[str, str | int] = crea_studente(
    nome="Laura", cognome="Bianchi", matricola=12346, anno=2
)
s3: dict[str, str | int] = crea_studente(
    "Giulia", "Verdi", 12347, corso="Matematica"
)

assert s1["corso"] == "Informatica"
assert s2["anno"] == 2
assert s3["corso"] == "Matematica"
print(f"Studente 1: {s1}")
print(f"Studente 2: {s2}")

# ============================================================
# 5. RETURN MULTIPLI (tuple)
# ============================================================
print("\n=== Return multipli ===")


def statistiche_base(valori: list[float]) -> tuple[float, float, float]:
    """Calcola minimo, massimo e media di una lista di valori."""
    minimo: float = min(valori)
    massimo: float = max(valori)
    media: float = sum(valori) / len(valori)
    return minimo, massimo, media


dati: list[float] = [10.0, 20.0, 30.0, 40.0, 50.0]
minimo, massimo, media_val = statistiche_base(dati)
assert minimo == 10.0
assert massimo == 50.0
assert media_val == 30.0
print(f"Min: {minimo}, Max: {massimo}, Media: {media_val}")

# ============================================================
# 6. SCOPE: VARIABILI LOCALI E GLOBALI
# ============================================================
print("\n=== Scope: locale vs globale ===")

contatore_globale: int = 0


def incrementa_locale() -> int:
    """Dimostra che le variabili locali non modificano quelle globali."""
    contatore: int = 0  # variabile LOCALE
    contatore += 1
    return contatore


# La variabile globale non viene toccata
risultato_locale: int = incrementa_locale()
assert risultato_locale == 1
assert contatore_globale == 0  # la globale è rimasta invariata!
print(f"Risultato locale: {risultato_locale}")
print(f"Contatore globale (invariato): {contatore_globale}")

# NOTA: usare 'global' è generalmente sconsigliato — meglio passare
# e restituire valori esplicitamente.

# ============================================================
# 7. FUNZIONI PURE
# ============================================================
print("\n=== Funzioni pure ===")

# Funzione PURA: stesso input → stesso output, nessun effetto collaterale


def aggiungi_elemento_puro(lista: list[int], elemento: int) -> list[int]:
    """Restituisce una NUOVA lista con l'elemento aggiunto (pura)."""
    return lista + [elemento]


# Funzione IMPURA: modifica l'argomento (effetto collaterale)
def aggiungi_elemento_impuro(lista: list[int], elemento: int) -> None:
    """Modifica la lista in place (IMPURA — effetto collaterale)."""
    lista.append(elemento)


originale: list[int] = [1, 2, 3]

# La funzione pura non modifica l'originale
nuova: list[int] = aggiungi_elemento_puro(originale, 4)
assert originale == [1, 2, 3]  # non modificato!
assert nuova == [1, 2, 3, 4]
print(f"Pura — originale: {originale}, nuova: {nuova}")

# La funzione impura modifica l'originale
copia: list[int] = [1, 2, 3]
aggiungi_elemento_impuro(copia, 4)
assert copia == [1, 2, 3, 4]  # modificato!
print(f"Impura — lista dopo modifica: {copia}")

# ============================================================
# 8. ESEMPIO: FUNZIONI STATISTICHE
# ============================================================
print("\n=== Funzioni statistiche ===")


def media_aritmetica(valori: list[float]) -> float:
    """Calcola la media aritmetica."""
    return sum(valori) / len(valori)


def media_ponderata(valori: list[float], pesi: list[float]) -> float:
    """Calcola la media ponderata."""
    somma_pesata: float = sum(v * p for v, p in zip(valori, pesi))
    somma_pesi: float = sum(pesi)
    return somma_pesata / somma_pesi


def varianza_popolazione(valori: list[float]) -> float:
    """Calcola la varianza della popolazione."""
    m: float = media_aritmetica(valori)
    return sum((x - m) ** 2 for x in valori) / len(valori)


voti_esame: list[float] = [24.0, 26.0, 28.0, 30.0, 27.0]

m: float = media_aritmetica(voti_esame)
assert m == 27.0
print(f"Media aritmetica: {m}")

pesi: list[float] = [3.0, 6.0, 9.0, 12.0, 6.0]  # crediti
mp: float = media_ponderata(voti_esame, pesi)
print(f"Media ponderata: {mp:.2f}")

var: float = varianza_popolazione(voti_esame)
print(f"Varianza: {var:.2f}")

# ============================================================
# 9. ESEMPIO: CONVERTITORE DI TEMPERATURE
# ============================================================
print("\n=== Convertitore di temperature ===")


def celsius_a_fahrenheit(celsius: float) -> float:
    """Converte gradi Celsius in Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_a_celsius(fahrenheit: float) -> float:
    """Converte gradi Fahrenheit in Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_a_kelvin(celsius: float) -> float:
    """Converte gradi Celsius in Kelvin."""
    return celsius + 273.15


# Test
assert celsius_a_fahrenheit(0) == 32
assert celsius_a_fahrenheit(100) == 212
assert abs(fahrenheit_a_celsius(32) - 0) < 1e-9
assert abs(fahrenheit_a_celsius(212) - 100) < 1e-9
assert celsius_a_kelvin(0) == 273.15
assert abs(celsius_a_kelvin(-273.15)) < 1e-9

temperature_celsius: list[float] = [0.0, 20.0, 37.0, 100.0]
print(f"{'Celsius':>10} {'Fahrenheit':>12} {'Kelvin':>10}")
print("-" * 35)
for temp in temperature_celsius:
    f: float = celsius_a_fahrenheit(temp)
    k: float = celsius_a_kelvin(temp)
    print(f"{temp:>10.1f} {f:>12.1f} {k:>10.2f}")

print("\n=== Fine esempi T13 ===")
