---
titulo: "VS Code: Temas e Personalização Visual"
tema: ferramentas
url: https://code.visualstudio.com/docs/getstarted/themes
data: 2026-06-22
fonte: vscode-docs
importancia: media
---

# VS Code: Temas e Personalização Visual

Como personalizar a aparência do VS Code — cores, ícones e fontes.

## Temas de Cor

### Abrir Seletor de Temas
- `⌘K ⌘T` (Mac) / `Ctrl+K Ctrl+T` (Win)
- File > Preferences > Theme > Color Theme

Prévia em tempo real: use as setas ↑↓ para navegar entre temas antes de confirmar com Enter.

### Temas Populares da Comunidade
- **One Dark Pro** (`zhuangtongfa.material-theme`) — escuro, muito popular
- **Dracula** (`dracula-theme.theme-dracula`) — escuro roxo/roxo
- **Night Owl** (`sdras.night-owl`) — escuro azulado
- **Solarized Light/Dark** — claro ou escuro com paleta suave
- **GitHub Light/Dark** — minimalista, similar ao GitHub

Instale pelo Marketplace: `@category:themes` ou **Browse Additional Color Themes...** no seletor.

### Salvar no Settings
```json
"workbench.colorTheme": "One Dark Pro"
```

## Personalizar Cores Específicas

### Cores da Interface (Workbench)
```json
"workbench.colorCustomizations": {
  "sideBar.background": "#1e1e2e",
  "activityBar.background": "#181825",
  "statusBar.background": "#313244",
  // Aplicar só a um tema específico:
  "[One Dark Pro]": {
    "editor.background": "#1a1a2e"
  }
}
```

Consulte **Theme Color Reference** no VS Code para a lista completa de elementos.

### Cores de Sintaxe (Tokens)
```json
"editor.tokenColorCustomizations": {
  "comments": "#6b7280",
  "strings": "#a3e635",
  "keywords": "#f472b6"
}
```

## Temas de Ícones de Arquivo

Ícones coloridos ao lado dos nomes de arquivo no Explorer.

- File > Preferences > Theme > **File Icon Theme**
- Temas inclusos: **Minimal** e **Seti** (padrão)
- Populares: `pkief.material-icon-theme` (muito popular), `PKief.material-icon-theme`

```json
"workbench.iconTheme": "material-icon-theme"
```

## Temas de Ícones do Produto

Modificam os ícones da interface do VS Code em si (Activity Bar, botões).
- File > Preferences > Theme > **Product Icon Theme**

## Fontes

### Tamanho e Família
```json
"editor.fontSize": 14,
"editor.fontFamily": "Fira Code, Menlo, Monaco, monospace",
"terminal.integrated.fontSize": 13
```

### Ligaduras (ligaduras tipográficas)
Transformam `=>` e `!=` em símbolos visuais mais limpos. Requer fonte que suporte (ex: Fira Code, JetBrains Mono):
```json
"editor.fontLigatures": true
```

Baixe Fira Code em: github.com/tonsky/FiraCode

## Zoom da Interface

```json
"window.zoomLevel": 1    // 0 = padrão, negativo = menor, positivo = maior
```

Ou: `⌘+` / `⌘-` para aumentar/diminuir temporariamente.

## Pré-visualizar Temas Online

Acesse `https://vscode.dev/editor/theme/<extensionId>` para prévia sem instalar.

Exemplo: `https://vscode.dev/editor/theme/sdras.night-owl`

## Remover Temas Padrão

Extensions → filtro **Built-in** → seção **THEMES** → clique direito → **Disable** nos temas que não usa para limpar a lista.
