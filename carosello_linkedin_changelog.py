"""Carosello LinkedIn (PDF, slide 1080x1350) dal report qgis_<ver>_summary.md.

Usa solo le sezioni fino a "Finanziatori" (esclusa l'"Elenco completo").
Richiede Pillow e i font Arial / Yu Gothic di Windows (C:/Windows/Fonts).

Uso:
    python carosello_linkedin_changelog.py changelog_QGIS-4.4/qgis_4.4_summary.md changelog_QGIS-4.4/qgis_4.4_carosello_linkedin.pdf --nome Auckland
    (--png salva anche ogni slide come PNG)
    GIF animata con i colori del brand QGIS:
    python carosello_linkedin_changelog.py changelog_QGIS-4.4/qgis_4.4_summary.md out.pdf --nome Auckland --tema qgis --gif changelog_QGIS-4.4/qgis_4.4_carosello_linkedin.gif
"""
import argparse
import re
import textwrap
from PIL import Image, ImageDraw, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument("src", help="report qgis_<ver>_summary.md")
ap.add_argument("out", help="PDF di uscita")
ap.add_argument("--nome", default="", help="nome della release, es. Auckland")
ap.add_argument("--png", action="store_true", help="salva anche le slide in PNG")
ap.add_argument("--gif", help="salva anche una GIF animata del carosello (percorso)")
ap.add_argument("--tema", choices=["base", "qgis"], default="base", help="qgis = palette ufficiale QGIS")
args = ap.parse_args()
src, out = args.src, args.out
md = open(src, encoding="utf-8").read().split("## Elenco completo")[0]

S = 2
W, H = 1080 * S, 1350 * S
F = "C:/Windows/Fonts/"
bold = lambda s: ImageFont.truetype(F + "arialbd.ttf", int(s * S))
reg = lambda s: ImageFont.truetype(F + "arial.ttf", int(s * S))

BG = (236, 236, 236)
CARD = (250, 250, 250)
ORANGE = (230, 110, 10)
GREEN = (79, 125, 50)       # serie unica (verde QGIS scuro)
BAND = [GREEN]              # fascia in alto
if args.tema == "qgis":     # palette del brand QGIS
    GREEN = (0x58, 0x96, 0x32)
    ORANGE = (0xEE, 0x79, 0x13)
    BAND = [GREEN, (0x93, 0xB0, 0x23), (0xF0, 0xE6, 0x4A), ORANGE]


def band(d):
    """Fascia colorata in alto: tinta unica o strisce con i colori QGIS."""
    w = W / len(BAND)
    for i, c in enumerate(BAND):
        d.rectangle((int(i * w), 0, int((i + 1) * w), 14 * S), fill=c)
TRACK = (222, 222, 222)
INK = (17, 17, 17)
INK2 = (75, 75, 75)
MUTED = (110, 110, 110)


def section(title):
    m = re.search(r"## " + re.escape(title) + r"\n(.*?)(?=\n## |\Z)", md, re.S)
    return m.group(1)


def table(title):
    rows = []
    for ln in section(title).splitlines():
        if ln.startswith("|") and not re.match(r"\|[-:| ]+\|$", ln):
            rows.append([c.strip() for c in ln.strip("|").split("|")])
    return rows[1:]


over = dict(re.findall(r"- \*\*(.+?):\*\* (.+)", section("Panoramica")))
ver = re.search(r"# Report QGIS (\S+)", md).group(1)
full = f"{ver} {args.nome}".strip()
cats = [(r[0], int(r[1])) for r in table("Feature per categoria")]
devs = [(r[1], int(r[2]), r[3]) for r in table("Top sviluppatori")]
comps = [(r[0], int(r[1])) for r in table("Feature per azienda (via mappatura sviluppatori)")]
funds = [(r[0], int(r[1])) for r in table("Finanziatori")]
TOTAL = 7


def base(n, kicker, title):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    band(d)
    d.text((80 * S, 80 * S), kicker, font=bold(30), fill=ORANGE)
    y = 128 * S
    for line in title.split("\n"):
        d.text((80 * S, y), line, font=bold(64), fill=INK)
        y += 76 * S
    d.line((80 * S, H - 110 * S, W - 80 * S, H - 110 * S), fill=(205, 205, 205), width=2 * S)
    d.text((80 * S, H - 86 * S), f"QGIS {full} in numeri", font=bold(24), fill=INK2)
    t = f"{n} / {TOTAL}"
    d.text((W - 80 * S - d.textlength(t, font=reg(24)), H - 86 * S), t, font=reg(24), fill=MUTED)
    return im, d, y + 30 * S


