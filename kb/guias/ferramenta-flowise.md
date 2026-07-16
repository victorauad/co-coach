---
titulo: Flowise
tema: ferramentas
tipo: guia
data: 2026-06-06
importancia: 3
---

# Flowise

**Repositorio:** github.com/FlowiseAI/Flowise
**Estrelas:** 30k

## O que e?

O Flowise e uma ferramenta visual para construir agentes de IA e chatbots arrastando e soltando blocos numa tela. E mais simples que o Dify e focado em prototipagem rapida — ideal para quem quer testar uma ideia de IA em minutos.

## Para que serve?

Criar rapidamente prototipos de aplicacoes com IA: chatbots com memoria, sistemas que consultam documentos, agentes que usam ferramentas externas. O Flowise conecta modelos de linguagem (como Claude) com bases de conhecimento e APIs de forma visual.

**Exemplos de uso:**
- Chatbot que le PDFs e responde perguntas sobre eles
- Agente que pesquisa na internet e resume os resultados
- Sistema de suporte ao cliente com base de conhecimento customizada
- Prototipo de produto de IA para apresentar para stakeholders

## Instalacao

### Requisito: Node.js instalado

Verifique com `node --version`. Se nao tiver, baixe em nodejs.org.

### Opcao 1: Instalacao rapida (recomendada)

```bash
npm install -g flowise
npx flowise start
```

Acesse `http://localhost:3000` no navegador.

### Opcao 2: Clonar e rodar localmente

```bash
git clone https://github.com/FlowiseAI/Flowise.git
cd Flowise
npm install
npm run build
npm run start
```

### Opcao 3: Docker

```bash
docker run -d --name flowise -p 3000:3000 flowiseai/flowise
```

## Conectar com Claude

Dentro do Flowise, ao criar um fluxo:
1. Adicione o bloco **ChatAnthropic**
2. Insira sua chave de API da Anthropic
3. Selecione o modelo (ex: claude-sonnet-4-6)
4. Conecte aos outros blocos do seu fluxo

## Diferenca do Dify

Flowise e mais leve e facil de comecar. Dify tem mais recursos para producao. Use Flowise para prototipar, Dify para escalar.
