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
