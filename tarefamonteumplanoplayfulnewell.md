# Handoff — co-coach: Skills com Knowledge Base

**Data:** 20/06/2026  
**Repo:** `victorauad/claude-code-growth` (apelido interno: co-coach)  
**Branch de desenvolvimento:** `claude/zen-ptolemy-aj6ytm` (já mergeado em `main` — próxima tarefa vai para um branch novo)  
**GitHub Pages:** `https://victorauad.github.io/claude-code-growth`

---

## Visão do projeto

O `claude-code-growth` é um sistema em três camadas:

1. **Knowledge base viva** — conteúdo indexado automaticamente via: (a) link enviado por GitHub Issue (iOS Shortcut ou manual), (b) repos do GitHub que o usuário estrelou (workflow semanal). Tudo fica em `07-inbox/` como arquivos `.md` com frontmatter.

2. **Feed mobile** — site estático em GitHub Pages gerado por `scripts/build-site.py`. Mostra os cards com filtro por tema e campo de contexto "o que estou fazendo agora".

3. **Skills instaláveis em outros projetos** — arquivos `SKILL.md` em `skills/`. São copiados para `.claude/skills/` de outros repos via `scripts/install-skills.sh` ou via GitHub Action `install-skills-remote.yml`.

**A peça que falta (esta tarefa):** as skills hoje são auditores estáticos — avaliam o projeto atual mas não consultam a knowledge base. Quando invocadas, devem também trazer recomendações da KB: "seu CLAUDE.md está em 6/10 — e da sua base de conhecimento, esses 3 recursos são relevantes para o que você está fazendo".

---

## Estado atual — o que já existe e funciona

### Estrutura de pastas relevante

```
claude-code-growth/
├── 07-inbox/                    # conteúdo indexado (30+ arquivos .md com frontmatter)
├── scripts/
│   ├── build-site.py            # gera docs/index.html + docs/style.css + docs/robots.txt
│   ├── ingest.py                # fetch + sumarização via Claude Haiku → salva em 07-inbox/
│   └── ingest-github-stars.py  # busca repos estrelados e indexa READMEs
├── skills/
│   ├── coach-claude-code/SKILL.md
│   ├── setup-review/SKILL.md
│   └── bigquery-workflow/SKILL.md
├── docs/
│   ├── index.html               # gerado automaticamente
│   ├── style.css                # gerado automaticamente
│   └── robots.txt               # gerado automaticamente
├── .github/workflows/
│   ├── ingest-link.yml          # dispara ao Issue receber label "add-link"
│   ├── ingest-github-stars.yml  # roda toda segunda 09h UTC + workflow_dispatch
│   ├── reindex-weekly.yml       # rebuild do site toda segunda 08h UTC
│   └── install-skills-remote.yml
└── .claude/settings.json        # SessionStart hook para memória global na web
```

### Como os cards são gerados (`scripts/build-site.py`)

A função `load_cards()` lê arquivos `.md` de múltiplas pastas. Para arquivos com frontmatter YAML (os do `07-inbox/`), extrai os campos diretamente. Para arquivos sem frontmatter (pastas de documentação), infere título e bullets do markdown.

Cada card tem:
```python
{
    "titulo": str,
    "tema": str,       # setup | metodologia | agentes | mcp | ferramentas | workflow | prompts | outros
    "url": str,
    "data": str,       # YYYY-MM-DD
    "bullets": list,   # 3 pontos
    "importancia": str,
    "filename": str,
    "pasta": str,
}
```

Alguns cards do `07-inbox/` têm campos extras no frontmatter:
- `fonte: github-stars` — veio de repo estrelado
- `github_stars: 1234`
- `github_repo: owner/repo`

---

## O que esta tarefa precisa fazer

### Parte 1 — `scripts/build-site.py`: gerar `docs/knowledge-base.json`

No final da função `main()`, após gerar o `index.html`, adicionar:

