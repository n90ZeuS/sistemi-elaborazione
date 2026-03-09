# L02 — Cicli, comprehension, stringhe
# Esercizi per il laboratorio 02
#
# Esercizi pratici su cicli for/while, list comprehension e manipolazione stringhe.
# Ogni esercizio include assert per verificare la correttezza.

# ============================================================================
# ESERCIZIO 1: Contare le vocali in un testo
# ============================================================================

def conta_vocali(testo: str) -> dict[str, int]:
    """
    Conta le occorrenze di ogni vocale (a, e, i, o, u) in un testo.
    Le vocali accentate vengono contate insieme alla vocale base.
    Il conteggio e' case-insensitive.

    Ritorna un dizionario con le chiavi 'a', 'e', 'i', 'o', 'u'.
    """
    # Mappa vocali accentate -> vocale base
    mappa_accenti: dict[str, str] = {
        'à': 'a', 'á': 'a', 'â': 'a', 'ä': 'a',
        'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
        'ì': 'i', 'í': 'i', 'î': 'i', 'ï': 'i',
        'ò': 'o', 'ó': 'o', 'ô': 'o', 'ö': 'o',
        'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u',
    }

    conteggio: dict[str, int] = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for carattere in testo.lower():
        # Controlla se e' una vocale base
        if carattere in conteggio:
            conteggio[carattere] += 1
        # Controlla se e' una vocale accentata
        elif carattere in mappa_accenti:
            conteggio[mappa_accenti[carattere]] += 1

    return conteggio


# --- Test conta vocali ---
risultato: dict[str, int] = conta_vocali("Ciao Mondo")
assert risultato['a'] == 1
assert risultato['o'] == 3
assert risultato['i'] == 1

# Test con vocali accentate
risultato_acc: dict[str, int] = conta_vocali("perché città università")
assert risultato_acc['e'] == 3  # e + é (perché=e+é, università=e)
assert risultato_acc['a'] == 2  # a + à (città=à, università=a)
assert risultato_acc['i'] == 3  # i (città=i, università=i+i)

# Test stringa vuota
assert conta_vocali("") == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
print("Esercizio 1 (Conta vocali): SUPERATO")


# ============================================================================
# ESERCIZIO 2: Verificatore di palindromi
# ============================================================================

def pulisci_testo(testo: str) -> str:
    """Rimuove spazi e punteggiatura, converte in minuscolo."""
    risultato: str = ""
    for c in testo.lower():
        if c.isalnum():
            risultato += c
    return risultato


