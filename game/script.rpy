# The game starts here.
#imagem MiniJogo
image bolha1 = "bolha.png"
image bolha2 = "bolha.png"
image bolha3 = "bolha.png"
image mini11 = "img1-minijogo.png"
image mini12 = "mini12.png"
image mini13 = "mini13.png"
#Cenários
image quarto = "quarto.jpg"
image ruaVazia = "rua vazia.jpg"
image quarto2 = "quarto2.jpg"
image quartoNoite = "quarto a noite.jpg"
image quartoManuel = "QuartoManuel.png"
image ruaPolicia = "cenaPolicia.png"
image cenaCafe = "cenaCafe.jfif"
image rua2 = "rua2.jpg"
image sala = "sala.jpg"
image consultorio = "consultorio.jpg"
image cenaminijogo = "cena_minijogo.png"
#Imagens
image notFacelook  = "Facelook.png"
image toqCelular = "Trim!.png"
image notCompleta = "NoticiaCompleta.png"
image not1 = "Noticia 1.png"
image toqTel = "toqTel.png"
image email = "E-mail Projeto.png"
image not2 = "Noticia 2.png"
image porta = "porta.jpg"
image msgClara = "msgClara.png"
#noticias MiniJogo
image not1_bolha= "not1_bolha.png"
image not2_bolha= "not2_bolha.png"
image not3_bolha= "not3_bolha.png"
image not4_bolha= "not4_bolha.png"
#Personagens
image pers = "char1.1.png"
image persMask = "char1.3.png"
image policial = "policial.png"
image manuel = "manuel.png"
image desconhecida = "desconhecida.png"
image clara = "char2.1.png"
image lucas = "lucas1.1.png"
image lucasMask ="lucas1.2.png"
image mae = "mae.png"
image nutri = "nutri.png"
image alex = "alex.png"
image irmao = "irmao.png"
#Nomes meramente ilustrativos
define p = Character("Personagem", color = "#FF0000")
define m = Character("Manuel")
define c = Character("Policial")
define d = Character("Desconhecida")
define s = Character("Senhor")
define cl = Character("Clara")
define l = Character("Lucas")
define mae = Character("Mãe")
define n = Character("Nutricionista")
define bro= Character("Irmão")
define a= Character("Alex")

init python:

    def drag_placed(drags, drop):
        if not drop:
            return


        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name


        return True

label start:
    play music "audio/fundo.wav"
    scene black
    centered "Capítulo 1" with dissolve
    scene black
    centered "“O começo é a metade do todo.” - Platão" with pixellate

    $ botaoAbrirSite = True

    with pixellate
    scene ruaVazia


#Cena 1
    "Dezembro de 2019, um lado do planeta detecta uma doença que resultará em uma grande adversidade. Ruas vazias e pessoas cantando nas janelas logo será uma realidade... "

    "Surge a doença causado pelo coronavírus."

    with pixellate
    scene toqTel
    stop music
    play music "audio/toqueTelefone.ogg"
    $renpy.pause()
    stop music
    play music "audio/cena2.mp3"

    scene quarto2

    show pers at right:
            zoom 0.4
            yalign 0.65
    with dissolve

    p"E aí, tudo bem? Nossa, você viu essa notícia sobre a Covid-19?"


    scene not1
    $renpy.pause()
    scene quartoManuel:
        zoom 2.8
    #mudar cena
    show manuel at left:
        zoom 0.4
        yalign 0.65
    m"Nossa, eu vi, mas não acredito que seja tão grave, esses jornalistas são todos sensacionalistas. Além disso, deve ser só uma gripe, algo bem leve."

    scene quarto2 with dissolve
    show pers at right:
            zoom 0.4
            yalign 0.65
    with dissolve
    menu:
        "Não concordar.":
            p"Viu, a situação do pessoal na China é algo muito sério."

            scene quartoManuel:
                zoom 2.8
            #mudar cena
            show manuel at left:
                zoom 0.4
                yalign 0.65

            m"Mas, esses jornalistas... Não consigo confiar neles."

            scene quarto2 with pixellate

            show pers at right:
                    zoom 0.4
                    yalign 0.65
            with dissolve

            p"Podemos confiar sim, são profissionais capacitados para nos trazer fatos verídicos. Além disso, eles têm grande responsabilidade nos veículos de imprensa em que trabalham."

            scene quartoManuel:
                zoom 2.8
            #mudar cena
            show manuel at left:
                zoom 0.4
                yalign 0.65

            m"Entendi... Pelo jeito eles têm um dever com a verdade."

            scene quarto2

            show pers at right:
                    zoom 0.4
                    yalign 0.65
            with dissolve

            p"Pois é. Vou indo nessa, se cuida!"
        "Concordar.":
            p"Difícil opinar hein, mas eu não confio neles. Vamos ver se eles me convencem, não acho que a doença é grave."

            scene quartoManuel:
                zoom 2.8
            #mudar cena
            show manuel at left:
                zoom 0.4
                yalign 0.65

            m"Pois é. Vamos ver..."

            scene quarto2

            show pers at right:
                    zoom 0.4
                    yalign 0.65
            with dissolve
            p"Valeu pela conversa, até mais, se cuida!"

scene black
centered "Dias depois..." with dissolve

#Cena 2
scene quartoNoite

show manuel at left:
    zoom 0.4
    yalign 0.65
#Adicionar Manuel
m"Veja essa notícia que te mandei!"


show pers at right:
        zoom 0.4
        yalign 0.65
with dissolve

p"Já vou ver."