```python
# Gera knowledge-base.json para consumo pelas skills
kb_entries = []
for card in cards:
    entry = {
        "titulo": card["titulo"],
        "tema": card["tema"],
        "url": card["url"],
        "data": card["data"],
        "bullets": card["bullets"],
        "importancia": card["importancia"],
    }
    # inclui campos extras se presentes no frontmatter original
    # (fonte, github_repo, github_stars já estão no card se vieram do frontmatter)
    kb_entries.append(entry)

(DOCS_DIR / "knowledge-base.json").write_text(
    json.dumps(kb_entries, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
print(f"Knowledge base exportada: docs/knowledge-base.json ({len(kb_entries)} entradas)")
```

**Nota:** os campos `fonte`, `github_repo`, `github_stars` estão no frontmatter dos arquivos de `07-inbox/` mas a função `load_cards()` atual não os captura. Você precisará ou (a) adicionar esses campos ao dict do card no `load_cards()`, ou (b) relê-los do frontmatter separadamente. A opção mais simples é expandir o bloco `if meta:` dentro de `load_cards()` para capturar campos extras:

```python
# dentro do bloco "if meta:" em load_cards()
fonte = meta.get("fonte", "")
github_repo = meta.get("github_repo", "")
github_stars = meta.get("github_stars", "")
```

E adicionar ao dict do card:
```python
cards.append({
    ...,  # campos existentes
    "fonte": fonte,
    "github_repo": github_repo,
    "github_stars": github_stars,
})
```

**Resultado esperado:** `https://victorauad.github.io/claude-code-growth/knowledge-base.json` — array JSON com todos os cards indexados, acessível publicamente.

---

### Parte 2 — `skills/coach-claude-code/SKILL.md`: adicionar Fase 2 (KB)

Após o passo 5 atual ("Retornar o relatório"), adicionar uma nova seção:

```markdown
### 6. Consultar a Knowledge Base do co-coach

Após gerar o relatório de score, faça:

1. Use `WebFetch` para buscar `https://victorauad.github.io/claude-code-growth/knowledge-base.json`
   - Se não tiver acesso a WebFetch, use `Bash(curl -s https://victorauad.github.io/claude-code-growth/knowledge-base.json)`
2. Com base no CLAUDE.md lido e no tipo de projeto, filtre os itens da KB que são mais relevantes.
   - Critério de relevância: correspondência de palavras-chave entre o tema/stack do projeto e os campos `titulo`, `bullets`, `importancia` dos itens da KB.
3. Selecione até 5 itens mais relevantes.
4. Adicione ao final do relatório a seção abaixo.

### Da sua Knowledge Base
> Recursos do co-coach relevantes para este projeto:

- **[titulo]** `[tema]` — [1 frase explicando por que é relevante para ESTE projeto específico] → [url]
- ...

> Se a KB estiver vazia ou inacessível, omita esta seção sem mencionar o erro.
```

Também atualizar a descrição no frontmatter do SKILL.md para refletir a nova capacidade:
```yaml
description: Avalia a qualidade do contexto do projeto (CLAUDE.md, skills, settings) com score 0–10 e sugestões concretas. Também consulta a knowledge base do co-coach e traz recursos relevantes para o projeto. Use quando pedir "/coach", "avalie meu contexto" ou "o que está faltando no meu setup".
```

---

### Parte 3 — `skills/setup-review/SKILL.md`: adicionar seção de KB

No final do SKILL.md (após o "Formato do relatório"), adicionar:

```markdown
### 7. Consultar Knowledge Base para ferramentas de setup

Após o relatório de auditoria:

1. Busque `https://victorauad.github.io/claude-code-growth/knowledge-base.json` via WebFetch ou Bash(curl)
2. Filtre itens com `tema` igual a `ferramentas` ou `setup`
3. Adicione ao relatório:

