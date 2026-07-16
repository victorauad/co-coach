---
titulo: "LangGraph: framework para agentes com estado, human-in-the-loop e checkpointing"
tema: agentes-ia
url: https://github.com/langchain-ai/langgraph
data: 2026-07-04
fonte: pesquisa
---

# LangGraph: framework para agentes com estado, human-in-the-loop e checkpointing

**Tema:** agentes-ia
**Fonte:** https://github.com/langchain-ai/langgraph

## Resumo

- Framework Python/JS para construir agentes como grafos de estado — nós (funções/LLMs) + arestas (roteamento condicional)
- Diferencial principal: `interrupt()` nativo para human-in-the-loop — pausa o grafo indefinidamente até o humano responder
- Checkpointing automático após cada nó: permite pausar, retomar e recuperar falhas sem perder estado
- Não é uma interface visual — LangGraph Studio é ferramenta de debug/observabilidade, não de construção

## Como funciona

### StateGraph básico

```python
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict

class MyState(TypedDict):
    input: str
    result: str

def node_a(state): return {"result": f"processado: {state['input']}"}

builder = StateGraph(MyState)
builder.add_node("node_a", node_a)
builder.set_entry_point("node_a")
builder.add_edge("node_a", END)

graph = builder.compile(checkpointer=MemorySaver())
```

### Human-in-the-loop com interrupt()

```python
from langgraph.types import interrupt, Command

def revisar_proposta(state):
    # Pausa o grafo e devolve dados para o humano
    decision = interrupt({
        "message": "Revise e aprove",
        "dados": state["proposta"]
    })
    # Retoma aqui com o valor que o humano enviou via Command(resume=...)
    approved = decision.get("approved_indices", [])
    return Command(update={"aprovados": approved}, goto="proximo_no")

# Retomar após aprovação humana:
graph.invoke(Command(resume={"approved_indices": [0, 2]}), config)
```

### Checkpointers por ambiente

| Ambiente | Checkpointer | Observação |
|---|---|---|
| Dev/MVP | `MemorySaver` | RAM — perde ao reiniciar |
| Single-server | `SqliteSaver` | Persistente, sem concorrência |
| Produção | `PostgresSaver` | Multi-instância, escalável |

### Thread ID para isolamento de sessões

```python
config = {"configurable": {"thread_id": "usuario-123"}}
graph.invoke(state, config)  # cada thread_id = contexto independente
```

## Padrões de agente — exemplos aplicados a marketing

### Loop Viral — Agente de Clipping

```
analisar_video → calcular_timestamps → gerar_proposta
→ [interrupt: revisar] → executar_corte → enfileirar_postagem
```

- `interrupt()` em `revisar_proposta` pausa até o operador aprovar os timestamps
- Guardrail: se nenhum clipe proposto, grafo termina sem cortar nada

### Loop Pago — Agente de Mídia

```
coletar_metricas_cpar → avaliar_performance
├─ "dentro benchmark" → manter_campanha
└─ "fora benchmark"  → propor_ajuste → [interrupt: aprovar]
                        → executar_via_mcp → registrar_resultado
```

- Teto de R$ 10k como aresta condicional — bloqueia proposta antes do interrupt
- `executar_via_mcp` chama o MCP do Meta/Google Ads após aprovação humana

## Comparação com alternativas

| Ferramenta | Visual? | Human-in-loop nativo | Estado persistente |
|---|---|---|---|
| **LangGraph** | Só debug | ✅ interrupt() | ✅ checkpointer |
| Flowise | ✅ total | Limitado | Limitado |
| n8n | ✅ total | Via webhook | Via DB externo |
| Claude Code + MCP | Não | ✅ (humano opera) | Contexto da sessão |

## Quando usar LangGraph (vs. Claude Code + MCP)

- **T1 MVP**: Claude Code + MCP é suficiente (você é o humano-in-the-loop)
- **T2/T3**: LangGraph entra quando os agentes precisarem de estado persistente entre sessões e orquestração entre si
- Ponto de transição: quando um agente precisar aguardar aprovação por mais de uma sessão do Claude Code

## Fontes

- [Documentação Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
- [How to add static breakpoints](https://langchain-ai.github.io/langgraph/cloud/how-tos/human_in_the_loop_breakpoint/)
- [LangGraph State Management — eastondev.com](https://eastondev.com/blog/en/posts/ai/20260424-langgraph-agent-architecture/)
- [LangGraph Persistence Guide 2026 — fast.io](https://fast.io/resources/langgraph-persistence/)
- [What Is LangGraph? 2026 — atlan.com](https://atlan.com/know/ai-agent/ai-agent-memory/what-is-langgraph/)
