# T02 — Logica booleana
# Demo interattiva per la lezione: due interruttori (A e B) a forma di LED,
# una porta logica e un LED di uscita. Ogni porta ha esempi presi dalla vita
# di tutti i giorni, così le tabelle di verità hanno un significato concreto.
#
# Avvio:  python3 demo/porte_logiche_led.py
#
# Comandi:
#   clic sui LED A e B (oppure tasti A e B)   accende / spegne l'ingresso
#   tasti 1-6 o clic sui pulsanti in alto     sceglie la porta
#   barra spaziatrice o "Altro esempio"       passa all'esempio successivo
#   tasto M                                   modalità astratta (A, B, 0/1)

import math
import tkinter as tk
from tkinter import font as tkfont

# =============================================================================
# Porte logiche ed esempi
# =============================================================================
# Ogni esempio ha: il significato di A, quello di B (None per NOT) e la frase
# che descrive l'uscita. "regola" è la frase completa mostrata sotto la porta.

PORTE: dict[str, dict] = {
    "AND": {
        "funzione": lambda a, b: a and b,
        "python": "A and B",
        "idea": "Vero solo se A e B sono entrambi veri",
        "esempi": [
            {"a": "Ho il biglietto", "b": "Ho un documento",
             "uscita": "Salgo sull'aereo",
             "regola": "Salgo sull'aereo SE ho il biglietto E ho un documento"},
            {"a": "Ho studiato", "b": "Sono presente all'appello",
             "uscita": "Supero l'esame",
             "regola": "Supero l'esame SE ho studiato E sono presente all'appello"},
            {"a": "In frigo ci sono le uova", "b": "In dispensa c'è la farina",
             "uscita": "Posso fare la pasta fresca",
             "regola": "Faccio la pasta fresca SE ho le uova E ho la farina"},
        ],
    },
    "OR": {
        "funzione": lambda a, b: a or b,
        "python": "A or B",
        "idea": "Vero se almeno uno tra A e B è vero",
        "esempi": [
            {"a": "Ho la carta", "b": "Ho i contanti",
             "uscita": "Posso pagare",
             "regola": "Posso pagare SE ho la carta O i contanti (anche entrambi)"},
            {"a": "È sabato", "b": "È domenica",
             "uscita": "È weekend",
             "regola": "È weekend SE è sabato O è domenica"},
            {"a": "Ho preso 18 allo scritto", "b": "Ho fatto il progetto",
             "uscita": "Posso iscrivermi all'orale",
             "regola": "Accedo all'orale SE ho passato lo scritto O ho fatto il progetto"},
        ],
    },
    "NOT": {
        "funzione": lambda a, b: not a,
        "python": "not A",
        "idea": "Inverte l'ingresso: vero diventa falso e viceversa",
        "esempi": [
            {"a": "Piove", "b": None,
             "uscita": "Esco senza ombrello",
             "regola": "Esco senza ombrello SE NON piove"},
            {"a": "Il negozio è chiuso", "b": None,
             "uscita": "Posso entrare a fare la spesa",
             "regola": "Posso entrare SE il negozio NON è chiuso"},
            {"a": "La sveglia sta suonando", "b": None,
             "uscita": "Continuo a dormire",
             "regola": "Continuo a dormire SE la sveglia NON suona"},
        ],
    },
    "NAND": {
        "funzione": lambda a, b: not (a and b),
        "python": "not (A and B)",
        "idea": "Falso solo se A e B sono entrambi veri",
        "esempi": [
            {"a": "La lavatrice è accesa", "b": "Il forno è acceso",
             "uscita": "Il contatore regge",
             "regola": "Il contatore salta solo se lavatrice E forno sono accesi insieme"},
            {"a": "Ho bevuto alcolici", "b": "Mi metto alla guida",
             "uscita": "Viaggio in regola",
             "regola": "Sono in regola SE NON (ho bevuto E guido)"},
            {"a": "Il telefono è al 2%", "b": "Sto facendo una videochiamata",
             "uscita": "Il telefono resta acceso",
             "regola": "Il telefono si spegne solo se è scarico E sto in videochiamata"},
        ],
    },
    "NOR": {
        "funzione": lambda a, b: not (a or b),
        "python": "not (A or B)",
        "idea": "Vero solo se A e B sono entrambi falsi",
        "esempi": [
            {"a": "Squilla il telefono", "b": "Suona il campanello",
             "uscita": "Dormo tranquillo",
             "regola": "Dormo tranquillo SE NÉ squilla il telefono NÉ suona il campanello"},
            {"a": "Ho la febbre", "b": "Ho la tosse",
             "uscita": "Vado in palestra",
             "regola": "Vado in palestra SE NON ho NÉ febbre NÉ tosse"},
            {"a": "C'è un dato mancante", "b": "C'è un valore anomalo",
             "uscita": "La riga è pulita",
             "regola": "Una riga del dataset è pulita SE NON ha NÉ mancanti NÉ anomalie"},
        ],
    },
    "XOR": {
        "funzione": lambda a, b: a != b,
        "python": "A != B",
        "idea": "Vero se A e B sono diversi",
        "esempi": [
            {"a": "Interruttore in cima alle scale", "b": "Interruttore in fondo alle scale",
             "uscita": "La luce delle scale è accesa",
             "regola": "Ogni interruttore cambia lo stato della luce (deviatore)"},
            {"a": "Ordino il primo", "b": "Ordino il secondo",
             "uscita": "Il menù fisso è valido",
             "regola": "Menù fisso: O il primo O il secondo, ma non entrambi"},
            {"a": "Gioco in casa", "b": "Gioco in trasferta",
             "uscita": "La partita è in calendario",
             "regola": "Una partita si gioca O in casa O in trasferta, mai entrambe"},
        ],
    },
}
ORDINE: list[str] = ["AND", "OR", "NOT", "NAND", "NOR", "XOR"]

