#!/usr/bin/env python3
"""
Gera o site estático (docs/index.html) a partir de múltiplas pastas do repo.
Roda automaticamente após cada ingestão e semanalmente.
"""

import os
import re
import json
import shutil
import datetime
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(exist_ok=True)

# Todo o conteúdo vive em kb/ (raiz = cards de links; subpastas = guias, templates, trilhas)
KB_DIR = Path("kb")

# Arquivos que são índices/navegação, não conteúdo
SKIP_FILES = {"README.md"}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extrai o frontmatter YAML simples e o corpo do markdown."""
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip()
            body = parts[2].strip()
    return meta, body


def extract_title(body: str, fallback: str) -> str:
    """Extrai o primeiro # H1 do markdown como título."""
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def extract_section(body: str, heading: str) -> str:
    """Extrai o texto de uma seção markdown pelo título."""
    pattern = rf"## {re.escape(heading)}\n+(.*?)(?=\n## |\Z)"
    match = re.search(pattern, body, re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_bullets_from_body(body: str) -> list[str]:
    """Extrai até 3 itens de lista do corpo do arquivo."""
    lines = [l.lstrip("*-• ").strip() for l in body.splitlines() if re.match(r"^\s*[-*•]\s+", l)]
    return [l for l in lines if l][:3]


def first_paragraph(body: str) -> str:
    """Retorna o primeiro parágrafo de texto simples (sem markdown)."""
    for line in body.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith(">") and not line.startswith("|"):
            return re.sub(r"\*+|`", "", line)[:200]
    return ""


def load_cards() -> list[dict]:
    cards = []
    for md_file in sorted(KB_DIR.rglob("*.md"), reverse=True):
        # Pula índices, templates de scaffolding (_*.md) e o SKILL.md de exemplo
        if md_file.name in SKIP_FILES or md_file.name.startswith("_") or md_file.name == "SKILL.md":
            continue
        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)

        # Todo arquivo de conteúdo em kb/ deve ter frontmatter; fallback para os campos ausentes
        titulo = meta.get("titulo") or extract_title(body, md_file.stem.replace("-", " ").title())
        tema = meta.get("tema", "outros")
        tipo = meta.get("tipo", "card")
        url = meta.get("url", "#")
        data = meta.get("data", "")
        fonte = meta.get("fonte", "")
        github_repo = meta.get("github_repo", "")
        github_stars = meta.get("github_stars", "")

        bullets_raw = extract_section(body, "Resumo")
        bullets = [l.lstrip("- ").strip() for l in bullets_raw.splitlines() if l.strip().startswith("-")]
        if not bullets:
            bullets = extract_bullets_from_body(body)
        importancia = extract_section(body, "Por que isso importa") or first_paragraph(body)

        if not bullets:
            bullets = [first_paragraph(body)] if first_paragraph(body) else ["Ver conteúdo completo no repo"]

        cards.append({
            "titulo": titulo,
            "tema": tema,
            "tipo": tipo,
            "url": url,
            "data": data,
            "bullets": bullets,
            "importancia": importancia,
            "filename": md_file.name,
            "pasta": md_file.parent.name,
            "fonte": fonte,
            "github_repo": github_repo,
            "github_stars": github_stars,
        })
    return cards


def load_proficiency() -> dict:
    """Lê static/proficiency.json (fonte de verdade); retorna {} se não existir."""
    p = Path("static") / "proficiency.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


TEMA_CORES = {
    "setup": "#4CAF50",
    "metodologia": "#2196F3",
    "agentes": "#9C27B0",
    "mcp": "#FF9800",
    "ferramentas": "#00BCD4",
    "workflow": "#F44336",
    "prompts": "#FFEB3B",
    "outros": "#757575",
}


STATUS_BADGE = {
    "novo":   ("🆕", "#555555"),
    "visto":  ("👁", "#2196F3"),
    "domina": ("✓",  "#4CAF50"),
}


