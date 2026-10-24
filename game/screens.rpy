################################################################################
## Initialization
################################################################################

init offset = -1



################################################################################
## Custom Cursor
################################################################################

define config.mouse = {"default":[ ("gui/cursor.png", 1, 1) ] }


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")
    idle_color "#5f3e2a"     
    hover_color '#e297b2'


style button:
    properties gui.button_properties("button")
    activate_sound "audio/sfx_click.ogg"

style button_text is gui_text:
    properties gui.text_properties("button")
    idle_color "#5f3e2a"     
    hover_color '#e297b2'
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/bar_empty.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bar_full.png", gui.vbar_borders, tile=gui.bar_tile)

#if route = 'albion':
    #thumb "gui/bar/_thumb.png"

#TODO#

style scrollbar:
    ysize 40
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    thumb_offset -20
    unscrollable "hide"
    left_gutter 15
    right_gutter 15

style vscrollbar:
    xsize 40
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
    thumb_offset -20
    unscrollable "hide"
    top_gutter 15
    bottom_gutter 15

style slider:
    ysize 40
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    thumb_offset -20
    left_gutter 15
    right_gutter 15

style vslider:
    xsize 40
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
    thumb_offset -20
    top_gutter 15
    bottom_gutter 15


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say


screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage(): 
            xalign 0.0 
            yalign 1.0
            xoffset -20
            #yoffset 55
    

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos 130
    xanchor gui.name_xalign
    xsize 450
    ypos -85
    ysize 100

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.5
    yalign 0.0
    yoffset 20


style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize 1150
    ypos 55


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
           
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            xoffset 0
            yalign 1.0
            yoffset -16

            #BACK BUTTON
            #textbutton _("BACK") action Rollback()
            textbutton _("LOG") action ShowMenu('history'):
                activate_sound "audio/sfx_click.ogg"
            textbutton _("GLOSSARY") action ShowMenu("glossary"):
                activate_sound "audio/sfx_click.ogg"
            textbutton _("SKIP") action Skip() alternate Skip(fast=True, confirm=True):
                activate_sound "audio/sfx_click.ogg"
            textbutton _("AUTO") action Preference("auto-forward", "toggle"):
                activate_sound "audio/sfx_click.ogg"
            textbutton _("SAVE") action ShowMenu('save'):
                activate_sound "audio/sfx_click.ogg"
            textbutton _("LOAD") action ShowMenu('load'):
                activate_sound "audio/sfx_click.ogg"
            textbutton _("SETTINGS") action ShowMenu('preferences'):
                activate_sound "audio/sfx_click.ogg"
            textbutton _("HELP") action ShowMenu("help"):
                activate_sound "audio/sfx_click.ogg"
            textbutton _("TITLE") action MainMenu():
                activate_sound "audio/sfx_click.ogg"
            if persistent.status_button:
                textbutton _("STATUS") sensitive route is not None action ShowMenu('relationship_pts'):
                    activate_sound "audio/sfx_click.ogg"


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    idle_color "#5f3e2a"     
    hover_color '#e297b2'
    selected_color '#e297b2'



