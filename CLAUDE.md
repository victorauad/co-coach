# Sobre este projeto e sobre mim

## Quem sou
Sou Victor, Head de Growth numa startup de Martech (MMM / media measurement). Não sou desenvolvedor — uso Claude Code como ferramenta de trabalho para dados, análises, automações e POCs. Estou aprendendo AI na prática, sem background técnico formal.

## Como prefiro que você se comunique
- Sem jargão de programação. Se precisar usar um termo técnico, explique em uma linha logo depois.
- Antes de tarefas não triviais, mostre um plano em 3 bullets e espere eu aprovar.
- Responda sempre em português (Brasil).
- Saídas que eu consiga colar direto no Notion ou Google Sheets sem reformatar.
- Se eu estiver seguindo um caminho ruim, me avise — não concorde só pra concordar.

## Stack e contexto
- Ferramentas do dia a dia: Notion, Slack, Gmail, HubSpot, Google Sheets, BigQuery.
- Dados sensíveis de cliente/CRM aparecem com frequência — nunca peça nem manuseie credenciais; eu cuido da autenticação.

## Regras de trabalho
- "Rodou" não significa "está certo": valide uma amostra dos resultados e me diga o que conferiu.
- Para queries no BigQuery, otimize para escanear o mínimo de dados.
- Para planilhas, siga o padrão: abas Resumo / Detalhe / Qualidade, datas em DD/MM/AAAA, moeda em R$.

## O que estou aprendendo
Estou aprendendo Claude Code e IA aplicada ao trabalho. Quando eu fizer algo sem entender o porquê, prefiro uma explicação rápida do conceito antes do resultado — não precisa ser longa, só o suficiente pra eu entender o que está acontecendo.

## Meta deste projeto
Usar Claude Code como ferramenta de trabalho — não virar engenheiro de software. O repositório é uma base de conhecimento viva e um sistema de skills instaláveis em outros projetos.

## Como trabalhar neste projeto (Spec-Driven Development)

Antes de qualquer tarefa não trivial, siga este ciclo de 4 fases:

1. **Specify** — escreva o que precisa ser feito em linguagem clara (o "o quê" e o "por quê"). Consulte `requirements.md` para contexto e `design.md` para restrições técnicas.
2. **Plan** — proponha um plano em bullets e aguarde aprovação antes de executar.
3. **Implement** — execute os passos do plano, um de cada vez.
4. **Validate** — confira se o resultado bate com o que foi especificado. "Rodou" não é suficiente.

Os 3 documentos de spec deste projeto:
- `requirements.md` — o que o sistema precisa fazer (histórias de usuário e objetivos)
- `design.md` — como está construído (arquitetura, decisões técnicas, restrições)
- `TASKS.md` — passos atômicos de implementação e backlog priorizado

Quando receber uma tarefa, consulte esses três arquivos antes de propor qualquer plano.

## Arquitetura em 3 camadas

1. **Knowledge base viva** — conteúdo indexado automaticamente em `kb/` via: (a) link enviado por GitHub Issue (iOS Shortcut), (b) repos do GitHub estrelados (workflow semanal). Cada arquivo `.md` tem frontmatter YAML com titulo, tema, bullets, url, importancia.

2. **Feed mobile** — site estático em GitHub Pages (`https://victorauad.github.io/co-coach`) gerado por `scripts/build-site.py`. Cards com filtro por tema e campo de contexto "o que estou fazendo agora".

3. **Skills instaláveis** — arquivos `SKILL.md` em `skills/*/`, copiados para `.claude/skills/` de outros repos via GitHub Action `sync-skills.yml`. Para ver skills disponíveis: `ls skills/`.

## Estrutura real do repositório
```
co-coach/
├── kb/                   — knowledge base indexada (arquivos .md com frontmatter)
├── static/               — HTMLs versionados copiados para docs/ a cada rebuild
├── scripts/
│   ├── build-site.py     — gera docs/ completo (index + json + static/)
│   ├── server.py         — servidor local para o gerenciador (porta 8765)
│   ├── ingest.py         — fetch + sumarização via Claude Haiku → kb/
│   └── ingest-github-stars.py
├── skills/               — 30+ skills co-coach-* (ls skills/ para ver todas)
├── docs/                 — gerado automaticamente pelo CI (nunca commitar)
├── config/
│   └── sync-targets.yml  — repos que recebem auto-sync de skills
├── requirements.md       — o que o sistema precisa fazer
├── design.md             — como está construído, decisões técnicas
├── TASKS.md              — backlog priorizado
└── .github/workflows/
    ├── ingest-link.yml        — dispara ao Issue receber label "add-link"
    ├── ingest-github-stars.yml — toda segunda 09h UTC
    ├── reindex-weekly.yml      — rebuild do site toda segunda 08h UTC
    └── sync-skills.yml         — distribui skills para repos registrados
```

## Como usar a knowledge base

Os arquivos em `kb/` são artigos, vídeos e repos indexados por tema (frontmatter `tema:`).
Quando receber uma tarefa relacionada a Claude Code, ferramentas, metodologia ou setup,
busque contexto relevante antes de responder:

```bash
grep -r "tema: <assunto>" kb/
```

Temas disponíveis: `agentes`, `ferramentas`, `mcp`, `metodologia`, `prompts`, `setup`, `workflow`.

As skills `co-coach-review` e `co-coach-setup` consultam `https://victorauad.github.io/co-coach/knowledge-base.json` via WebFetch para trazer recomendações contextualizadas da KB ao final de cada avaliação.