### Ferramentas e recursos da KB que podem ajudar
- **[titulo]** — [por que é útil para o setup deste projeto] → [url]

> Omita se a KB estiver inacessível.
```

---

### Parte 4 — Re-instalar skills no `iracing_analysis`

Após atualizar os SKILL.md, as skills precisam ser re-copiadas para o `iracing_analysis`. Isso é feito via GitHub Action:

- Actions → "Install Skills in Remote Repo" → Run workflow → target_repo: `victorauad/iracing_analysis`

---

## Ordem de execução

| Passo | Arquivo | Ação |
|---|---|---|
| 1 | `scripts/build-site.py` | Capturar `fonte`, `github_repo`, `github_stars` no `load_cards()` e gerar `docs/knowledge-base.json` no `main()` |
| 2 | terminal | `python scripts/build-site.py` — validar que `docs/knowledge-base.json` foi gerado com ≥10 entradas |
| 3 | `skills/coach-claude-code/SKILL.md` | Adicionar Fase 2 (consulta KB + seção "Da sua Knowledge Base") |
| 4 | `skills/setup-review/SKILL.md` | Adicionar seção "Ferramentas da KB" |
| 5 | git | `git add`, `git commit`, `git push` em branch novo → PR → merge |
| 6 | GitHub Actions | Re-instalar skills no `iracing_analysis` |
| 7 | Claude Code Web | Abrir sessão no `iracing_analysis` → `/coach-claude-code` → verificar seção KB no output |

---

## Verificação completa

1. **JSON gerado:** `curl https://victorauad.github.io/claude-code-growth/knowledge-base.json | python3 -m json.tool | head -40` → deve mostrar array com campos `titulo`, `tema`, `url`, `bullets`, `importancia`

2. **Skill com KB:** invocar `/coach-claude-code` no `iracing_analysis` → output deve terminar com seção "Da sua Knowledge Base" com links reais

3. **Dedup:** rodar `Ingest GitHub Stars` uma segunda vez → nenhum arquivo duplicado criado em `07-inbox/`

---

## Secrets e configurações necessárias (já estão no repo)

| Secret | Para que serve |
|---|---|
| `ANTHROPIC_API_KEY` | Sumarização via Claude Haiku em `ingest.py` e `ingest-github-stars.py` |
| `GH_PAT` | Instalar skills em repos externos e autenticar na API do GitHub em `ingest-github-stars.py` |

Label necessária no repo: `add-link` (já criada).

---

## Contexto adicional: como as skills são instaladas em outros repos

O workflow `install-skills-remote.yml` lê todos os `skills/*/SKILL.md` deste repo e os cria via API do GitHub no repo alvo em `.claude/skills/`. Ele usa o secret `GH_PAT`. Não precisa de acesso local — roda 100% no GitHub Actions.

Para re-instalar após atualizar skills:
- GitHub → claude-code-growth → Actions → "Install Skills in Remote Repo" → Run workflow → `target_repo: victorauad/iracing_analysis`

---

# Planos anteriores (histórico)

## Contexto

Hoje os skills (`coach-claude-code`, `setup-review`) são auditores estáticos: avaliam o estado do projeto mas não consultam a knowledge base do co-coach. A visão é que quando o skill roda em outro repo, ele combine avaliação do estado atual + recomendações vindas do que foi indexado (artigos, repos estrelados, vídeos). Para isso, o skill precisa acessar a KB em tempo de execução.

---

## Solução: JSON público no GitHub Pages + skills que o consultam

### Parte 1 — Gerar `docs/knowledge-base.json` no build

Modificar `scripts/build-site.py` para, além do `index.html`, gerar `docs/knowledge-base.json` com todos os cards indexados.

Estrutura de cada entrada:
```json
{
  "titulo": "...",
  "tema": "ferramentas | setup | metodologia | ...",
  "url": "https://...",
  "data": "2026-06-20",
  "bullets": ["ponto 1", "ponto 2", "ponto 3"],
  "importancia": "...",
  "fonte": "github-stars | issue | manual",
  "github_repo": "owner/repo"
}
```

