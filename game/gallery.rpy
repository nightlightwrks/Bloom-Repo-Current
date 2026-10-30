## Gallery screen ################################################################
##
## image rescale as thumbnail
## This screen view cg
init python:
    g = Gallery()

    #only edit g.image and cg_thumbnail when cgs is ready


    #albion cg
    g.button("albion1")
    g.condition("persistent.albion1")
    g.image("images/AlbionCG1.webp")

    g.button("albion2")
    g.condition("persistent.albion2")
    g.image("cg_test")

    #felix cg
    g.button("felix1")
    g.condition("persistent.felix1")
    g.image("images/FelixCG0.webp")
    g.image("images/FelixCG1.webp")

    g.button("felix2")
    g.condition("persistent.felix2")
    g.image("images/FelixCG2.webp")
    g.image("images/FelixCG3.webp")
   
    #qwynn cg
    g.button("qwynn1")
    g.condition("persistent.qwynn1")
    g.image("images/QwynnCG0.webp")
    g.image("images/QwynnCG1.webp")

    g.button("qwynn2")
    g.condition("persistent.qwynn2")
    g.image("images/QwynnCG2.webp")

    #caelan cg
    g.button("caelan1")
    g.condition("persistent.caelan1")
    #g.image("images/CaelanCG0.webp")
    #g.image("images/CaelanCG1.webp")

    g.button("caelan2")
    g.condition("persistent.caelan2")
    g.image("cg_test")

    THUMBNAIL_SIZE = (602, 338) 

image albion_cg1_thumbnail = Transform("images/AlbionCG1.webp", xysize=THUMBNAIL_SIZE)
image felix_cg0_thumbnail = Transform("images/FelixCG0.webp", xysize=THUMBNAIL_SIZE)
image felix_cg2_thumbnail = Transform("images/FelixCG2.webp", xysize=THUMBNAIL_SIZE)
image qwynn_cg0_thumbnail = Transform("images/QwynnCG0.webp", xysize=THUMBNAIL_SIZE)
image qwynn_cg1_thumbnail = Transform("images/QwynnCG1.webp", xysize=THUMBNAIL_SIZE)
image qwynn_cg2_thumbnail = Transform("images/QwynnCG2.webp", xysize=THUMBNAIL_SIZE)
image cg_thumbnail_test = Transform("images/cg_test.webp", xysize=THUMBNAIL_SIZE)
image albion_locked_cg = Transform("gui/gallery/albion_locked.webp", xysize=THUMBNAIL_SIZE)
image felix_locked_cg = Transform("gui/gallery/felix_locked.webp", xysize=THUMBNAIL_SIZE)
image qwynn_locked_cg = Transform("gui/gallery/qwynn_locked.webp", xysize=THUMBNAIL_SIZE)
image caelan_locked_cg = Transform("gui/gallery/caelan_locked.webp", xysize=THUMBNAIL_SIZE)

transform ts_galSpriteAppear():
    zoom 1.3
    xoffset -100
    linear 0.2 xoffset 0


screen gallery():
    style_prefix "g"

    tag menu
    default char = "albion"

    add "gui/game_menu.webp"
    add "gui/gallery/gal_title.webp" pos (1040, 40)


    ## SPRITE ##


    if char == "albion":
        add "images/Albion_N.webp":
            xpos 80
            at ts_galSpriteAppear()
        textbutton "Coming Soon":
            xpos 1660
            ypos 750
            
    if char == "felix":
        add "images/Felix_N.webp":
            xpos 80
            at ts_galSpriteAppear()

    if char == "qwynn":
        add "images/Qwynn_Smile.webp":
            xpos 80
            at ts_galSpriteAppear()

    if char == "caelan":
        add "images/Caelan_S2.webp":
            xpos 80
            at ts_galSpriteAppear()
        textbutton "Coming Soon":
            xpos 1660
            ypos 750
        textbutton "Coming Soon":
            xpos 1660
            ypos 400
           

    vbox:
        pos (1035, 190)
        xsize 660
        spacing 20
        

        hbox:
            #xalign 0.5
            xfill True
            if (persistent.caelanname == True):
                    xpos -35
            else:
                    xpos -25
            button:
                text _("ALBION")
                action SetScreenVariable("char","albion")
            button:
                text _("FELIX")
                action SetScreenVariable("char","felix")
            button:
                text _("QWYNN")
                action SetScreenVariable("char","qwynn")

            if (persistent.caelanname == True):
                button:
                    text _("CAELAN")
                    action SetScreenVariable("char","caelan")
            else:
                button:
                    text _("CAL")
                    action SetScreenVariable("char","caelan")
        
        if char == "felix":
            use felix
        elif char == "albion":
            use albion
        elif char == "qwynn":
            use qwynn
        elif char == "caelan":
            use caelan

    ## RETURN ##
    imagebutton:
        idle "images/return_idle.webp"
        hover "images/return_hover.webp"
        activate_sound "audio/sfx_click.ogg"
        pos (1546, 940)
        action Return()


style g_button is default:
    xysize (168, 50)
    background None
    hover_background "#E297B2"
    selected_background "#DEC9BC"
    selected_hover_background "#E297B2"
    idle_color "#844138"   

style g_text:
    align (0.5, 0.5)


#2 CGs per character
screen felix():

    grid 1 2:
        add g.make_button(name="felix1", unlocked="felix_cg0_thumbnail", locked="felix_locked_cg")

        add g.make_button(name="felix2", unlocked="felix_cg2_thumbnail", locked="felix_locked_cg")

        spacing 10


screen albion():

    grid 1 2:
        add g.make_button(name="albion1", unlocked="albion_cg1_thumbnail", locked="albion_locked_cg")

        add g.make_button(name="albion2", unlocked="cg_thumbnail_test", locked="albion_locked_cg")

        spacing 10


screen qwynn():
    grid 1 2:
        add g.make_button(name="qwynn1", unlocked="qwynn_cg0_thumbnail", locked="qwynn_locked_cg")

        add g.make_button(name="qwynn2", unlocked="qwynn_cg2_thumbnail", locked="qwynn_locked_cg")

        spacing 10

screen caelan():
    grid 1 2:
        add g.make_button(name="caelan1", unlocked="qwynn_cg0_thumbnail", locked="caelan_locked_cg")

        add g.make_button(name="caelan2", unlocked="cg_thumbnail_test", locked="caelan_locked_cg")

        spacing 10