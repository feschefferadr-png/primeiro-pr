#!/usr/bin/env bash
# Monta uma saudacao a partir de um nome.

saudacao() {
  local nome="$1"

  if [ -z "$nome" ]; then
    echo "Ola, visitante!"
    return 0
  fi

  echo "Ola, $nome!"
}

# Permite rodar direto: ./saudacao.sh Fernanda
if [ "${BASH_SOURCE[0]}" = "$0" ]; then
  saudacao "$1"
fi