URL pública após build: `https://victorauad.github.io/claude-code-growth/knowledge-base.json`

### Parte 2 — Atualizar `skills/coach-claude-code/SKILL.md`

Adicionar uma **Fase 2** ao skill após o assessment:

```
## Fase 2 — Recomendações da Knowledge Base

Após o assessment, faça:
1. Use WebFetch ou Bash(curl) para buscar https://victorauad.github.io/claude-code-growth/knowledge-base.json
2. Analise o CLAUDE.md e o contexto do projeto para identificar temas relevantes
3. Filtre os itens da KB com maior relevância para este projeto (máx 5)
4. Apresente como "Da sua Knowledge Base:"

Formato:
### Da sua Knowledge Base
- **[titulo]** — [1 frase de por que é relevante para este projeto] → [url]
```

### Parte 3 — Atualizar `skills/setup-review/SKILL.md`

Mesma lógica: após a auditoria de setup, adicionar seção "Ferramentas da KB que podem ajudar" filtrando por tema `ferramentas` e `setup`.

---

## Arquivos a modificar

| Arquivo | O que muda |
|---------|------------|
| `scripts/build-site.py` | Gerar `docs/knowledge-base.json` além do `index.html` |
| `skills/coach-claude-code/SKILL.md` | Adicionar Fase 2: fetch da KB + recomendações contextualizadas |
| `skills/setup-review/SKILL.md` | Adicionar seção de ferramentas da KB relevantes para o setup |

---

## Ordem de execução

| Passo | Ação |
|---|---|
| 1 | Modificar `build-site.py` para gerar `knowledge-base.json` |
| 2 | Rodar `build-site.py` localmente para validar o JSON |
| 3 | Atualizar `coach-claude-code/SKILL.md` com Fase 2 |
| 4 | Atualizar `setup-review/SKILL.md` com seção de KB |
| 5 | Commitar + push → GitHub Pages publica o JSON automaticamente |
| 6 | Re-instalar skills no `iracing_analysis` via Action |

## Verificação

- `docs/knowledge-base.json` acessível publicamente com pelo menos 10 entradas
- Invocar `/coach-claude-code` no `iracing_analysis` → output inclui seção "Da sua Knowledge Base" com itens relevantes
- Segunda rodada do workflow "Ingest GitHub Stars" → novos repos aparecem no JSON sem duplicação

---

# Planos anteriores (histórico)

## Contexto

O pipeline de ingestão já funciona: Issue → Action → `ingest.py` → `07-inbox/` → feed reconstruído. A nova feature usa a mesma base mas puxa conteúdo automaticamente dos repos que Victor estrelou no GitHub, sem precisar mandar link manualmente. O projeto também será renomeado de "claude-code-growth" para "co-coach" nas referências internas (o nome do repo no GitHub é mudado manualmente em Settings).

---

## Parte A — Renomeação para co-coach

Mudança do nome do repositório no GitHub é **manual** (Settings → Repository name). Arquivos internos a atualizar:

| Arquivo | O que mudar |
|---------|-------------|
| `STATUS.md` | Título e referências a "claude-code-growth" |
| `CLAUDE.md` | Seção de projetos ativos |
| `05-templates/memory-template.md` | "Projetos ativos" — `claude-code-growth` → `co-coach` |
| `docs/shortcut-ios.md` | URL da GitHub API com nome do repo |

> A URL do GitHub Pages muda automaticamente quando o repo for renomeado — não é necessário atualizar links manualmente.

---

## Parte B — Feature: Ingestão de GitHub Stars

### Fluxo

