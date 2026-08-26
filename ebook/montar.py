# -*- coding: utf-8 -*-
"""Monta o HTML do e-book de primavera. Rode e depois: node gerar.mjs"""
logo = open('logo.b64').read().strip()

def foto(nome, classe, alt=""):
    b64 = open(f'fotos/{nome}.b64').read().strip()
    return f'<img class="{classe}" src="data:image/jpeg;base64,{b64}" alt="{alt}">'


def pg(conteudo, n=None, blobs=""):
    rodape = (f'<div class="numero"><span>Mais cuidados para a primavera</span>'
              f'<span>{n}</span></div>') if n else ''
    return f'<div class="pagina">{blobs}{conteudo}{rodape}</div>\n'

B1 = '<div class="blob" style="width:120mm;height:115mm;background:var(--sage-pale);opacity:.45;top:-40mm;right:-35mm"></div>'
B2 = '<div class="blob" style="width:80mm;height:78mm;background:var(--lilac);opacity:.22;bottom:-25mm;left:-25mm;border-radius:46% 54% 58% 42% / 52% 44% 56% 48%"></div>'
B3 = '<div class="blob" style="width:70mm;height:68mm;background:var(--blush);opacity:.35;top:-22mm;left:-20mm"></div>'

P = []

# ---------------------------------------------------------------- 1. capa
P.append(pg(f'''
  {foto("capa", "foto-capa", "Flores de primavera")}
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <img src="data:image/png;base64,{logo}" style="width:34mm;margin-bottom:9mm">
    <p class="rotulo">Guia de autocuidado</p>
    <h1>Mais cuidados<br>para a primavera</h1>
    <p style="font-size:13pt;color:var(--ink-2);max-width:112mm;margin-top:8mm;line-height:1.5">
      Como a medicina tradicional chinesa e o ayurveda leem esta estação — e o que muda
      na sua rotina, na sua mesa e no seu descanso quando o ano vira.</p>
  </div>
  <div style="border-top:.3mm solid var(--sage-pale);padding-top:5mm">
    <p style="font-family:'Liberation Sans',sans-serif;font-size:9pt;color:var(--ink-3);letter-spacing:.04em">
      Fernanda Scheffer · Naturóloga<br>
      Pós-graduada em Psicologia Analítica · Pós-graduanda em Estilo de Vida</p>
  </div>''', blobs=B1+B2))

# ---------------------------------------------------------------- 2. como usar
P.append(pg('''
  <p class="rotulo">Como usar</p>
  <h2>Uma mudança de cada vez</h2>

  <div class="bloco">
    <p>Leia inteiro uma vez, sem anotar nada. Depois escolha <strong>uma</strong> mudança — só uma —
    e sustente por duas semanas antes de acrescentar qualquer outra.</p>
    <p>É contraintuitivo, mas funciona melhor: cinco mudanças ao mesmo tempo costumam durar quatro
    dias, enquanto uma mudança pequena sustentada vira hábito. E hábito é o que muda saúde.</p>
  </div>

  <div class="caixa lilas">
    <h3>Antes de qualquer coisa</h3>
    <p>Este é material de educação em saúde, não prescrição — e não foi escrito para o seu caso,
    porque eu ainda não o conheço.</p>
    <p style="margin-bottom:0">Nada aqui substitui acompanhamento médico. Se você tem condição
    diagnosticada, usa medicação contínua, está gestante ou apresenta sintomas persistentes,
    converse com seu médico antes de mudar hábitos — e siga com o tratamento que já faz. O cuidado
    integrativo caminha <strong>junto</strong> com a medicina, nunca no lugar dela.</p>
  </div>

  <div class="destaque-frase">
    Seu corpo não está contra você. Ele está se comunicando.
  </div>''', n=2, blobs=B3))

# ---------------------------------------------------------------- 3. medicina chinesa
P.append(pg(f'''
  {foto("campo", "faixa", "Campo de girassóis")}
  <p class="rotulo">A estação · parte um</p>
  <h2>Primavera na medicina chinesa</h2>

  <div class="bloco">
    <p>Na teoria dos cinco movimentos, a primavera corresponde ao elemento <strong>Madeira</strong>,
    ao órgão <strong>Fígado</strong> e à víscera <strong>Vesícula Biliar</strong>. Depois do
    recolhimento do inverno, é a estação em que tudo o que estava guardado começa a se mover —
    na natureza e em nós.</p>
  </div>

  <div class="caixa">
    <h3>O que a estação pede</h3>
    <p style="margin-bottom:0">Movimento suave e regular: alongamento, caminhada, ar livre. Menos
    rigidez na agenda. E espaço para a raiva ser sentida em vez de engolida — emoção contida é,
    nessa leitura, Qi parado, e Qi parado é onde o desconforto se instala.</p>
  </div>''', n=3))

