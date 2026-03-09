# L06 — Classi e oggetti
# Esercizi per il laboratorio 06
#
# Esercizi pratici su programmazione orientata agli oggetti:
# classi, metodi, ereditarieta', incapsulamento.
# Ogni esercizio include assert per verificare la correttezza.

from __future__ import annotations
import math
from typing import Optional, Any

# ============================================================================
# ESERCIZIO 1: Punto2D con operazioni geometriche
# ============================================================================

class Punto2D:
    """
    Rappresenta un punto nel piano cartesiano 2D.
    Supporta operazioni geometriche: distanza, traslazione, somma, ecc.
    """

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._x: float = x
        self._y: float = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def distanza_da(self, altro: Punto2D) -> float:
        """Calcola la distanza euclidea tra due punti."""
        dx: float = self._x - altro._x
        dy: float = self._y - altro._y
        return math.sqrt(dx * dx + dy * dy)

    def distanza_origine(self) -> float:
        """Calcola la distanza dall'origine (0, 0)."""
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def trasla(self, dx: float, dy: float) -> Punto2D:
        """Restituisce un nuovo punto traslato di (dx, dy)."""
        return Punto2D(self._x + dx, self._y + dy)

    def punto_medio(self, altro: Punto2D) -> Punto2D:
        """Calcola il punto medio tra self e altro."""
        mx: float = (self._x + altro._x) / 2.0
        my: float = (self._y + altro._y) / 2.0
        return Punto2D(mx, my)

    def __add__(self, altro: Punto2D) -> Punto2D:
        """Somma vettoriale: P1 + P2."""
        return Punto2D(self._x + altro._x, self._y + altro._y)

    def __sub__(self, altro: Punto2D) -> Punto2D:
        """Differenza vettoriale: P1 - P2."""
        return Punto2D(self._x - altro._x, self._y - altro._y)

    def __mul__(self, scalare: float) -> Punto2D:
        """Moltiplicazione per scalare."""
        return Punto2D(self._x * scalare, self._y * scalare)

    def __eq__(self, altro: object) -> bool:
        if not isinstance(altro, Punto2D):
            return NotImplemented
        return abs(self._x - altro._x) < 1e-9 and abs(self._y - altro._y) < 1e-9

    def __repr__(self) -> str:
        return f"Punto2D({self._x}, {self._y})"


# --- Test Punto2D ---
p1: Punto2D = Punto2D(0, 0)
p2: Punto2D = Punto2D(3, 4)
p3: Punto2D = Punto2D(1, 1)

# Distanza
assert abs(p1.distanza_da(p2) - 5.0) < 1e-9, "Distanza (0,0)-(3,4) deve essere 5"
assert abs(p2.distanza_origine() - 5.0) < 1e-9

# Traslazione
p_traslato: Punto2D = p3.trasla(2, 3)
assert p_traslato == Punto2D(3, 4)

# Punto medio
pm: Punto2D = p1.punto_medio(p2)
assert pm == Punto2D(1.5, 2.0)

# Operazioni vettoriali
somma: Punto2D = p2 + p3
assert somma == Punto2D(4, 5)

diff: Punto2D = p2 - p3
assert diff == Punto2D(2, 3)

scalato: Punto2D = p3 * 3
assert scalato == Punto2D(3, 3)

# Proprieta' della distanza: d(A,B) = d(B,A)
assert abs(p1.distanza_da(p2) - p2.distanza_da(p1)) < 1e-9
print("Esercizio 1 (Punto2D): SUPERATO")


# ============================================================================
# ESERCIZIO 2: Classe Polinomio
# ============================================================================

