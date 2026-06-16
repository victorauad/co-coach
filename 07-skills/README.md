# Skills deste repositório

Skills são comandos que você invoca no Claude Code com `/nome-da-skill`. Eles ficam em `.claude/commands/` no seu projeto — mas essa pasta é ignorada pelo `.gitignore` para não vazar configurações pessoais.

**Como instalar uma skill daqui:**

```bash
# No terminal, dentro do projeto onde quer usar a skill:
mkdir -p .claude/commands
cp ~/claude-code-growth/07-skills/process-inbox.md .claude/commands/
cp ~/claude-code-growth/07-skills/ai-review.md .claude/commands/
```

Depois disso, `/process-inbox` e `/ai-review` ficam disponíveis naquele projeto.

---

## Skills disponíveis

### `/process-inbox` → [process-inbox.md](process-inbox.md)
Processa os links do `inbox.md`, busca o conteúdo de cada um e atualiza os arquivos `.md` corretos do repositório com os aprendizados extraídos.

**Como usar:**
1. Cole links no `inbox.md` (um por linha)
2. Rode `/process-inbox`
3. Receba um relatório do que foi adicionado e onde

---

### `/ai-review` → [ai-review.md](ai-review.md)
Analisa outro projeto e compara com as boas práticas documentadas neste repositório. Retorna um relatório estruturado pronto para colar no Notion.

**Como usar:**
```
/ai-review ../caminho-do-projeto
```

Ou sem argumento para analisar o projeto atual:
```
/ai-review
```
