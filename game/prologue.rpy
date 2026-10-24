# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def text_scroll_sound(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/sfx_text.ogg", channel="sound", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")

# Apply this callback to dialogue
define config.all_character_callbacks = [text_scroll_sound]

define a = Character("ASTRA", color="#7e6fd6")
define q = Character("QWYNN", color="#e45472")
define al = Character("ALBION", color="#df6f98")
define f = Character("FELIX", color="#3c9b7c")
define s = Character("SYLPHIA", color="#3a0f0c")
define c = Character("CAL", color="#5187e4")
define ca = Character("CAELAN", color="#5187e4")
define n = Character("NIMUE", color="#3a0f0c")
define v = Character("VELVET", color="#3a0f0c")
define who = Character("???", color="#3a0f0c")
define att = Character("ATTENDANT", color="#3a0f0c")
define e = Character("ELLWOOD", color="#3a0f0c")
define ver = Character("MISS VERAC", color="#3a0f0c")
define cus = Character("CUSTOMER", color="#3a0f0c")
define ae = Character("AERIS", color="#3a0f0c")

#ASTRA SIDE IMAGE 

define aside = Character ("ASTRA", color="#7e6fd6", image="astra")
define asidee = Character ("ASTRA", color="#7e6fd6", image="astrae")
define asidep = Character ("ASTRA", color="#7e6fd6", image="astrap")
define asidea = Character ("ASTRA", color="#7e6fd6", image="astraa")
define asidesa = Character ("ASTRA", color="#7e6fd6", image="astra_sad")
define asidean = Character ("ASTRA", color="#7e6fd6", image="astra_angry")
define asidesh = Character ("ASTRA", color="#7e6fd6", image="astra_sheepish")
define asidesm = Character ("ASTRA", color="#7e6fd6", image="astra_smug")
define asidesp = Character ("ASTRA", color="#7e6fd6", image="astra_speak")
define asideem = Character ("ASTRA", color="#7e6fd6", image="astra_embarrased")
define asideb = Character ("ASTRA", color="#7e6fd6", image="astra_blush")
define asideeb = Character ("ASTRA", color="#7e6fd6", image="astra_extrablush")
image define aside = "side astra"
image define asidee = "side astrae"
image define asidep = "side astrap"
image define asidea = "side astraa"
image define asidesa = "side astra_sad"
image define asidean = "side astra_angry"
image define asidesh = "side astra_sheepish"
image define asidesm = "side astra_smug"
image define asidesp = "side astra_speak"
image define asideem = "side astra_embarrased"
image define asideb = "side astra_blush"
image define asideeb = "side astra_extrablush"

#ASTRA SIDE IMAGE WITH APRON

define aside2 = Character ("ASTRA", color="#7e6fd6", image="astra_apron")
define asidee2 = Character ("ASTRA", color="#7e6fd6", image="astrae_apron")
define asidep2 = Character ("ASTRA", color="#7e6fd6", image="astrap_apron")
define asidea2 = Character ("ASTRA", color="#7e6fd6", image="astraa_apron")
define asidesa2 = Character ("ASTRA", color="#7e6fd6", image="astra_sad_apron")
define asidean2 = Character ("ASTRA", color="#7e6fd6", image="astra_angry_apron")
define asidesh2 = Character ("ASTRA", color="#7e6fd6", image="astra_sheepish_apron")
define asidesm2 = Character ("ASTRA", color="#7e6fd6", image="astra_smug_apron")
define asidesp2 = Character ("ASTRA", color="#7e6fd6", image="astra_speak_apron")
define asideem2 = Character ("ASTRA", color="#7e6fd6", image="astra_embarrased_apron")
define asideb2 = Character ("ASTRA", color="#7e6fd6", image="astra_blush_apron")
define asideeb2 = Character ("ASTRA", color="#7e6fd6", image="astra_extrablush_apron")
image define aside2 = "side astra_apron"
image define asidee2 = "side astrae_apron"
image define asidep2 = "side astrap_apron"
image define asidea2 = "side astraa_apron"
image define asidesa2 = "side astra_sad_apron"
image define asidean2 = "side astra_angry_apron"
image define asidesh2 = "side astra_sheepish_apron"
image define asidesm2 = "side astra_smug_apron"
image define asidesp2 = "side astra_speak_apron"
image define asideem2 = "side astra_embarrased_apron"
image define asideb2 = "side astra_blush_apron"
image define asideeb2 = "side astra_extrablush_apron"

