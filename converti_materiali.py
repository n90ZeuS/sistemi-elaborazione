#!/usr/bin/env python3
"""
Script di conversione materiali del corso.
Converte:
  - Dispense Markdown → HTML (con syntax highlighting)
  - File Python → HTML (con syntax highlighting)
  - Cheatsheet, programma, calendario → HTML
Aggiunge slide di navigazione alle presentazioni.
"""

import re
import html
from pathlib import Path

# ─── Configurazione ───

BASE: Path = Path(__file__).parent

LEZIONI_FRONTALI: list[tuple[str, str]] = [
    ("T00", "Introduzione al corso"),
    ("T01", "Informazione, bit e numerazione"),
    ("T02", "Logica booleana e storia del calcolo"),
    ("T03", "Architettura degli elaboratori"),
    ("T04", "Sistemi operativi"),
    ("T05", "Rappresentazione dei dati"),
    ("T06", "Dal problema al programma"),
    ("T07", "Primi passi in Python"),
    ("T08", "Operatori, I/O e condizionali"),
    ("T09", "Cicli"),
    ("T10", "Comprehension e stringhe"),
    ("T11", "Liste e tuple"),
    ("T12", "Dizionari, set e mutabilità"),
    ("T13", "Funzioni: fondamenti"),
    ("T14", "Funzioni avanzate e moduli"),
    ("T15", "File, dati e gestione errori"),
    ("T16", "Programmazione a oggetti"),
    ("T17", "NumPy, Pandas e visualizzazione"),
]

LEZIONI_LAB: list[tuple[str, str]] = [
    ("L01", "Ambiente, variabili e condizionali"),
    ("L02", "Cicli, comprehension e stringhe"),
    ("L03", "Strutture dati"),
    ("L04", "Funzioni e modularità"),
    ("L05", "File e gestione dati"),
    ("L06", "Classi e oggetti"),
    ("L07", "NumPy e Pandas"),
    ("L08", "Visualizzazione e progetto"),
]

ALL_LEZIONI: list[tuple[str, str]] = LEZIONI_FRONTALI + LEZIONI_LAB
TITOLI: dict[str, str] = dict(ALL_LEZIONI)


def _ordine_calendario() -> list[str]:
    """Codici nell'ordine reale di svolgimento (calendario.json), usato per i
    link precedente/successiva. Se il calendario manca, ordine dei codici."""
    import json
    cal: Path = BASE / "calendario.json"
    if not cal.exists():
        return [c for c, _ in ALL_LEZIONI]
    slot = sorted(json.loads(cal.read_text(encoding="utf-8"))["slot"], key=lambda s: s["data"])
    ordine: list[str] = [c for s in slot for c in s["assegnato"] if c in TITOLI]
    return ordine + [c for c, _ in ALL_LEZIONI if c not in ordine]


ORDINE: list[str] = _ordine_calendario()

# Mappa codice lezione → nome file presentazione
PRES_FILES: dict[str, str] = {}
for p in (BASE / "presentazioni").glob("*.html"):
    if p.name == "template.html":
        continue
    code: str = p.stem.split("_")[0]
    PRES_FILES[code] = p.name

# Mappa codice lezione → nome file dispensa
DISP_FILES: dict[str, str] = {}
for subdir in ["frontali", "laboratori"]:
    dp: Path = BASE / "dispense" / subdir
    if dp.exists():
        for f in dp.glob("*.md"):
            code = f.stem.split("_")[0]
            DISP_FILES[code] = f"{subdir}/{f.stem}"

# Mappa codice lezione → cartella codice
CODE_DIRS: dict[str, str] = {}
codice_dir: Path = BASE / "codice"
if codice_dir.exists():
    for d in codice_dir.iterdir():
        if d.is_dir():
            code = d.name.split("_")[0]
            CODE_DIRS[code] = d.name


# ─── CSS condiviso ───

