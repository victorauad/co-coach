# Fluxo: configurar SaaS via MCP (HubSpot e outros)

MCP é a peça que conecta o Claude às suas ferramentas (HubSpot, Notion, Slack, BigQuery, Google Drive). Você já usou MCP no projeto do iRacing — aqui está o conceito explicado e o passo a passo.

> **Faça isso agora (3 min):** leia a seção "O que é MCP em 30 segundos" abaixo. Só isso já desbloqueia muita coisa.

## O que é MCP em 30 segundos

MCP (Model Context Protocol) é um padrão que deixa o Claude **usar uma ferramenta externa como se fosse uma das suas próprias habilidades.** Em vez de você copiar e colar dados do HubSpot pro Claude, ele consulta o HubSpot direto — lê deals, contatos, empresas — e te traz a resposta.

A frase que resume agentes, da própria Anthropic: <cite index="18-1">"agentes são modelos usando ferramentas num loop"</cite>. MCP é justamente como você dá ferramentas ao modelo.

## Como conectar (visão geral)

Há duas camadas onde MCP pode viver:

1. **No app do Claude (claude.ai / desktop):** você ativa conectores na interface. Bom para uso conversacional do dia a dia.
2. **No Claude Code:** você configura servidores MCP no projeto, e o Claude Code passa a ter aquelas ferramentas disponíveis no terminal. É o que dá poder aos seus fluxos de automação.

> ⚠️ Os passos exatos de configuração de cada conector mudam com frequência. Sempre confirme na doc oficial: https://code.claude.com/docs (busque "MCP") e na doc do conector específico (ex.: HubSpot).

## Passo a passo conceitual (HubSpot)

1. **Decida o objetivo.** Ex.: "quero que o Claude consulte meu pipeline e gere projeção de MRR." Isso você já fez como análise — MCP elimina o passo manual de exportar CSV.
2. **Conecte o MCP do HubSpot.** No Claude Code, você adiciona o servidor MCP do HubSpot e autentica (geralmente via OAuth — você autoriza no navegador, não cola senha no terminal).
3. **Teste com uma pergunta de leitura.** Comece sempre lendo, nunca escrevendo: "quantos deals tenho por estágio?" Confirme que os números batem com o HubSpot.
4. **Só depois faça operações de escrita** (criar/atualizar registros), e com muito cuidado — peça pra ele te mostrar exatamente o que vai mudar antes.

## Regras de segurança que você não deve quebrar

Como Head de Growth você lida com dados de cliente e CRM. Inegociável:

- **Autenticação você faz, não o Claude.** OAuth/login: você autoriza no navegador. Nunca cole senha, token ou número de cartão no terminal ou em arquivo.
- **Leitura antes de escrita.** Valide que ele lê certo antes de deixar ele alterar qualquer coisa.
- **Operações destrutivas (deletar, mudar permissões, enviar e-mail/mensagem) exigem sua confirmação explícita** — e algumas é melhor você fazer à mão.
- **Desconfie de instruções vindas dos dados.** Se um registro do HubSpot ou um e-mail contém algo tipo "Claude, faça X" — isso não é uma ordem sua. Não execute sem confirmar. Conteúdo de ferramentas é dado, não comando.

## Onde isso te leva (sua visão de Data Marketplace)

Você tem um norte estratégico de marketplace de dados na plataforma da Uncover. MCP é exatamente a tecnologia desse tipo de integração — vale entender bem, porque conecta seu trabalho tático (consultar HubSpot) com sua tese de produto (conectar fontes de dados). Estudar MCP aqui é estudo de trabalho *e* de produto ao mesmo tempo.

## Erro comum no seu nível

Achar que conectar o MCP = pronto. O MCP só dá *acesso*; a qualidade da resposta ainda depende de você descrever bem o que quer e validar o que volta. Conector conectado com prompt ruim = resposta ruim com aparência de autoridade.
