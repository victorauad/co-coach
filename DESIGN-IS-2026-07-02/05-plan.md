# Plano de Redesign — co-coach UI (dark mode + Rams)

> Gerado por /make-plan em 2026-07-02, a partir da auditoria DESIGN-IS-2026-07-02 (score 9/30, veredito REDESIGN).
> Decisão de arquitetura (aprovada pelo usuário): **remover Tailwind CDN e reescrever com um token system CSS próprio**, estendendo a paleta dark que já existe em `docs/style.css`.
> Cada fase é executável em um contexto novo de chat. Leia a Fase 0 antes de qualquer fase de implementação.

---

## Fase 0 — Fatos fundadores (LEIA PRIMEIRO, não implementa nada)

Esta fase consolida o que JÁ existe no código. Não invente APIs nem classes — copie destes padrões.

### Fonte de verdade da paleta (já existe, NÃO alterar os valores)
`docs/style.css:1-9`:
```css
:root {
  --bg: #0d1117;
  --card-bg: #161b22;
  --border: #30363d;
  --text: #e6edf3;
  --muted: #8b949e;
  --accent: #58a6ff;
  font-size: 16px;
}
```

### Padrões de componente já corretos (COPIAR destes, não reinventar)
- Card: `docs/style.css:63-69` (`.card` — bg var, border var, radius 8px, padding 1.2rem)
- Input com focus: `docs/style.css:36-46` (`#context-input` + `:focus { border-color: var(--accent) }`)
- Pill/filtro: `docs/style.css:51-61` (`.filtro-btn` — radius 20px, border var, hover bg var)
- Barra de progresso: `docs/style.css:117-129` (já dark-native, reaproveitar em gerenciador Progresso)

### Onde cada arquivo é editado
| Arquivo | Como é servido | Onde editar |
|---|---|---|
| `docs/index.html` | GERADO por `scripts/build-site.py` | editar o **template no Python**, nunca o HTML direto |
| `docs/style.css` | copiado 1:1 de onde? verificar | ver `build-site.py` — provável fonte é o próprio `docs/style.css` inline no script; CONFIRMAR na Fase 1 |
| `static/gerenciador.html` | copiado `static/`→`docs/` no build | editar direto em `static/` |
| `static/aprenda.html` | copiado `static/`→`docs/` no build | editar direto em `static/` |

⚠️ **CONFIRMAR antes da Fase 1:** rodar `grep -n "style.css\|<style\|:root" scripts/build-site.py` para descobrir se o CSS do feed é escrito pelo Python ou lido de um arquivo. Isso decide se `tokens.css` vira arquivo separado ou bloco no script.

### Anti-padrões a rejeitar (confirmados na auditoria)
- Tailwind utility classes (`bg-slate-50`, `text-slate-800`, `bg-white`, `rounded-2xl`...) — TODAS saem
- `<script src="https://cdn.tailwindcss.com">` (gerenciador.html:8, aprenda.html:7) — REMOVER
- Google Fonts CDN (gerenciador.html:9, aprenda.html:9) — REMOVER, usar system font stack já em uso: `docs/style.css:16`
- `.tag` com 3 implementações divergentes (style.css:73, gerenciador.html:19, aprenda.html:16) — UMA só

---

## Fase 1 — Criar o token system (`tokens.css`)

**O que implementar:** um único arquivo `static/tokens.css` que estende `docs/style.css:1-9` com os tokens que faltam. Copiar os 6 tokens existentes verbatim e ADICIONAR:

