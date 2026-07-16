# TASKS — co-coach

> Derivado de requirements.md em 2026-07-16 (pivô: produto público instalável com modo tutor).
> Legenda: `[ ]` pendente · `[x]` feito · `[-]` descartado

---

## Fase 0 — Higienização (pré-requisito de tudo; ordem importa)

- [x] **Inventariar conteúdo pessoal/sensível** no repo: `Briefing`, `07-outros/` (briefing de cliente), `WORKFLOWS.md` (entrevista pessoal), `memory/`, `sessoes/`, `DESIGN-IS-2026-07-02/`, referências a SMPL/Service-as-a-Software em CLAUDE.md e kb/
- [x] **Mover o conteúdo pessoal** para pasta privada fora do repo (`~/Projetos/co-coach-pessoal/`)
- [x] **Avaliar limpeza de histórico do git** — não necessária: `07-outros/` e `Briefing` já eram ignorados pelo `.gitignore` e nunca entraram no histórico
- [x] Adicionar `perfil-do-aluno.md`, `memory/` e `sessoes/` ao `.gitignore`

## Fase 1 — Migração `00`–`06` → `kb/`

- [x] Criar estrutura `kb/guias/`, `kb/templates/`, `kb/trilha-anthropic/`
- [x] Converter os arquivos das pastas `00`–`04` e `06` para `kb/guias/` com frontmatter YAML válido (25 guias; `pontos-cegos-do-meu-raciocinio.md` era pessoal → pasta privada)
- [x] Mover `05-templates/` → `kb/templates/` (`tipo: template`; personas de exemplo genericizadas)
- [x] Adaptar `scripts/build-site.py` para o campo `tipo` e subpastas de `kb/` (rglob; `kb/decisoes/` agora entra no feed como `tipo: decisao`)
- [x] Validar rebuild do feed (138 conteúdos: 110 cards, 25 guias, 2 templates, 1 decisão) e apagar as pastas numeradas

## Fase 2 — Modo tutor (o coração do pivô)

- [x] **Reescrever `CLAUDE.md` como persona de tutor** — sempre perguntar antes de agir, uma pergunta por vez, explicar o porquê, nunca exigir YAML do aluno
- [x] **Criar skill `co-coach-start`**: entrevista de 6 perguntas → gera `perfil-do-aluno.md` → recomenda primeira lição por nível. O CLAUDE.md manda ler `skills/co-coach-start/SKILL.md` diretamente, então funciona num clone sem skill instalada (teste vivo fim-a-fim fica no teste de fumaça da Fase 3)
- [x] Adaptar `co-coach-quiz` e `co-coach-digest` para ler o perfil do aluno em vez de assumir o Victor (quiz agora grava progresso no perfil, não mais em `static/proficiency.json`)
- [x] Definir registro de progresso: seção `## Progresso` do perfil (lições concluídas + tabela de quizzes + próximo passo)
- [x] Remover hook de `SessionStart` que copiava template para `~/.claude/CLAUDE.md` — caminho quebrou na Fase 1 e escrever na memória global de um estranho seria invasivo; o wizard cumpre o papel com consentimento

## Fase 3 — Instalabilidade

- [ ] Reescrever `README.md` público: o que é, instalação em 3 passos, primeiro uso
- [ ] Esvaziar `config/sync-targets.yml` (deixar exemplo comentado)
- [ ] Documentar automações opcionais (feed, ingestão) como recurso avançado com secrets próprios
- [ ] **Teste de fumaça:** clonar o repo numa pasta limpa e percorrer o fluxo completo de onboarding

## Fase 4 — Trilha do curso Anthropic (Skilljar)

- [ ] Acessar o curso com login do Victor e mapear módulos/lições
- [ ] Criar cards `kb/trilha-anthropic/` — resumo em palavras próprias + link da lição + perguntas de verificação (nunca conteúdo verbatim)
- [ ] Integrar a trilha ao tutor: "próxima lição é o módulo X — faça lá e volte para o quiz"

---

## Backlog herdado (pré-pivô, reavaliar depois da Fase 3)

- [ ] Painel de proficiência do feed (`static/proficiency.json`) ficou órfão — o quiz agora grava no perfil local; decidir se o painel sai do feed ou passa a ler outra fonte

- [ ] Ingestão de playlists do YouTube (`scripts/ingest.py`)
- [ ] Gap analysis simples na KB (relatório de temas pouco cobertos)
- [ ] Changelog automático de KB no `ingest-link.yml`
- [ ] Step de verificação nos workflows (falhar se arquivo gerado estiver vazio/malformado)

## Feito (referência)

- [x] Spec do pivô reescrita: `requirements.md`, `design.md`, `TASKS.md` (2026-07-16)
- [x] Fase pessoal do projeto (pré-pivô): ingestão via Issue, feed mobile no ar, 30+ skills, sync automático, gerenciador local, memória de sessão — ver git log até 2026-07-16

## Descartado

- [-] iOS Shortcut (fluxo URL → Issue → feed)
- [-] Direcionamento exclusivo à tese Service-as-a-Software — sai do repo público; vira contexto pessoal do Victor fora daqui
