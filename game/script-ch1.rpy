label ch1_main:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    play music t6   
    scene bg bedroom
    with open_eyes
    pause 0.5
    "J’étais épuisé par cette journée, ranger correctement tous nos livres et poèmes de l’année m’avais pris un temps fou."
    play sound "bgm/vibreur.ogg "
    pause 1.25 
    "Tient, un message de Natsuki."
    n "{size=-4}Salut ! Demain je vais faire des cupcakes, je te préviens d’avance, ce sera les meilleurs de toute ta vie ! Demain ont se réunit  toutes  chez Monika, le club de littérature va continuer même en été ! Mais il y a mon père chez moi et je ne pense pas réussir toute seule étant donné qu’il me manque des ingrédients.{/size}" 
    menu: 
        "Je l'aide ?"
        "Oui":
            $ n_appeal = 1
            mc "Je vais t’aider, ne t’inquiète pas il doit sûrement me rester des ingrédients depuis notre dernière fournaison, vient demain chez moi dans la matinée."
            n "Oki ! Ta intérêt à ne pas déclencher l’alarme incendie cette fois !"
            "Natsuki et moi avons continué à parler toute la nuit jusqu'à ce qu'elle s'endorme devant son téléphone, je fis de même juste après, j'avais hâte d'être demain."
            jump ch1_next
        "Non":
            menu:
                "Être agressif ?"
                "Oui":
                    $ n_appeal = n_appeal - 2
                    mc "Je suis juste fatigué, nous sommes en vacances et tu sais bien que ça aurait été un plaisir de t’aider mais je ne peux pas."
                    n "Moi aussi je suis fatiguée ! mais je fais quand même des efforts pour mes amies, tempi, a demain soir au club."
                "Non":
                    $ n_appeal = n_appeal - 1
                    mc "Demande à Sayori, je ne suis pas libre demain, enfin, pas avant l'après-midi et ce sera un peu tard pour commencer l"
                    n "Dit surtout que tu n’as pas envie de faire des cupcakes !"
                    "Mais non, tu sais bien que j’adore tes cupcakes et t’aider, mais malheureusement ce n’est pas possible demain."
            "Natsuki et moi n'avons pas continué à parler, elle à cesser de me répondre juste après, je m'endormis de suite, j'étais trop fatiguée pour répondre."
            jump ch1_next

label ch1_next:
    if n_appeal == 1:
        stop music fadeout 1.75
        play sound "bgm/interrupteur.ogg"
        scene bg bedroom_night
        pause 0.75
        scene black
        with close_eyes
        pause 1.0
        scene bg bedroom_night
        with open_eyes
        play music t6
        pause 1.0
        play sound "bgm/sonette.ogg"   
        pause 1.0
        "Qui ça peut être à cette heure-ci !?"
        play sound "bgm/interrupteur.ogg"
        scene bg bedroom
        pause 1.0
        scene bg mc_indoor_dusk_house
        with dissolve_scene
        "Ah, je viens de me rappeler. Ça doit être surement Natsuki, j'avais complétement oublié qu'elle devait venir."
        pause 0.5
        scene bg house
        with dissolve_scene
        show natsuki 5bd zorder 2 at t11
        mc "Oui ?"
        n "Ah bah enfin je croyais que...{nw}"
        show natsuki 5b2c at hf11
        n "[Player] !"
        n "Tu ... tu aurais pu au moins te changer."
        show natsuki 5b2c at t11
        mc "Désolé, mais je m'attendais pas à te voir aussi tôt."
        "Je sourie à Natsuki mais en réalité je suis un peu gêné moi aussi"
        show natsuki 2bj at f11
        n "Bref, ce n'est pas grave,"
        n 2by "la reine de la pâtisserie vient d'arriver"
        show natsuki 2by at t11
        mc "D'accord, dans ce cas si sa majesté me le permet je vais rentrer me changer pour cuisiner."
        show natsuki 2bj at t11 
        n "Je te suis."
        scene bg kitchen
        show natsuki 1bj at t11 
        with wipeleft
        mc "Attend moi juste 30 secondes le temps que je me change."
        n "Oki"
        return
    else:
        return
        show natsuki 4by at t11
        n "Tu en met du temps pour t'habiller."
        mc "Je cherchais des habilles que je peux sâlire"
        show natsuki 4ba at t11
        n "En effet c'est mieux pour cuisiner."
        mc "Bref, on fait les cupcakes habituels ?"
        show natsuki 1by at t11
        n "Ce ne sont pas des cupcakes habituels, ce sont mes cupcakes."
        "Elle bafouille"
        n 5bs "Je dirais même nos cupcakes."
        show natsuki 5bs at t11
        mc "Qu'est-ce que tu as dis ?"
        show natsuki 1bw at t11
        n "Rien, je disais qu'il fallait allumer le fourre."
        "Je sais très bien ce qu'elle a dit et ça me fait plaisir de l'entendre"
        mc "D'accord je le fais !"
        show natsuki 5bd at t11
        n "Comment veux-tu les décorer ?"
        mc "Eh si on faisait comme ceux que tu avais fait le jour de notre rencontre, des cupcakes chats, comme ça, vue que l’année scolaire est terminée on va recréer le tout premier souvenir qu’on a eu tous ensemble."
        show natsuki 5bs at t11
        "Roh..."
        mc "Qu’est ce qu’il y a? ce n’est pas une bonne idée?"
        show natsuki 5bs at t11
        n "Si justement, c’est énervant quand tu as des bonnes idées."
        n 5bx "Je ne peux pas te corriger..."
        show natsuki 5bx at t11
        mc "Je sais, tu me le dis souvent, ça en devient amusant."
        "Elle me donne un coup dans l'épaule avec le sourire"
        show natsuki 4bz at t11
        n "Tu te moque de moi en plus ! "
        mc "J’ai bien le droit de me moquer un peu, tu le fais bien toi."
        show natsuki 5bs at t11
        "Elle chuchotte"
        n "Oui mais c'est parceque je tiens a toi."
        mc "Qu'est-ce que tu dis tout bas ?"
        show natsuki 5bq at t11
        show natsuki 1bp at t11
        show natsuki 1bv at t11
        n "Rien ! Rien ! Je... Je, rien ! "
        "Je rigole un peu pour me moquer."
        mc "Bon, la reine des cupcakes compte venir m’aider ? On a du travail."
        show natsuki 4by at t11
        n "La reine n'aide pas le bouffon."
        "Je réplique en mettant du glaçage sur son nez pour plaisanter."
        mc "Voilà ce qui te fait le bouffon."
        show natsuki glaçage2 at t11
        n "mais ! "
        "Elle essuie son nez et esssaye de remettre le glaçage sur mon nez. J'esquive en tournant la tête mais reçois le glaçage sur la joue."
        mc "je ne suis  pas un cupcake tu sais."
        show natsuki 4by at t11
        n "Je sais, tu ne serai pas très appétissant si c’était le cas."
        mc "Et toi alors, tu penses avoir un bon goût."
        show natsuki 4bz at t11
        n "Bien sûr que oui ! Je suis une sucrerie."
        mc "Eh bah heureusement que la modestie ne tue pas, tu serais déjà six pieds sous terres."
        show natsuki 4bz at t11 
        n "Je dis la vérité."
        mc "mouais, on va dire ça"
        mc "Bon il reste un peu plus d'une heure avant d'aller chez Monika, une idée sur ce qu'on peut faire ?"
        show natsuki 5ba at t11
        n "On peut aller se promener si tu veux, tu préfères en ville ou au parc ?"
        
