SHARED_CSS: str = """
:root {
    --accent: #2563eb;
    --accent-light: #dbeafe;
    --accent-dark: #1e40af;
    --text: #1e293b;
    --text-muted: #64748b;
    --bg: #ffffff;
    --bg-alt: #f8fafc;
    --border: #e2e8f0;
    --code-bg: #1e293b;
    --code-text: #e2e8f0;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif;
    color: var(--text);
    background: var(--bg);
    line-height: 1.7;
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem 1.5rem;
}

nav.top-nav {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid var(--border);
    font-size: 0.9rem;
}

nav.top-nav a {
    color: var(--accent);
    text-decoration: none;
    font-weight: 500;
}

nav.top-nav a:hover { text-decoration: underline; }

h1 {
    font-size: 2rem;
    font-weight: 700;
    color: var(--accent-dark);
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
}

h2 {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--accent);
    margin-top: 2rem;
    margin-bottom: 0.5rem;
    border-bottom: 2px solid var(--accent-light);
    padding-bottom: 0.2rem;
}

h3 {
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--text);
    margin-top: 1.5rem;
    margin-bottom: 0.4rem;
}

h4 { font-size: 1.05rem; font-weight: 600; margin-top: 1.2rem; margin-bottom: 0.3rem; }

p { margin-bottom: 0.8rem; }

ul, ol { margin-left: 1.5rem; margin-bottom: 0.8rem; }
li { margin-bottom: 0.3rem; }

code {
    font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', 'Menlo', monospace;
    font-size: 0.88em;
    background: var(--bg-alt);
    padding: 0.15em 0.4em;
    border-radius: 4px;
    border: 1px solid var(--border);
}

pre {
    background: var(--code-bg);
    color: var(--code-text);
    padding: 1rem 1.2rem;
    border-radius: 8px;
    overflow-x: auto;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    line-height: 1.5;
}

pre code {
    background: none;
    border: none;
    padding: 0;
    color: inherit;
    font-size: inherit;
}

/* Syntax highlighting (monokai-inspired) */
.kw { color: #f92672; }       /* keywords */
.fn { color: #a6e22e; }       /* function names */
.st { color: #e6db74; }       /* strings */
.cm { color: #75715e; }       /* comments */
.nb { color: #66d9ef; }       /* builtins */
.mi { color: #ae81ff; }       /* numbers */
.op { color: #f8f8f2; }       /* operators */
.dc { color: #a6e22e; }       /* decorators */

blockquote {
    border-left: 4px solid var(--accent);
    padding: 0.5rem 1rem;
    margin: 1rem 0;
    background: var(--accent-light);
    border-radius: 0 4px 4px 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    font-size: 0.9rem;
}

th {
    background: var(--accent-dark);
    color: white;
    padding: 0.5rem 0.8rem;
    text-align: left;
    font-weight: 600;
}

td {
    padding: 0.5rem 0.8rem;
    border-bottom: 1px solid var(--border);
}

tr:hover { background: var(--bg-alt); }

strong { font-weight: 600; }
em { font-style: italic; }

hr {
    border: none;
    border-top: 2px solid var(--border);
    margin: 2rem 0;
}

a { color: var(--accent); }

.download-link {
    display: inline-block;
    margin-bottom: 1rem;
    padding: 0.4rem 1rem;
    background: var(--accent);
    color: white;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
}

.download-link:hover { background: var(--accent-dark); }

nav.bottom-nav {
    display: flex;
    justify-content: space-between;
    margin-top: 3rem;
    padding-top: 1rem;
    border-top: 2px solid var(--border);
    font-size: 0.9rem;
}

nav.bottom-nav a {
    color: var(--accent);
    text-decoration: none;
    font-weight: 500;
}

nav.bottom-nav a:hover { text-decoration: underline; }

@media print {
    nav.top-nav, nav.bottom-nav, .download-link { display: none; }
    body { max-width: none; padding: 0; }
    pre, table, blockquote { break-inside: avoid; }
    h2, h3 { break-after: avoid; }
}
"""


# ─── Syntax highlighting per Python ───

PYTHON_KEYWORDS: set[str] = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield',
}

PYTHON_BUILTINS: set[str] = {
    'print', 'len', 'range', 'int', 'float', 'str', 'bool', 'list',
    'dict', 'set', 'tuple', 'type', 'isinstance', 'input', 'open',
    'sum', 'min', 'max', 'abs', 'round', 'sorted', 'reversed',
    'enumerate', 'zip', 'map', 'filter', 'any', 'all', 'super',
    'property', 'staticmethod', 'classmethod', 'ValueError', 'TypeError',
    'KeyError', 'IndexError', 'FileNotFoundError', 'Exception',
    'StopIteration', 'RuntimeError', 'AttributeError', 'NotImplementedError',
    'ZeroDivisionError', 'OSError', 'IOError', 'callable', 'hasattr',
    'getattr', 'setattr', 'id', 'hash', 'hex', 'oct', 'bin', 'ord', 'chr',
    'frozenset', 'complex', 'bytes', 'bytearray', 'memoryview', 'object',
    'format', 'iter', 'next', 'repr',
}


