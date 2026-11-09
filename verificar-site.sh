#!/usr/bin/env bash
# Verifica o site em docs/ antes de cada commit.
#
# Existe para que qualquer mudanca -- feita a mao ou pela IA -- possa ser
# conferida em segundos, sem abrir o navegador. Sai com 0 quando esta tudo
# certo e 1 quando algo quebrou, listando o que foi.
#
# Uso: ./verificar-site.sh

set -uo pipefail
cd "$(dirname "$0")/docs"

falhas=0
falha() { echo "  FALHA - $1"; falhas=$((falhas + 1)); }
ok()    { echo "  ok    - $1"; }

paginas=$(find . -name '*.html' | sed 's|^\./||' | sort)

echo "Verificando o site..."

# 1. Links e imagens internos apontam para arquivos que existem.
antes=$falhas
for f in $paginas; do
  dir=$(dirname "$f")
  for alvo in $(grep -oE '(href|src)="[^"#?]+' "$f" | sed -E 's/^(href|src)="//' \
               | grep -vE '^(https?:|mailto:|tel:|//|data:)'); do
    caminho="$dir/$alvo"
    [[ $alvo == /* ]] && caminho=".$alvo"
    [ -e "$caminho" ] || falha "link quebrado em $f -> $alvo"
  done
done
[ $falhas -eq $antes ] && ok "todos os links e imagens internos existem"

# 2. Toda pagina tem titulo e descricao (a terapeuticas.html so redireciona).
antes=$falhas
for f in $paginas; do
  grep -q '<title>' "$f" || falha "$f sem <title>"
  [ "$f" = terapeuticas.html ] && continue
  grep -q 'name="description"' "$f" || falha "$f sem meta description"
done
[ $falhas -eq $antes ] && ok "toda pagina tem titulo e descricao"

# 3. Nada de homologacao vazou para producao.
antes=$falhas
[ -f CNAME ] || falha "CNAME sumiu: o dominio deixa de apontar para o site"
for f in $paginas; do
  grep -q '\[HOMOLOG\]' "$f" && falha "$f com [HOMOLOG] no titulo"
  [ "$f" = terapeuticas.html ] && continue
  grep -q 'noindex' "$f" && falha "$f com noindex: some do Google"
done
grep -q 'Disallow: /$' robots.txt 2>/dev/null && falha "robots.txt bloqueia o site inteiro"
[ $falhas -eq $antes ] && ok "sem marcas de homologacao em producao"

# 4. Toda pagina publica esta no sitemap.
antes=$falhas
[ -f sitemap.xml ] || { falha "sitemap.xml sumiu"; paginas_sitemap=""; }
for f in ${paginas_sitemap-$paginas}; do
  [ "$f" = terapeuticas.html ] && continue
  url="https://fernandascheffer.com/$f"
  [ "$f" = index.html ] && url="https://fernandascheffer.com/"
  grep -q "<loc>$url</loc>" sitemap.xml || falha "$f fora do sitemap.xml"
done
[ $falhas -eq $antes ] && ok "toda pagina publica esta no sitemap"

# 5. O ?dp=1 do Saude como Forma de Vida continua la (ver docs/README.md).
if grep -q 'H58750957Q' cursos.html && ! grep -q 'H58750957Q?dp=1' cursos.html; then
  falha "link do Saude como Forma de Vida perdeu o ?dp=1 -- o checkout nao abre"
else
  ok "link da Hotmart com ?dp=1 preservado"
fi

echo
if [ $falhas -eq 0 ]; then
  echo "Site ok."
  exit 0
else
  echo "$falhas problema(s) encontrado(s)."
  exit 1
fi
