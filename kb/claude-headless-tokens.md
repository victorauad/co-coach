---
titulo: "Claude Code Headless: Modo -p, Billing e Economia de Tokens"
tema: setup
url: https://code.claude.com/docs/en/costs
data: 2026-06-25
fonte: pesquisa-web
importancia: alta
bullets:
  - "Modo headless (claude -p) roda Claude Code sem interface — ideal para CI, cron e automações"
  - "Overhead fixo de 20k–30k tokens por sessão antes da primeira mensagem (system prompt + CLAUDE.md + MCP schemas)"
  - "CLAUDE.md de 3.847 tokens vs 312 tokens: redução de 91,9% no contexto sem perda de qualidade"
  - "Skills carregam sob demanda (on-demand) — mantêm o contexto base menor"
  - "Mudança de billing headless anunciada para 15/jun/2026 foi pausada — uso headless ainda consome do pool de assinatura"
---

# Claude Code Headless: Modo -p, Billing e Economia de Tokens

## O que é o modo headless

O flag `claude -p` (ou `--print`) executa o Claude Code em modo não-interativo: recebe um prompt, processa e retorna a resposta sem abrir a interface de chat. É o modo usado em:

- Pipelines de CI/CD (GitHub Actions, scripts de automação)
- Tarefas agendadas (cron jobs)
- Agent SDK e integrações third-party

Diferença do uso interativo: no modo headless, não há acumulação de contexto entre chamadas — cada execução começa do zero.

## Overhead fixo de tokens por sessão

Antes de você digitar a primeira palavra, o Claude Code já consumiu entre **20.000 e 30.000 tokens** com o overhead de inicialização:

| Componente | Custo estimado |
|---|---|
| System prompt interno | ~10k–15k tokens |
| CLAUDE.md global + projeto | variável (ver abaixo) |
| Schemas de ferramentas MCP | ~2k–5k por servidor |
| Nomes e descrições de skills | ~500–2k tokens |

Esse custo se repete a cada turno da conversa — não é pago só uma vez.

## CLAUDE.md: o maior alavancador de economia

Um CLAUDE.md de **3.847 tokens** comparado a uma versão enxuta de **312 tokens** mostrou:
- Redução de **91,9% no contexto** carregado por sessão
- **Sem regressão de qualidade** nas respostas

Regra prática: mantenha o CLAUDE.md abaixo de **200 linhas**. Inclua só o que o Claude não consegue inferir lendo o código ou o contexto do projeto.

### O que tirar do CLAUDE.md
- Convenções óbvias de código (o Claude já sabe)
- Instruções que só se aplicam a tarefas específicas → mova para uma skill
- Documentação de arquitetura que está no código → o Claude lê o código

### O que manter no CLAUDE.md
- Preferências de comunicação (idioma, tom, formato)
- Restrições de segurança não óbvias
- Decisões de arquitetura que contradizem o padrão esperado

## Skills: contexto sob demanda

Skills só entram no contexto quando invocadas — não ficam carregadas na sessão inteira. Isso significa que instruções especializadas (ex: "como fazer query no BigQuery", "como usar Dify") ficam fora do overhead até o momento de uso.

**Estratégia:** mover blocos de instrução do CLAUDE.md para skills equivale a pagar esses tokens só quando necessário.

## Billing headless: o que mudou (e foi pausado)

A Anthropic anunciou em 14/mai/2026 que o uso via Agent SDK e `claude -p` sairia do pool de assinatura em 15/jun/2026, passando a consumir um **pool de créditos separado** cobrado a preço de API:

| Plano | Crédito headless/mês |
|---|---|
| Pro | $20 |
| Max 5x | $100 |
| Max 20x | $200 |

**Atualização:** a mudança foi **pausada antes de entrar em vigor**. O uso headless continua consumindo do pool padrão de assinatura por enquanto.

O que isso sinaliza: a Anthropic tende a separar esses usos no futuro — vale monitorar e evitar automações desnecessariamente verbosas.

## Outras técnicas de economia de tokens

- **Prompt caching** — conteúdo repetido (system prompt, CLAUDE.md) é cacheado automaticamente; reduz ~90% do custo em sessões longas
- **Compactação automática** — ao aproximar do limite de contexto, o Claude resume a conversa automaticamente
- **Limite de mensagens por sessão** — o sweet spot é **15–20 mensagens**; além disso, há degradação de qualidade por "context rot"
- **Hooks de filtro de output** — um hook `PostToolUse` pode comprimir um log de 10.000 linhas para 200 linhas de erros antes de entrar no contexto
- **Escolha de modelo** — Sonnet 4.6 fica a 1,2 pontos do Opus no SWE-bench a 5× menos custo; use Opus só quando necessário

## Preços de referência (jun/2026)

| Modelo | Input (por 1M tokens) | Output (por 1M tokens) |
|---|---|---|
| Haiku 4.5 | $1 | $5 |
| Sonnet 4.6 | $3 | $15 |
| Opus 4.8 | $5 | $25 |
| Fable 5 | $10 | $50 |

## Links úteis

- [Manage costs effectively — Claude Code Docs](https://code.claude.com/docs/en/costs)
- [Claude Code Token Optimization Guide](https://buildtolaunch.substack.com/p/claude-code-token-optimization)
- [12 Ways to Cut Token Consumption](https://www.firecrawl.dev/blog/claude-code-token-efficiency)
- [Claude Billing Change June 2026 — pausada](https://www.digitalapplied.com/blog/anthropic-claude-credit-overhaul-june-15-2026)
