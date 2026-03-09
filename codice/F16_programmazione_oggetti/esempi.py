# F16 — Programmazione a oggetti
# Esempi per la lezione frontale 16

from __future__ import annotations
import math
from dataclasses import dataclass, field

# ============================================================
# 1. CLASSE BASE: Studente
# ============================================================
print("=== Classe Studente ===")


class Studente:
    """Rappresenta uno studente universitario."""

    # Attributo di classe (condiviso da tutte le istanze)
    universita: str = "Università degli Studi"
    _contatore: int = 0

    def __init__(self, nome: str, cognome: str, matricola: int) -> None:
        """Inizializza un nuovo studente."""
        # Attributi di istanza
        self.nome: str = nome
        self.cognome: str = cognome
        self.matricola: int = matricola
        self._voti: list[int] = []  # attributo "privato" per convenzione
        Studente._contatore += 1

    def aggiungi_voto(self, voto: int) -> None:
        """Aggiunge un voto alla lista (con validazione)."""
        if not 18 <= voto <= 30:
            raise ValueError(f"Voto {voto} non valido (deve essere 18-30)")
        self._voti.append(voto)

    def media_voti(self) -> float:
        """Calcola la media dei voti."""
        if not self._voti:
            return 0.0
        return sum(self._voti) / len(self._voti)

    @property
    def nome_completo(self) -> str:
        """Restituisce il nome completo (proprietà di sola lettura)."""
        return f"{self.nome} {self.cognome}"

    @property
    def numero_esami(self) -> int:
        """Restituisce il numero di esami sostenuti."""
        return len(self._voti)

    def __str__(self) -> str:
        """Rappresentazione leggibile per l'utente."""
        return f"{self.nome_completo} (mat. {self.matricola})"

    def __repr__(self) -> str:
        """Rappresentazione tecnica per il debug."""
        return f"Studente({self.nome!r}, {self.cognome!r}, {self.matricola})"

    @classmethod
    def conteggio_studenti(cls) -> int:
        """Restituisce il numero totale di studenti creati."""
        return cls._contatore


# Creazione e test
Studente._contatore = 0  # reset per i test
s1: Studente = Studente("Marco", "Rossi", 12345)
s2: Studente = Studente("Laura", "Bianchi", 12346)

s1.aggiungi_voto(28)
s1.aggiungi_voto(30)
s1.aggiungi_voto(25)

assert s1.nome_completo == "Marco Rossi"
assert s1.media_voti() == (28 + 30 + 25) / 3
assert s1.numero_esami == 3
assert str(s1) == "Marco Rossi (mat. 12345)"
assert Studente.conteggio_studenti() == 2

print(f"str:  {s1}")
print(f"repr: {repr(s1)}")
print(f"Media: {s1.media_voti():.2f}")
print(f"Esami: {s1.numero_esami}")
print(f"Studenti totali: {Studente.conteggio_studenti()}")

# Validazione
try:
    s1.aggiungi_voto(15)
except ValueError as e:
    print(f"Errore catturato: {e}")

# ============================================================
# 2. CLASSE Punto2D
# ============================================================
print("\n=== Classe Punto2D ===")


class Punto2D:
    """Rappresenta un punto nel piano cartesiano."""

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
        """Calcola la distanza euclidea da un altro punto."""
        return math.sqrt((self._x - altro._x) ** 2 + (self._y - altro._y) ** 2)

    def distanza_origine(self) -> float:
        """Calcola la distanza dall'origine."""
        return self.distanza_da(Punto2D(0, 0))

    def traslato(self, dx: float, dy: float) -> Punto2D:
        """Restituisce un NUOVO punto traslato (immutabile)."""
        return Punto2D(self._x + dx, self._y + dy)

    def __add__(self, altro: Punto2D) -> Punto2D:
        """Somma vettoriale di due punti."""
        return Punto2D(self._x + altro._x, self._y + altro._y)

    def __eq__(self, altro: object) -> bool:
        if not isinstance(altro, Punto2D):
            return NotImplemented
        return self._x == altro._x and self._y == altro._y

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"

    def __repr__(self) -> str:
        return f"Punto2D({self._x}, {self._y})"