```
Schedule semanal (ou workflow_dispatch manual)
  → GET /users/victorauad/starred (API GitHub, autenticado com GH_PAT existente)
  → Para cada repo (até 20 mais recentes):
      - Checa dedup: glob em 07-inbox/ por slug "{owner}-{repo}"
      - Se novo: GET /repos/{owner}/{repo}/readme → base64 decode → texto do README
      - summarize() com contexto "repositório GitHub"
      - Salva em 07-inbox/YYYY-MM-DD-{owner}-{repo}.md com fonte: github-stars
  → build-site.py → commit → push
```

### Arquivos a criar/modificar

**1. Refatorar `scripts/ingest.py`**
- Extrair `summarize(url, content)` e `save_to_inbox(url, data, extra={})` como funções importáveis
- `main()` continua idêntico para o fluxo de Issue

**2. Criar `scripts/ingest-github-stars.py`** (novo)
- Autentica com `GH_PAT` (secret já existente) → rate limit 5000 req/h
- `GET https://api.github.com/users/victorauad/starred?per_page=20&sort=created`
- Dedup: `list(Path("07-inbox").glob(f"*-{owner}-{repo}.md"))`
- Frontmatter extra: `github_stars`, `fonte: github-stars`, `tema: ferramentas`
- Prompt de sumarização adaptado: foco em "o que faz, pra quem, tecnologias, conexão com Growth/Martech/AI"

**3. Criar `.github/workflows/ingest-github-stars.yml`** (novo)
```yaml
on:
  schedule:
    - cron: '0 9 * * 1'  # toda segunda 09h UTC
  workflow_dispatch:
    inputs:
      max_repos:
        default: '20'
```
- Secrets: `GH_PAT` e `ANTHROPIC_API_KEY` (ambos já existem)
- Steps: checkout → python → pip install → script → build-site → commit → push

### Deduplicação

```python
slug = f"{owner}-{repo_name}".lower().replace("/", "-")
if list(Path("07-inbox").glob(f"*-{slug}.md")):
    continue  # já indexado
```

---

## Ordem de execução

| Passo | Ação |
|---|---|
| 1 | Renomear referências internas nos 4 arquivos |
| 2 | Refatorar `ingest.py` para expor funções importáveis |
| 3 | Criar `scripts/ingest-github-stars.py` |
| 4 | Criar `.github/workflows/ingest-github-stars.yml` |
| 5 | Commit + push → testar via workflow_dispatch |

## Verificação

- Rodar workflow_dispatch → novos arquivos em `07-inbox/` com `fonte: github-stars` visíveis no feed
- Rodar segunda vez → nenhum arquivo duplicado criado (dedup funcionando)
- Cards no feed com tema "ferramentas" e link para o repo original no GitHub

---

# Plano anterior (histórico): Próximos passos do claude-code-growth + integração com iracing_analysis

## Contexto

O fluxo principal está funcionando: 30 cards no feed, 7 pastas indexadas, ingestão por Issue ativa, GitHub Pages no ar. O que falta agora é (a) conectar o workflow a outros projetos reais do Victor, começando pelo `iracing_analysis`, e (b) fechar os itens de infraestrutura que ainda faltam no próprio repo.

---

## Parte 1 — Rodar o workflow do claude-code-growth no iracing_analysis

### Como funciona
As skills (`coach-claude-code` e `setup-review`) precisam estar no disco local do projeto onde são invocadas. O script `scripts/install-skills.sh` faz isso: copia de `skills/` para `<projeto>/.claude/skills/`.

### Opção escolhida: GitHub Action `install-skills-remote`

Criar uma Action em `claude-code-growth` com `workflow_dispatch` que:
1. Aceita `target_repo` como input (ex: `victorauad/iracing_analysis`)
2. Lê os arquivos de `skills/` neste repo
3. Usa a API do GitHub para criar/atualizar os arquivos em `<target_repo>/.claude/skills/`
4. Requer um PAT (Personal Access Token) com escopo `repo` salvo como Secret `GH_PAT` em `claude-code-growth`