################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    if renpy.get_screen("main_menu"):
        vbox:
            style_prefix "navigation"

            xalign 0.0
            yalign 0.0
            yoffset 310
            xoffset 20      
                      

            spacing gui.navigation_spacing

            if main_menu:

                textbutton _("START") action Start()
                    #xpos 735
                    #ypos 830
                textbutton _("LOAD") action ShowMenu("load")
                            
                textbutton _("GALLERY") action ShowMenu("gallery")
                    #xpos 88
                    #ypos 880

                textbutton _("AFTER STORIES") action ShowMenu("extra")            

            else:

                textbutton _("HISTORY") action ShowMenu("history")

                textbutton _("SAVE") action ShowMenu("save")

            #textbutton _("LOAD") action ShowMenu("load")
                #xpos 245
                #ypos 930

            textbutton _("SETTINGS") action ShowMenu("preferences")

            if _in_replay:

                textbutton _("END REPLAY") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("MAIN MENU") action MainMenu()

            textbutton _("ABOUT") action ShowMenu("about")
                #xpos 450
                #ypos 930

            #textbutton _("GLOSSARY") action ShowMenu("glossary")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("HELP") action ShowMenu("help")

            if renpy.variant("pc"):

                ## The quit button is banned on iOS and unnecessary on Android and
                ## Web.
                textbutton _("QUIT") action Quit(confirm=not main_menu)
    #else:
            #hbox:
                #style_prefix "gamemenu"

                #xalign 0.5
                #yalign 0.0
                #yoffset 195
                #xoffset 110
                #spacing 10
                                           
                #spacing gui.navigation_spacing

                #if main_menu:

                #   textbutton _("START") action Start()

                #else:                 

                    #textbutton _("HISTORY") action ShowMenu("history")

                    #textbutton _("SAVE") action ShowMenu("save")

                #textbutton _("LOAD") action ShowMenu("load")

                #textbutton _("OPTIONS") action ShowMenu("preferences")

                #if _in_replay:

                    #textbutton _("END REPLAY") action EndReplay(confirm=True)

                #elif not main_menu:

                    #textbutton _("TITLE") action MainMenu()

                    #textbutton _("GLOSSARY") action ShowMenu("glossary")
            
            #hbox:
                #style_prefix "gamemenu"

                #xalign 0.5
                #yalign 0.0
                #yoffset 240
                #xoffset 340
                #spacing 10      

                #if main_menu:
                    
                    #textbutton _("GALLERY") action ShowMenu("gallery")

                    #textbutton _("ABOUT") action ShowMenu("about")
                       
                #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                    ## Help isn't necessary or relevant to mobile devices.
                    #textbutton _("HELP") action ShowMenu("help")

                #if renpy.variant("pc"):

                    ## The quit button is banned on iOS and unnecessary on Android and
                    ## Web.
                    #textbutton _("QUIT") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text
style gamemenu_button is navigation_button
style gamemenu_button_text is navigation_button_text

style navigation_button:
    size_group "navigation"
    #properties gui.button_properties("navigation_button")
    #xoffset 570
    #yoffset -250
    background "gui/button/title_bg.png"
    xysize (400, 50)
    #xalign 1.0
    idle_color "#6a4e3d"     
    hover_color '#e297b2'

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    idle_color "#844138"     
    hover_color '#e297b2'
    xalign 0.5
    xoffset 5
    yoffset 22

style gamemenu_button_text:
    xalign 0.0
    xspacing 5
 


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"
            pos (1000, 500)

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20


style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    color "#fff"
    yalign .995
    size 18
    kerning -1
    xoffset 290

style main_menu_version:
    variant "small"
    xoffset 365


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

 

    if main_menu:
        add "gui/bg1.png"
    if renpy.get_screen("about"):
        add "gui/overlay/menu_overlay.png"
        add "gui/menubg/about_background.png" at truecenter
    elif renpy.get_screen ("extra"):
        add "gui/overlay/menu_overlay.png"
        add "gui/menubg/afterstories.png" at truecenter
    elif renpy.get_screen("load"):
        add "gui/overlay/menu_overlay.png"
        add "gui/menubg/load_background.png" at truecenter
    elif renpy.get_screen("save"):
        add "gui/overlay/menu_overlay.png"
        add "gui/menubg/save_background.png" at truecenter
    elif renpy.get_screen("help"):
        add "gui/overlay/menu_overlay.png"
        add "gui/menubg/help_background.png" at truecenter
    elif renpy.get_screen ("preferences"):
        add "gui/overlay/menu_overlay.png"
        add "gui/menubg/settings_background.png" at truecenter
        #textbutton _("HELP") action ShowMenu("help"):
            #pos (902,220)
        # add "gui/menubg/settings_background.png" at truecenter
    elif renpy.get_screen ("history"):
        add "gui/overlay/menu_overlay.png"
        add "gui/menubg/log_background.png" at truecenter
    elif renpy.get_screen ("glossary"):
        add "gui/overlay/menu_overlay.png"
        add "gui/menubg/glossary_background.png" at truecenter

           
    else:
        add gui.game_menu_background


    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation



    imagebutton:
        idle "images/return_idle.png"
        hover "images/return_hover.png"
        activate_sound "audio/sfx_click.ogg"
        xalign 0.0
        yalign 1.0
        yoffset -45
        xoffset 1130
        action Return()

    
    
    
    #label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")



style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    
    #background "gui/main_menubg.png"


style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 10
    right_margin 450
    top_margin 70


style game_menu_viewport:
    xysize (1000,670)

