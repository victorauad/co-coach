# requirements.md — co-coach

> O quê o sistema precisa fazer. Fonte de verdade para objetivos e histórias de usuário.
> Atualizado em: 2026-07-16 (pivô: de sistema pessoal do Victor para produto público instalável)

---

## Objetivo do sistema

O co-coach é um **tutor de IA instalável**: um repositório público que qualquer pessoa clona e, ao abrir o Claude Code dentro dele, é recebida por um tutor que ensina a usar IA aplicada ao trabalho — na prática, em português, sem exigir conhecimento de programação.

O tutor funciona como um wizard de instalação: coleta contexto por perguntas (uma de cada vez), monta um perfil do aluno, e a partir dele recomenda lições da knowledge base e da trilha oficial da Anthropic. O aprendizado acontece fazendo, dentro do próprio Claude Code.

**Problema que resolve:** aprender Claude Code hoje exige ler documentação técnica em inglês. Não existe um "tutor instalável" em português que ensine fazendo, adaptado ao contexto de quem não é desenvolvedor.

---

## Histórias de usuário

### Onboarding (o wizard)

- **Como** pessoa nova, **quero** clonar o repo, rodar `claude` e ser recebida por um tutor que se apresenta e me entrevista **para que** eu comece a aprender sem ler nenhuma documentação antes
- **Como** pessoa nova, **quero** que o tutor faça uma pergunta de cada vez, com opções claras, **para que** eu nunca fique perdida sobre o que responder
- **Como** aluna, **quero** que minhas respostas virem um perfil persistente (`perfil-do-aluno.md`) **para que** o tutor lembre de mim entre sessões e não repita perguntas

### Modo tutor (contínuo)

- **Como** aluna, **quero** que o tutor sempre pergunte antes de agir e explique o porquê em linguagem simples **para que** eu entenda o que está acontecendo, não só receba o resultado
- **Como** aluna, **quero** que a cada sessão o tutor sugira a próxima lição com base no meu perfil e no que já estudei **para que** eu tenha um caminho, não uma pilha de conteúdo
- **Como** aluna, **quero** ser testada com quizzes curtos sobre o que estudei **para que** eu saiba se realmente aprendi

### Knowledge base

- **Como** aluna, **quero** que todo o conteúdo de aprendizado (guias, metodologias, templates, ferramentas) esteja em `kb/`, organizado por tema **para que** o tutor e eu encontremos tudo num lugar só
- **Como** aluna, **quero** seguir a trilha do curso oficial da Anthropic (resumos próprios + links para as lições) **para que** eu estude a fonte oficial com o tutor me acompanhando

### Instalação e manutenção

- **Como** pessoa nova, **quero** instalar em no máximo 3 passos (instalar Claude Code → clonar → rodar `claude`) **para que** a barreira de entrada seja mínima
- **Como** mantenedor, **quero** que as automações opcionais (feed, ingestão de links) sejam documentadas mas desligadas por padrão **para que** o repo funcione num clone sem nenhum token ou configuração

---

## Critérios de aceitação globais

- Uma pessoa que nunca viu o projeto clona o repo, roda `claude`, e o wizard de boas-vindas inicia sem nenhuma edição de arquivo (MVP)
- O perfil do aluno persiste entre sessões e o tutor o consulta antes de recomendar qualquer lição
- Todo conteúdo de aprendizado vive em `kb/` com frontmatter YAML válido; as pastas numeradas `00`–`07` não existem mais
- O repo público não contém nenhum dado pessoal do mantenedor nem de clientes (nem no histórico do git, quando sensível)
- Nenhum conteúdo do curso da Anthropic é reproduzido verbatim — apenas resumos em palavras próprias e links para as lições oficiais
- O sistema funciona sem que o usuário precise saber programar

---

## Fora do escopo

- Dados pessoais do mantenedor no repo (contexto SMPL, briefings de cliente, memórias de sessão pessoais)
- Backend ou servidor obrigatório — o produto é contexto (CLAUDE.md + skills + KB), não software hospedado
- App mobile nativo — o feed continua sendo site estático opcional
- Republicação de material com direitos autorais (curso Anthropic, artigos pagos)
- Conteúdo em outros idiomas — o produto é PT-BR (decisão de 2026-07-16)
- Multi-tenancy/contas — cada pessoa tem seu próprio clone; o perfil é um arquivo local
