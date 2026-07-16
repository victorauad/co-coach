---
titulo: Repomix
tema: ferramentas
tipo: guia
data: 2026-06-06
importancia: 3
---

# Repomix

**Repositorio:** github.com/yamadashy/repomix
**Estrelas:** 20.9k

## O que e?

O Repomix pega todo o seu projeto — todos os arquivos de codigo, configuracoes e pastas — e transforma em um unico arquivo de texto otimizado para IA. Em vez de copiar e colar arquivos um por um para o Claude, voce envia o projeto inteiro de uma vez.

## Para que serve?

Quando voce precisa que o Claude entenda o contexto completo do seu projeto (por exemplo, "refatore essa funcao considerando como o resto do codigo funciona"), ele precisa ver varios arquivos ao mesmo tempo. O Repomix resolve isso comprimindo tudo de forma inteligente, reduzindo tokens e mantendo o que importa.

**Exemplos de uso:**
- Pedir ao Claude para revisar toda a arquitetura do projeto
- Gerar documentacao automatica do codebase
- Fazer refatoracoes que impactam multiplos arquivos
- Onboarding de novos devs ("explica o projeto inteiro para mim")

## Instalacao

### Opcao 1: Usar direto sem instalar (recomendado para comecar)

```bash
npx repomix
```

Rode esse comando na raiz do seu projeto. Ele gera um arquivo `repomix-output.txt` que voce cola no Claude.

### Opcao 2: Instalar globalmente

```bash
npm install -g repomix
```

Depois, na raiz do seu projeto:

```bash
repomix
```

### Opcao 3: Interface web

Acesse repomix.com, cole a URL do repositorio do GitHub e baixe o arquivo gerado.

## Como usar no Claude Code

1. Rode `npx repomix` na raiz do projeto
2. O arquivo `repomix-output.txt` sera criado
3. No Claude Code, arraste o arquivo ou use `@repomix-output.txt`
4. Faca sua pergunta normalmente — o Claude agora ve tudo