style game_menu_vscrollbar:
    xoffset -50
    ysize 670
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xalign 0.5
    yalign 0.0
    yoffset 60
    xoffset 160
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color

#style return_button:
    #xalign 0.0
    #yalign 1.0
    #yoffset -40
    #xoffset 1200


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.


screen about():



    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("ABOUT"), scroll="viewport"):
 
        style_prefix "about"
        #add "gui/menu bg/about_background.png"



        vbox:

            xpos 80

            vbox:
                label "[config.name!t]"
                text _("Version [config.version!t]\n")
            
            vbox:
                label _("WRITING")
                text _("Scenario: {a=https://nightlightwrks.itch.io/}Night Light{/a}")
                text _("Writers: {a=https://nightlightwrks.itch.io/}Night Light{/a} & {a=https://tenshistudios.itch.io/}tenshideve{/a}")
                text _("Editing: {a=https://www.christopherrexsmith.com/}Chris Smith{/a}")                
                text _("Proofreading: {a=https://nir4.itch.io/}Manedza\n")


            vbox:
                label _("PROGRAMMING")
                text _("Programer: {a=https://mawafu.itch.io/}Mawafu{/a}")
                text _("GUI/GUI Design: {a=https://vgen.co/OtokeNeko}Otoke Neko{/a}\n")

            vbox:
                label _("ARTWORK")
                text _("Character Linework/Sprites: {a=https://hanajii.carrd.co/}Hana-Jii{/a}")
                #text _("Silhouettes: {a=https://tenshistudios.itch.io/}tenshideve{/a}")
                text _("Backgrounds: {a=https://bsky.app/profile/ceefarer.bsky.social}Ceefarer{/a} & {a=https://vgen.co/OtokeNeko}Otoke Neko{/a}")
                text _("CGs: {a=https://prinxqe.itch.io/}Jam{/a}")
                text _("Cover Art: {a=https://bsky.app/profile/ceefarer.bsky.social}Ceefarer{/a}")  
                text _("Chibis: {a=https://vgen.co/MilinaBryce}Milina Bryce{/a}")                              
                text _("On Screen Assests: {a=https://nightlightwrks.itch.io/}Night Light{/a}")
                text _("Character Rendering: {a=https://nightlightwrks.itch.io/}Night Light{/a}")
                text _("Logo: {a=https://www.theresamacgillvo.com/}Theresa MacGillivray{/a}\n")
      
            vbox:
                label _("MUSIC")
                text _("Character & Emotion Tracks: {a=https://aidenrosecreative.itch.io/}Aiden Rose{/a}")
                text _("Location Tracks & SFX: {a=https://www.gabrielhabanamusic.com/}Gabriel Habana{/a}\n")
                #text _("Music: {a=https://janhehr.itch.io/city-date}Jan Hehr{/a}")
                #text _("Music: {a=https://lolurio.itch.io/jazz-bossa-nova-music}lolurio{/a}")                

            vbox:
                label _("VOICE")
                text _("Astra:{a=https://calistaiman.carrd.co/} Calista Iman")
                text _("Albion:{a=https://xihe.carrd.co/} Lu Scott{/a}")  
                text _("Felix: {a=https://hyzellcollinsjr.carrd.co/} Hyzell Collins Jr ")  
                text _("Qwynn: {a=https://phantazmagoriya.carrd.co/} Phantazmagoriya")  
                text _("Caelan: {a=https://ellisbertrellva.wixsite.com/voice} Ellis Bertrell Middleton\n")    

            vbox:
                label _("RESOURCES")
                text _("Renpy Transforms List: {a=https://otojang.itch.io/renpy-transforms-list}Otoke Neko")
                text _("Forest BG: {a=https://qdanp.itch.io/forest-stage-escenario-bosque}qDANp{/a}")  
                text _("Extra Sound Effects: Mixkit & Pixabay\n")      

            ## gui.about is usually set in options.rpy.
            vbox:
                if gui.about:
                    text "[gui.about!t]\n"
            vbox:
                xsize 900
                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("SAVE"))


screen load():

    tag menu

    use file_slots(_("LOAD"))


