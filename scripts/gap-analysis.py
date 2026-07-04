#!/usr/bin/env python3
"""
Analisa a distribuição de temas em kb/ e sinaliza lacunas de conhecimento.
Gera docs/gap-analysis.json, consumido pela aba "Lacunas" do gerenciador.
"""

import json
import datetime
from pathlib import Path

KB_DIR = Path("kb")
DOCS_DIR = Path("docs")

TEMAS_CONHECIDOS = [
    "setup", "metodologia", "agentes", "mcp", "ferramentas",
    "workflow", "prompts", "service-as-software", "outros",
]

TEMA_PRIORITARIO = "service-as-software"
LIMIAR_POUCOS_ARQUIVOS = 2
LIMIAR_DIAS_PARADO = 60


def parse_frontmatter(text: str) -> dict:
    meta = {}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip()
    return meta


def load_kb_metadata() -> list[dict]:
    entradas = []
    for path in sorted(KB_DIR.glob("*.md")):
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not meta.get("tema"):
            continue
        entradas.append(meta)
    return entradas


def analisar(entradas: list[dict]) -> dict:
    hoje = datetime.date.today()
    por_tema = {tema: [] for tema in TEMAS_CONHECIDOS}

    for meta in entradas:
        tema = meta.get("tema", "outros")
        por_tema.setdefault(tema, []).append(meta)

    lacunas = []
    for tema, itens in por_tema.items():
        total = len(itens)
        datas = []
        for item in itens:
            try:
                datas.append(datetime.date.fromisoformat(item.get("data", "")))
            except ValueError:
                continue
        dias_parado = (hoje - max(datas)).days if datas else None

        motivos = []
        prioridade = "normal"

        if tema == TEMA_PRIORITARIO and total == 0:
            motivos.append("tema prioritário do direcionamento atual de aprendizado (tese Service-as-a-Software) e ainda não tem nenhum conteúdo indexado")
            prioridade = "alta"
        elif total <= LIMIAR_POUCOS_ARQUIVOS:
            motivos.append(f"apenas {total} arquivo(s) indexado(s)")
            if tema == TEMA_PRIORITARIO:
                prioridade = "alta"

        if dias_parado is not None and dias_parado > LIMIAR_DIAS_PARADO:
            motivos.append(f"sem conteúdo novo há {dias_parado} dias")

        if motivos:
            lacunas.append({
                "tema": tema,
                "total_arquivos": total,
                "dias_sem_atualizar": dias_parado,
                "prioridade": prioridade,
                "motivos": motivos,
            })

    lacunas.sort(key=lambda x: (x["prioridade"] != "alta", x["total_arquivos"]))

    return {
        "gerado_em": hoje.isoformat(),
        "total_kb": len(entradas),
        "contagem_por_tema": {t: len(v) for t, v in por_tema.items()},
        "lacunas": lacunas,
    }


def main():
    entradas = load_kb_metadata()
    resultado = analisar(entradas)

    DOCS_DIR.mkdir(exist_ok=True)
    out_path = DOCS_DIR / "gap-analysis.json"
    out_path.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Analisadas {len(entradas)} entradas da KB.")
    print(f"Lacunas encontradas: {len(resultado['lacunas'])}")
    for lacuna in resultado["lacunas"]:
        print(f"  [{lacuna['prioridade']}] {lacuna['tema']}: {', '.join(lacuna['motivos'])}")
    print(f"Salvo em: {out_path}")


if __name__ == "__main__":
    main()