**Arquivo a criar:** `.github/workflows/install-skills-remote.yml`

**Secret necessário:** `GH_PAT` — Victor cria em github.com → Settings → Developer Settings → PAT → escopos: `repo`. Mesmo PAT que será usado pelo iOS Shortcut (pode ser o mesmo token).

**Como usar depois de configurado:** GitHub → claude-code-growth → Actions → "Install Skills in Remote Repo" → Run workflow → preencher `target_repo` → Run. As skills aparecem em `iracing_analysis/.claude/skills/` automaticamente.

> Alternativa: abrir uma sessão Claude Code com ambos os repos no escopo e executar a cópia direto via MCP — igualmente automático, sem precisar de PAT extra.

---

## Parte 2 — Itens pendentes no próprio claude-code-growth

### 2a. `requirements.txt` (2 min)
Falta arquivo de dependências Python. Sem ele, qualquer Action nova ou máquina nova precisa adivinhar o que instalar.

**Arquivo a criar:** `requirements.txt`
```
anthropic
requests
beautifulsoup4
youtube-transcript-api
```

### 2b. Marcar vídeos processados na lista (2 min)
Os 6 vídeos/webinars já estão no inbox mas `lista-de-videos.md` ainda mostra `[ ]` para todos.

**Arquivo a editar:** `04-biblioteca-de-estudos/lista-de-videos.md`  
Marcar `[x]` nos 5 vídeos YT + 1 webinar Anthropic já processados.

### 2c. Skill `bigquery-workflow` (opcional, 15 min)
Skill baseada em `02-fluxos-de-trabalho/banco-de-dados-bigquery.md`. Quando invocada em qualquer projeto com BigQuery, sugere o fluxo correto (Forma A vs B), lembra das regras de otimização de scan e gera esqueleto de query.

**Arquivo a criar:** `skills/bigquery-workflow/SKILL.md`

---

## Ordem de execução

| Passo | O que fazer | Tempo |
|---|---|---|
| 1 | Criar `requirements.txt` | 2 min |
| 2 | Marcar vídeos processados na lista | 2 min |
| 3 | Criar skill `bigquery-workflow` (opcional) | 15 min |
| 4 | Integração com iracing_analysis (manual, nova sessão) | 10 min |

## Verificação
- `requirements.txt`: `pip install -r requirements.txt` em ambiente limpo → `python3 scripts/ingest.py` roda sem erro de import.
- Lista de vídeos: 6 itens marcados com `[x]` no arquivo.
- iracing_analysis: `/coach-claude-code` retorna score baseado no CLAUDE.md daquele repo.

---

# Plano original (histórico)

# Plano: claude-code-growth como Knowledge Base viva + Coach de Setup + Feed Mobile

## Contexto

O repo `claude-code-growth` já tem uma estrutura editorial sólida (6 pastas, ~20 arquivos de conteúdo, templates de skill e CLAUDE.md). A pedido do Victor, ele precisa evoluir de uma "base de conhecimento estática que eu leio" para quatro coisas simultâneas:

1. **Um repo que cresce sozinho** — Victor manda links pelo celular, o sistema processa e indexa.
2. **Um coach plugável** — funciona como skill/agente em qualquer outro projeto, avaliando contexto e sugerindo boas práticas.
3. **Um gestor de setup** — cuida de CLAUDE.md, skills, memória e configurações do VS Code/Claude Code web.
4. **Um feed mobile** — webapp acessível pelo Chrome no celular mostrando o novo conteúdo ingerido em formato de cards.

---

## Decisões alinhadas

| Ponto | Decisão |
|-------|---------|
| Canal de ingestão | **GitHub Issue** com label `add-link` (criada via Apple Shortcuts no iOS) |
| Sumarização automática | **Sim** — API Anthropic como GitHub Secret (`ANTHROPIC_API_KEY`) |
| Instalação em outros repos | **Script de instalação** que copia os arquivos de skill para o projeto alvo |
| Skills remotas | Skills precisam ser arquivos locais — o script de instalação resolve isso copiando do repo clonado |

