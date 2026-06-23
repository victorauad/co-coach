---
titulo: "VS Code: Git e Controle de Versão"
tema: ferramentas
url: https://code.visualstudio.com/docs/sourcecontrol/overview
data: 2026-06-22
fonte: vscode-docs
importancia: alta
---

# VS Code: Git Integrado

Como usar Git diretamente no VS Code sem precisar do terminal para operações comuns.

## Abrir o Painel Source Control

- `Ctrl+Shift+G` (Mac: `⌃⇧G`)
- Activity Bar → ícone de bifurcação (terceiro ícone)

## Operações Básicas pelo Painel

### Ver Mudanças

O painel lista todos os arquivos modificados. Clique em qualquer arquivo para ver o **diff** lado a lado — verde = adicionado, vermelho = removido.

### Stage (Preparar para Commit)

- Clique no `+` ao lado do arquivo para fazer stage individualmente
- Clique no `+` no cabeçalho "Changes" para fazer stage de tudo
- **Stage parcial**: abra o diff → selecione linhas específicas → clique direito → **Stage Selected Ranges**

### Commit

1. Digite a mensagem no campo de texto
2. Clique em **Commit** ou pressione `Ctrl+Enter`
3. **Com IA**: clique no ✨ (estrela) → Copilot gera a mensagem automaticamente com base nas mudanças

### Desfazer Commit

Na seção "Commits" → clique direito no commit → **Undo Last Commit** (mantém as mudanças, só remove o commit).

## Branches

- **Ver branch atual**: barra de status no canto inferior esquerdo
- **Criar/trocar**: clique no nome do branch na barra de status
- Command Palette → **Git: Create Branch** ou **Git: Checkout to...**

## Worktrees

Para trabalhar em múltiplos branches simultaneamente sem precisar fazer stash:
- Command Palette → **Git: Add Worktree**
- Cria uma pasta separada para o branch, abrível em outra janela

## Stash (Guardar Mudanças Temporariamente)

- Command Palette → **Git: Stash**
- Para recuperar: **Git: Pop Stash** ou **Git: Apply Stash**

## Diff Visual

O VS Code mostra diffs com destaque por linha e por palavra. Para comparar dois arquivos quaisquer:
```bash
code --diff arquivo1 arquivo2
```

Ou Command Palette → **File: Compare Active File With...**

## Resolução de Conflitos de Merge

Quando houver conflito, o VS Code destaca as seções conflitantes com opções:
- **Accept Current Change** — mantém sua versão
- **Accept Incoming Change** — aceita a versão do outro branch
- **Accept Both Changes** — combina as duas
- **Compare Changes** — abre editor 3 vias para comparação detalhada

Com IA ativada, há opção de pedir para o Copilot resolver o conflito.

## GitLens (Extensão Recomendada)

A extensão `eamodio.gitlens` adiciona:
- **Git Blame inline**: mostra quem escreveu cada linha, diretamente no editor
- **Histórico de arquivo**: veja todas as versões anteriores
- **Comparações avançadas**: entre branches, commits, etc.

## Git Graph (Extensão Recomendada)

A extensão `mhutchie.git-graph` adiciona visualização gráfica de branches e commits — útil para entender o histórico do projeto.

## GitHub Pull Requests

A extensão `github.vscode-pull-request-github` permite:
- Ver, criar e revisar PRs sem sair do VS Code
- Comentar em código diretamente no diff
- Fazer merge pelo editor