```css
:root {
  /* --- base (copiado de docs/style.css:1-9, não alterar) --- */
  --bg: #0d1117;
  --card-bg: #161b22;
  --border: #30363d;
  --text: #e6edf3;
  --muted: #8b949e;
  --accent: #58a6ff;

  /* --- novos: superfícies --- */
  --surface-2: #21262d;      /* elevação (sidebar, modal) */

  /* --- novos: semânticos de status (paleta GitHub dark) --- */
  --danger: #f85149;
  --warning: #d29922;
  --success: #3fb950;

  /* --- escala de tipo (≤6 valores, substitui os 20 atuais) --- */
  --text-xs: 0.72rem;
  --text-sm: 0.85rem;
  --text-base: 1rem;
  --text-lg: 1.2rem;
  --text-xl: 1.4rem;
  --text-display: 1.8rem;

  /* --- raio (≤3 valores) --- */
  --radius-sm: 6px;
  --radius: 8px;
  --radius-pill: 999px;

  /* --- espaçamento (escala 4px) --- */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
}

/* badges de tema — dark-native (bg translúcido + texto claro) */
.badge-agentes     { background: rgba(156,39,176,.18); color: #d2a8ff; }
.badge-ferramentas { background: rgba(63,185,80,.18);  color: #7ee787; }
.badge-mcp         { background: rgba(210,153,34,.18); color: #e3b341; }
.badge-metodologia { background: rgba(88,166,255,.18); color: #79c0ff; }
.badge-workflow    { background: rgba(248,81,73,.18);  color: #ffa198; }
.badge-prompts     { background: rgba(219,39,119,.18); color: #ff9bce; }
.badge-setup       { background: rgba(240,136,62,.18); color: #ffab70; }
.badge-outros      { background: rgba(139,148,158,.18);color: #c9d1d9; }
```

**Referências:** valores base de `docs/style.css:1-9`. Cores semânticas seguem a paleta GitHub Dark (mesma família de `--accent: #58a6ff`), para coerência com #7 (long-lasting) que já pontuou 2.

**Verificação:**
- [ ] `static/tokens.css` existe e tem os 6 tokens base idênticos a `docs/style.css:1-9`
- [ ] Nenhum valor hex fora do bloco `:root` e do bloco de badges (grep: `grep -cE '#[0-9a-fA-F]{3,6}' static/tokens.css` deve bater com a contagem esperada ~20, todos dentro de tokens/badges)
- [ ] Escala de tipo tem exatamente 6 valores

**Anti-padrões:** não criar tokens que não serão usados; não duplicar a paleta em outro arquivo; não inventar tokens de sombra ou gradiente (não estão no escopo).

---

## Fase 2 — Passo de honestidade (copy) — barato e independente

Esta fase corrige o princípio #6 (score 0) SEM tocar em visual. Pode ser feita em qualquer ordem relativa às fases visuais.

**O que implementar (arquivo:linha → mudança):**

| Local | Texto atual | Ação |
|---|---|---|
| gerenciador.html:143 | "...em tempo real." | Remover "em tempo real" → "Visão geral do sistema co-coach." |
| gerenciador.html:415 | "...lidas do GitHub em tempo real." | → "...lidas do GitHub a cada carregamento." |
| gerenciador.html:368 | Botão "Salvar configurações (requer servidor)" | DECIDIR: implementar de verdade OU remover o botão. Se a config não persiste, remover o botão e o texto enganoso. |
| gerenciador.html:227 | "Requer servidor local rodando" | → remover (o editor usa GitHub API, confirmado em gerenciador.html:623-648) |
| gerenciador.html:277 | "Salvar (requer servidor)" | → "Salvar no GitHub" (usa API, não servidor) |
| index.html (template no build-site.py) | 120× `Por que importa:` vazio | Popular do campo `importancia` do frontmatter OU remover o bloco do template |
| index.html:12 vs :17 | duas datas de "Atualizado" | Unificar em uma só, formato DD/MM/AAAA |
| index.html:19 | `/proficiency-check` | Alinhar com o comando real `/co-coach-quiz` (confirmar qual existe: `ls skills/ | grep quiz`) |
| index.html badge | 🆕 em 100% dos cards | Mostrar 🆕 só se `status_proficiency == "novo"` (lógica já existe no build) |