def is_palindromo(testo: str) -> bool:
    """
    Verifica se un testo e' un palindromo.
    Ignora spazi, punteggiatura e distinzione maiuscole/minuscole.
    """
    pulito: str = pulisci_testo(testo)
    # Confronto con ciclo (senza usare slicing inverso per essere didattici)
    lunghezza: int = len(pulito)
    for i in range(lunghezza // 2):
        if pulito[i] != pulito[lunghezza - 1 - i]:
            return False
    return True


def trova_palindromi(parole: list[str]) -> list[str]:
    """Filtra una lista tenendo solo i palindromi, usando comprehension."""
    palindromi: list[str] = [p for p in parole if is_palindromo(p)]
    return palindromi


# --- Test palindromi ---
assert is_palindromo("anna") is True
assert is_palindromo("radar") is True
assert is_palindromo("python") is False
assert is_palindromo("I topi non avevano nipoti") is True  # famoso palindromo italiano
assert is_palindromo("") is True  # stringa vuota e' palindroma per convenzione

# Test con lista
lista_parole: list[str] = ["anna", "ciao", "otto", "radar", "python", "aba"]
palindromi_trovati: list[str] = trova_palindromi(lista_parole)
assert palindromi_trovati == ["anna", "otto", "radar", "aba"]
print("Esercizio 2 (Palindromi): SUPERATO")


# ============================================================================
# ESERCIZIO 3: Generazione del triangolo di Pascal
# ============================================================================

def triangolo_pascal(n_righe: int) -> list[list[int]]:
    """
    Genera le prime n_righe del triangolo di Pascal.

    Ogni riga inizia e finisce con 1.
    Ogni elemento interno e' la somma dei due elementi sopra di esso.

    Esempio per n_righe=5:
        [1]
        [1, 1]
        [1, 2, 1]
        [1, 3, 3, 1]
        [1, 4, 6, 4, 1]
    """
    if n_righe <= 0:
        return []

    triangolo: list[list[int]] = [[1]]

    for i in range(1, n_righe):
        riga_precedente: list[int] = triangolo[i - 1]
        # Costruisci la nuova riga: primo elemento e' 1
        nuova_riga: list[int] = [1]

        # Elementi intermedi: somma di coppie adiacenti dalla riga precedente
        for j in range(1, i):
            nuova_riga.append(riga_precedente[j - 1] + riga_precedente[j])

        # Ultimo elemento e' 1
        nuova_riga.append(1)
        triangolo.append(nuova_riga)

    return triangolo


def coefficiente_binomiale(n: int, k: int) -> int:
    """Calcola C(n, k) usando il triangolo di Pascal."""
    if k < 0 or k > n:
        return 0
    righe: list[list[int]] = triangolo_pascal(n + 1)
    return righe[n][k]


# --- Test triangolo di Pascal ---
pascal_5: list[list[int]] = triangolo_pascal(5)
assert pascal_5[0] == [1]
assert pascal_5[1] == [1, 1]
assert pascal_5[2] == [1, 2, 1]
assert pascal_5[3] == [1, 3, 3, 1]
assert pascal_5[4] == [1, 4, 6, 4, 1]
assert triangolo_pascal(0) == []
assert triangolo_pascal(1) == [[1]]

# Verifica che la somma della riga n e' 2^n
for n in range(8):
    righe: list[list[int]] = triangolo_pascal(n + 1)
    assert sum(righe[n]) == 2 ** n, f"La somma della riga {n} deve essere {2**n}"

# Test coefficiente binomiale
assert coefficiente_binomiale(5, 2) == 10
assert coefficiente_binomiale(10, 0) == 1
assert coefficiente_binomiale(10, 10) == 1
print("Esercizio 3 (Triangolo di Pascal): SUPERATO")


# ============================================================================
# ESERCIZIO 4: Inversore di parole
# ============================================================================

def inverti_parole(frase: str) -> str:
    """
    Inverte l'ordine delle parole in una frase, mantenendo
    le parole stesse invariate.
    Esempio: "Ciao mondo bello" -> "bello mondo Ciao"
    """
    parole: list[str] = frase.split()
    # Inversione manuale con ciclo (didattica)
    invertite: list[str] = []
    for i in range(len(parole) - 1, -1, -1):
        invertite.append(parole[i])
    return " ".join(invertite)


def inverti_ogni_parola(frase: str) -> str:
    """
    Inverte ogni singola parola nella frase, mantenendo l'ordine.
    Esempio: "Ciao mondo" -> "oaiC odnom"
    """
    # Uso di comprehension per invertire ogni parola
    parole_invertite: list[str] = [parola[::-1] for parola in frase.split()]
    return " ".join(parole_invertite)


# --- Test inversore di parole ---
assert inverti_parole("Ciao mondo bello") == "bello mondo Ciao"
assert inverti_parole("Python") == "Python"
assert inverti_parole("") == ""
assert inverti_parole("uno due tre quattro") == "quattro tre due uno"

assert inverti_ogni_parola("Ciao mondo") == "oaiC odnom"
assert inverti_ogni_parola("abc def") == "cba fed"
print("Esercizio 4 (Inversore parole): SUPERATO")


# ============================================================================
# ESERCIZIO 5: Numeri primi con il Crivello di Eratostene
# ============================================================================

def crivello_eratostene(n: int) -> list[int]:
    """
    Trova tutti i numeri primi fino a n usando il Crivello di Eratostene.

    Algoritmo:
    1. Crea una lista di booleani [True] * (n+1)
    2. Parti da 2: per ogni numero primo trovato, segna tutti i suoi
       multipli come non primi
    3. I numeri che restano True sono primi
    """
    if n < 2:
        return []

    # Inizializza: tutti potenzialmente primi
    is_primo: list[bool] = [True] * (n + 1)
    is_primo[0] = False
    is_primo[1] = False

    # Crivello: per ogni numero da 2 a sqrt(n)
    p: int = 2
    while p * p <= n:
        if is_primo[p]:
            # Segna tutti i multipli di p come non primi
            # Partiamo da p*p perche' i multipli minori sono gia' stati segnati
            multiplo: int = p * p
            while multiplo <= n:
                is_primo[multiplo] = False
                multiplo += p
        p += 1

    # Raccogli i primi con comprehension
    primi: list[int] = [i for i in range(2, n + 1) if is_primo[i]]
    return primi


def conta_primi_fino_a(n: int) -> int:
    """Conta quanti numeri primi ci sono fino a n."""
    return len(crivello_eratostene(n))


# --- Test crivello ---
assert crivello_eratostene(1) == []
assert crivello_eratostene(2) == [2]
assert crivello_eratostene(10) == [2, 3, 5, 7]
assert crivello_eratostene(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Verifica numeri noti: ci sono 25 primi fino a 100
assert conta_primi_fino_a(100) == 25
# Ci sono 168 primi fino a 1000
assert conta_primi_fino_a(1000) == 168
print("Esercizio 5 (Crivello di Eratostene): SUPERATO")


# ============================================================================
# ESERCIZIO 6: Statistiche di testo
# ============================================================================

def statistiche_testo(testo: str) -> dict[str, object]:
    """
    Analizza un testo e restituisce statistiche:
    - num_caratteri: numero totale di caratteri (spazi inclusi)
    - num_parole: numero di parole
    - num_frasi: numero di frasi (delimitati da . ! ?)
    - lunghezza_media_parola: lunghezza media delle parole (arrotondata a 1 decimale)
    - parola_piu_lunga: la parola piu' lunga nel testo
    - parola_piu_frequente: la parola che appare piu' volte (minuscolo)
    """
    if not testo.strip():
        return {
            "num_caratteri": 0,
            "num_parole": 0,
            "num_frasi": 0,
            "lunghezza_media_parola": 0.0,
            "parola_piu_lunga": "",
            "parola_piu_frequente": "",
        }

    num_caratteri: int = len(testo)

    # Conta frasi: ogni . ! ? termina una frase
    num_frasi: int = 0
    for c in testo:
        if c in '.!?':
            num_frasi += 1
    # Se il testo non termina con punteggiatura, conta come una frase
    if num_frasi == 0:
        num_frasi = 1

    # Estrai parole rimuovendo punteggiatura
    parole_raw: list[str] = testo.split()
    parole_pulite: list[str] = []
    for parola in parole_raw:
        # Rimuovi punteggiatura dai bordi
        pulita: str = ""
        for c in parola:
            if c.isalpha() or c == "'":
                pulita += c
        if pulita:
            parole_pulite.append(pulita)

    num_parole: int = len(parole_pulite)

    # Lunghezza media
    somma_lunghezze: int = sum(len(p) for p in parole_pulite)
    lunghezza_media: float = round(somma_lunghezze / num_parole, 1) if num_parole > 0 else 0.0

    # Parola piu' lunga
    parola_piu_lunga: str = max(parole_pulite, key=len) if parole_pulite else ""

    # Parola piu' frequente (case-insensitive)
    frequenze: dict[str, int] = {}
    for p in parole_pulite:
        chiave: str = p.lower()
        frequenze[chiave] = frequenze.get(chiave, 0) + 1

    parola_piu_frequente: str = ""
    max_freq: int = 0
    for parola, freq in frequenze.items():
        if freq > max_freq:
            max_freq = freq
            parola_piu_frequente = parola

    return {
        "num_caratteri": num_caratteri,
        "num_parole": num_parole,
        "num_frasi": num_frasi,
        "lunghezza_media_parola": lunghezza_media,
        "parola_piu_lunga": parola_piu_lunga,
        "parola_piu_frequente": parola_piu_frequente,
    }


# --- Test statistiche testo ---
testo_test: str = "Il gatto e il cane. Il gatto dorme. Il cane corre!"
stats: dict[str, object] = statistiche_testo(testo_test)

assert stats["num_parole"] == 11
assert stats["num_frasi"] == 3
assert stats["parola_piu_frequente"] == "il"  # appare 3 volte (case-insensitive)

# Testo vuoto
stats_vuoto: dict[str, object] = statistiche_testo("")
assert stats_vuoto["num_parole"] == 0
assert stats_vuoto["num_frasi"] == 0

# Testo senza punteggiatura
stats_no_punt: dict[str, object] = statistiche_testo("ciao mondo bello")
assert stats_no_punt["num_frasi"] == 1
assert stats_no_punt["num_parole"] == 3
assert stats_no_punt["parola_piu_lunga"] == "mondo"
print("Esercizio 6 (Statistiche testo): SUPERATO")


# ============================================================================
print("\n" + "=" * 60)
print("TUTTI GLI ESERCIZI DEL LABORATORIO 02 SUPERATI!")
print("=" * 60)
