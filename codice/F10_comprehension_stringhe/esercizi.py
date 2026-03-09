# F10 — Comprehension e stringhe
# Esercizi per la lezione frontale 10
# Frequenza parole, cifrario di Cesare, validazione email, trasposizione matrice

# =============================================================================
# Esercizio 1: Contatore di frequenza delle parole
# Dato un testo, contare quante volte appare ciascuna parola.
# =============================================================================
print("--- Esercizio 1: Frequenza parole ---")


def conta_parole(testo: str) -> dict[str, int]:
    """
    Conta la frequenza di ogni parola nel testo.
    Le parole sono normalizzate in minuscolo, la punteggiatura viene rimossa.
    """
    # Rimuoviamo la punteggiatura comune
    punteggiatura: str = ".,;:!?\"'()-"
    testo_pulito: str = testo.lower()
    for char in punteggiatura:
        testo_pulito = testo_pulito.replace(char, "")

    parole: list[str] = testo_pulito.split()
    frequenze: dict[str, int] = {}
    for parola in parole:
        frequenze[parola] = frequenze.get(parola, 0) + 1
    return frequenze


def parole_piu_frequenti(
    frequenze: dict[str, int], n: int = 5
) -> list[tuple[str, int]]:
    """Restituisce le n parole piu' frequenti, ordinate per frequenza decrescente."""
    ordinate: list[tuple[str, int]] = sorted(
        frequenze.items(), key=lambda coppia: coppia[1], reverse=True
    )
    return ordinate[:n]


# Testo di test
testo_test: str = (
    "Python e' un linguaggio di programmazione. "
    "Python e' versatile e Python e' potente. "
    "La programmazione in Python e' divertente!"
)

freq: dict[str, int] = conta_parole(testo_test)

assert freq["python"] == 4
assert freq["e"] == 5
assert freq["programmazione"] == 2
assert freq.get("Java", 0) == 0  # Parola assente

top_3: list[tuple[str, int]] = parole_piu_frequenti(freq, 3)
assert top_3[0][1] >= top_3[1][1] >= top_3[2][1]  # Ordine decrescente

print(f"  Testo: \"{testo_test[:50]}...\"")
print(f"  Parole uniche: {len(freq)}")
print(f"  Top 5 parole:")
for parola, conteggio in parole_piu_frequenti(freq, 5):
    barra: str = "#" * conteggio
    print(f"    {parola:<20} {conteggio:>3} {barra}")
print("  Esercizio 1 superato!\n")


# =============================================================================
# Esercizio 2: Cifrario di Cesare
# Cifrare e decifrare un messaggio spostando ogni lettera di N posizioni.
# =============================================================================
print("--- Esercizio 2: Cifrario di Cesare ---")


def cifra_cesare(testo: str, chiave: int) -> str:
    """
    Cifra un testo con il cifrario di Cesare.
    Sposta ogni lettera di 'chiave' posizioni nell'alfabeto.
    I caratteri non alfabetici restano invariati.
    """
    risultato: list[str] = []
    for char in testo:
        if char.isalpha():
            # Determiniamo la base ASCII (maiuscola o minuscola)
            base: int = ord("A") if char.isupper() else ord("a")
            # Spostamento con modulo 26 per restare nell'alfabeto
            nuovo_char: str = chr((ord(char) - base + chiave) % 26 + base)
            risultato.append(nuovo_char)
        else:
            risultato.append(char)
    return "".join(risultato)


def decifra_cesare(testo_cifrato: str, chiave: int) -> str:
    """Decifra un testo cifrato con Cesare (spostamento inverso)."""
    return cifra_cesare(testo_cifrato, -chiave)


# Test cifratura
assert cifra_cesare("ABC", 3) == "DEF"
assert cifra_cesare("XYZ", 3) == "ABC"  # Wrap-around
assert cifra_cesare("abc", 1) == "bcd"
assert cifra_cesare("Ciao Mondo!", 5) == "Hnft Rtsit!"

# Test decifratura
assert decifra_cesare("DEF", 3) == "ABC"
assert decifra_cesare("Hnft Rtsit!", 5) == "Ciao Mondo!"

# Test andata e ritorno
messaggio_originale: str = "La programmazione in Python e' fantastica!"
for chiave_test in range(0, 26):
    cifrato: str = cifra_cesare(messaggio_originale, chiave_test)
    decifrato: str = decifra_cesare(cifrato, chiave_test)
    assert decifrato == messaggio_originale

# Dimostrazione con chiave = 13 (ROT13)
originale: str = "Programmazione Python"
cifrato_13: str = cifra_cesare(originale, 13)
decifrato_13: str = decifra_cesare(cifrato_13, 13)
# ROT13 applicato due volte restituisce l'originale
assert cifra_cesare(cifrato_13, 13) == originale

print(f"  Originale:    '{originale}'")
print(f"  Cifrato (k=13): '{cifrato_13}'")
print(f"  Decifrato:    '{decifrato_13}'")

# Mostriamo tutte le 26 chiavi per "CIAO"
print(f"\n  Tutte le rotazioni di 'CIAO':")
for k in range(26):
    print(f"    k={k:>2}: {cifra_cesare('CIAO', k)}")
