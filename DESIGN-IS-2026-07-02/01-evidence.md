# Evidências — Auditoria co-coach UI

> Consolidado de 4 subagentes em paralelo. Todas as citações são file:line.

---

## Agente 1 — Estrutural

- **Elementos interativos:** gerenciador.html: 32 estáticos; index.html: ~134 (122 links + 11 botões + 1 input); aprenda.html: 5
- **Profundidade máxima de aninhamento:** gerenciador.html: 8 níveis (linha 224); aprenda.html: 7; index.html: 3 (estrutura plana)
- **Padrões repetidos:**
  - 3× "↺ Recarregar" com mesma função (gerenciador.html:384, 399, 417)
  - 2× "Salvar (requer servidor)" (gerenciador.html:277, 368)
  - 2× "Abrir Gerenciador" cross-link (aprenda.html:34, 299)
  - 120× `<div class="importancia">` vazio (index.html:43–44, padrão em todos os cards)
- **Elementos mortos/órfãos:**
  - gerenciador.html:40 — `#pat-modal hidden` (DOM presente, invisível até JS)
  - gerenciador.html:221 — botão "Salvar" hidden antes de skill carregada
  - index.html: 120 blocos `Por que importa:` com conteúdo vazio
- **3 sistemas de navegação distintos sem shell comum:**
  1. Sidebar tab (gerenciador.html:85) — JS showSection()
  2. Links entre páginas (aprenda.html:34, 299 ↔ gerenciador.html:76)
  3. Filtros por tema (index.html:28) — JS in-place filter
  - **index.html não tem link de volta para gerenciador.html — ilha de navegação**

---

## Agente 2 — Visual

- **Modo de cor split (crítico):**
  - `docs/index.html` + `style.css`: dark hardcoded (`--bg: #0d1117`, `--text: #e6edf3`)
  - `static/gerenciador.html` + `static/aprenda.html`: light (Tailwind `bg-slate-50`)
  - Nenhum arquivo usa `@media (prefers-color-scheme)` — sem suporte adaptativo
- **Escala de tipo:** 20 valores distintos de font-size (0.65rem a 36px). Três valores quase idênticos sem distinção semântica: 0.70rem (linha 114), 0.72rem (linha 77), 0.74rem (linha 129) de style.css
- **Paleta de cores:** 60+ valores hex únicos. Zero tokens compartilhados entre `docs/` e `static/`. Azul de acento: `#58a6ff` (style.css:7) vs `#2563eb` (gerenciador.html:14) — mesmo papel, cores diferentes
- **Cores órfãs:** `#555555` (index.html:38), `#f5a623` (aprenda.html:68), `#fff3e0/#e8f5e9/#f3e5f5` (aprenda.html:70,94,118) — cada uma aparece uma única vez
- **`.tag` definida 3 vezes incompativelmente:** style.css:73 (radius 4px, cor #000), gerenciador.html:19 (radius 999px), aprenda.html:16 como `.pill` (radius 999px)
- **Estados:**
  - index.html: empty ✗, loading ✗, error ✗, focus parcial (input only), disabled ✗
  - gerenciador.html: empty parcial, loading parcial (só texto), error parcial (só texto vermelho), success parcial (toast), focus parcial (inputs sim, botões não), disabled ✗
  - aprenda.html: N/A (página estática)
- **border-radius:** 9+ valores distintos sem regra unificadora (4px, 6px, 8px, 12px, 16px, 20px, 999px entre os arquivos)

---

## Agente 3 — Copy & Honesty

- **Falsas afirmações:**
  - "em tempo real" (gerenciador.html:143, 415) — não há polling, WebSocket ou live refresh. Dados carregados uma vez no load.
  - "120 conteúdos indexados" (index.html:12) — número hardcoded no HTML, diverge a cada rebuild
  - Dois "Atualizado em" com datas diferentes e formatos diferentes na mesma página (index.html:12 `01/07/2026` vs index.html:17 `2026-06-25`)
- **Ação quebrada:** "Salvar configurações (requer servidor)" (gerenciador.html:368) → chama `saveConfig()` que exibe toast "Edite scripts/ingest.py via aba Skills" sem salvar nada (gerenciador.html:659–661)
- **Label→comportamento incorreto:** "Requer servidor local rodando" (gerenciador.html:227) — skill editor usa GitHub API diretamente, sem servidor local (confirmado em gerenciador.html:623–648)
- **Promessa quebrada em massa:** 120× `Por que importa:` sem conteúdo (index.html:43+)
- **🆕 em todos os cards** (index.html:38+) — badge "novo" em 100% dos cards perde qualquer significado
- **Comando divergente:** index.html:19 instrui `/proficiency-check`; gerenciador.html:406 instrui `/co-coach-quiz` — mesmo recurso, nomes diferentes
- **Jargão não explicado no contexto:** PAT (gerenciador.html:47), Fine-grained (49), YAML (281), git push (294), MCP não expandido em gerenciador.html nem index.html
- **Terminologia inconsistente por conceito:**
  - Cards: "cards" / "artigos" / "conteúdos"
  - KB: "Knowledge Base" / "KB" / "kb/"
  - Automação: "robô" / "workflow" / "GitHub Actions"
  - Tarefas: "Task" (inglês) / "tarefa"

---

## Agente 4 — Peso & Fricção

- **Tamanho dos arquivos:** index.html 236KB; gerenciador.html 50KB; aprenda.html 19KB; style.css 4KB
- **Dependências externas:**
  - gerenciador.html: Tailwind CDN (gerenciador.html:8) + Google Fonts (gerenciador.html:9)
  - aprenda.html: Tailwind CDN (aprenda.html:7) + Mermaid CDN ~200KB (aprenda.html:8) + Google Fonts (aprenda.html:9)
  - index.html: 0 dependências externas
- **Scripts inline:** index.html 55 linhas (1482–1536); gerenciador.html 528 linhas (434–961); aprenda.html 10 linhas
- **Animações:** 5 transitions declaradas (style.css:127, gerenciador.html:12,18,33, aprenda.html:13,19). Sem `@keyframes`. Nenhuma gateada por `prefers-reduced-motion`
- **Modais no load inicial:** gerenciador.html:40 — `#pat-modal` é ativado imediatamente por `checkPAT()` em `init()` (linha 960) se token não configurado. Interrompe o fluxo antes de qualquer ação
- **Fricção por tarefa:**
  - index.html: 1–3 interações para ler um card (ótimo)
  - gerenciador.html KB add: 4 interações (3 in-app + 1 no GitHub)
  - gerenciador.html Skills: 4 interações para editar uma skill
