---
titulo: Ponytail — Skill que faz o agente escrever o mínimo de código possível
tema: metodologia
url: https://github.com/DietrichGebert/ponytail
data: 2026-07-12
fonte: github-stars
github_stars: 81259
github_repo: DietrichGebert/ponytail
---

# Ponytail — Skill que faz o agente escrever o mínimo de código possível

**Tema:** metodologia
**Fonte:** https://github.com/DietrichGebert/ponytail
**GitHub Stars:** 81259

## Resumo

- Skill que faz o agente de código pensar como "o dev sênior mais preguiçoso da sala": o melhor código é o que você nunca escreveu
- Resultados medidos em sessões reais de Claude Code: ~54% menos código (até 94% quando o agente tende a superconstruir), ~20% mais barato e ~27% mais rápido
- Combate o principal vício dos agentes: over-engineering — criar abstrações, arquivos e funcionalidades que ninguém pediu
- Mantém todas as guardas de segurança — diferente de um prompt simples "escreva uma linha só", que derruba proteções
- Funciona com 20+ agentes (Claude Code, Cursor, Codex etc), instalável via npm, licença MIT

## Por que isso importa

Para quem não é desenvolvedor e usa agentes para POCs e automações, over-engineering é custo direto: mais tokens, mais tempo e mais código para manter sem entender. Ponytail reduz a conta e o risco fazendo o agente entregar só o necessário — alinhado com o princípio de contexto enxuto da Anthropic.

## Citação

> He says nothing. He writes one line. It works.
