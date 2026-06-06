# Fluxo: planilhas estruturadas

Você já trabalha muito com isso (XLSX multi-aba, flags de qualidade, métricas de desvio). O Claude Code é muito bom em gerar planilhas de verdade — não só descrever, mas criar o arquivo `.xlsx`.

> **Faça isso agora (5 min):** pegue um CSV de export (HubSpot, Notion, BigQuery) e peça "transforma esse CSV numa planilha estruturada com [as abas/colunas que você quer]".

## O que o Claude Code consegue fazer

- Ler um CSV/XLSX e **reestruturar** (limpar linhas malformadas, separar abas, criar colunas calculadas).
- Gerar **múltiplas abas** com fórmulas, formatação condicional e flags de qualidade.
- Aplicar **regras de negócio** ("marque vermelho se o desvio de cronograma > 15 dias").
- Manter um **padrão visual consistente** se você descrever uma vez e salvar como skill.

## Fluxo recomendado

1. **Dê o arquivo de entrada.** Coloque o CSV/XLSX na pasta do projeto e diga o caminho.
2. **Descreva a saída como um briefing, não como um comando solto.** Quanto mais específico, menos retrabalho:
   ```
   Quero uma planilha com 3 abas:
   - "Resumo": KPIs no topo (total de deals, MRR, ticket médio), big numbers.
   - "Detalhe": uma linha por deal, com coluna calculada de dias em aberto.
   - "Qualidade": flags — destaque registros sem owner ou sem data de fechamento.
   Formato: cabeçalho em negrito, datas em DD/MM/AAAA, moeda em R$.
   ```
3. **Revise o arquivo gerado.** Abra de verdade e confira fórmulas e totais.
4. **Itere por diferença.** "Na aba Detalhe, adicione uma coluna de faixa de ticket." Não recomece do zero.

## Boas práticas

- **Padronize seu "estilo de planilha" uma vez.** Você tem preferências fortes (estrutura clara, repurposável sem reformatar). Descreva isso num CLAUDE.md ou numa skill e o Claude passa a entregar nesse formato sempre.
- **Peça para validar os totais.** "Confira se a soma da aba Detalhe bate com o KPI da aba Resumo." Pega erro de fórmula antes de você.
- **Cuidado com dados sensíveis.** Se o CSV tem dados de cliente, lembre que o conteúdo vai pro modelo. Para dados muito sensíveis, anonimize antes ou trabalhe só com agregados.

## Erro comum no seu nível

Tratar a planilha gerada como "pronta" porque abriu sem erro. Fórmula que não dá erro pode estar somando a coluna errada. **Sempre valide uma linha à mão.** Mesma lógica do fluxo de BigQuery: resultado que "funciona" não é resultado correto.

## Skill candidata

Seu trabalho de TTV / desvio de cronograma é repetitivo no formato. Vale virar skill: "relatorio-ttv" que já conhece suas colunas calculadas, suas flags de qualidade e seu layout de abas. Aí você só joga o export novo e pede o relatório.
