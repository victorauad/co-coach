# Everything Claude Code

**Repositorio:** github.com/affaan-m/everything-claude-code
**Estrelas:** 128k

## O que e?

Uma colecao gigante de recursos prontos para o Claude Code: 30 agentes especializados, 136 skills, 60 slash commands e hooks de automacao. E como um "pacote profissional" que expande o que o Claude Code consegue fazer por padrao.

## Para que serve?

Se voce usa o Claude Code no dia a dia e quer ir alem dos comandos basicos, esse repo entrega fluxos prontos para areas como seguranca, testes automatizados, documentacao, code review e muito mais — sem voce precisar criar tudo do zero.

**Exemplos de uso:**
- Rodar um agente de seguranca que escaneia vulnerabilidades no seu codigo
- Gerar testes automaticamente com um slash command
- Automatizar a criacao de documentacao tecnica
- Fazer code review padronizado com um comando so

## Instalacao

### Passo 1: Clonar o repositorio

```bash
git clone https://github.com/affaan-m/everything-claude-code.git
```

### Passo 2: Copiar os recursos para o Claude

Copie as regras da linguagem que voce usa (substitua `[linguagem]` por `python`, `javascript`, `typescript`, etc.):

```bash
cp -r everything-claude-code/rules/[linguagem] ~/.claude/rules/
```

Para copiar as skills:

```bash
cp -r everything-claude-code/skills/ ~/.claude/skills/
```

Para copiar os slash commands:

```bash
cp -r everything-claude-code/commands/ ~/.claude/commands/
```

### Passo 3: Verificar

Abra o Claude Code e digite `/` — voce vai ver os novos comandos disponíveis na lista.

## Dica

Comece pelos agentes de seguranca e testes — sao os mais maduros da colecao e entregam valor imediato.