class Polinomio:
    """
    Rappresenta un polinomio a coefficienti reali.
    I coefficienti sono memorizzati come lista dove l'indice corrisponde
    al grado: coefficienti[i] e' il coefficiente di x^i.
    Esempio: [3, 2, 1] rappresenta 3 + 2x + x^2
    """

    def __init__(self, coefficienti: list[float]) -> None:
        # Rimuovi zeri finali (tranne se il polinomio e' zero)
        while len(coefficienti) > 1 and coefficienti[-1] == 0:
            coefficienti.pop()
        self._coeff: list[float] = coefficienti.copy()

    @property
    def grado(self) -> int:
        """Restituisce il grado del polinomio."""
        if len(self._coeff) == 1 and self._coeff[0] == 0:
            return 0
        return len(self._coeff) - 1

    @property
    def coefficienti(self) -> list[float]:
        return self._coeff.copy()

    def valuta(self, x: float) -> float:
        """
        Calcola il valore del polinomio nel punto x.
        Usa il metodo di Horner per efficienza: O(n).
        """
        risultato: float = 0.0
        # Metodo di Horner: p(x) = ((...((a_n * x + a_{n-1}) * x + a_{n-2}) * x + ...) * x + a_0
        for i in range(len(self._coeff) - 1, -1, -1):
            risultato = risultato * x + self._coeff[i]
        return risultato

    def derivata(self) -> Polinomio:
        """Calcola la derivata del polinomio."""
        if self.grado == 0:
            return Polinomio([0])
        nuovi_coeff: list[float] = [
            self._coeff[i] * i for i in range(1, len(self._coeff))
        ]
        return Polinomio(nuovi_coeff)

    def __add__(self, altro: Polinomio) -> Polinomio:
        """Somma di due polinomi."""
        lunghezza: int = max(len(self._coeff), len(altro._coeff))
        risultato: list[float] = []
        for i in range(lunghezza):
            a: float = self._coeff[i] if i < len(self._coeff) else 0.0
            b: float = altro._coeff[i] if i < len(altro._coeff) else 0.0
            risultato.append(a + b)
        return Polinomio(risultato)

    def __mul__(self, altro: Polinomio) -> Polinomio:
        """Prodotto di due polinomi."""
        n: int = len(self._coeff) + len(altro._coeff) - 1
        risultato: list[float] = [0.0] * n
        for i in range(len(self._coeff)):
            for j in range(len(altro._coeff)):
                risultato[i + j] += self._coeff[i] * altro._coeff[j]
        return Polinomio(risultato)

    def __eq__(self, altro: object) -> bool:
        if not isinstance(altro, Polinomio):
            return NotImplemented
        return self._coeff == altro._coeff

    def __repr__(self) -> str:
        termini: list[str] = []
        for i, c in enumerate(self._coeff):
            if c == 0:
                continue
            if i == 0:
                termini.append(f"{c}")
            elif i == 1:
                termini.append(f"{c}x")
            else:
                termini.append(f"{c}x^{i}")
        return " + ".join(termini) if termini else "0"


# --- Test Polinomio ---
# p(x) = 3 + 2x + x^2
p: Polinomio = Polinomio([3, 2, 1])
assert p.grado == 2
assert p.valuta(0) == 3
assert p.valuta(1) == 6      # 3 + 2 + 1 = 6
assert p.valuta(2) == 11     # 3 + 4 + 4 = 11
assert p.valuta(-1) == 2     # 3 - 2 + 1 = 2

# Derivata: p'(x) = 2 + 2x
dp: Polinomio = p.derivata()
assert dp == Polinomio([2, 2])
assert dp.valuta(0) == 2
assert dp.valuta(1) == 4

# Somma: (3 + 2x + x^2) + (1 + x) = 4 + 3x + x^2
q: Polinomio = Polinomio([1, 1])
somma_p: Polinomio = p + q
assert somma_p == Polinomio([4, 3, 1])

# Prodotto: (1 + x) * (1 + x) = 1 + 2x + x^2
r: Polinomio = Polinomio([1, 1])
prodotto_p: Polinomio = r * r
assert prodotto_p == Polinomio([1, 2, 1])

# Polinomio zero
zero: Polinomio = Polinomio([0])
assert zero.grado == 0
assert zero.valuta(42) == 0
print("Esercizio 2 (Polinomio): SUPERATO")


# ============================================================================
# ESERCIZIO 3: Lista concatenata (Linked List)
# ============================================================================

class Nodo:
    """Un nodo della lista concatenata."""

    def __init__(self, dato: Any, successivo: Optional[Nodo] = None) -> None:
        self.dato: Any = dato
        self.successivo: Optional[Nodo] = successivo

    def __repr__(self) -> str:
        return f"Nodo({self.dato})"


