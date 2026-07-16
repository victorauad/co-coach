---
titulo: Agentes e subagentes
tema: agentes
tipo: guia
data: 2026-06-06
importancia: 3
---

# Agentes e subagentes

## Primeiro, o que é um "agente"

A melhor definição curta, da Anthropic, dada no AI Engineer Summit: <cite index="18-1">"agentes são modelos usando ferramentas num loop."</cite> Ou seja: o modelo pensa, usa uma ferramenta, vê o resultado, pensa de novo, repete — até terminar. Não é mágica; é esse loop.

Seu projeto de fundo de investimento "multi-agente" era exatamente isso: vários desses loops, cada um com um papel, conversando entre si. Agora você sabe o que aconteceu lá.

## O que é um subagente

<cite index="9-1">A Anthropic descreve subagentes como assistentes customizados para tipos específicos de tarefa. O Claude usa a descrição do subagente como pista de roteamento ao decidir se delega trabalho a ele — então um bom subagente é mais que uma persona: é um workflow bem delimitado, com as ferramentas e instruções certas para um trabalho recorrente.</cite>

<cite index="11-1">Subagentes são definidos em `.claude/agents/<nome>.md`, com frontmatter declarando suas ferramentas e modelo.</cite> Veja o exemplo pronto em `kb/templates/subagente-exemplo.md`.

## Por que usar subagentes: contexto limpo

A razão mais prática: <cite index="9-1">em sessões longas do Claude Code, o limite real geralmente não é a capacidade</cite> — é o contexto ficar poluído. Subagentes resolvem isso fazendo a tarefa numa janela separada e devolvendo só o resultado.

Conselho da comunidade: <cite index="10-1">tenha subagentes específicos por tarefa (com contexto extra) combinados com skills (progressive disclosure), em vez de um "engenheiro genérico". E diga "use subagents" pra jogar mais computação num problema — descarregue tarefas pra manter seu contexto principal limpo e focado.</cite>

## Project-level vs. user-level

<cite index="9-1">A Anthropic suporta subagentes a nível de projeto em `.claude/agents/` e a nível de usuário em `~/.claude/agents/`. Definições a nível de projeto são geralmente a melhor escolha quando o workflow depende das convenções de um código específico; agentes a nível de usuário servem melhor para hábitos portáteis, como exploração de repositório ou consulta de docs.</cite>

Detalhe importante que passa batido: <cite index="9-1">subagentes não herdam o system prompt completo padrão do Claude Code — eles recebem o próprio prompt mais detalhes básicos de ambiente, o que os torna mais fáceis de moldar deliberadamente.</cite>

## Subagentes que fariam sentido pra você

- **`explorador-de-repo`** (user-level) — pra entender repos novos da internet sem poluir seu contexto. Resolveria exatamente o problema do "segui o tutorial e não entendi". Pede pra ele explorar e te devolver só o resumo da arquitetura.
- **`revisor-de-numeros`** (project-level) — um subagente cujo único trabalho é validar os números de uma análise/planilha contra a fonte. Pega seus erros de "rodou mas tá errado".

Sobre o `revisor-de-numeros`, a comunidade tem uma técnica relevante: <cite index="10-1">use test-time compute — janelas de contexto separadas dão resultados melhores; um agente pode causar um bug e outro (mesmo modelo) pode encontrá-lo.</cite> Um agente faz, outro confere.

## Erro comum no seu nível

Criar um exército de subagentes antes de precisar. Comece com um (`explorador-de-repo`) que resolve uma dor real e sua. Multi-agente é sedutor — parece avançado — mas complexidade sem necessidade só te faz perder o fio de novo, que é justamente o que aconteceu no projeto do fundo.