#IMAGE DEFINES

image Felix = "Felix_N.png"
image Felix_U = "Felix_Upset.png"
image Felix_C = "Felix_Concern.png"
image Felix_B = "Felix_Blush.png"
image Felix_S = "Felix_S.png"
image Felix_E = "Felix_E.png"
image Felix_N2 = "Felix_N2.png"
image Felix_Sad = "Felix_Sad.png"
image Felix_EX = "Felix_Ex.png"
image Albion = "Albion_N.png"
image Albion_S = "Albion_Smile.png"
image Albion_SC = "Albion_Scowl.png"
image Albion_B = "Albion_B.png"
image Albion_N2 = "Albion_N2.png"
image Albion_H = "Albion_H.png"
image Albion_E = "Albion_E.png"
image Albion_Shy1 = "Albion_Shy1.png"
image Albion_Shy2 = "Albion_Shy2.png"
image Albion_Shy3 = "Albion_Shy3.png"
image Sylphia = At("Sylphia_N.png")
image Qwynn = At("Qwynn_N.png", half_size)
image Qwynn_M = At("Qwynn_Melon.png", half_size)
image Qwynn_B = At("Qwynn_Blush.png", half_size)
image Qwynn_S = At("Qwynn_Smile.png", half_size)
image Qwynn_EX = At("Qwynn_Ex.png", half_size)
image Qwynn_N2 = At("Qwynn_N2.png", half_size)
image Qwynn_N3 = At ("Qwynn_N3.png", half_size)
image Qwynn_A = At("Qwynn_A.png", half_size)
image Velvet = "Velvet_N.png"

image Astra = "Astra_N.png"
image Astra2 = "Astra_N_apron.png"
image Astra_E = "Astra_E.png"
image Astra_E2 = "Astra_E2.png"
image Astra_P = "Astra_pout.png"
image Astra_P2 = "Astra_pout_apron.png"
image Astra_A = "Astra_annoyed.png"
image Astra_A2 = "Astra_annoyed_apron.png"
image Astra_EM = "Astra_embarrased.png"
image Astra_EM2 = "Astra_embarrased_apron.png"
image Astra_AN = "Astra_angry.png"
image Astra_AN2 = "Astra_angry_apron.png"
image Astra_SA = "Astra_sad.png"
image Astra_SA2 = "Astra_sad_apron.png"
image Astra_SH = "Astra_sheepish.png"
image Astra_SH2 = "Astra_sheepish_apron.png"
image Astra_SM = "Astra_smug.png"
image Astra_SM2 = "Astra_smug_apron.png"
image Astra_B = "Astra_blush.png"
image Astra_B2 = "Astra_blush_apron.png"
image Astra_EB = "Astra_extrablush.png"
image Astra_EB2 = "Astra_extrablush_apron.png"


init python:
    # Register a new channel named "ambient", assigned to the "sfx" mixer
    renpy.music.register_channel("ambient", mixer="sfx", loop=True)
    renpy.music.register_channel("sfx", mixer="sfx", loop=False)



###################################
#HALF SIZE TRANSFORM THING
###################################

transform half_size:
    zoom 1.1  # Adjust zoom level as needed    
    xpos 600
    ypos -50

###################################
#ZOOM IN TRANSFORM THING
###################################

transform right:    
    xpos 900

###################################
#ZOOM IN TRANSFORM THING
###################################

transform left:    
    xpos 300


