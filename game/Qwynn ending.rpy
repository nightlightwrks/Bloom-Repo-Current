
#########################################
# LAUNCH - GOOD
#########################################    

label qwynn_good:


    window hide
    show qwynn_good with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    play music "Qwynn.ogg" fadeout 2.0 fadein 2.0
    scene market_evening 
    show voiced
    with squares

    "I wriggle from Qwynn's grasp, gently."
    voice "<from 94.1 to 105>audio/astra/astra_qwynn.ogg"
    aside "Thank you for saving us, Qwynn. I'm sorry I let Midna set our apartment on fire."

    show Qwynn_S:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  


    voice "<from 0 to 6.3>audio/qwynn/qwynn_2.ogg"
    q "It's fine! We'll just have to redecorate and fix everything! We can use this as an opportunity to cat-proof our kitchen."
    "A few moments pass as we just look at each other, the loud sound of Water Nymphs bending water to put out the fire behind us."
    "It is a relief to joke to Qwynn like this again, but—"
    voice "<from 119 to 123>audio/astra/astra_qwynn.ogg"
    asidea "Qwynn, we need to talk."

    hide Qwynn_S
    show Qwynn_M:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    "Their shoulders tense."
    voice "<from 130 to 136>audio/astra/astra_qwynn.ogg"
    asidesh "I've wanted to talk to you for a long time now."
    voice "<from 136.5 to 149>audio/astra/astra_qwynn.ogg"
    asideb "And I need to say this, because there's something else I want to tell you, but I can't say that until I get this out of the way first."
    voice "<from 16.5 to 18.3>audio/qwynn/qwynn_2.ogg"
    q "Aste…"
    "Qwynn's eyes quiver as they search mine. They look like they want to run away again."

    hide Qwynn_M
    show Qwynn:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  
    
    "Slowly, they nod."
    voice "<from 168 to 176>audio/astra/astra_qwynn.ogg"
    asideb "You mean so, so much to me, Qwynn. I've always admired you."
    voice "<from 182 to 193>audio/astra/astra_qwynn.ogg"
    asideb "You made me believe someone could build something out of pure passion. I love that when you put your mind to something, you make it happen no matter what."
    voice "<from 213 to 222>audio/astra/astra_qwynn.ogg"
    asidesh "That's why, Qwynn, it really, really hurts to see when you throw all that away… for me."

    hide Qwynn
    show Qwynn_N3:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    voice "<from 19 to 21>audio/qwynn/qwynn_2.ogg"
    q "O-oh."

    voice "<from 21 to 22>audio/qwynn/qwynn_2.ogg"
    q "I—"

    voice "<from 27.8 to 33.8 >audio/qwynn/qwynn_2.ogg"
    q "I thought that was what you wanted. I have to go above and beyond, right? Otherwise—"
    voice "<from 228 to 231>audio/astra/astra_qwynn.ogg"
    aside "I won't like you anymore?"

    hide Qwynn_N3
    show Qwynn_M:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    voice "<from 35.5 to 38>audio/qwynn/qwynn_2.ogg"
    q "Well, yes."
    voice "<from 38 to 42.5>audio/qwynn/qwynn_2.ogg"
    q "You only moved in with me because your parents were moving house..."
    voice "<from 232 to 239>audio/astra/astra_qwynn.ogg"
    aside "That's ridiculous. I moved in with {i}you{/i} because I wanted to live with {i}you{/i}."

    hide Qwynn_M
    show Qwynn_N3:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    voice "<from 56 to 68.8>audio/qwynn/qwynn_2.ogg"
    q "You're the most important person to {i}me{/i}, Aste. But I'm not to {i}you{/i}. You've got Felix, Albion, Sylphia…"
    voice "<from 68.9 to 74.2>audio/qwynn/qwynn_2.ogg"    
    q "I just wanted to be useful to you. I don't want to be the same as—"
    voice "<from 247 to 248.8>audio/astra/astra_qwynn.ogg"
    asidesm "What use is Midna?"
    
    hide Qwynn_N3
    show Qwynn_A:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    voice "<from 79.8 to 80.8>audio/qwynn/qwynn_2.ogg"   
    q "Huh?"

    hide Qwynn_A
    show Qwynn:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    voice "<from 256 to 259>audio/astra/astra_qwynn.ogg"
    asidesm "I said, what use is Midna?"
    "I smile."
    voice "<from 269 to 279>audio/astra/astra_qwynn.ogg"
    aside "All Midna does is eat and sleep and ignore us. She doesn't even pay rent! And she just destroyed our apartment!"
    "Midna drops into a loaf, confirming my words. I give her an affectionate pet, and she nudges her nose into my hand."
    voice "<from 282 to 286>audio/astra/astra_qwynn.ogg"
    asidesm "But we still love her, right?"

    hide Qwynn
    show Qwynn_N3:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    q "…"
    voice "<from 87 to 90.4>audio/qwynn/qwynn_2.ogg"   
    q "Well, I suppose you're right."
    voice "<from 286 to 297>audio/astra/astra_qwynn.ogg"
    aside "And {i}no one{/i} is as important to me as you, Qwynn. Even when you think you don't do anything, you inspire me to move forward."
    voice "<from 308 to 315>audio/astra/astra_qwynn.ogg"
    asideeb "You inspired me to apply for Bloom. You changed my life."
    voice "<from 334.3 to 337.3>audio/astra/astra_qwynn.ogg"
    asideb "That's why I fell in love with you."

    hide Qwynn_N3
    show Qwynn_B:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    "Qwynn goes completely silent. Their mouth is slightly open, and they're shaking a little."
    "Then… they burst into tears."

    hide Qwynn_B
    show Qwynn_S:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    voice "<from 92 to 94.3>audio/qwynn/qwynn_2.ogg"   
    q "Oh, Astra—!"

    hide Qwynn_S with dissolve
    scene qwynncg2 
    show voiced
    with dissolve
    $ persistent.qwynn2 = True

    "I pull them into my arms as they begin to cry."
    voice "<from 102 to 106>audio/qwynn/qwynn_2.ogg"   
    q "I love you too. I love you, Astra…"
    voice "<from 106 to 113>audio/qwynn/qwynn_2.ogg"   
    q "I'm so sorry, I thought you'd never return my feelings! I love you so much."

    hide Qwynn_S with dissolve

    "I let them sob against my shoulder. We stay like that for a long time."

    scene market_evening with dissolve

    "They pull back just enough to look at me again, eyes searching mine, asking a question without words."

    show Qwynn_B:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    "I take Qwynn's face in my hands and kiss them on the lips."

    show black with dissolve

    "Everything changes in that moment."
    "Best friends don't kiss. We've crossed a line, ended something so something new can begin in its place."
    "Something new and beautiful and just a bit scary for both of us."

    scene cafe_interior with dissolve
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadein 2.0

    "The day of the launch party arrives."
    "The scent of coffee fills the air before the doors even open—warm, rich, familiar. Outside, a small crowd has already gathered, their chatter blending with the soft hum of the city."
    "Flowers in soft, pastel tones adorn each table, their petals catching the light from the café windows and casting gentle color across the polished counters and gleaming cups."
    "Cortado is everywhere. We've put him on the menus and posters, and made little Cortado plush toys to put on the tables. Albion and I even learnt how to make latte art in the shape of Cortado."
    "Sylphia unlocks the front door, her smile bright and welcoming."
    
    show Sylphia with dissolve

    s "Alright, everyone. Let's make this day one to remember!"

    hide Sylphia with dissolve

    "The first guests to arrive are familiar faces: our regulars."
    "There's the elderly couple who always share a single slice of cake and two cups of cappuccino; the group of students who fill the corner table with laughter—" 
    "—even the dwarven courier who insists on getting his coffee 'to go' but always ends up staying anyway."
    "Each customer greets us warmly, their eyes wide as they see the new display of desserts and the menu highlighting the signature blend."
    cus "Ooh, this smells amazing! You've outdone yourself this time, Sylphia."
   
    show Sylphia with dissolve  
    
    s "Thank you~ But all credit goes to my team."
    "She gestures toward us, and for a moment, the café feels alive in a way that words can't quite capture. It is full of chatter, clinking cups, and the comforting rhythm of brewing coffee."
    
    hide Sylphia with dissolve
   
    "She gestures toward us, and for a moment, the café feels alive in a way that words can't quite capture. It is full of chatter, clinking cups, and the comforting rhythm of brewing coffee."
    "Somewhere between brewing and plating desserts, a familiar voice calls from the doorway."

    show Qwynn_S at half_size with dissolve

    q "Hey, superstar! Look at this place! It's incredible."
    asideb2 "Qwynn! You made it!"
    "My heart flutters. I would've pulled Qwynn into a hug if I didn't have to look professional right now."
    q "Wouldn't miss it for the world. You pulled this off, huh?"
    aside2 "We all did. Here. Bloom's signature blend, on the house."
    q "Oh, dangerous. You trust me with this?"
    "They grab the cream dispenser immediately and start pouring. A splash turns into a stream, and the rich brown coffee lightens with every swirl until it's nearly white."
    asidesm "(Typical Qwynn.)"
    who "Mama, can I have a Cortado?"

    hide Qwynn_S with dissolve

    "I turn to see a little were-folk girl, ears perked, tail swishing hopefully behind her. Her mother's smile is fond but apologetic."
    "WERE-FOLK MOTHER" "Sorry, sweetie. You're still a bit too young for coffee."
    "The girl's shoulders droop. I step forward."
    aside2 "We can make something for you without caffeine, if you like."
    "WERE-FOLK CHILD" "Really?"
    asidesm2 "Of course! How do you feel about... a hot chocolate? With extra foam?"
    "Her ears shoot straight up, eyes sparkling."
    "WERE-FOLK CHILD" "YES! Please!"
    "WERE-FOLK MOTHER" "Thank you, dear."
    aside2 "I'm glad she's excited."
    "Overhearing, Albion sets to work immediately, steaming milk until it's light and fluffy, swirling in melted chocolate, and finishing with a tiny Cortado face drawn in foam. The girl gasps when I hand it over."
    "WERE-FOLK CHILD" "He's so cute!"
    "WERE-FOLK MOTHER" "Make sure to say thank you."
    "WERE-FOLK CHILD" "Thank you, Miss!"
    aside2 "Anytime."
    "Simple, fleeting moments like this are what give Bloom that {i}second home{/i} feeling."
    "As more guests arrive, the café hums with life. The lights seem warmer, the air richer with laughter and soft conversation."
    "For a moment, it feels like everything has fallen into place—the culmination of every sleepless night, every trial, every ounce of effort."
    aside2 "(Sylphia was right. The café really did need this.)"

    stop ambient fadeout 3.0

    scene cafe_interior_evening with dissolve
    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0     
    
    "By the time the launch party winds down, only a handful of guests linger over empty cups."
    "While Sylphia counts the till, Albion and I clear the tables. Qwynn joins without being asked, scooping plates into stacks, wiping down surfaces, working faster than both of us combined."

    play music "city_night.ogg" fadeout 2.0 fadein 2.0
    scene market_evening with dissolve

    "After the last table is cleaned and the lights are dimmed, we step outside. The streets are quiet. Qwynn falls into step beside me."
    
    show Qwynn_S at half_size with dissolve
    
    q "So—"
    asidesm "Ice cream?"
    q "You know it."
    "We walk home together, hand in hand."

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "Qwynn.ogg" fadeout 2.0 fadein 2.0
    scene kitchen 
    show voiced
    with dissolve 

    voice "<from 344 to 347>audio/astra/astra_qwynn.ogg"
    aside "Are you sure these clothes will keep you cool enough?"
    "Qwynn glances up from their half-packed suitcase, holding a blouse in each hand, both equally flashy."
    
    show Qwynn_S at half_size with dissolve

    voice "<from 122 to 128>audio/qwynn/qwynn_2.ogg"
    q "Aste, come on. I've been to Valanche before. If it's too humid, I'll just buy more clothes when I get there."
    "They toss a one-piece onto the pile and roll another into a neat bundle. The suitcase is already a small mountain of loose blouses, shorts, sketchbooks, and travel containers."
    
    hide Qwynn_S with dissolve
    
    "Qwynn will be leaving for Valanche tonight for a trip that's long overdue. They'll be gone for three months."
    "It'll be the longest we've been apart since we moved in together. Yet, I'm happy they're doing things for themselves again."
    
    show Qwynn_S at half_size with dissolve

    voice "<from 135 to 137>audio/qwynn/qwynn_2.ogg"
    q "Last chance to fit yourself in the suitcase!"

    voice "<from 358 to 367>audio/astra/astra_qwynn.ogg"
    aside "Sylphia probably wouldn't mind if I took leave… but as I said, someone has to stay behind and watch Midna."
    "Midna loafs nearby with regal disinterest, tail flicking lazily as if she didn't burn down our apartment three weeks ago. She knows the universe bends to her whims."
    
    hide Qwynn_S with dissolve
    
    aside "(And this is Qwynn's trip, Qwynn's opportunity to rediscover who they are without me.)"
    voice "<from 374 to 381>audio/astra/astra_qwynn.ogg"
    asidesm "Plus—if I jumped in there, where would you put all the souvenirs you'll bring back for me?"
    
    show Qwynn_N3 at half_size with dissolve

    voice "<from 143 to 146.7>audio/qwynn/qwynn_2.ogg"
    q "You've never asked for souvenirs before."
    voice "<from 387 to 390>audio/astra/astra_qwynn.ogg"
    asidesm "I'm your girlfriend now. I get more privileges."

    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve

    "They smile so wide it reaches both ears. Affection blooms in my chest."

    voice "<from 395 to 399>audio/astra/astra_qwynn.ogg"
    asideb "I'm really going to miss you, Qwynn."

    hide Qwynn_S with dissolve

    "I sit on the suitcase so they can zip it shut. They tug the zipper smoothly around the edge."

    show Qwynn_S:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  
    
    "Then Qwynn kneels down in front of me and cups my cheeks with both hands."
    voice "<from 149.8 to 152.1>audio/qwynn/qwynn_2.ogg"
    q "Distance makes the heart grow fonder."

    scene black 
    show voiced
    with dissolve

    "They drop a kiss right on my lips."

    scene kitchen 
    show voiced
    with dissolve

    "I breathe out a small laugh when they pull away."

    voice "<from 406 to 411>audio/astra/astra_qwynn.ogg"
    asidesp "You're quoting Felix now? How the tables have turned."

    voice "<from 160 to 166>audio/qwynn/qwynn_2.ogg"
    q "I'm stealing his words. So when you get lunch with him tomorrow, you'll think of me."

    hide Qwynn_S with dissolve

    "I know Qwynn still gets a little jealous when I spend time with other people."
    "Progress doesn't happen overnight."
    "But… they don't let the knife twist anymore. In fact, Qwynn was the one who suggested I spend more time with Felix while they're gone."
    "They rest their forehead against mine, blue eyes sparkling vibrantly."

    show Qwynn_S:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    voice "<from 166.4 to 169.9>audio/qwynn/qwynn_2.ogg"
    q "Do you want to know what Voyage Étoilé really means?"

    voice "<from 415.7 to 418>audio/astra/astra_qwynn.ogg"
    asidesp "The name of your boutique?"

    voice "<from 175 to 180>audio/qwynn/qwynn_2.ogg"
    q "I tell people it means {i}journey{/i} and {i}stars.{/i} My two favorite things."
    voice "<from 187 to 198>audio/qwynn/qwynn_2.ogg"
    q "But the reason I named it that… was because of {i}you{/i}, Astra. You're the star that lights up my life."
    voice "<from 214 to 218.8>audio/qwynn/qwynn_2.ogg"
    q "And no matter where I am in the world, no matter how far apart we are—"
    voice "<from 219 to 224>audio/qwynn/qwynn_2.ogg"
    q "I can look up at the sky, knowing you're somewhere underneath the same sea of stars."
    voice "<from 230 to 232.4>audio/qwynn/qwynn_2.ogg"
    q "I love you... Astra."
    hide voiced with dissolve
    window hide
    $ renpy.pause (2.0)

    stop music fadeout 3.0

    play audio "<from 0 to 3>bell.mp3"

    window hide
    pause (1.0)
    show endcard_night with dissolve
    $ renpy.pause(5.0)

    # This ends the game.

    return


