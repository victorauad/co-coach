# Scorecard — Auditoria co-coach UI (Dieter Rams)

> Orquestrador apenas. Nenhuma delegação de pontuação.
> Regra de desempate: score menor. Score por pior instância, não por média.

---

1. **Good design is innovative — Score: 2/3**
   Evidence: A arquitetura (ingestão via GitHub Issue, sync automático de skills entre repos) não tem equivalente em 5+ produtos conhecidos.
   Justification: A *arquitetura* inova claramente; os padrões de UI (sidebar dashboard + card grid + filter strip) são convenções bem estabelecidas sem melhoria notável — isso é refresh, não inovação de forma.

2. **Good design makes a product useful — Score: 1/3**
   Evidence: "Salvar configurações" chama `saveConfig()` que não salva nada (01-evidence.md Agente 3, gerenciador.html:368→659); 120 blocos "Por que importa:" vazios reduzem utilidade de cada card; comando `/proficiency-check` (index.html:19) pode não existir.
   Justification: A tarefa primária do feed (ler card) completa em 1–3 passos, mas há ações quebradas em seções inteiras (Configurações) e promessas sistematicamente não cumpridas — não é só detour, é funcionalidade ausente.

3. **Good design is aesthetic — Score: 0/3**
   Evidence: 20 valores de font-size distintos (01-evidence.md Agente 2); 60+ cores sem tokens compartilhados entre docs/ e static/; split light/dark sem sistema; `.tag` definida 3× incompativelmente; 9+ valores de border-radius sem regra.
   Justification: Não há um sistema visual visível — as duas sub-interfaces (`docs/` e `static/`) operam em paletas, tipografias e modos de cor completamente separados. Isso vai além de "inconsistências menores": são dois sistemas paralelos sem ponte.

4. **Good design makes a product understandable — Score: 1/3**
   Evidence: Jargão não explicado em contexto (PAT, YAML, git push, Fine-grained, MCP — gerenciador.html:47–49, 281, 294); "Adicionar" abre GitHub em vez de adicionar (gerenciador.html:261→663); "Requer servidor" está errado (gerenciador.html:227).
   Justification: Mais de 3 controles têm labels que não descrevem o comportamento real; jargão técnico está presente em quase toda seção — não chega a 0 porque a estrutura de navegação (sidebar tabs) é autoexplicativa.

5. **Good design is unobtrusive — Score: 2/3**
   Evidence: Sidebar e filter strip recuam adequadamente; conteúdo é a figura principal tanto no feed quanto no gerenciador; modal PAT (gerenciador.html:40) interrompe antes de qualquer ação no primeiro uso.
   Justification: O chrome em geral fica em segundo plano, mas o modal forçado no primeiro acesso é intrusão real — não chega a 1 porque é episódico (só no onboarding), não permanente.

6. **Good design is honest — Score: 0/3**
   Evidence: "em tempo real" sem polling (gerenciador.html:143, 415); "Salvar configurações" não salva (gerenciador.html:368→659); "Requer servidor" é falso (gerenciador.html:227); 120× "Por que importa:" vazio (index.html:43+); duas datas conflitantes de atualização (index.html:12 vs 17); 🆕 em 100% dos cards.
   Justification: Há múltiplos fluxos enganosos simultâneos — não é inflação pontual (que seria 1–2), é um padrão sistêmico de afirmações que não correspondem ao comportamento real.

7. **Good design is long-lasting — Score: 2/3**
   Evidence: index.html usa paleta inspirada no GitHub Dark, atemporal; gerenciador.html/aprenda.html usam Tailwind CDN (padrão datado de 2023–2025) e Google Fonts (dependência externa sem controle).
   Justification: O dark theme do feed é sólido e resistirá ao tempo; o conjunto gerenciador+aprenda carrega 1–2 marcadores datáveis (CDN Tailwind, utilitarismo Tailwind excessivo visível) sem ser dominado por trend.

8. **Good design is thorough down to the last detail — Score: 0/3**
   Evidence: disabled ausente em todos os controles (01-evidence.md Agente 2); focus missing em botões do gerenciador; loading só como texto puro sem feedback visual; 4+ estados ausentes ou apenas esboçados em ambas as interfaces principais.
   Justification: 4+ estados faltando ou não acabados em ambas as interfaces principais — o critério de score 0 é atingido objetivamente.

9. **Good design is environmentally friendly — Score: 1/3**
   Evidence: Tailwind CDN (gerenciador.html:8, aprenda.html:7) + Mermaid CDN ~200KB (aprenda.html:8) + Google Fonts (gerenciador.html:9, aprenda.html:9); nenhuma transition gateada por `prefers-reduced-motion`; modo escuro ignorado em gerenciador/aprenda.
   Justification: A carga CDN total de aprenda.html ultrapassa 200KB só em Mermaid; gerenciador carrega Tailwind completo via CDN. Coloca o conjunto entre 500KB–2MB de assets externos; motion não gateado. index.html é o único arquivo limpo.

10. **Good design is as little design as possible — Score: 0/3**
    Evidence: 3 sistemas de navegação sem shell comum (01-evidence.md Agente 1); 120 blocos decorativos vazios (index.html:43+); `.tag` implementada 3× para o mesmo elemento semântico; 20 font-sizes; 60+ cores.
    Justification: A superfície é dominada por elementos redundantes (3 navs), vazios (120 blocos "importância"), e duplicações de implementação — remover qualquer um deles não quebra nenhuma tarefa.

---

## Total: 9/30

| # | Princípio | Score |
|---|---|---|
| 1 | Innovative | 2 |
| 2 | Useful | 1 |
| 3 | Aesthetic | 0 |
| 4 | Understandable | 1 |
| 5 | Unobtrusive | 2 |
| 6 | Honest | 0 |
| 7 | Long-lasting | 2 |
| 8 | Thorough | 0 |
| 9 | Environmentally friendly | 1 |
| 10 | As little design as possible | 0 |
| **Total** | | **9/30** |
