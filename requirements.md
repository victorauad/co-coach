# requirements.md — co-coach

> O quê o sistema precisa fazer. Fonte de verdade para objetivos e histórias de usuário.
> Atualizado em: 2026-07-04 (direção de aprendizado voltada à tese Service-as-a-Software / novo papel na SMPL)

---

## Objetivo do sistema

O co-coach é um sistema pessoal de aprendizado e produtividade para Victor — Head de Growth e Produto na SMPL — que usa Claude Code como ferramenta de trabalho, não como desenvolvedor. O sistema deve:

1. Capturar conteúdo relevante sobre Claude Code, IA e ferramentas com o mínimo de fricção
2. Tornar esse conteúdo acessível no celular, filtrado por tema e contexto
3. Distribuir habilidades (skills) especializadas para todos os projetos ativos automaticamente
4. Dar visibilidade para o Victor de todos os projetos ativos ao mesmo tempo numa visão de Kanban usando a @TASKS.md de cada projeto
5. **Ensinar Victor a usar Claude Code enquanto constrói funcionalidades reais no próprio co-coach** — aprender fazendo, não lendo documentação. Esse ensino deve acontecer através de interfaces visuais (feed, gerenciador, diagramas), nunca exigindo que Victor leia ou edite YAML, hooks ou arquivos de configuração para entender o que está acontecendo (decisão registrada em 2026-07-04, ver `kb/decisoes/`)
6. **Direcionar esse aprendizado para a tese Service-as-a-Software da Sequoia** (agentes de IA entregando trabalho de serviço, precificado por outcome em vez de assento/licença) — porque Victor vai aplicá-la na prática na SMPL, no papel de Head de Growth e Produto. Isso significa priorizar, dentro da KB e do caminho de estudo, os temas que sustentam essa tese: arquitetura de produto AI-first, agentes autônomos, pricing por outcome, e cases reais de empresas fazendo essa transição

---

## Histórias de usuário

### Ingestão de conteúdo

- **Como** Victor, **quero** compartilhar uma URL pelo iPhone **para que** ela seja sumarizada e apareça no feed em menos de 3 minutos, sem abrir o computador
- **Como** Victor, **quero** que repositórios que eu estrelo no GitHub sejam indexados automaticamente toda semana **para que** eu não precise fazer isso manualmente
- **Como** Victor, **quero** que o Claude extraia título, tema, pontos principais e nota de relevância de cada link **para que** eu não precise ler o conteúdo completo para decidir se vale a pena

### Feed mobile

- **Como** Victor, **quero** acessar todos os cards pelo celular com filtro por tema **para que** eu encontre o que preciso rapidamente durante uma sessão de trabalho
- **Como** Victor, **quero** ver a data do último rebuild e o total de cards por tema no feed **para que** eu saiba se o sistema está atualizado

### Skills

- **Como** Victor, **quero** criar uma skill em um lugar só **para que** ela fique disponível automaticamente em todos os meus projetos (iracing_analysis, alamtoco, novos futuros)
- **Como** Victor, **quero** invocar uma skill com `/co-coach-nome` em qualquer projeto **para que** o Claude execute um comportamento especializado sem eu precisar re-explicar o contexto

### Gerenciamento

- **Como** Victor, **quero** editar skills, ver os cards da KB e configurar sync pelo browser **para que** eu não precise editar arquivos de texto manualmente
- **Como** Victor, **quero** visualizar o sistema como um diagrama **para que** eu consiga explicar como funciona para outra pessoa
- **Como** Victor, **quero** poder visualizar todos os meus projetos ativos que tem o co-coach instalado em um lugar só, numa visã de Kan-ban, por meio do arquivo tasks.md de cada projeto.

### Aprender fazendo

- **Como** Victor, **quero** que funcionalidades novas do co-coach sejam construídas comigo e explicadas no processo **para que** eu aprenda Claude Code na prática, não só receba o resultado pronto
- **Como** Victor, **quero** que toda automação nova me seja explicada e exposta por uma interface visual **para que** eu não precise entender YAML, hooks ou configs de texto para confiar que o sistema funciona — tenho dificuldade de aprendizado por esse tipo de conteúdo
- **Como** Victor, **quero** que o conteúdo indexado e as sugestões de aprendizado priorizem a tese Service-as-a-Software **para que** eu desenvolva a base técnica e conceitual que preciso para o meu papel de Head de Growth e Produto na SMPL

---

## Critérios de aceitação globais

- Toda ingestão de link deve gerar um card com: `titulo`, `tema`, `url`, `data`, `importancia` (1–5) e pelo menos 3 bullets
- O feed deve reconstruir em menos de 5 minutos após um push em `kb/**`
- Skills distribuídas devem aparecer em `.claude/skills/` dos repos de destino sem intervenção manual
- O sistema deve funcionar sem que Victor precise saber programar para operá-lo no dia a dia
- Nenhuma automação nova deve depender de Victor entender ou editar hooks/config locais (`.claude/settings.json`) para confiar que ela funciona — se a automação precisa de configuração técnica, ela roda no servidor (GitHub Actions) e entrega o resultado por uma interface visual

---

## Fora do escopo

- Multi-usuário — o sistema é pessoal, para Victor apenas
- Autenticação — não há outros usuários
- Processamento de vídeos longos (>30 min) de YouTube sem transcrição disponível
- Interface mobile nativa (app) — o feed mobile é um site responsivo
