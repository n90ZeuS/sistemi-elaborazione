# T09 — Cicli
# Demo visiva per la lezione: i pattern comuni con i cicli (accumulatore,
# contatore, ricerca, filtro, min/max) eseguiti passo passo, a mano.
# Si vedono il percorso nel diagramma di flusso (blocco corrente e freccia
# appena percorsa evidenziati), la riga corrispondente del pseudocodice o del
# codice Python, la lista con l'elemento in esame, le variabili e l'uscita.
# I diagrammi delle slide sono generati da questi stessi dati.
#
# Avvio:  python3 demo/pattern_cicli.py
#
# Comandi:
#   Avanti, spazio, →, ↓, clic         passo successivo
#   ◀, ←, ↑                            passo precedente
#   PagGiù / PagSu (telecomando)       avanti / indietro
#   Da capo                            riparte da Inizio
#   1 … 5 o pulsanti in alto           sceglie il pattern
#   Pseudocodice / Python, tasto P     cambia il codice mostrato a destra
#   caselle dei dati + Invio           cambia la lista (e l'obiettivo della ricerca)

from __future__ import annotations

import re
import tkinter as tk
from dataclasses import dataclass, field
from tkinter import font as tkfont

# =============================================================================
# Colori (gli stessi delle slide)
# =============================================================================

SFONDO = "#f8fafc"
TESTO = "#1e293b"
TESTO_TENUE = "#64748b"
LINEA = "#334155"
ACCENTO = "#2563eb"
SPENTO = "#cbd5e1"

COLORI = {
    "terminale": ("#e2e8f0", "#334155"),
    "processo": ("#ede9fe", "#5b21b6"),
    "io": ("#dbeafe", "#1e40af"),
    "decisione": ("#fef3c7", "#92400e"),
    "si": ("#dcfce7", "#166534"),
    "no": ("#fee2e2", "#991b1b"),
}

SOGLIA = 18     # sufficienza, come nel codice delle slide

# =============================================================================
# Diagrammi di flusso: coordinate in un riquadro 720 x 520
# =============================================================================

LARGHEZZA, ALTEZZA = 720, 520


@dataclass
class Nodo:
    id: str
    tipo: str                 # terminale, processo, io, decisione
    x: float                  # centro
    y: float
    w: float
    h: float
    righe: list[str]
    colore: str | None = None  # "si" / "no" per le uscite colorate


@dataclass
class Arco:
    id: str
    punti: list[tuple[float, float]]
    punta: bool = True


@dataclass
class Etichetta:
    testo: str                # "sì", "no" o "break"
    x: float
    y: float
    arco: str


@dataclass
class Diagramma:
    nodi: list[Nodo]
    archi: list[Arco]
    etichette: list[Etichetta]
    giunzioni: list[tuple[float, float]] = field(default_factory=list)


def _inizio_fine() -> list[Nodo]:
    return [Nodo("inizio", "terminale", 260, 32, 160, 48, ["Inizio"]),
            Nodo("fine", "terminale", 560, 470, 160, 48, ["Fine"])]


def _diagramma_con_condizione(init: str, w_init: float, ciclo: list[str], cond: list[str],
                              azione: str, w_azione: float, uscita: str) -> Diagramma:
    """Schema comune a contatore, filtro e min/max: un SE dentro il ciclo."""
    return Diagramma(
        nodi=_inizio_fine() + [
            Nodo("init", "processo", 260, 112, w_init, 50, [init]),
            Nodo("ciclo", "decisione", 260, 220, 250, 104, ciclo),
            Nodo("cond", "decisione", 260, 350, 230, 96, cond),
            Nodo("azione", "processo", 260, 452, w_azione, 48, [azione]),
            Nodo("output", "io", 560, 350, 250, 52, [uscita]),
        ],
        archi=[
            Arco("e_inizio", [(260, 56), (260, 87)]),
            Arco("e_init", [(260, 137), (260, 168)]),
            Arco("e_si", [(260, 272), (260, 302)]),
            Arco("e_cond_si", [(260, 398), (260, 428)]),
            Arco("e_cond_no", [(145, 350), (50, 350)], punta=False),
            Arco("e_ritorno", [(260, 476), (260, 500), (50, 500)], punta=False),
            Arco("e_su_basso", [(50, 500), (50, 350)], punta=False),
            Arco("e_su", [(50, 350), (50, 220), (133, 220)]),
            Arco("e_esci", [(385, 220), (560, 220), (560, 324)]),
            Arco("e_fine", [(560, 376), (560, 446)]),
        ],
        etichette=[Etichetta("sì", 275, 290, "e_si"), Etichetta("no", 400, 208, "e_esci"),
                   Etichetta("sì", 275, 416, "e_cond_si"), Etichetta("no", 95, 338, "e_cond_no")],
        giunzioni=[(50, 350)],
    )


