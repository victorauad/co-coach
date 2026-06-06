# Marketing Skills

**Repositorio:** github.com/coreyhaines31/marketingskills
**Conteudo:** 23 fluxos de trabalho especializados

## O que e?

Uma suite completa de skills de marketing para o Claude Code. Sao 23 fluxos prontos cobrindo as principais tarefas de um time de marketing: SEO, copywriting, anuncios pagos, email marketing, redes sociais, analise de concorrentes e estrategias de crescimento.

## Para que serve?

Times de marketing que querem usar IA de forma estruturada e consistente — sem precisar reescrever prompts do zero toda vez. Cada skill e calibrada para uma tarefa especifica, entregando resultados no formato certo com as informacoes certas.

**Exemplos de uso:**
- Analisar um artigo e gerar versao otimizada para SEO
- Criar variacoes de copy para anuncios no Google e Meta
- Escrever sequencia de emails de nurturing para um produto
- Gerar calendario de conteudo para redes sociais por um mes
- Analisar posicionamento de concorrentes e identificar gaps
- Criar briefing de campanha a partir de um objetivo de negocio

## Skills incluidas (principais)

| Skill | O que faz |
|-------|-----------|
| `seo-optimizer` | Otimiza textos para mecanismos de busca |
| `ad-copywriter` | Gera copys para Google Ads, Meta e LinkedIn |
| `email-sequence` | Cria sequencias de email marketing |
| `social-calendar` | Monta calendario de conteudo para redes sociais |
| `competitor-analysis` | Analisa concorrentes e mapeia oportunidades |
| `landing-page` | Estrutura e escreve paginas de conversao |
| `growth-strategy` | Sugere estrategias de crescimento baseadas no contexto |

## Instalacao

### Passo 1: Clonar o repositorio

```bash
git clone https://github.com/coreyhaines31/marketingskills.git
```

### Opcao A: Instalar via npx (se disponivel)

```bash
npx skills add coreyhaines31/marketingskills
```

### Opcao B: Instalacao manual

```bash
cp -r marketingskills/skills/* ~/.claude/skills/
```

### Passo 3: Usar no Claude Code

```bash
# Otimizar um texto para SEO
@seo-optimizer [cole seu texto aqui]

# Criar copy de anuncio
@ad-copywriter produto: [nome], beneficio principal: [beneficio], publico: [descricao]

# Montar calendario de conteudo
@social-calendar tema: [tema], plataformas: Instagram e LinkedIn, periodo: julho 2026
```

## Para quem e mais util?

- Marketing managers que precisam produzir mais com menos tempo
- Founders que acumulam funcao de marketing
- Agencias que atendem multiplos clientes simultaneamente
- Times pequenos sem especialistas em todas as areas