menu:
    "Ler a matéria completa.":
    #Abrir notícia completa
        with pixellate
        scene quartoNoite

        scene notCompleta:
            zoom 2.1
        $renpy.pause()
        with pixellate
        scene quartoNoite

        show pers at right:
                zoom 0.4
                yalign 0.65
        with dissolve

        show manuel at left:
            zoom 0.4
            yalign 0.65
        with pixellate


        p"Nossa, que notícia apelativa, é apenas uma falta temporária de álcool em gel, além de nem ser de uma fonte confiável. Vou denunciar essa notícia."
        m"Nossa, pode crer, olhei de novo, é apelativa mesmo e essa fonte nada a ver. Também vou denunciar."
        p"Por isso é sempre bom ler a matéria inteira e verificar a fonte."
        m"Vou fazer isso, foi mal cara."
        p"Tranquilo, vou dormir, boa noite!"
        jump quarto
    "Ler apenas a manchete.":
        scene notFacelook:
            zoom 1.2

        $renpy.pause()
        with pixellate
        scene quartoNoite

        show pers at right:
                zoom 0.4
                yalign 0.65
        with pixellate

        show manuel at left:
            zoom 0.4
            yalign 0.65
        with pixellate


        p"Eita cara! E agora?"
        m"Isso vai se tornar um caos, talvez seja preciso ir ao supermercado o mais rápido possível. Vou ler por completo a notícia."


label continua:
    menu:
        "Isso, melhor checar.":
            jump noticia
        "Será? Precisamos é ir correndo ao supermercado.":
            jump noticia
label noticia:


    m"Nossa, espera aí! Vou ler a notícia por completo."
    p"Beleza!"

    scene notCompleta:
        zoom 2.1
    $renpy.pause()

    scene quartoNoite

    show manuel at left:
        zoom 0.4
        yalign 0.65
    with pixellate



    m"Olha, não precisamos nos desesperar. O texto da notícia está citando a chegada da Covid-19 e a maior utilização de álcool, com uma suposta falta temporária de álcool gel em supermercados."

    show pers at right:
            zoom 0.4
            yalign 0.65
    with dissolve

    p"Que alívio. Na próxima vez, vamos ficar mais espertos com essas chamadas e prestar atenção nessa fonte, que é sensacionalista."
    m"Sim, cara, me senti idiota. Vamos ficar mais espertos mesmo, principalmente com a questão da fonte e não se desesperar antes de verificarmos a notícia por completa."
    p"Concordo com você, cara. Vou dormir que amanhã meu dia vai ser cheio, boa noite!"

label quarto:
#colocar imagem da sala ou porta abrindo...
#novo personagem

    scene black
    stop music
    play music "audio/toctoc.wav"
    queue music "audio/cena3.mp3"
    centered "Toc toc" with dissolve
    scene porta:
        zoom 1.5

    show policial at left:
            zoom 0.4
            yalign 0.65
    with pixellate

    show pers at right:
            zoom 0.4
            yalign 0.65
    with pixellate

    p"Boa tarde, Policial!"
    c"Boa tarde, desculpe incomodar, mas você conhece o supermercado aqui da esquina?"

    menu:

        "Sim, conheço.":
             p"Já fui lá algumas vezes."
        #    p"Cheio de coisas sem sentido, e olha essa fonte!"
        "Não conheço, mas já ouvi falar.":
            p"Minha vizinhança costuma frequentar esse luga.r"
        #    p"Preciso comprar esses medicamentos, assim estarei completamente seguro!"

    c"Então, acredito que o senhor já saiba dos boatos que estão rondando por aí, certo?"
    p"Sobre o que?"
    c"Boatos que dizem haver sequestradores na manufatura do supermercado, que agridem crianças e as fazem de escravas para a produção em massa e a lucratividade. Estamos atônitos e investindo forte nessa investigação."
    p"Que horror! Mas vocês já têm alguma prova?"
    c"Não há provas, mas toda vizinhança está preocupada e isso viralizou no HeyApp. Estamos informando a vizinhança para nos avisar sobre movimentações suspeitas, mas que não devem se desesperar."
    c"Precisamos de provas concretas antes de tudo! Temos apenas e-mails vagos que foram utilizados para basear a história das redes sociais."
    p"Pode deixar, irei informar o pessoal aqui de casa."


    #adicionar personagens e fundo novo
    scene black
    centered "Horas depois..." with dissolve
    stop music
    play music "audio/toctoc.wav"
    queue music "audio/cena2.mp3"
    centered "Toc Toc" with dissolve

    scene porta:
        zoom 1.5
    show pers at right with dissolve:
            zoom 0.4
            yalign 0.65

    show desconhecida at left with pixellate:
        zoom 0.4
        yalign 0.65

    p"Olá, tudo bem? Quem é você?"
    d"E aí, vi que os policias já te informaram sobre o que está acontecendo no supermercado. Veja cara, está tudo mundo falando sobre o e-mail que o auxiliar do prefeito mandou para o supermercado."
    d"Espera que vou compartilhar com você!"

    scene email

    $renpy.pause()

    scene porta:
        zoom 1.5
    show pers at right with dissolve:
            zoom 0.4
            yalign 0.65
    menu:
        "Para mim é um e-mail normal.":
            p"É apenas um e-mail como qualquer outro."
        "É apenas uma lista de compras.":
            p"É apenas uma lista com produtos pedidos."

    show desconhecida at left:
        zoom 0.4
        yalign 0.65
    d"Você está errado! Eu e mais pessoas do grupo em que participo vimos a mensagem secreta por trás desse e-mail. Ele está pedindo 50 crianças para escravidão!"
    p"Mensagem secreta!? Como assim?"
    d"Veja os produtos: Esfirra, Salsicha, Cenoura, Requeijão, Abobrinha, Vagem e Ovos. Agora pegue a inicial de cada uma delas."
    p"E-s-c-r-a-v-o?"
    d"Exato, tem algo de errado rolando lá!"
    p"Mas isso não poder ser apenas uma coincidência? E como vocês sabem se é um e-mail verídico? Acho que vocês estão se influenciando muito por boatos."
    d"Não estamos, não! Você verá hoje à noite. A justiça será feita!"

    #Fazer transição

    scene black
    centered "Ao anoitecer" with dissolve

    scene quartoNoite
    show pers at right with dissolve:
            zoom 0.4
            yalign 0.65
    #Inserir barulho de sirene
    play music "audio/sirene.wav"
    p"Nossa, que é esse barulho de sirene? Vou lá fora ver..."
    show pers at right with dissolve:
            zoom 0.4
            yalign 0.65
    #transição
    scene ruaPolicia
    show pers at right with dissolve:
            zoom 0.4
            yalign 0.65

    p"O que aconteceu, senhor Policial?"

    show policial at left:
            zoom 0.4
            yalign 0.65
    with pixellate

    c"Um pessoal, que estava sendo influenciado por boatos, invadiu o supermercado e chegou a agredir os funcionários para salvar as supostas crianças escravas."

    menu:
        "Então era tudo mentira mesmo?":
            c"Sim, era."
        "Não era verdade? Até você veio investigar.":
            c"Pois é, ainda nos fizeram perder tempo..."
    c"Tudo isso foi fruto de uma grande teoria da conspiração. Até o prefeito entrou no rolo e foi investigado, por causa desses boatos na Internet. Pessoas foram agredidas por nada, mas agora os autores da “investigação” foram presos."
    p"Eita, que loucura!"
    c"Para você ver como fake news e boatos podem fazer um grande estrago, tudo começou por causa de um e-mail, que nem era real. Agora pessoas foram machucadas e outras foram presas."
    c"Acreditar em tudo que está nas redes sociais pode ser problemático. É muito importante se informar através de jornais sérios, feito por profissionais."
    p"Pois é, o senhor tem razão."
    stop music
    #Transição ao acordar