DIAGRAMMI: dict[str, Diagramma] = {
    "accumulatore": Diagramma(
        nodi=_inizio_fine() + [
            Nodo("init", "processo", 260, 112, 240, 50, ["somma = 0"]),
            Nodo("ciclo", "decisione", 260, 220, 250, 104, ["c'è un altro", "voto?"]),
            Nodo("azione", "processo", 260, 345, 280, 50, ["somma = somma + voto"]),
            Nodo("dopo", "processo", 560, 300, 280, 50, ["media = somma / numero voti"]),
            Nodo("output", "io", 560, 385, 220, 52, ["Scrivi media"]),
        ],
        archi=[
            Arco("e_inizio", [(260, 56), (260, 87)]),
            Arco("e_init", [(260, 137), (260, 168)]),
            Arco("e_si", [(260, 272), (260, 320)]),
            Arco("e_ritorno", [(260, 370), (260, 400), (50, 400)], punta=False),
            Arco("e_su", [(50, 400), (50, 220), (133, 220)]),
            Arco("e_esci", [(385, 220), (560, 220), (560, 275)]),
            Arco("e_dopo", [(560, 325), (560, 359)]),
            Arco("e_fine", [(560, 411), (560, 446)]),
        ],
        etichette=[Etichetta("sì", 275, 300, "e_si"), Etichetta("no", 400, 208, "e_esci")],
    ),
    "contatore": _diagramma_con_condizione(
        "sufficienze = 0", 240, ["c'è un altro", "voto?"], [f"voto ≥ {SOGLIA}?"],
        "sufficienze = sufficienze + 1", 300, "Scrivi sufficienze"),
    "ricerca": Diagramma(
        nodi=[
            Nodo("inizio", "terminale", 260, 32, 160, 48, ["Inizio"]),
            Nodo("fine", "terminale", 560, 482, 160, 48, ["Fine"]),
            Nodo("init", "processo", 260, 112, 240, 50, ["trovato = False"]),
            Nodo("ciclo", "decisione", 260, 220, 250, 104, ["c'è un altro", "elemento?"]),
            Nodo("cond", "decisione", 260, 350, 250, 100, ["elemento ==", "obiettivo?"]),
            Nodo("azione", "processo", 260, 455, 220, 48, ["trovato = True"]),
            Nodo("output", "io", 560, 330, 230, 52, ["Scrivi trovato"]),
        ],
        archi=[
            Arco("e_inizio", [(260, 56), (260, 87)]),
            Arco("e_init", [(260, 137), (260, 168)]),
            Arco("e_si", [(260, 272), (260, 300)]),
            Arco("e_cond_si", [(260, 400), (260, 431)]),
            Arco("e_cond_no", [(135, 350), (50, 350), (50, 220), (133, 220)]),
            Arco("e_break", [(370, 455), (480, 455), (480, 358)]),
            Arco("e_esci", [(385, 220), (560, 220), (560, 304)]),
            Arco("e_fine", [(560, 356), (560, 458)]),
        ],
        etichette=[Etichetta("sì", 275, 290, "e_si"), Etichetta("no", 400, 208, "e_esci"),
                   Etichetta("sì", 275, 418, "e_cond_si"), Etichetta("no", 85, 338, "e_cond_no"),
                   Etichetta("break", 382, 441, "e_break")],
    ),
    "filtro": _diagramma_con_condizione(
        "sufficienti = lista vuota", 280, ["c'è un altro", "voto?"], [f"voto ≥ {SOGLIA}?"],
        "aggiungi voto a sufficienti", 300, "Scrivi sufficienti"),
    "minmax": _diagramma_con_condizione(
        "massimo = primo valore", 270, ["c'è un altro", "valore?"], ["valore >", "massimo?"],
        "massimo = valore", 240, "Scrivi massimo"),
}

# =============================================================================
# Codice di ogni pattern (lo stesso delle slide)
# =============================================================================

PSEUDOCODICE: dict[str, list[str]] = {
    "accumulatore": [
        "INIZIO",
        "    somma = 0",
        "    PER OGNI voto IN voti",
        "        somma = somma + voto",
        "    FINE PER",
        "    media = somma / numero voti",
        "    SCRIVI media",
        "FINE",
    ],
    "contatore": [
        "INIZIO",
        "    sufficienze = 0",
        "    PER OGNI voto IN voti",
        f"        SE voto ≥ {SOGLIA} ALLORA",
        "            sufficienze = sufficienze + 1",
        "        FINE SE",
        "    FINE PER",
        "    SCRIVI sufficienze",
        "FINE",
    ],
    "ricerca": [
        "INIZIO",
        "    trovato = False",
        "    PER OGNI elemento IN lista",
        "        SE elemento = obiettivo ALLORA",
        "            trovato = True",
        "            ESCI DAL CICLO",
        "        FINE SE",
        "    FINE PER",
        "    SCRIVI trovato",
        "FINE",
    ],
    "filtro": [
        "INIZIO",
        "    sufficienti = lista vuota",
        "    PER OGNI voto IN voti",
        f"        SE voto ≥ {SOGLIA} ALLORA",
        "            aggiungi voto a sufficienti",
        "        FINE SE",
        "    FINE PER",
        "    SCRIVI sufficienti",
        "FINE",
    ],
    "minmax": [
        "INIZIO",
        "    massimo = primo valore",
        "    PER OGNI valore DAL SECONDO IN POI",
        "        SE valore > massimo ALLORA",
        "            massimo = valore",
        "        FINE SE",
        "    FINE PER",
        "    SCRIVI massimo",
        "FINE",
    ],
}