screen file_slots(title):


    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Auto saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"
    
                key_events True
                xalign 0.0
                xoffset -5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value
              
            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                                
                xalign 0.1
                xoffset -10
                yalign 0.5
        

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has hbox
                        xsize 905
                        ysize 170

                        add FileScreenshot(slot, empty="gui/button/slot_locked.png"):
                            xalign 0.0
                            xsize 300
                            ysize 170
                            ypos -5
                            zoom 0.92
                        vbox:
                            xsize 580
                            ysize 70
                            label _("Slot #[slot]")
                            text FileTime(slot, format=_("{#file_time}%d/%m/%Y, %H:%M"), empty=_("NO DATA")):
                                style "slot_time_text"
                                size 30
                                

                            text FileSaveName(slot):
                                style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.38
                yalign 1.0
                yoffset -770

                spacing -5#gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    ypos 705
    xalign 0.3
    xpadding 75
    ypadding 5
    xoffset 115

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")
    xoffset 115  
    padding (7,0)

style page_button_text:
    properties gui.button_text_properties("page_button")
    size 27

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    idle_color "#6a4e3d"     
    hover_color "#e297b2"


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("OPTIONS")):

        hbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        #label _("~Display")
                    imagebutton: #_("Window") 
                        idle "images/checkmark_idle.png"
                        hover "images/checkmark_hover.png"
                        selected_idle "images/checkmark_selected_idle.png"
                        selected_hover "images/checkmark_selected_hover.png"
                        pos (610,405)
                        action Preference("display", "window")

                    imagebutton: #_("Fullscreen") 
                        idle "images/checkmark_idle.png"
                        hover "images/checkmark_hover.png"
                        selected_idle "images/checkmark_selected_idle.png"
                        selected_hover "images/checkmark_selected_hover.png"
                        pos (588, 447)
                        action Preference("display", "fullscreen")

                #vbox:
                    #style_prefix "radio"
                    #label _("~Rollback Side")
                    #textbutton _("Disable") action Preference("rollback side", "disable")
                    #textbutton _("Left") action Preference("rollback side", "left")
                    #textbutton _("Right") action Preference("rollback side", "right")

                                                           
                vbox:
                    style_prefix "check"
                    #label _("~Skip")
                    imagebutton: #_("Unseen Text")
                        idle "images/checkmark_idle.png"
                        hover "images/checkmark_hover.png"
                        selected_idle "images/checkmark_selected_idle.png"
                        selected_hover "images/checkmark_selected_hover.png"
                        pos (567, 198)
                        action Preference("skip", "toggle")
                    
                    imagebutton: #_("After Choices")
                        idle "images/checkmark_idle.png"
                        hover "images/checkmark_hover.png"
                        selected_idle "images/checkmark_selected_idle.png"
                        selected_hover "images/checkmark_selected_hover.png"
                        pos (567, 215)                   
                        action Preference("after choices", "toggle")

                    imagebutton: #_("Transitions")
                        idle "images/checkmark_idle.png"
                        hover "images/checkmark_hover.png"
                        selected_idle "images/checkmark_selected_idle.png"
                        selected_hover "images/checkmark_selected_hover.png"
                        pos (567,233)                        
                        action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    xpos -600
                    ypos 100
                
                    label _("~Text Speed~")

                    bar value Preference("text speed")

                    label _("~Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:
                    xpos -600
                    ypos 170
             
                    if config.has_music:
                        label _("~Music Volume~")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("~Sound Volume~")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                
            


                    if config.has_voice:
                        label _("~Voice Volume~")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")


style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 490

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html


screen history():
    style_prefix "history"
    modal True
    predict False
    add "gui/overlay/menu_overlay.png"
    fixed:
        at ts_screenfadein()

        add "gui/menubg/log_background.png" align (0.5, 0.5)

        viewport:
            xysize (875, 550)
            pos (515, 260)
            scrollbars "vertical"
            yinitial 1.0

            draggable True pagekeys True mousewheel True

            has vbox
            for h in _history_list:
                null height 50
                frame:
                    has hbox
                    if h.who:
                        label h.who style "history_name":
                            substitute False
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                            xsize 200

                    else:
                        null width 200

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False
                        xsize 600
                        size 30
                        
                null height 50
                add "gui/history_line_divider.png" xalign 0.5
                

            if not _history_list:
                label _("The dialogue history is empty.")

        ## RETURN ##
        imagebutton:
            idle "images/return_idle.png"
            hover "images/return_hover.png"
            activate_sound "audio/sfx_click.ogg"
            pos (1135, 920)
            action Return()



screen history_old():

    tag menu
    

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("HISTORY"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
            
    
                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                            substitute False

            
        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }

############################################################
## HISTORY STYLES ##
############################################################

style history_name:
    xalign 0.0
    yalign 0.5

style history_frame:
    background None
    xfill True

# style history_name is gui_label
# style history_name_text is gui_label_text
# style history_text is gui_text

# style history_text is gui_text

# style history_label is gui_label
# style history_label_text is gui_label_text

# style history_window:
#     xfill True
#     ysize gui.history_height

# style history_name:
#     xpos gui.history_name_xpos
#     xanchor gui.history_name_xalign
#     ypos gui.history_name_ypos
#     xsize gui.history_name_width

# style history_name_text:
#     min_width gui.history_name_width
#     text_align gui.history_name_xalign

# style history_text:
#     xpos gui.history_text_xpos
#     ypos gui.history_text_ypos
#     xanchor gui.history_text_xalign
#     size 30
#     xsize gui.history_text_width
#     min_width gui.history_text_width
#     text_align gui.history_text_xalign
#     layout ("subtitle" if gui.history_text_xalign else "tex")

# style history_label:
#     xfill True

# style history_label_text:
#     xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("HELP"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 10

            hbox:

                xalign 0.5
                xoffset 30

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    vbox:
        xpos -40  
 

        hbox:
            label _("Enter")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Space")
            text _("Advances dialogue without selecting choices.")

        hbox:
            label _("Arrow Keys")
            text _("Navigate the interface.")

        hbox:
            label _("Escape")
            text _("Opens the save menu.")

        hbox:
            label _("Ctrl")
            text _("Skips dialogue while held down.")

        hbox:
            label _("Tab")
            text _("Toggles dialogue skipping.")

        hbox:
            label _("Page Up")
            text _("Rolls back dialogue.")

        hbox:
            label _("Page Down")
            text _("Rolls forward dialogue.")

        hbox:
            label "H"
            text _("Hides the user interface.")

        hbox:
            label "S"
            text _("Takes a screenshot.")

        hbox:
            label "V"
            text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

        hbox:
            label "Shift+A"
            text _("Opens the accessibility menu.")


screen mouse_help():

    vbox:
        xpos 75


        hbox:
            label _("Left Click")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Middle Click")
            text _("Hides the user interface.")

        hbox:
            label _("Right Click")
            text _("Accesses the game menu.")

        hbox:
            label _("Mouse Wheel Up") #\nClick Rollback Side
            text _("Rolls back dialogue.")

        hbox:
            label _("Mouse Wheel Down")
            text _("Rolls forward dialogue.")

        hbox:
            label _("Mouseover+Del")
            text _("Delete save files.")


screen gamepad_help():

    vbox:
        xpos 75

        hbox:
            label _("Right Trigger\nA/Bottom Button")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Left Trigger\n/Left Shoulder")
            text _("Rolls back dialogue.")


        hbox:
            label _("Right Shoulder")
            text _("Rolls forward dialogue.")
            
        hbox:
            label _("D-Pad, Sticks")
            text _("Navigate the interface.")

        hbox:
            label _("Start, Guide")
            text _("Accesses the game menu.")

        hbox:
            label _("Y/Top Button")
            text _("Hides the user interface.")

        textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0




################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    yoffset 25

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)