def card_html(card: dict) -> str:
    bullets_html = "".join(f"<li>{b}</li>" for b in card["bullets"])
    cor = TEMA_CORES.get(card["tema"], "#757575")
    data_str = f'<span class="data">{card["data"]}</span>' if card["data"] else f'<span class="data pasta">{card["pasta"]}</span>'
    status = card.get("status_proficiency", "novo")
    badge_icon, badge_color = STATUS_BADGE.get(status, ("🆕", "#555555"))
    badge_html = f'<span class="badge-status" style="background:{badge_color}" title="{status}">{badge_icon}</span>'
    importancia_html = (
        f'<div class="importancia"><strong>Por que importa:</strong> {card["importancia"]}</div>'
        if card["importancia"] else ""
    )
    return f"""
<article class="card" data-tema="{card['tema']}" data-titulo="{card['titulo'].lower()}" data-importancia="{card['importancia'].lower()}">
  <div class="card-header">
    <span class="tag" style="background:{cor}">{card['tema']}</span>
    <div class="card-header-right">{data_str}{badge_html}</div>
  </div>
  <h2><a href="{card['url']}" target="_blank" rel="noopener">{card['titulo']}</a></h2>
  <ul>{bullets_html}</ul>
  {importancia_html}
</article>"""


def proficiency_panel_html(prof: dict) -> str:
    temas_data = prof.get("temas", {})
    if not temas_data:
        return ""
    linhas = []
    for tema, dados in sorted(temas_data.items(), key=lambda x: -x[1].get("score", 0)):
        score = dados.get("score", 0)
        blocos = "█" * (score // 10) + "░" * (10 - score // 10)
        exposicao = dados.get("exposicao", 0)
        qa = dados.get("quiz_acertos", 0)
        qt = dados.get("quiz_total", 0)
        quiz_str = f"quiz: {qa}/{qt}" if qt > 0 else "sem quiz"
        cor = TEMA_CORES.get(tema, "#757575")
        fill_pct = score
        linhas.append(
            f'<div class="prof-barra">'
            f'<span class="prof-nome" style="color:{cor}">{tema}</span>'
            f'<div class="prof-track"><div class="prof-fill" style="width:{fill_pct}%;background:{cor}"></div></div>'
            f'<span class="prof-pct">{score}%</span>'
            f'<span class="prof-detalhe">visto {exposicao}x · {quiz_str}</span>'
            f'</div>'
        )
    ultima = prof.get("ultima_atualizacao", "")
    if ultima:
        try:
            ultima_fmt = datetime.datetime.strptime(ultima, "%Y-%m-%d").strftime("%d/%m/%Y")
        except ValueError:
            ultima_fmt = ultima
    else:
        ultima_fmt = ""
    updated_str = f'<span class="prof-updated">Último quiz em {ultima_fmt}</span>' if ultima_fmt else ""
    return f"""<section class="proficiency-panel">
  <h2>Progresso por Tema <button class="prof-toggle" onclick="toggleProf()">▼</button></h2>
  {updated_str}
  <div id="prof-content">{''.join(linhas)}</div>
  <p class="prof-hint">Use <code>/co-coach-quiz</code> no Claude Code para fazer um quiz e atualizar os scores.</p>
</section>"""


def build_html(cards: list[dict], prof: dict = None) -> str:
    if prof is None:
        prof = {}
    # Injeta status de proficiência em cada card
    cards_prof = prof.get("cards", {})
    for c in cards:
        status = cards_prof.get(c["filename"], {}).get("status", "novo")
        c["status_proficiency"] = status

    cards_html = "\n".join(card_html(c) for c in cards)
    temas = sorted(set(c["tema"] for c in cards))
    tema_buttons = "".join(
        f'<button class="filtro-btn" data-tema="{t}" style="border-color:{TEMA_CORES.get(t,"#757575")}">{t}</button>'
        for t in temas
    )
    total = len(cards)
    updated = datetime.date.today().strftime("%d/%m/%Y")

    # Contagem por tema para o footer
    tema_counts = {}
    for c in cards:
        tema_counts[c["tema"]] = tema_counts.get(c["tema"], 0) + 1
    tema_stats = " · ".join(
        f'<span style="color:{TEMA_CORES.get(t,"#757575")}">{t} {n}</span>'
        for t, n in sorted(tema_counts.items(), key=lambda x: -x[1])
    )

    cards_json = json.dumps(cards, ensure_ascii=False)
    panel_html = proficiency_panel_html(prof)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Claude Code Growth — Feed</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header>
  <div class="header-top">
    <h1>Claude Code Growth</h1>
    <a href="gerenciador.html" class="header-nav-link">⚙ Gerenciador</a>
  </div>
  <p class="subtitle">{total} conteúdos indexados · Atualizado em {updated}</p>
</header>

{panel_html}

<div class="context-box">
  <label for="context-input">O que estou fazendo agora:</label>
  <input id="context-input" type="text" placeholder="Ex: estruturando meu CLAUDE.md, pipeline de BigQuery, criando agentes..." />
  <p class="context-hint">Digite para ver os conteúdos mais relevantes primeiro.</p>
</div>

<div class="filtros">
  <button class="filtro-btn active" data-tema="todos">todos</button>
  {tema_buttons}
</div>

<main id="feed">
{cards_html}
</main>

<footer>
  <p>Alimentado por <a href="https://github.com/victorauad/co-coach">co-coach</a> · Rebuild: {updated} · {total} cards</p>
  <p class="footer-temas">{tema_stats}</p>
  <p style="margin-top:0.5rem"><a href="aprenda.html">📖 Como funciona</a> · <a href="gerenciador.html">⚙️ Gerenciador</a></p>
</footer>

<script>
const cards = {cards_json};
let temaAtivo = 'todos';

function score(card, query) {{
  if (!query) return 0;
  const q = query.toLowerCase();
  const campos = [card.titulo, card.tema, card.importancia, ...card.bullets].join(' ').toLowerCase();
  return (campos.match(new RegExp(q.split(' ').filter(Boolean).join('|'), 'g')) || []).length;
}}

function render() {{
  const query = document.getElementById('context-input').value;
  const articles = document.querySelectorAll('.card');

  let visiveis = Array.from(articles).filter(el => {{
    const tema = el.dataset.tema;
    return temaAtivo === 'todos' || tema === temaAtivo;
  }});

  const ocultos = Array.from(articles).filter(el => !visiveis.includes(el));
  ocultos.forEach(el => el.style.display = 'none');

  if (query.trim()) {{
    visiveis.sort((a, b) => {{
      const cardA = cards.find(c => c.titulo.toLowerCase() === a.dataset.titulo);
      const cardB = cards.find(c => c.titulo.toLowerCase() === b.dataset.titulo);
      return score(cardB, query) - score(cardA, query);
    }});
  }}

  const feed = document.getElementById('feed');
  visiveis.forEach(el => {{
    el.style.display = '';
    feed.appendChild(el);
  }});
}}

function toggleProf() {{
  const el = document.getElementById('prof-content');
  const btn = document.querySelector('.prof-toggle');
  if (el) {{ el.style.display = el.style.display === 'none' ? '' : 'none'; btn.textContent = el.style.display === 'none' ? '▶' : '▼'; }}
}}

document.getElementById('context-input').addEventListener('input', render);

document.querySelectorAll('.filtro-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.filtro-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    temaAtivo = btn.dataset.tema;
    render();
  }});
}});
</script>
</body>
</html>"""


def build_css() -> str:
    return """@import url("tokens.css");

