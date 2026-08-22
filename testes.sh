#!/usr/bin/env bash
# Suite de testes do saudacao.sh

source "$(dirname "$0")/saudacao.sh"

falhas=0

verificar() {
  local descricao="$1"
  local esperado="$2"
  local obtido="$3"

  if [ "$esperado" = "$obtido" ]; then
    echo "  ok   - $descricao"
  else
    echo "  FALHA - $descricao"
    echo "          esperado: '$esperado'"
    echo "          obtido:   '$obtido'"
    falhas=$((falhas + 1))
  fi
}

echo "Rodando testes..."

verificar "sauda uma pessoa pelo nome" \
  "Ola, Fernanda!" "$(saudacao 'Fernanda')"

verificar "aceita nomes compostos" \
  "Ola, Ana Maria!" "$(saudacao 'Ana Maria')"

echo
if [ "$falhas" -eq 0 ]; then
  echo "Todos os testes passaram."
  exit 0
else
  echo "$falhas teste(s) falharam."
  exit 1
fi