# ---------------------------------------------------------------- 4. as tres funcoes
P.append(pg('''
  <p class="rotulo">A estação · parte um</p>
  <h2>As três funções do Fígado</h2>

  <p style="margin-bottom:6mm;color:var(--ink-2)">Cada uma explica um grupo diferente de sintomas
  desta época — e é por isso que vale conhecê-las separadamente.</p>

  <div class="bloco">
    <h3>Regula e suaviza o fluir do Qi</h3>
    <p>Quando esse fluir encontra obstáculo, aparece como irritabilidade, suspiros frequentes,
    sensação de aperto no peito ou pavio curto.</p>
  </div>

  <div class="bloco">
    <h3>Armazena o sangue</h3>
    <p>Daí a relação com o sono e com o ciclo menstrual — é à noite, em repouso, que o sangue
    retorna ao Fígado.</p>
  </div>

  <div class="bloco">
    <h3>Controla os tendões</h3>
    <p>É por isso que a rigidez desta época costuma aparecer em ombros, pescoço, mandíbula e atrás
    dos joelhos, e não em qualquer lugar.</p>
  </div>

  <div class="caixa lilas">
    <p style="margin-bottom:0">A tradição acrescenta que o Fígado <em>se abre nos olhos</em> — o que
    dá contexto aos olhos secos, cansados ou sensíveis à luz que muita gente relata justamente nesta
    estação.</p>
  </div>''', n=4, blobs=B1))

# ---------------------------------------------------------------- 4. ayurveda
P.append(pg('''
  <p class="rotulo">A estação · parte dois</p>
  <h2>Primavera no ayurveda</h2>

  <div class="bloco">
    <p>O ayurveda chama de <em>ritucharya</em> o conjunto de ajustes sazonais, e de
    <strong>vasanta ritucharya</strong> os que dizem respeito à primavera.</p>
    <p>Durante o inverno o corpo acumula <strong>kapha</strong> — a qualidade densa, úmida e pesada.
    Com o calor que chega, esse acúmulo se liquefaz e passa a circular. É a lógica da neve que
    derrete: o que estava parado se move, e o movimento passa por onde couber.</p>
  </div>

  <div class="bloco">
    <h3>Duas coisas acontecem ao mesmo tempo</h3>
    <ul>
      <li><strong>Kapha se agrava</strong> — congestão, catarro, peso ao acordar, letargia,
      retenção de líquido, vontade de ficar.</li>
      <li><strong>Agni enfraquece.</strong> O fogo digestivo, que estava forte no inverno, perde
      força justo agora. Por isso a mesma refeição que caía bem em julho começa a pesar em outubro.</li>
    </ul>
    <p>Essa combinação explica o paradoxo da estação: o clima melhora, os dias alongam, e o corpo
    parece não acompanhar.</p>
  </div>

  <div class="caixa pessego">
    <h3>Onde as duas tradições se encontram</h3>
    <p>Vindas de lugares e séculos diferentes, chinesa e ayurvédica chegam à mesma orientação
    prática para esta estação: <strong>leveza e movimento</strong>. Menos peso na comida, mais
    circulação no corpo, e uma rotina que não prenda.</p>
  </div>''', n=5, blobs=B2))

