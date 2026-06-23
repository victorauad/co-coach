---
titulo: "VS Code: Tips & Tricks de Produtividade"
tema: ferramentas
url: https://code.visualstudio.com/docs/getstarted/tips-and-tricks
data: 2026-06-22
fonte: vscode-docs
importancia: alta
---

# VS Code: Tips & Tricks

Funcionalidades escondidas e atalhos que fazem diferença no dia a dia.

## Atalhos de Navegação Essenciais

| Função | macOS | Windows/Linux |
|--------|-------|---------------|
| Command Palette (acesso a tudo) | ⇧⌘P | Ctrl+Shift+P |
| Quick Open (arquivo por nome) | ⌘P | Ctrl+P |
| Pastas recentes | ⌃R | Ctrl+R |
| Símbolo no workspace | ⌘T | Ctrl+T |
| Toggle Sidebar | ⌘B | Ctrl+B |
| Toggle Panel inferior | ⌘J | Ctrl+J |
| Terminal | ⌃` | Ctrl+` |
| Zen Mode | ⌘K Z | Ctrl+K Z |

## Edição Poderosa

### Multi-Cursor (editar múltiplos pontos ao mesmo tempo)
- `Option+Click` (Mac) / `Alt+Click` (Win) — coloca cursor em qualquer ponto
- `⌥⌘↑/↓` / `Ctrl+Alt+Up/Down` — adiciona cursores acima/abaixo
- `⇧⌘L` / `Ctrl+Shift+L` — seleciona TODAS as ocorrências da palavra
- `⌘D` / `Ctrl+D` — seleciona próxima ocorrência (uma a uma)
- `Shift+Alt+Drag` — seleciona bloco de texto em coluna

### Operações de Linha
- `⇧⌥↑/↓` / `Shift+Alt+Up/Down` — duplica linha acima/abaixo
- `⌥↑/↓` / `Alt+Up/Down` — move linha para cima/baixo
- `⌘L` / `Ctrl+L` — seleciona a linha inteira
- `⌘K ⌘X` / `Ctrl+K Ctrl+X` — remove espaços em branco extras

### Formatação
- `⇧⌥F` / `Shift+Alt+F` — formata o documento inteiro
- `⌘K ⌘F` / `Ctrl+K Ctrl+F` — formata apenas a seleção

## Busca e Substituição Avançada

- Ative **Regex** com `⌥⌘R` / `Alt+R` — permite buscas com expressões regulares
- Use grupos capturadores: `$1`, `$2` no campo Replace para reutilizar partes encontradas
- Exemplo: buscar `(\w+)_(\w+)` e substituir por `$2_$1` para inverter nomes

## Linha de Comando

```bash
code .                           # abre pasta atual
code -r .                        # abre na janela existente (reutiliza)
code -n                          # abre nova janela
code --diff arquivo1 arquivo2    # compara dois arquivos
code --goto arquivo:linha:coluna # abre em posição específica
code --disable-extensions .      # abre sem extensões (diagnóstico)
```

## Git Integrado (sem sair do VS Code)

- `⌃⇧G` / `Ctrl+Shift+G` — abre painel Source Control
- Staging parcial: selecione linhas e faça stage apenas da seleção
- Diff lado a lado: F7/⇧F7 para navegar entre mudanças
- `⌘K C` / `Ctrl+K C` — compara com conteúdo da área de transferência

## Configurações Rápidas para o Dia a Dia

```json
"editor.fontSize": 14,
"editor.formatOnSave": true,
"editor.autoSave": "afterDelay",
"files.autoSave": "afterDelay",
"editor.wordWrap": "on",
"editor.rulers": [80, 120],      // linhas guia verticais
"editor.renderWhitespace": "all", // mostra espaços invisíveis
"window.zoomLevel": 1,
"editor.fontLigatures": true     // requer fonte como FiraCode
```

## Janelas Flutuantes

Arraste uma aba do editor para fora da janela → cria janela flutuante independente. Menu direito na aba → **Move into New Window** ou **Copy into New Window**.

## Snippets Personalizados

File > Preferences > Configure Snippets — crie atalhos de texto para blocos de código que você usa com frequência.

## Task Runner

Terminal > Configure Tasks → gera `tasks.json`. Automatize scripts recorrentes (build, lint, testes) vinculados a atalhos de teclado.

## Dicas de Conforto Visual

- **Scroll rápido**: `Alt+scroll` com velocidade configurável via `editor.fastScrollSensitivity`
- **Scroll sincronizado**: comando "Toggle Locked Scrolling" — mantém dois editores lado a lado em sincronia de rolagem
- **Transformar texto**: pesquise "Transform" na Command Palette para converter para maiúsculas/minúsculas/título
