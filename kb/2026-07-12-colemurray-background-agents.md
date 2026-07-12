---
titulo: Open-Inspect — Sistema open-source de agentes de código em background
tema: agentes
url: https://github.com/ColeMurray/background-agents
data: 2026-07-12
fonte: github-stars
github_stars: 2223
github_repo: ColeMurray/background-agents
---

# Open-Inspect — Sistema open-source de agentes de código em background

**Tema:** agentes
**Fonte:** https://github.com/ColeMurray/background-agents
**GitHub Stars:** 2223

## Resumo

- Sistema open-source de agentes que trabalham em background enquanto você faz outra coisa, inspirado no Inspect da Ramp
- Acionável de qualquer lugar: web, Slack, PRs do GitHub, issues do Linear ou webhooks — o agente abre PRs com atribuição correta ao autor do pedido
- Roda em agenda (cron), reage a alertas (Sentry) e cria subtarefas paralelas em sandboxes separados
- Sessões "multiplayer": várias pessoas colaboram com o mesmo agente em tempo real
- Atenção ao modelo de segurança: single-tenant apenas — todos os usuários compartilham as credenciais do GitHub App, então só serve para times onde todos são confiáveis

## Por que isso importa

É o padrão "delegue e siga em frente" aplicado a automações: em vez de supervisionar o agente na tela, você despacha tarefas via Slack ou agenda e recebe o resultado como PR. Conecta com as palestras da KB sobre não ficar de babá de agente — o gargalo é sua atenção, não a capacidade do agente.

## Citação

> Work on tasks in the background while you focus on other things — connect from anywhere: web UI, Slack, GitHub PRs, Linear issues, or webhooks.