# =============================================================================
# Aspetto grafico
# =============================================================================

SFONDO = "#16181d"
PANNELLO = "#20232a"
BORDO = "#353a45"
TESTO = "#e8eaf0"
TESTO_DEBOLE = "#8b93a5"
FILO_SPENTO = "#4a505c"
INGRESSO_ON = "#ffb020"      # ambra
INGRESSO_ALONE = "#5a4010"
USCITA_ON = "#38e07b"        # verde
USCITA_ALONE = "#134a2b"
LED_SPENTO = "#2c3038"
VERO_COL = "#38e07b"
FALSO_COL = "#ff6b6b"
EVIDENZIA = "#2f4a7a"
PORTA_FILL = "#2a2e37"
PORTA_LINEA = "#c9cfdb"

LARGH, ALT = 1040, 440       # dimensioni della tela con il circuito


def scegli_font(root: tk.Tk) -> str:
    """Usa Inter se installato, altrimenti il font di sistema."""
    disponibili = set(tkfont.families(root))
    for nome in ("Inter", "SF Pro Text", "Helvetica Neue", "Helvetica", "Arial"):
        if nome in disponibili:
            return nome
    return "TkDefaultFont"


def bezier(p0, p1, p2, n=24):
    """Punti di una curva di Bézier quadratica (serve per disegnare le porte)."""
    punti = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        punti.append((x, y))
    return punti


