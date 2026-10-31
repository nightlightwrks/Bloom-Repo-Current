# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


transform left:    
    xpos 300


label chp3:

    $ persistent.status_button = False

    window hide
    pause (1.0)
    window auto
    show prochp3 with squares
    $ renpy.pause(3.0)
    
    #The Water Nymph

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior_dawn with squares

    play audio "<from 0 to 3>bell.mp3"

    "The bell of the café rings, echoing in the silence of the early morning. Today is Saint's Day, the day that the Water Dragon, Caelan, was born."
    asidesp2 "(A customer? So soon after opening? That's rare.)"
    "Entering the café is a beautiful water nymph, with long flowing hair and eyes clear as a mountain spring."

    show Nimue with dissolve

    who "Good morning—"
    "She looks around, and between my surprised expression and the empty café, she appears to reconsider her entrance."
    who "Apologies, you {i}are{/i} open right?"
    asidesp2 "Yes! We are. How can I help you?"
    who "Oh, perfect. I was hoping you could help me with a special request."
    aside2 "Sure!"
    "The woman smiles. A faint thing."
    who "Today is my… friend's birthday. I want to bring them something special. They have a soft spot for anything warm."
    asidee2 "Oh? Being born on Saint's day is a good omen! At least, that's what they say." 
    n "It certainly is an auspicious day."
    "As she speaks, her smile warms."
    aside2 "So… something off the menu?"
    who "Precisely."
    asidesp2 "I can do that. Any preferences?"
    who "Sweet. Nothing bitter… so, no coffee."
    asidep2 "(Okay, no… coffee. At a coffee shop…)"
    aside2 "Right— uh, okay. Sweet. No coffee. Anything else?"
    who "That's all. I'll leave the rest up to you." 
    "Free reign is both a blessing and a curse. What if I make something terrible?"
    asidesm2 "(Only one way to find out.)"
    aside2 "Alright then, I'll get started right away Miss…"
    n "Nimue."
    aside2 "Miss Nimue. Please take a seat anywhere you like! I'll call you when it's ready."
    "She nods, turning away with an elegant flourish." 

    hide Nimue with dissolve

    "..."
    aside2 "(I guess I'll start with a milk base.)"
    "I recall a memory, back when I had just finished school and before I met Qwynn. It was the first time I had spent my birthday alone."
    "I remember making myself a drink... something my mother used to make for me after a long day."
    asidesh2 "(What was in it again?)"
    "My hands rummage through our seasonings and syrups. My hands gravitate towards the cinnamon, vanilla, and honey."
    asidee2 "(I think this is it.)"
    "The ingredients certainly {i}sound{/i} nice, but I still feel like it's missing one last thing."
    asidesp2 "(...Oh right, tea!)"
    "Our signature black tea jumps out at me."
    aside2 "(Similar to a Lushwyn Fog… but sweeter, and with more milk.)"
    "The process to put it all together is nothing too different from anything I usually make, and so it doesn't take me much time to put it together."
    asidesp2 "Miss Nimue? I've finished."

    show Nimue with dissolve

    aside2 "I hope your friend likes it. It's been some time since I made this particular drink."
    n "...I'm sure they will."
    "Nimue takes in her surroundings with a small smile."
    n "This is a beautiful place, I'd like to bring them here myself—but I'm afraid my friend can be quite stubborn."
    aside2 "Ah, a creature of habit?"
    "She nods." 
    aside2 "I can be the same way sometimes… Oh! And take this as well—"
    "I reach towards the display cabinet, carefully placing a chocolate croissant into a brown bag."
    aside2 "On the house."
    n "Are you sure?"
    asidee2 "Positive. Enjoy the rest of your day, Miss Nimue! And tell your friend I say 'Happy Birthday'."
    n "I think I just might. Thank you…"
    aside2 "Astra."
    n "Astra then. I'll pass your message along." 
    "With all the grace of a flowing stream, she disappears through the door of the café."

    hide Nimue with dissolve

    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior_evening with dissolve

    "The lights in the café are dim as the sun begins to set." 
    "Albion works quietly beside me, diligently cleaning a coffee tamper. I sit at one of the tables, using my break to soak in the serene calm and eating a delicious scone that Albion had forcibly given me."

    play audio "<from 0 to 3>bell.mp3"

    "I lift my head up from where it rests on my arms. A cloaked figure steps into the café and steps directly up to Albion at the bar."
    
    show Albion at left with dissolve
    
    al "Welcome in."

    show Caelan2 at right 
    show voiced
    with dissolve

    voice "<from 3.2 to 7>audio/Caelan/Caelan_intro.ogg" 
    who "My apologies, I'm looking for someone." 

    al "…"

    hide Caelan2
    show Caelan_ST2 at right 
    with dissolve

    voice "<from 11 to 15>audio/Caelan/Caelan_intro.ogg" 
    who "...Someone who works here. Astra."

    hide voiced
    hide Albion
    show Albion_SC at left 
    with dissolve

    "Albion's eyes slide over to me in what I think is him asking permission to tell this stranger who I am." 
    
    hide Albion_SC
    hide Caelan_ST2
    with dissolve

    asidesh2 "(Despite our disagreement the other day, Albion is still looking out for me.)"
    "He's giving me a choice."
    asidesa2 "(Do I want to talk to this stranger?)"
    
    #ROUTE CHOICE #2
    
    menu: 

        "Shake my head.": 
            show Albion at left with dissolve
            al "Sorry, I don't know anyone named Astra."
            show Caelan2 at right with dissolve
            who "Ah—I must have gotten mixed up. Apologies for wasting your time."
            "It's difficult to tell from where I sit, but they almost look disappointed." 
            "Albion shrugs, not denying that his time was wasted." 
            al "Can I help you with anything else?"
            who "No, that was all. Thank you."
            "And without lingering for even a second, the stranger turns away leaving behind only the faint scent of lavender."
            hide Albion
            hide Caelan2
            with dissolve
            jump route_select

        "Nod.":
            show screen choice_indicator(CAELAN_COLOR) 
            jump chp3_choice
  
