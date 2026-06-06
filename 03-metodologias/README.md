# Metodologias de trabalho com AI

Como estruturar o jeito que você trabalha com o Claude — segundo a Anthropic e a comunidade (AI Engineer Summit etc.). Isto é o que separa "uso o ChatGPT às vezes" de "tenho um sistema".

## O modelo mental que organiza tudo

A comunidade convergiu num modelo mental simples para os recursos do Claude Code. Vale memorizar este resumo:

> <cite index="9-1">CLAUDE.md guarda o contexto contínuo do projeto, skills armazenam playbooks reutilizáveis, e subagentes lidam com tarefas isoladas onde a sessão principal só precisa do resultado.</cite>

Os arquivos desta pasta destrincham cada peça:

| Peça | Arquivo | Pra quê serve |
|---|---|---|
| Prompts | [prompts.md](prompts.md) | Como pedir as coisas |
| Skills | [skills.md](skills.md) | Playbooks reutilizáveis ("ensine uma vez") |
| Agentes / subagentes | [agentes-e-subagentes.md](agentes-e-subagentes.md) | Delegar tarefas isoladas |
| Workflows | [workflows.md](workflows.md) | Encadear tudo num processo |
| Seus pontos cegos | [pontos-cegos-do-meu-raciocinio.md](pontos-cegos-do-meu-raciocinio.md) | Erros típicos do seu estágio |

## A hierarquia de esforço (não pule etapas)

Não saia criando subagentes e skills no dia 1. A ordem que a comunidade recomenda:

1. **Prompt bom** resolve 80% dos casos. Domine isso primeiro.
2. **CLAUDE.md** quando você se cansar de repetir contexto.
3. **Comando (`/slash`)** quando você repete o mesmo prompt todo dia.
4. **Skill** quando o "como fazer" é um playbook estável que você reusa.
5. **Subagente** quando você quer isolar uma tarefa pra não poluir o contexto principal.

Regra prática da comunidade: <cite index="10-1">se você faz algo mais de uma vez por dia, transforme em skill ou comando.</cite>
