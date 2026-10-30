## Glossary screen ################################################################
##
## This screen explains in-game terms

############################################################
### WORD DICT ###
############################################################
## Define all words here
##
transform ts_screenfadein():
    on show:
        alpha 0.0 yoffset 20
        linear 0.3 alpha 1.0 yoffset 0

define glossary_world = {
    
    "Eras": "The city of ice. Not much is known about the Ice Dragon Saint. Only that they are a rare dragon blessed with the ability to use ice magic. Which is famously not included as one of the four core elements recognized in Feldoria.",

    "Feldoria": "The country in which the city of Halis is located. It is a magical land overflowing with natural energy. In spite of this, Feldoria is actually most notable for its five Intergrative Cities which have proven to be fruitful in their endeavor to house a large variety of races with minimal conflict.",

    "Halis": "The city of water watched over by Saint Caelan. Possesses the miracle of pure and unpollutable water. One of the five Intergrative cities in the country of Feldoria.",

    "Intergrative City": "A city that is built and developed specifically to be home to both humans and various magical races. There are five major and official Intergrative cities in the country of Feldoria.\n\nOther cities, towns, and villages exist where humans and magical races live together, but because those places were not designed with the intent to house multiple races they are not classified as 'Intergrative'.",
    
    "Sholair": "The city of air. Watched over by the Air Dragon Saint, Aiolos. One of the five Intergrative cities. Located along the coast of Feldoria. Large floating ecosystems attract those who wish to see how the Air Dragon's miracle defies gravity. Additionally, rumors say you can encounter the elusive Mermaids there.",

    "Grav": "The city of earth. Watched over by the Earth Dragon Saint and the giants who've made the mountains surrounding Grav their home.",

    "Valanche": "The city of fire, watched over by the Fire Dragon Saint. Many people from all over Feldoria come to Valanche in search of rest and relaxation. Good vibes practically ooze from every corner. The first of the five Intergrative Cities. The city of Valanche possesses a healing aura, making it a popular place for those who wish to ease symptoms of disease.",
}

define glossary_magic = {
    "Elements": "The four elements are defined as fire, water, air, and earth.",

    "Magic": "Any feat that influences one of the four elements.",

    "Miracles": "The presence of a Dragon often results in magic so powerful that it can cause 'miracles'.\n\nThis can range from creating pure water unaffected by pollution or waste, to causing chunks of land to float off of the ground and creating floating ecosystems.",

    "Tethering": "Many Dragons will choose a forest, spring, mountain or some other natural place to settle in. Dragons spend their first hundred or so years traveling the world before settling. \n\nOnce they choose where they wish to live they will tether themselves to it. This increases both the Dragons magic, and the magic in the land. However, some choose to forever roam free, accepting of the fact that it will shorten their life span.",
}
define glossary_races = {
    "Magical Races": "Any races that has a connection to one of the four elements (fire, water, air, and earth). A large majority of magical races also have the ability to influence the elements that their race is connected to.",

    "Were-folk": "A race that is defined by their various animalistic features. They cannot directly influence any of the elements but they do share a close relationship with nature, which enhances their sense of touch, smell, taste, and sight.",

    "Humans": "A race that does not have any connection to one of the four elements. As such, humans cannot influence the elements.",

    ## races 2 ##
    "Dragons": "Dragon are powerful beings who hold a stronger connection to magic than other race, they are made of pure magic and survive off of its natural energy.\n\nAs a result, they are at their strongest when they tether themselves to a place with a high concentration of magic. Dragons are able to take a humanoid form, though many only do this when necessary.",

    "Dwarves": "Dwarves live among the mountains and underground cave systems of Feldoria. They are closely connected to the element of fire which they use to craft superior weapons and tools.\n\nDwarves are also avid traders and will travel to towns and cities selling their wares.",

    "Elves": "A long lived race characterized by their connection to nature, their ability to influence any of the four elements, and their everlasting youth.\n\nAdditionally, Elves boast a speed and strength that is superior to that of humans. In terms of appearance they look similar to humans, but they tend to be taller with long ears that face outwards.",

    ## races3 ##
    "Giants": "Large creatures who look like they have been carved from stone. Giants live in the mountains in close proximity to the Dwarves.\n\nTheir ability to speak is limited, but they are a peaceful and sedentary race who spend their years observing the lives of the 'little ones' down below. Giants are connected to the element of earth.",

    "Mermaid": "Beautiful creatures of water, mermaids live in the oceans surrounding Feldoria. They are rarely seen, but it is said they have their own advanced infrastructure in the depths of the oceans. Sometimes they will bring things to the surface in an attempt to trade with the races of the surface.",

    "Unicorn": "Unicorns live among nature, often in groups near Dragons. The two races share mutually-beneficial relationship.\n\nUnicorns are not connected to one specific element, but like Dragons they release a natural energy that vitalizes the land around them. Albeit in a lesser amount."

}