def bars(d, y0, items, label_w, row_h, note=None, fs=26):
    """Barre orizzontali ordinate, serie unica, valore a fine barra."""
    x_lab, x_bar = 80 * S, (80 + label_w) * S
    x_max = W - 150 * S
    mx = max(v for _, v, *_ in items)
    bh = int(row_h * 0.46) * S
    y = y0
    for it in items:
        name, v = it[0], it[1]
        sub = it[2] if len(it) > 2 else None
        cy = y + row_h * S // 2
        lines = textwrap.wrap(name, width=int(label_w / (fs * 0.52))) or [name]
        lh = (fs + 6) * S
        block = lh * len(lines) + ((fs - 4 + 6) * S if sub else 0)
        ty = cy - block // 2
        for ln in lines:
            cjk = any(ord(ch) > 0x2E80 for ch in ln)  # Arial non ha i glifi CJK
            fnt = ImageFont.truetype(F + "YuGothM.ttc", int(fs * S)) if cjk else reg(fs)
            d.text((x_lab, ty), ln, font=fnt, fill=INK)
            ty += lh
        if sub:
            d.text((x_lab, ty), sub, font=reg(fs - 4), fill=MUTED)
        d.rounded_rectangle((x_bar, cy - bh // 2, x_max, cy + bh // 2), 4 * S, fill=TRACK)
        xe = x_bar + max(int((x_max - x_bar) * v / mx), 8 * S)
        d.rounded_rectangle((x_bar, cy - bh // 2, xe, cy + bh // 2), 4 * S, fill=GREEN)
        d.text((xe + 14 * S, cy - (fs + 4) * S // 2 - 2 * S), str(v), font=bold(fs + 4), fill=INK)
        y += row_h * S
    if note:
        y += 20 * S
        for ln in textwrap.wrap(note, 70):
            d.text((80 * S, y), ln, font=reg(22), fill=MUTED)
            y += 30 * S
    return y


slides = []

# 1. copertina
im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)
band(d)
if args.nome:
    d.text((80 * S, 230 * S), f"QGIS {ver}", font=bold(120), fill=INK)
    d.text((80 * S, 370 * S), args.nome, font=bold(120), fill=GREEN)
    d.text((84 * S, 510 * S), "in numeri", font=bold(64), fill=ORANGE)
else:
    d.text((80 * S, 300 * S), f"QGIS {ver}", font=bold(120), fill=INK)
    d.text((80 * S, 440 * S), "in numeri", font=bold(120), fill=GREEN)
d.text((84 * S, 610 * S), "Cosa racconta il changelog della nuova", font=reg(38), fill=INK2)
d.text((84 * S, 660 * S), "release, candidata Long Term Release", font=reg(38), fill=INK2)
for i, (k, v) in enumerate([("feature", over["Feature totali"]), ("categorie", over["Categorie"]),
                            ("sviluppatori", over["Sviluppatori distinti"])]):
    x = (84 + i * 300) * S
    d.text((x, 800 * S), v, font=bold(96), fill=ORANGE)
    d.text((x + 4 * S, 915 * S), k, font=reg(32), fill=INK2)
d.text((84 * S, H - 120 * S), "by @opendatasicilia · hfcqgis.opendatasicilia.it", font=reg(26), fill=MUTED)
cover_gif = im.copy()  # nella GIF le slide avanzano da sole: niente "Scorri"
d.text((84 * S, H - 200 * S), "Scorri  →", font=bold(36), fill=INK)
slides.append(im)

# 2. panoramica: stat tile
im, d, y = base(2, "PANORAMICA", "I numeri chiave")
pct = lambda s: re.search(r"\((\d+%)\)", s).group(1)
tiles = [
    (over["Feature totali"], "feature nuove"),
    (over["Categorie"], "categorie"),
    (over["Sviluppatori distinti"], "sviluppatori distinti"),
    (over["Finanziatori distinti"], "finanziatori distinti"),
    (pct(over["Feature con sviluppatore indicato"]), "feature con sviluppatore indicato"),
    (pct(over["Feature con finanziatore indicato"]), "feature con un finanziatore"),
]
tw, th, gap = 440, 250, 40
for i, (v, lab) in enumerate(tiles):
    x = (80 + (i % 2) * (tw + gap)) * S
    ty = y + 40 * S + (i // 2) * (th + gap) * S
    d.rounded_rectangle((x, ty, x + tw * S, ty + th * S), 18 * S, fill=CARD)
    d.text((x + 36 * S, ty + 36 * S), v, font=bold(96), fill=ORANGE if i == 5 else INK)
    for j, ln in enumerate(textwrap.wrap(lab, 22)):
        d.text((x + 38 * S, ty + (160 + j * 34) * S), ln, font=reg(28), fill=INK2)
slides.append(im)

# 3. categorie
im, d, y = base(3, "FEATURE PER CATEGORIA", "Processing in testa")
bars(d, y, cats, 400, 52, fs=24)
slides.append(im)

# 4. sviluppatori
im, d, y = base(4, "TOP SVILUPPATORI", "Chi ha scritto\nle novità")
bars(d, y, [(n, v, c if c != "—" else None) for n, v, c in devs], 360, 66, fs=26,
     note="Conteggio delle feature, esclusi i pacchetti di bug fix.")
slides.append(im)

# 5. aziende
im, d, y = base(5, "FEATURE PER AZIENDA", "Le aziende dietro\nil codice")
bars(d, y + 20 * S, comps, 360, 110, fs=30,
     note="Attribuzione tramite gli sviluppatori (mappatura manuale), esclusi i pacchetti di bug fix.")
slides.append(im)

# 6. finanziatori
im, d, y = base(6, "FINANZIATORI", "Chi ha finanziato\nlo sviluppo")
bars(d, y, funds, 470, 58, fs=22,
     note="Numero di feature finanziate. Alcune feature hanno più finanziatori.")
slides.append(im)

# 7. chiusura
im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)
band(d)
d.text((80 * S, 300 * S), "Approfondisci", font=bold(84), fill=INK)
items = [
    ("Changelog ufficiale", f"changelog.qgis.org/en/version/{ver}"),
    ("Le novità per espressioni e Field Calc", "hfcqgis.opendatasicilia.it"),
    ("Discussioni e domande", "github.com/opendatasicilia/HfcQGIS-md"),
]
yy = 470 * S
for t, u in items:
    d.rounded_rectangle((80 * S, yy, W - 80 * S, yy + 150 * S), 18 * S, fill=CARD)
    d.rectangle((80 * S, yy, 92 * S, yy + 150 * S), fill=GREEN)
    d.text((124 * S, yy + 32 * S), t, font=bold(34), fill=INK)
    d.text((124 * S, yy + 86 * S), u, font=reg(28), fill=INK2)
    yy += 180 * S
d.text((84 * S, H - 200 * S), "Ti è stato utile? Condividi!", font=bold(36), fill=ORANGE)
d.text((84 * S, H - 120 * S), "by @opendatasicilia · hfcqgis.opendatasicilia.it", font=reg(26), fill=MUTED)
slides.append(im)

slides = [s.resize((1080, 1350), Image.LANCZOS) for s in slides]
slides[0].save(out, save_all=True, append_images=slides[1:], resolution=72)
if args.gif:
    # GIF: slide ridotte, pausa su ogni slide e scorrimento orizzontale (swipe)
    gw, gh, hold, steps = 720, 900, 2600, 8
    small = [s.resize((gw, gh), Image.LANCZOS) for s in [cover_gif.resize((1080, 1350), Image.LANCZOS)] + slides[1:]]
    frames, durs = [], []
    for i, s in enumerate(small):
        frames.append(s)
        durs.append(hold + (600 if i == 0 else 0))
        nxt = small[(i + 1) % len(small)]
        for k in range(1, steps + 1):
            t = k / (steps + 1)
            off = int(gw * (1 - (1 - t) ** 3))  # ease-out
            f = Image.new("RGB", (gw, gh), BG)
            f.paste(s, (-off, 0))
            f.paste(nxt, (gw - off, 0))
            frames.append(f)
            durs.append(40)
    pal = [f.quantize(colors=128, method=Image.Quantize.MEDIANCUT) for f in frames]
    pal[0].save(args.gif, save_all=True, append_images=pal[1:], duration=durs, loop=0,
                optimize=True, disposal=1)
    print("gif", args.gif, len(frames), "frame")
if args.png:
    for i, s in enumerate(slides, 1):
        s.save(out.replace(".pdf", f"_{i}.png"))
print("ok", out, len(slides), "slide")
