# E-book: Mais cuidados para a primavera

Material gratuito de 10 páginas, entregue por WhatsApp a quem pede pela
página `docs/guia.html`.

## Arquivos

| Arquivo | O que é |
|---|---|
| `montar.py` | Monta o HTML a partir do conteúdo — **edite aqui** |
| `primavera.html` | O HTML gerado (não edite direto: `montar.py` sobrescreve) |
| `estilo.css` | O layout de impressão (A4, paleta da marca) |
| `gerar.mjs` | Renderiza o PDF via Chromium |
| `fotos/*.b64` | As fotos, já redimensionadas e em base64 |
| `Mais-cuidados-para-a-primavera.pdf` | O arquivo final |

## Como regerar depois de editar

```bash
python3 montar.py && node gerar.mjs
```

Edite o texto em `montar.py` e rode os dois comandos. O PDF é reescrito.

## Decisões

**Não fica em `docs/`** de propósito. Se estivesse, teria URL pública e
qualquer um baixaria direto — e a entrega manual por WhatsApp existe
justamente para começar uma conversa.

**Corpo em 12,6pt, margem lateral de 26mm.** A primeira versão usava 11,2pt
com margem de 22mm — pequeno demais para ler em tela, e com linha longa
demais para o olho voltar sozinho. A medida atual dá cerca de 75 caracteres
por linha, que é a faixa confortável.

**As fotos vêm do backup do site antigo**, redimensionadas para 1300px e
embutidas em base64 para o PDF não depender de arquivo externo. São cinco:
flores de primavera na capa, campo de girassóis, girassol ao entardecer,
prato de folhas, e o retrato dela no fechamento.

**A fonte é Bitstream Charter**, não a Spectral do site. Charter estava
disponível no sistema e foi desenhada para impressão; o site usa Google
Fonts, que não se pode embutir num PDF sem os arquivos da fonte.

**As fontes.** O conteúdo segue a terminologia como é ensinada no Brasil:
Fígado / Vesícula Biliar / elemento Madeira e as três funções do Fígado
(EBRAMEC); *vasanta ritucharya*, agravamento de kapha e enfraquecimento de
agni (Vida Veda e literatura de ritucharya). A página 5 — sobre a primavera
variar por região do Brasil — é o que diferencia este material de traduções
diretas de textos indianos.

**O guia não repete o curso.** Ele apresenta a estação e entrega o mapa de
observação; o curso Desperte a Sua Saúde na Primavera aprofunda, e tem um
módulo inteiro de planejamento que o guia nem toca. A última página do PDF
menciona o curso como o passo seguinte para quem quer seguir sozinha.
