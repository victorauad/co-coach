"""
Lê um CSV exportado do HubSpot e mostra quantos deals existem por estágio.

Como usar:
    python deals-por-estagio.py seu-arquivo.csv

O script detecta automaticamente a coluna de estágio — funciona com
exportações em português ("Estágio do negócio") e inglês ("Deal Stage").
"""

import csv
import sys
from collections import Counter


NOMES_POSSIVEIS_DA_COLUNA = [
    "Deal Stage",
    "Estágio do negócio",
    "Estagio do negocio",
    "Stage",
    "deal_stage",
    "stage",
]


def encontrar_coluna_estagio(cabecalhos):
    for nome in NOMES_POSSIVEIS_DA_COLUNA:
        if nome in cabecalhos:
            return nome
    # Busca parcial: aceita qualquer coluna que contenha "stage" ou "estágio"
    for cabecalho in cabecalhos:
        if "stage" in cabecalho.lower() or "estágio" in cabecalho.lower() or "estagio" in cabecalho.lower():
            return cabecalho
    return None


def analisar(caminho_csv):
    with open(caminho_csv, newline="", encoding="utf-8-sig") as f:
        leitor = csv.DictReader(f)
        cabecalhos = leitor.fieldnames or []

        coluna = encontrar_coluna_estagio(cabecalhos)
        if not coluna:
            print("Erro: não encontrei uma coluna de estágio no CSV.")
            print(f"Colunas disponíveis: {', '.join(cabecalhos)}")
            sys.exit(1)

        contagem = Counter()
        total = 0
        for linha in leitor:
            estagio = linha[coluna].strip() or "(sem estágio)"
            contagem[estagio] += 1
            total += 1

    print(f"\nArquivo: {caminho_csv}")
    print(f"Coluna usada: '{coluna}'")
    print(f"Total de deals: {total}")
    print("-" * 40)
    print(f"{'Estágio':<30} {'Qtd':>5}  {'%':>6}")
    print("-" * 40)
    for estagio, qtd in contagem.most_common():
        pct = qtd / total * 100 if total else 0
        print(f"{estagio:<30} {qtd:>5}  {pct:>5.1f}%")
    print("-" * 40)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python deals-por-estagio.py seu-arquivo.csv")
        sys.exit(1)

    analisar(sys.argv[1])
