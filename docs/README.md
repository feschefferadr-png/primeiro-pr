# Site estático — Fernanda Scheffer, Naturóloga

Versão em HTML puro do site que rodava em WordPress. Sem PHP, sem banco de
dados, sem plugins: são arquivos de texto que qualquer servidor entrega.

## O que tem aqui

```
docs/
├── index.html            Início
├── acompanhamento.html   A oferta: acompanhamento de 3 meses
├── terapeuticas.html     Redirecionamento — a URL antiga aponta para a nova
├── cursos.html           Os 3 cursos, com link para a Hotmart
├── sobre.html            Bio e formação
├── depoimentos.html      Os 6 depoimentos
├── blog.html             Índice do blog
├── guia.html             Material gratuito — porta de entrada para a lista
├── contato.html          WhatsApp, e-mail e redes
├── blog/                 Os 6 textos do blog
├── favicon.svg           Ícone da aba do navegador
└── assets/css/site.css   Todo o visual do site
```

## Como editar

Cada página é um arquivo de texto. Abra, mude o que quiser entre as tags,
salve. Não existe painel, build nem compilação — o que está no arquivo é o
que aparece no navegador.

Para mudar cores ou tipografia, mexa só em `assets/css/site.css`. As cores da
marca estão logo no topo, em `:root`, e valem para o site inteiro:

```css
--sage-deep:  #889878;   /* verde da logo */
--sage-pale:  #C0C8B8;
--lilac:      #A898B0;
--violet:     #706888;   /* roxo da logo */
--blush:      #E0D0B8;
```

Valores extraídos pixel a pixel da imagem da Paleta Nova, não estimados.
Trocar esses cinco valores muda o site inteiro — é assim que se troca a
identidade visual sem mexer em mais nada.

## Publicar no GitHub Pages

Nas configurações do repositório → **Pages** → *Deploy from a branch* →
branch `main`, pasta `/docs`. Em poucos minutos o site fica no ar, com HTTPS
gratuito e automático.

## Imagens

Em `assets/img/`, todas já otimizadas para web:

| Arquivo | Onde aparece |
|---|---|
| `logo.png` | Cabeçalho de todas as páginas |
| `icone.png` | Ícone da aba do navegador |
| `fernanda.jpg` | Início e Sobre |
| `guilherme.jpg` `daniela.jpg` `gabriel.jpg` `camila.jpg` `rodolfo.jpg` `elisa.jpg` | Depoimentos |

A logo veio como JPEG com fundo branco; o branco foi removido e a arte
recortada, então ela assenta sobre qualquer cor de fundo.

### O que ainda pode entrar

As ilustrações dos serviços e dos cursos (`Design-sem-nome-*.png`,
`naturologia.jpg`, `desperta.jpeg` e companhia) estão no backup mas ainda não
foram usadas — as páginas de Terapêuticas e Cursos hoje são só texto e cor.

## A oferta

O site vende **uma coisa só**: um acompanhamento de três meses, por R$ 990
(ou 3x R$ 330). Não há serviços avulsos, nem preço por sessão, nem botão de
agendar por prática.

As oito práticas — floral, auriculoterapia, arte integrativa, ventosaterapia,
aromaterapia, dietoterapia chinesa, respiração e meditação — aparecem como
**glossário, não como cardápio**. Nenhuma tem preço próprio nem botão próprio,
e todas são descritas com "Indicada para", em linguagem condicional.

**Isso é deliberado. Não adicione preço nem botão de agendamento a nenhuma
prática individual** — seria voltar ao modelo avulso que o site abandonou de
propósito.

A página fecha com um parágrafo sobre graus de evidência científica e sobre o
cuidado caminhar junto ao acompanhamento médico, nunca no lugar dele. Isso
segue a orientação do CABSIN e não deve ser removido.

## O guia gratuito

`guia.html` existe para transformar leitor em contato. Hoje a entrega é
**manual, por WhatsApp** — funciona sem nenhum serviço externo e, no volume
atual, uma conversa vale mais que um e-mail capturado.

Dentro do HTML há um comentário marcando exatamente onde trocar o botão pelo
formulário embutido do Mailchimp ou do Brevo, quando existir lista. Peça só
nome e e-mail: cada campo a mais derruba a conversão.

**O material é o e-book "Mais Cuidados para o Inverno"**, que já acompanha um
dos cursos. A página foi escrita sem citar a estação no título justamente
para poder ser reaproveitada — mas o conteúdo entregue é de inverno, e vale
fazer uma versão de primavera quando der.

## Elementos de conversão

Cada um destes existe por um motivo. Se for mexer, saiba o que está desfazendo.

| Elemento | Onde | Por quê |
|---|---|---|
| Convite no fim de cada post | `blog/*.html` | Antes, os posts terminavam em "Voltar ao blog" — quem lia o texto inteiro não tinha para onde ir |
| Resumo e etiqueta na lista | `blog.html` | Só título não convida a clicar; e a data "2020" em tudo sinalizava blog abandonado |
| FAQ com seis perguntas | `acompanhamento.html` | Dúvidas que travam a decisão e que ninguém escreve para perguntar |
| Barra fixa no rodapé (celular) | `acompanhamento.html` | A página tem 8.000px; sem ela, quem se convence no meio precisa rolar até o fim |
| Ponte dos cursos | `cursos.html` | Quem chega pelo curso e quer atenção pessoal precisa saber que existe |

A barra fixa aparece **só** na página do acompanhamento, via `body.tem-cta-fixa`,
e só abaixo de 760px. O `padding-bottom` do body existe para ela não cobrir o
rodapé — se mudar a altura da barra, ajuste o padding junto.

### Ainda faltando nos cursos

A página não mostra **preço** nem **prova**. Os dois furos são reais e dependem
de informação que não está no backup: os valores atuais na Hotmart e algum
retorno de aluno. Capas existem no backup para dois dos três cursos.

## Os links da Hotmart

Dois cursos usam o link curto normal, que leva à página de vendas:

```
https://go.hotmart.com/X75026038O    Primavera
https://go.hotmart.com/G72063648B    Inverno
```

O terceiro precisa do parâmetro `?dp=1`, que pula direto para o checkout:

```
https://go.hotmart.com/H58750957Q?dp=1    Saúde como Forma de Vida
```

**Não remova esse `?dp=1` para "padronizar" os três.** Esse curso não tem
página de vendas publicada na Hotmart, então o link curto normal não abre.
Testado em agosto de 2026.

## Decisões que valem registro

- **A Hotmart cuida dos cursos** e o **WhatsApp cuida do contato** — os dois
  são links externos, então nada precisa rodar no servidor. Foi isso que tornou
  a migração possível.
- **O tema Astra não foi reaproveitado.** Era justamente ele que quebrou o site,
  por exigir uma versão de PHP mais nova que a do servidor. O visual foi
  reconstruído do zero em CSS, seguindo a paleta e a identidade da marca.
- **Os formulários de contato saíram.** Eram 5 formulários do plugin WPForms,
  a maioria em inglês e sem uso. O contato agora vai direto para o WhatsApp.
- **Os 4 "produtos" em inglês** (`Discovery Session`, `1:1 Coaching`,
  `Couple's Guidance`, `Self-Improvement`) ficaram de fora: eram conteúdo de
  demonstração de tema, não serviços reais.
