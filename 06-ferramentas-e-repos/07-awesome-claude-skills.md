# Awesome Claude Skills

**Repositorio:** github.com/travisvn/awesome-claude-skills
**Instalacoes:** 22k+

## O que e?

Um marketplace comunitario de skills para o Claude Code. Enquanto as skills oficiais da Anthropic cobrem casos basicos, essa colecao traz centenas de skills criadas pela comunidade para areas especificas: SEO, marketing, seguranca, design, financas, juridico e muito mais.

## Para que serve?

Expandir as capacidades do Claude Code com conhecimento especializado de dominios que voce usa no trabalho. Em vez de escrever prompts longos explicando contexto toda vez, uma skill encapsula esse conhecimento e o Claude ja sabe como agir.

**Exemplos de uso:**
- Skill de SEO: analisa um texto e sugere otimizacoes automaticamente
- Skill de seguranca: audita codigo buscando vulnerabilidades especificas
- Skill de design: avalia interfaces seguindo principios de UX
- Skill juridica: revisa contratos buscando clausulas problematicas

## Instalacao

### Opcao 1: Via comando do plugin (se disponivel)

```bash
/plugin marketplace add travisvn/awesome-claude-skills
```

### Opcao 2: Instalacao manual

```bash
git clone https://github.com/travisvn/awesome-claude-skills.git
```

Navegue pela pasta e copie as skills que te interessam:

```bash
# Exemplo: copiar as skills de SEO
cp -r awesome-claude-skills/seo ~/.claude/skills/

# Exemplo: copiar as skills de seguranca
cp -r awesome-claude-skills/security ~/.claude/skills/

# Copiar tudo
cp -r awesome-claude-skills/skills/* ~/.claude/skills/
```

### Passo 3: Usar no Claude Code

As skills ficam disponiveis automaticamente. Voce pode:
- Referenciar diretamente: `@seo-analyzer`
- Ou simplesmente descrever a tarefa — o Claude escolhe a skill certa

## Como escolher quais instalar?

Comece pelas areas do seu trabalho diario. Se voce e dev, pegue as de seguranca e code review. Se e de marketing, as de SEO e copywriting. Nao precisa instalar tudo — so o que vai usar.
