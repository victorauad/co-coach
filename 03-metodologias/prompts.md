# Prompts

A habilidade de base. Tudo o mais (skills, agentes) é prompt organizado. Se você melhora só isto, já melhora tudo.

## Os princípios que mais movem o ponteiro

1. **Seja claro e específico.** O modelo não adivinha contexto que você não deu. "Faça uma análise" é ruim; "compare conversão por canal nos últimos 3 meses e me diga o canal com pior tendência" é bom.
2. **Dê contexto e exemplos.** Mostre um exemplo de saída boa (e uma ruim, se ajudar). Exemplos valem mais que adjetivos.
3. **Peça raciocínio passo a passo** em tarefas complexas. "Pense em etapas antes de responder" melhora resultado em análise e lógica.
4. **Especifique formato.** Diga se quer tabela, bullets, prosa, JSON, planilha. Você tem preferência forte por saídas estruturadas e repurposáveis — *diga isso explicitamente.*
5. **Use tags/seções** para separar contexto de instrução. Ajuda o modelo a não confundir "o que é dado" com "o que é ordem".

## Um esqueleto de prompt que serve quase sempre

```
[CONTEXTO] Quem sou, qual a situação, quais dados existem.
[OBJETIVO] O que eu quero, em uma frase.
[FORMATO] Como quero a saída (tabela? bullets? planilha? em português?).
[RESTRIÇÕES] O que evitar, limites, o que NÃO fazer.
[ANTES DE EXECUTAR] "Me mostre o plano em 3 bullets primeiro."
```

## Aprofundamento oficial

A Anthropic mantém um guia de prompt engineering que vale ler com calma: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview — tem exemplos de cada técnica acima.

## Para o seu caso de disciplina

Crie um prompt-base salvo (no CLAUDE.md ou num bloco de notas) com o seu esqueleto preenchido com quem você é e como gosta das respostas. Assim você não começa do zero toda vez — reduz o atrito de começar, que é seu maior inimigo.

## Erro comum

Prompt longo ≠ prompt bom. O que importa é *especificidade*, não tamanho. Um prompt de 3 linhas muito específico bate um de 3 parágrafos vago. E o erro inverso também existe: prompt curto demais que obriga o modelo a adivinhar — e ele adivinha errado com confiança.
