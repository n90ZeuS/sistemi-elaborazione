# L06 — Classi e oggetti
# Soluzioni degli esercizi del laboratorio 06
#
# Ogni esercizio corrisponde a un file della traccia (nome tra parentesi).
# Per provarne uno solo, copiatelo in un file a parte.


# ============================================================================
# ESERCIZIO 1: un esame del libretto — esame.py
# ============================================================================
print("--- Esercizio 1: Un esame del libretto ---")
class Esame:
    """Un esame superato: nome, crediti e voto."""

    def __init__(self, nome: str, cfu: int, voto: int) -> None:
        self.nome: str = nome
        self.cfu: int = cfu
        self.voto: int = voto

    def punti(self) -> int:
        """Voto moltiplicato per i crediti."""
        return self.voto * self.cfu

esami: list[Esame] = [Esame("Analisi 1", 12, 26),
                      Esame("Statistica 1", 9, 29),
                      Esame("Informatica", 6, 30)]
cfu: int = 0
punti: int = 0
for e in esami:
    print(f"{e.nome}: {e.voto} ({e.cfu} CFU)")
    cfu += e.cfu
    punti += e.punti()
print(f"CFU: {cfu}, media ponderata: {punti / cfu:.2f}")
print()


# ============================================================================
# ESERCIZIO 2: la tessera della mensa — tessera_mensa.py
# ============================================================================
print("--- Esercizio 2: La tessera della mensa ---")
class Tessera:
    """Tessera prepagata della mensa universitaria."""

    def __init__(self, titolare: str, saldo: float) -> None:
        if saldo < 0:
            raise ValueError("Il saldo iniziale è negativo")
        self.titolare: str = titolare
        self.saldo: float = saldo

    def ricarica(self, importo: float) -> None:
        if importo <= 0:
            raise ValueError("La ricarica deve essere positiva")
        self.saldo += importo

    def paga(self, prezzo: float) -> None:
        if prezzo > self.saldo:
            raise ValueError(f"Saldo insufficiente: {self.saldo:.2f}")
        self.saldo -= prezzo

    def __str__(self) -> str:
        return f"Tessera di {self.titolare}: {self.saldo:.2f} EUR"

tessera: Tessera = Tessera("Anna Rossi", 10.0)
print(tessera)
for prezzo in [4.50, 4.50, 4.50]:
    try:
        tessera.paga(prezzo)
    except ValueError as e:
        print(e)
    else:
        print(f"Pagato {prezzo:.2f} EUR, restano {tessera.saldo:.2f}")
tessera.ricarica(20.0)
print(tessera)
print()


# ============================================================================
# ESERCIZIO 3: la coda in segreteria — segreteria.py
# ============================================================================
print("--- Esercizio 3: La coda in segreteria ---")
class Ticket:
    """Biglietto numerato per la coda della segreteria."""
    SERVIZI: tuple[str, ...] = ("iscrizioni", "tasse", "esami")
    emessi: int = 0                       # attributo di classe

    def __init__(self, servizio: str) -> None:
        if servizio not in Ticket.SERVIZI:
            raise ValueError(f"Servizio sconosciuto: {servizio}")
        Ticket.emessi += 1
        self.numero: int = Ticket.emessi  # attributo di istanza
        self.servizio: str = servizio

    def __str__(self) -> str:
        return f"Numero {self.numero} ({self.servizio})"

    def __repr__(self) -> str:
        return f"Ticket({self.numero}, '{self.servizio}')"

coda: list[Ticket] = []
for s in ["esami", "tasse", "esami", "iscrizioni", "esami"]:
    coda.append(Ticket(s))
print(coda)
print(f"Prossimo: {coda[0]}")
print(f"Biglietti emessi: {Ticket.emessi}")
for servizio in Ticket.SERVIZI:
    n: int = len([t for t in coda if t.servizio == servizio])
    print(f"{servizio}: {n}")
print()