class DemoPorte:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.f = scegli_font(root)
        self.a = False
        self.b = False
        self.porta = "AND"
        self.indice_esempio = {nome: 0 for nome in ORDINE}
        self.astratto = False

        root.title("Porte logiche — T02")
        root.configure(bg=SFONDO)
        root.resizable(False, False)

        self._crea_barra()
        self.tela = tk.Canvas(root, width=LARGH, height=ALT, bg=SFONDO,
                              highlightthickness=0)
        self.tela.pack(padx=20)
        self._crea_parte_bassa()

        root.bind("<KeyPress-a>", lambda e: self.commuta("a"))
        root.bind("<KeyPress-b>", lambda e: self.commuta("b"))
        root.bind("<space>", lambda e: self.prossimo_esempio())
        root.bind("<KeyPress-m>", lambda e: self.commuta_astratto())
        for i, nome in enumerate(ORDINE, start=1):
            root.bind(str(i), lambda e, n=nome: self.scegli_porta(n))

        self.disegna()

    # ------------------------------------------------------------------ UI
    def _bottone(self, genitore, testo, comando, larghezza=None):
        etichetta = tk.Label(genitore, text=testo, bg=PANNELLO, fg=TESTO,
                             font=(self.f, 15, "bold"), padx=16, pady=8,
                             cursor="hand2", highlightthickness=1,
                             highlightbackground=BORDO, width=larghezza)
        etichetta.bind("<Button-1>", lambda e: comando())
        return etichetta

    def _crea_barra(self) -> None:
        barra = tk.Frame(self.root, bg=SFONDO)
        barra.pack(fill="x", padx=20, pady=(18, 6))
        self.bottoni_porta: dict[str, tk.Label] = {}
        for nome in ORDINE:
            b = self._bottone(barra, nome, lambda n=nome: self.scegli_porta(n), 6)
            b.pack(side="left", padx=(0, 8))
            self.bottoni_porta[nome] = b

        self.bottone_astratto = self._bottone(barra, "Modo 0/1", self.commuta_astratto)
        self.bottone_astratto.pack(side="right")
        self._bottone(barra, "Altro esempio ↻", self.prossimo_esempio).pack(
            side="right", padx=8)

    def _crea_parte_bassa(self) -> None:
        basso = tk.Frame(self.root, bg=SFONDO)
        basso.pack(fill="x", padx=20, pady=(4, 20))

        # Tabella di verità della porta scelta
        sx = tk.Frame(basso, bg=PANNELLO, highlightthickness=1,
                      highlightbackground=BORDO)
        sx.pack(side="left", fill="both", expand=True, padx=(0, 10))
        self.titolo_tabella = tk.Label(sx, bg=PANNELLO, fg=TESTO_DEBOLE,
                                       font=(self.f, 13, "bold"), anchor="w")
        self.titolo_tabella.pack(fill="x", padx=14, pady=(10, 4))
        self.tabella = tk.Frame(sx, bg=PANNELLO)
        self.tabella.pack(padx=14, pady=(0, 12), anchor="w")

        # Tutte le porte con gli stessi ingressi
        dx = tk.Frame(basso, bg=PANNELLO, highlightthickness=1,
                      highlightbackground=BORDO)
        dx.pack(side="left", fill="both", expand=True)
        tk.Label(dx, text="Stessi ingressi, tutte le porte", bg=PANNELLO,
                 fg=TESTO_DEBOLE, font=(self.f, 13, "bold"), anchor="w").pack(
            fill="x", padx=14, pady=(10, 4))
        griglia = tk.Frame(dx, bg=PANNELLO)
        griglia.pack(padx=14, pady=(0, 12), anchor="w")
        self.mini_led: dict[str, tuple[tk.Canvas, tk.Label]] = {}
        for i, nome in enumerate(ORDINE):
            r, c = divmod(i, 3)
            cella = tk.Frame(griglia, bg=PANNELLO, cursor="hand2")
            cella.grid(row=r, column=c, padx=(0, 26), pady=4, sticky="w")
            led = tk.Canvas(cella, width=26, height=26, bg=PANNELLO,
                            highlightthickness=0)
            led.pack(side="left")
            et = tk.Label(cella, text=nome, bg=PANNELLO, fg=TESTO,
                          font=(self.f, 15, "bold"), width=5, anchor="w")
            et.pack(side="left", padx=(6, 0))
            for w in (cella, led, et):
                w.bind("<Button-1>", lambda e, n=nome: self.scegli_porta(n))
            self.mini_led[nome] = (led, et)

    # ------------------------------------------------------------- azioni
    def commuta(self, quale: str) -> None:
        if quale == "a":
            self.a = not self.a
        elif self.porta != "NOT":
            self.b = not self.b
        self.disegna()

    def scegli_porta(self, nome: str) -> None:
        self.porta = nome
        self.disegna()

    def prossimo_esempio(self) -> None:
        n = len(PORTE[self.porta]["esempi"])
        self.indice_esempio[self.porta] = (self.indice_esempio[self.porta] + 1) % n
        if self.astratto:
            self.commuta_astratto()
        else:
            self.disegna()

    def commuta_astratto(self) -> None:
        self.astratto = not self.astratto
        self.bottone_astratto.config(
            text="Modo esempi" if self.astratto else "Modo 0/1")
        self.disegna()

    # ------------------------------------------------------------ disegno
    def uscita(self, nome: str | None = None) -> bool:
        nome = nome or self.porta
        return bool(PORTE[nome]["funzione"](self.a, self.b))

    def valore(self, v: bool) -> str:
        if self.astratto:
            return "1" if v else "0"
        return "VERO" if v else "FALSO"

    def disegna(self) -> None:
        for nome, b in self.bottoni_porta.items():
            attivo = nome == self.porta
            b.config(bg=EVIDENZIA if attivo else PANNELLO,
                     highlightbackground="#5b82c9" if attivo else BORDO)

        t = self.tela
        t.delete("all")
        porta = PORTE[self.porta]
        esempio = porta["esempi"][self.indice_esempio[self.porta]]
        solo_a = self.porta == "NOT"
        out = self.uscita()

        # posizioni
        led_x = 130
        ya, yb = (210, 210) if solo_a else (130, 300)
        gx, gy = 520, 215          # centro porta
        gw, gh = 150, 120
        x0 = gx - gw / 2
        out_x = 880

        # fili d'ingresso
        def filo(x1, y1, x2, y2, acceso, colore):
            t.create_line(x1, y1, x2, y2, fill=colore if acceso else FILO_SPENTO,
                          width=6 if acceso else 4, capstyle="round")

        ingresso_ya, ingresso_yb = (gy, gy) if solo_a else (gy - 32, gy + 32)
        gomito = 330
        filo(led_x + 40, ya, gomito, ya, self.a, INGRESSO_ON)
        filo(gomito, ya, gomito, ingresso_ya, self.a, INGRESSO_ON)
        filo(gomito, ingresso_ya, x0 + 20, ingresso_ya, self.a, INGRESSO_ON)
        if not solo_a:
            filo(led_x + 40, yb, gomito + 20, yb, self.b, INGRESSO_ON)
            filo(gomito + 20, yb, gomito + 20, ingresso_yb, self.b, INGRESSO_ON)
            filo(gomito + 20, ingresso_yb, x0 + 20, ingresso_yb, self.b, INGRESSO_ON)

        # filo d'uscita (parte dal centro della porta, coperto dal disegno)
        filo(gx, gy, out_x - 50, gy, out, USCITA_ON)

        self._disegna_porta(gx, gy, gw, gh)

        # nome della porta e idea
        t.create_text(gx, gy + gh / 2 + 34, text=self.porta, fill=TESTO,
                      font=(self.f, 26, "bold"))
        t.create_text(gx, gy + gh / 2 + 66, text=porta["idea"], fill=TESTO_DEBOLE,
                      font=(self.f, 14))

        # LED
        self._led(led_x, ya, 34, self.a, INGRESSO_ON, INGRESSO_ALONE, "a")
        if not solo_a:
            self._led(led_x, yb, 34, self.b, INGRESSO_ON, INGRESSO_ALONE, "b")
        self._led(out_x, gy, 46, out, USCITA_ON, USCITA_ALONE, None)

        # etichette
        if self.astratto:
            nome_a, nome_b, nome_out = "A", "B", porta["python"].replace(
                "and", "AND").replace("or", "OR").replace("not", "NOT")
            if self.porta in ("NAND", "NOR", "XOR"):
                nome_out = f"A {self.porta} B"
        else:
            nome_a, nome_b, nome_out = esempio["a"], esempio["b"], esempio["uscita"]

        self._etichetta_led(led_x, ya, 34, "A", nome_a, self.a)
        if not solo_a:
            self._etichetta_led(led_x, yb, 34, "B", nome_b, self.b)
        self._etichetta_led(out_x, gy, 46, "USCITA", nome_out, out)

        # regola in alto
        testo_regola = (f"In Python:  {porta['python']}" if self.astratto
                        else esempio["regola"])
        t.create_text(LARGH / 2, 34, text=testo_regola, fill=TESTO,
                      font=(self.f, 20, "bold"), width=LARGH - 60)
        if not self.astratto:
            n = len(porta["esempi"])
            t.create_text(LARGH / 2, 66,
                          text=f"esempio {self.indice_esempio[self.porta] + 1} di {n}"
                               "   ·   clic sui LED gialli per cambiare gli ingressi",
                          fill=TESTO_DEBOLE, font=(self.f, 12))

        self._aggiorna_tabella(esempio)
        self._aggiorna_mini_led()

    def _led(self, x, y, r, acceso, colore, alone, tag) -> None:
        t = self.tela
        if acceso:
            for i, k in enumerate((1.9, 1.55, 1.25)):
                t.create_oval(x - r * k, y - r * k, x + r * k, y + r * k,
                              fill=alone if i < 2 else self._mescola(alone, colore, 0.35),
                              outline="", tags=tag)
            t.create_oval(x - r, y - r, x + r, y + r, fill=colore,
                          outline="#ffffff", width=2, tags=tag)
            # riflesso
            t.create_oval(x - r * 0.55, y - r * 0.65, x - r * 0.05, y - r * 0.25,
                          fill="#ffffff", outline="", stipple="gray50", tags=tag)
        else:
            t.create_oval(x - r, y - r, x + r, y + r, fill=LED_SPENTO,
                          outline=BORDO, width=2, tags=tag)
            t.create_oval(x - r * 0.55, y - r * 0.65, x - r * 0.05, y - r * 0.25,
                          fill="#3a3f4a", outline="", tags=tag)
        if tag:
            t.tag_bind(tag, "<Button-1>", lambda e, q=tag: self.commuta(q))
            t.tag_bind(tag, "<Enter>", lambda e: t.config(cursor="hand2"))
            t.tag_bind(tag, "<Leave>", lambda e: t.config(cursor=""))

    def _etichetta_led(self, x, y, r, sigla, testo, valore) -> None:
        t = self.tela
        t.create_text(x, y - r - 20 - (6 if valore else 0), text=sigla,
                      fill=TESTO_DEBOLE, font=(self.f, 12, "bold"))
        t.create_text(x, y + r + 34, text=testo, fill=TESTO,
                      font=(self.f, 15, "bold"), width=210, anchor="n")
        t.create_text(x, y + r + 16, text=self.valore(valore),
                      fill=VERO_COL if valore else FALSO_COL,
                      font=(self.f, 13, "bold"))

    @staticmethod
    def _mescola(c1: str, c2: str, k: float) -> str:
        a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
        b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
        return "#" + "".join(f"{int(x + (y - x) * k):02x}" for x, y in zip(a, b))

    def _disegna_porta(self, gx, gy, w, h) -> None:
        """Simboli ANSI: AND a D, OR a punta, NOT a triangolo, pallino = negazione."""
        t = self.tela
        x0, top, bot = gx - w / 2, gy - h / 2, gy + h / 2
        tipo = self.porta
        stile = dict(fill=PORTA_FILL, outline=PORTA_LINEA, width=3)
        bolla = tipo in ("NOT", "NAND", "NOR")
        r_bolla = 10

        if tipo in ("AND", "NAND"):
            xm = x0 + w - h / 2 - (r_bolla if bolla else 0)
            punti = [(x0, top), (xm, top)]
            for i in range(31):
                ang = -math.pi / 2 + math.pi * i / 30
                punti.append((xm + h / 2 * math.cos(ang), gy + h / 2 * math.sin(ang)))
            punti += [(x0, bot)]
            punta = xm + h / 2
        elif tipo in ("OR", "NOR", "XOR"):
            punta = x0 + w - (2 * r_bolla if bolla else 0)
            punti = bezier((x0, top), (x0 + w * 0.55, top), (punta, gy))
            punti += bezier((punta, gy), (x0 + w * 0.55, bot), (x0, bot))[1:]
            punti += bezier((x0, bot), (x0 + 34, gy), (x0, top))[1:]
            if tipo == "XOR":
                arco = bezier((x0 - 14, bot), (x0 + 20, gy), (x0 - 14, top))
                t.create_line(*[c for p in arco for c in p], fill=PORTA_LINEA,
                              width=3, smooth=True)
        else:  # NOT
            punta = x0 + w - 2 * r_bolla
            punti = [(x0, top + 8), (punta, gy), (x0, bot - 8)]

        t.create_polygon(*[c for p in punti for c in p], **stile)
        if bolla:
            t.create_oval(punta, gy - r_bolla, punta + 2 * r_bolla, gy + r_bolla,
                          **stile)

    def _aggiorna_tabella(self, esempio) -> None:
        for w in self.tabella.winfo_children():
            w.destroy()
        solo_a = self.porta == "NOT"
        self.titolo_tabella.config(text=f"Tabella di verità — {self.porta}")

        intest = ["A"] if solo_a else ["A", "B"]
        intest.append(self.porta if self.porta == "NOT" else f"A {self.porta} B")
        if not self.astratto:
            intest[-1] = esempio["uscita"]
        for c, testo in enumerate(intest):
            tk.Label(self.tabella, text=testo, bg=PANNELLO, fg=TESTO_DEBOLE,
                     font=(self.f, 13, "bold"), padx=12, pady=2,
                     wraplength=200).grid(row=0, column=c, sticky="w")

        righe = [(False, False), (True, False)] if solo_a else [
            (False, False), (False, True), (True, False), (True, True)]
        for r, (a, b) in enumerate(righe, start=1):
            corrente = a == self.a and (solo_a or b == self.b)
            sfondo = EVIDENZIA if corrente else PANNELLO
            valori = [a] if solo_a else [a, b]
            valori.append(bool(PORTE[self.porta]["funzione"](a, b)))
            for c, v in enumerate(valori):
                ultimo = c == len(valori) - 1
                tk.Label(self.tabella, text=self.valore(v), bg=sfondo,
                         fg=(VERO_COL if v else FALSO_COL) if ultimo else TESTO,
                         font=(self.f, 15, "bold" if ultimo else "normal"),
                         padx=12, pady=3, anchor="w").grid(
                    row=r, column=c, sticky="we")

    def _aggiorna_mini_led(self) -> None:
        for nome, (led, et) in self.mini_led.items():
            v = self.uscita(nome)
            led.delete("all")
            if v:
                led.create_oval(1, 1, 25, 25, fill=USCITA_ALONE, outline="")
                led.create_oval(5, 5, 21, 21, fill=USCITA_ON, outline="#ffffff")
            else:
                led.create_oval(5, 5, 21, 21, fill=LED_SPENTO, outline=BORDO,
                                width=2)
            et.config(fg=TESTO if nome == self.porta else TESTO_DEBOLE)


if __name__ == "__main__":
    finestra = tk.Tk()
    DemoPorte(finestra)
    finestra.mainloop()