def highlight_python(code_text: str) -> str:
    """Evidenzia la sintassi Python con span colorati."""
    result: list[str] = []
    i: int = 0
    n: int = len(code_text)

    while i < n:
        # Commenti
        if code_text[i] == '#':
            end: int = code_text.find('\n', i)
            if end == -1:
                end = n
            result.append(f'<span class="cm">{html.escape(code_text[i:end])}</span>')
            i = end
            continue

        # Stringhe triple-quoted
        if code_text[i:i+3] in ('"""', "'''"):
            quote: str = code_text[i:i+3]
            end = code_text.find(quote, i + 3)
            if end == -1:
                end = n - 3
            result.append(f'<span class="st">{html.escape(code_text[i:end+3])}</span>')
            i = end + 3
            continue

        # Stringhe f-string o normali
        if code_text[i] in ('"', "'") or (code_text[i] in ('f', 'r', 'b') and i + 1 < n and code_text[i+1] in ('"', "'")):
            start: int = i
            if code_text[i] in ('f', 'r', 'b'):
                i += 1
            quote_char: str = code_text[i]
            i += 1
            while i < n and code_text[i] != quote_char:
                if code_text[i] == '\\':
                    i += 1
                i += 1
            if i < n:
                i += 1
            result.append(f'<span class="st">{html.escape(code_text[start:i])}</span>')
            continue

        # Decoratori
        if code_text[i] == '@' and (i == 0 or code_text[i-1] in (' ', '\n')):
            end = i + 1
            while end < n and (code_text[end].isalnum() or code_text[end] in '_.'):
                end += 1
            result.append(f'<span class="dc">{html.escape(code_text[i:end])}</span>')
            i = end
            continue

        # Numeri
        if code_text[i].isdigit() or (code_text[i] == '.' and i + 1 < n and code_text[i+1].isdigit()):
            end = i
            while end < n and (code_text[end].isalnum() or code_text[end] in '._'):
                end += 1
            result.append(f'<span class="mi">{html.escape(code_text[i:end])}</span>')
            i = end
            continue

        # Identificatori (keyword / builtin / normali)
        if code_text[i].isalpha() or code_text[i] == '_':
            end = i
            while end < n and (code_text[end].isalnum() or code_text[end] == '_'):
                end += 1
            word: str = code_text[i:end]
            if word in PYTHON_KEYWORDS:
                result.append(f'<span class="kw">{html.escape(word)}</span>')
            elif word in PYTHON_BUILTINS:
                result.append(f'<span class="nb">{html.escape(word)}</span>')
            else:
                # Check if it's a function definition
                # Look back for 'def ' or 'class '
                prev_text: str = ''.join(result[-5:]) if len(result) >= 5 else ''.join(result)
                if 'class="kw">def</span>' in prev_text or 'class="kw">class</span>' in prev_text:
                    result.append(f'<span class="fn">{html.escape(word)}</span>')
                else:
                    result.append(html.escape(word))
            i = end
            continue

        # Operatori
        if code_text[i] in '+-*/%=<>!&|^~':
            result.append(f'<span class="op">{html.escape(code_text[i])}</span>')
            i += 1
            continue

        # Tutto il resto
        result.append(html.escape(code_text[i]))
        i += 1

    return ''.join(result)


# ─── Convertitore Markdown → HTML ───

