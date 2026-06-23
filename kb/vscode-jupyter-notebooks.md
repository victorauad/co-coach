---
titulo: "VS Code: Jupyter Notebooks — Guia Completo"
tema: ferramentas
url: https://code.visualstudio.com/docs/datascience/jupyter-notebooks
data: 2026-06-22
fonte: vscode-docs
importancia: alta
---

# VS Code: Jupyter Notebooks

Guia completo para criar, editar e executar notebooks Jupyter diretamente no VS Code — sem precisar do browser tradicional.

## O que é Jupyter Notebook

Arquivo `.ipynb` que combina código executável + texto em Markdown + resultados/gráficos numa sequência de células. Ideal para análises de dados, experimentos e documentação interativa.

## Criar ou Abrir um Notebook

- Command Palette → **Create: New Jupyter Notebook**
- Crie manualmente um arquivo `.ipynb`
- Abra um arquivo existente pelo Explorer

**Importante**: ao abrir, selecione o **kernel** (interpretador Python) no canto superior direito. O kernel é o que executa o código.

## Executar Células

| Ação | Atalho |
|------|--------|
| Executar célula atual | Ctrl+Enter |
| Executar e avançar para próxima | Shift+Enter |
| Executar e criar célula abaixo | Alt+Enter |
| Executar todas | Barra principal → Run All |
| Executar acima | Run All Above |
| Executar abaixo | Run All Below |

## Modos de Célula

- **Modo comando** (barra vertical à esquerda): aceita atalhos de navegação
- **Modo edição** (borda ao redor): permite editar conteúdo

Pressione `Enter` para editar, `Esc` para modo comando.

## Gerenciar Células

| Ação | Atalho (modo comando) |
|------|----------------------|
| Adicionar célula acima | A |
| Adicionar célula abaixo | B |
| Deletar célula | dd |
| Desfazer | z |
| Código → Markdown | M |
| Markdown → Código | Y |
| Mover célula | Alt+Seta ↑/↓ |

## Explorador de Variáveis

Após executar código, clique em **Variables** na barra principal → veja todas as variáveis da sessão atual com tipos e valores.

### Data Viewer

Duplo clique em uma variável DataFrame/array → abre visualizador de dados com:
- Ordenação por coluna
- Filtragem: texto simples (busca parcial), `=valor` (exato), regex

## Gráficos e Visualizações

Gráficos gerados por matplotlib, seaborn, plotly aparecem inline abaixo da célula. Passe o mouse sobre o gráfico → ícone **Save** para exportar.

## Outline / Tabela de Conteúdo

Painel **Outline** na sidebar → navegue por cabeçalhos Markdown e seções do notebook. Configure para mostrar também células de código via `Notebook > Outline: Show Code Cells`.

## Depurar Notebooks

### Run by Line
Clique em **Run by Line** na barra da célula → executa linha por linha. Requer `ipykernel 6+`.

### Debug Cell
1. Coloque breakpoints na margem esquerda
2. Clique em **Debug Cell**
3. Use o Debug Panel normalmente

## Buscar no Notebook

`Ctrl+F` → busca em todas as células. Use o ícone de funil para filtrar onde buscar (source Markdown, código, saídas).

## Salvar e Exportar

- **Salvar**: Ctrl+S
- **Exportar**: `...` na barra principal → Export → escolha `.py`, PDF ou HTML

**Dica**: para PDF com gráficos, exporte primeiro para HTML e imprima pelo navegador.

## Conectar a Servidor Jupyter Remoto

Kernel Picker → **Existing Jupyter Server** → **Enter URL** → informe `http://servidor:8888/?token=SEU_TOKEN`

## Perfil Recomendado

Use o template **Data Science Profile** (Profiles → Create Profile) → vem pré-configurado com Jupyter, Data Wrangler, Copilot e extensões de dados.