label start:

    $ persistent.status_button = False
    
    show prochp0
    $ renpy.pause(1.0)
    window hide
    pause (3.0)
    window auto

    play music "cafebloom_night.ogg" 
    
    scene cafe_interior_evening with dissolve

    aside2 "Thank you! Come again!"
   
    play audio "<from 0 to 3>bell.mp3"
    
    "The bell at the door jingles as the customer leaves the café. I sigh, once more enveloped in peaceful quiet."
    "Sunset seeps in through the open windows bathing the room in soft pink light. A light breeze gently blows the curtains around."
    "With no other customers around, I reach for a cloth to start cleaning the coffee bar."
    "Back and forth, I move the cloth across the counter... Something about the motion, combined with the serene atmosphere, is soothing."
    "The only sounds are the sweet chirping of the birds and the distant rush of water through the street's canals."
    asidesh2 "Haaaah..."
    s "Astra? Do you have a moment?"
   
    play sound "sfx_shake.ogg"
    show cafe_interior_evening with vpunch
  
    "My body jerks, so startled by the sudden voice that I freeze mid wipe... Seems like working in silence for hours has lulled me into a false sense of security."
    "Behind me stands Sylphia, smiling knowingly."
   
    show Sylphia with moveinright
  
    aside2 "(She definitely wasn't there just a second ago.)"
    asidea2 "...You do that on purpose, don't you?"
    "Sylphia's smile doesn't change, her face as placating as ever."
    s "Certainly not. Why would I want to scare you?"
    asidea2 "...That's what I'd like to know."
    "Sylphia doesn't respond. Instead she rounds the counter where I've been cleaning and settles into one of the chairs lining the bar."
  
    show Sylphia:
        zoom 1.5
        xoffset 0 
        yoffset 400
    with dissolve
    
    s "I'd like your opinion on something important."
    "Her tone is calm, but there's a seriousness in her eyes. I straighten a little, curious."
    s "With Halis' popularity increasing, I've been thinking of ways to revitalize the café. If we want Bloom to thrive, we can't just keep doing the same thing forever."
    s "I've lived long enough to know that it just doesn't work."
    s "In other words, I'm looking to spice things up."
    aside2 "Spice... things up?"
    s "Mhm! I want you to help me make some changes around here to help boost our patronage."
    asidee2 "Really? That sounds like fun! I'd love to help."
    aside2 "What kinds of changes are we making?"
    s "Well, I have a few ideas, though I was hoping you could help me decide." 
    aside2 "Me? But— I mean, I've barely been here for a full year! Should I really have a say in this?" 
    s "Of course! I trust you. Besides, who better to help improve our little café than its number one fan?"

    hide Sylphia with dissolve

    "My cheeks grow red with embarrassment, though what Sylphia says {i}is{/i} accurate…" 
    "However, underneath that embarrassment lies a tentative excitement."
    aside2 "...Alright then, what are you thinking?"

    show Sylphia with dissolve

    s "I've narrowed it down to three possibilities." 

    s "Option one, we focus on the menu. Not that there's anything wrong with the one we have now, but it could certainly use a refresh." 
    s "I figure doing something seasonal might give customers a reason to come back over and over again."
    s "Option two, we really hone in on the community aspect of Café Bloom. We become a place that not only serves good coffee and food, but a place that creates a space for local artists and creatives to gather."
    s "Option three, renovations, stronger branding, actually marketing ourselves instead of hoping people will stumble across us. Or more simply put, the overall atmosphere."
    s "What do you think?"

    hide Sylphia with dissolve 

    "If I'm being honest with myself, it sounds fantastic."
    "Having the opportunity to work on a project like this... knowing that Sylphia trusts me to do it? It's the opportunity of my dreams."
    asidesa2 "(Can I really do this?)"
    "To anyone else this might seem like a simple request. But for me? This is a step forward in my career, a chance to further earn my place at Café Bloom."
    "Though it's small, and simple, I love it with every ounce of my being." 
    "In a short amount of time, Café Bloom has become special to me." 
    "Everyday is fun as I spend my days learning how to make coffee, interacting with customers, and working beside Sylphia and Albion who—despite what {i}one{/i} of them might say—"
    "...are some of my closest friends."
    aside2 "(...)"
    aside2 "(Seems like I've made up my mind already.)"
    aside2 "I'd love to help!"
   
    show Sylphia with dissolve
   
    s "Great! I didn't have a backup plan if you were to say no."
    s "I suppose I could have asked Albion but..."
    asidesh2 "...Yeah."
    "Sylphia and I share a knowing smile."
    aside2 "Good thing I said yes then."
    s "Yes, everything fell into place perfectly."
    s "I don't think we have to rush, but I thought it might be nice if we could choose which plan to execute by next week."
    aside2 "No problem! I'll do my best to consider each option thoroughly!" 
    s "I already put together a budget to pay for anything we might need so no need to worry about that."
    s "Just, don't work yourself too hard. I know what you're like." 
    asidesh2 "{i}Ahaha{/i}, I think I can manage that."
    s "Then, we have ourselves a deal."
    "Sylphia reaches her right hand out to me from over the bar."

    hide Sylphia with dissolve

    "My own right hand mirrors hers, sealing the deal."
    
    
    asidee2 "(What an exciting way to start spring!)"


    jump chp1





