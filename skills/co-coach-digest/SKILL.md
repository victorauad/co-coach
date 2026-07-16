---
name: co-coach-digest
description: Gera um briefing curto dos itens mais recentes e importantes da knowledge base do co-coach — "o que há de novo" — priorizando o objetivo do aluno. Use quando pedir "/co-coach-digest", "o que tem de novo na KB", "me atualiza", "resumo da semana" ou "novidades".
---

# Co-coach Digest — O que há de novo na KB

Você gera um resumo curto e escaneável dos conteúdos mais recentes/relevantes da knowledge base, para o aluno se manter atualizado sem abrir o feed.

## O que fazer quando invocado

### 1. Carregar o contexto do aluno
Leia `perfil-do-aluno.md` na raiz (se existir) e use o objetivo e o progresso para priorizar os itens. Se não existir, siga sem personalização — e ao final sugira o `co-coach-start`.

### 2. Carregar a Knowledge Base
Na ordem, use a primeira fonte que funcionar:
1. `docs/knowledge-base.json` local, se existir
2. Gere-o com `python3 scripts/build-site.py`
3. Em último caso, leia os arquivos de `kb/` diretamente (frontmatter + seção `## Resumo`)

Cada item tem `titulo`, `tema`, `tipo`, `url`, `data`, `bullets`, `importancia`.

### 3. Selecionar os itens
- Ordene por `data` (mais recente primeiro).
- Se o usuário pedir um período ("essa semana", "últimos 7 dias"), filtre por `data`.
- Por padrão, traga os **8 itens mais recentes** — dando peso extra a temas ligados ao objetivo do perfil.
- Agrupe por `tema`.

### 4. Montar o briefing
Formato da resposta:

```
## 📰 Novidades da sua Knowledge Base
_Atualizado em [data de hoje] — [N] itens recentes_

### [tema]
- **[titulo]** — [1 frase do que é / por que importa] → [url]

### [outro tema]
- **[titulo]** — [1 frase] → [url]

---
**Destaque:** [o item mais ligado ao objetivo do aluno e por quê, em 1 frase]
```

### 5. Fechamento
Ao final, ofereça um próximo passo:
- "Quer que eu detalhe algum desses?" ou
- "Quer testar seu conhecimento sobre algum tema? (use `/co-coach-quiz`)"

## Regras de comportamento
- Respostas em português (Brasil), sem jargão.
- Seja conciso: 1 frase por item. O objetivo é escanear rápido.
- Se a KB estiver vazia ou inacessível, avise de forma simples e não invente itens.
