# L03 — Strutture dati
# Esercizi per il laboratorio 03
#
# Esercizi pratici su liste, tuple, dizionari e set.
# Ogni esercizio include assert per verificare la correttezza.

from typing import Any

# ============================================================================
# ESERCIZIO 1: Stack implementato con una lista
# ============================================================================
# Uno stack (pila) e' una struttura dati LIFO (Last In, First Out).
# Operazioni: push (inserisci in cima), pop (rimuovi dalla cima),
# peek (guarda la cima senza rimuovere), is_empty, size.

class Stack:
    """
    Implementazione di uno stack usando una lista Python.
    Gli elementi vengono aggiunti e rimossi dalla fine della lista
    (operazione O(1) in Python).
    """

    def __init__(self) -> None:
        """Inizializza uno stack vuoto."""
        self._dati: list[Any] = []

    def push(self, elemento: Any) -> None:
        """Inserisce un elemento in cima allo stack."""
        self._dati.append(elemento)

    def pop(self) -> Any:
        """Rimuove e restituisce l'elemento in cima allo stack."""
        if self.is_empty():
            raise IndexError("Pop da uno stack vuoto")
        return self._dati.pop()

    def peek(self) -> Any:
        """Restituisce l'elemento in cima senza rimuoverlo."""
        if self.is_empty():
            raise IndexError("Peek su uno stack vuoto")
        return self._dati[-1]

    def is_empty(self) -> bool:
        """Verifica se lo stack e' vuoto."""
        return len(self._dati) == 0

    def size(self) -> int:
        """Restituisce il numero di elementi nello stack."""
        return len(self._dati)

    def to_list(self) -> list[Any]:
        """Restituisce una copia della lista interna (dal fondo alla cima)."""
        return self._dati.copy()


def parentesi_bilanciate(espressione: str) -> bool:
    """
    Usa uno stack per verificare che le parentesi siano bilanciate.
    Supporta: (), [], {}
    """
    stack: Stack = Stack()
    aperte: str = "([{"
    chiuse: str = ")]}"
    coppie: dict[str, str] = {')': '(', ']': '[', '}': '{'}

    for carattere in espressione:
        if carattere in aperte:
            stack.push(carattere)
        elif carattere in chiuse:
            if stack.is_empty():
                return False
            if stack.pop() != coppie[carattere]:
                return False

    return stack.is_empty()


# --- Test stack ---
s: Stack = Stack()
assert s.is_empty() is True
assert s.size() == 0

s.push(10)
s.push(20)
s.push(30)
assert s.size() == 3
assert s.peek() == 30
assert s.pop() == 30
assert s.pop() == 20
assert s.size() == 1

# Test errore su stack vuoto
errore_pop: bool = False
try:
    vuoto: Stack = Stack()
    vuoto.pop()
except IndexError:
    errore_pop = True
assert errore_pop

# Test parentesi bilanciate
assert parentesi_bilanciate("()") is True
assert parentesi_bilanciate("([{}])") is True
assert parentesi_bilanciate("(]") is False
assert parentesi_bilanciate("((())") is False
assert parentesi_bilanciate("{[a + b] * (c - d)}") is True
assert parentesi_bilanciate("") is True
print("Esercizio 1 (Stack): SUPERATO")


# ============================================================================
# ESERCIZIO 2: Contatore di frequenze per testo
# ============================================================================

def conta_frequenze_parole(testo: str) -> dict[str, int]:
    """
    Conta la frequenza di ogni parola in un testo.
    Le parole sono convertite in minuscolo e la punteggiatura viene rimossa.
    """
    # Rimuovi punteggiatura e converti in minuscolo
    testo_pulito: str = ""
    for c in testo.lower():
        if c.isalnum() or c.isspace():
            testo_pulito += c

    frequenze: dict[str, int] = {}
    for parola in testo_pulito.split():
        frequenze[parola] = frequenze.get(parola, 0) + 1

    return frequenze


def top_n_parole(frequenze: dict[str, int], n: int) -> list[tuple[str, int]]:
    """
    Restituisce le n parole piu' frequenti come lista di tuple (parola, frequenza),
    ordinate per frequenza decrescente.
    """
    # Ordinamento per frequenza decrescente
    ordinato: list[tuple[str, int]] = sorted(
        frequenze.items(),
        key=lambda coppia: coppia[1],
        reverse=True
    )
    return ordinato[:n]


def conta_frequenze_caratteri(testo: str) -> dict[str, int]:
    """Conta la frequenza di ogni carattere (esclusi gli spazi)."""
    freq: dict[str, int] = {}
    for c in testo.lower():
        if c != ' ':
            freq[c] = freq.get(c, 0) + 1
    return freq


# --- Test frequenze ---
testo_freq: str = "il gatto e il cane, il gatto dorme e il cane corre"
freq: dict[str, int] = conta_frequenze_parole(testo_freq)
assert freq["il"] == 4
assert freq["gatto"] == 2
assert freq["cane"] == 2
assert freq["e"] == 2
assert freq["dorme"] == 1

