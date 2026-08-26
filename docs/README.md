# Site estático — Fernanda Scheffer, Naturóloga

Versão em HTML puro do site que rodava em WordPress. Sem PHP, sem banco de
dados, sem plugins: são arquivos de texto que qualquer servidor entrega.

## O que tem aqui

```
docs/
├── index.html            Início
├── terapeuticas.html     Os 7 atendimentos, com valores
├── cursos.html           Os 3 cursos, com link para a Hotmart
├── sobre.html            Bio e formação
├── depoimentos.html      Os 6 depoimentos
├── blog.html             Índice do blog
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
--sage-deep:  #8B9C7C;   /* verde da logo */
--sage-pale:  #C6D0C2;
--lilac:      #AB98BE;
--violet:     #6E6790;   /* roxo da logo */
--blush:      #E8CDB8;
```

> Esses tons foram lidos a olho da imagem da paleta. Se você tiver os códigos
> exatos, troque aqui e o site inteiro acompanha.

## Publicar no GitHub Pages

Nas configurações do repositório → **Pages** → *Deploy from a branch* →
branch `main`, pasta `/docs`. Em poucos minutos o site fica no ar, com HTTPS
gratuito e automático.

## O que ainda falta

- **As imagens.** O site antigo usava 61 imagens, todas hospedadas no domínio
  que está suspenso. Elas ficaram de fora para não gerar link quebrado. Quando
  a pasta `wp-content/uploads` estiver em mãos, é só colocar os arquivos em
  `assets/img/` e referenciar nas páginas.
- **A logo.** Hoje o cabeçalho usa o nome em tipografia. Com o arquivo da logo
  em `assets/img/`, vira imagem.

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