def md_to_html(md_text: str) -> str:
    """Converte Markdown basilare in HTML."""
    lines: list[str] = md_text.split('\n')
    out: list[str] = []
    in_code: bool = False
    code_lang: str = ""
    code_buf: list[str] = []
    in_list: str = ""  # "ul" or "ol"
    in_table: bool = False
    in_blockquote: bool = False
    table_header_done: bool = False

    def flush_list() -> None:
        nonlocal in_list
        if in_list:
            out.append(f'</{in_list}>')
            in_list = ""

    def flush_table() -> None:
        nonlocal in_table, table_header_done
        if in_table:
            out.append('</tbody></table>')
            in_table = False
            table_header_done = False

    def flush_blockquote() -> None:
        nonlocal in_blockquote
        if in_blockquote:
            out.append('</blockquote>')
            in_blockquote = False

    for line in lines:
        # Code blocks
        if line.strip().startswith('```'):
            if not in_code:
                flush_list()
                flush_table()
                flush_blockquote()
                in_code = True
                code_lang = line.strip()[3:].strip()
                code_buf = []
            else:
                code_text: str = '\n'.join(code_buf)
                if code_lang in ('python', 'py', ''):
                    highlighted: str = highlight_python(code_text)
                    out.append(f'<pre><code>{highlighted}</code></pre>')
                else:
                    out.append(f'<pre><code>{html.escape(code_text)}</code></pre>')
                in_code = False
                code_lang = ""
            continue

        if in_code:
            code_buf.append(line)
            continue

        stripped: str = line.strip()

        # Empty line
        if not stripped:
            flush_list()
            flush_table()
            flush_blockquote()
            continue

        # Blockquote
        if stripped.startswith('> '):
            flush_list()
            flush_table()
            if not in_blockquote:
                out.append('<blockquote>')
                in_blockquote = True
            out.append(f'<p>{inline_md(stripped[2:])}</p>')
            continue
        elif in_blockquote:
            flush_blockquote()

        # Headings
        heading_match = re.match(r'^(#{1,6})\s+(.+)', stripped)
        if heading_match:
            flush_list()
            flush_table()
            level: int = len(heading_match.group(1))
            text: str = inline_md(heading_match.group(2))
            out.append(f'<h{level}>{text}</h{level}>')
            continue

        # Horizontal rule
        if stripped in ('---', '***', '___'):
            flush_list()
            flush_table()
            out.append('<hr>')
            continue

        # Table
        if '|' in stripped and stripped.startswith('|'):
            cells: list[str] = [c.strip() for c in stripped.split('|')[1:-1]]
            # Check if separator row
            if all(re.match(r'^-+:?$|^:?-+:?$|^:?-+$', c) for c in cells if c):
                table_header_done = True
                continue
            if not in_table:
                flush_list()
                out.append('<table>')
                out.append('<thead><tr>')
                for cell in cells:
                    out.append(f'<th>{inline_md(cell)}</th>')
                out.append('</tr></thead><tbody>')
                in_table = True
            else:
                out.append('<tr>')
                for cell in cells:
                    out.append(f'<td>{inline_md(cell)}</td>')
                out.append('</tr>')
            continue

        # Unordered list
        ul_match = re.match(r'^[-*+]\s+(.+)', stripped)
        if ul_match:
            flush_table()
            if in_list != "ul":
                flush_list()
                out.append('<ul>')
                in_list = "ul"
            out.append(f'<li>{inline_md(ul_match.group(1))}</li>')
            continue

        # Ordered list
        ol_match = re.match(r'^\d+\.\s+(.+)', stripped)
        if ol_match:
            flush_table()
            if in_list != "ol":
                flush_list()
                out.append('<ol>')
                in_list = "ol"
            out.append(f'<li>{inline_md(ol_match.group(1))}</li>')
            continue

        # Paragraph
        flush_list()
        flush_table()
        out.append(f'<p>{inline_md(stripped)}</p>')

    flush_list()
    flush_table()
    flush_blockquote()

    return '\n'.join(out)


def inline_md(text: str) -> str:
    """Converte Markdown inline: bold, italic, code, links."""
    # Code spans (prima, per evitare conflitti)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Bold + italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.+?)_', r'<em>\1</em>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text


# ─── Generazione pagina HTML ───

