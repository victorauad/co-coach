---
titulo: "[Decisão] PAT do GitHub armazenado em arquivo local vs. localStorage"
tema: metodologia
data: 2026-06-30
projeto: co-coach
importancia: alta
---

## Contexto

O gerenciador do co-coach precisava autenticar na GitHub API para ler os TASKS.md dos projetos e popular o Kanban. O PAT (token de acesso) era inserido manualmente toda vez que o gerenciador era aberto — porque o localStorage do browser apagava o valor entre sessões quando o arquivo era aberto como `file://` no Safari.

## Opções consideradas

- **Opção A: Manter localStorage** — simples, mas o Safari limpa entre sessões para arquivos locais. Exige reinserção constante.
- **Opção B: Backend com .env** — PAT fica seguro no servidor, nunca exposto. Mas exige servidor local rodando sempre, contrariando a decisão anterior de eliminar o `server.py`.
- **Opção C: `config.local.js` gitignored** — arquivo JS local que define `window.GH_PAT`. O gerenciador tenta carregá-lo com `<script onerror="void 0">`. Se existir, PAT sempre disponível. Se não (GitHub Pages), cai para localStorage.

## Decisão

Escolhi **Opção C** porque:
- Zero dependência de servidor
- Um único arquivo para preencher uma vez (`static/config.local.js`)
- O `onerror="void 0"` garante que o GitHub Pages continue funcionando sem o arquivo
- PAT nunca vai para o repositório (gitignored)

## O que aprendi

`localStorage` é armazenado por *origem* (origin) no browser — e `file://` é tratado como origem instável pelo Safari. O mesmo token salvo no localhost funciona diferente de um salvo em `file://`. A solução com arquivo JS separado é o padrão "progressive enhancement": a feature existe se o arquivo existir, sem quebrar se não existir.