class ListaConcatenata:
    """
    Implementazione di una lista concatenata semplice (singly linked list).
    Ogni nodo contiene un dato e un puntatore al nodo successivo.
    """

    def __init__(self) -> None:
        self._testa: Optional[Nodo] = None
        self._lunghezza: int = 0

    def __len__(self) -> int:
        return self._lunghezza

    def is_vuota(self) -> bool:
        return self._testa is None

    def aggiungi_in_testa(self, dato: Any) -> None:
        """Inserisce un elemento in testa alla lista - O(1)."""
        nuovo_nodo: Nodo = Nodo(dato, self._testa)
        self._testa = nuovo_nodo
        self._lunghezza += 1

    def aggiungi_in_coda(self, dato: Any) -> None:
        """Inserisce un elemento in coda alla lista - O(n)."""
        nuovo_nodo: Nodo = Nodo(dato)
        if self._testa is None:
            self._testa = nuovo_nodo
        else:
            corrente: Nodo = self._testa
            while corrente.successivo is not None:
                corrente = corrente.successivo
            corrente.successivo = nuovo_nodo
        self._lunghezza += 1

    def rimuovi_testa(self) -> Any:
        """Rimuove e restituisce l'elemento in testa - O(1)."""
        if self._testa is None:
            raise IndexError("Lista vuota")
        dato: Any = self._testa.dato
        self._testa = self._testa.successivo
        self._lunghezza -= 1
        return dato

    def cerca(self, dato: Any) -> bool:
        """Verifica se un dato e' presente nella lista - O(n)."""
        corrente: Optional[Nodo] = self._testa
        while corrente is not None:
            if corrente.dato == dato:
                return True
            corrente = corrente.successivo
        return False

    def ottieni(self, indice: int) -> Any:
        """Restituisce l'elemento all'indice specificato - O(n)."""
        if indice < 0 or indice >= self._lunghezza:
            raise IndexError(f"Indice {indice} fuori range [0, {self._lunghezza - 1}]")
        corrente: Optional[Nodo] = self._testa
        for _ in range(indice):
            assert corrente is not None
            corrente = corrente.successivo
        assert corrente is not None
        return corrente.dato

    def to_list(self) -> list[Any]:
        """Converte la lista concatenata in una lista Python."""
        risultato: list[Any] = []
        corrente: Optional[Nodo] = self._testa
        while corrente is not None:
            risultato.append(corrente.dato)
            corrente = corrente.successivo
        return risultato

    def inverti(self) -> None:
        """Inverte la lista in-place - O(n)."""
        precedente: Optional[Nodo] = None
        corrente: Optional[Nodo] = self._testa

        while corrente is not None:
            successivo: Optional[Nodo] = corrente.successivo
            corrente.successivo = precedente
            precedente = corrente
            corrente = successivo

        self._testa = precedente

    def __repr__(self) -> str:
        elementi: list[str] = [str(e) for e in self.to_list()]
        return " -> ".join(elementi) + " -> None"


# --- Test lista concatenata ---
ll: ListaConcatenata = ListaConcatenata()
assert ll.is_vuota() is True
assert len(ll) == 0

# Aggiungi elementi
ll.aggiungi_in_coda(1)
ll.aggiungi_in_coda(2)
ll.aggiungi_in_coda(3)
ll.aggiungi_in_testa(0)

assert len(ll) == 4
assert ll.to_list() == [0, 1, 2, 3]
assert ll.is_vuota() is False

# Cerca
assert ll.cerca(2) is True
assert ll.cerca(99) is False

# Ottieni per indice
assert ll.ottieni(0) == 0
assert ll.ottieni(3) == 3

# Rimuovi testa
rimosso: Any = ll.rimuovi_testa()
assert rimosso == 0
assert ll.to_list() == [1, 2, 3]

# Inverti
ll.inverti()
assert ll.to_list() == [3, 2, 1]

# Test errore su indice fuori range
errore_indice: bool = False
try:
    ll.ottieni(10)
except IndexError:
    errore_indice = True
assert errore_indice
print("Esercizio 3 (Lista concatenata): SUPERATO")


# ============================================================================
# ESERCIZIO 4: Sistema Studente/Corso con iscrizioni
# ============================================================================

class Studente:
    """Rappresenta uno studente con matricola, nome e voti."""

    def __init__(self, matricola: str, nome: str, cognome: str) -> None:
        self._matricola: str = matricola
        self._nome: str = nome
        self._cognome: str = cognome
        self._voti: dict[str, float] = {}  # materia -> voto

    @property
    def matricola(self) -> str:
        return self._matricola

    @property
    def nome_completo(self) -> str:
        return f"{self._nome} {self._cognome}"

    def registra_voto(self, materia: str, voto: float) -> None:
        """Registra un voto per una materia."""
        if voto < 18 or voto > 30:
            raise ValueError(f"Voto {voto} non valido (deve essere tra 18 e 30)")
        self._voti[materia] = voto

    def media_voti(self) -> float:
        """Calcola la media dei voti."""
        if not self._voti:
            return 0.0
        return round(sum(self._voti.values()) / len(self._voti), 2)

    def num_esami(self) -> int:
        """Restituisce il numero di esami superati."""
        return len(self._voti)

    def ha_superato(self, materia: str) -> bool:
        """Verifica se lo studente ha superato un esame."""
        return materia in self._voti

    def __repr__(self) -> str:
        return f"Studente({self._matricola}, {self.nome_completo})"

    def __eq__(self, altro: object) -> bool:
        if not isinstance(altro, Studente):
            return NotImplemented
        return self._matricola == altro._matricola