label chp3_choice:

    "Curiosity wins. I nod once, giving him the okay."

    show Albion_SC with dissolve

    "Albion's brows pinch together, but he points to where I sit by the windows."
    al "She's right over there."

    hide Albion_SC with dissolve
    show voiced with dissolve
    "The stranger follows the direction of Albion's finger. When our eyes meet I see a split second of shock cross over the figure's face."
    voice "<from 41 to 43>audio/Caelan/Caelan_intro.ogg" 
    who "...Thank you."
    asidesa2 "(I can't think of anyone who'd be looking for me. Which only makes me more curious.)" 
    
    show Caelan2 with dissolve

    voice "<from 3 to 5>audio/Astra/astra_prologue_3.ogg"       
    aside2 "Hello."
    "Their clothes are oddly ornate and formal. An outfit of gold chains, delicate details, and smooth lines."
    aside2 "(I wonder why they're so dressed up.)"

    hide Caelan2
    show Caelan_ST2 
    with dissolve

    voice "<from 45 to 47>audio/Caelan/Caelan_intro.ogg" 
    who "You are Astra?"
    voice "<from 13.3 to 15>audio/Astra/astra_prologue_3.ogg" 
    aside2 "The one and only."

    hide Caelan_ST2
    show Caelan_C2
    with dissolve

    voice "<from 51.7 to 54.2>audio/Caelan/Caelan_intro.ogg" 
    who "...You are the only 'Astra' in Feldoria?"
    voice "<from 17 to 24.9>audio/Astra/astra_prologue_3.ogg" 
    asidesh2 "Oh, well, probably not. I— It's just a figure of speech."
    voice "<from 55 to 57>audio/Caelan/Caelan_intro.ogg" 
    who "I see."
    voice "<from 35.3 to 43>audio/Astra/astra_prologue_3.ogg" 
    aside2 "So… can I help you? How do you know my name?"
    
    hide Caelan_C2
    show Caelan_B2
    with dissolve

    voice "<from 59 to 62>audio/Caelan/Caelan_intro.ogg" 
    who "Yes. I suppose that would be jarring."

    hide Caelan_B2
    show Caelan_ST2
    with dissolve

    voice "<from 66 to 70>audio/Caelan/Caelan_intro.ogg" 
    who "One of my nymphs came here recently. Nimue."
    asidesa2 "(One of {i}their{/i} nymphs?)"
    voice "<from 59 to 66>audio/Astra/astra_prologue_3.ogg" 
    asidesp2 "Nimue… Ah! Yes, the Naiad. I remember now." 
    voice "<from 78.2 to 83>audio/Caelan/Caelan_intro.ogg" 
    who "She told me that you were the one responsible for my offering."
    voice "<from 67 to 72>audio/Astra/astra_prologue_3.ogg" 
    asidesp2 "Your… offering?"
    voice "<from 83 to 89.5>audio/Caelan/Caelan_intro.ogg"  
    who "A 'gift' she calls it. But an offering nonetheless."
    "Suddenly, it clicks."
    voice "<from 78 to 81>audio/Astra/astra_prologue_3.ogg" 
    asidee2 "You must be the friend she told me about!"

    hide Caelan_ST2
    show Caelan_B2
    with dissolve

    voice "<from 96 to 99>audio/Caelan/Caelan_intro.ogg"  
    who "...Ah—yes."
    voice "<from 84.9 to 92>audio/Astra/astra_prologue_3.ogg" 
    asidee2 "If you're here, that must mean you liked it, right? The 'offering'."
    voice "<from 99 to 110>audio/Astra/astra_prologue_3.ogg" 
    asidesh2 "At least, I hope that you liked it… I guess you could be here to tell me how terrible it was."
    voice "<from 103 to 107>audio/Caelan/Caelan_intro.ogg"  
    who "...It was delicious. The croissant as well."
    voice "<from 117 to 120>audio/Caelan/Caelan_intro.ogg"  
    who "I came to thank you in person." 
    voice "<from 119 to 124>audio/Astra/astra_prologue_3.ogg" 
    aside2 "Oh. That's… nice of you."

    hide Caelan_B2
    show Caelan2
    with dissolve

    voice "<from 121 to 125>audio/Caelan/Caelan_intro.ogg"  
    who "The flavors were just like something I used to have many years ago."
    voice "<from 130 to 135>audio/Caelan/Caelan_intro.ogg"  
    who "I… I did not think I would ever taste it again."
    voice "<from 140 to 145>audio/Caelan/Caelan_intro.ogg"  
    who "For that, I thank you. I will remember your kindness, Astra."
    asidesh2 "(They came here just to thank me?)"
    aside2 "(Who is this person?)"
    voice "<from 124 to 133.7>audio/Astra/astra_prologue_3.ogg" 
    asidesp2 "…Well, it's not on the menu, but—if you come back—I'd be happy to make it for you anytime."
    
    hide Caelan2
    show Caelan_EM2
    with dissolve

    voice "<from 154 to 155>audio/Caelan/Caelan_intro.ogg"  
    who "Truly?"
    voice "<from 142.8 to 145.2>audio/Astra/astra_prologue_3.ogg" 
    asidesp2 "Of course! Everyone is welcome here."
    "Even under the shadow of their hood, the smallest of smiles can be made out."
    voice "<from 160 to 165.2>audio/Caelan/Caelan_intro.ogg"  
    who "A kind offer. I will… consider it."
    "They say it with a subtle reverence. Their features are soft and their eyes gleam. It's not the kind of gaze I'd normally expect from a stranger."

    hide Caelan_EM2
    show Caelan2
    with dissolve

    voice "<from 173 to 176>audio/Caelan/Caelan_intro.ogg"  
    who "I must go now, thank you. Again."
    "And without lingering, the stranger turns away. As they leave, I catch a whiff of lavender." 
    
    hide voiced
    hide Caelan2 
    with dissolve
    
    asidesh2 "(Halis really does attract people from all over the country, huh?)"
    "My gaze flickers over to Albion who looks away sharply. Not that he'd admit it, but he was probably watching to make sure nothing happened." 
    
    show Albion_SC with dissolve
    
    al "Break time's over. Get back over here."
    asidesp2 "Coming!" 

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "city_day.ogg" fadeout 2.0 fadein 2.0
    scene sky with dissolve

    "The next few days are uneventful. Work proceeds as smoothly as ever, though the question of what plan I should choose plagues nearly every waking moment."
    "For the moment, I lay in the grass of Halis' largest park, staring at the sky."  
    asidesa "…What should I do?"
    who "Silver for your thoughts?"

    play sfx "shake.ogg"
    show market with vpunch

    asidesp "Ah—!"
    "A low voice chuckles behind me, startlingly familiar. Propping myself up on an elbow reveals a friendly face."  
    
    show market 
    show Felix 
    with dissolve
    
    f "Hey. Astra, right?"
    aside "Yeah. And you're Felix."
    f "Good memory."
    asidesp "What are you doing here?"
    "He shifts, lifting up the small easel and canvas he carries with him."
    f "Painting. What are {i}you{/i} doing?"

    scene sky 
    with vpunch

    "I sigh, flopping back onto the grass dramatically."
    asidesh "Thinking."
    "Felix hums quietly."
    f "Need someone to hear you out?"
    asidesm "…Are you offering?"
    f "I am. So long as you don't mind me multitasking."
    "I can't see Felix with the way I'm splayed out, but I can hear the rustling of bags and clacking of wood as he presumably sets himself up to paint."
    aside "I don't mind."
    f "Great! Then— I'm listening."
    asidesa "(Where to start…)"
    aside "Well. I'm a barista at a place called Café Bloom. The owner wants to breathe some new life into the place."
    f "A coffee enthusiast?"
    asidesm "More than most."
    f "Interesting. Alright, go on."
    aside "She laid out three options, each with their own perks."
    asidesh "The problem is, she asked {i}me{/i} to decide which of the three to go with."
    f "Sounds like she trusts you."
    aside "Yeah. That's what I keep telling myself. But, I have no clue how I'm supposed to choose."
    asidesp "Any one of them would be good for business."
    asidesh "They're all great… I wish I could just choose them all."
    f "Bigger isn't always better… I learned that the hard way." 
    asidesp "Exactly! That's the other problem. I really want this to work. I always give one-hundred percent you know? At least, I try to."
    asidesp "I want to do it all, but I don't want to crash and burn either."
    "I fall silent, letting the words hang in the air."
    f "…Have you tried making your own plan?"
    aside "My own plan?"
    asidesp "But— Sylphia, the owner, only gave me three options."
    f "Yeah, but surely you could make your own plan. One that incorporates all three ideas {i}without{/i} being unrealistic." 
    asidesa "…"
    asidesh "(Oh. Is it that simple?)"
    "I turn the suggestion over in my mind. A plan that's the best of all three options…. Would Sylphia really go for that?"
    "…"
    asidesm "(Only one way to find out.)"
    aside "Huh. You might be onto something there. I suppose it's worth a shot." 
    
    scene market with dissolve

    "I stand up suddenly and dust the grass off of my clothes with determination."

    show Felix with dissolve

    asidesp "Thanks Felix! I really needed that."
    "Felix grins brightly."
    f "No worries!"
    "This new idea fills me with a fresh burst of energy. The possibilities flood my mind and my hand itches to grab and pen."
    "Unfortunately, my notebook is at home."
    asidesp "Sorry, Felix. I have to go— Good luck with your painting!"
    f "See you around, Astra! Careful on your way back!"

    hide Felix with dissolve

    "My hand raises in acknowledgement as I dash back to my apartment, unwilling to let my motivation escape before I can write down my rush of ideas."

    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0
    scene kitchen with dissolve

    "I practically tumble into the apartment, startling Qwynn from their place at the kitchen island."
    
    show Qwynn_N3 at half_size 

    q "Saints—! You okay, Aste?"
    asidee "Fine! I just really need my notebook—" 
    asidee "I've had an epiphany!"
    "The smile that splits my face is so wide, I know I must look half crazed. Still, I can't help it."
    "Already Qwynn is reaching for the leather bound book which happened to be lying nearby."
    
    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve
    
    q "Here you go."
    aside "Thanks."

    hide Qwynn_S with dissolve

    "I slip into the seat next to theirs. From there, no time is wasted in scribbling down pro-con lists and vague logistics."
   
    show Qwynn_S at half_size with dissolve

    q "Woah, you weren't kidding. Is this for Bloom?"

    hide Qwynn_S with dissolve

    asidee "Yep! I was agonizing over which plan to go with when I ran into someone who suggested I make my own plan."
    asidee "I want to combine all three of Sylphia's plans into one—what do you think?"
    
    show Qwynn_S at half_size with dissolve
    
    "I pause my frantic writing to glance over at Qwynn."
    q "It's very you."
    asidesh "Is that a good thing?"
    q "The best. I'm sure Sylphia will accept it."
    asidesp "I hope so!"
    "Qwynn leans over abruptly, pulling me into an embrace."

    hide Qwynn_S
    show Qwynn_S:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    q "She will— No one can resist you when you're this passionate."
    "They pull back and gesture at themselves."
    
    hide Qwynn_S
    show qcutin1 with easeinleft
    
    q "Exhibit A."

    hide qcutin1 with easeoutright

    asidesh "I'm just following my heart."
    
    show Qwynn_S at half_size with dissolve

    q "That's a bigger strength than you realize, Aste. Not everyone can do that."
    "My eyebrows furrow at Qwynn's admission. Not because of what they said, but because of the look on their face when they did."
    "I open my mouth to question them just as they exclaim suddenly."
    q "Oh! I almost forgot. I heard some more rumors today!"
    asidesm "‘Heard' or eavesdropped?"
    "Qwynn waves their hand dismissively."

    hide Qwynn_S
    show Qwynn_N3 at half_size 
    with dissolve

    q "I just happened to be nearby, besides, it wasn't personal information. It was about our elusive Saint. Seems they were spotted in the city again."
    asidea "People say that all the time, Qwynn. There's a ‘Saint Caelan sighting' every few months or so, but never any proof."
   
    hide Qwynn_N3 
    show Qwynn_S at half_size 
    with dissolve
   
    q "You're right. But the traveler in me can't help but hope. I have so many questions about dragon culture!" 
    asidesm "You'd be more likely to catch a glimpse of the Saints in Sholair or Valanche."
    q "Even so, I believe one day our Saint will appear. Hopefully in my lifetime."
    aside "For your sake, I hope that's true."

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadein 2.0
    scene cafe_interior with dissolve

    "Albion works quietly next to me. The hiss of machines, and the idle chatter of customers floats through the air gently."
    "It's peaceful. For now."

    show Albion with dissolve

    asidesp2 "Hey, Albion."
    al "Hm."
    asidesp2 "About the plans for the café—"

    hide Albion
    show Albion_SC 
    with dissolve

    al "This again? Astra, I really don't want to talk about it."
    asidea2 "Why?"
    al "Because things are fine as is. I don't understand why we need to expand."
    asidesh2 "We're not necessarily expanding… just making a few adjustments."
    al "And what happens when you make so many 'adjustments' that the original is lost?"
    "There it is. I feel like I've scratched the surface of Albion's hesitation."
    asidesp2 "The people are ones who make this place what it is. All Sylphia and I want is to open these doors to a wider community."
    al "..."
    aside2 "At least let me tell you my idea?"
    al "Fine."

    hide Albion_SC with easeoutleft

    "The hissing of the machine in front of Albion stops, and he moves to grab the waiting mug."
    
    show Albion with easeinleft

    "He's listening."
    asidesp2 "Sylphia proposed three options."

    hide Albion
    show Albion_SC 
    with dissolve

    al "She told me that much. Get to the point."
    aside2 "Right, well, I want to take something from each of them."
    "His movements pause. Then resume as if nothing is wrong."
    al "...Great."
    asidesp2 "It {i}is{/i} great. At least, I hope so. It's not some grand scheme like you think."
    al "Then what is it?"
    asidesp2 "It's how we all win. The changes are small, concentrated in three key areas."
    aside2 "We start marketing, have a mural painted, and tweak our menu."
    aside2 "We're not uprooting anything."
    "Albion puts the finishing touches on the cappuccino before serving it up. As soon as it hits the countertop, he turns to me with his arms crossed."
    
    hide Albion_SC
    show Albion
    with dissolve

    al "Have you told Sylphia?"
    asidesh2 "...Not yet. I wanted to gather some more opinions."
    "He sighs heavily, and his eyes shut. My stomach drops."
    asidesa2 "You hate it."
    al "No… It's not terrible."
    asidee2 "Really?!" 
    "From Albion, 'not terrible' actually meant 'good'. It's the final vote of confidence that I need. The timing is perfect. Since tomorrow is the day I'm supposed to have an answer for Sylphia."
    asidee2 "Thank you!"

    hide Albion
    show Albion_SC
    with dissolve

    stop ambient fadeout 3.0
    al "Yeah, yeah. Are you done now? We're still on the clock."

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0 
    scene cafe_interior_evening with dissolve

    "The next day, Sylphia pulls me aside to ask for updates about the development plan."
    
    show Sylphia with dissolve

    s "Astra? Do you have a moment?"
    "Sylphia sits at the bar facing me. The café is empty, outside of Sylphia and myself, so her question isn't really necessary, but I answer it anyway."
    asidesp2 "Of course!"
    s "About what we discussed… It's time to make your choice—I want to hear what you think."
    "My heart skips a beat."
    s "As it was before, the first option is to focus on our menu. Add seasonal treats, new items, new coffees. Something to keep customers excited every time they visit."
    s "The second option is to turn the café into more of a community space. We could host events, bring in local artists, create something alive and ever-changing."
    s "And finally... we could focus on marketing. Renovations, a stronger identity, and come up with something that makes us stand out from every other café in the district. A bold step forward."
    "My heart quickens. Three choices, each carrying its own weight. I glance back at Sylphia, who watches me with quiet patience."
    s "So, Astra... which vision speaks to you?"
    
    hide Sylphia with dissolve

