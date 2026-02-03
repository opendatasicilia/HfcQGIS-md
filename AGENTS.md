# Repository Guidelines

## Project Structure & Module Organization
- `docs/` contains the documentation source (Markdown pages, images in `docs/img/`, styles in `docs/stylesheets/`, and theme overrides in `docs/theme_override/`).
- `mkdocs.yml` is the site configuration and navigation for the MkDocs Material build.
- Helper scripts live at the repo root (e.g., `file_con_gruppi_funzioni_field_calc.py`, `nro_espressioni_x_gruppi_field_calc.py`).
- Misc project notes are in `LOG.md` and licenses in `LICENSE.md` / `docs/LICENSE_my.md`.

## Build, Test, and Development Commands
- `python -m venv .venv && source .venv/bin/activate` creates/activates a local venv.
- `pip install -r requirements-mkdocs.txt` installs site build dependencies.
- `mkdocs serve` runs the docs locally with live reload.
- `mkdocs build` generates the static site in `site/` (default MkDocs output).

## Coding Style & Naming Conventions
- Markdown content lives under `docs/` and often uses YAML front matter (see `docs/pull-request.md`).
- Keep file and folder names lowercase with underscores where needed (example: `docs/gr_funzioni/stringhe_di_testo/`).
- Follow existing indentation: 2 spaces in YAML (`mkdocs.yml`) and 4 spaces in Python scripts.
- Prefer concise, instructional prose; include screenshots or GIFs in `docs/img/` when a step is visual.

## Testing Guidelines
- There is no dedicated test suite for content. If you add Python utilities, you may use `pytest` (listed in `requirements-mkdocs.txt`) and keep tests alongside scripts or under a new `tests/` directory.

## Commit & Pull Request Guidelines
- Recent commits use a simple prefix style such as `fix:` or `add:` (Italian descriptions are common). Match this pattern for consistency.
- PRs should describe the doc pages touched (paths under `docs/`) and include screenshots for visual/layout changes.
- Link related issues or QGIS references when updating release notes or function documentation.

## Security & Configuration Tips
- Avoid committing generated `site/` output; treat it as build artifact unless explicitly requested.
- Keep external links and embedded assets stable; prefer repository-hosted images in `docs/img/`.