def lista_python(valori: list[float]) -> str:
    return "[" + ", ".join(numero(v) for v in valori) + "]"


def codice_python(pattern: str, dati: list[float], obiettivo: float) -> list[str]:
    lista = lista_python(dati)
    if pattern == "accumulatore":
        return [
            f"voti: list[int] = {lista}",
            "",
            "somma: int = 0",
            "for voto in voti:",
            "    somma += voto",
            "",
            "media: float = somma / len(voti)",
            'print(f"Media: {media:.2f}")',
        ]
    if pattern == "contatore":
        return [
            f"voti: list[int] = {lista}",
            "",
            "sufficienze: int = 0",
            "for voto in voti:",
            f"    if voto >= {SOGLIA}:",
            "        sufficienze += 1",
            "",
            'print(f"Sufficienze: {sufficienze} su {len(voti)}")',
        ]
    if pattern == "ricerca":
        return [
            f"lista: list[int] = {lista}",
            f"obiettivo: int = {numero(obiettivo)}",
            "",
            "trovato: bool = False",
            "for elemento in lista:",
            "    if elemento == obiettivo:",
            "        trovato = True",
            "        break",
            "",
            'print(f"Trovato: {trovato}")',
        ]
    if pattern == "filtro":
        return [
            f"voti: list[int] = {lista}",
            "",
            "sufficienti: list[int] = []",
            "for voto in voti:",
            f"    if voto >= {SOGLIA}:",
            "        sufficienti.append(voto)",
            "",
            'print(f"Voti sufficienti: {sufficienti}")',
        ]
    return [
        f"valori: list[int] = {lista}",
        "",
        "massimo: int = valori[0]",
        "for valore in valori[1:]:",
        "    if valore > massimo:",
        "        massimo = valore",
        "",
        'print(f"Massimo: {massimo}")',
    ]


# =============================================================================
# Esecuzione passo passo
# =============================================================================

FINE_FOR = "il ciclo for è finito: si prosegue dopo il blocco rientrato"
FINE_FILE = "FINE: dopo l'ultima riga il programma termina"

# frecce percorse per tornare all'inizio del ciclo
DA_AZIONE = {"e_ritorno", "e_su_basso", "e_su"}
DA_COND_NO = {"e_cond_no", "e_su"}


@dataclass
class Passo:
    nodo: str
    archi: set[str]              # frecce appena percorse
    pseudo: int                  # riga del pseudocodice
    python: int | str            # riga Python, oppure spiegazione se non ce n'è una
    variabili: dict[str, str]
    corrente: int | None         # indice dell'elemento in esame
    segnati: frozenset[int]      # elementi contati / scelti / trovati
    uscita: list[str]
    nota: str = ""


class Traccia:
    """Raccoglie i passi mentre si simula il pattern."""

    def __init__(self) -> None:
        self.passi: list[Passo] = []
        self.variabili: dict[str, str] = {}
        self.segnati: set[int] = set()
        self.uscita: list[str] = []

    def __call__(self, nodo, archi, pseudo, python, corrente=None, nota="") -> None:
        self.passi.append(Passo(nodo, set(archi), pseudo, python, dict(self.variabili), corrente,
                                frozenset(self.segnati), list(self.uscita), nota))


def numero(x: float) -> str:
    """Numero come lo scriverebbe Python, senza ".0" inutile."""
    return str(int(x)) if x == int(x) else f"{x:g}"