# ---------------------------------------------------------------- 5. o Brasil
P.append(pg('''
  <p class="rotulo">Uma ressalva necessária</p>
  <h2>A primavera brasileira não é uma só</h2>

  <div class="bloco">
    <p>Quase todo material sobre estações traduz textos escritos para o clima da Índia ou do
    hemisfério norte. Aqui isso não funciona direto, e vale dizer com honestidade: <strong>o que
    a sua primavera pede depende de onde você mora.</strong></p>
  </div>

  <div class="bloco">
    <h3>Sul</h3>
    <p>A primavera pode seguir fria e muito úmida por semanas. A transição de kapha é lenta, e os
    ajustes de leveza fazem sentido por mais tempo — sem pressa de aliviar o aquecimento.</p>
  </div>

  <div class="bloco">
    <h3>Sudeste</h3>
    <p>Um dia parece inverno e o seguinte parece verão. Vata e kapha se alternam, e o corpo gasta
    energia só para acompanhar a oscilação. Aqui o que mais ajuda é <strong>regularidade</strong>:
    horários estáveis de comer e dormir funcionam como âncora quando o clima não dá nenhuma.</p>
  </div>

  <div class="bloco">
    <h3>Centro-Oeste e Nordeste</h3>
    <p>Calor e secura chegam cedo, e pitta e vata sobem antes que kapha tenha terminado de sair.
    Aqui a leveza continua valendo, mas com atenção redobrada à hidratação e ao excesso de
    picante — o que serviria a uma primavera fria pode aquecer demais.</p>
  </div>

  <div class="caixa lilas">
    <p style="margin-bottom:0">Se as recomendações das próximas páginas não baterem com o que você
    sente, <strong>confie no que você sente</strong>. O corpo à sua frente vale mais que o texto
    na página — inclusive este.</p>
  </div>''', n=6, blobs=B3))

# ---------------------------------------------------------------- 7. rotina, manha
P.append(pg(f'''
  {foto("entardecer", "faixa", "Girassol ao entardecer")}
  <p class="rotulo">A rotina do dia</p>
  <h2>Dinacharya, ajustada à estação</h2>

  <p style="margin-bottom:7mm;color:var(--ink-2)">O ayurveda chama de <em>dinacharya</em> a rotina
  diária — a ideia de que a hora em que você faz cada coisa importa tanto quanto a coisa em si.</p>

  <div class="bloco">
    <h3>Ao acordar</h3>
    <ul style="margin-bottom:0">
      <li>Levante mais cedo do que levantava no inverno. Dormir demais na primavera aumenta o peso, não o descanso.</li>
      <li>Raspe a língua e beba um copo de água morna antes de qualquer outra coisa.</li>
      <li>Movimente-se antes de sentar: cinco minutos de alongamento já mudam o dia.</li>
    </ul>
  </div>''', n=7))

# ---------------------------------------------------------------- 8. rotina, dia e noite
P.append(pg('''
  <p class="rotulo">A rotina do dia</p>
  <h2>Do meio-dia ao adormecer</h2>

  <div class="bloco">
    <h3>Ao longo do dia</h3>
    <ul>
      <li>Almoce no meio do dia, quando o agni está no ponto mais alto que consegue nesta época.</li>
      <li><strong>Evite dormir durante o dia.</strong> O cochilo depois do almoço agrava kapha e
      atrapalha tanto a digestão quanto o sono da noite — é das recomendações mais consistentes
      para esta estação.</li>
      <li>Procure ar livre e luz natural, nem que seja por dez minutos.</li>
    </ul>
  </div>

  <div class="bloco">
    <h3>À noite</h3>
    <ul>
      <li>Jante cedo e leve — idealmente três horas antes de deitar.</li>
      <li>Diminua as telas na última hora, ou ao menos a luz delas.</li>
      <li>Se o sono ficou mais leve nesta época, escureça mais o quarto: a primavera clareia o fim
      da tarde e o corpo responde à luz.</li>
    </ul>
  </div>

  <div class="caixa lilas">
    <p style="margin-bottom:0">Se for escolher <strong>uma só</strong> destas mudanças, escolha o
    jantar mais cedo. É a que costuma render diferença mais rápido, e a que menos exige de você.</p>
  </div>''', n=8, blobs=B3))

# ---------------------------------------------------------------- 7. mesa
P.append(pg(f'''
  {foto("mesa", "faixa", "Prato de folhas e legumes frescos")}
  <p class="rotulo">A mesa</p>
  <h2>O que favorece e o que pesa</h2>

  <p style="margin-bottom:6mm;color:var(--ink-2)">Não é dieta, é direção. Com o agni mais fraco e
  kapha em movimento, o corpo pede o que é leve, seco e levemente aquecido.</p>

  <div class="duas">
    <div class="caixa" style="margin:0">
      <h3>Favorece</h3>
      <ul style="margin-bottom:0">
        <li>Sabores <strong>amargo, picante e adstringente</strong></li>
        <li>Folhas amargas — rúcula, agrião, almeirão, dente-de-leão</li>
        <li>Grãos mais leves: cevada, milho, lentilha</li>
        <li>Preparos leves e secos: refogados, grelhados, assados</li>
        <li>Especiarias que acendem o agni: gengibre, pimenta-do-reino, cúrcuma, canela</li>
        <li>Bebidas mornas ou quentes ao longo do dia</li>
      </ul>
    </div>
    <div class="caixa pessego" style="margin:0">
      <h3>Pesa</h3>
      <ul style="margin-bottom:0">
        <li>Laticínios em excesso, principalmente à noite</li>
        <li>Frituras e preparos muito oleosos</li>
        <li>Doces e farinhas refinadas</li>
        <li>Gelados e bebidas muito frias</li>
        <li>Comer tarde da noite</li>
        <li>Repetir o prato sem fome</li>
      </ul>
    </div>
  </div>

  <p style="margin-top:6mm;font-size:11.8pt;color:var(--ink-2)">E antes de comer, uma pergunta que
  vale mais que a lista inteira: <strong>estou com fome, ou com outra coisa?</strong> Com o agni
  enfraquecido, a vontade de comer aumenta sem que a fome aumente junto.</p>''', n=9, blobs=B2))