# ============================================================================
# ESERCIZIO 4: la graduatoria erasmus — erasmus.py
# ============================================================================
print("--- Esercizio 4: La graduatoria Erasmus ---")
class Candidato:
    """Candidato a una borsa Erasmus."""

    def __init__(self, nome: str, media: float, cfu: int) -> None:
        self.nome: str = nome
        self.media: float = media
        self.cfu: int = cfu

    def __eq__(self, altro: object) -> bool:
        if not isinstance(altro, Candidato):
            return NotImplemented
        return self.media == altro.media and self.cfu == altro.cfu

    def __lt__(self, altro: "Candidato") -> bool:
        """Viene prima chi ha la media più alta, poi più CFU."""
        if self.media != altro.media:
            return self.media > altro.media
        return self.cfu > altro.cfu

    def __str__(self) -> str:
        return f"{self.nome} (media {self.media:.2f}, {self.cfu} CFU)"

candidati: list[Candidato] = [
    Candidato("Luca", 27.4, 90), Candidato("Sara", 28.1, 84),
    Candidato("Paolo", 27.4, 102), Candidato("Elena", 26.9, 120),
    Candidato("Davide", 28.1, 84)]
classifica: list[Candidato] = sorted(candidati)
for posto, c in enumerate(classifica, start=1):
    print(f"{posto}. {c}")
print(f"Pari merito tra 1 e 2: {classifica[0] == classifica[1]}")
print(f"Pari merito tra 3 e 4: {classifica[2] == classifica[3]}")
print()


# ============================================================================
# ESERCIZIO 5: un campione di misure — campione.py
# ============================================================================
print("--- Esercizio 5: Un campione di misure ---")
class Campione:
    """Campione di misure numeriche."""

    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self._valori: list[float] = []   # uso interno

    def aggiungi(self, x: float) -> None:
        self._valori.append(x)

    @property
    def n(self) -> int:
        return len(self._valori)

    @property
    def media(self) -> float:
        return sum(self._valori) / self.n

    @property
    def varianza(self) -> float:
        """Varianza campionaria, con divisore n - 1."""
        m: float = self.media
        scarti: list[float] = [(x - m) ** 2 for x in self._valori]
        return sum(scarti) / (self.n - 1)

altezze: Campione = Campione("Altezze (cm)")
for x in [172, 165, 180, 158, 175]:
    altezze.aggiungi(x)
print(f"{altezze.nome}: {altezze.n} valori")
print(f"Media: {altezze.media:.2f}, varianza: {altezze.varianza:.2f}")
print(f"Deviazione standard: {altezze.varianza ** 0.5:.2f}")
try:
    altezze.media = 175.0
except AttributeError:
    print("La media non si assegna: è calcolata dai valori")
print()


# ============================================================================
# ESERCIZIO 6: il libretto: un oggetto che contiene oggetti — libretto.py
# ============================================================================
print("--- Esercizio 6: Il libretto: un oggetto che contiene oggetti ---")
class Esame:
    def __init__(self, nome: str, cfu: int, voto: int) -> None:
        self.nome: str = nome
        self.cfu: int = cfu
        self.voto: int = voto

    def __str__(self) -> str:
        return f"{self.nome}: {self.voto} ({self.cfu} CFU)"


class Libretto:
    def __init__(self, studente: str) -> None:
        self.studente: str = studente
        self.esami: list[Esame] = []

    def cerca(self, nome: str) -> Esame | None:
        for e in self.esami:
            if e.nome == nome:
                return e
        return None

    def aggiungi(self, esame: Esame) -> None:
        if self.cerca(esame.nome) is not None:
            raise ValueError(f"{esame.nome} è già nel libretto")
        self.esami.append(esame)

    def media(self) -> float:
        cfu: int = sum([e.cfu for e in self.esami])
        return sum([e.voto * e.cfu for e in self.esami]) / cfu