def make_html_page(title: str, body: str, nav_links: dict[str, str] | None = None,
                   download_link: str | None = None,
                   download_label: str = "Scarica file .py") -> str:
    """Crea una pagina HTML completa con CSS e navigazione."""
    nav_html: str = ""
    if nav_links:
        parts: list[str] = []
        for label, href in nav_links.items():
            parts.append(f'<a href="{href}">{label}</a>')
        nav_html = f'<nav class="top-nav">{" &bull; ".join(parts)}</nav>'

    download_html: str = ""
    if download_link:
        download_html = f'<a class="download-link" href="{download_link}" download>{download_label}</a>'

    bottom_nav: str = ""
    if nav_links:
        items: list[str] = list(nav_links.items())
        left: str = ""
        right: str = ""
        for label, href in items:
            if "Precedente" in label or "←" in label:
                left = f'<a href="{href}">{label}</a>'
            elif "Successiv" in label or "→" in label:
                right = f'<a href="{href}">{label}</a>'
        home: str = '<a href="' + nav_links.get("Home", "../../index.html") + '">Home</a>'
        bottom_nav = f'<nav class="bottom-nav"><span>{left}</span><span>{home}</span><span>{right}</span></nav>'

    return f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)} — Sistemi di Elaborazione</title>
    <style>{SHARED_CSS}</style>
