### PAUSE MENU SCREEN ############################################################
##
##

############################################################
## PYTHON ##
############################################################
init python:
    _game_menu_screen = "pause_menu"


############################################################
## PAUSE SCREEN ##
############################################################
screen pause_menu:
    style_prefix "pm"
    modal True
    add "gui/overlay/menu_overlay.webp"

    fixed:
        at ts_screenfadein()

        add "gui/menubg/pause_background.webp" align (0.5, 0.5)

        add "gui/history_line_divider.webp" xalign 0.5 ypos 232

        vbox:
            xysize (890, 580)
            xalign 0.5
            xoffset -31
            ypos 265

            button:
                text _("LOG")
                action ShowMenu("history")

            button:
                text _("GLOSSARY")
                action ShowMenu("glossary")

            button:
                text _("SAVE")
                action ShowMenu("save")

            button:
                text _("LOAD")
                action ShowMenu("load")

            #button:
                #text _("GALLERY")
                #action ShowMenu("gallery")

            button:
                text _("SETTINGS")
                action ShowMenu("preferences")

            button:
                text _("ABOUT")
                action ShowMenu("about")

            button:
                text _("HELP")
                action ShowMenu("help")

            button:
                text _("TITLE")
                action MainMenu()


        ## RETURN ##
        imagebutton:
            idle "images/return_idle.webp"
            hover "images/return_hover.webp"
            activate_sound "audio/sfx_click.ogg"
            pos (1135, 920)
            action Return()

style pm_button:
    #is gloss_page_button
    is pm_button
    xalign 0.5

style pm_text:
    is pm_text
    align (0.5, 0.5)

style pm_button is default:
    xysize (300, 50)
    xoffset 30
    background None
    hover_background "#E297B2"
    selected_background "#DEC9BC"
    selected_hover_background "#E297B2"

style pm_text is default:
    xalign 0.5
    yalign 0.5

