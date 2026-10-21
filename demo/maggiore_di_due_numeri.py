# T06 — Dal problema al programma
# Demo visiva per la lezione: l'algoritmo "a è maggiore di b?" eseguito passo
# passo, a mano. Quando l'esecuzione arriva a LEGGI a (e poi a LEGGI b) il
# programma chiede il numero nel terminale, come farebbe input() in Python.
# Si vedono il percorso evidenziato nel diagramma di flusso, la riga
# corrispondente del pseudocodice, il confronto grafico e l'uscita.
#
# Avvio:  python3 demo/maggiore_di_due_numeri.py
#
# Comandi:
#   Avanti, spazio, →, ↓, clic         passo successivo
#   ◀, ←, ↑                            passo precedente
#   Invio                              conferma il numero / passo successivo
#   PagGiù / PagSu (telecomando)       avanti / indietro, anche durante l'input
#   Da capo                            riparte da Inizio e chiede di nuovo i numeri
#   Pseudocodice / Python, tasto P     cambia il codice mostrato a destra

import tkinter as tk
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
    "io": ("#dbeafe", "#1e40af"),
    "decisione": ("#fef3c7", "#92400e"),
    "si": ("#dcfce7", "#166534"),
    "no": ("#fee2e2", "#991b1b"),
}

PSEUDOCODICE = [
    "INIZIO",
    "    LEGGI a",
    "    LEGGI b",
    "    SE a > b ALLORA",
    '        SCRIVI "a è maggiore di b"',
    "    ALTRIMENTI",
    '        SCRIVI "a non è maggiore di b"',
    "    FINE SE",
    "FINE",
]

PYTHON = [
    'a = float(input("Primo numero: "))',
    'b = float(input("Secondo numero: "))',
    "",
    "if a > b:",
    '    print("a è maggiore di b")',
    "else:",
    '    print("a non è maggiore di b")',
]

# riga del pseudocodice -> riga Python corrispondente, oppure una spiegazione
# per le righe che in Python non hanno un equivalente
DA_PSEUDO_A_PYTHON: dict[int, int | str] = {
    0: "INIZIO: l'esecuzione parte dalla prima riga del file",
    1: 0,
    2: 1,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: "FINE SE: nessuna riga, il blocco finisce dove finisce il rientro",
    8: "FINE: dopo l'ultima riga il programma termina",
}



def formatta(x: float) -> str:
    """Numero senza ".0" inutile, con la virgola italiana."""
    if x == int(x):
        return str(int(x))
    return f"{x:g}".replace(".", ",")


def leggi_numero(testo: str) -> float | None:
    try:
        return float(testo.strip().replace(",", "."))
    except ValueError:
        return None