#Cena 4
    scene black
    centered "7:OO AM"
    scene quarto

    show pers at right with dissolve:
            zoom 0.4
            yalign 0.65

    p"Acordei mais cedo do que precisava, vou verificar meu celular."

    scene not2:
        zoom 1
    $renpy.pause()

    scene quarto
    show pers at right with dissolve:
            zoom 0.4
            yalign 0.65

    menu:
        "Pesquisar a notícia.":
            "Eita, espera um pouco, essa fonte é muito estranha e não saiu nada em outros sites jornalísticos sobre isso, vou denunciar essa notícia"
            $compart = "0"

        "Não pesquisar a notícia.":
            "Mais pessoas precisam saber disso, pode ser a cura, vou compartilhar essa notícia no HeyApp e Facelook."
            $compart = "1"



#MiniJogo A
    scene black
    centered "Algumas horas depois..."

    play music "audio/toqueTelefone.ogg"
    $renpy.pause()
    stop music
    play music "audio/cena1.mp3"
    scene msgClara with dissolve
    $renpy.pause()
    scene quarto

    p"Que legal, vou lá! Estou com saudades."


    scene black
    centered "Chegando lá..." with dissolve
    scene cenaCafe

    show clara at left with pixellate:
        zoom 0.4
        yalign 0.65


    #O personagem recebe uma mensagem de sua melhor amiga de infância, Clara,
    #que estuda jornalismo em Portugal e está visitando sua cidade natal.

    cl"Oi, há quanto tempo! Tudo bem?"

    show pers at right with pixellate:
            zoom 0.4
            yalign 0.65

    p"Oi Clara, é mesmo!"
    p"Estou bem, e você como está?"
    cl"Estou bem também, andei vendo suas redes sociais esses dias."
    p"Eita, tinha algo ruim?"

    if compart == "1":
    #Caso tenha compartinhado noticía falsa na cena 4:
        cl"Preciso te falar uma coisa, fiquei meio decepcionada que você compartilhou fake news."
        p"Ah, nem prestei atenção. Achei que era verdade, ué."
        cl"Fala sério, achei que você era mais esperto, você não pesquisa as fontes antes de compartilhar?"
        p"Ah, nem..."
        cl"Você precisa levar isso mais a sério, você tem noção que fazem isso com fins políticos?"
        jump contMiniJogo
    else: #Caso não tenha compartilhado notícia falsa:
        cl"Ainda bem que você não compartilhou nenhuma fake news, meu Facelook está bizarro."
        p"Pois é, as pessoas acreditam em qualquer coisa ultimamente."
        cl"Sabe que atualmente muitas dessas notícias falsas possuem fins políticos né?"
        jump contMiniJogo

label contMiniJogo:
   p"O que você quer dizer?"
   cl"Notícias falsas sempre existiram na Internet, mas no início era só para coletar endereços de e-mails para propaganda ou para tentar golpes."
   cl"Há pessoas que se organizam para criar e espalhar notícias falsas. E eles ainda acusam os jornais tradicionais de fake news, é uma loucura."
   cl"Querem fazer a gente acreditar no que é interessante para eles, e também polarizar todo mundo."
   p"Polarizar?"
   cl"Aham. Para os políticos é interessante dividir a sociedade em grupos que se odeiam e não dialogam, assim é mais fácil manipular todo mundo."
   cl"Já percebeu como notícias falsas são sensacionalistas?"
   cl"Elas mexem com o emocional das pessoas."
   p"Sim, isso é algo que sempre me chamou a atenção!"
   cl"Vou te mostrar algumas notícias que estou usando no meu TCC."
   cl"Algumas são falsas, outras verdadeiras, quero ver se você consegue identificar quais são as verdadeiras."
   cl"Você pode pesquisar antes de responder, se quiser! Ah, você também pode usar o botão ‘Voltar’ quando precisar, ele fica na parte inferior da tela."
   p"Beleza, vamos lá!"

