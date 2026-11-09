# Contexto para a IA

Este arquivo é lido automaticamente no início de cada sessão do Claude Code.
Ele existe para que a IA não precise redescobrir o projeto toda vez.
Mantenha-o curto e atualizado: quando uma decisão mudar, mude aqui também.

## O que é este repositório

Apesar do nome `primeiro-pr`, o projeto principal é o **site da Fernanda
Scheffer, naturóloga** — <https://fernandascheffer.com>, servido pelo GitHub
Pages a partir de `docs/` no branch `main`.

| Pasta / arquivo | O que é |
|---|---|
| `docs/` | O site, HTML puro + um CSS. **Leia `docs/README.md` antes de mexer** — lá estão a oferta, os elementos de conversão e as decisões |
| `ebook/` | O e-book gratuito (PDF). Edite `montar.py`, nunca `primavera.html`. Ver `ebook/README.md` |
| `homologacao.sh` | Gera a cópia de teste. Rode só no branch `homologacao`, nunca no `main` |
| `verificar-site.sh` | Confere links, metadados, sitemap e vazamento de homologação |
| `saudacao.sh`, `testes.sh` | Exercício antigo de Git, sem relação com o site |

## Regras que não se quebram

- **Uma oferta só**: acompanhamento de 28 dias, R$ 350 (ou 2x R$ 175).
  Nenhuma prática ganha preço ou botão próprio.
- **Linguagem condicional** nas práticas ("Indicada para"), e o parágrafo
  sobre evidência científica e acompanhamento médico fica (orientação CABSIN).
  Nunca prometer cura nem tratar diagnóstico.
- **O `?dp=1` do link `H58750957Q`** na Hotmart não sai.
- **Endereço do consultório**: só o bairro, nunca a rua.
- **Depoimentos** citando crianças ou diagnósticos não entram sem autorização.
- O e-book **não vai para `docs/`** — a entrega é manual, por WhatsApp.
- Sem build, sem framework, sem dependências: o site é editável à mão.

## Como trabalhar aqui

1. Antes de propor, leia a página inteira que vai mudar e o trecho
   correspondente de `docs/README.md`.
2. Depois de mudar, rode `./verificar-site.sh`. Só faça commit com "Site ok."
3. Se mudou algo descrito em `docs/README.md`, atualize o README no mesmo commit.
4. Decisões de negócio (preço, público, o que a Fernanda divulga) são dela:
   pergunte em vez de decidir. Pode sugerir, com o motivo.
5. Escreva em português, com o tom do site: direto, acolhedor, sem jargão de
   marketing.

## Commits

Título no infinitivo, em português, sem acento (ex.: "Trocar o botao da home").
O corpo explica **por quê** e o que ficou de fora de propósito — é a memória
do projeto. Um assunto por commit.

## Pendências conhecidas

Dependem de informação ou decisão da Fernanda — não invente:

- Público prioritário (adulto x infantil).
- Preço definitivo, depois do cálculo do piso econômico.
- Preço e prova social na página de cursos (valores atuais da Hotmart).
- Resultados e depoimentos do novo acompanhamento (após os 10 primeiros).
- Capas dos cursos e ilustrações do backup ainda não usadas.
- Formulário de lista (Mailchimp/Brevo) no `guia.html`, quando houver lista.
