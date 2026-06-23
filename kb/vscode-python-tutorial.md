---
titulo: "VS Code: Tutorial Completo de Python"
tema: ferramentas
url: https://code.visualstudio.com/docs/python/python-tutorial
data: 2026-06-22
fonte: vscode-docs
importancia: alta
---

# VS Code: Python — Do Zero ao Debug

Guia completo para configurar e usar Python no VS Code, incluindo execução de scripts e debugging.

## Pré-requisitos

1. **Python instalado** (a extensão do VS Code não inclui Python)
   - Mac: `brew install python3` no terminal
   - Windows: baixe em python.org ou Microsoft Store
   - Verifique: `python3 --version` (Mac/Linux) ou `py -3 --version` (Windows)

2. **Extensão Python** para VS Code (`ms-python.python`)

## Configuração Inicial

### Criar Ambiente Virtual

Command Palette → **Python: Create Environment** → Venv → selecione o interpretador Python.

O VS Code cria a pasta `.venv` na raiz do projeto automaticamente. Ambientes virtuais isolam os pacotes do projeto dos pacotes globais do sistema.

### Selecionar Interpretador

- Clique na versão Python na Status Bar (barra inferior)
- Ou: Command Palette → **Python: Select Interpreter**

## Executar um Script Python

1. Crie um arquivo `.py`
2. Clique no botão **▶ Run Python File** (canto superior direito)
3. Ou clique direito → **Run Python > Run Python File in Terminal**
4. Para executar apenas linhas selecionadas: `Shift+Enter`
5. Para REPL interativo: Command Palette → **Python: Start Terminal REPL**

## IntelliSense

Ao digitar, o VS Code oferece autocompletar para:
- Módulos padrão do Python
- Pacotes instalados no ambiente
- Funções e variáveis do arquivo atual

## Debugging — Encontrar e Corrigir Erros

### Adicionar Breakpoint
Clique na margem esquerda de uma linha (aparece círculo vermelho) ou pressione `F9`.

### Iniciar Debug
Pressione `F5` → selecione **Python File** (na primeira vez) → VS Code cria `launch.json`.

### Controles de Debug
| Ação | Atalho |
|------|--------|
| Continuar | F5 |
| Próxima linha (sem entrar) | F10 |
| Entrar na função | F11 |
| Sair da função | Shift+F11 |
| Reiniciar | Ctrl+Shift+F5 |
| Parar | Shift+F5 |

### Inspecionar Variáveis

No painel **Variables** (durante debug), veja todos os valores atuais. No **Debug Console**, execute comandos para inspecionar:
- Digite `msg` → mostra o valor
- Digite `msg.upper()` → executa transformações

### Logpoints (alternativa ao print)
No lugar de `print()`, clique direito na margem → **Add Logpoint** → define mensagem de log sem parar a execução.

## Gerenciar Pacotes

### Via Interface do VS Code
1. Activity Bar → seção **Python Environments**
2. Expanda o ambiente → **Manage Packages**
3. Pesquise e instale

### Via Terminal
```bash
pip install numpy pandas matplotlib
pip freeze > requirements.txt       # salvar dependências
pip install -r requirements.txt     # reinstalar em outro ambiente
```

## Extensões Python Úteis

- `ms-python.python` — suporte principal (obrigatório)
- `ms-python.black-formatter` — formatação automática
- `ms-python.pylint` — análise de erros em tempo real
- `ms-toolsai.jupyter` — notebooks Jupyter
