---
name: relatorio-pipeline
description: Gera um relatório estruturado de pipeline de vendas a partir de um export do HubSpot (CSV ou via MCP), no formato de abas Resumo/Detalhe/Qualidade. Use quando eu pedir relatório de pipeline, análise de funil ou projeção de MRR.
---

# Como gerar o relatório de pipeline

Este é um exemplo de skill. Adapte os passos e regras ao seu caso real.

## Entrada
- Um CSV de export do HubSpot, OU acesso via MCP do HubSpot.
- Colunas esperadas: deal_name, stage, amount, owner, created_at, closed_at.

## Passos
1. Carregue os dados. Se faltar alguma coluna esperada, avise antes de prosseguir.
2. Calcule colunas derivadas:
   - dias_em_aberto = hoje − created_at (para deals abertos).
   - faixa_ticket = baixo/médio/alto conforme amount.
3. Monte 3 abas:
   - **Resumo:** big numbers (total de deals, MRR projetado, ticket médio) e contagem por estágio.
   - **Detalhe:** uma linha por deal, com as colunas derivadas.
   - **Qualidade:** flags — destaque em vermelho deals sem owner, sem data de fechamento, ou parados há mais de 30 dias.
4. Valide: confirme que a soma dos amounts da aba Detalhe bate com o total da aba Resumo. Reporte o que conferiu.

## Formato de saída
- XLSX. Cabeçalhos em negrito. Datas em DD/MM/AAAA. Moeda em R$.
- Estrutura pensada pra eu colar/importar sem reformatar.

## Observações
- Nunca peça nem manuseie credenciais — a autenticação do MCP eu faço.
- Se algum número parecer estranho, me avise em vez de seguir em silêncio.
