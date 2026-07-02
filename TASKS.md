# TASKS — co-coach

> Derivado de [STATUS.md](STATUS.md) em 2026-06-24.
> Atualizado em 2026-06-25 (limpeza pós-handoff).
> Legenda: `[ ]` pendente · `[x]` feito · `[-]` descartado

---

## Prioridade alta

- [x] **`docs/proficiency.json`** — criar o arquivo com schema de scores por tema e garantir que a skill `co-coach-quiz` escreve e lê nele corretamente
- [x] **`config/sync-targets.yml`** — registrar novos repos que precisem receber auto-sync de skills (preencher conforme novos projetos forem criados)

---

## Prioridade média

- [x] **Dashboard de sync** — adicionar step ao final de `sync-skills.yml` que gera/atualiza `config/sync-status.md` com: repo, skills instaladas, data do último sync
- [ ] **Ingestão de playlists do YouTube** — modificar `scripts/ingest.py` para aceitar URLs de playlist e iterar sobre os vídeos

---

## Prioridade baixa

- [ ] **Changelog automático de KB** — adicionar step no `ingest-link.yml` que acrescenta uma linha em `kb/CHANGELOG.md` com: data, URL e título do conteúdo indexado
- [ ] **Reorganizar `skills/README.md`** — atualizar o índice de skills por categoria: produtividade, marketing, dados, ferramentas, integrações
- [ ] **Step de verificação nos workflows** — adicionar ao `ingest-link.yml` e `sync-skills.yml` um step básico de validação que falha se o arquivo gerado estiver vazio ou malformado

---

## Feito (referência)

- [x] Ingestão via GitHub Issue (testado em Issue #1 — ~23s, card no feed, Issue fechada)
- [x] Feed mobile no ar: `https://victorauad.github.io/co-coach`
- [x] 30+ skills criadas e no padrão `co-coach-*`
- [x] Sync automático de skills para `iracing_analysis` e `alamtoco`
- [x] Workflow de setup de novo projeto (`setup-project.yml`)
- [x] Rebuild automático do site por push em `kb/**` ou `skills/**`
- [x] Memória de sessão via `/co-coach-handoff`
- [x] Estatísticas no feed mobile (rodapé com data do rebuild e contagem por tema em `docs/index.html`)
- [x] `static/gerenciador.html` — interface de gerenciamento via browser (porta 8765)
- [x] `static/aprenda.html` — diagrama visual explicativo do sistema (absorveu o `docs/sistema.html`)
- [x] `build-site.py` atualizado para copiar `static/` → `docs/` a cada rebuild
- [x] Spec SDD completa: `requirements.md`, `design.md`, CLAUDE.md atualizado

## Descartado

- [-] **iOS Shortcut** — fluxo URL → Issue → feed descartado; não será implementado
