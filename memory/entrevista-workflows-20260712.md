# Entrevista — Workflows de IA por tipo de projeto

> Objetivo: mapear seus projetos (pessoais e SMPL) para estruturar, a partir da knowledge base do co-coach, workflows de metodologia ("como usar") e setup ("configuração") otimizados para cada tipo de projeto.
>
> Pode preencher por partes, fora de ordem, ou deixar perguntas em branco se não se aplicarem — é só editar este arquivo e me avisar quando quiser que eu leia e consolide.

---

## Bloco 1 — Inventário de projetos

**1. Liste seus projetos ativos hoje (pessoais e SMPL).**
Já tenho pista destes — confirme e complete:
- `co-coach` (base de conhecimento + skills)
- `iracing_analysis` (análise de dados de corrida)
- `AuaDriving` (criado em julho — qual o objetivo dele?)
- `alamtoco` (aparece nas suas pastas — o que é?)
- Projetos da SMPL: quais existem ou você pretende criar?

> Sua resposta:
> **Projetos pessoas, na pasta projetos-pessoais**
> 
> `co-coach` (base de conhecimento + skills)
>`iracing_analysis` (análise de dados de corrida)
> `AuaDriving` (webapp para analisar telemetria e ganhar insights de pilotagem no iRacing)
> `alamtoco` (projeto de pesqusia para estudar a estruturação da empresa AlamTec em SaaS 2.0)>
> 
> **Projetos da SMPL, na pasta projetos-smpl**
> 
> `SMPL-research` (projeto de pesquisa para estudar a estruturação da empresa SMPL em SaaS 2.0)
> `smpl-interface-creators` (projeto de MVP da interface de 01 dos atores da SMPL em SaaS 2.0, os creators)
> `smpl-daily-history-aqueles-caras` (adhoc - análise estatística para gerar insights de produção de conteúdo no Youtube)
> `smpl_org-agencias` (adhoc - python para transformar ~150 documentos em uma lista de contatos)
> `SMPL_MVP` (projeto recém-criado para ser o MVP da estruturação da SMPL em SaaS 2.0)

**2. Para cada um, qual é o "produto final" que sai dele?**
(ex.: relatório, dashboard, decisão, planilha, site, aprendizado)

> Sua resposta:
> **Projetos pessoas, na pasta projetos-pessoais**
> 
> `co-coach` (Usado para estudar AI, instalar/testar configurações)
>`iracing_analysis` (análise de dados de corrida)
> `AuaDriving` (webapp para analisar telemetria e ganhar insights de pilotagem no iRacing)
> `alamtoco` (projeto de pesqusia para estudar a estruturação da empresa AlamTec em SaaS 2.0)>
> 
> **Projetos da SMPL, na pasta projetos-smpl**
> 
> `SMPL-research` (aprendizado)
> `smpl-interface-creators` (interface web)
> `smpl-daily-history-aqueles-caras` (análise)
> `smpl_org-agencias` (lista de contatos)
> `SMPL_MVP` (O MVP da SMPL funcionando em SaaS 2.0)

**3. Quais desses você mexe toda semana e quais são esporádicos?**

> Sua resposta:
> Os meus pessoias eu mexo no meu tempo livre, de 2-4 horas/semana. Os da SMPL eu mexi semana passada, quando comecei lá. Para todos os efeitos, o `SMPL_MVP` é o projeto mais importante agora.

---

## Bloco 2 — Tipos de trabalho que você faz com IA

**4. Na SMPL, como Head de Growth: quais tarefas você já faz com Claude Code hoje, e quais gostaria de fazer?**
(ex.: análise de campanhas no BigQuery, relatórios de CRM/HubSpot, pesquisa de mercado, conteúdo, propostas comerciais)

> Sua resposta:
> Todos os exemplos - meu grande objetivo lá como Head de Growth é estruturar a SMPL em SaaS 2.0 e operar o crescimento da empresa por esse sistema

**5. Do seu trabalho recorrente, o que é repetitivo com formato fixo (mesmo relatório toda semana) vs. exploratório (cada análise é diferente)?**
Isso define o que vira skill/automação vs. o que fica como conversa.

