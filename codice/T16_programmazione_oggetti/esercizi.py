# T16 — Programmazione a oggetti
# Esercizi per la lezione frontale 16

from __future__ import annotations
import math

# ============================================================
# ESERCIZIO 1: Classe Matrice
# Implementare una classe per matrici con operazioni base.
# ============================================================
print("=== Esercizio 1: Classe Matrice ===")


class Matrice:
    """Matrice bidimensionale con operazioni base."""

    def __init__(self, dati: list[list[float]]) -> None:
        """
        Inizializza la matrice da una lista di liste.
        Verifica che tutte le righe abbiano la stessa lunghezza.
        """
        if not dati or not dati[0]:
            raise ValueError("La matrice non può essere vuota")
        n_colonne: int = len(dati[0])
        for i, riga in enumerate(dati):
            if len(riga) != n_colonne:
                raise ValueError(
                    f"Riga {i} ha {len(riga)} colonne, attese {n_colonne}"
                )
        # Copia profonda per evitare aliasing
        self._dati: list[list[float]] = [riga.copy() for riga in dati]
        self._righe: int = len(dati)
        self._colonne: int = n_colonne

    @property
    def righe(self) -> int:
        """Numero di righe."""
        return self._righe

    @property
    def colonne(self) -> int:
        """Numero di colonne."""
        return self._colonne

    @property
    def dimensioni(self) -> tuple[int, int]:
        """Dimensioni della matrice (righe, colonne)."""
        return (self._righe, self._colonne)

    def __getitem__(self, indici: tuple[int, int]) -> float:
        """Accesso con m[i, j]."""
        i, j = indici
        return self._dati[i][j]

    def __setitem__(self, indici: tuple[int, int], valore: float) -> None:
        """Assegnamento con m[i, j] = valore."""
        i, j = indici
        self._dati[i][j] = valore

    def __add__(self, altra: Matrice) -> Matrice:
        """Somma di due matrici."""
        if self.dimensioni != altra.dimensioni:
            raise ValueError("Le matrici devono avere le stesse dimensioni")
        risultato: list[list[float]] = [
            [self._dati[i][j] + altra._dati[i][j] for j in range(self._colonne)]
            for i in range(self._righe)
        ]
        return Matrice(risultato)

    def __mul__(self, scalare: float) -> Matrice:
        """Moltiplicazione per uno scalare."""
        risultato: list[list[float]] = [
            [self._dati[i][j] * scalare for j in range(self._colonne)]
            for i in range(self._righe)
        ]
        return Matrice(risultato)

    def prodotto(self, altra: Matrice) -> Matrice:
        """Prodotto matriciale (self x altra)."""
        if self._colonne != altra._righe:
            raise ValueError(
                f"Dimensioni incompatibili: {self.dimensioni} x {altra.dimensioni}"
            )
        risultato: list[list[float]] = [
            [
                sum(self._dati[i][k] * altra._dati[k][j] for k in range(self._colonne))
                for j in range(altra._colonne)
            ]
            for i in range(self._righe)
        ]
        return Matrice(risultato)

    def trasposta(self) -> Matrice:
        """Restituisce la matrice trasposta."""
        risultato: list[list[float]] = [
            [self._dati[j][i] for j in range(self._righe)]
            for i in range(self._colonne)
        ]
        return Matrice(risultato)

    def __eq__(self, altra: object) -> bool:
        if not isinstance(altra, Matrice):
            return NotImplemented
        return self._dati == altra._dati

    def __str__(self) -> str:
        righe_str: list[str] = []
        for riga in self._dati:
            valori: str = "  ".join(f"{v:7.2f}" for v in riga)
            righe_str.append(f"| {valori} |")
        return "\n".join(righe_str)

    def __repr__(self) -> str:
        return f"Matrice({self._dati})"

    @staticmethod
    def identita(n: int) -> Matrice:
        """Crea una matrice identità n x n."""
        dati: list[list[float]] = [
            [1.0 if i == j else 0.0 for j in range(n)]
            for i in range(n)
        ]
        return Matrice(dati)

    @staticmethod
    def zeros(righe: int, colonne: int) -> Matrice:
        """Crea una matrice di zeri."""
        return Matrice([[0.0] * colonne for _ in range(righe)])