#Inicia-se um minijogo em que o personagem tem que avaliar uma série de notícias, com título e resumo, e descobrir quais são as falsas.
#Dependendo do resultado do jogo a resposta do personagem varia.
#Bom desempenho: Até que foi fácil, as notícias falsas realmente eram dramáticas.
#Baixo desempenho: Parece que não sei identificar muito bem...
stop music
play music "audio/game1.mp3"
scene mini11
$renpy.pause()

scene cenaminijogo

default points = 0
menu:
    "A Notícia A é a verdadeira":
        centered"Que pena, você errou!"
    "A Notícia B é a verdadeira":
        centered"Parabéns, você acertou!"
        $points = points + 1

centered "Próxima questão..."

scene mini12
$renpy.pause()
scene cenaminijogo
menu:
    "A Notícia C é a verdadeira":
        centered"Que pena, você errou!"
    "A Notícia D é a verdadeira":
        centered"Parabéns, você acertou!"
        $points = points + 1
scene black
centered "Último teste..."
scene mini13
$renpy.pause()
scene cenaminijogo
menu:
    "A Notícia E é a verdadeira":
        centered"Parabéns, você acertou!"
        $points = points + 1
    "A Notícia F é a verdadeira":
        centered"Que pena, você errou!"

scene cenaCafe

show clara at left with pixellate:
    zoom 0.4
    yalign 0.65

if points == 3:
    cl"Parabéns, você soube identificar todas as fake news!"
    jump fimcap1
elif points == 2:
    cl"Você soube identificar, porém precisa prestar mais atenção nas fontes das notícias!"
    jump fimcap1
else:
    cl"Poxa, estude um pouco mais sobre fake news e para saber como identificá-las."
    cl"Dica: sempre verifique as fontes!"
    jump fimcap1


label fimcap1:
    stop music
    play music "audio/cena3.mp3"
    show pers at right with pixellate:
            zoom 0.4
            yalign 0.65
    cl"Temos que ser muito críticos para identificar fake news."
    cl"A notícia falsa pode ser desde algo totalmente falso e inventado ou simplesmente algo verdadeiro, mas tirado de contexto."
    p"E tem um jeito mais fácil de saber o que é real ou não?"
    cl"Tem sim."
    cl"Além de jornais tradicionais serem mais seguros, existem jornalistas que trabalham com checagem de fatos e verificam as principais fake news compartilhadas."
    cl"Vou te passar os links."
    stop music

scene black
centered "Aos Fatos: www.aosfatos.org/ \n\n Fato ou fake: g1.globo.com/fato-ou-fake/" with dissolve
centered "Boatos.org: www.boatos.org/ \n\n Lupa: piaui.folha.uol.com.br/lupa/" with dissolve

centered "Fim Capítulo 1" with dissolve

centered "Referências Bibliográficas: \n\n GRINBERG, Nir et al. Fake news on Twitter during the 2016 US presidential election. Science, v. 363, n. 6425, p. 374-378, 2019. \n \n DA SILVA GOMES, Wilson; DOURADO, Tatiana. Fake news, um fenômeno de comunicação política entre jornalismo, política e democracia. Estudos em Jornalismo e Mídia, v. 16, n. 2, p. 33-45, 2019. \n \n VAN DER LINDEN, Sander; PANAGOPOULOS, Costas; ROOZENBEEK, Jon. You are fake news: political bias in perceptions of fake news. Media, Culture & Society, v. 42, n. 3, p. 460-470, 2020. \n \n FARHALL, Kate et al. Political elites' use of fake news discourse across communications platforms. International Journal of Communication, v. 13, p. 23, 2019."

centered "“As convicções são inimigas mais perigosas da verdade do que a mentira.“ - Friedrich Nietzsche"

label startCap2:
    scene black
    centered "Capítulo 2" with dissolve
    scene black
    centered "Se você encontrar um caminho sem obstáculos, ele provavelmente não leva a lugar nenhum. - Frank A. Clark"

    play music "audio/cena1.mp3"
    scene rua2

    show lucas at left with pixellate:
        zoom 0.4
        yalign 0.65
    l"Parabéns cara, muitas felicidades! Vamos ter algum rolê hoje?"

    show pers at right with pixellate:
        zoom 0.4
        yalign 0.65

    p"Muito obrigado, desejo tudo em dobro pra você!"
    p"Então, estava pensando aqui, quer vir em casa hoje?"
    p"Seria só nós mesmo. Como está tudo fechado, pedimos algo por delivery."
    l"Claro, eu adoraria. Mas como estamos em uma pandemia e estou trabalhando presencial, devo ir com máscara?"

    menu:
        "Cobrar medidas de segurança":
            p"Acho melhor, além disso seria interessante mantermos uma distância mínima entre a gente."
            p"Ah, traga também seu álcool em gel. Melhor fazer um rolê seguro, já que estamos fazendo certo em evitar aglomeração."
            l"Tem razão! Pode deixar, à noite estarei aí."
            l"Mal posso esperar."
            jump ccena1
        "Não cobrar medidas de segurança":
            #adicionar 10 pontos na variável.
            p"Ah, você que sabe, por mim está tudo bem, somos só nós dois mesmo, sem aglomeração. Pode chegar em casa à noite, sem problemas."
            l"Pode deixar, à noite estarei aí."
            p"Mal posso esperar."
            jump ccena1

