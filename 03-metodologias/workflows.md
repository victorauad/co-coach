# Workflows

Onde tudo se junta: prompts + CLAUDE.md + skills + subagentes encadeados num processo que você repete.

## Os blocos de construção (resumo)

Da comunidade, os recursos do Claude Code e pra que servem:

- **CLAUDE.md** — <cite index="13-1">está sempre carregado, sempre consumindo espaço da janela de contexto, então mantenha focado.</cite> É a memória permanente do projeto.
- **Comandos (`/slash`)** — <cite index="10-1">use comandos slash para todo workflow de "inner loop" que você faz muitas vezes por dia; eles vivem em `.claude/commands/` e são versionados no git.</cite>
- **Skills** — playbooks reutilizáveis (ver `skills.md`).
- **Subagentes** — tarefas isoladas (ver `agentes-e-subagentes.md`).
- **Hooks** — <cite index="11-1">comandos de shell que disparam em pontos do ciclo de vida; diferente das instruções do CLAUDE.md que são consultivas, hooks são determinísticos e garantem que a ação aconteça.</cite> Avançado — deixe pra depois.

## A diferença consultivo vs. determinístico (importante)

Uma lição da comunidade que economiza frustração: <cite index="10-1">use `settings.json` para comportamento que precisa ser garantido (permissões, modelo, atribuição) — não coloque regras críticas no CLAUDE.md esperando obediência total.</cite> O CLAUDE.md é orientação, não lei. Se algo *precisa* sempre acontecer, é hook ou settings, não uma instrução em maiúsculas no CLAUDE.md (que o modelo pode ignorar).

## Metodologia de planejamento

O hábito mais valioso, e o mais fácil de adotar: **planejar antes de executar.** A comunidade trata "Plan / Context / Prompting" como pilares. Em ordem prática:

1. **Plan Mode (`Shift+Tab`)** antes de tarefas não triviais.
2. **Contexto limpo** — não deixe a sessão virar uma sopa; delegue a subagentes ou comece sessão nova quando o assunto muda.
3. **Sessões nomeadas** — `claude --resume` pra retomar; `/rename` pra organizar.

## Cross-model (avançado, mas bom saber que existe)

A comunidade documenta usar o Claude Code junto com outros modelos: <cite index="10-1">um fluxo manual de dois terminais com Plan no Claude e revisão de QA noutro modelo.</cite> Útil quando você quer uma segunda opinião "de fora" numa análise importante. Não precisa fazer agora — só saiba que dá.

## Um workflow completo pro seu mundo (exemplo)

"Relatório semanal de pipeline":

1. **Comando `/pipeline-semanal`** dispara o fluxo.
2. **MCP do HubSpot** puxa os deals (sem export manual).
3. **Skill `relatorio-ttv`** estrutura no seu formato de abas.
4. **Subagente `revisor-de-numeros`** valida os totais.
5. Você recebe o XLSX pronto, conferido, no seu padrão.

Você não constrói isso no dia 1. Constrói peça por peça, conforme cada dor aparece. Mas é pra cá que o caminho leva — e cada peça que você adiciona te devolve tempo toda semana.

## Erro comum no seu nível

Querer montar o workflow completo de uma vez (igual o exemplo acima) antes de dominar as peças. Monte uma peça, use por uma semana, adicione a próxima. Workflow é planta que cresce, não prédio que você ergue de uma vez.
