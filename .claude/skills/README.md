# Skills do co-coach

Skills instaláveis do Claude Code. Cada pasta tem um `SKILL.md` com frontmatter (`name`, `description`) e instruções.

> **Gerado automaticamente** por `scripts/build-site.py`. Não edite manualmente — as alterações serão sobrescritas no próximo build.

## Convenção de nomenclatura

Toda skill segue o padrão **`co-coach-<palavra>`**. Ao criar uma nova, use a `co-coach-builder`.

---

## Produtividade & Metodologia

| Skill | Função |
|-------|--------|
| `co-coach-builder` | Ajuda a criar uma nova skill do Claude Code no padrão do co-coach — faz perguntas, gera o SKILL.md com frontmatter corre |
| `co-coach-handoff` | Gera um arquivo de memória da sessão atual, salva em memory/YYYYMMDD-projeto.md e imprime um bloco pronto para colar na  |
| `co-coach-list` | Índice vivo das skills co-coach — lista todas as skills co-coach-* instaladas com descrição detalhada do que cada uma fa |
| `co-coach-mermaid` | Cria e refina diagramas Mermaid de alta qualidade — flowcharts, sequências, arquitetura, jornadas, Gantt |
| `co-coach-obsidian` | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syn |
| `co-coach-quiz` | Faz um quiz rápido por tema baseado na knowledge base e registra o resultado na seção Progresso do perfil-do-aluno.md |
| `co-coach-repomix` | Usa o Repomix para compactar um projeto inteiro em um único arquivo de texto otimizado para o Claude |
| `co-coach-review` | Avalia a qualidade do contexto do projeto atual (CLAUDE.md, skills, settings) com score 0–10 e sugestões concretas |
| `co-coach-sdd` | Guia o usuário pelo ciclo Spec-Driven Development (SDD) aplicado ao projeto atual — cria ou valida os 3 documentos de sp |
| `co-coach-setup` | Audita a configuração completa do Claude Code no projeto atual — CLAUDE.md, settings.json, skills instaladas, memória gl |
| `co-coach-start` | Wizard de boas-vindas do co-coach |
| `co-coach-support` | Tira-dúvidas sobre Claude Code, ferramentas, metodologia e setup respondendo SOMENTE com base na knowledge base do co-co |
| `co-coach-ui` | Projeta e gera interfaces web simples — layouts, componentes HTML/CSS/Tailwind, dashboards e protótipos de POC |
| `co-coach-wizard` | Criador conversacional de projetos Claude Code |

## Marketing & Growth

| Skill | Função |
|-------|--------|
| `co-coach-ads` | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X,  |
| `co-coach-analytics` | When the user wants to set up, improve, or audit analytics tracking and measurement |
| `co-coach-competitor` | When the user wants to research, profile, or analyze competitors from their URLs |
| `co-coach-content` | When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover |
| `co-coach-copy` | When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, prici |
| `co-coach-market` | Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source attribution |
| `co-coach-marketing-plan` | When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product |
| `co-coach-research` | Multi-source deep research using firecrawl and exa MCPs |
| `co-coach-seo` | When the user wants to audit, review, or diagnose SEO issues on their site |
| `co-coach-social` | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, Ti |

## Dados & Automação

| Skill | Função |
|-------|--------|
| `co-coach-bigquery` | Ajuda a montar queries BigQuery Standard SQL para perguntas de negócio |
| `co-coach-digest` | Gera um briefing curto dos itens mais recentes e importantes da knowledge base do co-coach — "o que há de novo" — priori |
| `co-coach-xlsx` | Use this skill any time a spreadsheet file is the primary input or output |

## Documentos & Apresentações

| Skill | Função |
|-------|--------|
| `co-coach-docx` | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) |
| `co-coach-pdf` | Use this skill whenever the user wants to do anything with PDF files |
| `co-coach-pptx` | Use this skill any time a .pptx file is involved in any way — as input, output, or both |

## Ferramentas & Integrações

| Skill | Função |
|-------|--------|
| `co-coach-dify` | Orienta na criação de aplicações de IA usando o Dify — plataforma visual sem código |
| `co-coach-flowise` | Orienta na criação rápida de agentes e chatbots com o Flowise — construtor visual com arrastar e soltar |
| `co-coach-notebooklm` | Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed  |
| `co-coach-onyx` | Orienta na instalação e uso do Onyx — plataforma de chat com IA auto-hospedada que conecta com Google Drive, Slack, Noti |

---

## Como as skills são distribuídas

O workflow `.github/workflows/sync-skills.yml` copia cada pasta de `.claude/skills/` para o `.claude/skills/` dos repos registrados em `config/sync-targets.yml`.