style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

### Choice Indicator Screen ############################################################
##
## Screen that pops up then you make a good choice for that love interest.
## Why use a screen instead of an image?
# - Pauses user interaction
# - one line: i'm lazy



############################################################
### DEFAULTS/DEFINES ###
############################################################

define FELIX_COLOR = "#51a34f"
define QWYNN_COLOR = "#E45472"
define CAELAN_COLOR = "#51ABE4"

image f01 = "gui/flowers/f01.png"
image f02 = "gui/flowers/f02.png"
image f03 = "gui/flowers/f03.png"
image f04 = "gui/flowers/f04.png"
image f05 = "gui/flowers/f05.png"
image f06 = "gui/flowers/f06.png"


# Change ts_speed to adjust speed.
# Remeber to also adjust the screen timer.
transform ts_indicator_anim(ts_speed=2.5):
    alpha 0.0
    xoffset 60
    parallel:
        linear ts_speed/3 alpha 1.0
    parallel:
        linear ts_speed xoffset -20 # Change xoffset to adjust speed. 
    parallel:
        pause ts_speed - 1.5
        linear ts_speed/3 alpha 0.0

transform ts_rotate(ts_speed=4.0):
    anchor (0.5, 0.5)
    subpixel True # Enables smooth movements
    rotate 0
    linear ts_speed rotate 360
    repeat

