---
titulo: Fluxo: banco de dados (BigQuery)
tema: workflow
tipo: guia
data: 2026-06-06
importancia: 3
---

# Fluxo: banco de dados (BigQuery)

Você já fez isso de forma parecida no projeto do iRacing (API → BigQuery → MCP → Slides). Aqui está o fluxo destilado e reutilizável.

> **Faça isso agora (5 min):** abra um projeto, rode `claude` e peça "me ajude a montar uma query no BigQuery para [pergunta de negócio]". Veja o plano antes de rodar.

## Duas formas de o Claude falar com o BigQuery

### Forma A — Claude escreve SQL, você roda (mais simples, mais seguro)

O Claude **não toca no banco**; ele só escreve a query e você cola no console do BigQuery ou roda via `bq` na sua máquina. Bom para começar e para queries sensíveis.

```
Você: "Tenho uma tabela `deals` com colunas stage, amount, created_at, closed_at.
Quero MRR projetado por mês até dez/2026. Escreve a query BigQuery Standard SQL
e me explica a lógica."
```

### Forma B — Claude executa via MCP (mais poderoso)

Com um conector MCP de BigQuery configurado, o Claude consulta o banco direto e já te traz os resultados. É o que você fez no iRacing. Veja `mcp-hubspot-e-saas.md` para o conceito de MCP — é o mesmo mecanismo.

## Boas práticas que evitam dor de cabeça

- **Descreva o schema.** O Claude acerta muito mais SQL se você colar a estrutura da tabela (nomes e tipos de coluna). Sem isso, ele adivinha.
- **Peça a query em Plan Mode primeiro.** Você lê a lógica antes de gastar processamento (BigQuery cobra por dados escaneados).
- **Comece com `LIMIT` e custo baixo.** Peça pra ele incluir `LIMIT 100` e usar partições/filtros de data pra não escanear a tabela inteira numa query de teste.
- **Peça explicação linha a linha** quando a query for complexa. Você quer *entender*, não só rodar — esse é o ponto cego que estamos corrigindo.

## Padrão de prompt reutilizável

```
Contexto: [o que a tabela representa, e o schema]
Pergunta de negócio: [o que você quer saber]
Quero: query BigQuery Standard SQL, com comentários explicando cada CTE,
otimizada para escanear o mínimo de dados.
Antes de escrever, me mostre o plano em 3 bullets.
```

## Erro comum no seu nível

Pedir "me dá os números" sem entender de onde vieram. Sempre peça ao Claude pra **explicar a query** e **validar uma amostra à mão**. Uma query errada que "roda" é pior que nenhuma — ela te dá confiança falsa num número errado, e você leva pra uma reunião.

## Skill candidata

Se você consulta BigQuery toda semana com o mesmo tipo de pergunta, isso é forte candidato a virar uma *skill* (ver `kb/guias/metodologia-skills.md`). Ex.: uma skill "relatorio-pipeline" que já sabe o schema das suas tabelas e o formato de saída que você gosta.
