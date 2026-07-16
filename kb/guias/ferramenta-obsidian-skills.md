---
titulo: Obsidian Skills
tema: ferramentas
tipo: guia
data: 2026-06-06
importancia: 3
---

# Obsidian Skills

**Repositorio:** github.com/kepano/obsidian-skills

## O que e?

Uma camada de integracao que conecta o Claude Code com o Obsidian — o popular aplicativo de notas baseado em Markdown. Com essas skills, o Claude entende a estrutura do seu vault do Obsidian (pastas, links entre notas, tags, templates) e consegue trabalhar diretamente com seu sistema de conhecimento pessoal.

## Para que serve?

Se voce usa o Obsidian para guardar conhecimento, ideias, projetos e pesquisas, essas skills permitem que o Claude navegue e manipule esse conhecimento como se fosse um assistente que conhece seu sistema de notas.

**Exemplos de uso:**
- "Crie uma nota de reuniao seguindo meu template padrao"
- "Resuma todas as notas com a tag #projeto-x"
- "Quais notas estao relacionadas com esse topico?" (usando os links do Obsidian)
- "Mova essas notas para a pasta certa seguindo minha estrutura"
- Gerar conexoes entre notas que voce ainda nao percebeu

## Pre-requisito

- Ter o Obsidian instalado (obsidian.md)
- Seu vault do Obsidian configurado localmente

## Instalacao

### Passo 1: Clonar o repositorio

```bash
git clone https://github.com/kepano/obsidian-skills.git
```

### Passo 2: Copiar as skills

```bash
cp -r obsidian-skills ~/.claude/skills/obsidian
```

### Passo 3: Configurar o caminho do seu vault

Edite o arquivo de configuracao da skill para apontar para seu vault:

```bash
# Abra o arquivo de config
nano ~/.claude/skills/obsidian/config.md
```

Altere a linha do caminho:
```
vault_path: /Users/seu-usuario/Documents/MeuVault
```

### Passo 4: Usar no Claude Code

No Claude Code, voce ja pode referenciar suas notas:

```
@obsidian crie uma nota de reuniao sobre o projeto Alpha
```

## Dica

Funciona melhor se voce tem uma estrutura consistente no Obsidian (pastas organizadas, templates definidos). Quanto mais organizado o vault, mais preciso o Claude consegue ser.
