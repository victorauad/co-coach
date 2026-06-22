---
titulo: "VS Code: GitHub Copilot e Recursos de IA"
tema: ferramentas
url: https://code.visualstudio.com/docs/copilot/ai-powered-suggestions
data: 2026-06-22
fonte: vscode-docs
importancia: alta
---

# VS Code: GitHub Copilot e IA

Recursos de inteligência artificial disponíveis no VS Code para aumentar produtividade.

## Sugestões Inline (Ghost Text)

O Copilot mostra sugestões semitransparentes enquanto você digita:
- **Tab** — aceita a sugestão completa
- **⌘→** (Ctrl+Right) — aceita palavra por palavra
- **Esc** — rejeita a sugestão

## Next Edit Suggestions (NES)

Além de autocompletar, o Copilot **prediz onde será sua próxima edição** e o que ela deve ser. Uma seta na margem indica que há uma sugestão de edição disponível.

Casos de uso:
- **Correção em cascata**: muda uma variável e o Copilot sugere todas as ocorrências afetadas
- **Refatoração**: renomeia com propagação automática
- **Mudança de intenção**: ao converter uma classe `Point` para `Point3D`, sugere os ajustes necessários

## Chat de IA

- `Cmd+I` (inline chat) — abre chat diretamente no editor, ao lado do código
- Chat panel (ícone de balão) — conversa mais longa com contexto do projeto
- `@terminal` — participante especializado em terminal e comandos

## Commit com IA

No painel Source Control, clique no **ícone de estrela** no campo de mensagem de commit → Copilot gera a mensagem automaticamente baseado nas mudanças staged.

## Selecionar Modelo de IA

Menu Chat → **Configure Inline Suggestions** → **Change Completions Model** → alterne entre modelos disponíveis (GPT-4o, Claude, etc. dependendo do plano).

## Controle das Sugestões

- Ative/desative via ícone Copilot na barra de status (canto inferior direito)
- Opções de "snooze" temporário
- Desative para linguagem específica sem afetar outras

## Claude Code no VS Code

O Claude Code tem extensão dedicada para VS Code (`anthropics.claude-code`) com integração mais profunda que o Copilot padrão. Veja `anthropic-ide-integrations.md` para detalhes completos de instalação e uso.

## Diferença Copilot vs Claude Code

| | GitHub Copilot | Claude Code |
|--|--|--|
| Foco | Sugestões de código inline | Tarefas completas, terminal, arquivos |
| Interface | Dentro do editor | Terminal + extensão VS Code |
| Contexto | Arquivo atual | Todo o repositório |
| Agent mode | Sim (limitado) | Sim (amplo) |