def traccia(pattern: str, dati: list[float], obiettivo: float) -> list[Passo]:
    t = Traccia()
    v = t.variabili
    if pattern == "accumulatore":
        t("inizio", (), 0, 0)
        somma = 0.0
        v["somma"] = "0"
        t("init", {"e_inizio"}, 1, 2)
        arrivo = {"e_init"}
        for i, voto in enumerate(dati):
            v["voto"] = numero(voto)
            t("ciclo", arrivo, 2, 3, i, f"c'è un altro voto: voto = {numero(voto)}")
            nuova = somma + voto
            v["somma"] = numero(nuova)
            t("azione", {"e_si"}, 3, 4, i, f"somma = {numero(somma)} + {numero(voto)} = {numero(nuova)}")
            somma = nuova
            arrivo = {"e_ritorno", "e_su"}
        t("ciclo", arrivo, 4, FINE_FOR, None, "non ci sono altri voti: si esce dal ciclo")
        media = somma / len(dati)
        v["media"] = f"{media:g}"
        t("dopo", {"e_esci"}, 5, 6, None, f"media = {numero(somma)} / {len(dati)} = {media:g}")
        t.uscita.append(f"Media: {media:.2f}")
        t("output", {"e_dopo"}, 6, 7)
        t("fine", {"e_fine"}, 7, FINE_FILE)

    elif pattern in ("contatore", "filtro"):
        conta = pattern == "contatore"
        nome = "sufficienze" if conta else "sufficienti"
        scelti: list[float] = []
        t("inizio", (), 0, 0)
        v[nome] = "0" if conta else "[]"
        t("init", {"e_inizio"}, 1, 2)
        arrivo = {"e_init"}
        for i, voto in enumerate(dati):
            v["voto"] = numero(voto)
            t("ciclo", arrivo, 2, 3, i, f"c'è un altro voto: voto = {numero(voto)}")
            if voto >= SOGLIA:
                t("cond", {"e_si"}, 3, 4, i, f"{numero(voto)} ≥ {SOGLIA}? sì")
                scelti.append(voto)
                t.segnati.add(i)
                v[nome] = str(len(scelti)) if conta else lista_python(scelti)
                nota = f"{nome} = {len(scelti) - 1} + 1 = {len(scelti)}" if conta \
                    else f"{numero(voto)} aggiunto a sufficienti"
                t("azione", {"e_cond_si"}, 4, 5, i, nota)
                arrivo = DA_AZIONE
            else:
                t("cond", {"e_si"}, 3, 4, i, f"{numero(voto)} ≥ {SOGLIA}? no: si torna al ciclo")
                arrivo = DA_COND_NO
        t("ciclo", arrivo, 6, FINE_FOR, None, "non ci sono altri voti: si esce dal ciclo")
        if conta:
            t.uscita.append(f"Sufficienze: {len(scelti)} su {len(dati)}")
        else:
            t.uscita.append(f"Voti sufficienti: {lista_python(scelti)}")
        t("output", {"e_esci"}, 7, 7)
        t("fine", {"e_fine"}, 8, FINE_FILE)

    elif pattern == "ricerca":
        t("inizio", (), 0, 0)
        v["obiettivo"] = numero(obiettivo)
        v["trovato"] = "False"
        t("init", {"e_inizio"}, 1, 3)
        arrivo = {"e_init"}
        for i, elemento in enumerate(dati):
            v["elemento"] = numero(elemento)
            t("ciclo", arrivo, 2, 4, i, f"c'è un altro elemento: elemento = {numero(elemento)}")
            if elemento == obiettivo:
                t("cond", {"e_si"}, 3, 5, i, f"{numero(elemento)} == {numero(obiettivo)}? sì")
                t.segnati.add(i)
                v["trovato"] = "True"
                t("azione", {"e_cond_si"}, 4, 6, i, "trovato!")
                t("azione", set(), 5, 7, i, "break: si esce subito dal ciclo, gli altri elementi non si guardano")
                arrivo = {"e_break"}
                break
            t("cond", {"e_si"}, 3, 5, i, f"{numero(elemento)} == {numero(obiettivo)}? no: si torna al ciclo")
            arrivo = {"e_cond_no"}
        else:
            t("ciclo", arrivo, 7, FINE_FOR, None, "elementi finiti senza trovare l'obiettivo")
            arrivo = {"e_esci"}
        t.uscita.append(f"Trovato: {v['trovato']}")
        t("output", arrivo, 8, 9)
        t("fine", {"e_fine"}, 9, FINE_FILE)

    else:  # minmax
        t("inizio", (), 0, 0)
        massimo = dati[0]
        v["massimo"] = numero(massimo)
        t.segnati = {0}
        t("init", {"e_inizio"}, 1, 2, 0, f"massimo = primo valore = {numero(massimo)}")
        arrivo = {"e_init"}
        for i in range(1, len(dati)):
            valore = dati[i]
            v["valore"] = numero(valore)
            t("ciclo", arrivo, 2, 3, i, f"c'è un altro valore: valore = {numero(valore)}")
            if valore > massimo:
                t("cond", {"e_si"}, 3, 4, i, f"{numero(valore)} > {numero(massimo)}? sì")
                massimo = valore
                v["massimo"] = numero(massimo)
                t.segnati = {i}
                t("azione", {"e_cond_si"}, 4, 5, i, f"nuovo massimo: {numero(massimo)}")
                arrivo = DA_AZIONE
            else:
                t("cond", {"e_si"}, 3, 4, i, f"{numero(valore)} > {numero(massimo)}? no: si torna al ciclo")
                arrivo = DA_COND_NO
        t("ciclo", arrivo, 6, FINE_FOR, None, "non ci sono altri valori: si esce dal ciclo")
        t.uscita.append(f"Massimo: {numero(massimo)}")
        t("output", {"e_esci"}, 7, 7)
        t("fine", {"e_fine"}, 8, FINE_FILE)
    return t.passi


