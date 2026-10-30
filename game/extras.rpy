### PAUSE MENU SCREEN ############################################################
##
##

############################################################
## PYTHON ##
############################################################
init python:
    _game_menu_screen = "extra"


############################################################
## PAUSE SCREEN ##
############################################################
screen extra():

    tag menu

    add "gui/overlay/afterstories.webp"
    
    hbox:
            style_prefix "extra"
            xysize (890, 580)
            xalign 0.5

            textbutton _("ALBION") action Start("albion_after"):
                activate_sound "audio/sfx_click.ogg"
                xpos -90
                ypos 830
            textbutton _("FELIX") action Start("felix_after"):
                activate_sound "audio/sfx_click.ogg"
                xpos -30
                ypos 830           
            textbutton _("QWYNN") action Start("qwynn_after"):
                activate_sound "audio/sfx_click.ogg"
                xpos 28
                ypos 830 
            if (persistent.caelanname == True):
                textbutton _("CAELAN") action Start("caelan_after"):
                    activate_sound "audio/sfx_click.ogg"    
                    xpos 92
                    ypos 830
            else:
                textbutton _("CAL") action Start("caelan_after"):
                    activate_sound "audio/sfx_click.ogg"    
                    xpos 92
                    ypos 830
        
    ## RETURN ##
    imagebutton:
            idle "images/return_idle.webp"
            hover "images/return_hover.webp"
            activate_sound "audio/sfx_click.ogg"
            pos (1546, 940)
            action Return()
   
style extra_button:
    size_group "extra"
    #properties gui.button_properties("navigation_button")
    #xoffset 570
    #yoffset -250
    background "gui/button/title_bg.webp"
    xysize (400, 50)
    #xalign 1.0
    idle_color "#6a4e3d"     
    hover_color '#e297b2'

style extra_button_text:
    properties gui.button_text_properties("extra")
    idle_color "#844138"     
    hover_color '#e297b2'
    xalign 0.5
    xoffset 0
    yoffset 22


   