class Corso:
    """Rappresenta un corso universitario con studenti iscritti."""

    def __init__(self, codice: str, nome: str, crediti: int) -> None:
        self._codice: str = codice
        self._nome: str = nome
        self._crediti: int = crediti
        self._iscritti: list[Studente] = []

    @property
    def codice(self) -> str:
        return self._codice

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def crediti(self) -> int:
        return self._crediti

    def iscrivi(self, studente: Studente) -> bool:
        """
        Iscrive uno studente al corso.
        Restituisce True se l'iscrizione e' avvenuta, False se gia' iscritto.
        """
        if studente in self._iscritti:
            return False
        self._iscritti.append(studente)
        return True

    def disiscrivi(self, studente: Studente) -> bool:
        """Rimuove uno studente dal corso."""
        if studente not in self._iscritti:
            return False
        self._iscritti.remove(studente)
        return True

    def num_iscritti(self) -> int:
        return len(self._iscritti)

    def lista_iscritti(self) -> list[str]:
        """Restituisce la lista dei nomi degli iscritti, ordinata."""
        return sorted([s.nome_completo for s in self._iscritti])

    def media_corso(self) -> float:
        """
        Calcola la media dei voti degli studenti iscritti che hanno
        superato l'esame di questo corso.
        """
        voti: list[float] = []
        for studente in self._iscritti:
            if studente.ha_superato(self._nome):
                voti.append(studente.media_voti())
        if not voti:
            return 0.0
        return round(sum(voti) / len(voti), 2)

    def __repr__(self) -> str:
        return f"Corso({self._codice}, {self._nome}, {self.num_iscritti()} iscritti)"


# --- Test Studente e Corso ---
# Crea studenti
alice: Studente = Studente("MAT001", "Alice", "Rossi")
bob: Studente = Studente("MAT002", "Bob", "Bianchi")
carla: Studente = Studente("MAT003", "Carla", "Verdi")

# Registra voti
alice.registra_voto("Analisi I", 28)
alice.registra_voto("Programmazione", 30)
bob.registra_voto("Analisi I", 24)
bob.registra_voto("Programmazione", 22)
carla.registra_voto("Programmazione", 27)

assert alice.media_voti() == 29.0
assert bob.media_voti() == 23.0
assert alice.num_esami() == 2
assert alice.ha_superato("Analisi I") is True
assert carla.ha_superato("Analisi I") is False

# Test voto non valido
errore_voto: bool = False
try:
    alice.registra_voto("Fisica", 15)  # troppo basso
except ValueError:
    errore_voto = True
assert errore_voto

# Crea corsi
analisi: Corso = Corso("MAT101", "Analisi I", 12)
prog: Corso = Corso("INF101", "Programmazione", 9)

# Iscrizioni
assert analisi.iscrivi(alice) is True
assert analisi.iscrivi(bob) is True
assert analisi.iscrivi(alice) is False   # gia' iscritta
assert analisi.num_iscritti() == 2

assert prog.iscrivi(alice) is True
assert prog.iscrivi(bob) is True
assert prog.iscrivi(carla) is True
assert prog.num_iscritti() == 3

# Lista iscritti (ordinata alfabeticamente)
assert analisi.lista_iscritti() == ["Alice Rossi", "Bob Bianchi"]

# Disiscrizione
assert analisi.disiscrivi(bob) is True
assert analisi.num_iscritti() == 1
assert analisi.disiscrivi(bob) is False  # non piu' iscritto

# Uguaglianza basata su matricola
alice_copia: Studente = Studente("MAT001", "Alice", "Rossi")
assert alice == alice_copia
print("Esercizio 4 (Studente/Corso): SUPERATO")


# ============================================================================
print("\n" + "=" * 60)
print("TUTTI GLI ESERCIZI DEL LABORATORIO 06 SUPERATI!")
print("=" * 60)
