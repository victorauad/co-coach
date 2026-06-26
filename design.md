# design.md — co-coach

> Como o sistema está construído. Decisões técnicas, arquitetura e restrições.
> Atualizado em: 2026-06-25

---

## Arquitetura em 3 camadas

```
[ENTRADA]          [PROCESSAMENTO]        [SAÍDA]
iPhone / Stars  →  GitHub Actions      →  Feed mobile (GitHub Pages)
                   Claude Haiku API    →  kb/*.md
                   build-site.py       →  knowledge-base.json
skills/*.md     →  sync-skills.yml     →  .claude/skills/ nos repos
```

---

## Camada 1 — Knowledge Base (`kb/`)

**Tecnologia:** arquivos `.md` com frontmatter YAML

**Campos obrigatórios por arquivo:**
```yaml
titulo: string (máx 80 chars)
tema: setup | metodologia | agentes | mcp | ferramentas | workflow | prompts | outros
url: string
data: YYYY-MM-DD
importancia: 1-5
```

**Como conteúdo entra:**
1. Via iPhone → iOS Shortcut → Issue com label `add-link` → `ingest-link.yml` → `scripts/ingest.py`
2. Via GitHub Stars → `ingest-github-stars.yml` (toda segunda 09h UTC) → `scripts/ingest-github-stars.py`

**Modelo de IA:** `claude-haiku-4-5-20251001` (velocidade e custo — não usa Sonnet para ingestão em lote)

**Restrição:** conteúdo de URLs inacessíveis (paywall, login) não é indexado. YouTube usa `youtube-transcript-api`; sem transcrição, usa título e descrição.

---

## Camada 2 — Feed Mobile (`docs/`)

**Tecnologia:** HTML estático gerado por `scripts/build-site.py`

**Artefatos gerados:**
- `docs/index.html` — feed com filtro por tema (Tailwind CSS, vanilla JS)
- `docs/knowledge-base.json` — dump completo da KB em JSON (consumido pelo gerenciador e pelas skills de review)

**Publicação:** GitHub Pages, branch `main`, pasta `docs/`

**Importante:** `docs/` está no `.gitignore` — nunca commitar manualmente. O CI reconstrói automaticamente a cada push em `kb/**`.

**Rebuild:** `reindex-weekly.yml` toda segunda 08h UTC, ou via push em `kb/**` ou `scripts/**`

---

## Camada 3 — Hub de Skills (`skills/`)

**Estrutura de cada skill:**
```
skills/
└── co-coach-nome/
    └── SKILL.md    ← instruções que o Claude lê ao invocar /co-coach-nome
```

**Frontmatter do SKILL.md:**
```yaml
name: co-coach-nome
description: descrição em texto corrido (sem listas YAML — quebra o Claude Code)
```

**Restrição crítica:** campos com listas YAML no frontmatter (ex: `triggers:`) quebram a leitura da `description` silenciosamente no Claude Code. Tudo deve ser texto corrido em `description:`.

**Distribuição:** `sync-skills.yml` dispara a cada push em `skills/**` e envia todas as skills via GitHub API para os repos em `config/sync-targets.yml`. Não há controle granular por skill — todas vão para todos os repos listados.

**Repos registrados em `config/sync-targets.yml`:**
- `victorauad/iracing_analysis`
- `victorauad/alamtoco`

---

## Gerenciador local (`docs/gerenciador.html` + `scripts/server.py`)

**Tecnologia:** HTML + Tailwind + JavaScript (frontend) / Python stdlib (backend)

**Porta:** `8765` (localhost)

**Endpoints do servidor:**
- `GET /ping` — verifica se o servidor está vivo
- `GET /skills` — lista nomes das skills em `skills/*/`
- `GET /file?path=<rel>` — lê arquivo do repo
- `POST /file` — salva arquivo no repo (body: `{path, content}`)

**Restrição de segurança:** o servidor rejeita qualquer path fora da raiz do repo (`../` traversal bloqueado).

**Como iniciar:**
```bash
python3 scripts/server.py
# depois abrir docs/gerenciador.html no browser
```

---

## Fluxo de automação completo

```
1. Victor compartilha URL no iPhone
2. iOS Shortcut → POST GitHub Issues API (label: add-link)
3. ingest-link.yml detecta a Issue
4. scripts/ingest.py: fetch → Claude Haiku → kb/YYYY-MM-DD-slug.md
5. build-site.py → docs/index.html + docs/knowledge-base.json
6. git push automático pelo Actions
7. GitHub Pages publica → card aparece no feed (~2 min total)
```

---

## Decisões técnicas e seus motivos

| Decisão | Motivo |
|---|---|
| Claude Haiku para ingestão | 10x mais barato que Sonnet; suficiente para sumarização |
| Arquivos `.md` em vez de banco de dados | Zero infraestrutura; funciona com git nativo; editável por humano |
| `docs/` no `.gitignore` | Evita conflitos entre builds locais e CI |
| GitHub Pages em vez de Vercel/servidor | Gratuito, zero manutenção, integrado ao repositório |
| Servidor Python stdlib para gerenciador | Zero dependências externas para instalar |
| Todas as skills sincronizadas para todos os repos | Simplicidade > controle granular neste momento |
