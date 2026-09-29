#!/usr/bin/env python3
"""
Pubblicazione progressiva dei materiali del corso.

Legge calendario.json (sorgente unica di date e assegnazioni) e allinea index.html:
  - aggiunge la colonna "Data" alle tabelle di lezioni e laboratori
  - il materiale diventa cliccabile ANTICIPO giorni prima della lezione (default 7)
  - le lezioni piu' lontane compaiono disattivate, con la loro data

L'operazione e' reversibile e ripetibile: rilanciare lo script dopo aver
modificato calendario.json riallinea tutto, riattivando o disattivando
le righe secondo le nuove date.

Uso:
    python3 pianifica.py                 # usa la data odierna
    python3 pianifica.py --data 2026-11-15   # simula un'altra data
    python3 pianifica.py --controlla     # solo diagnostica, non scrive nulla
    python3 pianifica.py --anticipo 3    # pubblica 3 giorni prima invece di 7
    python3 pianifica.py --pota          # cancella i file bloccati (solo sulla copia del sito!)
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import sys
from pathlib import Path

BASE = Path(__file__).parent
CALENDARIO = BASE / "calendario.json"
INDEX = BASE / "index.html"
CALENDARIO_MD = BASE / "calendario_lezioni.md"

TITOLI_EXTRA = {"T00": "Introduzione al corso"}

ANTICIPO_DEFAULT = 7   # giorni di anticipo con cui il materiale viene pubblicato

GIORNI = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]
MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
        "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]

# Prerequisiti: ogni laboratorio richiede che queste lezioni siano gia' state tenute
PREREQUISITI = {
    "L01": ["T07", "T08"],
    "L02": ["T09", "T10"],
    "L03": ["T11", "T12"],
    "L04": ["T13", "T14"],
    "L05": ["T15"],
    "L06": ["T16"],
    "L07": ["T17"],
    "L08": ["T17"],
}

CSS_MARKER = "/* === pianifica.py: stato di pubblicazione === */"
CSS_BLOCCO = f"""
        {CSS_MARKER}
        .lesson-date {{
            white-space: nowrap;
            font-variant-numeric: tabular-nums;
            color: var(--text-muted, #64748b);
            font-size: 0.85em;
        }}
        tr.futura {{ opacity: 0.55; }}
        tr.futura .lesson-title {{ font-style: italic; }}
        .badge-locked {{
            display: inline-block;
            border: 1px dashed #cbd5e1;
            color: #94a3b8;
            background: #f8fafc;
            cursor: not-allowed;
        }}
        tr.prossima {{
            background: #eff6ff;
            opacity: 1;
        }}
        tr.prossima .lesson-title {{ font-style: normal; font-weight: 600; }}
"""


# ─── Lettura del calendario ───

def carica_calendario() -> list[dict]:
    if not CALENDARIO.exists():
        sys.exit(f"ERRORE: manca {CALENDARIO.name}")
    dati = json.loads(CALENDARIO.read_text(encoding="utf-8"))
    slot = dati["slot"]
    for s in slot:
        s["_data"] = dt.date.fromisoformat(s["data"])
    return sorted(slot, key=lambda s: s["_data"])


def mappa_codici(slot: list[dict]) -> dict[str, dict]:
    """codice lezione -> slot in cui viene tenuta"""
    m: dict[str, dict] = {}
    for s in slot:
        for codice in s["assegnato"]:
            if codice in m:
                print(f"  ATTENZIONE: {codice} assegnato due volte "
                      f"({m[codice]['data']} e {s['data']})")
            m[codice] = s
    return m


def data_estesa(d: dt.date) -> str:
    return f"{GIORNI[d.weekday()]} {d.day} {MESI[d.month - 1]}"


def data_breve(d: dt.date) -> str:
    return f"{d.day:02d}/{d.month:02d}"


# ─── Diagnostica ───

def controlla(slot: list[dict], codici: dict[str, dict]) -> bool:
    ok = True
    attesi = [f"T{i:02d}" for i in range(18)] + [f"L{i:02d}" for i in range(1, 9)]

    mancanti = [c for c in attesi if c not in codici]
    if mancanti:
        ok = False
        print(f"  Non assegnate: {', '.join(mancanti)}")

    ignoti = [c for c in codici if c not in attesi]
    if ignoti:
        ok = False
        print(f"  Codici sconosciuti in calendario.json: {', '.join(ignoti)}")

    for lab, richiesti in PREREQUISITI.items():
        if lab not in codici:
            continue
        for req in richiesti:
            if req not in codici:
                continue
            if codici[req]["_data"] >= codici[lab]["_data"]:
                ok = False
                print(f"  {lab} ({codici[lab]['data']}) richiede {req}, "
                      f"ma {req} e' previsto il {codici[req]['data']}")

    riserve = [s for s in slot if not s["assegnato"]]
    lezioni = [s for s in slot if s["tipo"] == "lezione"]
    lab = [s for s in slot if s["tipo"] == "laboratorio"]
    print(f"  Slot totali: {len(slot)}  (lezioni {len(lezioni)}, laboratori {len(lab)})")
    print(f"  Riserve non assegnate: {len(riserve)}"
          + (f" -> {', '.join(s['data'] for s in riserve)}" if riserve else ""))
    return ok


# ─── Trasformazione di index.html ───

RE_RIGA = re.compile(
    r'<tr[^>]*>\s*<td class="lesson-id">(T\d{2}|L\d{2})</td>(.*?)</tr>',
    re.DOTALL,
)
RE_CELLA_DATA = re.compile(r'\s*<td class="lesson-date">.*?</td>', re.DOTALL)
RE_TITOLO = re.compile(r'(<td class="lesson-title">.*?</td>)', re.DOTALL)
RE_LINK = re.compile(r'<a class="badge ([a-z- ]+)" href="([^"]+)">([^<]*)</a>')
RE_LOCK = re.compile(r'<span class="badge ([a-z- ]+) badge-locked" data-href="([^"]+)">([^<]*)</span>')


def sblocca(corpo: str) -> str:
    return RE_LOCK.sub(lambda m: f'<a class="badge {m.group(1)}" href="{m.group(2)}">{m.group(3)}</a>', corpo)


def blocca(corpo: str) -> str:
    return RE_LINK.sub(lambda m: f'<span class="badge {m.group(1)} badge-locked" data-href="{m.group(2)}">{m.group(3)}</span>', corpo)


def aggiungi_intestazioni(html: str) -> str:
    """Inserisce <th>Data</th> dopo la colonna del titolo, una volta sola."""
    def sost(m: re.Match) -> str:
        blocco = m.group(0)
        if "<th>Data</th>" in blocco:
            return blocco
        return re.sub(
            r'(<th>(?:Lezione|Laboratorio)</th>)',
            r'\1\n                    <th>Data</th>',
            blocco,
            count=1,
        )
    return re.sub(r'<thead>.*?</thead>', sost, html, flags=re.DOTALL)


def pubblicato(slot: dict, oggi: dt.date, anticipo: int) -> bool:
    return slot["_data"] - dt.timedelta(days=anticipo) <= oggi


def aggiorna_index(html: str, codici: dict[str, dict], oggi: dt.date,
                   anticipo: int = ANTICIPO_DEFAULT) -> tuple[str, int, int]:
    html = aggiungi_intestazioni(html)

    # prossimo slot in programma, per evidenziarlo
    futuri = sorted((s["_data"] for s in codici.values() if s["_data"] >= oggi))
    prossima = futuri[0] if futuri else None

    pubbl = fut = 0

    def sost_riga(m: re.Match) -> str:
        nonlocal pubbl, fut
        codice, corpo = m.group(1), m.group(2)
        slot = codici.get(codice)

        corpo = RE_CELLA_DATA.sub("", corpo)
        corpo = sblocca(corpo)

        if slot is None:
            cella = '<td class="lesson-date">&mdash;</td>'
            classe = ""
        else:
            d = slot["_data"]
            cella = f'<td class="lesson-date">{data_breve(d)}</td>'
            if pubblicato(slot, oggi, anticipo):
                classe = ' class="prossima"' if d == prossima else ""
                pubbl += 1
            else:
                corpo = blocca(corpo)
                classe = ' class="futura prossima"' if d == prossima else ' class="futura"'
                fut += 1

        corpo = RE_TITOLO.sub(
            lambda t: t.group(1) + "\n                    " + cella, corpo, count=1
        )
        return f"<tr{classe}>\n                    " \
               f'<td class="lesson-id">{codice}</td>{corpo}</tr>'

    html = RE_RIGA.sub(sost_riga, html)

    if CSS_MARKER not in html:
        html = html.replace("    </style>", CSS_BLOCCO + "    </style>", 1)

    return html, pubbl, fut


# ─── Trasformazione di calendario_lezioni.md ───

# accetta sia la forma originale ("Lezione 4") sia quella gia' convertita ("T04")
RE_H_LEZ = re.compile(r'^### (?:Lezione (\d+)|T(\d{2})) — (.+)$', re.MULTILINE)
RE_H_LAB = re.compile(r'^### (🖥️ )?(?:Laboratorio (\d+)|L(\d{2})) — (.+)$', re.MULTILINE)
RE_QUANDO = re.compile(r'\n\n\*\*Quando:\*\* [^\n]*')

NOTA_ORDINE = ("*Le sezioni qui sotto sono raggruppate per tema, non in ordine cronologico. "
               "L'ordine reale di svolgimento è nello schema in fondo alla pagina.*")


def _riga_quando(slot: dict, extra: str = "") -> str:
    d = slot["_data"]
    quando = f"{data_estesa(d)} {d.year}, {slot['ora']} — {slot['aula']}"
    if slot["tipo"] == "laboratorio":
        quando += " (due turni)"
    return f"\n\n**Quando:** {quando}{extra}"


def aggiorna_calendario_md(codici: dict[str, dict]) -> bool:
    if not CALENDARIO_MD.exists():
        print("  calendario_lezioni.md non trovato, salto.")
        return False

    testo = originale = CALENDARIO_MD.read_text(encoding="utf-8")
    titoli: dict[str, str] = dict(TITOLI_EXTRA)

    def sost_lez(m: re.Match) -> str:
        num, gia, titolo = m.group(1), m.group(2), m.group(3)
        codice = f"T{int(num):02d}" if num else f"T{gia}"
        titoli[codice] = titolo.strip()
        return f"### {codice} — {titolo}"

    def sost_lab(m: re.Match) -> str:
        icona, num, gia, titolo = m.group(1) or "", m.group(2), m.group(3), m.group(4)
        codice = f"L{int(num):02d}" if num else f"L{gia}"
        titoli[codice] = titolo.strip()
        return f"### {icona}{codice} — {titolo}"

    testo = RE_H_LEZ.sub(sost_lez, testo)
    testo = RE_H_LAB.sub(sost_lab, testo)

    # rimuove eventuali righe "Quando" di una passata precedente, poi le reinserisce
    testo = RE_QUANDO.sub("", testo)

    def inserisci(m: re.Match) -> str:
        riga = m.group(0)
        codice = m.group(1)
        slot = codici.get(codice)
        if slot is None:
            return riga
        extra = ""
        if codice == "T01" and "T00" in slot["assegnato"]:
            extra = " — nello stesso incontro anche T00, apertura del corso"
        return riga + _riga_quando(slot, extra)

    testo = re.sub(r'^### (?:🖥️ )?([TL]\d{2}) — .+$', inserisci, testo, flags=re.MULTILINE)

    # intestazioni di fase: non implicano piu' un ordine cronologico
    testo = testo.replace(
        "## Fase 1 — Solo lezioni frontali (Fondamenti)",
        "## Blocco tematico — Fondamenti: la macchina e l'informazione")
    testo = testo.replace(
        "## Fase 2 — Lezioni frontali + laboratori alternati",
        "## Blocco tematico — Python, strutture dati e librerie")
    for vecchia in (
        "*Le prime 6 lezioni costruiscono le fondamenta: dalla materia alla macchina, "
        "dalla macchina al pensiero computazionale, dal pensiero al linguaggio.*",
        "*Schema tipico: 2 frontali → 1 laboratorio. Gli studenti mettono in pratica "
        "ciò che hanno visto nelle frontali precedenti.*",
    ):
        testo = testo.replace(vecchia, NOTA_ORDINE)

    testo = re.sub(r"\n{3,}", "\n\n", testo)   # nessun accumulo di righe vuote
    testo = _riscrivi_schema(testo, titoli)

    if testo != originale:
        CALENDARIO_MD.write_text(testo, encoding="utf-8")
        return True
    return False


def _riscrivi_schema(testo: str, titoli: dict[str, str]) -> str:
    slot = carica_calendario()
    righe = ["## Schema riassuntivo",
             "",
             "*Ordine reale di svolgimento, dall'orario ufficiale dell'Ateneo.*",
             "",
             "| # | Data | Tipo | Contenuto | Aula |",
             "|---|------|------|-----------|------|"]
    for i, s in enumerate(slot, 1):
        d = s["_data"]
        data = f"{GIORNI[d.weekday()][:3]} {d.day:02d}/{d.month:02d}"
        if not s["assegnato"]:
            righe.append(f"| {i} | {data} | — | *{s.get('nota', 'riserva')}* | {s['aula']} |")
            continue
        tipo = "**Lab**" if s["tipo"] == "laboratorio" else "Frontale"
        voci = " + ".join(
            f"**{c}** {titoli.get(c, '')}".strip() for c in s["assegnato"]
        )
        righe.append(f"| {i} | {data} | {tipo} | {voci} | {s['aula']} |")

    nuovo = "\n".join(righe) + "\n"
    if "## Schema riassuntivo" in testo:
        return re.sub(r'## Schema riassuntivo.*\Z', nuovo, testo, flags=re.DOTALL)
    return testo.rstrip() + "\n\n---\n\n" + nuovo


# ─── Potatura della copia del sito ───

def pota(codici: dict[str, dict], oggi: dt.date, anticipo: int) -> None:
    """Cancella file e cartelle il cui nome inizia con il codice di una
    lezione non ancora pubblicata (es. presentazioni/T09_cicli.html,
    codice/T09_cicli/, autovalutazione/T09_autovalutazione.md)."""
    if (BASE / ".git").exists():
        sys.exit("ERRORE: --pota va usato sulla copia del sito, non sul repository.")
    bloccati = sorted(c for c, s in codici.items() if not pubblicato(s, oggi, anticipo))
    rimossi = 0
    for codice in bloccati:
        for voce in sorted(BASE.rglob(f"{codice}_*"), key=lambda v: -len(v.parts)):
            if not voce.exists():
                continue
            if voce.is_dir():
                shutil.rmtree(voce)
            else:
                voce.unlink()
            rimossi += 1
    print(f"  Potatura: {rimossi} file/cartelle rimossi per {len(bloccati)} lezioni non pubblicate.")

    # I link rimasti verso materiale rimosso (es. "T06 →" nella navigazione)
    # diventano testo semplice, cosi' non portano a una pagina 404.
    re_link = re.compile(r'<a ([^>]*?)href="([^"#:]+\.(?:html|pdf|py))"([^>]*)>(.*?)</a>', re.DOTALL)
    disattivati = 0
    for pagina in BASE.rglob("*.html"):
        testo = pagina.read_text(encoding="utf-8")

        def sost(m: re.Match) -> str:
            nonlocal disattivati
            destinazione = (pagina.parent / m.group(2)).resolve()
            if destinazione.exists() or not any(
                    Path(m.group(2)).name.startswith(f"{c}_") or f"/{c}_" in m.group(2)
                    for c in bloccati):
                return m.group(0)
            disattivati += 1
            return f'<span class="link-non-pubblicato" title="Non ancora pubblicato" ' \
                   f'style="opacity: 0.5; cursor: not-allowed;">{m.group(4)}</span>'

        nuovo = re_link.sub(sost, testo)
        if nuovo != testo:
            pagina.write_text(nuovo, encoding="utf-8")
    print(f"  Link a materiale non pubblicato disattivati: {disattivati}")


# ─── main ───

def main() -> None:
    ap = argparse.ArgumentParser(description="Pubblicazione progressiva dei materiali")
    ap.add_argument("--data", help="data di riferimento (AAAA-MM-GG), default: oggi")
    ap.add_argument("--controlla", action="store_true", help="solo diagnostica")
    ap.add_argument("--sblocca", action="store_true",
                    help="sblocca tutto il materiale, ignorando le date (uso locale)")
    ap.add_argument("--anticipo", type=int, default=ANTICIPO_DEFAULT,
                    help=f"giorni di anticipo della pubblicazione (default {ANTICIPO_DEFAULT})")
    ap.add_argument("--pota", action="store_true",
                    help="cancella i file delle lezioni non ancora pubblicate "
                         "(da usare SOLO sulla copia del sito, mai sul repo)")
    args = ap.parse_args()

    sbloccato = args.sblocca
    oggi = dt.date.max if sbloccato else (
        dt.date.fromisoformat(args.data) if args.data else dt.date.today())

    slot = carica_calendario()
    codici = mappa_codici(slot)

    print("=" * 62)
    if sbloccato:
        print("Pianificazione — TUTTO SBLOCCATO (date ignorate, solo per uso locale)")
    else:
        print(f"Pianificazione — data di riferimento: {data_estesa(oggi)} {oggi.year}, "
              f"anticipo {args.anticipo} giorni")
    print("=" * 62)

    valido = controlla(slot, codici)
    if not valido:
        print("\n  Il calendario ha incoerenze (vedi sopra).")
    if args.controlla:
        pubbl = [c for c, s in codici.items() if pubblicato(s, oggi, args.anticipo)]
        print(f"\n  Pubblicate: {len(pubbl)} -> {', '.join(sorted(pubbl)) or 'nessuna'}")
        sys.exit(0 if valido else 1)

    html = INDEX.read_text(encoding="utf-8")
    nuovo, pubbl, fut = aggiorna_index(html, codici, oggi, args.anticipo)

    if nuovo == html:
        print("\n  index.html gia' allineato, nessuna modifica.")
    else:
        INDEX.write_text(nuovo, encoding="utf-8")
        print(f"\n  index.html aggiornato: {pubbl} righe pubblicate, {fut} disattivate.")

    if aggiorna_calendario_md(codici):
        print("  calendario_lezioni.md aggiornato: date e schema cronologico.")
    else:
        print("  calendario_lezioni.md gia' allineato.")

    if args.pota:
        pota(codici, oggi, args.anticipo)

    prossimi = [s for s in slot if s["_data"] >= oggi]
    if prossimi:
        p = prossimi[0]
        eti = ", ".join(p["assegnato"]) if p["assegnato"] else p.get("nota", "riserva")
        print(f"  Prossimo incontro: {data_estesa(p['_data'])} — {eti} ({p['aula']})")


if __name__ == "__main__":
    main()
