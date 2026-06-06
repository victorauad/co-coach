# Onyx

**Repositorio:** github.com/onyx-dot-app/onyx
**Estrelas:** 17.3k

## O que e?

O Onyx e uma plataforma de chat com IA que voce hospeda no seu proprio servidor — nao na nuvem de terceiros. Ele conecta com mais de 40 fontes de dados (Google Drive, Slack, Notion, Confluence, GitHub, etc.) e permite que sua equipe faca perguntas sobre todos esses documentos usando linguagem natural.

## Para que serve?

Empresas que lidam com informacoes sensiveis e nao podem (ou nao querem) enviar documentos internos para servicos externos como o ChatGPT. Com o Onyx, tudo fica dentro da sua infraestrutura.

**Exemplos de uso:**
- "Qual e nossa politica de ferias?" — o Onyx busca no Notion e responde
- "Qual foi a decisao sobre o projeto X?" — ele busca no Slack e no Confluence
- Onboarding de novos funcionarios: eles perguntam e o Onyx explica
- Suporte tecnico interno conectado ao repositorio de codigo e documentacao

## Instalacao

### Pre-requisito: Docker instalado

### Passo 1: Clonar o repositorio

```bash
git clone https://github.com/onyx-dot-app/onyx.git
cd onyx/deployment/docker_compose
```

### Passo 2: Configurar variaveis de ambiente

```bash
cp .env.gpu-free.template .env
```

Edite o `.env` e adicione pelo menos:

```
GEN_AI_API_KEY=sua-chave-anthropic-aqui
AUTH_TYPE=disabled  # para teste local sem login
```

### Passo 3: Subir os servicos

```bash
docker compose -f docker-compose.dev.yml up -d
```

### Passo 4: Acessar

Abra `http://localhost:3000` e configure as conexoes com suas fontes de dados.

## Por que auto-hospedar?

- Seus documentos nunca saem da sua infraestrutura
- Conformidade com LGPD, GDPR e outras regulacoes
- Sem custo por usuario como nas versoes SaaS
- Controle total sobre os modelos de IA usados