---

## Esclarecimento importante: Skills não são "cloud"

Skills do Claude Code **precisam estar no disco local** — não há como apontar para um repo GitHub diretamente. A solução para usar em múltiplas máquinas é:
- Clonar este repo uma vez por máquina (`git clone`).
- Rodar o script de instalação que copia as skills para `~/.claude/skills/` ou `.claude/skills/` do projeto.
- Para atualizar: `git pull` neste repo + rodar o script novamente.

---

## Arquitetura: quatro camadas

---

### Camada 1 — Ingestão de conteúdo (Objetivo 1)

**Fluxo completo:**

```
Victor no iPhone
  → Abre Apple Shortcut "Add to Growth Repo"
  → Shortcut faz POST na API do GitHub criando uma Issue com label "add-link" e o URL no corpo
  → GitHub Action detecta a issue, roda script Python:
      1. Fetch do conteúdo da URL
         - Se YouTube: pega transcrição via youtube-transcript-api
         - Se artigo: extrai texto via requests + BeautifulSoup
      2. Chama API Claude (claude-haiku-4-5, barato) para gerar resumo em markdown:
         - título, tema (1 das categorias do repo), 3 bullets, 1 citação-chave, link original
         - campo "por que isso importa para Growth/Martech"
      3. Salva em `07-inbox/YYYY-MM-DD-slug.md` e commita
      4. Fecha a issue automaticamente com link para o arquivo criado
  → Script semanal (cron Action) re-categoriza arquivos do inbox nas pastas 02–06 e atualiza READMEs
```

**Configuração do Apple Shortcut (5 min, sem código):**
- Ação "Get Contents of URL" com método POST para `https://api.github.com/repos/victorauad/claude-code-growth/issues`
- Headers: `Authorization: Bearer {PAT}`, `Accept: application/vnd.github+json`
- Body JSON: `{"title": "add-link", "body": "[URL colado]", "labels": ["add-link"]}`
- O URL pode vir do Share Sheet (botão "Compartilhar" de qualquer app)

**Arquivos a criar:**
- `.github/workflows/ingest-link.yml` — Action disparada por issue com label `add-link`
- `.github/workflows/reindex-weekly.yml` — cron semanal de re-categorização
- `scripts/ingest.py` — fetch + resumo via API Claude
- `scripts/reindex.py` — re-categorização e atualização de READMEs
- `07-inbox/` — pasta de entrada para conteúdo processado
- `docs/shortcut-ios.md` — passo a passo para configurar o Apple Shortcut

---

### Camada 2 — Coach plugável em outros projetos (Objetivo 2)

**Mecanismo:** Skill do Claude Code instalável via script.

**Skill `/coach-claude-code`** — quando invocada em qualquer projeto:
1. Lê o `CLAUDE.md` do projeto atual.
2. Avalia e retorna:
   - **Score de contexto** (0–10): itens presentes vs. itens recomendados (quem sou, stack, regras, formato de saída).
   - **Skills disponíveis** neste repo que se aplicam ao tipo de projeto.
   - **Próximos passos** baseados em `03-metodologias/` deste repo.
3. Sugere melhorias específicas no CLAUDE.md com exemplos prontos para copiar.

**Script de instalação** (`scripts/install-skills.sh`):
```bash
# Copia as skills deste repo para o projeto alvo
# Uso: bash install-skills.sh /caminho/do/projeto
```

**Arquivos a criar:**
- `.claude/skills/coach-claude-code/SKILL.md`
- `.claude/skills/setup-review/SKILL.md`
- `scripts/install-skills.sh`

---

### Camada 3 — Gestor de setup (Objetivo 3)

