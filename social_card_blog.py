"""Genera una social card 800x464 per i post del blog (stile hfc_blog_db_manager.png).

Richiede Pillow e i font Arial di Windows (C:/Windows/Fonts).
L'icona a destra (finestra web con </> e spunta) è specifica del post QGIS 4.4:
per altri post va ridisegnata nella sezione "icona".

Uso:
    python social_card_blog.py docs/img/card_social/hfc_blog_html_layout.png
    python social_card_blog.py out.png --etichetta "QGIS 4.6" --titolo "Riga 1" "Riga 2" \
        --sottotitolo "..." --nota "..."
"""
import argparse
from PIL import Image, ImageDraw, ImageFilter, ImageFont

p = argparse.ArgumentParser()
p.add_argument("out")
p.add_argument("--etichetta", default="QGIS 4.4")
p.add_argument("--titolo", nargs="+", default=["Elemento", "HTML"], help="una o due righe")
p.add_argument("--sottotitolo", default="torna nel layout di stampa")
p.add_argument("--nota", default="ora con QtWebEngine")
a = p.parse_args()
out = a.out
S = 2  # supersampling
W, H = 800 * S, 464 * S
F = "C:/Windows/Fonts/"
bold = lambda s: ImageFont.truetype(F + "arialbd.ttf", s * S)
reg = lambda s: ImageFont.truetype(F + "arial.ttf", s * S)

BG = (236, 236, 236, 255)
ORANGE = (245, 130, 31, 255)
GREEN_L = (141, 198, 63, 255)
GREEN = (106, 160, 50, 255)
GREEN_D = (79, 125, 50, 255)
DARK = (17, 17, 17, 255)
GREY = (90, 90, 90, 255)

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# ombra + card
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(shadow).rounded_rectangle((14 * S, 14 * S, 786 * S, 452 * S), 18 * S, fill=(0, 0, 0, 90))
img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(6 * S)))
d = ImageDraw.Draw(img)
d.rounded_rectangle((8 * S, 8 * S, 780 * S, 444 * S), 18 * S, fill=BG)

# testi
d.text((48 * S, 40 * S), a.etichetta, font=bold(28), fill=ORANGE)
for i, riga in enumerate(a.titolo[:2]):
    d.text((44 * S, (92 + 68 * i) * S), riga, font=bold(60), fill=DARK)
d.text((48 * S, 240 * S), a.sottotitolo, font=bold(25), fill=GREY)
d.text((48 * S, 284 * S), a.nota, font=reg(17), fill=GREY)
d.text((574 * S, 404 * S), "by @opendatasicilia", font=reg(18), fill=GREY)

# icona: finestra/pagina web
x0, y0, x1, y1 = 520 * S, 100 * S, 720 * S, 300 * S
d.rounded_rectangle((x0 + 6 * S, y0 + 8 * S, x1 + 6 * S, y1 + 8 * S), 14 * S, fill=(0, 0, 0, 35))
d.rounded_rectangle((x0, y0, x1, y1), 14 * S, fill=(255, 255, 255, 255), outline=GREEN_D, width=4 * S)
d.rounded_rectangle((x0, y0, x1, y0 + 36 * S), 14 * S, fill=GREEN_D)
d.rectangle((x0, y0 + 20 * S, x1, y0 + 36 * S), fill=GREEN_D)
for i, c in enumerate((ORANGE, GREEN_L, (255, 255, 255, 255))):
    cx = x0 + (22 + i * 20) * S
    d.ellipse((cx - 6 * S, y0 + 12 * S, cx + 6 * S, y0 + 24 * S), fill=c)
tag = "</>"
f = bold(64)
bb = d.textbbox((0, 0), tag, font=f)
tx = (x0 + x1) // 2 - (bb[2] - bb[0]) // 2 - bb[0]
ty = y0 + 36 * S + ((y1 - y0 - 36 * S) - (bb[3] - bb[1])) // 2 - bb[1]
d.text((tx, ty), tag, font=f, fill=GREEN)

# badge arancione con spunta
bx, by, r = 712 * S, 292 * S, 34 * S
d.ellipse((bx - r - 4 * S, by - r - 4 * S, bx + r + 4 * S, by + r + 4 * S), fill=(255, 255, 255, 255))
d.ellipse((bx - r, by - r, bx + r, by + r), fill=ORANGE)
d.line([(bx - 15 * S, by + 1 * S), (bx - 4 * S, by + 13 * S), (bx + 17 * S, by - 12 * S)],
       fill=(255, 255, 255, 255), width=8 * S, joint="curve")

img.resize((800, 464), Image.LANCZOS).save(out, optimize=True)
print("salvata", out)