label ccena1:
    scene black
    centered "Horas depois..." with dissolve

    scene sala:
        zoom 1.2

    show persMask at right with pixellate:
        zoom 0.4
        yalign 0.65
    #adicionar personagens
    p"E aí, beleza?"

    show lucasMask at left with pixellate:
        zoom 0.4
        yalign 0.65

    l"Tudo certo, que bom que me chamou, apesar do momento que vivemos!"
    p"Pois é, mas vamos sobrevivendo da melhor maneira possível."
    l"Podemos ficar mais tranquilos cara, vi na Internet que beber bastante água já elimina o vírus, sem contar que descobriram que prata coloidal é eficiente contra o coronavírus."
    menu:
        "Acho que é mentira, não vi notícia sobre isso!":
            jump ccena2
        "Pode crê, não sabia disso ainda!":
            jump ccena2

label ccena2:

    p"Mas acho melhor pesquisarmos em algum site confiável para termos certeza."
    l"É pra já! Pensando bem, há muitos mitos sobre a Covid-19 por aí. Por exemplo que o “Calor mata o vírus”, mas temperatura em 72 graus mata até a gente junto."
    l"Também tem das mais absurdas: comer alho ajuda prevenir a Covid-19, se fosse assim ninguém pegaria..."
    p"Nossa, é muita coisa louca, duro que tem pessoas que acreditam em tudo."
    l"Sempre que ouvirmos boatos ou desconfiarmos de algo, principalmente por notícias ou conversas não confiáveis, devemos investigar para sabermos o que é verdade e o que é falso."
    l"E essa dica serve para além da pandemia, serve para a nossa vida, mano. "

    scene black
    centered "Alguns momentos depois..." with dissolve

    scene sala:
        zoom 1.2

    show persMask at right with pixellate:
        zoom 0.4
        yalign 0.65

    show lucasMask at left with pixellate:
        zoom 0.4
        yalign 0.65
    l"Olha, foi muito bom te ver! Me diverti bastante! Pena que estamos em pandemia, nem deveríamos ter saído... Mas enfim, quando faremos o próximo rolê?"

    menu:
        "Vamos fazer o próximo rolê o mais rápido possível.":
        #mais 10 pontos
            jump ccena3
        "Agora só depois de melhorar essa pandemia, foi uma exceção de aniversário.":
            jump ccena3

label ccena3:
    p"OK! Vamos nos falando então. Valeu por hoje cara, até mais."
    #Cena 7: Personagem se sente acima do peso e decide buscar ajuda na Internet

    scene black
    centered "Alguns dias depois..." with dissolve

    scene sala:
        zoom 1.2
    show pers at right with pixellate:
        zoom 0.4
        yalign 0.65

    p"Bom dia Mãe, percebi que estou um pouco acima do peso..."

    show mae at left with pixellate:
        zoom 0.4
        yalign 0.65

    mae"Pois é, está mesmo! rsrs"
    p"Vou pesquisar sobre o que posso fazer."
    menu:
        "Pesquisar no site do Bem Estar.":
            p"Aqui diz que a melhor forma é buscar ajuda, porém já posso reduzir meus doces."
            mae"Excelente, marque uma nutricionista para você queimar essa gordurinha."
            $pesq = "0"
        "Perguntar em um grupo do Facelook.":
            p"Aqui diz que ao tomar esse shake nutritivo e cortar totalmente os carboidratos, eu já perco 7 kg em 1 semana, mãe!"
            mae"Isso está meio exagerado, é melhor você procurar um profissional."
            p"OK mãe, vou marcar."
            $pesq = "1"
    #Cena 8: Personagem vai na nutricionista buscando ajuda profissional
    #Adicionar personagens
    scene black
    centered "Poucos dias depois..." with dissolve
    #Muda cenário
    scene sala:
        zoom 1.2
    show pers at right with pixellate:
        zoom 0.4
        yalign 0.65

    p"Mãe, estou indo na nutricionista, até mais!"
    scene black
    centered "Chegando lá..." with dissolve
    #Muda cenário
    scene consultorio

    show nutri at left with pixellate:
        zoom 0.4
        yalign 0.65
    n"Boa tarde!"

    show persMask at right with pixellate:
        zoom 0.4
        yalign 0.65

    p"Olá, boa tarde!"
    n"O que te traz até aqui?"
    p"Olha, com essa pandemia não ando me exercitando e ainda por cima estou comendo mal."
    n"Te entendo, vamos dar um jeito nisso. Você fez alguma dieta própria ou algo relacionado?"

    if compart == "0":
        p"Olha, eu optei pela espera de uma ajuda profissional, porém reduzi os doces."
        n"Fez bem, eles são grandes vilões. E parabéns por buscar ajuda profissional, hoje em dia está difícil..."
        p"Ué, por quê?"
        jump nutri
    else:
        p"Até pensei em fazer, mas minha mãe achou melhor eu buscar ajuda profissional."
        n"Como assim?"
        p"Pesquisei na Internet e vi vários sites com shakes que emagrecem mais rapidamente sem fazer exercício."
        n"Não confie nesses sites, existem muitos vigaristas por aí nas redes sociais, hoje em dia está difícil..."
        p"Ué, por quê?"
        jump nutri

    label nutri:

    n"Não só em nossa área, mas muitas pessoas deixam de consultar profissionais preparados para seguir dietas de sites e influenciadores com fontes não confiáveis."
    n"E não é só isso, com as redes sociais, o número de compartilhamentos de notícias falsas aumentou."
    p"Nossa, por que será que acontece isso?"
    n"Eu andei lendo sobre isso, acontece que notícias falsas geram mais engajamento."
    n"Os algoritmos das redes sociais priorizam mostrar para seus usuários esse tipo de notícia. Já que, para a maioria, a verdade é considerada “entediante” ou difícil. Além disso, há muitas pessoas mal-intencionadas que fabricam conteúdo falso."
    p"Poxa, faz total sentido, ainda bem que vim com uma profissional, alguém com que posso contar."
    p"É realmente difícil saber o que é verdade quando não somos da área."

    n"Vamos lá, agora que está aqui, vou verificar sua taxa de gordura, passar uma dieta adequada e recomendar exercícios."

    p"Isso, estou precisando..."
    n"Na questão dos exercícios, faça na sua casa, seguro da Covid-19. Você até pode fazer em locais públicos abertos, mas não aconselho por enquanto, a taxa de transmissão ainda está muito alta."

    menu:
        "Fazer exercícios em local público.":
            p"Vou optar por fazer exercícios em locais públicos, mesmo você não recomendando, preciso sair de casa para me exercitar, apesar de correr risco."
            jump nutricont
            #somar mais 10 pontos
        "Fazer exercícios em casa.":
            p"Vou optar por fazer exercícios em casa, não quero me contagiar e passar para a minha família."
            p"Estarei me exercitando do mesmo jeito."
            jump nutricont
    label nutricont:
    n"Tudo bem."
    n"Aqui está tudo que você precisa, parabéns por optar por um profissional, espero que siga o que te passei e obtenha hábitos saudáveis. Nos vemos em breve!"
    #Imagem ação de personagem levantando.
    p"Obrigado, vou seguir sim, até mais!"
    stop music