:root { font-size: 16px; }

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  max-width: 720px;
  margin: 0 auto;
  padding: 1rem;
}

header { padding: var(--space-6) 0 var(--space-4); }
.header-top { display: flex; align-items: center; justify-content: space-between; gap: var(--space-3); }
header h1 { font-size: var(--text-xl); margin: 0; }
.header-nav-link {
  color: var(--muted); border: 1px solid var(--border); border-radius: var(--radius-sm);
  padding: 0.3rem 0.7rem; font-size: var(--text-xs); text-decoration: none; flex-shrink: 0;
}
.header-nav-link:hover { color: var(--accent); border-color: var(--accent); }
.subtitle { color: var(--muted); font-size: var(--text-sm); margin-top: var(--space-1); }

.context-box {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: var(--space-4);
  margin: var(--space-4) 0;
}

.context-box label { display: block; font-size: var(--text-sm); color: var(--muted); margin-bottom: var(--space-2); }

#context-input {
  width: 100%;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  color: var(--text);
  font-size: var(--text-base);
  padding: 0.6rem 0.8rem;
}

#context-input:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
.context-hint { font-size: var(--text-xs); color: var(--muted); margin-top: var(--space-2); }

.filtros { display: flex; flex-wrap: wrap; gap: var(--space-2); margin: var(--space-4) 0; }

