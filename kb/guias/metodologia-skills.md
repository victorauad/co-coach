---
titulo: Skills
tema: metodologia
tipo: guia
data: 2026-06-06
importancia: 3
---

# Skills

A ideia central de skills, na frase da própria Anthropic: parar de se repetir e **ensinar o Claude uma vez.**

## O que é uma skill

<cite index="12-1">Skills são recursos reutilizáveis, baseados em arquivos, que dão ao Claude expertise específica de um domínio: workflows, contexto e boas práticas que transformam um agente genérico num especialista.</cite> <cite index="12-1">Diferente de prompts (instruções de conversa, pra tarefas pontuais), skills carregam sob demanda e eliminam a necessidade de repetir a mesma orientação em várias conversas.</cite>

Na prática: <cite index="11-1">uma skill é um workflow reutilizável definido em `.claude/skills/<nome>/SKILL.md`. O frontmatter dá o nome e uma descrição de uma linha; o corpo descreve o workflow. O agente invoca a skill como se fosse uma ferramenta.</cite>

## Anatomia (veja o exemplo pronto em 05-templates/skill-exemplo/SKILL.md)

```markdown
---
name: relatorio-ttv
description: Gera relatório de Time-to-Value a partir de um export do Notion, com flags de qualidade e desvio de cronograma.
---

# Como gerar o relatório de TTV

1. Leia o CSV de deliverables.
2. Calcule as colunas: dias até primeira entrega, desvio vs. SLA...
3. Aplique flags de qualidade: [suas regras]
4. Gere XLSX com 3 abas: Resumo, Detalhe, Qualidade.
5. Formato: [suas preferências de layout]
```

## A grande sacada: progressive disclosure

A descrição no frontmatter é o que o Claude lê pra *decidir se usa* a skill. O corpo só carrega quando ele realmente a invoca. Isso mantém o contexto enxuto. Por isso a descrição tem que ser boa — é o gatilho.

## Quando criar uma skill (pra você especificamente)

Você tem candidatas óbvias, porque seu trabalho tem padrões que se repetem:

- **`relatorio-ttv`** — seu fluxo de Time-to-Value com flags e desvio de cronograma.
- **`analise-pipeline`** — análise de pipeline do HubSpot no seu formato de abas.
- **`mockup-uncover`** — você já tem um design system (fundo escuro, verde-limão, serifa editorial). Uma skill que conhece esses tokens entrega mockups no padrão sem você re-explicar. (Aliás, isso já existe parcialmente nos seus skills internos da Uncover.)

## Segurança

<cite index="12-1">Use skills só de fontes confiáveis: as que você criou ou obteve da Anthropic. Skills dão capacidades novas ao Claude através de instruções e código — o que as torna poderosas, mas também significa que uma skill maliciosa pode direcionar comportamento indevido.</cite> Não instale skill de fonte aleatória da internet sem ler o que ela faz.

## Curso oficial

A Anthropic tem um curso de introdução a Agent Skills: https://anthropic.skilljar.com/introduction-to-agent-skills — <cite index="14-1">cobre criar sua primeira skill do zero, escrever o frontmatter, descrições que disparam de forma confiável, e organizar o diretório com progressive disclosure.</cite>

## Erro comum no seu nível

Criar skill cedo demais, pra algo que você fez uma vez. Skill é pra padrão *estável e repetido*. Se você ainda está descobrindo como faz, fique no prompt. Skill prematura é manutenção sem retorno — você acaba mantendo um playbook de algo que mudou.
