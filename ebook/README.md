# E-book: Mais cuidados para a primavera

Material gratuito de 10 páginas, entregue por WhatsApp a quem pede pela
página `docs/guia.html`.

## Arquivos

| Arquivo | O que é |
|---|---|
| `primavera.html` | O conteúdo, em HTML |
| `estilo.css` | O layout de impressão (A4, paleta da marca) |
| `gerar.mjs` | Renderiza o PDF via Chromium |
| `Mais-cuidados-para-a-primavera.pdf` | O arquivo final |

## Como regerar depois de editar

```bash
node gerar.mjs
```

Edite o texto em `primavera.html` e rode o comando. O PDF é reescrito.

## Decisões

**Não fica em `docs/`** de propósito. Se estivesse, teria URL pública e
qualquer um baixaria direto — e a entrega manual por WhatsApp existe
justamente para começar uma conversa.

**A fonte é Bitstream Charter**, não a Spectral do site. Charter estava
disponível no sistema e foi desenhada para impressão; o site usa Google
Fonts, que não se pode embutir num PDF sem os arquivos da fonte.

**O guia não repete o curso.** Ele apresenta a estação e entrega o mapa de
observação; o curso Desperte a Sua Saúde na Primavera aprofunda, e tem um
módulo inteiro de planejamento que o guia nem toca. A última página do PDF
menciona o curso como o passo seguinte para quem quer seguir sozinha.