> Sua resposta:
> Na SMPL eu ainda não tenho essa visibilidade. Como estou focado no SaaS 2.0, eu tenho tarefas pontuais se forem de importância para os sócios - o projeto `smpl-inteface-creators` nasceu disso, eu só usei a situação para já estruturar um pequeno pedaço do `SMPL_MVP`

**6. Existe algo que hoje você faz manualmente e desconfia que dava para automatizar de ponta a ponta (sem você no meio)?**

> Sua resposta:
> Por enquanto não. Essa semana terei entrevistas com os funcionários da SMPL (13 ao todo) para entender quais são esses fluxos, mas da SMPL como um todo - nao sao fluxos meus.

---

## Bloco 3 — Dados, ferramentas e sensibilidade

**7. Quais fontes de dados cada contexto usa?**
(SMPL: BigQuery, HubSpot, Sheets…? Pessoal: arquivos locais, APIs…?)

> Sua resposta:
> SMPL: BQ, Hubspot, Sheets, API’s do YouTube, API’s do TikTok, API’s do Instagram, e mais fontes que estou mapeando ou terei que construir no projeto de Saas 2.0

**8. O que é dado sensível em cada projeto — o que nunca pode sair para serviços externos?**
Isso define quais MCPs e ferramentas podem estar ativos em cada projeto.

> Sua resposta:
> Na SMPL, teremos tabelas de bancos de dados com dados de transações financeiras, cadastro de creators, contratos, cadastro de clipadores. Acho que esses são os principais dados sensíveis - além dos logins que serão usados para integrar todas as fontes e bancos (os arquivos .env)

**9. Na SMPL, existe alguma política ou restrição da empresa sobre uso de IA que os workflows precisam respeitar?**

> Sua resposta:
> Não

---

## Bloco 4 — Pessoas e colaboração

**10. Nos projetos da SMPL, você trabalha sozinho com a IA ou o resultado passa por outras pessoas (revisão, aprovação, apresentação)? Quem consome o que você produz?**

> Sua resposta:
> Poucas pessoas usam, para poucas tarefas…eu sei que os sócios usam para fazer apresentações

**11. Alguém mais da SMPL usa ou vai usar Claude Code?**
Define se os workflows precisam ser "instaláveis" para o time, como o co-coach faz com skills.

> Sua resposta:
> Minha idéia como Head de Growth, além de construir o SaaS 2.0, é ter workshops recorrentes de IA com os funcionários da SMPL para incentivar e ensinar o uso

---

## Bloco 5 — Dores e critério de sucesso

**12. Qual é a sua maior fricção hoje ao usar Claude Code?**
(ex.: perder contexto entre sessões, retrabalho explicando o projeto, resultados que "rodam mas estão errados", não saber qual skill usar)

> Sua resposta:
> Por não ter experiência como dev (eu entendo o básico de bancos de dado, sei ler python e entender API's) mas muita experiência com negócio, eu nunca tenho certeza se estou estudando/criando/análisando do jeito mais eficiente usando o Claude Code (ou IA no geral)

**13. Já sabemos que você tem as duas contas (pessoal e SMPL) com troca por alias — a separação está funcionando ou ainda atrapalha?**

> Sua resposta:
> Ainda atrapalha. Estou tendo que usar o terminal do VisualStudio para a conta pessoal e o plugin da Anthropic no VisualStudio para a SMPL

**14. Daqui a 3 meses, o que teria que ser verdade para você dizer "meus workflows de IA estão redondos"?**

> Sua resposta:
> Além de ter a SMPL em SaaS 2.0, saber que eu estou usando IA do jeito mais eficiente - maximizando a aplicabilidade da tecnologia

---

## Depois de preenchido

Quando terminar, me avise (ex.: "preenchi a entrevista") que eu leio este arquivo, cruzo com a knowledge base (`kb/`) e monto:
- **(a)** uma tipologia dos seus projetos (arquétipos como "análise recorrente", "POC/produto", "base de conhecimento")
- **(b)** para cada arquétipo, o workflow de uso (quando usar SDD, plan mode, delegar a agente)
- **(c)** o setup padrão (CLAUDE.md, skills, MCPs ativos, memória, permissões)