**Verificação:**
- [ ] `grep -rn "tempo real" static/` retorna vazio
- [ ] `grep -rn "requer servidor" static/` (case-insensitive) retorna vazio ou só onde de fato requer servidor
- [ ] Uma única data de atualização em index.html
- [ ] Comando de quiz idêntico em index.html e gerenciador.html

**Anti-padrões:** não trocar um texto falso por outro texto vago; cada label deve descrever a ação real.

---

## Fase 3 — Reescrever `gerenciador.html` sem Tailwind

**O que implementar:** substituir o `<head>` e todas as classes utilitárias Tailwind por classes semânticas apoiadas em `tokens.css`.

Passos:
1. No `<head>`: remover linhas 8-9 (Tailwind CDN + Google Fonts). Adicionar `<link rel="stylesheet" href="tokens.css">`. Mover o CSS component-level para um `<style>` que usa `var(--*)`.
2. `<body class="bg-slate-50 min-h-screen">` → `<body>` (fundo vem de `--bg` via tokens). COPIAR a regra body de `docs/style.css:13-20` mas SEM o `max-width: 720px` (o gerenciador é full-width com sidebar).
3. Converter cada bloco de utilitários para uma classe semântica. Mapa de conversão (COPIAR deste mapa):
   - `bg-white rounded-2xl shadow-2xl p-8` → `.modal-card`
   - `bg-white ... rounded-xl` (stat cards) → `.stat-card`
   - `text-slate-800` → cor default (`--text`), remover
   - `text-slate-500` → `color: var(--muted)`
   - `border-slate-200` → `border-color: var(--border)`
   - `bg-blue-600 text-white` (botão primário) → `.btn-primary` (bg `--accent`, texto `--bg`)
   - `focus:ring-2 focus:ring-blue-300` → `:focus-visible { outline: 2px solid var(--accent) }`
4. Sidebar nav: `.nav-link` (gerenciador.html:12-14) reescrever com tokens — hover `--surface-2`, active `--accent`.
5. `.tag` (gerenciador.html:19) e badges: DELETAR daqui, passam a vir de `tokens.css`.
6. Modal PAT: fundo `--card-bg`, overlay `rgba(0,0,0,.6)`.

**Referências:** body de `docs/style.css:13-20`; card de `docs/style.css:63-69`; input de `docs/style.css:36-46`.