# Test
m1: Matrice = Matrice([[1.0, 2.0], [3.0, 4.0]])
m2: Matrice = Matrice([[5.0, 6.0], [7.0, 8.0]])

# Test dimensioni
assert m1.dimensioni == (2, 2)
assert m1.righe == 2
assert m1.colonne == 2

# Test accesso
assert m1[0, 0] == 1.0
assert m1[1, 1] == 4.0

# Test somma
m3: Matrice = m1 + m2
assert m3[0, 0] == 6.0
assert m3[1, 1] == 12.0
print(f"m1 + m2 =\n{m3}\n")

# Test moltiplicazione per scalare
m4: Matrice = m1 * 2
assert m4[0, 0] == 2.0
assert m4[1, 1] == 8.0
print(f"m1 * 2 =\n{m4}\n")

# Test prodotto matriciale
m5: Matrice = m1.prodotto(m2)
assert m5[0, 0] == 19.0  # 1*5 + 2*7
assert m5[0, 1] == 22.0  # 1*6 + 2*8
assert m5[1, 0] == 43.0  # 3*5 + 4*7
assert m5[1, 1] == 50.0  # 3*6 + 4*8
print(f"m1 x m2 =\n{m5}\n")

# Test trasposta
mt: Matrice = Matrice([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
mt_t: Matrice = mt.trasposta()
assert mt_t.dimensioni == (3, 2)
assert mt_t[0, 1] == 4.0
assert mt_t[2, 0] == 3.0
print(f"Trasposta di\n{mt}\nè\n{mt_t}\n")

# Test identità
identita: Matrice = Matrice.identita(3)
assert identita[0, 0] == 1.0
assert identita[0, 1] == 0.0
print(f"Identità 3x3:\n{identita}\n")

# A * I = A
prodotto_id: Matrice = m1.prodotto(Matrice.identita(2))
assert prodotto_id == m1

print("Esercizio 1 superato!\n")

# ============================================================
# ESERCIZIO 2: Classe Statistiche
# Classe che calcola statistiche su una collezione di dati.
# ============================================================
print("=== Esercizio 2: Classe Statistiche ===")


class Statistiche:
    """Calcola e memorizza statistiche su una collezione di dati numerici."""

    def __init__(self, dati: list[float]) -> None:
        if not dati:
            raise ValueError("I dati non possono essere vuoti")
        self._dati: list[float] = sorted(dati.copy())
        self._n: int = len(dati)
        # Pre-calcolo delle statistiche principali
        self._media: float = sum(self._dati) / self._n
        self._varianza: float = (
            sum((x - self._media) ** 2 for x in self._dati) / (self._n - 1)
            if self._n > 1 else 0.0
        )

    @property
    def n(self) -> int:
        """Numero di osservazioni."""
        return self._n

    @property
    def media(self) -> float:
        """Media aritmetica."""
        return self._media

    @property
    def varianza(self) -> float:
        """Varianza campionaria."""
        return self._varianza

    @property
    def deviazione_standard(self) -> float:
        """Deviazione standard campionaria."""
        return math.sqrt(self._varianza)

    @property
    def mediana(self) -> float:
        """Mediana."""
        mid: int = self._n // 2
        if self._n % 2 == 1:
            return self._dati[mid]
        return (self._dati[mid - 1] + self._dati[mid]) / 2

    @property
    def minimo(self) -> float:
        return self._dati[0]

    @property
    def massimo(self) -> float:
        return self._dati[-1]

    @property
    def range(self) -> float:
        """Intervallo (max - min)."""
        return self.massimo - self.minimo

    def percentile(self, p: float) -> float:
        """
        Calcola il p-esimo percentile (0-100) con interpolazione lineare.
        """
        if not 0 <= p <= 100:
            raise ValueError("Il percentile deve essere tra 0 e 100")
        if self._n == 1:
            return self._dati[0]
        indice: float = (p / 100) * (self._n - 1)
        inferiore: int = int(indice)
        superiore: int = min(inferiore + 1, self._n - 1)
        peso: float = indice - inferiore
        return self._dati[inferiore] * (1 - peso) + self._dati[superiore] * peso

    @property
    def q1(self) -> float:
        """Primo quartile (25° percentile)."""
        return self.percentile(25)

    @property
    def q3(self) -> float:
        """Terzo quartile (75° percentile)."""
        return self.percentile(75)

    @property
    def iqr(self) -> float:
        """Intervallo interquartile (Q3 - Q1)."""
        return self.q3 - self.q1

    def riepilogo(self) -> dict[str, float]:
        """Restituisce un dizionario con tutte le statistiche."""
        return {
            "n": float(self._n),
            "media": self.media,
            "mediana": self.mediana,
            "varianza": self.varianza,
            "dev_standard": self.deviazione_standard,
            "minimo": self.minimo,
            "massimo": self.massimo,
            "range": self.range,
            "Q1": self.q1,
            "Q3": self.q3,
            "IQR": self.iqr,
        }

    def __str__(self) -> str:
        return (
            f"Statistiche(n={self._n}, media={self.media:.2f}, "
            f"mediana={self.mediana:.2f}, ds={self.deviazione_standard:.2f})"
        )


# Test
voti: list[float] = [18.0, 22.0, 24.0, 25.0, 27.0, 28.0, 28.0, 30.0, 30.0, 30.0]
stats: Statistiche = Statistiche(voti)

assert stats.n == 10
assert stats.minimo == 18.0
assert stats.massimo == 30.0
assert stats.range == 12.0
assert abs(stats.media - 26.2) < 1e-9
assert stats.mediana == 27.5  # media di 27 e 28

print(f"Dati: {voti}")
print(f"{stats}")
print("\nRiepilogo completo:")
for chiave, valore in stats.riepilogo().items():
    print(f"  {chiave:<15}: {valore:>8.2f}")

print("\nEsercizio 2 superato!\n")

# ============================================================
# ESERCIZIO 3: Classe Rubrica (address book)
# ============================================================
print("=== Esercizio 3: Classe Rubrica ===")


class ContattoRubrica:
    """Singolo contatto nella rubrica."""

    def __init__(
        self, nome: str, cognome: str,
        telefono: str = "", email: str = ""
    ) -> None:
        self.nome: str = nome
        self.cognome: str = cognome
        self.telefono: str = telefono
        self.email: str = email

    @property
    def nome_completo(self) -> str:
        return f"{self.nome} {self.cognome}"

    def corrisponde(self, termine: str) -> bool:
        """Verifica se il contatto corrisponde a un termine di ricerca."""
        termine_lower: str = termine.lower()
        return (
            termine_lower in self.nome.lower()
            or termine_lower in self.cognome.lower()
            or termine_lower in self.telefono
            or termine_lower in self.email.lower()
        )

    def __str__(self) -> str:
        parti: list[str] = [self.nome_completo]
        if self.telefono:
            parti.append(f"tel: {self.telefono}")
        if self.email:
            parti.append(f"email: {self.email}")
        return " | ".join(parti)

    def __repr__(self) -> str:
        return (f"ContattoRubrica({self.nome!r}, {self.cognome!r}, "
                f"{self.telefono!r}, {self.email!r})")

    def __eq__(self, altro: object) -> bool:
        if not isinstance(altro, ContattoRubrica):
            return NotImplemented
        return (self.nome == altro.nome and self.cognome == altro.cognome
                and self.telefono == altro.telefono)


class Rubrica:
    """Rubrica telefonica con operazioni di gestione contatti."""

    def __init__(self) -> None:
        self._contatti: list[ContattoRubrica] = []

    @property
    def dimensione(self) -> int:
        """Numero di contatti nella rubrica."""
        return len(self._contatti)

    def aggiungi(self, contatto: ContattoRubrica) -> None:
        """Aggiunge un contatto alla rubrica."""
        # Verifica duplicati
        for c in self._contatti:
            if c == contatto:
                raise ValueError(f"Contatto '{contatto.nome_completo}' già presente")
        self._contatti.append(contatto)

    def rimuovi(self, nome: str, cognome: str) -> bool:
        """Rimuove un contatto per nome e cognome. Restituisce True se trovato."""
        for i, c in enumerate(self._contatti):
            if c.nome.lower() == nome.lower() and c.cognome.lower() == cognome.lower():
                self._contatti.pop(i)
                return True
        return False

    def cerca(self, termine: str) -> list[ContattoRubrica]:
        """Cerca contatti che corrispondono al termine."""
        return [c for c in self._contatti if c.corrisponde(termine)]

    def tutti_ordinati(self, per_cognome: bool = True) -> list[ContattoRubrica]:
        """Restituisce tutti i contatti ordinati."""
        if per_cognome:
            return sorted(self._contatti, key=lambda c: (c.cognome.lower(), c.nome.lower()))
        return sorted(self._contatti, key=lambda c: (c.nome.lower(), c.cognome.lower()))

    def esporta(self) -> list[dict[str, str]]:
        """Esporta la rubrica come lista di dizionari."""
        return [
            {
                "nome": c.nome,
                "cognome": c.cognome,
                "telefono": c.telefono,
                "email": c.email,
            }
            for c in self.tutti_ordinati()
        ]

    @classmethod
    def da_lista(cls, dati: list[dict[str, str]]) -> Rubrica:
        """Crea una rubrica da una lista di dizionari."""
        rubrica: Rubrica = cls()
        for d in dati:
            contatto: ContattoRubrica = ContattoRubrica(
                nome=d.get("nome", ""),
                cognome=d.get("cognome", ""),
                telefono=d.get("telefono", ""),
                email=d.get("email", ""),
            )
            rubrica.aggiungi(contatto)
        return rubrica

    def __len__(self) -> int:
        return self.dimensione

    def __str__(self) -> str:
        if not self._contatti:
            return "Rubrica vuota"
        righe: list[str] = [f"Rubrica ({self.dimensione} contatti):"]
        for c in self.tutti_ordinati():
            righe.append(f"  - {c}")
        return "\n".join(righe)


# Test
rubrica: Rubrica = Rubrica()

# Aggiungi contatti
rubrica.aggiungi(ContattoRubrica("Marco", "Rossi", "333-1234567", "marco@email.it"))
rubrica.aggiungi(ContattoRubrica("Laura", "Bianchi", "333-7654321", "laura@email.it"))
rubrica.aggiungi(ContattoRubrica("Giulia", "Rossi", "333-1111111", "giulia@email.it"))
rubrica.aggiungi(ContattoRubrica("Paolo", "Verdi", "333-2222222", "paolo@email.it"))
rubrica.aggiungi(ContattoRubrica("Anna", "Neri", "333-3333333", "anna@email.it"))

assert rubrica.dimensione == 5
assert len(rubrica) == 5
print(rubrica)

# Test ricerca
risultati_rossi: list[ContattoRubrica] = rubrica.cerca("Rossi")
assert len(risultati_rossi) == 2
print(f"\nRicerca 'Rossi': {len(risultati_rossi)} risultati")
for c in risultati_rossi:
    print(f"  {c}")

risultati_email: list[ContattoRubrica] = rubrica.cerca("laura")
assert len(risultati_email) == 1
assert risultati_email[0].nome == "Laura"

# Test rimozione
rimosso: bool = rubrica.rimuovi("Paolo", "Verdi")
assert rimosso is True
assert rubrica.dimensione == 4
non_rimosso: bool = rubrica.rimuovi("Inesistente", "Persona")
assert non_rimosso is False

# Test duplicato
try:
    rubrica.aggiungi(ContattoRubrica("Marco", "Rossi", "333-1234567"))
except ValueError as e:
    print(f"\nErrore duplicato: {e}")

# Test esportazione
esportati: list[dict[str, str]] = rubrica.esporta()
assert len(esportati) == 4
assert esportati[0]["cognome"] == "Bianchi"  # ordinato per cognome
print(f"\nEsportazione: {len(esportati)} contatti")

# Test creazione da lista
dati_import: list[dict[str, str]] = [
    {"nome": "Test1", "cognome": "A", "telefono": "111", "email": "a@a.it"},
    {"nome": "Test2", "cognome": "B", "telefono": "222", "email": "b@b.it"},
]
rubrica2: Rubrica = Rubrica.da_lista(dati_import)
assert len(rubrica2) == 2

print("\nEsercizio 3 superato!")
print("\n=== Tutti gli esercizi T16 completati! ===")
