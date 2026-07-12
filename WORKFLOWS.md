# Workflows de IA por tipo de projeto

> Gerado a partir da entrevista de 12/07/2026 (`memory/entrevista-workflows-20260712.md`) cruzada com a knowledge base (`kb/`).
> Princípio central (Anthropic, context engineering): dar ao agente **o menor conjunto de contexto de alto sinal** — cada arquétipo define qual contexto é sinal e qual é ruído.

---

## A tipologia — 4 arquétipos

| Arquétipo | Projetos | Produto final | Horizonte |
|---|---|---|---|
| **A. Produto/MVP** | `SMPL_MVP` ⭐, `AuaDriving`, `smpl-interface-creators` | Software funcionando | Semanas/meses, multi-sessão |
| **B. Análise ad-hoc** | `iracing_analysis`, `smpl-daily-history-aqueles-caras`, `smpl_org-agencias` | Insight, planilha, lista | Horas/dias, 1–3 sessões |
| **C. Pesquisa/estudo** | `SMPL-research`, `alamtoco` | Aprendizado, tese, decisão | Contínuo, incremental |
| **D. Laboratório/infra** | `co-coach` | Skills, KB, automações | Contínuo, é o meta-projeto |

Regra de bolso para classificar projeto novo: **o resultado é código que vai viver? → A. É uma resposta a uma pergunta? → B. É entendimento acumulado? → C.**

---

## Arquétipo A — Produto/MVP (o mais importante: SMPL_MVP)

### Metodologia
1. **SDD completo é obrigatório.** Os 3 documentos (`requirements.md`, `design.md`, `TASKS.md`) antes de qualquer código. Use `/co-coach-sdd` para criar/validar. Base: curso DeepLearning.AI e as 6 perguntas do Addy Osmani (o quê, quem usa, limites, restrições, sucesso, riscos) — qualquer pergunta em aberto, o agente decide sozinho.
2. **Toda sessão começa com plan mode** (Shift+Tab): explorar → planejar → aprovar → implementar. Nunca "vai fazendo".
3. **Uma task do TASKS.md por vez.** Task atômica = cabe numa sessão. Se não cabe, quebre antes.
4. **Validate ≠ rodou.** Todo incremento precisa de verificação que o agente executa sozinho (teste, screenshot, amostra de dados conferida). É o que permite iterar sem você supervisionar cada passo.
5. **Fim de sessão: `/co-coach-handoff`** — o resumo em `memory/` é o que faz a próxima sessão começar em 2 minutos em vez de 20.
6. **Anti-over-engineering:** MVP é a menor coisa que funciona. A skill Ponytail (kb) existe exatamente para isso — considere instalá-la nos projetos deste arquétipo.

### Setup padrão
- **CLAUDE.md** com: o que é o produto, para quem, stack, comandos de rodar/testar, restrições, e o ciclo SDD (copiar o bloco do co-coach).
- **Specs:** `requirements.md`, `design.md`, `TASKS.md` na raiz.
- **Skills:** `co-coach-sdd`, `co-coach-handoff`, `co-coach-ui` (interfaces), `co-coach-mermaid` (diagramas de arquitetura).
- **MCPs:** só os do domínio do produto. SMPL_MVP: BigQuery e Sheets quando necessário; **HubSpot/Gmail desligados** durante desenvolvimento (ruído + risco).
- **Git:** repositório privado no GitHub desde o dia 1; commit ao fim de cada task concluída.
- **Dados sensíveis:** `.env` no `.gitignore` sempre; transações, cadastros de creators/clipadores e contratos só em amostras anonimizadas durante o desenvolvimento.

---

## Arquétipo B — Análise ad-hoc

### Metodologia
1. **Sem SDD** — o custo não se paga para trabalho de 1–3 sessões. Substituto: **plano em 3 bullets aprovado antes de executar** (sua regra global).
2. **Especifique o output antes da análise:** "quero uma planilha com abas Resumo/Detalhe/Qualidade" ou "quero 5 bullets de insight". Análise sem formato de saída definido vira exploração infinita.
3. **Validação por amostra é inegociável:** o agente confere N linhas contra a fonte e diz o que conferiu ("rodou ≠ está certo").
4. **BigQuery: sempre otimizar para escanear o mínimo** (partições, `LIMIT` em exploração, `SELECT` só das colunas usadas).
5. Se a mesma análise acontecer pela **3ª vez → vira skill** (`/co-coach-builder`). Duas vezes é coincidência, três é processo.

### Setup padrão
- **CLAUDE.md** curto: fontes de dados, dicionário das tabelas/colunas principais, convenções de saída (DD/MM/AAAA, R$), regra da amostra.
- **Skills:** `co-coach-bigquery`, `co-coach-xlsx`, `co-coach-analytics`.
- **MCPs:** só a fonte da análise (BigQuery OU Sheets OU HubSpot — não todos ao mesmo tempo; ferramenta demais confunde o agente, kb: tool curation).
- **Memória:** handoff só se a análise continuar amanhã; adhoc de um dia não precisa.

