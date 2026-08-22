# primeiro-pr

Repositorio pequeno para praticar o ciclo de contribuicao no GitHub:
branch -> commit -> push -> Pull Request.

## O que tem aqui

- `saudacao.sh` - uma funcao que monta uma saudacao a partir de um nome.
- `testes.sh` - a suite de testes da funcao.

## Como usar

```bash
./saudacao.sh Fernanda
# Ola, Fernanda!
```

Sem nome, a funcao usa um tratamento padrao:

```bash
./saudacao.sh
# Ola, visitante!
```

## Como rodar os testes

```bash
./testes.sh
```

A saida lista cada teste e termina com o total de falhas. O comando sai com
codigo 0 quando tudo passa e 1 quando algo falha.
