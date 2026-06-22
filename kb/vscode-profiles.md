---
titulo: "VS Code: Profiles (Perfis de Configuração)"
tema: ferramentas
url: https://code.visualstudio.com/docs/editor/profiles
data: 2026-06-22
fonte: vscode-docs
importancia: media
---

# VS Code: Profiles

Profiles permitem criar conjuntos de configurações e alternar entre eles rapidamente — ou compartilhá-los com outras pessoas.

## O que um Profile Inclui

- Extensões instaladas
- Settings (configurações)
- Atalhos de teclado
- Snippets
- Tema visual
- Layout da interface

## Como Criar um Profile

1. File > Preferences > Profiles (ou botão ⚙️ na Activity Bar)
2. Clique em **New Profile**
3. Escolha: copiar de template, copiar de profile existente, ou criar vazio
4. Selecione quais componentes incluir (pode herdar o resto do Default)
5. **Preview** antes de confirmar

## Templates Disponíveis

O VS Code já vem com templates prontos:
- **Python** — extensões Python, formatter Ruff
- **Data Science** — Jupyter, Data Wrangler, GitHub Copilot
- **Node.js** — ESLint, Jest, Prettier
- **Doc Writer** — spell checker, Markdown, lint
- **Angular, Java, Java Spring**

## Alternar entre Profiles

- Command Palette → **Profiles: Switch Profile**
- Clique em **Use this Profile for Current Window** no editor de Profiles
- O Profile ativo aparece no título da janela

## Associar Profile a uma Pasta/Projeto

Ao abrir uma pasta e ativar um Profile, o VS Code lembra essa associação. Na próxima vez que abrir a pasta, o Profile certo é ativado automaticamente.

## Exportar e Compartilhar

### Via GitHub Gist
- Clique em **Export...** no Profile → salva como Gist secreto
- Você recebe uma URL: `https://vscode.dev/editor/profile/github/{GUID}`
- Compartilhe o link — quem acessa pode importar direto

### Via Arquivo Local
- Exporta como `.code-profile`
- Útil para backup ou distribuição por email/repositório

## Importar Profile

No editor de Profiles → **Import Profile...** → cole a URL do Gist ou selecione o arquivo `.code-profile`.

## Casos de Uso Práticos

- **Trabalho com dados**: profile com Jupyter, Python, Data Wrangler ativados
- **Escrita/Documentação**: spell checker, Markdown preview, sem linters de código
- **Apresentações**: fonte maior, tema de alto contraste, sem distrações
- **Diagnóstico de problemas**: profile vazio desativa todas as extensões para isolar bugs

## Linha de Comando

```bash
code ~/meu-projeto --profile "Data Science"
```

Se o Profile não existir, um novo vazio é criado automaticamente.

## Temporary Profile

Para testar extensões sem afetar seus profiles: Command Palette → **Profiles: Create a Temporary Profile**. Desaparece ao fechar o VS Code.

## Localização dos Arquivos

- **Mac**: `~/Library/Application Support/Code/User/profiles/`
- **Windows**: `%APPDATA%\Code\User\profiles\`