define glossary_nymph = {
    "Nymphs": "Nymphs and Elves are closely related. They share a similar ear shape to elves (though they slope downwards rather than upwards), have a connection to the elements (Nymphs are separated into three subraces, each connected to a different element), and maintain their youthful appearance forever.\n\nHowever, they are not long-lived and they do not possess any superior strength or speed. Some have coined the term 'lesser-elf' to use as an insult to Nymphs.",

    "~The Aurea": "A sub-race of Nymphs that are connected to the element of air. The Aurea tend to enjoy traveling and are typically more social than other Nymphs.",

    "~The Naiad": "A sub-race of Nymphs that are connected to the element of water. This race is often found living in places with a lot of water.",

    "~The Dryad": "A sub-race of Nymphs that are connected to the element of earth. They are often found living in forests or smaller settlements in order to be closer with nature.",
    
}

############################################################
### GLOSSARY SCREEN ###
############################################################

screen glossary():
    modal True
    default page = "world"

    add "gui/overlay/menu_overlay.webp"

    fixed:
        at ts_screenfadein()
        add "gui/menubg/glossary_background.webp" align (0.5, 0.5) 

        ### PAGES ###
        hbox:
            at ts_screenfadein()
            
            pos (740, 210)
            spacing 20

            textbutton _("World") action SetScreenVariable("page","world")
            textbutton _("Magic") action SetScreenVariable("page","magic")
            textbutton _("Races") action SetScreenVariable("page","races")
            textbutton _("Races: Nymph") action SetScreenVariable("page","nymhs")


        if page == "world":
            use world()
        elif page == "magic":
            use magic()
        elif page == "races":
            use races()

        elif page == "nymhs":
            use nymhs()

        ## RETURN ##
        imagebutton:
            idle "images/return_idle.webp"
            hover "images/return_hover.webp"
            activate_sound "audio/sfx_click.ogg"
            pos (1250, 920)
            action Return()
        

            

screen world():
    style_prefix "gloss_page"
    default def_text = glossary_world.get("Feldoria")

    hbox:
        pos (427, 345)

        ## BUTTONS ##
        vbox:
            for word, defin in glossary_world.items():
                button:
                    text word
                    action SetLocalVariable("def_text", defin)

        
        ## TEXT ##
        if def_text:
            viewport id "glosspvp":
                xsize 700
                #xalign 1.0
                xpos -38
                
                scrollbars "vertical"

                mousewheel True draggable True pagekeys True

                text def_text 




screen magic():
    style_prefix "gloss_page"
    default def_text = glossary_magic.get("Elements")

    hbox:
        pos (427, 345)

        ## BUTTONS ##
        vbox:
            for word, defin in glossary_magic.items():
                button:
                    text word
                    action SetLocalVariable("def_text", defin)

        
        ## TEXT ##
        if def_text:
            viewport id "glosspvp":
                xsize 700
                xpos -38
                
                scrollbars "vertical"

                mousewheel True draggable True pagekeys True

                text def_text 

        
screen races():
    style_prefix "gloss_page"
    default def_text = glossary_races.get("Magical Races")

    hbox:
        pos (427, 345)

        ## BUTTONS ##
        vbox:
            for word, defin in glossary_races.items():
                button:
                    text word
                    action SetLocalVariable("def_text", defin)

        
        ## TEXT ##
        if def_text:
            viewport id "glosspvp":
                xsize 700
                xpos -38
                
                scrollbars "vertical"

                mousewheel True draggable True pagekeys True

                text def_text 


screen nymhs():
    style_prefix "gloss_page"
    default def_text = glossary_nymph.get("Nymph")

    hbox:
        pos (427, 345)

        ## BUTTONS ##
        vbox:
            for word, defin in glossary_nymph.items():
                button:
                    text word
                    action SetLocalVariable("def_text", defin)

        
        ## TEXT ##
        if def_text:
            viewport id "glosspvp":
                xsize 700
                xpos -38
                
                scrollbars "vertical"

                mousewheel True draggable True pagekeys True

                text def_text 


############################################################
### GLOSSARY STYLES ###
############################################################
style gloss_page_hbox:
    xysize (1065, 583)
    xfill True
    

style gloss_page_vbox:
    xsize 500
    spacing 10

style gloss_page_button is default:
    xysize (400, 50)
    background None
    hover_background "#E297B2"
    selected_background "#DEC9BC"
    selected_hover_background "#E297B2"

style gloss_page_text:
    xoffset 20
    yalign 0.5



# style glossary_button is gui_button
# style glossary_button_text is gui_button_text
# style glossary_label is gui_label
# style glossary_label_text is gui_label_text
# style glossary_text is gui_text

# style glossary_button:
#     properties gui.button_properties("glossary_button")
#     xmargin 12

# style glossary_button_text:
#     properties gui.text_properties("glossary_button")

# style glossary_label_text:
#     color "#e297b2"
#     size gui.text_size
#     xalign 1.0
#     textalign 0.5

# style glossary_text:
#     justify True