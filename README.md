# Claude Code para Growth — Repositório de Estudos

Guia de estudo e referência para usar **Claude Code** no trabalho de Growth/Martech. Tudo aqui é feito para ser lido no VS Code e consultado conforme você precisa — não para ser engolido de uma vez.

> **Como este repositório foi pensado.** Você disse que não tem facilidade com disciplina. Então a estrutura aqui é *anti-procrastinação*: nada de "leia 40 páginas antes de começar". Cada arquivo abre com um bloco **"Faça isso agora (5 min)"**, e o conteúdo mais longo vem depois, pra quando você quiser aprofundar. Comece sempre pela ação pequena.

## Por onde começar

1. **[00-comece-aqui/LEIA-PRIMEIRO.md](00-comece-aqui/LEIA-PRIMEIRO.md)** — como navegar e como estudar sem se perder.
2. **[01-setup/instalacao-vscode-mac.md](01-setup/instalacao-vscode-mac.md)** — instalar e configurar o Claude Code no terminal do VS Code (Mac). Faça isso primeiro, na prática.
3. **[02-fluxos-de-trabalho/](02-fluxos-de-trabalho/)** — fluxos reais para BigQuery, planilhas, POCs e MCP (HubSpot).
4. **[03-metodologias/](03-metodologias/)** — como estruturar prompts, skills, agentes e workflows segundo a Anthropic e a comunidade.
5. **[04-biblioteca-de-estudos/](04-biblioteca-de-estudos/)** — lista de vídeos catalogada por tema.
6. **[05-templates/](05-templates/)** — arquivos prontos pra copiar (CLAUDE.md, subagentes, skills).
7. **[06-ferramentas-e-repos/](06-ferramentas-e-repos/)** — os 10 repos mais populares do GitHub para turbinar o Claude Code, com instalação e use case para cada um.

## Estrutura

```
claude-code-growth/
├── README.md
├── 00-comece-aqui/
│   ├── LEIA-PRIMEIRO.md
│   └── como-estudar-sem-disciplina.md
├── 01-setup/
│   ├── instalacao-vscode-mac.md
│   └── checklist-primeiro-dia.md
├── 02-fluxos-de-trabalho/
│   ├── README.md
│   ├── banco-de-dados-bigquery.md
│   ├── planilhas-estruturadas.md
│   ├── pocs-ai-coding.md
│   └── mcp-hubspot-e-saas.md
├── 03-metodologias/
│   ├── README.md
│   ├── prompts.md
│   ├── skills.md
│   ├── agentes-e-subagentes.md
│   ├── workflows.md
│   └── pontos-cegos-do-meu-raciocinio.md
├── 04-biblioteca-de-estudos/
│   └── lista-de-videos.md
├── 05-templates/
│   ├── CLAUDE.md.exemplo
│   ├── subagente-exemplo.md
│   └── skill-exemplo/SKILL.md
├── 06-ferramentas-e-repos/
│   ├── README.md
│   ├── 01-repomix.md
│   ├── 02-everything-claude-code.md
│   ├── 03-dify.md
│   ├── 04-flowise.md
│   ├── 05-onyx.md
│   ├── 06-claude-skills-oficial.md
│   ├── 07-awesome-claude-skills.md
│   ├── 08-obsidian-skills.md
│   ├── 09-notebooklm-skill.md
│   └── 10-marketing-skills.md
└── .claude/
    └── skills/   (onde suas skills reais vão morar)
```

## Seu contexto

- **Papel:** Head de Growth em startup de Martech (MMM / media measurement).
- **Nível:** aprendendo AI, mas já entregou coisas reais (repo multi-agente de fundo de investimento; pipeline iRacing → BigQuery → MCP → Google Slides).
- **Stack do dia a dia:** Notion, Slack, Gmail, HubSpot, Google Sheets, BigQuery.
- **Meta:** usar Claude Code como ferramenta de trabalho — não virar engenheiro de software.

---
*Atualizado em maio/2026. Setup e features do Claude Code mudam rápido — sempre confira a doc oficial: https://code.claude.com/docs*