</head>
<body>
{nav_html}
<h1>{html.escape(title)}</h1>
{download_html}
{body}
{bottom_nav}
</body>
</html>
"""


# ─── Navigazione helper ───

def get_nav_links(code: str, kind: str, base_path: str = "../../") -> dict[str, str]:
    """Genera i link di navigazione per una pagina."""
    nav: dict[str, str] = {"Home": f"{base_path}index.html"}

    all_codes: list[str] = ORDINE
    if code in all_codes:
        idx: int = all_codes.index(code)
        if idx > 0:
            prev_code: str = all_codes[idx - 1]
            prev_title: str = TITOLI[prev_code]
            if kind == "dispensa":
                subdir: str = "frontali" if prev_code.startswith("T") else "laboratori"
                prev_file: str = DISP_FILES.get(prev_code, "")
                if prev_file:
                    nav[f"← {prev_code}"] = f"{base_path}dispense/{prev_file}.html"
            elif kind == "codice":
                prev_dir: str = CODE_DIRS.get(prev_code, "")
                if prev_dir:
                    nav[f"← {prev_code}"] = f"{base_path}codice/{prev_dir}/esercizi.html"

        if idx < len(all_codes) - 1:
            next_code: str = all_codes[idx + 1]
            next_title: str = TITOLI[next_code]
            if kind == "dispensa":
                subdir = "frontali" if next_code.startswith("T") else "laboratori"
                next_file: str = DISP_FILES.get(next_code, "")
                if next_file:
                    nav[f"{next_code} →"] = f"{base_path}dispense/{next_file}.html"
            elif kind == "codice":
                next_dir: str = CODE_DIRS.get(next_code, "")
                if next_dir:
                    nav[f"{next_code} →"] = f"{base_path}codice/{next_dir}/esercizi.html"

    return nav


# ─── Conversione dispense ───

def convert_dispense() -> None:
    """Converte tutte le dispense .md in .html."""
    for subdir in ["frontali", "laboratori"]:
        dp: Path = BASE / "dispense" / subdir
        if not dp.exists():
            continue
        for md_file in sorted(dp.glob("*.md")):
            code: str = md_file.stem.split("_")[0]
            title: str = ""
            for c, t in ALL_LEZIONI:
                if c == code:
                    title = f"{c} — {t}"
                    break
            if not title:
                title = md_file.stem.replace("_", " ")

            md_text: str = md_file.read_text(encoding="utf-8")
            body: str = md_to_html(md_text)

            nav: dict[str, str] = {"Home": "../../index.html"}
            all_codes: list[str] = ORDINE
            if code in all_codes:
                idx: int = all_codes.index(code)
                if idx > 0:
                    prev_code: str = all_codes[idx - 1]
                    prev_file: str = DISP_FILES.get(prev_code, "")
                    if prev_file:
                        # Same directory or cross-directory
                        prev_subdir: str = "frontali" if prev_code.startswith("T") else "laboratori"
                        if prev_subdir == subdir:
                            nav[f"← {prev_code}"] = f"{Path(DISP_FILES[prev_code]).name}.html"
                        else:
                            nav[f"← {prev_code}"] = f"../{prev_subdir}/{Path(DISP_FILES[prev_code]).name}.html"
                if idx < len(all_codes) - 1:
                    next_code: str = all_codes[idx + 1]
                    next_file: str = DISP_FILES.get(next_code, "")
                    if next_file:
                        next_subdir: str = "frontali" if next_code.startswith("T") else "laboratori"
                        if next_subdir == subdir:
                            nav[f"{next_code} →"] = f"{Path(DISP_FILES[next_code]).name}.html"
                        else:
                            nav[f"{next_code} →"] = f"../{next_subdir}/{Path(DISP_FILES[next_code]).name}.html"

            # Link alla presentazione
            if code in PRES_FILES:
                nav["Presentazione"] = f"../../presentazioni/{PRES_FILES[code]}"

            # Il PDF viene generato da genera_pdf.mjs al momento della pubblicazione
            html_content: str = make_html_page(title, body, nav,
                                               download_link=f"{md_file.stem}.pdf",
                                               download_label="Scarica PDF")
            out_file: Path = md_file.with_suffix('.html')
            out_file.write_text(html_content, encoding="utf-8")
            print(f"  ✓ {out_file.relative_to(BASE)}")


# ─── Conversione file Python ───

def convert_python_files() -> None:
    """Converte tutti i file .py in codice/ in .html con highlighting."""
    codice: Path = BASE / "codice"
    if not codice.exists():
        print("  ⚠ Cartella codice/ non trovata")
        return

    for py_file in sorted(codice.rglob("*.py")):
        code_text: str = py_file.read_text(encoding="utf-8")
        highlighted: str = highlight_python(code_text)
        body: str = f'<pre><code>{highlighted}</code></pre>'

        dir_code: str = py_file.parent.name.split("_")[0]
        title: str = f"{py_file.parent.name}/{py_file.name}"

        nav: dict[str, str] = {"Home": "../../index.html"}

        # Link alla dispensa corrispondente
        if dir_code in DISP_FILES:
            nav["Dispensa"] = f"../../dispense/{DISP_FILES[dir_code]}.html"

        # Link alla presentazione
        if dir_code in PRES_FILES:
            nav["Presentazione"] = f"../../presentazioni/{PRES_FILES[dir_code]}"

        # Link agli altri file nella stessa cartella
        for sibling in sorted(py_file.parent.glob("*.py")):
            if sibling != py_file:
                nav[sibling.stem.capitalize()] = f"{sibling.stem}.html"

        html_content: str = make_html_page(title, body, nav, download_link=py_file.name)
        out_file: Path = py_file.with_suffix('.html')
        out_file.write_text(html_content, encoding="utf-8")
        print(f"  ✓ {out_file.relative_to(BASE)}")


# ─── Conversione documenti root ───

def convert_root_docs() -> None:
    """Converte cheatsheet, programma e calendario in HTML."""
    docs: list[tuple[str, str]] = [
        ("cheatsheet_python.md", "Cheatsheet Python"),
        ("programma_sistemi_elaborazione.md", "Programma del corso"),
        ("calendario_lezioni.md", "Calendario delle lezioni"),
    ]

    for filename, title in docs:
        md_file: Path = BASE / filename
        if not md_file.exists():
            print(f"  ⚠ {filename} non trovato")
            continue

        md_text: str = md_file.read_text(encoding="utf-8")
        body: str = md_to_html(md_text)
        nav: dict[str, str] = {"Home": "index.html"}
        html_content: str = make_html_page(title, body, nav)
        out_file: Path = md_file.with_suffix('.html')
        out_file.write_text(html_content, encoding="utf-8")
        print(f"  ✓ {out_file.relative_to(BASE)}")


# ─── Conversione materiale supplementare ───

def convert_supplementary() -> None:
    """Converte autovalutazione, errori comuni, schede, progetti e glossario."""

    # Autovalutazione
    auto_dir: Path = BASE / "autovalutazione"
    if auto_dir.exists():
        for md_file in sorted(auto_dir.glob("*.md")):
            code: str = md_file.stem.split("_")[0]
            title_map: dict[str, str] = {c: t for c, t in ALL_LEZIONI}
            lesson_title: str = title_map.get(code, "")
            title: str = f"Autovalutazione — {code}: {lesson_title}" if lesson_title else md_file.stem.replace("_", " ")
            md_text: str = md_file.read_text(encoding="utf-8")
            body: str = md_to_html(md_text)
            nav: dict[str, str] = {"Home": "../index.html"}
            if code in DISP_FILES:
                nav["Dispensa"] = f"../dispense/{DISP_FILES[code]}.html"
            # Link a errori comuni corrispondente
            errori_file: Path = BASE / "errori_comuni" / f"{code}_errori.md"
            if errori_file.exists():
                nav["Errori comuni"] = f"../errori_comuni/{code}_errori.html"
            html_content: str = make_html_page(title, body, nav)
            out_file: Path = md_file.with_suffix('.html')
            out_file.write_text(html_content, encoding="utf-8")
            print(f"  ✓ {out_file.relative_to(BASE)}")

    # Errori comuni
    errori_dir: Path = BASE / "errori_comuni"
    if errori_dir.exists():
        for md_file in sorted(errori_dir.glob("*.md")):
            code = md_file.stem.split("_")[0]
            title_map = {c: t for c, t in ALL_LEZIONI}
            lesson_title = title_map.get(code, "")
            title = f"Errori comuni — {code}: {lesson_title}" if lesson_title else md_file.stem.replace("_", " ")
            md_text = md_file.read_text(encoding="utf-8")
            body = md_to_html(md_text)
            nav = {"Home": "../index.html"}
            if code in DISP_FILES:
                nav["Dispensa"] = f"../dispense/{DISP_FILES[code]}.html"
            auto_file: Path = BASE / "autovalutazione" / f"{code}_autovalutazione.md"
            if auto_file.exists():
                nav["Autovalutazione"] = f"../autovalutazione/{code}_autovalutazione.html"
            html_content = make_html_page(title, body, nav)
            out_file = md_file.with_suffix('.html')
            out_file.write_text(html_content, encoding="utf-8")
            print(f"  ✓ {out_file.relative_to(BASE)}")

    # Schede di confronto
    schede_dir: Path = BASE / "schede"
    if schede_dir.exists():
        for md_file in sorted(schede_dir.glob("*.md")):
            title = md_file.stem.replace("_", " ").title()
            md_text = md_file.read_text(encoding="utf-8")
            body = md_to_html(md_text)
            nav = {"Home": "../index.html"}
            html_content = make_html_page(title, body, nav)
            out_file = md_file.with_suffix('.html')
            out_file.write_text(html_content, encoding="utf-8")
            print(f"  ✓ {out_file.relative_to(BASE)}")

    # Progetti guidati
    progetti_dir: Path = BASE / "progetti"
    if progetti_dir.exists():
        for proj_dir in sorted(progetti_dir.iterdir()):
            if not proj_dir.is_dir():
                continue
            guida_md: Path = proj_dir / "guida.md"
            if guida_md.exists():
                title = proj_dir.name.replace("_", " ").replace("progetto ", "Progetto ").title()
                md_text = guida_md.read_text(encoding="utf-8")
                body = md_to_html(md_text)
                nav = {"Home": "../../index.html"}
                # Link alla soluzione .py se presente
                sol_py: Path = proj_dir / "soluzione.py"
                if sol_py.exists():
                    nav["Soluzione (.py)"] = "soluzione.py"
                html_content = make_html_page(title, body, nav)
                out_file = guida_md.with_suffix('.html')
                out_file.write_text(html_content, encoding="utf-8")
                print(f"  ✓ {out_file.relative_to(BASE)}")

    # Glossario
    glossario_md: Path = BASE / "glossario.md"
    if glossario_md.exists():
        md_text = glossario_md.read_text(encoding="utf-8")
        body = md_to_html(md_text)
        nav = {"Home": "index.html"}
        html_content = make_html_page("Glossario Python", body, nav)
        out_file = glossario_md.with_suffix('.html')
        out_file.write_text(html_content, encoding="utf-8")
        print(f"  ✓ {out_file.relative_to(BASE)}")


# ─── Aggiunta navigazione alle presentazioni ───

def add_nav_to_presentations() -> None:
    """Aggiunge una slide finale di navigazione a ogni presentazione."""
    pres_dir: Path = BASE / "presentazioni"
    if not pres_dir.exists():
        return

    for pres_file in sorted(pres_dir.glob("*.html")):
        if pres_file.name == "template.html":
            continue

        code: str = pres_file.stem.split("_")[0]
        title: str = ""
        for c, t in ALL_LEZIONI:
            if c == code:
                title = t
                break

        content: str = pres_file.read_text(encoding="utf-8")

        # Se la slide di navigazione c'è già, la si rigenera (l'ordine segue il calendario)
        content = re.sub(r'\n*[ \t]*<!-- Slide di navigazione -->\s*<section class="nav-slide">.*?</section>\s*</section>\n?',
                         '', content, count=1, flags=re.DOTALL)

        # Costruisci i link
        all_codes: list[str] = ORDINE
        nav_items: list[str] = []

        nav_items.append('<a href="../index.html" style="color: var(--accent);">&#127968; Home del corso</a>')
        nav_items.append(f'<a href="{pres_file.with_suffix(".pdf").name}" style="color: #475569;">&#11015; Scarica PDF</a>')

        if code in all_codes:
            idx: int = all_codes.index(code)
            if idx > 0:
                prev_code: str = all_codes[idx - 1]
                prev_name: str = TITOLI[prev_code]
                prev_file: str = PRES_FILES.get(prev_code, "")
                if prev_file:
                    nav_items.append(f'<a href="{prev_file}" style="color: var(--accent);">&larr; {prev_code}: {prev_name}</a>')

            if idx < len(all_codes) - 1:
                next_code: str = all_codes[idx + 1]
                next_name: str = TITOLI[next_code]
                next_file: str = PRES_FILES.get(next_code, "")
                if next_file:
                    nav_items.append(f'<a href="{next_file}" style="color: var(--accent);">{next_code}: {next_name} &rarr;</a>')

        # Link a dispensa
        if code in DISP_FILES:
            nav_items.append(f'<a href="../dispense/{DISP_FILES[code]}.html" style="color: #16a34a;">&#128214; Dispensa</a>')

        # Link a codice
        if code in CODE_DIRS:
            nav_items.append(f'<a href="../codice/{CODE_DIRS[code]}/esercizi.html" style="color: #d97706;">&#128187; Codice</a>')

        nav_slide: str = f"""
            <!-- Slide di navigazione -->
            <section class="nav-slide">
                <section>
                    <h2>Navigazione</h2>
                    <div style="display: flex; flex-direction: column; gap: 1.2rem; align-items: center; margin-top: 2rem; font-size: 0.95em;">
                        {''.join(f'<div>{item}</div>' for item in nav_items)}
                    </div>
                </section>
            </section>