.filtro-btn {
  background: transparent;
  border: 1px solid var(--border);
  border-radius: var(--radius-pill);
  color: var(--text);
  cursor: pointer;
  font-size: var(--text-sm);
  padding: 0.3rem 0.8rem;
}

.filtro-btn.active, .filtro-btn:hover { background: var(--border); }
.filtro-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }

.card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.2rem;
  margin-bottom: var(--space-4);
}

.card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3); }

.tag { color: #000; text-transform: uppercase; }

.data { color: var(--muted); font-size: var(--text-xs); }

.card h2 { font-size: var(--text-base); margin-bottom: var(--space-3); }
.card h2 a { color: var(--accent); text-decoration: none; }
.card h2 a:hover, .card h2 a:focus-visible { text-decoration: underline; }
.card h2 a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

.card ul { padding-left: 1.2rem; font-size: var(--text-sm); line-height: 1.6; color: var(--muted); }
.card ul li { margin-bottom: var(--space-1); }

.importancia {
  border-top: 1px solid var(--border);
  font-size: var(--text-sm);
  margin-top: var(--space-3);
  padding-top: var(--space-3);
  color: var(--muted);
}

.importancia strong { color: var(--text); }

footer { color: var(--muted); font-size: var(--text-xs); padding: var(--space-8) 0 var(--space-4); text-align: center; }
footer a { color: var(--accent); }
footer a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.footer-temas { margin-top: var(--space-2); font-size: var(--text-xs); }

.proficiency-panel {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: var(--space-4);
  margin: var(--space-4) 0;
}

.proficiency-panel h2 { font-size: var(--text-lg); margin-bottom: var(--space-3); display: flex; align-items: center; gap: var(--space-2); }
.prof-toggle { background: transparent; border: 1px solid var(--border); border-radius: var(--radius-sm); color: var(--muted); cursor: pointer; font-size: var(--text-xs); padding: 0.1rem 0.4rem; }
.prof-toggle:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
.prof-updated { display: block; font-size: var(--text-xs); color: var(--muted); margin-bottom: var(--space-2); }

.prof-barra {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-1);
  font-size: var(--text-sm);
}

.prof-nome { width: 90px; font-weight: 600; flex-shrink: 0; }
.prof-track { flex: 1; background: var(--border); border-radius: var(--radius-sm); height: 8px; overflow: hidden; }
.prof-fill { height: 100%; border-radius: var(--radius-sm); transition: width 0.3s; }
.prof-pct { width: 36px; text-align: right; flex-shrink: 0; color: var(--text); font-weight: 600; }
.prof-detalhe { color: var(--muted); font-size: var(--text-xs); flex-shrink: 0; }
.prof-hint { font-size: var(--text-xs); color: var(--muted); margin-top: var(--space-3); }
.prof-hint code { background: var(--border); border-radius: var(--radius-sm); padding: 0.1rem 0.3rem; font-size: var(--text-xs); }

.card-header-right { display: flex; align-items: center; gap: var(--space-2); }

.badge-status {
  border-radius: 50%;
  width: 22px;
  height: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: var(--text-xs);
  flex-shrink: 0;
}