top3: list[tuple[str, int]] = top_n_parole(freq, 3)
assert top3[0] == ("il", 4)
assert len(top3) == 3

# Test stringa vuota
assert conta_frequenze_parole("") == {}
print("Esercizio 2 (Frequenze parole): SUPERATO")


# ============================================================================
# ESERCIZIO 3: Registro voti studenti (dizionario di liste)
# ============================================================================

class RegistroVoti:
    """
    Gestisce un registro di voti per studenti.
    Struttura interna: dict[str, list[float]] dove la chiave e' il nome
    dello studente e il valore e' la lista dei suoi voti.
    """

    def __init__(self) -> None:
        self._registro: dict[str, list[float]] = {}

    def aggiungi_studente(self, nome: str) -> None:
        """Aggiunge uno studente al registro (senza voti)."""
        if nome not in self._registro:
            self._registro[nome] = []

    def aggiungi_voto(self, nome: str, voto: float) -> None:
        """Aggiunge un voto allo studente. Crea lo studente se non esiste."""
        if voto < 0 or voto > 30:
            raise ValueError(f"Voto {voto} non valido (deve essere tra 0 e 30)")
        if nome not in self._registro:
            self._registro[nome] = []
        self._registro[nome].append(voto)

    def media_studente(self, nome: str) -> float:
        """Calcola la media dei voti di uno studente."""
        if nome not in self._registro or len(self._registro[nome]) == 0:
            raise ValueError(f"Nessun voto per lo studente '{nome}'")
        voti: list[float] = self._registro[nome]
        return round(sum(voti) / len(voti), 2)

    def media_classe(self) -> float:
        """Calcola la media complessiva di tutti gli studenti."""
        tutti_i_voti: list[float] = []
        for voti in self._registro.values():
            tutti_i_voti.extend(voti)
        if not tutti_i_voti:
            raise ValueError("Nessun voto nel registro")
        return round(sum(tutti_i_voti) / len(tutti_i_voti), 2)

    def migliore_studente(self) -> str:
        """Restituisce il nome dello studente con la media piu' alta."""
        miglior_nome: str = ""
        miglior_media: float = -1.0
        for nome, voti in self._registro.items():
            if voti:
                media: float = sum(voti) / len(voti)
                if media > miglior_media:
                    miglior_media = media
                    miglior_nome = nome
        return miglior_nome

    def studenti_sufficienti(self, soglia: float = 18.0) -> list[str]:
        """Restituisce la lista degli studenti con media >= soglia."""
        sufficienti: list[str] = []
        for nome, voti in self._registro.items():
            if voti and (sum(voti) / len(voti)) >= soglia:
                sufficienti.append(nome)
        return sorted(sufficienti)

    def num_studenti(self) -> int:
        return len(self._registro)


# --- Test registro voti ---
reg: RegistroVoti = RegistroVoti()
reg.aggiungi_voto("Alice", 28)
reg.aggiungi_voto("Alice", 30)
reg.aggiungi_voto("Alice", 26)
reg.aggiungi_voto("Bob", 22)
reg.aggiungi_voto("Bob", 18)
reg.aggiungi_voto("Carla", 15)
reg.aggiungi_voto("Carla", 14)

assert reg.media_studente("Alice") == 28.0
assert reg.media_studente("Bob") == 20.0
assert reg.migliore_studente() == "Alice"
assert reg.studenti_sufficienti() == ["Alice", "Bob"]
assert reg.num_studenti() == 3

# Test voto non valido
errore_voto: bool = False
try:
    reg.aggiungi_voto("Test", 35)
except ValueError:
    errore_voto = True
assert errore_voto
print("Esercizio 3 (Registro voti): SUPERATO")


# ============================================================================
# ESERCIZIO 4: Trova duplicati con i set
# ============================================================================

def trova_duplicati(lista: list[Any]) -> list[Any]:
    """
    Trova tutti gli elementi duplicati in una lista usando i set.
    Restituisce i duplicati nell'ordine in cui appaiono la prima volta come duplicato.
    """
    visti: set[Any] = set()
    duplicati_set: set[Any] = set()
    duplicati_ordinati: list[Any] = []

    for elemento in lista:
        if elemento in visti:
            if elemento not in duplicati_set:
                duplicati_ordinati.append(elemento)
                duplicati_set.add(elemento)
        else:
            visti.add(elemento)

    return duplicati_ordinati


def elementi_comuni(lista_a: list[Any], lista_b: list[Any]) -> list[Any]:
    """Trova gli elementi comuni a due liste usando i set."""
    set_a: set[Any] = set(lista_a)
    set_b: set[Any] = set(lista_b)
    comuni: set[Any] = set_a & set_b  # intersezione
    return sorted(comuni)


def elementi_unici_combinati(lista_a: list[Any], lista_b: list[Any]) -> list[Any]:
    """Trova tutti gli elementi unici presenti in almeno una delle due liste."""
    return sorted(set(lista_a) | set(lista_b))  # unione


