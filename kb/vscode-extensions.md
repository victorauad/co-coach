---
titulo: "VS Code: Extensões — Instalar, Gerenciar e Recomendar"
tema: ferramentas
url: https://code.visualstudio.com/docs/editor/extension-marketplace
data: 2026-06-22
fonte: vscode-docs
importancia: alta
---

# VS Code: Extensões

Como encontrar, instalar, configurar e recomendar extensões no VS Code.

## Abrir o Marketplace de Extensões

- Atalho: `Ctrl+Shift+X` (Mac: `⇧⌘X`)
- Activity Bar → ícone de blocos
- Command Palette → "Extensions: Focus on Installed View"

## Instalar uma Extensão

1. Pesquise pelo nome na barra de busca
2. Clique em **Install**
3. Na primeira instalação de publisher desconhecido, o VS Code pede confirmação de confiança

**Outras opções de instalação:**
- Versão específica: clique direito → **Install Another Version**
- Versão pré-lançamento: dropdown de instalação → **Install Pre-Release Version**
- Sem sincronizar entre máquinas: **Install (Do not Sync)**
- Via arquivo `.vsix`: Command Palette → "Extensions: Install from VSIX"
- Via linha de comando: `code --install-extension publisher.extensao`

## Gerenciar Extensões Instaladas

- **Desabilitar**: ícone de engrenagem → Disable (globalmente ou só no workspace)
- **Desinstalar**: ícone de engrenagem → Uninstall
- **Atualização automática**: ativada por padrão. Configure com `extensions.autoUpdate`
- **Listar instaladas**: `code --list-extensions` no terminal

## Filtros de Pesquisa Úteis

Digite `@` na busca para ver opções de filtro:

| Filtro | O que mostra |
|--------|-------------|
| `@installed` | Extensões que você tem instaladas |
| `@enabled` / `@disabled` | Ativas ou desativadas |
| `@recommended` | Sugeridas para o contexto atual |
| `@popular` | Mais baixadas |
| `@updates` | Extensões com atualização disponível |
| `@category:themes` | Apenas temas |
| `@sort:installs` | Ordenado por downloads |
| `@sort:rating` | Ordenado por avaliação |
| `@ext:ms-python.python` | Por ID específico |

## Extensões Recomendadas por Categoria

### Para Python e Dados
- `ms-python.python` — suporte completo Python
- `ms-toolsai.jupyter` — notebooks Jupyter
- `ms-toolsai.datawrangler` — visualizador de dados interativo
- `ms-python.black-formatter` — formatador de código

### Para Produtividade Geral
- `esbenp.prettier-vscode` — formatar JSON, Markdown, etc.
- `streetsidesoftware.code-spell-checker` — corretor ortográfico
- `eamodio.gitlens` — histórico Git avançado linha por linha
- `mhutchie.git-graph` — visualização gráfica de branches Git

### Para IA e Claude Code
- `anthropics.claude-code` — Claude Code integrado ao VS Code
- `github.copilot` — GitHub Copilot (sugestões inline com IA)
- `github.copilot-chat` — chat com IA dentro do editor

### Para Aparência
- `pkief.material-icon-theme` — ícones de arquivo coloridos por tipo
- `dracula-theme.theme-dracula` — tema escuro popular
- `zhuangtongfa.material-theme` — One Dark Pro

## Recomendar Extensões para o Time

Crie `.vscode/extensions.json` na raiz do projeto:

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-toolsai.jupyter"
  ]
}
```

O VS Code notifica quem abrir o projeto para instalar as extensões recomendadas. Ótimo para padronizar o ambiente do time.

## Ignorar Recomendações

Na página da extensão → ícone de engrenagem → **Ignore Recommendation**.

## Onde as Extensões Ficam Salvas

- **Mac/Linux**: `~/.vscode/extensions/`
- **Windows**: `%USERPROFILE%\.vscode\extensions\`
