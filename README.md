# co-coach — aprenda a usar IA com um tutor dentro do seu terminal

O co-coach é um **tutor instalável**. Você clona este repositório, abre o Claude Code dentro dele, e é recebido por um tutor que te entrevista, monta seu plano de aprendizado e te ensina a usar IA aplicada ao trabalho — na prática, em português, sem exigir que você saiba programar.

Não é um curso em vídeo nem uma pilha de documentação: é uma pasta que transforma o Claude Code num professor particular.

## Instalação em 3 passos

1. **Instale o Claude Code** (precisa de uma conta Claude): siga [code.claude.com/docs](https://code.claude.com/docs)
2. **Clone este repositório:**
   ```bash
   git clone https://github.com/victorauad/co-coach.git
   cd co-coach
   ```
3. **Inicie o tutor:**
   ```bash
   claude
   ```

Na primeira vez, o tutor vai se apresentar e fazer 6 perguntas rápidas (como um assistente de instalação). Suas respostas viram o `perfil-do-aluno.md` — um arquivo que fica **só na sua máquina** e faz o tutor lembrar de você entre sessões.

> Se o tutor não iniciar o wizard sozinho, diga: **"quero começar do zero"**.

## O que tem dentro

| Onde | O que é |
|---|---|
| `kb/guias/` | Guias de aprendizado: instalação, primeiro dia, prompts, skills, agentes, fluxos de trabalho reais |
| `kb/templates/` | Modelos prontos para copiar para os seus projetos (CLAUDE.md, settings, skill de exemplo) |
| `kb/trilha-anthropic/` | Trilha guiada do curso oficial da Anthropic — resumos e links, com o tutor acompanhando |
| `kb/*.md` | Cards de conteúdo indexado (artigos, vídeos e repositórios), filtráveis por tema |
| `skills/` | Habilidades do tutor: quiz, digest de novidades, criador de projetos e mais |

## Como o aprendizado funciona

- **Uma pergunta por vez.** O tutor nunca te sobrecarrega — cada sessão avança um passo.
- **Aprender fazendo.** Em vez de teoria, exercícios pequenos no seu contexto real de trabalho.
- **Progresso persistente.** Lições concluídas e resultados de quiz ficam no seu perfil; a cada sessão o tutor sugere o próximo passo.
- **Três comandos para guardar:**
  - `/co-coach-digest` — "o que tem de novo pra eu estudar?"
  - `/co-coach-quiz` — testar o que você aprendeu
  - `/co-coach-handoff` — salvar a sessão antes de sair

## Recursos avançados (opcionais)

O repositório também traz automações que **não são necessárias** para aprender — funcionam só se você fizer um fork e configurar:

- **Feed mobile** — site estático gerado de `kb/` (GitHub Pages). Ative o Pages no seu fork apontando para a pasta `docs/`.
- **Ingestão automática de links** — GitHub Action que transforma Issues com URL em cards da KB (requer `ANTHROPIC_API_KEY` nos secrets do fork).
- **Sync de skills** — distribui as skills deste repo para outros repositórios seus (edite `config/sync-targets.yml` no fork).

## Contribuindo

O projeto segue Spec-Driven Development: `requirements.md` (o quê), `design.md` (como) e `TASKS.md` (backlog). Leia os três antes de propor mudanças.

---
*O Claude Code muda rápido — em caso de dúvida sobre instalação ou features, a fonte é a doc oficial: [code.claude.com/docs](https://code.claude.com/docs)*