def differenza_simmetrica(lista_a: list[Any], lista_b: list[Any]) -> list[Any]:
    """Trova elementi presenti in una sola delle due liste (non in entrambe)."""
    return sorted(set(lista_a) ^ set(lista_b))


# --- Test duplicati e operazioni su set ---
assert trova_duplicati([1, 2, 3, 2, 4, 3, 5]) == [2, 3]
assert trova_duplicati([1, 2, 3]) == []
assert trova_duplicati([]) == []
assert trova_duplicati([1, 1, 1, 1]) == [1]

assert elementi_comuni([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
assert elementi_comuni([1, 2], [3, 4]) == []

assert elementi_unici_combinati([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]
assert differenza_simmetrica([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]
print("Esercizio 4 (Duplicati con set): SUPERATO")


# ============================================================================
# ESERCIZIO 5: Operazioni su matrici (liste di liste)
# ============================================================================

# Tipo alias per leggibilita'
Matrice = list[list[float]]


def crea_matrice_zero(righe: int, colonne: int) -> Matrice:
    """Crea una matrice di zeri con le dimensioni specificate."""
    return [[0.0 for _ in range(colonne)] for _ in range(righe)]


def dimensioni(matrice: Matrice) -> tuple[int, int]:
    """Restituisce (numero_righe, numero_colonne) della matrice."""
    if not matrice:
        return (0, 0)
    return (len(matrice), len(matrice[0]))


def somma_matrici(a: Matrice, b: Matrice) -> Matrice:
    """
    Somma di due matrici: C[i][j] = A[i][j] + B[i][j].
    Le matrici devono avere le stesse dimensioni.
    """
    dim_a: tuple[int, int] = dimensioni(a)
    dim_b: tuple[int, int] = dimensioni(b)
    if dim_a != dim_b:
        raise ValueError(f"Dimensioni incompatibili: {dim_a} vs {dim_b}")

    righe: int = dim_a[0]
    colonne: int = dim_a[1]

    risultato: Matrice = [
        [a[i][j] + b[i][j] for j in range(colonne)]
        for i in range(righe)
    ]
    return risultato


def moltiplica_matrici(a: Matrice, b: Matrice) -> Matrice:
    """
    Prodotto matriciale: C[i][j] = somma(A[i][k] * B[k][j]) per ogni k.
    Richiede: colonne di A == righe di B.
    """
    righe_a, colonne_a = dimensioni(a)
    righe_b, colonne_b = dimensioni(b)

    if colonne_a != righe_b:
        raise ValueError(
            f"Impossibile moltiplicare: A ha {colonne_a} colonne, B ha {righe_b} righe"
        )

    # Inizializza matrice risultato
    risultato: Matrice = crea_matrice_zero(righe_a, colonne_b)

    for i in range(righe_a):
        for j in range(colonne_b):
            somma: float = 0.0
            for k in range(colonne_a):
                somma += a[i][k] * b[k][j]
            risultato[i][j] = somma

    return risultato


def trasposta(matrice: Matrice) -> Matrice:
    """Calcola la trasposta della matrice: T[j][i] = M[i][j]."""
    righe, colonne = dimensioni(matrice)
    # Uso comprehension nidificata
    return [[matrice[i][j] for i in range(righe)] for j in range(colonne)]


def matrice_identita(n: int) -> Matrice:
    """Crea una matrice identita' n x n."""
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


# --- Test operazioni matrici ---
m1: Matrice = [[1, 2], [3, 4]]
m2: Matrice = [[5, 6], [7, 8]]

# Somma
somma: Matrice = somma_matrici(m1, m2)
assert somma == [[6, 8], [10, 12]]

# Prodotto: [[1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]] = [[19, 22], [43, 50]]
prodotto: Matrice = moltiplica_matrici(m1, m2)
assert prodotto == [[19, 22], [43, 50]]

# Trasposta
t: Matrice = trasposta(m1)
assert t == [[1, 3], [2, 4]]

# Moltiplicazione per identita' non cambia la matrice
identita: Matrice = matrice_identita(2)
assert moltiplica_matrici(m1, identita) == [[1.0, 2.0], [3.0, 4.0]]

# Test dimensioni incompatibili
errore_dim: bool = False
try:
    somma_matrici([[1, 2]], [[1, 2], [3, 4]])
except ValueError:
    errore_dim = True
assert errore_dim

# Matrici non quadrate: (2x3) * (3x2) = (2x2)
a: Matrice = [[1, 2, 3], [4, 5, 6]]
b: Matrice = [[7, 8], [9, 10], [11, 12]]
ris: Matrice = moltiplica_matrici(a, b)
assert ris == [[58, 64], [139, 154]]
print("Esercizio 5 (Operazioni matrici): SUPERATO")


# ============================================================================
print("\n" + "=" * 60)
print("TUTTI GLI ESERCIZI DEL LABORATORIO 03 SUPERATI!")
print("=" * 60)
