"""Genera il report riepilogativo (in italiano) da un export MD del changelog QGIS.

L'export si scarica dal pulsante "MD" della pagina
https://changelog.qgis.org/en/version/<versione>/ (zip con index.md + images/).

Uso:
    python report_changelog_qgis.py changelog_QGIS-4.4/index.md changelog_QGIS-4.4/qgis_4.4_summary.md 4.4

Le mappe COMPANY (sviluppatore -> azienda) e ALIAS (varianti dei nomi dei
finanziatori) vanno aggiornate a mano a ogni nuova release.
"""
import re
import sys
from collections import Counter, OrderedDict

src, dst, version = sys.argv[1], sys.argv[2], sys.argv[3]
text = open(src, encoding="utf-8").read()

COMPANY = {
    "Nyall Dawson": "North Road",
    "Mathieu Pellerin": "OPENGIS.ch",
    "Denis Rouzaud": "OPENGIS.ch",
    "Celia Buira": "OPENGIS.ch",
    "Germán Carrillo": "OPENGIS.ch",
    "Stefanos Natsis": "Lutra Consulting",
    "Martin Dobias": "Lutra Consulting",
    "Jan Caha": "Lutra Consulting",
    "Jean Felder": "Oslandia",
    "Julien Cabieces": "Oslandia",
    "Loïc Bartoletti": "Oslandia",
    "Jacky Volpes": "Oslandia",
    "Alessandro Pasotti": "QCooperative",
    "Alexander Bruy": "QCooperative",
}


ALIAS = {  # varianti dello stesso finanziatore -> nome unico
    "the switzerland qgis user group": "QGIS User Group Switzerland",
    "the qgis swiss user group": "QGIS User Group Switzerland",
    "qgis user group switzerland": "QGIS User Group Switzerland",
}


def clean(s):
    s = " ".join(s.split())
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)  # link -> testo
    s = s.replace("\\", "").strip().rstrip(".")
    return ALIAS.get(s.lower(), s)


features = []  # (categoria, titolo, dev, fondi)
category = None
blocks = re.split(r"\n(?=## |### Feature: )", text)
for b in blocks:
    if b.startswith("## "):
        category = b.splitlines()[0][3:].strip()
        continue
    if not b.startswith("### Feature: "):
        continue
    title = clean(b.splitlines()[0][len("### Feature: "):])
    dev = re.search(r"This feature was developed by (.*?)(?:\n\n|\Z)", b, re.S)
    fund = re.search(r"This feature was funded by (.*?)(?:\n\n|\Z)", b, re.S)
    funders = [clean(fund.group(1))] if fund else []
    # finanziamento collettivo indicato nel testo della descrizione
    coll = re.search(r"collective funding effort from:\s*\n(.*?)(?:\n\n|\Z)", b, re.S)
    if coll:
        funders += [clean(x) for x in coll.group(1).splitlines() if clean(x)]
    features.append((category, title, clean(dev.group(1)) if dev else None,
                     funders))

n = len(features)
cats = OrderedDict()
for f in features:
    cats.setdefault(f[0], []).append(f)
devs_all = {f[2] for f in features if f[2]}
# finanziatori: unifica varianti che differiscono solo per maiuscole
fund_counter, fund_name = Counter(), {}
for f in features:
    for fu in f[3]:
        k = fu.lower()
        fund_name.setdefault(k, fu[0].upper() + fu[1:])
        fund_counter[k] += 1

is_bugfix = lambda f: f[1].startswith("Bug fixes by")
dev_counter = Counter(f[2] for f in features if f[2] and not is_bugfix(f))
order = {}
for i, f in enumerate(features):
    if f[2]:
        order.setdefault(f[2], i)
comp_counter = Counter()
for d, c in dev_counter.items():
    if d in COMPANY:
        comp_counter[COMPANY[d]] += c

with_dev = sum(1 for f in features if f[2])
with_fund = sum(1 for f in features if f[3])
out = [f"# Report QGIS {version}", "", f"Riepilogo generato dal changelog QGIS {version}.", "",
       "## Panoramica", "",
       f"- **Feature totali:** {n}",
       f"- **Categorie:** {len(cats)}",
       f"- **Sviluppatori distinti:** {len(devs_all)}",
       f"- **Finanziatori distinti:** {len(fund_counter)}",
       f"- **Feature con sviluppatore indicato:** {with_dev}/{n} ({round(100 * with_dev / n)}%)",
       f"- **Feature con finanziatore indicato:** {with_fund}/{n} ({round(100 * with_fund / n)}%)",
       "", "## Feature per categoria", "", "| Categoria | Feature | |", "|---|--:|:--|"]
cat_sorted = sorted(cats.items(), key=lambda kv: -len(kv[1]))
mx = max(len(v) for v in cats.values())
for c, v in cat_sorted:
    w = round(24 * len(v) / mx)
    out.append(f"| {c} | {len(v)} | `{'█' * w}{'·' * (24 - w)}` |")
out += ["", "## Top sviluppatori", "", "| # | Sviluppatore | Feature | Azienda |", "|--:|---|--:|---|"]
for i, (d, c) in enumerate(sorted(dev_counter.items(), key=lambda kv: (-kv[1], order[kv[0]]))[:15], 1):
    out.append(f"| {i} | {d} | {c} | {COMPANY.get(d, '—')} |")
out += ["", "## Feature per azienda (via mappatura sviluppatori)", "", "| Azienda | Feature |", "|---|--:|"]
for comp, c in comp_counter.most_common():
    out.append(f"| {comp} | {c} |")
out += ["", "## Finanziatori", "", "| Finanziatore | Feature |", "|---|--:|"]
for k, c in fund_counter.most_common():
    out.append(f"| {fund_name[k]} | {c} |")
out += ["", "## Elenco completo delle feature"]
for c, v in cat_sorted:
    out += ["", f"### {c}", ""]
    for _, title, dev, fund in v:
        line = f"- **{title}** — dev: *{dev or '—'}*"
        if fund:
            line += f" · fondi: *{', '.join(fund)}*"
        out.append(line)
open(dst, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"{n} feature, {len(cats)} categorie -> {dst}")