# ---------------------------------------------------------------- 8. práticas
P.append(pg('''
  <p class="rotulo">Duas práticas</p>
  <h2>Para fazer, não para saber</h2>

  <div class="caixa">
    <h3>Uma respiração para quando a irritação subir</h3>
    <p>Serve para o momento em que você percebe o pavio encurtando — no trânsito, numa reunião,
    numa conversa que azedou.</p>
    <p><strong>Expire mais do que inspira.</strong> Inspire pelo nariz contando até quatro. Solte o
    ar pela boca, devagar, contando até seis ou oito. Repita cinco vezes.</p>
    <p style="margin-bottom:0">A expiração alongada é o que sinaliza ao corpo que ele pode sair do
    alerta. Funciona em menos de um minuto, e ninguém à sua volta precisa perceber.</p>
  </div>

  <div class="caixa lilas">
    <h3>Um movimento para a manhã</h3>
    <p>De pé, pés na largura do quadril. Inspire subindo os braços pelos lados até acima da cabeça.
    Expire descendo o tronco à frente, joelhos levemente dobrados, deixando cabeça e braços
    pendurados.</p>
    <p>Fique aí três respirações. Suba devagar, vértebra por vértebra. <strong>Repita cinco vezes.</strong></p>
    <p style="margin-bottom:0">Leva dois minutos e alonga justamente a cadeia que a estação tende a
    encurtar — costas, posterior das pernas, pescoço. Os tendões que o Fígado governa.</p>
  </div>

  <div class="bloco">
    <p style="font-size:10.4pt;color:var(--ink-2)">Se sentir dor durante qualquer uma das duas, pare.
    Desconforto de alongamento é uma coisa; dor é outra, e é informação para investigar, não para
    atravessar.</p>
  </div>''', n=10, blobs=B3))

# ---------------------------------------------------------------- 9. mapa
P.append(pg('''
  <p class="rotulo">Sete dias</p>
  <h2>Um mapa do seu próprio corpo</h2>

  <p style="margin-bottom:4mm">Esta é a parte mais útil do guia, e a que quase ninguém faz.</p>
  <p style="margin-bottom:5mm;color:var(--ink-2)">Por uma semana, anote três coisas por dia. Leva
  menos de um minuto, e no sétimo dia você enxerga padrões que passaram despercebidos a vida inteira.</p>

  <div class="caixa" style="margin-bottom:5mm">
    <p style="margin-bottom:2mm"><strong>Energia</strong> — nota de 0 a 10 ao acordar, no meio da tarde e à noite</p>
    <p style="margin-bottom:2mm"><strong>Jantar</strong> — a que horas, e se foi leve ou pesado</p>
    <p style="margin-bottom:0"><strong>Pausa</strong> — houve algum momento sem tela, sem tarefa, sem resolver nada?</p>
  </div>

  <table>
    <tr><th>Dia</th><th>Energia<br>manhã · tarde · noite</th><th>Jantar</th><th>Pausa</th></tr>
    <tr><td class="dia">Segunda</td><td></td><td></td><td></td></tr>
    <tr><td class="dia">Terça</td><td></td><td></td><td></td></tr>
    <tr><td class="dia">Quarta</td><td></td><td></td><td></td></tr>
    <tr><td class="dia">Quinta</td><td></td><td></td><td></td></tr>
    <tr><td class="dia">Sexta</td><td></td><td></td><td></td></tr>
    <tr><td class="dia">Sábado</td><td></td><td></td><td></td></tr>
    <tr><td class="dia">Domingo</td><td></td><td></td><td></td></tr>
  </table>''', n=11, blobs=B1))