#ROUTE CHOICE #3 

    menu:
        "Now's the time to present my idea." if persistent.qwynn_route_unlocked == True:
            $ route = 'caelan'
            $ caelan_pts += 20
            show screen choice_indicator(CAELAN_COLOR) 
            aside2 "Actually— I was hoping you'd allow me to propose a fourth option."
            show Sylphia with dissolve           
            s "Oh? Sure, go ahead. I'd love to hear it."
            aside2 "Well, I was thinking… All of the options are great. Why don't we combine them together?"
            "Sylphia raises an eyebrow, but doesn't interrupt."
            asidesp2 "For the menu, we create one signature drink that embodies our café. To cultivate community, we have a local artist paint a mural. And to spread the word, we solidify our branding and promote Café Bloom that way."
            asidesh2 "Something from each, but still attainable in scope."
            hide Sylphia with dissolve            
            "I chew on my bottom lip nervously. The sting distracts me from the pounding of my heart just enough to focus."
            "What is probably only a brief pause feels like it stretches on forever."
            show Sylphia with dissolve            
            "Finally, Sylphia breaks into a grin."
            s "I like it! It's just like you to try and do it all."
            "I exhale, letting out all my anxiety with it."
            aside2 "Thank you, Sylphia. For always trusting me."
            "Her gaze softens."
            s "Anytime, Astra."
            hide Sylphia with dissolve
            jump Caelan_chp1

        "I should stick to one of Sylphia's plans.":
            jump route_select2