# =============================================================================
# Interfaccia
# =============================================================================

PATTERN = [
    # chiave, nome, nome della lista, dati iniziali, obiettivo (solo ricerca)
    ("accumulatore", "Accumulatore", "voti", [28, 30, 25, 27, 22]),
    ("contatore", "Contatore", "voti", [28, 30, 25, 27, 22, 15, 12]),
    ("ricerca", "Ricerca", "lista", [28, 30, 25, 27, 22]),
    ("filtro", "Filtro", "voti", [28, 30, 25, 27, 22, 15, 12]),
    ("minmax", "Min/Max", "valori", [4, 9, 2, 11, 7]),
]


def leggi_lista(testo: str) -> list[float] | None:
    parti = [p for p in re.split(r"[,;\s\[\]]+", testo) if p]
    try:
        return [float(p) for p in parti] or None
    except ValueError:
        return None


class Demo:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("Pattern comuni con i cicli")
        root.configure(bg=SFONDO)
        root.geometry("1400x840")

        self.f_titolo = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self.f_testo = tkfont.Font(family="Helvetica", size=17)
        self.f_pulsante = tkfont.Font(family="Helvetica", size=17, weight="bold")
        self.f_blocco = tkfont.Font(family="Helvetica", size=16)
        self.f_blocco_b = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self.f_titoletto = tkfont.Font(family="Helvetica", size=17, weight="bold")
        self.f_var = tkfont.Font(family="Menlo", size=20, weight="bold")
        self.f_cella = tkfont.Font(family="Menlo", size=19, weight="bold")
        self.f_mono = tkfont.Font(family="Menlo", size=15)
        self.f_mono_b = tkfont.Font(family="Menlo", size=15, weight="bold")
        self.f_term = tkfont.Font(family="Menlo", size=19, weight="bold")

        self.pattern = "accumulatore"
        self.dati = {chiave: list(d) for chiave, _, _, d in PATTERN}
        self.obiettivo = 25.0
        self.modo = "pseudo"
        self.passi: list[Passo] = []
        self.indice = 0
        self.errore = ""

        self._costruisci_comandi()
        self.canvas = tk.Canvas(root, bg=SFONDO, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda e: self._ridisegna())
        self.canvas.bind("<Button-1>", lambda e: (self.canvas.focus_set(), self.avanti()))

        for tasto in ("<Return>", "<KP_Enter>"):
            root.bind(tasto, lambda e: self.applica_dati() if self._in_casella() else self.avanti())
        root.bind("<Next>", lambda e: self.avanti())
        root.bind("<Prior>", lambda e: self.indietro())
        for tasto in ("<space>", "<Right>", "<Down>"):
            root.bind(tasto, lambda e: self._da_tasto(self.avanti))
        for tasto in ("<Left>", "<Up>"):
            root.bind(tasto, lambda e: self._da_tasto(self.indietro))
        for tasto in ("<Key-p>", "<Key-P>"):
            root.bind(tasto, lambda e: self._da_tasto(self.cambia_modo))
        for n, (chiave, *_resto) in enumerate(PATTERN, start=1):
            root.bind(f"<Key-{n}>", lambda e, k=chiave: self._da_tasto(lambda: self.scegli(k)))

    # -------------------------------------------------------------------------
    # Comandi in alto
    # -------------------------------------------------------------------------

    def _costruisci_comandi(self) -> None:
        riga1 = tk.Frame(self.root, bg=SFONDO, pady=10)
        riga1.pack(fill="x")
        tk.Label(riga1, text="Pattern", font=self.f_titolo, fg=ACCENTO, bg=SFONDO).pack(side="left", padx=(28, 16))
        scelta = tk.Frame(riga1, bg="#e2e8f0", padx=3, pady=3)
        scelta.pack(side="left")
        self.pulsanti_pattern = {}
        for chiave, nome, *_resto in PATTERN:
            p = self._pulsante(scelta, nome, lambda k=chiave: self.scegli(k), "#e2e8f0", TESTO)
            p.pack(side="left")
            self.pulsanti_pattern[chiave] = p

        selettore = tk.Frame(riga1, bg="#e2e8f0", padx=3, pady=3)
        selettore.pack(side="right", padx=28)
        self.pulsanti_modo = {}
        for modo, testo in (("pseudo", "Pseudocodice"), ("python", "Python")):
            p = self._pulsante(selettore, testo, lambda m=modo: self.cambia_modo(m), "#e2e8f0", TESTO)
            p.pack(side="left")
            self.pulsanti_modo[modo] = p

        riga2 = tk.Frame(self.root, bg=SFONDO, pady=4)
        riga2.pack(fill="x")
        self._pulsante(riga2, "◀", self.indietro, "#e2e8f0", TESTO).pack(side="left", padx=(28, 4))
        self._pulsante(riga2, "Avanti ▶", self.avanti, ACCENTO, "white").pack(side="left", padx=4)
        self._pulsante(riga2, "Da capo", self.da_capo, "#e2e8f0", TESTO).pack(side="left", padx=(16, 4))
        self.contatore = tk.Label(riga2, text="", font=self.f_testo, fg=TESTO_TENUE, bg=SFONDO, width=18, anchor="w")
        self.contatore.pack(side="left", padx=(20, 0))

        # dati modificabili: la lista e, per la ricerca, l'obiettivo
        self.var_obiettivo = tk.StringVar()
        self.casella_obiettivo = tk.Entry(riga2, textvariable=self.var_obiettivo, width=5, font=self.f_mono_b,
                                          relief="flat", bd=6, bg="white", fg=TESTO)
        self.etichetta_obiettivo = tk.Label(riga2, text="obiettivo", font=self.f_testo, fg=TESTO_TENUE, bg=SFONDO)
        self.var_lista = tk.StringVar()
        self.casella_lista = tk.Entry(riga2, textvariable=self.var_lista, width=28, font=self.f_mono_b,
                                      relief="flat", bd=6, bg="white", fg=TESTO)
        self.etichetta_lista = tk.Label(riga2, text="voti", font=self.f_testo, fg=TESTO_TENUE, bg=SFONDO)
        self._pulsante(riga2, "Usa questi dati", self.applica_dati, "#e2e8f0", TESTO).pack(side="right", padx=(8, 28))

    def _pulsante(self, padre, testo, comando, sfondo, colore) -> tk.Label:
        # Label al posto di Button: su macOS i Button ignorano il colore di sfondo
        p = tk.Label(padre, text=testo, font=self.f_pulsante, bg=sfondo, fg=colore,
                     padx=14, pady=6, cursor="hand2")
        p.bind("<Button-1>", lambda e: comando())
        return p

    def _aggiorna_comandi(self) -> None:
        for chiave, p in self.pulsanti_pattern.items():
            p.configure(bg=ACCENTO if chiave == self.pattern else "#e2e8f0",
                        fg="white" if chiave == self.pattern else TESTO)
        for modo, p in self.pulsanti_modo.items():
            p.configure(bg=ACCENTO if modo == self.modo else "#e2e8f0",
                        fg="white" if modo == self.modo else TESTO)
        nome_lista = next(n for k, _, n, _ in PATTERN if k == self.pattern)
        self.etichetta_lista.configure(text=nome_lista)
        self.var_lista.set(", ".join(numero(x) for x in self.dati[self.pattern]))
        self.var_obiettivo.set(numero(self.obiettivo))
        for w in (self.casella_obiettivo, self.etichetta_obiettivo, self.casella_lista, self.etichetta_lista):
            w.pack_forget()
        if self.pattern == "ricerca":
            self.casella_obiettivo.pack(side="right", padx=(6, 0))
            self.etichetta_obiettivo.pack(side="right", padx=(18, 0))
        self.casella_lista.pack(side="right", padx=(6, 0))
        self.etichetta_lista.pack(side="right")

    def _in_casella(self) -> bool:
        return isinstance(self.root.focus_get(), tk.Entry)

    def _da_tasto(self, azione) -> None:
        # dentro le caselle spazio, frecce e numeri servono per scrivere
        if not self._in_casella():
            azione()

    def scegli(self, pattern: str) -> None:
        self.pattern = pattern
        self.errore = ""
        self._aggiorna_comandi()
        self.da_capo()

    def cambia_modo(self, modo: str | None = None) -> None:
        self.modo = modo or ("python" if self.modo == "pseudo" else "pseudo")
        self._aggiorna_comandi()
        self._ridisegna()

    def applica_dati(self) -> None:
        valori = leggi_lista(self.var_lista.get())
        obiettivo = leggi_lista(self.var_obiettivo.get()) if self.pattern == "ricerca" else [self.obiettivo]
        if valori is None or obiettivo is None or len(obiettivo) != 1:
            self.errore = "Scrivi numeri separati da virgole (decimali con il punto: 2.5)"
            self._ridisegna()
            return
        self.errore = ""
        self.dati[self.pattern] = valori[:10]
        self.obiettivo = obiettivo[0]
        self._aggiorna_comandi()
        self.da_capo()

    def da_capo(self) -> None:
        self.passi = traccia(self.pattern, self.dati[self.pattern], self.obiettivo)
        self._vai(0)

    def avanti(self) -> None:
        if self.indice + 1 < len(self.passi):
            self._vai(self.indice + 1)

    def indietro(self) -> None:
        if self.indice > 0:
            self._vai(self.indice - 1)

    def _vai(self, i: int) -> None:
        self.indice = i
        fine = "  (fine)" if i == len(self.passi) - 1 else ""
        self.contatore.configure(text=f"Passo {i + 1} di {len(self.passi)}{fine}")
        self.canvas.focus_set()
        self._ridisegna()

    # -------------------------------------------------------------------------
    # Disegno
    # -------------------------------------------------------------------------

    def _ridisegna(self) -> None:
        c = self.canvas
        c.delete("all")
        w, h = c.winfo_width(), c.winfo_height()
        if w < 50 or not self.passi:
            return
        larg_diag = int(w * 0.50)
        self._diagramma(16, 6, larg_diag, h - 12)
        x0 = larg_diag + 36
        lw = w - x0 - 28
        y_codice = 8
        fine_codice = self._codice(x0, y_codice, lw)
        y_term = h - 150
        self._dati(x0, fine_codice + 22, lw, y_term - fine_codice - 34)
        self._terminale(x0, y_term, lw, 142)

    def _diagramma(self, x0: int, y0: int, w: int, h: int) -> None:
        c = self.canvas
        diagramma = DIAGRAMMI[self.pattern]
        s = min(w / LARGHEZZA, h / ALTEZZA)
        ox = x0 + (w - LARGHEZZA * s) / 2
        oy = y0 + (h - ALTEZZA * s) / 2
        P = lambda x, y: (ox + x * s, oy + y * s)

        passo = self.passi[self.indice]
        visti_nodi = {p.nodo for p in self.passi[:self.indice + 1]}
        visti_archi = set().union(*(p.archi for p in self.passi[:self.indice + 1]))

        self.f_blocco.configure(size=max(10, round(15 * s)))
        self.f_blocco_b.configure(size=max(10, round(16 * s)))

        for arco in diagramma.archi:
            if arco.id in passo.archi:
                colore, spessore = ACCENTO, 5
            elif arco.id in visti_archi:
                colore, spessore = LINEA, 2.5
            else:
                colore, spessore = SPENTO, 2.5
            punti = [v for x, y in arco.punti for v in P(x, y)]
            c.create_line(*punti, fill=colore, width=spessore, arrow="last" if arco.punta else "none",
                          arrowshape=(12 * s + 2, 14 * s + 2, 5 * s + 1), joinstyle="miter")
        for x, y in diagramma.giunzioni:
            gx, gy = P(x, y)
            acceso = "e_su" in visti_archi
            c.create_oval(gx - 5, gy - 5, gx + 5, gy + 5, fill=LINEA if acceso else SPENTO, outline="")

        for e in diagramma.etichette:
            colore = {"sì": COLORI["si"][1], "no": COLORI["no"][1]}.get(e.testo, LINEA)
            acceso = e.arco in visti_archi
            c.create_text(*P(e.x, e.y), text=e.testo, anchor="w", font=self.f_blocco_b,
                          fill=colore if acceso else TESTO_TENUE)

        for n in diagramma.nodi:
            chiaro, scuro = COLORI[n.colore or n.tipo]
            if n.id == passo.nodo:
                fill, outline, spessore, col_testo = chiaro, ACCENTO, 5, TESTO
            elif n.id in visti_nodi:
                fill, outline, spessore, col_testo = chiaro, scuro, 2, TESTO
            else:
                fill, outline, spessore, col_testo = "#ffffff", SPENTO, 2, TESTO_TENUE
            sx, sy, dx, dy = n.x - n.w / 2, n.y - n.h / 2, n.x + n.w / 2, n.y + n.h / 2
            if n.tipo == "terminale":
                c.create_oval(*P(sx, sy), *P(dx, dy), fill=fill, outline=outline, width=spessore)
            elif n.tipo == "processo":
                c.create_rectangle(*P(sx, sy), *P(dx, dy), fill=fill, outline=outline, width=spessore)
            elif n.tipo == "io":
                k = 14
                c.create_polygon(*P(sx + k, sy), *P(dx + k, sy), *P(dx - k, dy), *P(sx - k, dy),
                                 fill=fill, outline=outline, width=spessore)
            else:
                c.create_polygon(*P(n.x, sy), *P(dx, n.y), *P(n.x, dy), *P(sx, n.y),
                                 fill=fill, outline=outline, width=spessore)
            passo_riga = 21
            for j, riga in enumerate(n.righe):
                yy = n.y + (j - (len(n.righe) - 1) / 2) * passo_riga
                c.create_text(*P(n.x, yy), text=riga, font=self.f_blocco_b if n.id == passo.nodo else self.f_blocco,
                              fill=col_testo)

    def _codice(self, x0: int, y0: int, w: int) -> int:
        """Pseudocodice o Python con la riga corrente evidenziata; restituisce dove finisce."""
        c = self.canvas
        passo = self.passi[self.indice]
        riga_h = 27
        top = y0 + 32
        pseudo = PSEUDOCODICE[self.pattern]
        python = codice_python(self.pattern, self.dati[self.pattern], self.obiettivo)
        n_righe = max(len(pseudo), len(python)) + 1.6   # spazio per la nota sotto il codice
        basso = top + riga_h * n_righe + 6
        # il riquadro ha sempre la stessa altezza, così il resto non si sposta
        c.create_rectangle(x0, top - 6, x0 + w, basso, fill="white", outline="#e2e8f0")
        if self.modo == "pseudo":
            titolo, righe, attiva, nota = "Pseudocodice", pseudo, passo.pseudo, None
        else:
            titolo, righe = "Python", python
            attiva = passo.python if isinstance(passo.python, int) else None
            nota = passo.python if isinstance(passo.python, str) else None
        c.create_text(x0, y0 + 4, text=titolo, anchor="nw", font=self.f_titoletto, fill=TESTO_TENUE)
        for i, riga in enumerate(righe):
            yy = top + i * riga_h
            on = i == attiva
            if on:
                c.create_rectangle(x0 + 2, yy, x0 + w - 2, yy + riga_h, fill="#dbeafe", outline="")
                c.create_rectangle(x0 + 2, yy, x0 + 8, yy + riga_h, fill=ACCENTO, outline="")
            c.create_text(x0 + 20, yy + riga_h // 2, text=riga, anchor="w",
                          font=self.f_mono_b if on else self.f_mono, fill=TESTO if on else TESTO_TENUE)
        if nota:
            yy = top + riga_h * (len(righe) + 0.3)
            c.create_rectangle(x0 + 2, yy, x0 + w - 2, yy + riga_h * 1.2, fill="#dbeafe", outline="")
            c.create_rectangle(x0 + 2, yy, x0 + 8, yy + riga_h * 1.2, fill=ACCENTO, outline="")
            c.create_text(x0 + 20, yy + riga_h * 0.6, text=nota, anchor="w", width=w - 30,
                          font=self.f_testo, fill=TESTO)
        return int(basso)

    def _dati(self, x0: int, y0: int, w: int, h: int) -> None:
        """La lista con l'elemento in esame e le variabili del programma."""
        c = self.canvas
        passo = self.passi[self.indice]
        nome_lista = next(n for k, _, n, _ in PATTERN if k == self.pattern)
        dati = self.dati[self.pattern]
        c.create_text(x0, y0, text="Dati e variabili", anchor="nw", font=self.f_titoletto, fill=TESTO_TENUE)

        # la lista, una cella per elemento
        y_celle = y0 + 36
        etichetta = f"{nome_lista} ="
        c.create_text(x0, y_celle + 26, text=etichetta, anchor="w", font=self.f_var, fill=TESTO)
        xs = x0 + self.f_var.measure(etichetta) + 16
        lc = min(76, (x0 + w - xs) / max(len(dati), 1) - 6)
        for i, val in enumerate(dati):
            xc = xs + i * (lc + 6)
            if i in passo.segnati:
                fill, bordo = COLORI["si"][0], COLORI["si"][1]
            else:
                fill, bordo = "white", SPENTO
            spessore = 2
            if i == passo.corrente:
                bordo, spessore = ACCENTO, 5
                if i not in passo.segnati:
                    fill = "#dbeafe"
            c.create_rectangle(xc, y_celle, xc + lc, y_celle + 52, fill=fill, outline=bordo, width=spessore)
            c.create_text(xc + lc / 2, y_celle + 26, text=numero(val), font=self.f_cella, fill=TESTO)
            c.create_text(xc + lc / 2, y_celle + 66, text=str(i), font=self.f_blocco, fill=TESTO_TENUE)

        # le variabili, nell'ordine in cui sono comparse
        yy = y_celle + 104
        xv = x0
        for nome, valore in passo.variabili.items():
            testo = f"{nome} = {valore}"
            lv = self.f_var.measure(testo) + 28
            if xv + lv > x0 + w and xv > x0:
                xv, yy = x0, yy + 50
            c.create_rectangle(xv, yy - 20, xv + lv, yy + 20, fill="#ede9fe", outline="")
            c.create_text(xv + 14, yy, text=testo, anchor="w", font=self.f_var, fill=COLORI["processo"][1])
            xv += lv + 12

        testo = self.errore or passo.nota
        if testo:
            colore = COLORI["no"][1] if self.errore else TESTO
            c.create_text(x0, yy + 44, text=testo, anchor="nw", width=w, font=self.f_testo, fill=colore)

    def _terminale(self, x0: int, y0: int, w: int, h: int) -> None:
        """Quello che vedrebbe chi usa il programma."""
        c = self.canvas
        passo = self.passi[self.indice]
        c.create_text(x0, y0, text="Terminale", anchor="nw", font=self.f_titoletto, fill=TESTO_TENUE)
        c.create_rectangle(x0, y0 + 30, x0 + w, y0 + h, fill="#1e293b", outline="")
        for i, riga in enumerate(passo.uscita):
            c.create_text(x0 + 20, y0 + 30 + 30 + i * 40, text=riga, anchor="w", width=w - 40,
                          font=self.f_term, fill="#4ade80")


if __name__ == "__main__":
    root = tk.Tk()
    app = Demo(root)
    root.after(300, lambda: app.scegli("accumulatore"))
    root.mainloop()
