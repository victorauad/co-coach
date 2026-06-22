---
titulo: "VS Code: Configurações (Settings)"
tema: ferramentas
url: https://code.visualstudio.com/docs/getstarted/settings
data: 2026-06-22
fonte: vscode-docs
importancia: alta
---

# VS Code: Configurações

Como abrir, entender e personalizar as configurações do VS Code.

## Acessar Configurações

- **Atalho**: ⌘, (Mac) ou Ctrl+, (Windows/Linux)
- **Menu**: File > Preferences > Settings
- **JSON direto**: Command Palette → "Preferences: Open User Settings (JSON)"

## User Settings vs Workspace Settings

| | User Settings | Workspace Settings |
|--|--|--|
| Escopo | Todo o VS Code | Apenas o projeto aberto |
| Onde fica | `~/Library/Application Support/Code/User/settings.json` (Mac) | `.vscode/settings.json` na raiz do projeto |
| Compartilhável | Não (é pessoal) | Sim (commitar no Git) |
| Override | Workspace sobrescreve User | — |

**Nota**: configurações de segurança (como `git.path`) só podem ser definidas em User Settings.

## Interface do Settings Editor

- **Barra de pesquisa**: filtre configurações digitando palavras-chave
- **Barra colorida à esquerda**: indica configurações que você modificou
- **Filtros com @**:
  - `@modified` — só o que você alterou
  - `@ext:nome-da-extensao` — configurações de uma extensão específica
  - `@lang:python` — configurações específicas de linguagem
  - `@tag:experimental` — recursos experimentais

## Configurações Mais Úteis para o Dia a Dia

```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "editor.formatOnSave": true,
  "editor.wordWrap": "on",
  "editor.minimap.enabled": false,
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "window.zoomLevel": 1,
  "workbench.colorTheme": "Default Dark Modern",
  "terminal.integrated.fontSize": 13
}
```

## Configurações por Linguagem

Para aplicar configurações apenas para Python, por exemplo:
```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.tabSize": 4
  },
  "[markdown]": {
    "editor.wordWrap": "on"
  }
}
```

## Precedência (do menor para maior)

1. Padrões do VS Code
2. User settings
3. Remote settings
4. Workspace settings
5. Workspace Folder settings
6. Settings específicos de linguagem (em cada nível)
7. Policy settings (admin — prioridade máxima)

## Settings Sync

Sincronize suas configurações entre máquinas via **Backup and Sync Settings** (botão no canto superior direito do Settings Editor). Sincroniza: configurações, atalhos, extensões, snippets e profiles.

**Limitação**: extensões em ambientes remotos (SSH, WSL, Dev Containers) não são sincronizadas.

## Localização dos Arquivos

- **Mac**: `~/Library/Application Support/Code/User/settings.json`
- **Windows**: `%APPDATA%\Code\User\settings.json`
- **Linux**: `~/.config/Code/User/settings.json`

## Resetar Configurações

- **Individual**: ícone de engrenagem ao lado da configuração → Reset Setting
- **Todas**: apague o conteúdo entre `{}` no settings.json (irreversível)
