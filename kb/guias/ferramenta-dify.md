---
titulo: Dify
tema: ferramentas
tipo: guia
data: 2026-06-06
importancia: 3
---

# Dify

**Repositorio:** github.com/langgenius/dify
**Estrelas:** 130k+

## O que e?

O Dify e uma plataforma visual para criar aplicacoes de IA — sem precisar escrever codigo. Voce monta fluxos de trabalho arrastando blocos numa tela, conecta fontes de dados (PDFs, bancos de dados, APIs) e publica como uma aplicacao pronta.

## Para que serve?

Empresas que querem usar IA mas nao tem um time de engenharia para isso. O Dify permite criar chatbots internos, sistemas de Q&A sobre documentos, automacoes com IA e muito mais — tudo pela interface visual.

**Exemplos de uso:**
- Criar um chatbot que responde perguntas sobre o manual da empresa
- Montar um fluxo que recebe um PDF e gera um resumo automatico
- Construir um agente que pesquisa na web e consolida relatorios
- Criar aplicacoes de IA para clientes sem escrever uma linha de codigo

## Instalacao (via Docker)

### Pre-requisito: Docker instalado

Se nao tiver o Docker, baixe em docker.com/get-started.

### Passo 1: Clonar o repositorio

```bash
git clone https://github.com/langgenius/dify.git
cd dify/docker
```

### Passo 2: Configurar o ambiente

```bash
cp .env.example .env
```

Abra o arquivo `.env` e configure pelo menos a `SECRET_KEY`:

```
SECRET_KEY=coloque-aqui-uma-chave-secreta-qualquer
```

### Passo 3: Subir os servicos

```bash
docker compose up -d
```

### Passo 4: Acessar

Abra o navegador em: `http://localhost`

Crie sua conta de admin na primeira vez que acessar.

## Custo

Dify e open source e gratuito para auto-hospedar. Existe tambem uma versao cloud em dify.ai com plano gratuito limitado.
