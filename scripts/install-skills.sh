#!/bin/bash
# Instala as skills do co-coach em um projeto ou globalmente.
# Uso: bash install-skills.sh /caminho/do/projeto
#      bash install-skills.sh --global
# Exemplo: bash install-skills.sh ~/meu-projeto-hubspot

set -e

SKILLS_SOURCE="$(cd "$(dirname "$0")/.." && pwd)/skills"
ARG="${1:-}"

if [ -z "$ARG" ]; then
  echo "Erro: informe o projeto alvo ou use --global."
  echo "Uso: bash install-skills.sh /caminho/do/projeto"
  echo "     bash install-skills.sh --global"
  exit 1
fi

if [ "$ARG" = "--global" ]; then
  TARGET_SKILLS="$HOME/.claude/skills"
  LABEL="global (~/.claude/skills)"
else
  if [ ! -d "$ARG" ]; then
    echo "Erro: pasta '$ARG' não encontrada."
    exit 1
  fi
  TARGET_SKILLS="$ARG/.claude/skills"
  LABEL="projeto '$ARG'"
fi

mkdir -p "$TARGET_SKILLS"

echo "Instalando skills em: $TARGET_SKILLS"
echo ""

INSTALLED=0
SKIPPED=0

for skill_dir in "$SKILLS_SOURCE"/*/; do
  skill_name=$(basename "$skill_dir")
  dest="$TARGET_SKILLS/$skill_name"

  if [ -d "$dest" ]; then
    # Atualiza o SKILL.md mesmo se a pasta já existir
    cp "$skill_dir/SKILL.md" "$dest/SKILL.md"
    echo "  🔄 $skill_name atualizada"
    SKIPPED=$((SKIPPED + 1))
  else
    cp -r "$skill_dir" "$dest"
    echo "  ✅ $skill_name instalada"
    INSTALLED=$((INSTALLED + 1))
  fi
done

echo ""
echo "Pronto — $LABEL"
echo "  $INSTALLED novas · $SKIPPED atualizadas"
echo ""
echo "Para atualizar no futuro:"
echo "  1. git pull neste repo (co-coach)"
echo "  2. bash scripts/install-skills.sh --global"