# Cenário Minijogo B
scene black
centered "Uma semana depois..."
play music "audio/cena4.mp3"
scene sala:
    zoom 1.2

show mae at left with pixellate:
    zoom 0.4
    yalign 0.65

show pers at right with pixellate:
    zoom 0.4
    yalign 0.65


if compart == "0":
    mae"Nossa filho, não aguento mais, toda vez que abro o celular aparece apenas as mesmas notícias para mim"
    p"Pois é, depois que comecei a realizar exercícios, só aparecem notícias sobre isso para mim."
    mae"Parece que estão me espionando, você acha que estão invadindo nossa privacidade?"
    menu:
        "Acredito que sim.":
            p"Tudo que pesquiso ou vejo, aparece com mais frequência para mim."
            jump cenaIrmao
        "Não exatamente.":
            p"Há uma lei para evitar isso, mas eles podem usar dados que nós mesmos permitimos."
            jump cenaIrmao
else:
    p"Depois que cliquei em um site duvidoso, parece que há mais deles aparecendo, alguns até absurdos. Não sei o que está acontecendo."
    mae"O meu celular também é da mesma forma, toda vez aparecem notícias relacionadas ao que pesquisei antes. Deve ser alguma espionagem isso."
    mae"O que você acha, filho?"
    menu:
        "Acredito que é espionagem.":
            p"Tudo que pesquiso ou vejo, aparece com mais frequência para mim."
            jump cenaIrmao
        "Não é espionagem.":
            p"Há a lei LGPD, para justamente evitar isso."
            mae"Não consigo acreditar em lei nenhuma."
            jump cenaIrmao

label cenaIrmao:

    show irmao at center with pixellate:
        zoom 0.4
        yalign 0.65

    #Irmão mais velho aparece na cena e explica cada coisa:
    #Incluir irmão no meio da cena, só adicionar imagem dele.
    bro"Calma pessoal, não há espionagem, ou teorias da conspiração. Existe a LGPD, aqui no Brasil, que é a Lei Geral de Proteção de Dados Pessoais, em que cada empresa deve se enquadrar e respeitar."
    bro"No que se diz respeito a nossa privacidade, elas não podem vazar seus dados, ou utilizá-los para fins próprios."
    bro"Porém é permitido utilizar alguns dados de uso após nosso consentimento, antes de usar cada app ou página na Web. Além disso, redes sociais utilizam esses dados para os filtros bolha."
    mae"Nossa! Filtros o quê!? Nunca ouvi falar."
    bro"Filtros bolha, são códigos que coletam dados de uso de cada usuário e fazem com que você receba apenas o que é considerado relevante para você, como notícias, vídeos, informações… E isso é um perigo!"
    mae"Mas me parece tão bom ver apenas o que eu gosto no Facelook. Por que é um perigo?"
    bro"Porque você acaba obtendo apenas um lado de situações, principalmente na política."
    bro"Dessa forma, aumenta a polarização do país, pois, para o usuário, só sua visão é válida, devido a mente fechada que os filtros bolha reforçam."
    mae"Uau, que louco tudo isso meu filho."
    #Campainha toca (Inserir som de Campainha)
    #mudar cenario
    scene black with pixellate
    centered "Horas mais tarde..."

    scene sala:
        zoom 1.2

    show mae at left with pixellate:
        zoom 0.4
        yalign 0.65

    mae"Filho, seu amigo veio te ver."

    show pers at right with pixellate:
        zoom 0.4
        yalign 0.65
    p"Quem?"
    mae"O Alex, aquele menino que estuda Computação."
    p"Vou lá, saudades dele!"
    scene black
    centered "Chegando lá..." with dissolve

    scene porta:
        zoom 1.5
    show persmask at right with dissolve:
            zoom 0.4
            yalign 0.65
    show alex at left with pixellate:
        zoom 0.4
        yalign 0.65
    menu:
        "E aí mano, quanto tempo.":
            jump cirmao2
        "Salve cara, senti sua falta,":
            jump cirmao2
