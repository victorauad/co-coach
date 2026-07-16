# design.md — co-coach

> Como o sistema está construído. Decisões técnicas, arquitetura e restrições.
> Atualizado em: 2026-07-16 (pivô: produto público instalável com modo tutor)

---

## Ideia central de arquitetura

O co-coach **não tem backend**. O "produto" é contexto bem desenhado que o Claude Code lê ao abrir a pasta:

```
[PESSOA]                [TUTOR]                       [CONTEÚDO]
clona o repo    →   CLAUDE.md (persona tutor)    →   kb/ (guias, trilhas, cards)
roda `claude`   →   skill co-coach-start (wizard) →  perfil-do-aluno.md (gerado)
```

Camadas opcionais (herdadas da fase pessoal, desligadas por padrão num clone):
feed mobile em GitHub Pages, ingestão automática de links, sync de skills para outros repos.

---

## Camada 1 — Modo tutor (`CLAUDE.md` + `perfil-do-aluno.md`)

**Tecnologia:** só contexto — nenhum código.

- `CLAUDE.md` define a persona: sempre perguntar antes de agir, uma pergunta por vez, explicar o porquê em linguagem simples, nunca exigir que o aluno leia YAML/configs.
- `perfil-do-aluno.md` (gerado pelo wizard, ignorado pelo git via `.gitignore`) guarda: quem é o aluno, objetivo, nível, lições concluídas, resultado dos quizzes.
- A cada sessão, o tutor lê o perfil antes de qualquer recomendação.

**Restrição:** o perfil é local e por clone — não há sincronização entre máquinas (fora do escopo).

---

## Camada 2 — Wizard de onboarding (`skills/co-coach-start/`)

Evolução do antigo `co-coach-wizard`. Fluxo:

1. Detecta ausência de `perfil-do-aluno.md` → inicia entrevista (nome, objetivo, nível, contexto de trabalho)
2. Gera o perfil e apresenta o mapa do conteúdo disponível
3. Recomenda a primeira lição da trilha

**Restrição crítica de skills (herdada):** frontmatter do `SKILL.md` aceita só `name:` e `description:` em texto corrido — listas YAML quebram a leitura silenciosamente no Claude Code.

---

## Camada 3 — Knowledge Base (`kb/`)

**Tecnologia:** arquivos `.md` com frontmatter YAML (formato herdado, estendido).

```yaml
titulo: string (máx 80 chars)
tema: setup | metodologia | agentes | mcp | ferramentas | workflow | prompts | outros
tipo: card | guia | template | trilha      # novo campo do pivô
url: string (opcional para guias)
data: YYYY-MM-DD
importancia: 1-5
```

**Estrutura após a migração das pastas numeradas:**

```
kb/
├── *.md                  ← cards de links (formato antigo, ~111 arquivos)
├── guias/                ← ex-00 a 04 e 06 (comece-aqui, setup, fluxos, metodologias, ferramentas)
├── templates/            ← ex-05-templates
└── trilha-anthropic/     ← resumos próprios + links do curso oficial (Skilljar)
```

**Regra da trilha-anthropic:** nunca reproduzir o conteúdo do curso — cada arquivo tem resumo em palavras próprias, o link da lição oficial e perguntas de verificação que o tutor usa.

---

## Camadas opcionais (desligadas por padrão)

Herdadas da fase pessoal do projeto; um clone funciona 100% sem elas:

- **Feed mobile** — `scripts/build-site.py` gera `docs/` (GitHub Pages). Só roda se a pessoa habilitar Pages no fork.
- **Ingestão de links/stars** — `ingest-link.yml`, `ingest-github-stars.yml`. Exigem `ANTHROPIC_API_KEY` como secret; documentadas como recurso avançado.
- **Sync de skills** — `sync-skills.yml` + `config/sync-targets.yml` (vazio por padrão, com exemplo comentado).

---

## Decisões técnicas e seus motivos

| Decisão | Motivo |
|---|---|
| Produto = contexto, não software | O Claude Code já é o motor; CLAUDE.md + skills + KB entregam o tutor sem backend |
| Perfil do aluno como `.md` local no `.gitignore` | Persistência entre sessões sem banco de dados; privacidade por padrão |
| Repo único público (sem fork pessoal) | Simplicidade de manutenção; conteúdo pessoal sai do repo (decisão 2026-07-16) |
| Idioma PT-BR | Quase não há material de Claude Code para não-devs em português — é o diferencial |
| Trilha Anthropic por resumos + links | Direitos autorais impedem cópia; apontar para a fonte oficial é pedagogicamente melhor |
| Automações opcionais e desligadas por padrão | Critério de aceitação: funcionar num clone sem token nenhum |
| Arquivos `.md` em vez de banco | Zero infraestrutura; git nativo; editável por humano |

---

## Restrições

- Nenhum dado pessoal do mantenedor ou de clientes no repo (nem no histórico, quando sensível)
- Nenhuma automação nova pode ser pré-requisito do fluxo principal de aprendizado
- O tutor nunca exige que o aluno edite arquivos de configuração para confiar no sistema — automações avançadas rodam no servidor (GitHub Actions) e entregam resultado por interface visual
- Conteúdo de terceiros entra só como resumo próprio + link

## O que NÃO está documentado aqui

- Código e lógica de implementação — estão nos arquivos de código
- Histórico de mudanças — está no git log