lib: Libretto = Libretto("Giulia Verdi")
lib.aggiungi(Esame("Analisi 1", 12, 26))
lib.aggiungi(Esame("Statistica 1", 9, 29))
lib.aggiungi(Esame("Informatica", 6, 30))
try:
    lib.aggiungi(Esame("Informatica", 6, 28))
except ValueError as e:
    print(e)

print(lib.cerca("Statistica 1"))
print(f"Esami: {len(lib.esami)}, media ponderata {lib.media():.2f}")
print()


# ============================================================================
# ESERCIZIO 7: abbonamenti ai mezzi pubblici — abbonamenti.py
# ============================================================================
print("--- Esercizio 7: Abbonamenti ai mezzi pubblici ---")
class Abbonamento:
    """Abbonamento ai mezzi pubblici, pagato a mesi."""
    PREZZO_MESE: float = 40.0

    def __init__(self, titolare: str, mesi: int) -> None:
        if mesi < 1 or mesi > 12:
            raise ValueError(f"Durata non valida: {mesi} mesi")
        self.titolare: str = titolare
        self.mesi: int = mesi

    def prezzo(self) -> float:
        return self.PREZZO_MESE * self.mesi

    def __str__(self) -> str:
        return (f"{self.titolare}, {self.mesi} mesi: "
                f"{self.prezzo():.2f} EUR")


class AbbonamentoStudente(Abbonamento):
    """Abbonamento scontato per chi ha una matricola."""
    SCONTO: float = 0.3

    def __init__(self, titolare: str, mesi: int,
                 matricola: str) -> None:
        super().__init__(titolare, mesi)
        self.matricola: str = matricola

    def prezzo(self) -> float:
        return super().prezzo() * (1 - self.SCONTO)

    def __str__(self) -> str:
        return f"{super().__str__()}, matricola {self.matricola}"

abbonamenti: list[Abbonamento] = [
    Abbonamento("Marco Bianchi", 12),
    AbbonamentoStudente("Anna Rossi", 10, "2101234"),
    AbbonamentoStudente("Luca Russo", 3, "2102345"),
    Abbonamento("Elena Romano", 2)]

for a in abbonamenti:
    print(a)

print(f"Incasso: {sum([a.prezzo() for a in abbonamenti]):.2f} EUR")
print()


# ============================================================================
# ESERCIZIO 8: la biblioteca di dipartimento — biblioteca.py
# ============================================================================
print("--- Esercizio 8: La biblioteca di dipartimento ---")
class Pubblicazione:
    """Un libro o una rivista della biblioteca."""
    GIORNI: int = 30                      # durata del prestito

    def __init__(self, titolo: str, anno: int) -> None:
        self.titolo: str = titolo
        self.anno: int = anno

    def __str__(self) -> str:
        return f"{self.anno} {self.titolo}: {self.GIORNI} giorni"

    def __lt__(self, altro: "Pubblicazione") -> bool:
        return self.anno < altro.anno


class Rivista(Pubblicazione):
    GIORNI: int = 7                       # le riviste durano meno


class Biblioteca:
    """Una biblioteca ha un catalogo di libri e riviste."""

    def __init__(self) -> None:
        self._catalogo: list[Pubblicazione] = []

    def aggiungi(self, p: Pubblicazione) -> None:
        self._catalogo.append(p)

    def cerca(self, parola: str) -> list[Pubblicazione]:
        return [p for p in self._catalogo
                if parola.lower() in p.titolo.lower()]

    def in_ordine(self) -> list[Pubblicazione]:
        return sorted(self._catalogo)

bib: Biblioteca = Biblioteca()
bib.aggiungi(Pubblicazione("Statistica di base", 2019))
bib.aggiungi(Rivista("Rivista di statistica applicata", 2024))
bib.aggiungi(Pubblicazione("Probabilità e inferenza", 2015))
bib.aggiungi(Rivista("Bollettino di demografia", 2023))
for p in bib.in_ordine():
    print(p)

