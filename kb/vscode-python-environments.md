---
titulo: "VS Code: Ambientes Python (venv, conda, pyenv)"
tema: ferramentas
url: https://code.visualstudio.com/docs/python/environments
data: 2026-06-22
fonte: vscode-docs
importancia: media
---

# VS Code: Ambientes Python

Como gerenciar ambientes virtuais Python no VS Code — criação, seleção e gerenciamento de pacotes.

## Por que Usar Ambientes Virtuais?

Cada projeto pode ter versões diferentes de pacotes. Um ambiente virtual isola as dependências do projeto das instalações globais do sistema — evita conflitos e facilita reprodução em outras máquinas.

## Gerenciadores Suportados

O VS Code detecta automaticamente ambientes criados com:
- **venv** — padrão do Python, simples
- **conda** — popular em data science, gerencia Python + pacotes não-Python
- **pyenv** — gerencia múltiplas versões do Python
- **poetry** — gerenciamento avançado de dependências
- **pipenv** — combina pip + virtualenv

## Selecionar Interpretador

- Clique na versão Python na **Status Bar** (barra inferior do VS Code)
- Command Palette → **Python: Select Interpreter**

A extensão busca automaticamente em:
- Pasta `.venv` do projeto
- PATH do sistema
- Ambientes conda (`conda info --envs`)
- Pyenv (`$PYENV_ROOT/versions`)

## Criar Ambiente

### Rápido (Quick Create)
Clique no botão **+** na seção Environment Managers. Usa padrões (venv, Python mais recente, nome `.venv`).

### Personalizado
Command Palette → **Python: Create Environment** → escolha:
1. Gerenciador (venv ou conda)
2. Versão do Python
3. Nome do ambiente
4. Arquivo de dependências (`requirements.txt` ou `pyproject.toml`)

### Com uv (mais rápido)
Se tiver `uv` instalado, o VS Code usa automaticamente para criar e instalar pacotes mais rápido. Force com `"python-envs.alwaysUseUv": true`.

## Gerenciar Pacotes pela Interface

1. Activity Bar → **Python Environments**
2. Expanda o ambiente
3. Clique direito → **Manage Packages**
4. Pesquise e selecione pacotes para instalar

Para desinstalar: expanda o ambiente → clique direito no pacote → **Uninstall Package**.

## Configurar Caminhos de Busca

### Dentro do workspace (relativo)
```json
// .vscode/settings.json
{
  "python-envs.workspaceSearchPaths": ["./**/.venv", "./envs/**"]
}
```

### Fora do workspace (absoluto)
```json
// settings.json
{
  "python-envs.globalSearchPaths": ["/Users/victor/envs", "/opt/shared-envs"]
}
```

## Variáveis de Ambiente (.env)

Para injetar credenciais/configurações sem commitar:
1. Crie `.env` na raiz do projeto
2. `"python.terminal.useEnvFile": true` nas settings
3. Defina no `.env`: `MINHA_CHAVE=valor`

As variáveis são injetadas automaticamente no terminal e nas execuções de scripts.

## Ativação Automática no Terminal

O VS Code ativa o ambiente ao abrir o terminal. Configure com `python-envs.terminal.autoActivationType`:
- `command` — mostra o comando de ativação (padrão)
- `shellStartup` — ativa via script de inicialização do shell
- `off` — desativa a ativação automática

## requirements.txt

Para compartilhar dependências com o time:
```bash
pip freeze > requirements.txt      # exportar ambiente atual
pip install -r requirements.txt    # reinstalar em nova máquina
```

O VS Code detecta `requirements.txt` automaticamente ao criar novos ambientes.
