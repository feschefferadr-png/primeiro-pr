#!/usr/bin/env bash
# Transforma a copia de docs/ no ambiente de homologacao.
#
# Homologacao e producao servem o MESMO site. A unica diferenca sao as
# marcas abaixo, que existem para que o ambiente de teste nunca seja
# confundido com o site real nem apareca no Google.
#
# Uso, a partir do branch main ja atualizado:
#
#   git checkout -B homologacao main
#   ./homologacao.sh
#   git commit -am "Marcar como ambiente de homologacao"
#   git push -f homolog homologacao:main
#
# O branch homologacao e sempre recriado a partir do main, nunca mesclado.
# Assim as duas copias jamais divergem em conteudo.

set -euo pipefail
cd "$(dirname "$0")"

# 1. O CNAME reivindica o dominio proprio. Em homologacao ele nao pode
#    existir: dois repositorios pedindo o mesmo dominio se atrapalham.
rm -f docs/CNAME

# 2. O sitemap aponta para as URLs de producao. Nao serve aqui.
rm -f docs/sitemap.xml

# 3. Bloqueio de indexacao, arquivo e meta.
#    O robots.txt de um projeto em user.github.io/repo/ e ignorado pelos
#    buscadores (eles leem o da raiz do dominio), entao a meta em cada
#    pagina e o que de fato protege.
cat > docs/robots.txt <<'EOF'
User-agent: *
Disallow: /
EOF

marca='<meta name="robots" content="noindex, nofollow">'
for f in $(find docs -name '*.html'); do
  grep -q 'name="robots"' "$f" && continue
  # entra logo depois do viewport, que existe em todas as paginas
  perl -0pi -e "s{(<meta name=\"viewport\"[^>]*>\n)}{\$1$marca\n}" "$f"
  # prefixo no titulo, visivel na aba do navegador
  perl -0pi -e 's{<title>(?!\[HOMOLOG\])}{<title>[HOMOLOG] }' "$f"
done

echo "Homologacao marcada: $(find docs -name '*.html' | wc -l) paginas."