@media (prefers-reduced-motion: reduce) {
  .prof-fill { transition: none; }
}
"""


SKILL_CATEGORIES = {
    "Produtividade & Metodologia": [
        "co-coach-builder", "co-coach-handoff", "co-coach-list",
        "co-coach-mermaid", "co-coach-obsidian", "co-coach-quiz",
        "co-coach-repomix", "co-coach-review", "co-coach-sdd",
        "co-coach-setup", "co-coach-start", "co-coach-support", "co-coach-ui", "co-coach-wizard",
    ],
    "Marketing & Growth": [
        "co-coach-ads", "co-coach-analytics", "co-coach-competitor",
        "co-coach-content", "co-coach-copy", "co-coach-market",
        "co-coach-marketing-plan", "co-coach-research", "co-coach-seo", "co-coach-social",
    ],
    "Dados & Automação": [
        "co-coach-bigquery", "co-coach-digest", "co-coach-xlsx",
    ],
    "Documentos & Apresentações": [
        "co-coach-docx", "co-coach-pdf", "co-coach-pptx",
    ],
    "Ferramentas & Integrações": [
        "co-coach-dify", "co-coach-flowise", "co-coach-notebooklm", "co-coach-onyx",
    ],
}


def build_skills_readme():
    skills_dir = Path(".claude/skills")
    if not skills_dir.exists():
        return

    # Extrai description de cada SKILL.md lendo só até achar a linha
    descriptions = {}
    for skill_file in skills_dir.glob("*/SKILL.md"):
        skill_name = skill_file.parent.name
        for line in skill_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("description:"):
                raw = line[len("description:"):].strip().strip('"')
                # Primeira frase apenas (até o primeiro ponto final ou 120 chars)
                short = raw.split(". ")[0].rstrip(".")
                descriptions[skill_name] = short[:120]
                break

    lines = [
        "# Skills do co-coach",
        "",
        "Skills instaláveis do Claude Code. Cada pasta tem um `SKILL.md` com frontmatter (`name`, `description`) e instruções.",
        "",
        "> **Gerado automaticamente** por `scripts/build-site.py`. Não edite manualmente — as alterações serão sobrescritas no próximo build.",
        "",
        "## Convenção de nomenclatura",
        "",
        "Toda skill segue o padrão **`co-coach-<palavra>`**. Ao criar uma nova, use a `co-coach-builder`.",
        "",
        "---",
        "",
    ]

    # Skills sem categoria conhecida vão para "Outras"
    categorized = {s for skills in SKILL_CATEGORIES.values() for s in skills}
    uncategorized = [s for s in descriptions if s not in categorized]

    categories = dict(SKILL_CATEGORIES)
    if uncategorized:
        categories["Outras"] = sorted(uncategorized)

    for category, skill_names in categories.items():
        lines.append(f"## {category}")
        lines.append("")
        lines.append("| Skill | Função |")
        lines.append("|-------|--------|")
        for skill_name in skill_names:
            desc = descriptions.get(skill_name, "—")
            lines.append(f"| `{skill_name}` | {desc} |")
        lines.append("")

    lines += [
        "---",
        "",
        "## Como as skills são distribuídas",
        "",
        "O workflow `.github/workflows/sync-skills.yml` copia cada pasta de `.claude/skills/` para o `.claude/skills/` dos repos registrados em `config/sync-targets.yml`.",
        "",
    ]

    (skills_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f".claude/skills/README.md gerado ({len(descriptions)} skills)")


def main():
    cards = load_cards()
    print(f"Encontrados {len(cards)} cards em kb/")

    prof = load_proficiency()
    html = build_html(cards, prof)
    css = build_css()

    (DOCS_DIR / "index.html").write_text(html, encoding="utf-8")
    (DOCS_DIR / "style.css").write_text(css, encoding="utf-8")

    # robots.txt para não indexar no Google
    (DOCS_DIR / "robots.txt").write_text("User-agent: *\nDisallow: /\n")

    # Gera knowledge-base.json para consumo pelas skills
    kb_fields = ["titulo", "tema", "tipo", "url", "data", "bullets", "importancia", "fonte", "github_repo", "github_stars"]
    kb_entries = [{k: c[k] for k in kb_fields} for c in cards]
    (DOCS_DIR / "knowledge-base.json").write_text(
        json.dumps(kb_entries, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Copia arquivos estáticos versionados (static/) para docs/
    # config.local.js é gitignored e contém o PAT — nunca deve ir para docs/
    STATIC_EXCLUDE = {"config.local.js"}
    static_dir = Path("static")
    if static_dir.exists():
        copied = []
        for f in static_dir.iterdir():
            if f.name not in STATIC_EXCLUDE:
                shutil.copy2(f, DOCS_DIR / f.name)
                copied.append(f.name)
        print(f"Arquivos estáticos copiados: {copied}")

    build_skills_readme()

    print(f"Site gerado em docs/ ({len(cards)} cards)")
    print(f"Knowledge base exportada: docs/knowledge-base.json ({len(kb_entries)} entradas)")


if __name__ == "__main__":
    main()