label route_select2:
    menu:
        "Focus on adding new menu items and seasonal treats.":
            $ route = 'albion'
            $ albion_pts += 10
            show screen choice_indicator()
            asidesp2 "Let's focus on the menu. New items, seasonal treats, the works."
            show Sylphia with dissolve
            s "Very well. We'll make Bloom taste brand new!"
            hide Sylphia with dissolve
            jump Albion_chp1

        "Focus on creating a community space/artist gallery in the café":
            $ route = 'felix'
            $ felix_pts += 10
            show screen choice_indicator(FELIX_COLOR) 
            asidesp2 "I want Bloom to become a community space... to bring in local artists and keep it lively."
            show Sylphia with dissolve
            s "Bold, I like it! I'll reach out to a few contacts."
            hide Sylphia with dissolve
            jump Felix_chp1

        "Focus on marketing the café." if persistent.qwynn_route_unlocked == True and persistent.bracelet == True:
            $ route = 'qwynn'
            $ qwynn_pts += 10
            show screen choice_indicator(QWYNN_COLOR) 
            asidesp2 "Let's focus on marketing the café. If Bloom's going to grow, people need to know about it."
            show Sylphia with dissolve
            s "A sensible approach! We'll need to make Bloom stand out from the rest."
            asidesh2 "(I know someone who might know a thing or two about marketing...)"
            hide Sylphia with dissolve
            jump Qwynn_chp1