# ---------------------------------------------------------------- 10. ler o mapa
P.append(pg('''
  <p class="rotulo">No sétimo dia</p>
  <h2>Como ler o que você anotou</h2>

  <div class="bloco">
    <p>Olhe a semana inteira de uma vez, não dia a dia. O que interessa não é nenhum dia isolado —
    é o que os dias piores têm em comum.</p>
  </div>

  <div class="bloco">
    <h3>Procure por estas relações</h3>
    <ul>
      <li>Os dias de energia baixa vieram <strong>depois</strong> de jantares tardios ou pesados?</li>
      <li>Os dias melhores tiveram pausa de verdade, ou foi coincidência?</li>
      <li>A queda da tarde acontece sempre no mesmo horário?</li>
      <li>A energia da noite é maior que a da manhã? Isso costuma dizer algo sobre o sono, não sobre disposição.</li>
    </ul>
  </div>

  <div class="caixa lilas">
    <h3>Se nada mudar</h3>
    <p>Se você ajustar o jantar, criar pausas, e ainda assim a semana toda for de energia baixa —
    isso também é informação, e das importantes. Cansaço persistente que não responde a mudança de
    hábito merece investigação médica: anemia, alterações de tireoide, apneia do sono e deficiências
    nutricionais aparecem exatamente assim.</p>
    <p style="margin-bottom:0"><strong>Procure um médico e peça exames.</strong> Nenhum guia, nenhuma
    prática integrativa e nenhum profissional não-médico substitui esse passo.</p>
  </div>''', n=12, blobs=B2))

# ---------------------------------------------------------------- 11. fechamento
P.append(pg(f'''
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    {foto("fernanda", "retrato-fim", "Fernanda Scheffer")}
    <p class="rotulo">Para seguir</p>
    <h2 style="font-size:22pt;margin-bottom:7mm">Se você quiser olhar isso<br>no seu caso</h2>

    <p style="margin-bottom:4mm">Este guia é geral — e é honesto dizer isso. Ele descreve tendências
    de uma estação, não o seu corpo, a sua história e o seu momento.</p>

    <p style="margin-bottom:4mm">Se a semana de observação levantou mais perguntas do que respostas,
    talvez seja hora de olhar isso com alguém junto.</p>

    <div class="caixa" style="margin-top:5mm">
      <h3>Acompanhamento Integrativo em Saúde</h3>
      <p>Duas consultas com 28 dias entre elas: uma inicial aprofundada, o tratamento e o plano
      personalizado, suporte por mensagem ao longo do período, e o retorno para avaliar o que mudou.
      Presencial em São Paulo e online para o Brasil inteiro.</p>
      <p style="margin-bottom:0"><strong>A conversa inicial é de vinte minutos e não custa nada</strong> —
      serve para a gente entender junto se faz sentido para você.</p>
    </div>

    <p style="font-size:11pt;color:var(--ink-2);margin-top:5mm">E se preferir seguir sozinha por
    enquanto, existe o curso <strong>Desperte a Sua Saúde na Primavera</strong> — cinco módulos
    gravados que aprofundam o que este guia apresenta.</p>

    <div style="margin-top:4mm">
      <p style="font-family:'Liberation Sans',sans-serif;font-size:10pt;line-height:1.7">
        <strong>WhatsApp</strong> · 11 95990-7416<br>
        <strong>Instagram</strong> · @fernandascheffer_<br>
        <strong>Site</strong> · fernandascheffer.com
      </p>
    </div>
  </div>

  <div style="border-top:.3mm solid var(--sage-pale);padding-top:5mm;display:flex;
              justify-content:space-between;align-items:flex-end">
    <p style="font-family:'Liberation Sans',sans-serif;font-size:8pt;color:var(--ink-3);line-height:1.6">
      Fernanda Scheffer · Naturóloga<br>
      Material de educação em saúde. Não substitui avaliação<br>nem tratamento médico.</p>
    <img src="data:image/png;base64,{logo}" style="width:24mm">
  </div>''', blobs=B2+B3))

html = ('<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8">\n'
        '<title>Mais cuidados para a primavera</title>\n'
        '<link rel="stylesheet" href="estilo.css"></head>\n<body>\n'
        + ''.join(P) + '</body></html>')
open('primavera.html','w',encoding='utf-8').write(html)
print(f"{len(P)} páginas montadas")