print("  Esercizio 2 superato!\n")


# =============================================================================
# Esercizio 3: Validatore semplice di email
# Verifica che una stringa abbia il formato base di un'email.
# =============================================================================
print("--- Esercizio 3: Validatore email (semplice) ---")


def valida_email(email: str) -> tuple[bool, str]:
    """
    Valida un indirizzo email con regole base:
    - Contiene esattamente un '@'
    - La parte locale (prima di @) non e' vuota
    - Il dominio contiene almeno un '.'
    - Il dominio non inizia e non finisce con '.'
    - Nessuno spazio presente
    Restituisce (valida, messaggio).
    """
    # Nessuno spazio
    if " " in email:
        return False, "Contiene spazi"

    # Esattamente un @
    if email.count("@") != 1:
        return False, f"Deve contenere esattamente un '@' (trovati: {email.count('@')})"

    locale: str
    dominio: str
    locale, dominio = email.split("@")

    # Parte locale non vuota
    if len(locale) == 0:
        return False, "Parte locale vuota"

    # Dominio non vuoto e contiene almeno un punto
    if len(dominio) == 0:
        return False, "Dominio vuoto"

    if "." not in dominio:
        return False, "Il dominio deve contenere almeno un '.'"

    if dominio.startswith(".") or dominio.endswith("."):
        return False, "Il dominio non puo' iniziare o finire con '.'"

    # Estensione (TLD) di almeno 2 caratteri
    tld: str = dominio.split(".")[-1]
    if len(tld) < 2:
        return False, f"Estensione troppo corta: '{tld}'"

    return True, "Email valida"


# Test email valide
assert valida_email("utente@example.com")[0] is True
assert valida_email("nome.cognome@unibo.it")[0] is True
assert valida_email("test123@mail.co.uk")[0] is True

# Test email non valide
assert valida_email("senza-chiocciola.com")[0] is False
assert valida_email("@dominio.com")[0] is False
assert valida_email("utente@")[0] is False
assert valida_email("utente@dominio")[0] is False
assert valida_email("utente@@dominio.com")[0] is False
assert valida_email("utente@.dominio.com")[0] is False
assert valida_email("utente@dominio.")[0] is False
assert valida_email("utente @dominio.com")[0] is False

# Dimostrazione
email_test: list[str] = [
    "mario.rossi@unibo.it",
    "studente@gmail.com",
    "senza-at.com",
    "@manca-locale.it",
    "doppia@@chiocciola.it",
    "utente@dominio",
    "nome cognome@mail.com",
    "test@.inizio-punto.com",
]

print(f"  {'Email':<35}{'Valida':<8}{'Messaggio'}")
print(f"  {'-' * 70}")
for email in email_test:
    valida, msg = valida_email(email)
    simbolo: str = "SI" if valida else "NO"
    print(f"  {email:<35}{simbolo:<8}{msg}")
print("  Esercizio 3 superato!\n")


# =============================================================================
# Esercizio 4: Trasposizione di matrice con comprehension
# Data una matrice MxN, restituire la trasposta NxM.
# =============================================================================
print("--- Esercizio 4: Trasposizione matrice ---")


def trasponi(matrice: list[list[int]]) -> list[list[int]]:
    """Traspone una matrice usando una list comprehension annidata."""
    if not matrice:
        return []
    n_colonne: int = len(matrice[0])
    # Per ogni colonna j, crea una riga con tutti gli elementi matrice[i][j]
    trasposta: list[list[int]] = [
        [matrice[i][j] for i in range(len(matrice))]
        for j in range(n_colonne)
    ]
    return trasposta


def trasponi_zip(matrice: list[list[int]]) -> list[list[int]]:
    """Traspone usando zip (modo idiomatico Python)."""
    return [list(riga) for riga in zip(*matrice)]


def stampa_matrice(matrice: list[list[int]], nome: str = "M") -> None:
    """Stampa una matrice in formato leggibile."""
    print(f"  {nome}:")
    for riga in matrice:
        print(f"    {riga}")


# Test matrice 2x3
m1: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
]
t1: list[list[int]] = trasponi(m1)
assert t1 == [
    [1, 4],
    [2, 5],
    [3, 6],
]

# Test matrice 3x3
m2: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
t2: list[list[int]] = trasponi(m2)
assert t2 == [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
]

# La trasposta della trasposta e' la matrice originale
assert trasponi(trasponi(m1)) == m1
assert trasponi(trasponi(m2)) == m2

# Verifica che le due implementazioni diano lo stesso risultato
assert trasponi(m1) == trasponi_zip(m1)
assert trasponi(m2) == trasponi_zip(m2)

# Test matrice vuota
assert trasponi([]) == []

# Test matrice 1xN
m3: list[list[int]] = [[1, 2, 3, 4, 5]]
t3: list[list[int]] = trasponi(m3)
assert t3 == [[1], [2], [3], [4], [5]]

stampa_matrice(m1, "M (2x3)")
stampa_matrice(t1, "M^T (3x2)")
print()
stampa_matrice(m2, "M (3x3)")
stampa_matrice(t2, "M^T (3x3)")
print("  Esercizio 4 superato!\n")


print("Tutti gli esercizi F10 completati con successo!")
