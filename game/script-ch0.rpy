label ch0_main:
    stop music fadeout 2.0
    scene bg club_sunset
    with dissolve_scene_full
    play music t9g
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ y_name = "Yuri"
    $ n_name = "Natsuki"

    python:
        try: 
            renpy.file("../characters/yuri.chr")
        except: 
            try: 
                renpy.file("./characters/monika.chr") 
            except: 
                try: 
                    renpy.file("../characters/natuski.chr")
                except: 
                    try: 
                        renpy.file("../characters/sayori.chr")
                    except: renpy.jump("ch0_badtime")

    $ restore_all_characters()
    $ state = "Act 1"
    $ details = "Premier jour"

    "C’était la fin de journée, comme habituellement nous nous retrouvions ici, mais, pas ce soir."
    "Nous étions le dernier soir du lycée, demain, je ne serai plus là."
    "Les vacances d’été venaient de débuter, et comme une page d’un livre voici que j’en commencez une nouvelle, un nouveau chapitre, mais un chapitre sans le club."
    "{size=-3}J’avais finalement pris goût à ce club, même si au départ j’étais réticent, je dois avouer que les cupcakes de Natsuki vont me manquer, la bonne humeur de  Sayori, la présence de Yuri et la voix de Monika, dans un sens elles vont toutes me manquer.{/size}"
    "Bon je pense qu'il est temps pour moi de rentrer"
    scene bg corridor_sunset
    with dissolve_scene
    "Combien de fois suis-je passer par là pour me rendre au club ou pour traîner juste avec elles, et c'est la dernière fois que je l'empreinte avant la rentrée prochaine."
    scene bg residential_sunset
    with dissolve_scene
    pause 1.5
    "A vrai dire, j’avais rêvé du club par un instant, un rêve étrange mais pourtant"
    $ style.say_dialogue = style.edited
    "si réel."
    $ style.say_dialogue = style.normal
    stop music fadeout 1.0
    scene black
    with close_eyes
    $ saturation = 0.0
    pause 1.5
    show mask_2b
    show mask_3b
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bgb
    show monika_bg_highlightb
    play music t10y2
    pause 2.5
    scene bg sayori_bedroomb 
    with wipeleft_scene
    show s_kill_bg2b
    show s_kill2b
    show s_kill_bgb as s_kill_bgb at s_kill_bg_start
    show s_killb as s_killb at s_kill_start
    pause 2.5
    scene bg club_dayb
    with wipeleft_scene
    show yuri 3db at i11
    pause 1.43
    show yuri stab_1b
    pause 0.75
    show yuri stab_2b
    show bloodb:
        pos (610,485)
    pause 1.25
    show yuri stab_3b
    pause 0.75
    show yuri stab_2b
    show bloodb:
        pos (610,485)
    show yuri stab_4b with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    pause 1.25
    show yuri stab_5b
    pause 0.70
    show yuri stab_6b:
        2.55
        easeout_cubic 0.5 yoffset 300
    show bloodb as blood2:
        pos (635,335)
    pause 2.55
    hide bloodb
    hide blood2
    pause 0.25
    play sound fall
    pause 0.25
    scene black
    pause 1.5
    scene bg club_dayb
    with wipeleft_scene
    show natsuki ghost2b zorder 2 at t11
    show darkredb zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    show natsuki_ghost_bloodb zorder 3
    hide n_rects_ghost3
    pause 1
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_bloodb
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3b
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4b onlayer front at i11
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    pause 0.5
    "Mais, au final ce cauchemar n'était pas réel."
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t3
    show sayori 4p zorder 2 at t11
    s "J'ai encore trop dormis... Tu aurais pus m'attendre "
    "Sayori, comme d'habitude arrivait en retard."
    scene bg club_day
    with wipeleft_scene 
    show sayori 1q zorder 2 at t41
    show natsuki 4t zorder 2 at t42
    show yuri 2c zorder 2 at t43
    show monika 1a zorder 2 at t44
    "J'ai rencontré les filles comme dans mon rêve, parfois le hasard qu'est l'imaginaire fait bien les choses"
    scene bg corridor_festival
    with wipeleft_scene
    show sayori 1ba zorder 2 at h41
    show natsuki 3bz zorder 2 at h42 
    show yuri 3bc zorder 2 at h43
    show monika 1ba zorder 2 at h44
    "{size=-5}J'ai tout de même passé une très bonne année avec elles, parfois Yuri et Natsuki se disputait, parfois il y avait des tensions entres elles indirectement par ma faute mais Sayori était toujours là pour renouer les liens de leur amitiée, maintenant que l'été est arrivé je n'ai qu'une question en tête, vais-je les revoirs toutes ensemble ?{/size}"
    jump ch1_main

label ch0_badtime:
    show monika 1a zorder 2 at t11
    m "..."
    m "Pas mal"
    $ restore_all_characters()
    $ renpy.quit()
    return

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