**Skill `/setup-review`** — auditoria de configuração do projeto atual:
- Verifica se existe `CLAUDE.md`, `settings.json`, pasta `.claude/skills/`.
- Compara o `CLAUDE.md` encontrado com o template deste repo e lista campos faltando.
- Aponta configurações recomendadas para VS Code (extensão Claude Code) e Claude Code web.
- Gera um relatório de setup com checklist do que fazer.

**Templates expandidos em `05-templates/`:**
- `settings.json.exemplo` — configuração base para projetos de dados (BigQuery, Sheets).
- `settings.json.vscode.exemplo` — configurações específicas para uso via VS Code.
- `memory-template.md` — template para arquivo de memória persistente entre sessões.

**Arquivos a criar/modificar:**
- `.claude/skills/setup-review/SKILL.md`
- `05-templates/settings.json.exemplo`
- `05-templates/memory-template.md`
- `01-setup/checklist-setup-completo.md` (atualiza o atual `checklist-primeiro-dia.md`)

---

### Camada 4 — Feed mobile / webapp (Objetivo novo)

**Mecanismo:** Site estático gerado automaticamente, hospedado no **GitHub Pages** (gratuito, zero servidor).

**O que é:** Uma URL pública (ex: `victorauad.github.io/claude-code-growth`) que Victor abre no Chrome do celular. Visual de blog/feed com cards.

**Como funciona:**
- Cada arquivo em `07-inbox/` vira um card no feed.
- A Action de ingestão (Camada 1) já inclui um passo final: regenerar o site estático e fazer push para o branch `gh-pages`.
- O site é um HTML+CSS+JS gerado por script Python a partir dos markdowns — sem framework, sem backend, carrega rápido no celular.

**Funcionalidades do feed:**
- **Cards de conteúdo:** título, tema, 3 bullets, data de ingestão, link para o conteúdo original.
- **Campo "O que estou fazendo agora":** campo de texto no topo da página. Quando Victor digita (ex: "estruturando meu CLAUDE.md" ou "construindo pipeline de dados"), o JS filtra e reordena os cards mostrando primeiro os mais relevantes para o contexto digitado — comparação simples de palavras-chave nos metadados dos markdowns.
- **Filtro por tema:** botões para filtrar por categoria (setup, metodologia, ferramentas, etc.).
- **Sem login:** a URL é pública mas obscura (não indexada no Google via `robots.txt`).

**Arquivos a criar:**
- `scripts/build-site.py` — lê `07-inbox/*.md`, gera `docs/index.html` com os cards.
- `docs/index.html` — gerado automaticamente (não editar à mão).
- `docs/style.css` — estilo mobile-first (fundo escuro, tipografia legível).

---

## Ordem de implementação

| Fase | O que fazer | Valor imediato |
|------|------------|---------------|
| 1 | Skills `/coach` e `/setup-review` + script de instalação | Auditoria de qualquer projeto hoje |
| 2 | Templates expandidos em `05-templates/` | Setup novo em minutos |
| 3 | Action de ingestão + script `ingest.py` | Repo cresce pelo celular |
| 4 | Feed mobile (GitHub Pages) | Ver o que foi ingerido no celular |
| 5 | Cron de re-indexação semanal | Conteúdo auto-organizado nas pastas corretas |

---

## Verificação (como testar cada parte)

- **Skills:** Em outro repo qualquer, invocar `/coach` e conferir se o score e sugestões fazem sentido para o `CLAUDE.md` daquele projeto.
- **Ingestão:** Usar o Apple Shortcut para mandar um URL do YouTube; verificar em ~2 min se o arquivo aparece em `07-inbox/` com resumo gerado.
- **Feed mobile:** Abrir `victorauad.github.io/claude-code-growth` no Chrome do iPhone; digitar "BigQuery" no campo e ver se os cards relevantes sobem.
- **Setup review:** Invocar `/setup-review` num projeto sem `CLAUDE.md` e confirmar que a skill lista todos os itens faltando.
