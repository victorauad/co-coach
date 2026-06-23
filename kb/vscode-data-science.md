---
titulo: "VS Code: Tutorial de Data Science (Titanic + ML)"
tema: ferramentas
url: https://code.visualstudio.com/docs/datascience/data-science-tutorial
data: 2026-06-22
fonte: vscode-docs
importancia: media
---

# VS Code: Data Science na Prática

Tutorial completo da Anthropic cobrindo análise de dados reais, visualização e modelo de machine learning dentro do VS Code com Jupyter Notebooks.

## Ferramentas Necessárias

- VS Code com extensões: **Python** + **Jupyter**
- Python com: `pandas`, `jupyter`, `seaborn`, `scikit-learn`, `keras`, `tensorflow`
- Opcional: Miniconda ou Anaconda

## Fluxo Típico de Análise de Dados

### 1. Carregar Dados

```python
import pandas as pd
import numpy as np

df = pd.read_csv('dados.csv', na_values='?')
```

O **Data Viewer** do VS Code permite explorar o DataFrame visualmente com ordenação e filtros — sem precisar escrever código.

### 2. Limpar Dados

```python
# Corrigir tipos
df['coluna'] = df['coluna'].astype(float)

# Substituir valores ausentes
df['coluna'].fillna(df['coluna'].median(), inplace=True)

# Converter categórico em numérico
df['sexo'] = df['sexo'].map({'male': 1, 'female': 0})
```

### 3. Visualizar com Seaborn/Matplotlib

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.violinplot(x='sobreviveu', y='idade', hue='sexo', data=df)
plt.show()
```

Gráficos aparecem inline no notebook, abaixo da célula executada.

### 4. Análise de Correlação

```python
print(abs(df.corr()['sobreviveu']).sort_values(ascending=False))
```

Variáveis mais próximas de 1.0 têm maior relação com o resultado a prever.

### 5. Preparar Dados para Modelo

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Separar features e target
X = df[['sexo', 'classe', 'idade', 'familiares', 'tarifa']]
y = df['sobreviveu']

# 80% treino, 20% teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Normalizar
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

### 6. Treinar Modelo (Naive Bayes)

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X_train, y_train)
print(f'Acurácia: {model.score(X_test, y_test):.2%}')
# ~75% de acurácia
```

### 7. Rede Neural com Keras

```python
from keras.models import Sequential
from keras.layers import Dense

model = Sequential([
    Dense(5, input_dim=5, activation='relu'),
    Dense(5, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50, batch_size=32)
# ~79% de acurácia — melhor que Naive Bayes
```

## Recursos do VS Code para Data Science

### Data Wrangler
Extensão `ms-toolsai.datawrangler` — interface visual para limpar e transformar dados sem código. Gera o código Python automaticamente.

### Explorador de Variáveis
Painel **Variables** durante execução de notebook → veja todos os DataFrames e arrays com uma linha de resumo.

### Data Viewer
Duplo clique em qualquer DataFrame no explorador de variáveis → interface de tabela com filtros e ordenação.

## Perfil Recomendado

Use o template **Data Science Profile** do VS Code (Profiles → Create Profile → Data Science) — inclui todas as extensões relevantes pré-configuradas.