print(f"Titoli con 'statistica': {len(bib.cerca('statistica'))}")
print()


# ============================================================================
# CHALLENGE MERCATI E FINANZA: il portafoglio a oggetti — ch_mercati.py
# ============================================================================
print("--- Challenge Mercati e finanza: Il portafoglio a oggetti ---")
class Titolo:
    """Un titolo del portafoglio con i prezzi di chiusura."""

    def __init__(self, sigla: str, azioni: int,
                 prezzi: list[float]) -> None:
        if azioni <= 0 or len(prezzi) < 2 or min(prezzi) <= 0:
            raise ValueError(f"{sigla}: azioni o prezzi non validi")
        self.sigla: str = sigla
        self.azioni: int = azioni
        self.prezzi: list[float] = prezzi

    def rendimento(self) -> float:
        return (self.prezzi[-1] - self.prezzi[0]) / self.prezzi[0]

    def valore(self) -> float:
        return self.azioni * self.prezzi[-1]

    def __str__(self) -> str:
        return (f"{self.sigla}: valore {self.valore():.2f}, "
                f"rendimento {self.rendimento():.1%}")

    def __lt__(self, altro: "Titolo") -> bool:
        return self.rendimento() < altro.rendimento()


class Portafoglio:
    """Il portafoglio di un investitore: una lista di titoli."""

    def __init__(self, titolare: str) -> None:
        self.titolare: str = titolare
        self.titoli: list[Titolo] = []

    def aggiungi(self, titolo: Titolo) -> None:
        self.titoli.append(titolo)

    def cerca(self, sigla: str) -> Titolo | None:
        for t in self.titoli:
            if t.sigla == sigla:
                return t
        return None

    def valore_totale(self) -> float:
        return sum([t.valore() for t in self.titoli])

port: Portafoglio = Portafoglio("Giulia")
for sigla, azioni, prezzi in [
        ("ENRG", 20, [24.10, 24.60, 25.30, 25.10]),
        ("BANK", 50, [12.40, 12.20, 12.70, 12.90]),
        ("TECH", 10, [48.00, 49.20, 50.40, 51.20]),
        ("MIB", 0, [33.50, 33.90, 34.20, 34.10])]:
    try:
        port.aggiungi(Titolo(sigla, azioni, prezzi))
    except ValueError as e:
        print(e)

for t in sorted(port.titoli, reverse=True):
    print(t)

print(port.cerca("BANK"))
print(port.cerca("MIB"))
print(f"Valore totale: {port.valore_totale():.2f}")
print()


# ============================================================================
# CHALLENGE SPORT: il campionato a oggetti — ch_sport.py
# ============================================================================
print("--- Challenge Sport: Il campionato a oggetti ---")
class Pilota:
    """Un pilota con i suoi tempi sul giro, in secondi."""

    def __init__(self, nome: str, scuderia: str,
                 tempi: list[float]) -> None:
        if len(tempi) == 0 or min(tempi) <= 0:
            raise ValueError(f"{nome}: tempi non validi")
        self.nome: str = nome
        self.scuderia: str = scuderia
        self.tempi: list[float] = tempi

    def media(self) -> float:
        return sum(self.tempi) / len(self.tempi)

    def migliore(self) -> float:
        return min(self.tempi)

    def __str__(self) -> str:
        return (f"{self.nome}: media {self.media():.2f}, "
                f"migliore {self.migliore():.2f}")

    def __lt__(self, altro: "Pilota") -> bool:
        return self.media() < altro.media()


class Gara:
    """Una gara del campionato: una lista di piloti."""

    def __init__(self, circuito: str) -> None:
        self.circuito: str = circuito
        self.piloti: list[Pilota] = []

    def aggiungi(self, pilota: Pilota) -> None:
        self.piloti.append(pilota)

    def cerca(self, nome: str) -> Pilota | None:
        for p in self.piloti:
            if p.nome == nome:
                return p
        return None

    def giro_veloce(self) -> float:
        return min([p.migliore() for p in self.piloti])

