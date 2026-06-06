# NotebookLM Integration

**Repositorio:** github.com/PleasePrompto/notebooklm-skill

## O que e?

Uma skill que conecta o Claude ao estilo de trabalho do NotebookLM (ferramenta do Google para pesquisa). Ela ensina o Claude a processar colecoes de fontes — artigos, PDFs, transcricoes — e gerar saidas estruturadas como resumos, mapas mentais, flashcards e perguntas de estudo.

## Para que serve?

Pesquisadores, estudantes e profissionais que precisam absorver grandes volumes de informacao rapidamente. Em vez de ler 20 artigos manualmente, voce joga tudo no Claude com essa skill e ele organiza o conhecimento para voce.

**Exemplos de uso:**
- Processar 10 artigos academicos e gerar um resumo comparativo
- Criar flashcards automaticos de um capitulo de livro
- Gerar um mapa mental de um tema a partir de multiplas fontes
- Preparar perguntas de revisao para um exame ou apresentacao
- Consolidar anotacoes de reunioes em insights acionaveis

## Instalacao

### Passo 1: Clonar o repositorio

```bash
git clone https://github.com/PleasePrompto/notebooklm-skill.git
```

### Passo 2: Copiar a skill

```bash
cp -r notebooklm-skill ~/.claude/skills/notebooklm
```

### Passo 3: Usar no Claude Code

Adicione seus arquivos de pesquisa ao contexto e chame a skill:

```bash
# Exemplo: processar PDFs de uma pasta
@notebooklm processe esses artigos e gere um resumo com os principais pontos de cada um
```

Ou para flashcards:
```bash
@notebooklm crie 20 flashcards de estudo a partir desse capitulo
```

## Diferenca do NotebookLM original

O NotebookLM do Google e uma ferramenta separada e fechada. Essa skill traz uma experiencia similar dentro do Claude Code, com a vantagem de voce poder combinar com outras skills e automacoes do seu fluxo de trabalho.

## Dica de uso

Funciona melhor quando voce fornece fontes bem delimitadas. Em vez de "pesquise sobre X", prefira "aqui estao 5 artigos — processe esses".