# Test
p1: Punto2D = Punto2D(3, 4)
p2: Punto2D = Punto2D(0, 0)

assert p1.distanza_origine() == 5.0
assert p1.distanza_da(p2) == 5.0

p3: Punto2D = p1.traslato(1, 1)
assert p3 == Punto2D(4, 5)

p4: Punto2D = p1 + p2
assert p4 == p1

print(f"p1 = {p1}")
print(f"Distanza dall'origine: {p1.distanza_origine()}")
print(f"p1 traslato di (1,1): {p3}")
print(f"p1 + Punto2D(1,2) = {p1 + Punto2D(1, 2)}")

# ============================================================
# 3. CLASSE ContoBancario con @property
# ============================================================
print("\n=== Classe ContoBancario ===")


class ContoBancario:
    """Rappresenta un conto bancario con saldo protetto."""

    def __init__(self, titolare: str, saldo_iniziale: float = 0.0) -> None:
        self._titolare: str = titolare
        self._saldo: float = saldo_iniziale
        self._operazioni: list[str] = []
        if saldo_iniziale > 0:
            self._operazioni.append(f"Apertura: +{saldo_iniziale:.2f}")

    @property
    def titolare(self) -> str:
        """Nome del titolare (sola lettura)."""
        return self._titolare

    @property
    def saldo(self) -> float:
        """Saldo attuale (sola lettura diretta)."""
        return self._saldo

    def deposita(self, importo: float) -> None:
        """Deposita un importo sul conto."""
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        self._saldo += importo
        self._operazioni.append(f"Deposito: +{importo:.2f}")

    def preleva(self, importo: float) -> None:
        """Preleva un importo dal conto."""
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        if importo > self._saldo:
            raise ValueError(f"Saldo insufficiente ({self._saldo:.2f})")
        self._saldo -= importo
        self._operazioni.append(f"Prelievo: -{importo:.2f}")

    def estratto_conto(self) -> list[str]:
        """Restituisce la lista delle operazioni."""
        return self._operazioni.copy()  # copia per sicurezza

    def __str__(self) -> str:
        return f"Conto di {self._titolare}: {self._saldo:.2f} EUR"


# Test
conto: ContoBancario = ContoBancario("Marco Rossi", 1000.0)
conto.deposita(500.0)
conto.preleva(200.0)

assert conto.saldo == 1300.0
assert conto.titolare == "Marco Rossi"
assert len(conto.estratto_conto()) == 3

print(f"{conto}")
print("Estratto conto:")
for op in conto.estratto_conto():
    print(f"  {op}")

# Test prelievo eccessivo
try:
    conto.preleva(5000.0)
except ValueError as e:
    print(f"Errore catturato: {e}")

# ============================================================
# 4. EREDITARIETÀ
# ============================================================
print("\n=== Ereditarietà ===")


class Persona:
    """Classe base per le persone."""

    def __init__(self, nome: str, cognome: str, eta: int) -> None:
        self.nome: str = nome
        self.cognome: str = cognome
        self.eta: int = eta

    def presentati(self) -> str:
        return f"Sono {self.nome} {self.cognome}, ho {self.eta} anni"

    def __str__(self) -> str:
        return f"{self.nome} {self.cognome}"


class StudenteUni(Persona):
    """Studente universitario che estende Persona."""

    def __init__(
        self, nome: str, cognome: str, eta: int,
        matricola: int, corso: str
    ) -> None:
        super().__init__(nome, cognome, eta)  # chiama __init__ del genitore
        self.matricola: int = matricola
        self.corso: str = corso

    def presentati(self) -> str:
        # Override del metodo del genitore
        base: str = super().presentati()
        return f"{base}, studio {self.corso} (mat. {self.matricola})"


