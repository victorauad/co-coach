# Claude Skills (Oficial Anthropic)

**Repositorio:** github.com/anthropics/skills
**Mantido por:** Anthropic (criadores do Claude)

## O que e?

O repositorio oficial da Anthropic com templates de skills para o Claude Code. Sao instrucoes padronizadas que ensinam o Claude a lidar com tipos especificos de arquivo — PDFs, planilhas Excel, apresentacoes PowerPoint, documentos Word — de forma consistente e eficiente.

## Para que serve?

Quando voce trabalha com arquivos que o Claude nao processa nativamente de forma otima, as skills oficiais ensinam exatamente como ele deve interpretar, extrair e transformar esses dados. E a forma "correta" e testada pela Anthropic de fazer isso.

**Exemplos de uso:**
- Extrair tabelas de um PDF e transformar em dados estruturados
- Ler uma planilha Excel e gerar analises automaticas
- Processar apresentacoes e extrair os pontos principais
- Criar fluxos de processamento de documentos em lote

## Instalacao

### Passo 1: Clonar o repositorio

```bash
git clone https://github.com/anthropics/skills.git
```

### Passo 2: Copiar as skills que voce quer usar

Para skills de PDF:
```bash
cp -r skills/pdf ~/.claude/skills/
```

Para skills de planilhas:
```bash
cp -r skills/spreadsheet ~/.claude/skills/
```

Para skills de apresentacoes:
```bash
cp -r skills/presentation ~/.claude/skills/
```

Para todas as skills de uma vez:
```bash
cp -r skills/* ~/.claude/skills/
```

### Passo 3: Verificar

No Claude Code, as skills ficam automaticamente disponiveis. Voce pode referenciar usando `@nome-da-skill` ou o Claude as usa automaticamente quando detecta o tipo de arquivo.

## Por que usar as oficiais?

As skills da Anthropic sao testadas extensivamente com o Claude e seguem as melhores praticas. Sao o ponto de partida ideal antes de customizar com skills da comunidade.
