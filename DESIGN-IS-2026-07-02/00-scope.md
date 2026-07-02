# Scope — Design Audit co-coach UI

**Data:** 2026-07-02

## O que está sendo auditado
- `static/gerenciador.html` — interface de gerenciamento (KB, decisões, progresso)
- `static/aprenda.html` — diagrama explicativo do sistema
- `docs/index.html` — feed mobile principal
- `docs/style.css` — folha de estilos compartilhada

## Usuário primário
Victor — Head of Growth, não-desenvolvedor. Usa as interfaces via browser local (porta 8765) e GitHub Pages no celular.

## Tarefa primária
- `index.html`: consumir cards de conhecimento filtrados por tema
- `gerenciador.html`: gerenciar KB, ver progresso de aprendizado, registrar decisões
- `aprenda.html`: entender a arquitetura do sistema co-coach

## Pedido do usuário
Converter todas as interfaces para dark mode e otimizar a UI com base nos princípios de Dieter Rams.

## Constraints
- Stack: HTML/CSS puro + JS vanilla (sem frameworks)
- Sem build step — arquivos são copiados diretamente de `static/` → `docs/`
- Deve manter compatibilidade com GitHub Pages
- Acessibilidade mínima: contraste legível no celular

## Referências
Nenhuma referência externa fornecida.