class Docente(Persona):
    """Docente che estende Persona."""

    def __init__(
        self, nome: str, cognome: str, eta: int,
        dipartimento: str
    ) -> None:
        super().__init__(nome, cognome, eta)
        self.dipartimento: str = dipartimento

    def presentati(self) -> str:
        base: str = super().presentati()
        return f"{base}, insegno nel dipartimento di {self.dipartimento}"


# Test polimorfismo
persone: list[Persona] = [
    Persona("Mario", "Verdi", 45),
    StudenteUni("Marco", "Rossi", 22, 12345, "Informatica"),
    Docente("Prof. Anna", "Bianchi", 50, "Matematica"),
]

for persona in persone:
    print(f"  {persona.presentati()}")

assert isinstance(persone[1], StudenteUni)
assert isinstance(persone[1], Persona)  # è anche una Persona!

# ============================================================
# 5. COMPOSIZIONE
# ============================================================
print("\n=== Composizione ===")


class Indirizzo:
    """Rappresenta un indirizzo postale."""

    def __init__(self, via: str, citta: str, cap: str) -> None:
        self.via: str = via
        self.citta: str = citta
        self.cap: str = cap

    def __str__(self) -> str:
        return f"{self.via}, {self.cap} {self.citta}"


class Contatto:
    """Contatto con nome e indirizzo (composizione)."""

    def __init__(self, nome: str, email: str, indirizzo: Indirizzo) -> None:
        self.nome: str = nome
        self.email: str = email
        self.indirizzo: Indirizzo = indirizzo  # composizione

    def __str__(self) -> str:
        return f"{self.nome} <{self.email}> — {self.indirizzo}"


ind: Indirizzo = Indirizzo("Via Roma 1", "Milano", "20100")
contatto: Contatto = Contatto("Marco Rossi", "marco@email.it", ind)
assert "Milano" in str(contatto)
print(f"Contatto: {contatto}")

# ============================================================
# 6. DATACLASSES
# ============================================================
print("\n=== Dataclasses ===")


@dataclass
class PuntoDataclass:
    """Punto 2D implementato come dataclass."""
    x: float
    y: float

    def distanza_da(self, altro: PuntoDataclass) -> float:
        return math.sqrt((self.x - altro.x) ** 2 + (self.y - altro.y) ** 2)


@dataclass
class StudenteDataclass:
    """Studente implementato come dataclass."""
    nome: str
    cognome: str
    matricola: int
    voti: list[int] = field(default_factory=list)

    @property
    def nome_completo(self) -> str:
        return f"{self.nome} {self.cognome}"

    def media(self) -> float:
        if not self.voti:
            return 0.0
        return sum(self.voti) / len(self.voti)


# Le dataclass generano automaticamente __init__, __repr__, __eq__
pd1: PuntoDataclass = PuntoDataclass(3.0, 4.0)
pd2: PuntoDataclass = PuntoDataclass(3.0, 4.0)
pd3: PuntoDataclass = PuntoDataclass(0.0, 0.0)

assert pd1 == pd2  # __eq__ generato automaticamente
assert pd1.distanza_da(pd3) == 5.0
print(f"Punto: {pd1}")  # __repr__ generato automaticamente
print(f"pd1 == pd2: {pd1 == pd2}")

sd: StudenteDataclass = StudenteDataclass("Marco", "Rossi", 12345, [28, 30, 25])
assert sd.nome_completo == "Marco Rossi"
assert abs(sd.media() - 27.666666) < 0.001
print(f"Studente: {sd}")
print(f"Media: {sd.media():.2f}")

# Dataclass con default_factory — ogni istanza ha la propria lista
sd2: StudenteDataclass = StudenteDataclass("Laura", "Bianchi", 12346)
assert sd2.voti == []  # lista vuota indipendente
sd2.voti.append(30)
assert sd.voti == [28, 30, 25]  # non influenzato!
print(f"\n{sd.nome_completo}: voti={sd.voti}")
print(f"{sd2.nome_completo}: voti={sd2.voti}")

print("\n=== Fine esempi F16 ===")