gara: Gara = Gara("Monza")
for nome, scuderia, tempi in [
        ("Ferri", "Scuderia Rossa", [92.4, 92.1, 92.6]),
        ("Lanza", "Scuderia Rossa", [92.9, 92.7, 92.5]),
        ("Moro", "Scuderia Blu", [93.1, 92.8, 92.3]),
        ("Neri", "Scuderia Blu", [93.6, 93.0, 0.0])]:
    try:
        gara.aggiungi(Pilota(nome, scuderia, tempi))
    except ValueError as e:
        print(e)

for p in sorted(gara.piloti):
    print(p)

print(gara.cerca("Lanza"))
print(gara.cerca("Neri"))
print(f"Giro più veloce: {gara.giro_veloce():.2f}")
print()


# ============================================================================
# CHALLENGE IMPRESE E MARKETING: il negozio online a oggetti — ch_negozio.py
# ============================================================================
print("--- Challenge Imprese e marketing: Il negozio online a oggetti ---")
class Prodotto:
    """Un prodotto con il prezzo e i pezzi venduti ogni settimana."""

    def __init__(self, nome: str, prezzo: float,
                 vendite: list[int]) -> None:
        if prezzo <= 0 or len(vendite) == 0 or min(vendite) < 0:
            raise ValueError(f"{nome}: prezzo o vendite non validi")
        self.nome: str = nome
        self.prezzo: float = prezzo
        self.vendite: list[int] = vendite

    def pezzi(self) -> int:
        return sum(self.vendite)

    def fatturato(self) -> float:
        return self.prezzo * self.pezzi()

    def __str__(self) -> str:
        return (f"{self.nome}: {self.pezzi()} pezzi, "
                f"fatturato {self.fatturato():.2f}")

    def __lt__(self, altro: "Prodotto") -> bool:
        return self.fatturato() < altro.fatturato()


class Negozio:
    """Il negozio online: una lista di prodotti."""

    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.prodotti: list[Prodotto] = []

    def aggiungi(self, prodotto: Prodotto) -> None:
        self.prodotti.append(prodotto)

    def cerca(self, nome: str) -> Prodotto | None:
        for p in self.prodotti:
            if p.nome == nome:
                return p
        return None

    def fatturato_totale(self) -> float:
        return sum([p.fatturato() for p in self.prodotti])

negozio: Negozio = Negozio("StudioShop")
for nome, prezzo, vendite in [
        ("zaino", 39.90, [3, 5, 4]),
        ("borraccia", 14.50, [10, 8, 12]),
        ("quaderno", 3.20, [30, 25, 30]),
        ("cuffie", 59.00, [2, 4, 2]),
        ("lampada", 24.90, [2, -1, 3])]:
    try:
        negozio.aggiungi(Prodotto(nome, prezzo, vendite))
    except ValueError as e:
        print(e)

for p in sorted(negozio.prodotti, reverse=True):
    print(p)

print(negozio.cerca("cuffie"))
print(negozio.cerca("lampada"))
print(f"Fatturato totale: {negozio.fatturato_totale():.2f}")
print()


# ============================================================================
# CHALLENGE SALUTE E SCIENZA: lo studio clinico a oggetti — ch_salute.py
# ============================================================================
print("--- Challenge Salute e scienza: Lo studio clinico a oggetti ---")
class Paziente:
    """Un paziente con la pressione sistolica di ogni visita."""

    def __init__(self, codice: str, gruppo: str,
                 misure: list[float]) -> None:
        if len(misure) < 2 or min(misure) < 60 or max(misure) > 250:
            raise ValueError(f"{codice}: misure non valide")
        self.codice: str = codice
        self.gruppo: str = gruppo
        self.misure: list[float] = misure

    def variazione(self) -> float:
        return self.misure[-1] - self.misure[0]

    def migliorato(self) -> bool:
        return self.variazione() <= -10

    def __str__(self) -> str:
        return (f"{self.codice} ({self.gruppo}): "
                f"variazione {self.variazione():.1f} mmHg")

    def __lt__(self, altro: "Paziente") -> bool:
        return self.variazione() < altro.variazione()


