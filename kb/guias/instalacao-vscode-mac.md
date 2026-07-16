---
titulo: Configurar o Claude Code no terminal do VS Code (Mac)
tema: setup
tipo: guia
data: 2026-06-06
importancia: 3
---

# Configurar o Claude Code no terminal do VS Code (Mac)

> **Faça isso agora (≈15 min na primeira vez).** É chato uma vez só. Depois é só digitar `claude`.

## Pré-requisitos

Você precisa de três coisas antes de instalar:

1. **Conta Claude paga** — Pro, Max, Team ou Enterprise. <cite index="2-1">Contas gratuitas não funcionam com o Claude Code.</cite> O plano Pro ($20/mês) já libera.
2. **Node.js 18+** — o Claude Code é distribuído como pacote npm. <cite index="4-1">Confira com `node --version`; se não tiver, baixe em nodejs.org.</cite>
3. **Git** (recomendado) — <cite index="4-1">o Claude Code funciona melhor quando seu projeto está versionado com Git.</cite>

> ⚠️ Os passos abaixo refletem maio/2026. Setup muda rápido — a fonte de verdade é sempre https://code.claude.com/docs/en/quickstart

## Caminho recomendado: extensão do VS Code (inclui o CLI)

A extensão é o caminho mais simples porque **ela já instala o CLI pra você** — você não precisa rodar um comando de instalação separado.

### Passo 1 — Instalar a extensão

<cite index="6-1">No VS Code, aperte `Cmd+Shift+X` pra abrir a aba de extensões, busque por "Claude Code" e clique em Install.</cite>

<cite index="6-1">Se a extensão não aparecer depois de instalar, reinicie o VS Code ou rode "Developer: Reload Window" na paleta de comandos (`Cmd+Shift+P`).</cite>

### Passo 2 — Confiar no workspace

<cite index="5-1">O Claude Code não funciona no modo restrito (Restricted Mode) do VS Code; mudar o workspace para "trusted" resolve.</cite> Quando o VS Code perguntar se você confia na pasta, diga que sim.

### Passo 3 — Abrir uma pasta de projeto

<cite index="3-1">Rodar o Claude dentro da pasta do seu projeto faz com que ele enxergue seus arquivos e ajude ali mesmo.</cite> Use `File → Open Folder` e abra a pasta deste repositório (ou qualquer pasta de trabalho).

### Passo 4 — Abrir o terminal e autenticar

Abra o terminal integrado: menu `Terminal → New Terminal` (ou `` Ctrl+` ``). Digite:

```bash
claude
```

<cite index="4-1">Siga o link do navegador para autenticar sua conta Anthropic. O token de sessão fica salvo localmente, então você não precisa logar toda vez.</cite>

### Passo 5 — Verificar a saúde da instalação

```bash
claude doctor
```

Isso confirma se está tudo certo. Se aparecer algo quebrado, ele te diz o quê.

## Painel gráfico vs. estilo terminal

<cite index="6-1">Por padrão a extensão abre um painel de chat gráfico. Se você prefere a interface estilo CLI, abra a configuração "Use Terminal" e marque a caixa — em VS Code settings (`Cmd+,`) → Extensions → Claude Code → Use Terminal.</cite>

Recomendação pra você: **comece com o terminal.** Os fluxos deste repositório (BigQuery, MCP, headless) são todos de terminal, e é onde está o poder de verdade.

## Layout sugerido (opcional, mas ajuda muito)

<cite index="8-1">Clique com o botão direito na palavra "TERMINAL" no topo do painel do terminal e mova-o para a lateral direita</cite> — assim você lê documentos/arquivos à esquerda e conversa com o Claude à direita. Fica: Explorer na ponta esquerda, editor no centro, terminal à direita.

## Se der erro de PATH

<cite index="2-1">Se você instalou via npm e mesmo assim recebe erro de comando não encontrado, é porque o bin global do npm não está no seu PATH.</cite> Nesse caso, prefira reinstalar pela extensão do VS Code (Passo 1), que evita esse problema.

## O recurso de segurança que você vai notar

<cite index="2-1">O Claude Code pede sua permissão antes de rodar qualquer comando no terminal — você vê um prompt de confirmação toda vez que ele quer executar algo.</cite> Isso é de propósito: nada roda na sua máquina sem você aprovar. No começo aprove com calma, lendo o que ele vai fazer.

## Próximo passo

Vá para `checklist-primeiro-dia.md` e faça os 4 exercícios de aquecimento.