---

## Arquétipo C — Pesquisa/estudo

### Metodologia
1. **Toda pesquisa parte de uma pergunta escrita** — não de um tema. "Como a SMPL cobraria por outcome em vez de assento?" rende; "estudar SaaS 2.0" não.
2. **Use `/co-coach-research` ou `/co-coach-market`** para varreduras multi-fonte com citação — exigir fonte em toda afirmação.
3. **Todo achado vira nota permanente** no padrão da kb (frontmatter + bullets + "por que importa"). Pesquisa sem nota escrita evapora.
4. **Feche cada ciclo com uma decisão ou tese**, registrada no diário de decisões (`kb/decisoes/`) — pesquisa que não muda uma decisão é entretenimento.
5. `SMPL-research` e `alamtoco` estudam a mesma tese (SaaS 2.0) em empresas diferentes — **mantenha um índice comum de aprendizados** para um alimentar o outro.

### Setup padrão
- **CLAUDE.md** com: a pergunta central do projeto, teses atuais, o que já foi descartado.
- **Skills:** `co-coach-research`, `co-coach-market`, `co-coach-competitor`, `deep-research` (para relatórios profundos).
- **MCPs:** nenhum de dados internos; WebSearch/WebFetch são as ferramentas principais.
- **Estrutura:** `notas/` (achados), `decisoes/` (teses fechadas), `fontes/` (links e PDFs).

---

## Arquétipo D — Laboratório/infra (co-coach)

### Metodologia
1. co-coach é onde se **testa antes de propagar**: skill nova, plugin novo, configuração nova — experimenta aqui, e só depois sincroniza aos outros projetos via `sync-skills.yml`.
2. **Automação via GitHub Actions, nunca hooks locais** (decisão de 05/07 — tudo visível e auditável no repo).
3. Toda automação precisa **falhar visivelmente** (lição de 12/07: workflow verde com 100% de falha por API sem créditos).
4. Os 5 rituais de sessão (digest, sdd, support, handoff, quiz) continuam sendo o coração do uso.

### Setup padrão
- Já existe e está maduro. Mudanças aqui seguem o próprio SDD do projeto.

---

## Transversal 1 — Separação de contas (dor declarada nº 13)

Situação atual: terminal VS Code = pessoal, plugin Anthropic = SMPL. Funciona mas confunde.

**Recomendação: direnv** (já estudado em sessão de 07/07). Um arquivo `.envrc` em cada pasta-mãe define a conta automaticamente ao entrar:
- `~/Projetos/projetos-pessoais/.envrc` → perfil pessoal (padrão, `~/.claude`)
- `~/Projetos/projetos-smpl/.envrc` → `export CLAUDE_CONFIG_DIR=~/.claude-smpl`

Efeito: `cd` na pasta certa = conta certa, sem alias, sem lembrar de nada. Pré-requisito: fazer login uma única vez no perfil `~/.claude-smpl` (hoje ele existe mas está vazio).

## Transversal 2 — "Estou usando IA do jeito mais eficiente?" (dor nº 12)

A insegurança não se resolve com mais ferramentas — se resolve com **critérios de eficiência por arquétipo**:

| Arquétipo | Você está eficiente quando… |
|---|---|
| A. Produto | Cada sessão fecha ≥1 task do TASKS.md validada; retomar o projeto leva <5 min |
| B. Análise | O insight chega com amostra conferida na primeira entrega, sem retrabalho |
| C. Pesquisa | Cada ciclo fecha com nota escrita + decisão registrada |
| D. Lab | O que você testa aqui chega aos outros projetos sem esforço manual |

Ritual de calibração: 1× por mês, rode `/co-coach-review` no projeto mais ativo e compare com esta tabela.

## Transversal 3 — Dados sensíveis SMPL (regras fixas)

1. `.env` nunca é lido pelo agente, nunca commitado, nunca colado em chat.
2. Transações, cadastros (creators/clipadores) e contratos: trabalhar com amostras anonimizadas em desenvolvimento; dados reais só em produção.
3. MCPs de nuvem (Gmail, Drive, HubSpot) desligados nos projetos que manipulam esses dados localmente.
4. Antes de qualquer `git push` em repo SMPL: conferir `git status` por arquivos de dados que escaparam do `.gitignore`.

---

## Próximos passos sugeridos (em ordem)

1. **SMPL_MVP:** rodar `/co-coach-sdd` para criar os 3 documentos de spec — é o projeto mais importante e ainda é recém-criado.
2. **Contas:** implementar o direnv (30 min, resolve a dor nº 13 de vez).
3. **Entrevistas com os 13 funcionários:** usar o roteiro para identificar fluxos repetitivos → cada fluxo mapeado é candidato a virar skill/automação do SaaS 2.0 (e material dos workshops).
4. **Workshops de IA:** o formato instalável do co-coach (skills via sync) é a infraestrutura pronta para distribuir o que você ensinar.