class Studio:
    """Lo studio clinico: una lista di pazienti."""

    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.pazienti: list[Paziente] = []

    def aggiungi(self, paziente: Paziente) -> None:
        self.pazienti.append(paziente)

    def cerca(self, codice: str) -> Paziente | None:
        for p in self.pazienti:
            if p.codice == codice:
                return p
        return None

    def quota_migliorati(self) -> float:
        n: int = len([p for p in self.pazienti if p.migliorato()])
        return n / len(self.pazienti)

studio: Studio = Studio("Integratore per la pressione")
for codice, gruppo, misure in [
        ("P01", "trattamento", [152, 146, 138]),
        ("P02", "controllo", [148, 147, 145]),
        ("P03", "trattamento", [160, 151, 149]),
        ("P04", "controllo", [155, 150, 144]),
        ("P05", "trattamento", [145, 0, 139])]:
    try:
        studio.aggiungi(Paziente(codice, gruppo, misure))
    except ValueError as e:
        print(e)

for p in sorted(studio.pazienti):
    print(p)

print(studio.cerca("P02"))
print(studio.cerca("P05"))
print(f"Migliorati: {studio.quota_migliorati():.1%}")
print()


# ============================================================================
# CHALLENGE CASO E PROBABILITÀ: il tavolo da gioco a oggetti — ch_probabilita.py
# ============================================================================
print("--- Challenge Caso e probabilità: Il tavolo da gioco a oggetti ---")
class Dado:
    """Un dado del tavolo con i risultati dei lanci registrati."""

    def __init__(self, colore: str, lanci: list[int]) -> None:
        if len(lanci) == 0 or min(lanci) < 1 or max(lanci) > 6:
            raise ValueError(f"{colore}: lanci non validi")
        self.colore: str = colore
        self.lanci: list[int] = lanci

    def media(self) -> float:
        return sum(self.lanci) / len(self.lanci)

    def quota(self, faccia: int) -> float:
        return self.lanci.count(faccia) / len(self.lanci)

    def __str__(self) -> str:
        return (f"{self.colore}: media {self.media():.2f}, "
                f"quota di 6: {self.quota(6):.1%}")

    def __lt__(self, altro: "Dado") -> bool:
        return self.media() < altro.media()


class Tavolo:
    """Il tavolo da gioco: una lista di dadi."""

    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.dadi: list[Dado] = []

    def aggiungi(self, dado: Dado) -> None:
        self.dadi.append(dado)

    def cerca(self, colore: str) -> Dado | None:
        for d in self.dadi:
            if d.colore == colore:
                return d
        return None

    def media_generale(self) -> float:
        somma: int = sum([sum(d.lanci) for d in self.dadi])
        return somma / sum([len(d.lanci) for d in self.dadi])

tavolo: Tavolo = Tavolo("Tavolo 1")
for colore, lanci in [("rosso", [4, 6, 1, 6, 3, 6]),
                      ("blu", [2, 5, 3, 1, 4, 6]),
                      ("verde", [6, 2, 5, 3, 3, 1]),
                      ("bianco", [1, 4, 7, 2, 5, 3])]:
    try:
        tavolo.aggiungi(Dado(colore, lanci))
    except ValueError as e:
        print(e)

for d in sorted(tavolo.dadi, reverse=True):
    print(d)

print(tavolo.cerca("blu"))
print(tavolo.cerca("bianco"))
print(f"Media di tutti i lanci: {tavolo.media_generale():.2f}")
print()


# ============================================================================
print("=" * 60)
print("Fine degli esercizi del laboratorio 06")
print("=" * 60)
