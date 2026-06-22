---
titulo: "VS Code: Terminal Integrado"
tema: ferramentas
url: https://code.visualstudio.com/docs/terminal/basics
data: 2026-06-22
fonte: vscode-docs
importancia: alta
---

# VS Code: Terminal Integrado

Como usar e personalizar o terminal embutido no VS Code — sem precisar alternar janelas.

## Abrir o Terminal

| Método | Ação |
|--------|------|
| Atalho | ⌃` (Mac) / Ctrl+` (Win/Linux) |
| Novo terminal | ⌃⇧` (Mac) / Ctrl+Shift+` |
| Menu | Terminal > New Terminal |
| Command Palette | "View: Toggle Terminal" |
| Via Explorer | Clique direito em pasta → Open in Integrated Terminal |

## Múltiplos Terminais

- **Adicionar**: ícone `+` na barra de terminais ou `Ctrl+Shift+``
- **Remover**: passe o mouse sobre a aba → ícone de lixeira, ou `Delete`
- **Alternar**: clique nas abas ou `Ctrl+PageUp/Down`

## Split (Terminais Lado a Lado)

Divida o painel de terminal para ver dois terminais simultaneamente:
- `⌘\` (Mac) / `Ctrl+Shift+5` (Win)
- Menu direito na aba → **Split**
- `Alt + clique` em uma aba
- Navegue entre splits: `Alt+Left` / `Alt+Right`

## Atalhos de Terminal

| Função | macOS | Windows/Linux |
|--------|-------|---------------|
| Toggle terminal | ⌃` | Ctrl+` |
| Novo terminal | ⌃⇧` | Ctrl+Shift+` |
| Split terminal | ⌘\ | Ctrl+Shift+5 |
| Foco terminal anterior | ⇧⌘[ | Ctrl+PageUp |
| Foco terminal seguinte | ⇧⌘] | Ctrl+PageDown |
| Buscar no terminal | ⌘F | Ctrl+F |
| Scroll uma linha | ⌥⌘PageUp/Down | — |
| Scroll uma página | PageUp/Down | PageUp/Down |
| Topo / fim | ⌘Home/End | Ctrl+Home/End |

## Configuração Inicial do Diretório

O terminal abre na raiz do workspace por padrão. Configure com:
```json
"terminal.integrated.cwd": "/caminho/especifico"
```

Para terminais split no Mac/Linux, herdam o diretório do terminal original. Configure com `terminal.integrated.splitCwd`.

## GitHub Copilot no Terminal

- `Cmd+I` — abre chat inline para ajuda com comandos
- `@terminal` no chat panel — participante especializado em terminal

Útil para: "como listo todos os arquivos modificados nos últimos 3 dias?" — o Copilot sugere o comando correto.

## Perfis de Terminal

O VS Code detecta automaticamente shells disponíveis (bash, zsh, PowerShell, Git Bash, WSL) e os apresenta no dropdown do `+`. Configure perfis personalizados em `terminal.integrated.profiles`.

## Automação com Tasks

Automatize a abertura de terminais ao iniciar um workspace via `.vscode/tasks.json`. Configure tarefas recorrentes (servidores, watchers) que abrem terminais automaticamente.

## Dimensões Fixas

Command Palette → **Terminal: Set Fixed Dimensions** → define colunas e linhas. Adiciona scrollbars quando o conteúdo excede o tamanho.

## Links Clicáveis

O terminal detecta automaticamente URLs, caminhos de arquivo e números de linha em mensagens de erro → clique para abrir diretamente no editor. Funcionalidade chamada de "sofisticada detecção de links com integração de editor".