"""

        # Inserisci prima della chiusura di </div> (slides container)
        # Cerchiamo il pattern </div> seguito dal footer
        insert_marker: str = '    </div>\n        <div class="slide-footer">'
        if insert_marker in content:
            content = content.replace(
                insert_marker,
                nav_slide + '\n    </div>\n        <div class="slide-footer">'
            )
        else:
            # Fallback: inserisci prima dell'ultimo </div> prima di </div>\n\n    <script
            alt_marker: str = '        </div>\n    </div>\n\n    <script'
            if alt_marker in content:
                content = content.replace(
                    alt_marker,
                    nav_slide + '\n        </div>\n    </div>\n\n    <script'
                )
            else:
                # Ultimo tentativo: prima del tag </body>
                content = content.replace('</body>', nav_slide + '\n</body>')

        pres_file.write_text(content, encoding="utf-8")
        print(f"  ✓ {pres_file.name}")


# ─── Main ───

def main() -> None:
    print("=" * 60)
    print("Conversione materiali — Sistemi di Elaborazione")
    print("=" * 60)

    # Aggiorna le mappe dopo che i file codice sono stati creati
    global CODE_DIRS
    codice_dir_check: Path = BASE / "codice"
    if codice_dir_check.exists():
        CODE_DIRS = {}
        for d in codice_dir_check.iterdir():
            if d.is_dir():
                code: str = d.name.split("_")[0]
                CODE_DIRS[code] = d.name

    print("\n📄 Conversione dispense Markdown → HTML...")
    convert_dispense()

    print("\n🐍 Conversione file Python → HTML...")
    convert_python_files()

    print("\n📋 Conversione documenti root → HTML...")
    convert_root_docs()

    print("\n📚 Conversione materiale supplementare → HTML...")
    convert_supplementary()

    print("\n🔗 Aggiunta navigazione alle presentazioni...")
    add_nav_to_presentations()

    print("\n✅ Conversione completata!")
    print(f"   Portale: {BASE / 'index.html'}")


if __name__ == "__main__":
    main()
