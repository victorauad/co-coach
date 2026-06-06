# Fluxo: POCs rápidas de AI-coding

Você já fez uma POC real (iRacing → BigQuery → MCP → Slides). O objetivo deste fluxo é você conseguir repetir esse tipo de coisa **com intenção**, entendendo cada parte — não só seguindo um tutorial.

> **Faça isso agora (5 min):** escolha uma pergunta de negócio pequena ("será que dá pra prever churn com os campos que tenho no HubSpot?") e peça ao Claude um plano de POC em Plan Mode.

## O que é uma POC aqui

Um protótipo descartável que responde **uma** pergunta: "isso é viável / vale a pena?". Não é produto. POC boa é rápida, feia e conclusiva. Se você está caprichando no visual, já fugiu do objetivo.

## O loop de uma POC com Claude Code

1. **Escreva a pergunta numa frase.** "Consigo cruzar dados de participação do produto com estágio de funil pra ver se uso prevê conversão?"
2. **Plan Mode (`Shift+Tab`).** Peça o plano: quais dados, quais passos, qual a saída. Revise antes de qualquer código.
3. **Construa em pedaços pequenos e verificáveis.** Não peça a POC inteira de uma vez. Peça o passo 1, rode, confira. Depois o passo 2. Isso é o oposto de "rodei o tutorial inteiro e não sei o que aconteceu".
4. **Peça explicação a cada salto.** "Por que você usou esse formato aqui?" Você está construindo entendimento, não só artefato.
5. **Conclua e descarte (ou promova).** A POC respondeu sim/não? Ótimo. Se for promissora, aí sim vira um projeto sério — outra conversa.

## Modo headless (o que você usou no iRacing)

Modo "headless" é rodar o Claude Code sem a interface interativa — num script, num pipeline. É poderoso pra automação, mas é também onde você "perdeu o fio" antes. Recomendação: **só vá pra headless depois de entender o fluxo no modo interativo.** Faça interativo primeiro, entenda cada passo, *depois* automatize. Headless cedo demais = caixa-preta.

## Sobre repos da internet (o caso do fundo multi-agente)

Você montou um repo de YouTube e não entendeu o que aconteceu. Padrão pra próxima vez:

1. Antes de rodar: peça ao Claude "leia este repo e me explique a arquitetura como se eu não programasse".
2. Pergunte especificamente: "o que é cada agente, por que tem mais de um, e onde os dados entram e saem?"
3. Só rode depois de entender o desenho. Rodar primeiro e entender depois é como dirigir de olhos fechados — às vezes chega, mas você não aprende o caminho.

## Erro comum no seu nível

Confundir "consegui rodar" com "entendi". São coisas diferentes. Uma POC que roda mas que você não entende não te dá poder de decisão — você não consegue defender as conclusões numa reunião nem adaptar pra um caso novo. **O entregável de uma POC não é o código; é a sua capacidade de explicar o resultado.**