########################################
# BAD END
########################################

label qwynn_bad:

    window hide
    show qwynn_bad with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    #TODO change track
    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0
    scene market_evening with squares

    "I clutch the back of their blouse, fingers curling into the fabric. I don't want to let go."
    asidesp "Qwynn, I was wrong. I was so wrong. I didn't mean to push you away. I'm sorry."

    show Qwynn_B:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve

    q "W-what?"

    hide Qwynn_B with dissolve

    "I promised myself I'd tell them how I feel."
    "But now—looking at their face, flushed and desperate—all that resolve has crumpled."
    "If they rejected me, I'd lose everything... everything I have with them."
    "I need them."
    
    show Qwynn_B:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve
   
    q "...Aste?"

    hide Qwynn_B
    show Qwynn_S:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve

    q "Oh, Astra—I'm so glad you feel this way!"
    q "I didn't want anything to change between us."
    asidean "Nothing will. I wouldn't change a thing for the world. You're my best friend."
    "The words they always say to me—I finally manage to say them back."
    "I couldn't even lift a sofa without them. What was I thinking, that I'd be able to live without them."

    #BAD ENDING: Launch Party

    window hide
    show black with dissolve
    window auto
    pause (2.0)
 
    scene cafe_interior with dissolve
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadein 2.0

    "The day of the launch party arrives."
    "The scent of coffee fills the air before the doors even open—warm, rich, familiar. Outside, a small crowd has already gathered, their chatter blending with the soft hum of the city."
    "Flowers in soft, pastel tones adorn each table, their petals catching the light from the café windows and casting gentle color across the polished counters and gleaming cups."
    "Cortado is everywhere. We've put him on the menus and posters, and made little Cortado plush toys to put on the tables. Albion and I even learnt how to make latte art in the shape of Cortado."
    "Sylphia unlocks the front door, her smile bright and welcoming."
    
    show Sylphia with dissolve

    s "Alright, everyone. Let's make this day one to remember!"

    hide Sylphia with dissolve

    "The first guests to arrive are familiar faces: our regulars."
    "There's the elderly couple who always share a single slice of cake and two cups of cappuccino; the group of students who fill the corner table with laughter—" 
    "—even the dwarven courier who insists on getting his coffee 'to go' but always ends up staying anyway."
    "Each customer greets us warmly, their eyes wide as they see the new display of desserts and the menu highlighting the signature blend."
    cus "Ooh, this smells amazing! You've outdone yourself this time, Sylphia."
   
    show Sylphia with dissolve  
    
    s "Thank you~ But all credit goes to my team."
    "She gestures toward us, and for a moment, the café feels alive in a way that words can't quite capture. It is full of chatter, clinking cups, and the comforting rhythm of brewing coffee."
    
    hide Sylphia with dissolve
   
    "She gestures toward us, and for a moment, the café feels alive in a way that words can't quite capture. It is full of chatter, clinking cups, and the comforting rhythm of brewing coffee."
    "Somewhere between brewing and plating desserts, a familiar voice calls from the doorway."

    show Qwynn_S at half_size with dissolve

    q "Hey, superstar! Look at this place! It's incredible."
    asideb2 "Qwynn! You made it!"
    "My heart flutters. I would've pulled Qwynn into a hug if I didn't have to look professional right now."
    q "Wouldn't miss it for the world. You pulled this off, huh?"
    aside2 "We all did. Here. Bloom's signature blend, on the house."
    q "Oh, dangerous. You trust me with this?"
    "They grab the cream dispenser immediately and start pouring. A splash turns into a stream, and the rich brown coffee lightens with every swirl until it's nearly white."
    asidesm "(Typical Qwynn.)"
    who "Mama, can I have a Cortado?"

    hide Qwynn_S with dissolve

    "I turn to see a little were-folk girl, ears perked, tail swishing hopefully behind her. Her mother's smile is fond but apologetic."
    "WERE-FOLK MOTHER" "Sorry, sweetie. You're still a bit too young for coffee."
    "The girl's shoulders droop. I step forward."
    aside2 "We can make something for you without caffeine, if you like."
    "WERE-FOLK CHILD" "Really?"
    asidesm2 "Of course! How do you feel about... a hot chocolate? With extra foam?"
    "Her ears shoot straight up, eyes sparkling."
    "WERE-FOLK CHILD" "YES! Please!"
    "WERE-FOLK MOTHER" "Thank you, dear."
    aside2 "I'm glad she's excited."
    "Overhearing, Albion sets to work immediately, steaming milk until it's light and fluffy, swirling in melted chocolate, and finishing with a tiny Cortado face drawn in foam. The girl gasps when I hand it over."
    "WERE-FOLK CHILD" "He's so cute!"
    "WERE-FOLK MOTHER" "Make sure to say thank you."
    "WERE-FOLK CHILD" "Thank you, Miss!"
    aside2 "Anytime."
    "Simple, fleeting moments like this are what give Bloom that {i}second home{/i} feeling."
    "As more guests arrive, the café hums with life. The lights seem warmer, the air richer with laughter and soft conversation."
    "For a moment, it feels like everything has fallen into place—the culmination of every sleepless night, every trial, every ounce of effort."
    aside2 "(Sylphia was right. The café really did need this.)"
    
    stop ambient fadeout 3.0
    
    scene cafe_interior_evening with dissolve
    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0     
    
    "By the time the launch party winds down, only a handful of guests linger over empty cups."
    "While Sylphia counts the till, Albion and I clear the tables. Qwynn joins without being asked, scooping plates into stacks, wiping down surfaces, working faster than both of us combined."

    play music "city_night.ogg" fadeout 2.0 fadein 2.0
    scene market_evening with dissolve

    "After the last table is cleaned and the lights are dimmed, we step outside. The streets are quiet. Qwynn falls into step beside me."
    
    show Qwynn_S at half_size with dissolve
    
    q "So—"
    asidesm "Ice cream?"
    q "You know it."
    "We walk home together, hand in hand."

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0
    scene kitchen_night with dissolve

    "Dinner steams in bowls on the table, scenting the apartment with ginger and cream. Qwynn ladles a bit of sauce over my portion before I can protest."
    "Midna devours her tuna with the enthusiasm of someone who is, frankly, eating better than us."

    show Qwynn_S at half_size with dissolve

    q "So? Be honest. How's the flavour?"
    asidee "It's perfect."
    "They beam, the same way they always do, as if my approval means more than the entire world."
    q "I added a bit of rose water to the appetisers. I'm sorry if you hate them."
    asidesh "(It really doesn't match the dish, but—)"
    asideeb "I'd never hate anything you make."
    "Midna sneezes violently and we both laugh."
    "It's only been three weeks since the fight, but everything feels normal again. Qwynn has fixed or replaced everything that was burnt in the fire."
    q "It's nice, being home this much. Now that Voyage Étoilé runs mostly on part-timers, I finally get to slow down a little."
    
    hide Qwynn_S with dissolve

    "My fork pauses. I think about my days and how they blur into routines built around Qwynn. Waking, eating, walking, cooking, existing together. I barely remember what I used to do with my time."
    "But this is what best friends do... right?"

    show Qwynn_N3 at half_size with dissolve

    q "Aste?"
    "Their voice wavers—too nervous for such a small question."

    hide Qwynn_N3
    show Qwynn at half_size 
    with dissolve

    q "Are you... okay? You looked down for a second."
    asidesp "I'm fine! Just thinking about how good the food is."

    hide Qwynn
    show Qwynn_S at half_size 
    with dissolve

    "Their shoulders relax."
    "Midna hops onto Qwynn's lap, demanding affection. They oblige, laughing as she bumps her head into their chest."
    asidesp "Aww, no fair, Midna! Let me do that too!"

    hide Qwynn_S
    show Qwynn_S:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  

    q "Then come here, Astra."
    "I think about how we've shaped a life so carefully around each other, fitting together so neatly that there's no room for others, no room for anything else."
    "Nothing has to change."

    window hide
    $ renpy.pause (2.0)

    stop music fadeout 3.0

    play audio "<from 0 to 3>bell.mp3"

    window hide
    pause (1.0)
    show endcard_night with dissolve
    $ renpy.pause(5.0)

    # This ends the game.

    return
   