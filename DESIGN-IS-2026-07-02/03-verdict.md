# Veredito — Auditoria co-coach UI

## Veredito: REDESIGN

**Score total: 9/30.** O co-coach UI falhou em 4 princípios load-bearing com score 0 — incluindo #6 (Honest) e #3 (Aesthetic) — e não atingiu score 2 em nenhum princípio crítico de qualidade; REDESIGN é o único veredito válido pelo critério de score < 20 com múltiplos zeros em dimensões load-bearing.

---

## Por que REDESIGN e não REFINE

- Score 9/30 está muito abaixo do limiar de 20 para REFINE
- **Princípio #6 (Honest)** scored 0: há múltiplos fluxos com afirmações falsas ("em tempo real"), ações quebradas ("Salvar configurações" não salva), e 120 promessas vazias repetidas — não é ajuste pontual
- **Princípio #3 (Aesthetic)** scored 0: os dois subsistemas (`docs/` e `static/`) operam com paletas, tipografias e modos de cor completamente diferentes — unificar isso exige redesign de token system, não ajuste de valores
- **Princípio #8 (Thorough)** scored 0: 4+ estados ausentes sistematicamente — não é uma tela mal acabada, é ausência de design de estados como prática
- **Princípio #10 (As little design as possible)** scored 0: 3 sistemas de navegação paralelos, 120 blocos vazios, `.tag` triplicada — a estrutura em si é o problema

---

## O que preservar (não é negociável)

- **Arquitetura do sistema** (#1 scored 2): ingestão via GitHub Issue, sync automático de skills, feed estático — permanecem intocados
- **Fluxo de tarefas do index.html** (#2 parcial): 1–3 cliques para ler um card é correto e eficiente
- **Paleta dark do index.html** (#7 scored 2): `--bg: #0d1117`, `--card-bg: #161b22`, `--accent: #58a6ff` — usada como base do token system unificado
- **Estrutura de sidebar** do gerenciador: hierarquia Sistema/Gerenciar é conceitualmente correta

---

## Top 5 movimentos de maior alavancagem

1. **#6 Honest — Remover ou corrigir todas as afirmações falsas**
   - Deletar "em tempo real" (gerenciador.html:143, 415)
   - Implementar ou remover o botão "Salvar configurações" (gerenciador.html:368→659)
   - Corrigir "Requer servidor" para "Salvo no GitHub" (gerenciador.html:227)
   - Unificar `/co-coach-quiz` vs `/proficiency-check` (index.html:19 vs gerenciador.html:406)
   - Preencher ou remover os 120 blocos "Por que importa:" (index.html:43+)

2. **#3 Aesthetic — Criar um token system único e aplicar dark mode em todos os arquivos**
   - Definir 1 arquivo de tokens CSS (cores, tipo, radius, espaçamento) baseado na paleta do index.html
   - Unificar gerenciador.html e aprenda.html no mesmo dark theme
   - Reduzir font-sizes de 20 para ≤6 valores com semântica (xs/sm/base/lg/xl/display)
   - Eliminar os 60+ hex órfãos — máximo 12 tokens de cor no sistema

3. **#8 Thorough — Implementar os estados faltantes**
   - Adicionar `disabled` visual em todos os botões que dependem de carregamento
   - Adicionar estados de focus em botões (não só inputs)
   - Criar skeleton loading em vez de texto "Carregando..."
   - Adicionar empty states com ação sugerida onde `[]` é possível

4. **#4 Understandable — Substituir jargão técnico por linguagem do usuário**
   - PAT → "Chave de acesso ao GitHub" (gerenciador.html:47)
   - YAML → "um repositório por linha, ex: victorauad/nome-do-repo" (gerenciador.html:281)
   - "pipeline de sumarização" → "como o sistema processa novos conteúdos" (gerenciador.html:312)
   - MCP → "MCP (plugins para o Claude)" em todas as ocorrências
   - "git push" → "quando você salva uma skill" (gerenciador.html:294)

5. **#10 As little design as possible — Eliminar redundâncias estruturais**
   - Unificar os 3 sistemas de navegação: adicionar link "Gerenciador →" no header do index.html
   - Remover os 120 blocos `Por que importa:` vazios do template de card (ou popular o campo no ingest.py)
   - Unificar `.tag` / `.pill` em uma única classe com uma única implementação
   - Consolidar os 3× "↺ Recarregar" em um padrão de componente reutilizável
