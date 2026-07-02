# Handoff — /make-plan

```
/make-plan Redesign das interfaces co-coach (gerenciador.html, aprenda.html, docs/index.html + style.css). Score atual: 9/30 com zeros em Aesthetic (#3), Honest (#6), Thorough (#8) e As little design as possible (#10).

Verdict paragraph (auditoria Dieter Rams, 2026-07-02):
> Score total 9/30. O co-coach UI falhou em 4 princípios load-bearing com score 0 — incluindo #6 (Honest) e #3 (Aesthetic) — com múltiplos fluxos com afirmações falsas, dois subsistemas visuais completamente desconexos, ausência de design de estados, e 3 sistemas de navegação paralelos sem shell comum; REDESIGN é o único veredito válido.

Por que redesign e não refine:
- "Salvar configurações" (gerenciador.html:368) não salva nada — chama saveConfig() que exibe um toast
- "em tempo real" (gerenciador.html:143, 415) é falso — não há polling ou WebSocket
- docs/ usa dark theme hardcoded; static/ usa Tailwind light — zero tokens compartilhados
- 120 blocos "Por que importa:" vazios em index.html (linha 43, padrão em todos os cards)
- 3 sistemas de navegação separados sem shell comum; index.html é ilha sem link de volta

Preservar do design atual (OBRIGATÓRIO — não tocar):
- Paleta dark do index.html/style.css: --bg: #0d1117, --card-bg: #161b22, --accent: #58a6ff (style.css:2–7) — base do novo token system
- Fluxo de tarefas do index.html: 1–3 cliques para ler um card (structure: article.card → filtros → link)
- Estrutura de sidebar do gerenciador: hierarquia Sistema/Gerenciar é conceitualmente correta
- Arquitetura geral: GitHub Issue → ingestão → card → feed (não é UI, mas não tocar os scripts)

Descartar do design atual (OBRIGATÓRIO — nomear o que vai):
- Split de color mode: gerenciador/aprenda em Tailwind light vs index em dark hardcoded — eliminar completamente
- Tailwind CDN (gerenciador.html:8, aprenda.html:7) — substituir por CSS custom properties nativas, mesmo padrão já usado em style.css
- Google Fonts CDN (gerenciador.html:9, aprenda.html:9) — usar system font stack
- Os 3 sistemas de navegação paralelos — unificar com link de volta ao gerenciador em index.html e header fixo consistente
- Os 120 blocos <div class="importancia"> vazios — remover do template de card em build-site.py ou popular o campo
- As 3 implementações divergentes de .tag/.pill — uma única classe, uma única implementação
- "Salvar configurações" fake — implementar de verdade ou remover o botão

Top 5 movimentos do redesign (prioridade ordem):

1. #6 Honest — Corrigir afirmações falsas antes de qualquer mudança visual:
   - Remover "em tempo real" de gerenciador.html:143 e 415
   - Implementar saveConfig() corretamente ou remover o botão gerenciador.html:368
   - Corrigir "Requer servidor local rodando" (gerenciador.html:227) → "Salvo no GitHub"
   - Unificar o nome do comando: escolher /co-coach-quiz OU /proficiency-check e usar consistentemente em index.html:19 e gerenciador.html:406
   - Remover ou popular os 120 blocos "Por que importa:" (index.html template em build-site.py)

2. #3 Aesthetic — Criar token system único em style.css e aplicar dark mode nos 3 arquivos:
   - Definir ≤12 tokens de cor baseados na paleta dark de style.css (já bem definida com --bg, --card-bg, --border, --text, --muted, --accent)
   - Adicionar tokens para: --danger, --warning, --success, --surface-2
   - Definir ≤6 tamanhos de tipo com semântica (--text-xs=0.72rem, --text-sm=0.85rem, --text-base=1rem, --text-lg=1.2rem, --text-xl=1.4rem, --text-display para títulos)
   - Aplicar esses tokens em gerenciador.html e aprenda.html removendo Tailwind CDN
   - Resultado esperado: 1 arquivo de tokens, 3 arquivos que o consomem

3. #8 Thorough — Implementar estados faltantes sistematicamente:
   - disabled: todos os botões que dependem de dados carregados recebem [disabled] + opacity visual enquanto carregam
   - focus: adicionar :focus-visible com --accent em todos os botões, não só inputs
   - loading: substituir texto "Carregando..." por skeleton (div animado com background gradient)
   - empty: cada seção do gerenciador com lista vazia recebe mensagem + ação sugerida (padrão já existe em Kanban/Decisões — generalizar)

4. #4 Understandable — Substituir jargão por linguagem do usuário (lista específica):
   - "Personal Access Token (PAT)" → "Chave de acesso ao GitHub" (gerenciador.html:43–49)
   - "ghp_..." placeholder → "Cole aqui a chave gerada no GitHub" (gerenciador.html:48)
   - "Formato YAML: uma lista de owner/repo" → "Um repositório por linha, ex: victorauad/co-coach" (gerenciador.html:281)
   - "pipeline de sumarização de conteúdo" → "como o sistema processa novos conteúdos" (gerenciador.html:312)
   - "O git push dispara automaticamente o workflow" → "Quando você salva uma skill, o GitHub distribui automaticamente" (gerenciador.html:294)
   - MCP → "MCP (plugins para o Claude)" em gerenciador.html nav (linha 103) e index.html filtro (linha 30)
   - "Tasks de todos os projetos" → "Tarefas de todos os projetos" (gerenciador.html:415)

5. #10 As little design as possible — Eliminar redundâncias estruturais:
   - Adicionar link "Gerenciador →" no header do index.html para conectar as ilhas de navegação
   - Unificar .tag / .pill em uma classe no token system (--tag: border-radius 999px, padding 2px 8px, font-size --text-xs)
   - Consolidar os 3× "↺ Recarregar" em um template HTML reutilizável
   - Remover Mermaid CDN de aprenda.html (aprenda.html:8) — substituir o diagrama por SVG estático ou ASCII art equivalente

Princípios de redesign em ordem de prioridade:
1. #6 Honest — cada label descreve exatamente o que acontece; remover toda afirmação não verificável
2. #3 Aesthetic — 1 token system, dark mode em todos os arquivos, ≤6 tamanhos de tipo, ≤12 cores
3. #8 Thorough — disabled/focus/loading/empty em toda superfície interativa

Entregáveis do plano:
- Lista de todas as mudanças de copy falsas a corrigir (arquivo:linha → texto novo)
- Arquivo tokens.css com definição completa do design system
- Checklist de aplicação por arquivo (gerenciador.html, aprenda.html, index.html, style.css)
- Checklist de estados por componente interativo
- Critério de cutover: quando o Tailwind CDN pode ser removido com segurança (após quais mudanças)

Restrições:
- Stack: HTML/CSS puro + JS vanilla. Sem frameworks. Sem build step.
- index.html é gerado por build-site.py — mudanças de template vão no script Python, não no HTML
- gerenciador.html e aprenda.html são editados diretamente em static/
- Compatibilidade com GitHub Pages obrigatória

Anti-patterns a evitar neste redesign:
- Portar a estrutura visual do Tailwind (classes utilitárias) para CSS manual — usar CSS custom properties declarativas, não utilitários
- Manter os dois sistemas de cor em paralelo durante a migração — fazer a transição de um arquivo de cada vez, mas commitar só quando os 3 estiverem unificados
- Redesenhar para seguir uma trend (glassmorphism, etc.) — o dark theme do GitHub já é a referência certa e está no style.css atual
- Tratar os entregáveis do plano como opcionais — a checklist de estados é tão importante quanto as mudanças visuais
```