# This is used to recolor the flower
# The default is a transparent color: e.g. Nothing.
transform ts_recolor(color):
    matrixcolor TintMatrix(color)


############################################################
### CHOICE INDICATOR SCREEN ###
############################################################
## Simply show this screen under the correct choice

screen choice_indicator(color="#FFFFFF00"):
    modal True # disable user interaction when this screen shows; you can comment this out if you don't like it

    zorder 100 # So that it appears on top of textbox.

    frame: # To keep everything together
        background None
        
        xysize (91, 107)
        pos (1418, 821) # CHANGE THIS: if you want to reposition where the flowers appear

        ## Images ##
        add "f01":
            at ts_rotate(), ts_indicator_anim(), ts_recolor(color)
            pos (36, 36)

        add "f02":
            at ts_rotate(), ts_indicator_anim(), ts_recolor(color)
            pos (0, 0)

        add "f03":
            at ts_rotate(), ts_indicator_anim(), ts_recolor(color)
            pos (5, 65)

        add "f04":
            at ts_rotate(), ts_indicator_anim(), ts_recolor(color)
            pos (37, 87)

        add "f05":
            at ts_rotate(), ts_indicator_anim(), ts_recolor(color)
            pos (52, 14)

        add "f06":
            at ts_rotate(), ts_indicator_anim(), ts_recolor(color)
            pos (74, 28)

        # hides screen after 3.0 seconds, re-enabling user interaction
        timer 2.7 action Hide()


### Relationship Screen ############################################################
##
## This screen shows the current affection points for the current love interest.
##

############################################################
### DEFAULTS/DEFINES ###
############################################################

# Change this to whatever name you like, but be sure to update it everywhere else too.
default felix_pts = 0
default albion_pts = 0
default qwynn_pts = 0
default caelan_pts = 0

# Change this to either felix or albion depending on route
# This is also used for screen choice_indicator()
# It WIL NOT work if you keep this to None
default route = None

define config.developer = True

transform ts_spriteREnter(xoff=200, ts_speed=0.5):
    # if you don't want the sprites to fade in, comment out the alpha
    alpha 0.0
    xoffset xoff
    linear ts_speed xoffset 0 alpha 1.0

### Add this to either your screen quick_menu() or anywhere you want

    

############################################################
### RELATIONSHIP SCREEN ###
############################################################
##

screen relationship_pts():
    style_prefix "rs"

    tag menu

    add "gui/overlay/game_menu.png"
    #add "gui/affection/affection_title.png":
        #pos (60,100)
    

    # if you want the player to still access this screen when not on a route, but show no one, uncomment below
#if route:
    vbox:
        pos (350, 125)
        
        #label _(route.capitalize())

        ## Affection points bar
        # https://feniksdev.com/the-definitive-default-define-renpy-article/
        # all defaults and defines are stored in the 'store' namespace
        vbar value AnimatedValue(getattr(store, route+"_pts"), 100):
            style "rs_vbar"
            pos (80, 20)
            xsize 300
            ysize 750
            


    add route + "_Aff.png" at ts_spriteREnter():
        zoom 1.8
        pos (200, -150)
    
    
    add route + "_title_card.png" at ts_spriteREnter():
        xpos 0.59
        ypos 90

        #if $ route = 'caelan' and $ persistent.caelanname == True
            #add route + "caelan2_title_card.png" at ts_spriteREnter():
                # xpos 0.59
                #ypos 90

        

    ## RETURN ##
    imagebutton:
        idle "images/return_idle.png"
        hover "images/return_hover.png"
        activate_sound "audio/sfx_click.ogg"
        xalign 0.0
        yalign 1.0
        yoffset -45
        xoffset 1550
        action Return()
    


############################################################
### STYLES ###
############################################################

style rs_vbox:
    xalign 0.5
    spacing 30
    underline True

style rs_label_text:
    size 50
    text_align 0.5
    xalign 0.5

style rs_vbar:
    xalign 0.5
    xsize 251
    ysize 600
    thumb "gui/affection/[route]_thumb.png"
    thumb_offset -100