class Demo:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("a è maggiore di b?")
        root.configure(bg=SFONDO)
        root.geometry("1360x800")

        self.f_titolo = tkfont.Font(family="Helvetica", size=26, weight="bold")
        self.f_testo = tkfont.Font(family="Helvetica", size=17)
        self.f_blocco = tkfont.Font(family="Helvetica", size=16)
        self.f_blocco_b = tkfont.Font(family="Helvetica", size=18, weight="bold")
        self.f_numero = tkfont.Font(family="Helvetica", size=30, weight="bold")
        self.f_mono = tkfont.Font(family="Menlo", size=15)
        self.f_mono_b = tkfont.Font(family="Menlo", size=15, weight="bold")
        self.f_term = tkfont.Font(family="Menlo", size=19, weight="bold")

        # valori letti finora (None = non ancora letto)
        self.a: float | None = None
        self.b: float | None = None
        self.indice = 0
        self.passi: list = []
        self.attivi: set[str] = set()
        self.riga_attiva: int | None = None
        self.attesa: str | None = None     # "a" o "b" mentre si aspetta l'input
        self.modo = "pseudo"               # codice mostrato: "pseudo" o "python"
        self.errore = ""                   # messaggio se l'input non è un numero

        self._costruisci_comandi()
        self.canvas = tk.Canvas(root, bg=SFONDO, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda e: self._ridisegna())
        self.canvas.bind("<Button-1>", lambda e: (self.canvas.focus_set(), self.avanti()))

        # casella di input, mostrata nel terminale solo durante LEGGI
        self.var_input = tk.StringVar()
        self.casella = tk.Entry(self.canvas, textvariable=self.var_input, width=8, font=self.f_term,
                                relief="flat", bd=0, fg="#fde68a", bg="#334155",
                                insertbackground="#fde68a", insertwidth=3)

        # Invio e PagGiù/PagSu (telecomando) funzionano anche dentro la casella
        for tasto in ("<Return>", "<KP_Enter>", "<Next>"):
            root.bind(tasto, lambda e: self.avanti())
        root.bind("<Prior>", lambda e: self.indietro())
        for tasto in ("<space>", "<Right>", "<Down>"):
            root.bind(tasto, lambda e: self._da_tasto(self.avanti))
        for tasto in ("<Left>", "<Up>"):
            root.bind(tasto, lambda e: self._da_tasto(self.indietro))
        for tasto in ("<Key-p>", "<Key-P>"):
            root.bind(tasto, lambda e: self._da_tasto(self.cambia_modo))

    # -------------------------------------------------------------------------
    # Comandi in alto
    # -------------------------------------------------------------------------

    def _costruisci_comandi(self) -> None:
        barra = tk.Frame(self.root, bg=SFONDO, pady=14)
        barra.pack(fill="x")

        tk.Label(barra, text="a è maggiore di b?", font=self.f_titolo,
                 fg=ACCENTO, bg=SFONDO).pack(side="left", padx=(28, 40))

        self._pulsante(barra, "◀", self.indietro, "#e2e8f0", TESTO).pack(side="left", padx=4)
        self._pulsante(barra, "Avanti ▶", self.avanti, ACCENTO, "white").pack(side="left", padx=4)
        self._pulsante(barra, "Da capo", self.da_capo, "#e2e8f0", TESTO).pack(side="left", padx=(16, 4))

        # selettore Pseudocodice / Python
        selettore = tk.Frame(barra, bg="#e2e8f0", padx=3, pady=3)
        selettore.pack(side="right", padx=28)
        self.pulsanti_modo = {}
        for modo, testo in (("pseudo", "Pseudocodice"), ("python", "Python")):
            p = self._pulsante(selettore, testo, lambda m=modo: self.cambia_modo(m), "#e2e8f0", TESTO)
            p.pack(side="left")
            self.pulsanti_modo[modo] = p
        self._aggiorna_selettore()

        self.contatore = tk.Label(barra, text="", font=self.f_testo, fg=TESTO_TENUE, bg=SFONDO)
        self.contatore.pack(side="left", padx=(20, 0))

    def _pulsante(self, padre, testo, comando, sfondo, colore) -> tk.Label:
        # Label al posto di Button: su macOS i Button ignorano il colore di sfondo
        p = tk.Label(padre, text=testo, font=self.f_blocco_b, bg=sfondo, fg=colore,
                     padx=14, pady=6, cursor="hand2")
        p.bind("<Button-1>", lambda e: comando())
        return p

    def cambia_modo(self, modo: str | None = None) -> None:
        self.modo = modo or ("python" if self.modo == "pseudo" else "pseudo")
        self._aggiorna_selettore()
        self._ridisegna()

    def _aggiorna_selettore(self) -> None:
        for modo, p in self.pulsanti_modo.items():
            if modo == self.modo:
                p.configure(bg=ACCENTO, fg="white")
            else:
                p.configure(bg="#e2e8f0", fg=TESTO)

    def _da_tasto(self, azione) -> None:
        # dentro la casella spazio e frecce servono per scrivere
        if isinstance(self.root.focus_get(), tk.Entry):
            return
        azione()

    # -------------------------------------------------------------------------
    # Esecuzione passo passo
    # -------------------------------------------------------------------------

    def _costruisci_passi(self) -> None:
        """Passi: (blocchi accesi, riga del pseudocodice, input atteso).

        Finché a e b non sono letti non si sa quale ramo prenderà il programma,
        quindi la lista si allunga solo quando i due valori sono noti.
        """
        lettura = {"inizio", "f_lettura", "lettura"}
        decisione = lettura | {"f_decisione", "decisione"}
        self.passi = [
            ({"inizio"}, 0, None),
            (lettura, 1, "a"),
            (lettura, 2, "b"),
        ]
        if self.a is None or self.b is None:
            return
        self.passi.append((decisione, 3, None))
        if self.a > self.b:
            self.passi.append((decisione | {"f_si", "si"}, 4, None))
            ramo = "si"
        else:
            # con il "no" si passa prima da ALTRIMENTI, poi da SCRIVI
            self.passi.append((decisione | {"f_no"}, 5, None))
            self.passi.append((decisione | {"f_no", "no"}, 6, None))
            ramo = "no"
        finale = decisione | {f"f_{ramo}", ramo, f"f_{ramo}_fine"}
        self.passi.append((finale, 7, None))
        self.passi.append((finale | {"f_fine", "fine"}, 8, None))

    def da_capo(self) -> None:
        self.a = self.b = None
        self.var_input.set("")
        self.errore = ""
        self._vai(0)

    def avanti(self) -> None:
        if self.attesa:
            valore = leggi_numero(self.var_input.get())
            if valore is None:
                self.errore = "Scrivi un numero (es. 7 oppure 2,5) e premi Invio"
                self._ridisegna()
                self.casella.focus_set()
                return
            self.errore = ""
            vecchio = (self.a, self.b)
            setattr(self, self.attesa, valore)
            if (self.a, self.b) != vecchio:
                self._costruisci_passi()
        if self.indice + 1 < len(self.passi):
            self._vai(self.indice + 1)

    def indietro(self) -> None:
        if self.indice > 0:
            self.errore = ""
            self._vai(self.indice - 1)

    def _vai(self, i: int) -> None:
        self._costruisci_passi()
        self.indice = i
        self.attivi, self.riga_attiva, self.attesa = self.passi[i]
        if self.attesa:
            valore = getattr(self, self.attesa)
            self.var_input.set("" if valore is None else formatta(valore))
        fine = "  (fine)" if i == len(self.passi) - 1 and len(self.passi) > 3 else ""
        totale = len(self.passi) if len(self.passi) > 3 else "?"
        self.contatore.configure(text=f"Passo {i + 1} di {totale}{fine}")
        self._ridisegna()
        if self.attesa:
            self.casella.focus_set()
            self.casella.icursor("end")
        else:
            self.canvas.focus_set()

    # stato visibile, ricavato dal passo corrente ----------------------------

    def _letto(self, nome: str) -> float | None:
        """Il valore è mostrato solo dopo che il programma ha superato la sua riga LEGGI."""
        riga = 1 if nome == "a" else 2
        if self.riga_attiva is None or self.indice <= riga:
            return None
        return getattr(self, nome)

    def _esito(self) -> str | None:
        if self.riga_attiva in (4, 6) or (self.riga_attiva in (7, 8)):
            return "si" if self.a > self.b else "no"
        return None

    @property
    def etichetta_lettura(self) -> str:
        a, b = self._letto("a"), self._letto("b")
        if self.attesa == "a":
            return "Leggi a  …"
        if self.attesa == "b":
            return f"a = {formatta(a)}   Leggi b  …"
        if a is not None and b is not None:
            return f"a = {formatta(a)},  b = {formatta(b)}"
        return "Leggi a, b"

    @property
    def etichetta_decisione(self) -> str:
        if self.indice >= 3 and self.a is not None and self.b is not None:
            return f"{formatta(self.a)} > {formatta(self.b)} ?"
        return "a > b ?"

    # -------------------------------------------------------------------------
    # Disegno
    # -------------------------------------------------------------------------

    def _ridisegna(self) -> None:
        c = self.canvas
        c.delete("all")
        w, h = c.winfo_width(), c.winfo_height()
        if w < 50:
            return
        larg_diag = int(w * 0.52)
        self._diagramma(20, 10, larg_diag, h - 20)
        x0 = larg_diag + 40
        lw = w - x0 - 28
        self._pseudocodice(x0, 10, lw)
        self._confronto(x0, 330, lw, h - 330 - 200)
        self._terminale(x0, h - 185, lw, 175)

    def _acceso(self, chiave: str) -> bool:
        return chiave in self.attivi

    def _diagramma(self, x0: int, y0: int, w: int, h: int) -> None:
        c = self.canvas
        cx = x0 + w // 2
        # coordinate verticali in proporzione all'altezza disponibile
        y = lambda f: y0 + int(h * f)
        dx = int(w * 0.33)
        sx, dx_ = cx - dx, cx + dx

        def freccia(punti, chiave, punta=True):
            on = self._acceso(chiave)
            c.create_line(*punti, fill=ACCENTO if on else SPENTO, width=5 if on else 3,
                          arrow="last" if punta else "none", arrowshape=(14, 16, 6))

        def colori(chiave, tipo):
            chiaro, scuro = COLORI[tipo]
            if self._acceso(chiave):
                return chiaro, scuro, 4
            return "#ffffff", SPENTO, 2

        def testo(x, yy, s, chiave, font=None):
            c.create_text(x, yy, text=s, font=font or self.f_blocco,
                          fill=TESTO if self._acceso(chiave) else TESTO_TENUE)

        # frecce (sotto i blocchi)
        freccia((cx, y(0.10), cx, y(0.16)), "f_lettura")
        freccia((cx, y(0.27), cx, y(0.33)), "f_decisione")
        freccia((cx + 150, y(0.44), dx_, y(0.44), dx_, y(0.60)), "f_si")
        freccia((cx - 150, y(0.44), sx, y(0.44), sx, y(0.60)), "f_no")
        freccia((dx_, y(0.72), dx_, y(0.83), cx, y(0.83)), "f_si_fine", punta=False)
        freccia((sx, y(0.72), sx, y(0.83), cx, y(0.83)), "f_no_fine", punta=False)
        on_fine = self._acceso("f_fine")
        freccia((cx, y(0.83), cx, y(0.88)), "f_fine")
        c.create_oval(cx - 6, y(0.83) - 6, cx + 6, y(0.83) + 6,
                      fill=ACCENTO if on_fine else SPENTO, outline="")

        # etichette sì / no
        c.create_text(cx + 175, y(0.44) - 18, text="sì", font=self.f_blocco_b,
                      fill=COLORI["si"][1] if self._acceso("f_si") else TESTO_TENUE)
        c.create_text(cx - 175, y(0.44) - 18, text="no", font=self.f_blocco_b,
                      fill=COLORI["no"][1] if self._acceso("f_no") else TESTO_TENUE)

        # inizio / fine
        for chiave, yy, s in (("inizio", y(0.055), "Inizio"), ("fine", y(0.93), "Fine")):
            f, o, sp = colori(chiave, "terminale")
            c.create_oval(cx - 90, yy - 28, cx + 90, yy + 28, fill=f, outline=o, width=sp)
            testo(cx, yy, s, chiave, self.f_blocco_b)

        # lettura
        f, o, sp = colori("lettura", "io")
        yt, yb = y(0.16), y(0.27)
        c.create_polygon(cx - 150, yt, cx + 170, yt, cx + 150, yb, cx - 170, yb,
                         fill=f, outline=o, width=sp)
        testo(cx, (yt + yb) // 2, self.etichetta_lettura, "lettura", self.f_blocco_b)

        # decisione
        f, o, sp = colori("decisione", "decisione")
        yc = y(0.44)
        dh = (y(0.55) - y(0.33)) // 2
        c.create_polygon(cx, yc - dh, cx + 150, yc, cx, yc + dh, cx - 150, yc,
                         fill=f, outline=o, width=sp)
        testo(cx, yc, self.etichetta_decisione, "decisione", self.f_blocco_b)

        # i due rami di uscita
        lb = int(w * 0.30)
        for chiave, xx, s in (("si", dx_, "a è maggiore di b"), ("no", sx, "a non è maggiore di b")):
            f, o, sp = colori(chiave, chiave)
            yt, yb = y(0.60), y(0.72)
            c.create_polygon(xx - lb // 2 + 14, yt, xx + lb // 2 + 14, yt, xx + lb // 2 - 14, yb,
                             xx - lb // 2 - 14, yb, fill=f, outline=o, width=sp)
            testo(xx, yt + (yb - yt) * 0.32, "Scrivi", chiave)
            testo(xx, yt + (yb - yt) * 0.68, f'"{s}"', chiave)

    def _pseudocodice(self, x0: int, y0: int, w: int) -> None:
        c = self.canvas
        riga_h = 30
        top = y0 + 38
        # il riquadro ha sempre l'altezza del pseudocodice, così il resto non si sposta
        c.create_rectangle(x0, top - 6, x0 + w, top + riga_h * len(PSEUDOCODICE) + 6,
                           fill="white", outline="#e2e8f0")
        if self.modo == "pseudo":
            titolo, righe, attiva, nota = "Pseudocodice", PSEUDOCODICE, self.riga_attiva, None
        else:
            titolo, righe = "Python", PYTHON
            corrisp = DA_PSEUDO_A_PYTHON.get(self.riga_attiva) if self.riga_attiva is not None else None
            attiva = corrisp if isinstance(corrisp, int) else None
            nota = corrisp if isinstance(corrisp, str) else None
        c.create_text(x0, y0 + 6, text=titolo, anchor="nw", font=self.f_blocco_b, fill=TESTO_TENUE)
        if nota:
            yy = top + riga_h * (len(PYTHON) + 0.5)
            c.create_rectangle(x0 + 2, yy, x0 + w - 2, yy + riga_h * 1.4, fill="#dbeafe", outline="")
            c.create_rectangle(x0 + 2, yy, x0 + 8, yy + riga_h * 1.4, fill=ACCENTO, outline="")
            c.create_text(x0 + 20, yy + riga_h * 0.7, text=nota, anchor="w", width=w - 30,
                          font=self.f_blocco, fill=TESTO)
        for i, riga in enumerate(righe):
            yy = top + i * riga_h
            on = i == attiva
            if on:
                c.create_rectangle(x0 + 2, yy, x0 + w - 2, yy + riga_h, fill="#dbeafe", outline="")
                c.create_rectangle(x0 + 2, yy, x0 + 8, yy + riga_h, fill=ACCENTO, outline="")
            c.create_text(x0 + 20, yy + riga_h // 2, text=riga, anchor="w",
                          font=self.f_mono_b if on else self.f_mono,
                          fill=TESTO if on else TESTO_TENUE)

    def _confronto(self, x0: int, y0: int, w: int, h: int) -> None:
        c = self.canvas
        c.create_text(x0, y0, text="I due numeri", anchor="nw", font=self.f_blocco_b, fill=TESTO_TENUE)
        valori = [(n, v) for n, v in (("a", self._letto("a")), ("b", self._letto("b"))) if v is not None]
        if not valori:
            return
        esito = self._esito()
        alto = y0 + 40
        massimo = max([abs(v) for _, v in valori] + [1])
        negativi = any(v < 0 for _, v in valori)
        base = (alto + y0 + h) // 2 if negativi else y0 + h   # linea dello zero
        scala = (base - alto - 30) / massimo
        lb = min(120, w // 5)
        c.create_line(x0, base, x0 + w, base, fill=LINEA, width=2)
        for nome, val in valori:
            xc = x0 + w * (0.3 if nome == "a" else 0.7)
            if esito is None:
                col = "#93c5fd"
            elif nome == "a":
                col = "#22c55e" if esito == "si" else "#f87171"
            else:
                col = "#94a3b8"
            top = base - val * scala
            c.create_rectangle(xc - lb / 2, min(top, base), xc + lb / 2, max(top, base) + (2 if val == 0 else 0),
                               fill=col, outline="")
            yy = min(top, base) - 20 if val >= 0 else max(top, base) + 20
            c.create_text(xc, yy, text=f"{nome} = {formatta(val)}", font=self.f_blocco_b, fill=TESTO)
        if len(valori) == 2 and self.indice >= 3:
            a, b = self.a, self.b
            simbolo = ">" if a > b else ("=" if a == b else "<")
            c.create_text(x0 + w / 2, (alto + base) / 2 if not negativi else alto + 20,
                          text=simbolo, font=self.f_numero, fill=TESTO)

    def _terminale(self, x0: int, y0: int, w: int, h: int) -> None:
        """Quello che vedrebbe chi usa il programma: le domande, le risposte e l'uscita."""
        c = self.canvas
        c.create_text(x0, y0, text="Terminale", anchor="nw", font=self.f_blocco_b, fill=TESTO_TENUE)
        c.create_rectangle(x0, y0 + 30, x0 + w, y0 + h, fill="#1e293b", outline="")
        riga_h = 40
        yy = y0 + 30 + 28
        tx = x0 + 20
        for nome, domanda in (("a", "Primo numero: "), ("b", "Secondo numero: ")):
            if self.indice < (1 if nome == "a" else 2):
                break
            c.create_text(tx, yy, text=domanda, anchor="w", font=self.f_term, fill="#e2e8f0")
            x_val = tx + self.f_term.measure(domanda) + 6
            if self.attesa == nome:
                c.create_window(x_val, yy, window=self.casella, anchor="w")
            else:
                c.create_text(x_val, yy, text=formatta(getattr(self, nome)), anchor="w",
                              font=self.f_term, fill="#fde68a")
            yy += riga_h
        if self.errore and self.attesa:
            c.create_text(tx, yy, text=self.errore, anchor="w", font=self.f_testo, fill="#fca5a5")
        esito = self._esito()
        if esito:
            testo = "a è maggiore di b" if esito == "si" else "a non è maggiore di b"
            c.create_text(tx, yy, text=testo, anchor="w", font=self.f_term,
                          fill="#4ade80" if esito == "si" else "#fca5a5")


if __name__ == "__main__":
    root = tk.Tk()
    app = Demo(root)
    root.after(300, app.da_capo)
    root.mainloop()