label cirmao2:

    a"Opa, saudades, resolvi dar uma passada aqui, pra gente conversar."
    p"Que bom que você veio, e aí gostou do jogo que te emprestei?"
    a"Nossa, é muito massa, já até zerei ele! Agora estou esperando lançar aquele novo jogo de corrida..."
    p"Eu também, vai ser muito legal."
    p"Essas semanas estava vendo no Facelook da Clara, ela está aproveitando demais Portugal, tirou várias fotos maneiras lá."
    a"Você não vai acreditar, vi ela esses dias aqui na cidade, ela já voltou, porém vai ficar só alguns dias."
    menu:
        "Será que a gente consegue dar um rolê?":
            jump cirmao3
        "Bora dar uma saída com ela.":
            jump cirmao3
label cirmao3:
    a"Então cara, Clara até queria sair com a gente, porém ela está ocupada com o TCC sobre fake news, que inclusive estou estudando também e dando uma força pra ela."
    p"Como assim? O que você está estudando?"
    a"É sobre como os algoritmos das redes sociais impulsionam notícias falsas e também como eles deixam as pessoas em “bolhas” que só reforçam a visão delas."
    p"Meu irmão falou um pouco sobre isso, mas como assim impulsionam notícias falsas?"
    a"Já ouviu falar do MIT? Uma das mais importantes universidades dos Estados Unidos?"
    a"Pesquisadores de lá descobriram que fake news se espalham 6 vezes mais rápido que notícias verdadeiras. E no caso de fake news sobre política, essas se espalham ainda mais rápido!"
    a"No Twister, por exemplo, eles perceberam que uma notícia falsa tem uma chance 70 porcentagem maior de ser compartilhada."
    p"Mas como assim? Por que isso acontece?!"
    a"Porque além de gerar mais engajamento, por serem sensacionalistas, essas notícias são espalhadas dentro da bolha das pessoas, o que aumenta a chance de compartilharem."
    a"Nas redes sociais a gente visualiza as postagens de pessoas que têm interesses em comum ou pensam igual a gente. É o que a gente chama de algoritmo 'filtro bolha'."
    menu:
        "É verdade, já notei que no Facelook não aparece tudo, sempre vejo posts das mesmas pessoas.":
            jump cirmao4
        "Sério? Não tinha reparado, vou prestar mais atenção nisso!":
            jump cirmao4
label cirmao4:
    a"Pois é mano, mas fica mais louco. Já ouviu falar do pessoal que acredita que a terra é plana?"
    a"Se você buscar sobre esse assunto no Youtubil ele vai te mostrar mais e mais vídeos sobre terraplanismo."
    a"Aí a pessoa fica presa em vídeos que confirmam a mesma visão e acaba não vendo os vídeos que explicam de forma científica que a terra é geoide."
    menu:
        "Quê?! Tem mesmo gente que acaba acreditando nisso?":
            jump cirmao5
        "Que triste, as pessoas precisam estudar mais.":
            jump cirmao5
label cirmao5:
    a"Pra piorar, gente mal-intencionada tem utilizado esse algoritmo para espalhar desinformação política."
    p"Tipo como?"
    a"Imagina por exemplo o cara que acredita na terra plana."
    a"Ele é visto como alguém que pode acreditar mais em teorias da conspiração e outras lorotas."
    a"Quanto mais você se envolve com notícias falsas, mais fica preso nesse ciclo."
    p"Temos de ficar mais espertos."
    a"Vou fazer um teste com você! Já que falamos sobre filtros-bolha, quero que reúna notícias parecidas nas diferentes bolhas!"
    a"Assim como ocorre nas mídias sociais e nem percebemos!"
    menu:
        "Vamos lá!":
            p"Vou dar o meu melhor!"
        "É pra já!":
            p"Vou dar o meu melhor!"

    #Aparece um minijogo sobre reunir imagens de notícias parecidas em diferentes bolhas. 

    scene cenaminijogo
    stop music
    play music "audio/game2.mp3"
    show screen drag_sample2
    hide screen drag_sample1A
    call screen drag_sample2
    show screen drag_sample3

    default acerto = 0
    if droppable == "Pró-vacina":
        $ xpos_var = 640
    else:
        $ xpos_var = 790
    if draggable == "noticia":
        show noticia:
            xpos xpos_var ypos 460

    hide screen drag_sample3
    centered "A [draggable] foi colocada como  [droppable]!"
    centered"Você tem certeza?"
    show not1_bolha:
        ypos 0.55
        xpos 0.35
    menu:
        "A notícia é Pró-vacina":
            $acerto = 0
        "A notícia é Antivacina":
            $acerto = 1

    hide not1_bolha
    centered "Vamos para a próxima escolha!"



    hide screen drag_sample1A
    call screen drag_sample4


    show screen drag_sample4


    if droppable == "Pró-vacina":
        $ xpos_var = 640
    else:
        $ xpos_var = 790
    if draggable == "noticia":
        show noticia:
            xpos xpos_var ypos 460

    hide screen drag_sample4

    centered "A [draggable] foi colocada como [droppable]!"
    centered"Você tem certeza?"

    show not2_bolha:
        ypos 0.55
        xpos 0.35
    menu:
        "A notícia é Pró-vacina":
            $acerto = acerto
        "A notícia é Antivacina":
            $acerto =  acerto + 1

    hide not2_bolha
    centered "Vamos para a outra escolha!"

    hide screen drag_sample1A
    call screen drag_sample5


    show screen drag_sample5


    if droppable == "Pró-vacina":
        $ xpos_var = 640
    else:
        $ xpos_var = 790
    if draggable == "noticia":
        show noticia:
            xpos xpos_var ypos 460

    hide screen drag_sample5

    centered "A [draggable] foi colocada como assunto da [droppable]!"
    centered"Você tem certeza?"

    show not3_bolha:
        ypos 0.55
        xpos 0.35
    menu:
        "A notícia é Pró-vacina":
            $acerto = acerto + 1
        "A notícia é Antivacina":
            $acerto =  acerto
    hide not3_bolha