**Estados (resolve #8 nesta tela):**
- [ ] Todo botão dependente de dado carregado recebe `[disabled]` + `.is-loading` com `opacity:.5; cursor:not-allowed`
- [ ] `:focus-visible` com `outline: 2px solid var(--accent)` em TODOS os botões (não só inputs)
- [ ] Substituir texto "Carregando..." por `.skeleton` (bloco com background animado usando `--surface-2`)

**Verificação:**
- [ ] `grep -c "cdn.tailwindcss\|fonts.googleapis" static/gerenciador.html` == 0
- [ ] `grep -cE "bg-(white|slate|blue)|text-slate|rounded-(xl|2xl)|shadow-" static/gerenciador.html` == 0 (nenhuma classe Tailwind sobrou)
- [ ] Abrir no browser: fundo escuro, texto legível, sidebar dark, modal dark
- [ ] Contraste texto/fundo ≥ 4.5:1 (já garantido pela paleta GitHub Dark)

**Anti-padrões:** não recriar utilitários Tailwind manualmente (`.p-4`, `.mb-6`); usar classes semânticas (`.stat-card`, `.section-header`). Não deixar nenhum `bg-white` residual — o modal e stat cards são as armadilhas mais comuns.

---

## Fase 4 — Reescrever `aprenda.html` sem Tailwind

**O que implementar:** mesmo tratamento da Fase 3. Ponto de decisão específico: o **Mermaid CDN** (aprenda.html:8, ~200KB).

- Opção A (recomendada p/ #9): substituir o diagrama Mermaid por um SVG estático dark ou blocos HTML/CSS. Remove a dependência de 200KB.
- Opção B: manter Mermaid mas reconfigurar `themeVariables` (aprenda.html:147,180-183) para a paleta dark de `tokens.css`.
- **Se incerto, escolher B** (menor risco) e registrar como dívida técnica para #9.

Passos de conversão idênticos à Fase 3 (mesmo mapa). `.pill` (aprenda.html:16) → usar `.tag`/badge de tokens. `.layer-card` border-left: usar `--accent` e variantes de badge por camada.

**Verificação:**
- [ ] `grep -c "cdn.tailwindcss\|fonts.googleapis" static/aprenda.html` == 0
- [ ] Se Opção A: `grep -c "mermaid" static/aprenda.html` == 0
- [ ] Diagrama legível em fundo escuro (sem texto preto em card escuro)
- [ ] `.pill` não existe mais como classe separada

**Anti-padrões:** não deixar `themeVariables` com cores claras (`#eff6ff`, `#fff3e0`) num fundo dark — é o erro mais provável aqui.

---

## Fase 5 — Ajustes no feed (`build-site.py` + index.html)

**O que implementar:**
1. Adicionar link de navegação "⚙ Gerenciador" no header do template do feed (resolve #10 — ilha de navegação). Localizar o bloco `<header>` no template dentro de `scripts/build-site.py`.
2. Aplicar as correções de copy da Fase 2 que vivem no template Python (blocos `importancia`, badge 🆕, datas, comando quiz).
3. Reduzir os font-sizes do CSS do feed para consumir os tokens de `tokens.css` (se o CSS do feed for inline no Python, importar tokens; se for arquivo, adicionar `@import` ou `<link>`).

**Referências:** template está em `scripts/build-site.py` — localizar com `grep -n "def build\|<header>\|importancia\|proficiency-check" scripts/build-site.py`.

**Verificação:**
- [ ] Rodar `python3 scripts/build-site.py` sem erro
- [ ] `docs/index.html` gerado tem link para gerenciador.html
- [ ] `grep -c "Por que importa:" docs/index.html` == 0 (se removido) OU todos com conteúdo
- [ ] Uma só data de atualização

**Anti-padrões:** não editar `docs/index.html` diretamente (é sobrescrito pelo build); toda mudança vai no Python.

---

## Fase 6 — Verificação final (Rams re-check)

1. **Consistência de tokens:** `grep -rhoE '#[0-9a-fA-F]{3,6}' static/*.html | sort -u` — deve haver pouquíssimos hex fora de `tokens.css` (idealmente zero).
2. **Sem Tailwind/CDN:** `grep -rn "cdn.tailwindcss\|fonts.googleapis" static/` == vazio.
3. **Dark mode uniforme:** abrir os 3 arquivos no browser — mesma paleta, mesmo font stack, mesmo comportamento de foco.
4. **Estados:** cada tela interativa tem disabled + focus + loading + empty demonstráveis.
5. **Honestidade:** `grep -rin "tempo real\|requer servidor" static/` == vazio (ou justificado).
6. **Build:** `python3 scripts/build-site.py` roda e `static/`→`docs/` copia tokens.css junto (CONFIRMAR que o loop de cópia em build-site.py:602-607 inclui `.css`).
7. **Re-score mental:** #3, #6, #8, #10 devem sair de 0. Meta: ≥20/30.

**Anti-padrões finais:** não declarar pronto sem abrir no browser; "grep passou" não é "está bonito e legível". Validar contraste e uma amostra visual real de cada tela.

---

## Sequência recomendada de execução
1. Fase 0 (confirmações) → 2. Fase 1 (tokens) → 3. Fase 2 (copy, rápida) → 4. Fase 3 (gerenciador) → 5. Fase 4 (aprenda) → 6. Fase 5 (feed) → 7. Fase 6 (verificação)

Fases 2 e 5 (copy/feed) podem rodar em paralelo às visuais se em contextos separados. Fases 3 e 4 dependem da 1.
