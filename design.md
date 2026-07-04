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
tema: setup | metodologia | agentes | mcp | ferramentas | workflow | prompts | service-as-software | outros
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
- `docs/index.html` — feed com filtro por tema (CSS próprio via `static/tokens.css`, vanilla JS — sem dependência de CDN externo desde a redesign de 2026-07-04)
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

## Arquivos estáticos (`static/`)

**Propósito:** HTMLs versionados no git que precisam ser servidos pelo GitHub Pages mas não são gerados pelo `build-site.py`.

**Como funciona:** o `build-site.py` copia todos os arquivos de `static/` para `docs/` a cada rebuild. Isso garante que eles sobrevivam ao CI sem precisar remover `docs/` do `.gitignore`.

**Arquivos atuais:**
- `static/aprenda.html` — diagrama visual do sistema para aprendizado (explicação não-técnica)
- `static/gerenciador.html` — interface de gerenciamento com 4 seções (skills, KB, sync, config)

**Regra:** qualquer arquivo HTML que deve ficar permanentemente em `docs/` vai em `static/`, nunca criado diretamente em `docs/`.

---

## Gerenciador local (`static/gerenciador.html` + `scripts/server.py`)

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

---

## Regra de arquitetura — "aprender fazendo" (desde 2026-07-04)

O co-coach tem um objetivo explícito de ensinar Victor a usar Claude Code na prática (ver `requirements.md`). Isso impõe uma restrição a toda automação nova:

- **Hooks e configs locais (`.claude/settings.json`) são desencorajados** para lógica que Victor precisa confiar no dia a dia — eles vivem só na máquina onde foram configurados e exigem entender o conceito de "hook" para confiar que funcionam.
- **Preferir GitHub Actions** (roda no servidor, sem configuração local, já é o padrão usado por `ingest-link.yml`, `ingest-github-stars.yml` e `reindex-weekly.yml`).
- **Todo resultado de automação nova deve ganhar uma superfície visual** (card no feed, seção no `gerenciador.html`, diagrama no `aprenda.html`) — nunca ficar só em texto de terminal ou arquivo de config para Victor interpretar.
- Essa regra nasceu de uma discussão concreta: a ideia de rodar "gap analysis da KB" via hook de `SessionStart` foi descartada por violar essa regra; a alternativa (Action semanal + superfície visual) foi adotada no lugar.

---

## Direcionamento de aprendizado — tese Service-as-a-Software (desde 2026-07-04)

Victor assume o papel de Head de Growth e Produto na SMPL e precisa aplicar a tese Service-as-a-Software da Sequoia no trabalho. Isso muda como a KB e as skills de aprendizado (`co-coach-quiz`, `co-coach-digest`, `co-coach-review`) devem priorizar conteúdo:

- **Novo tema na KB:** `service-as-software` — conteúdo específico sobre a tese (agentes substituindo trabalho de serviço, pricing por outcome, produtos AI-first).
- **Curadoria com viés:** ao sugerir o que estudar (digest, quiz semanal), dar peso maior a conteúdo desse tema e a temas de suporte direto (`agentes`, `metodologia` aplicada a produto).
- **Critério de relevância:** ao decidir a `importancia` (1–5) de um link novo relacionado a agentes/produto AI-first, considerar a conexão com a tese como fator de nota mais alta.