#Starts here

    hide screen drag_sample1A
    call screen drag_sample6


    show screen drag_sample6


    if droppable == "Pró-vacina":
        $ xpos_var = 640
    else:
        $ xpos_var = 790
    if draggable == "noticia":
        show noticia:
            xpos xpos_var ypos 460

    hide screen drag_sample6

    centered "A [draggable] foi colocada como assunto da [droppable]!"
    centered"Você tem certeza?"

    show not4_bolha:
        ypos 0.55
        xpos 0.35
    menu:
        "A notícia é Pró-vacina":
            $acerto = acerto + 1
        "A notícia é Antivacina":
            $acerto =  acerto
    hide not4_bolha
    scene porta:
        zoom 1.5
    show persmask at right with dissolve:
            zoom 0.4
            yalign 0.65
    show alex at left with pixellate:
        zoom 0.4
        yalign 0.65

    if acerto <= 1:
        a"Poxa! Você não reuniu as notícias nos assuntos corretos!"
    elif acerto == 4:
        a"Parabéns! Você reuniu todas as notícias nos assuntos corretos!"
    else:
        a"Você precisa treinar mais, faltaram notícias para reunir corretamente!"

    p"Esse jogo foi interessante!"
    a"Pois é... E representa bem o que são os filtros bolha, a união de um mesmo tipo de conteúdo em nossos celulares."
    p"Valeu Alex, foi bom te ver,até mais!"
    a"Até, foi bom te ver!"
    stop music

    scene black
    centered "Fim capítulo 2" with dissolve

    centered "Referências Bibliográficas: \n\n O que é a Lei Geral de Proteção de Dados Pessoais?: https://www.serpro.gov.br/lgpd/menu/a-lgpd/o-que-muda-com-a-lgpd \n \n LGPD nas redes sociais - saiba o que muda: https://www.comunique-se.com.br/blog/lgpd-nas-redes-sociais/ \n \n Caçadores de mitos sobre COVID-19: https://www.paho.org/pt/cacadores-mitos-sobre-covid-19"

    centered "“As convicções são inimigas mais perigosas da verdade do que as mentiras.” - Friedrich Nietzsche" with pixellate
return

screen drag_sample1A:
    draggroup:
        drag:
            xpos 0.25
            ypos 0.45
            draggable False
            drag_raise False

            child "bolha_provacina.png"
            frame:
                xpadding 20
                ypadding 20


        drag:
            xpos 0.75
            ypos 0.45
            draggable False
            drag_raise False

            child "bolha_antivacina.png"
            frame:
                xpadding 20
                ypadding 20



screen drag_sample2:
    draggroup:
        drag:
            drag_name "notícia"
            child "not1_bolha.png"
            xpos 600
            ypos 100
            draggable True
            droppable False
            dragged drag_placed

        drag:
            drag_name "Pró-vacina"
            xpos 0.1
            ypos 0.6
            child "bolha_provacina.png"
            draggable False
            droppable True

        drag:
            drag_name "Antivacina"
            xpos 0.7
            ypos 0.6
            child "bolha_antivacina.png"
            draggable False
            droppable True


screen drag_sample3:
    draggroup:
        drag:
            drag_name "Pró-vacina"
            xpos 0.1
            ypos 0.6
            child "bolha_provacina.png"
            draggable False
            droppable False

        drag:
            drag_name "Antivacina"
            xpos 0.7
            ypos 0.6
            child "bolha_antivacina.png"
            draggable False
            droppable False

screen drag_sample4:
    draggroup:
        drag:
            drag_name "notícia"
            child "not2_bolha.png"
            xpos 600
            ypos 100
            draggable True
            droppable False
            dragged drag_placed

        drag:
            drag_name "Pró-vacina"
            xpos 0.1
            ypos 0.6
            child "bolha_provacina.png"
            draggable False
            droppable True

        drag:
            drag_name "Antivacina"
            xpos 0.7
            ypos 0.6
            child "bolha_antivacina.png"
            draggable False
            droppable True

screen drag_sample5:
    draggroup:
        drag:
            drag_name "notícia"
            child "not3_bolha.png"
            xpos 600
            ypos 100
            draggable True
            droppable False
            dragged drag_placed

        drag:
            drag_name "Pró-vacina"
            xpos 0.1
            ypos 0.6
            child "bolha_provacina.png"
            draggable False
            droppable True

        drag:
            drag_name "Antivacina"
            xpos 0.7
            ypos 0.6
            child "bolha_antivacina.png"
            draggable False
            droppable True

screen drag_sample6:
    draggroup:
        drag:
            drag_name "notícia"
            child "not4_bolha.png"
            xpos 600
            ypos 100
            draggable True
            droppable False
            dragged drag_placed

        drag:
            drag_name "Pró-vacina"
            xpos 0.1
            ypos 0.6
            child "bolha_provacina.png"
            draggable False
            droppable True

        drag:
            drag_name "Antivacina"
            xpos 0.7
            ypos 0.6
            child "bolha_antivacina.png"
            draggable False
            droppable True
