# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



#########################################
# CAELAN ENDING
#########################################

label caelan_good:
  
    window hide
    show caelan_good with squares
    window auto
    pause (2.0)


    play music "Caelan.ogg" fadeout 2.0 fadein 2.0
    scene market_night
    show voiced 
    with squares

    $ persistent.status_button = True

    show Caelan_A with dissolve

    "Caelan sighs, and fixes me with a wary look. Like they're waiting for the other shoe to drop."
    
    voice "<from 154 to 157>audio/astra/astra_caelan.ogg"
    asidean "I came back to help people evacuate."
    "I take a step towards them."

    hide Caelan_A
    show Caelan_ST:
        zoom 1.1
        xoffset 550
        yoffset -60
    with dissolve     

    voice "<from 3 to 6>audio/caelan/caelan_good.ogg"
    ca "Very reckless of you."
   
    hide Caelan_ST
    show Caelan_B:
        zoom 1.1
        xoffset 550
        yoffset -60
    with dissolve  

    voice "<from 8 to 10>audio/caelan/caelan_good.ogg"
    ca "...But, thank you."
    voice "<from 10.7 to 15.5>audio/caelan/caelan_good.ogg"
    ca "Things would have been worse if you did not intervene."
    voice "<from 170 to 174.3>audio/astra/astra_caelan.ogg"
    asidesm "You can be really stubborn when you want to be."
    "Another step."

    hide Caelan_B
    show Caelan_EM:
        zoom 1.3
        xoffset 450
        yoffset -60
    with dissolve  

    "They smile."
    a "(Finally.)"
    voice "<from 21 to 23>audio/caelan/caelan_good.ogg"
    ca "I have been told that before."
    "Then it fades."
   
    hide Caelan_EM
    show Caelan_ST:
        zoom 1.3
        xoffset 450
        yoffset -60
    with dissolve  

    voice "<from 31 to 34>audio/caelan/caelan_good.ogg"
    ca "You are still hurt… that is my fault."
    voice "<from 179 to 183>audio/astra/astra_caelan.ogg"
    aside "Not your fault. You didn't know this would happen."
    "Their hands worry at the edge of their cloak."

    hide Caelan_ST
    show Caelan_A:
        zoom 1.3
        xoffset 450
        yoffset -60
    with dissolve  

    voice "<from 36 to 40>audio/caelan/caelan_good.ogg"
    ca "...I truly had no idea."
    voice "<from 183 to 184>audio/astra/astra_caelan.ogg"
    aside "I know."
    "I take another step to fully close the gap between us. Beneath the heavy dampness that hangs in the air I can still faintly smell the soothing lavender scent that always clings to Caelan."

    voice "<from 191 to 195>audio/astra/astra_caelan.ogg"
    asidesh "I think I'm still high on adrenaline."

    #CAELAN POV START

    window hide
    show caelan_pov with squares
    window auto
    pause (2.0)

    play music "tension.ogg" fadeout 2.0 fadein 2.0
    scene forest 
    show voiced
    with squares

    "It smells like ash and cinder. The field of lavender that serves to mark the entrance to the Sanctuary is scorched."
    "Caelan stands at the center of it all, chest heaving."
    "The elemental was calmed. The culprit was caught. Aeris was safe."
    "Yet this doesn't feel like a victory."

    voice "<from 48 to 53>audio/caelan/caelan_good.ogg"
    ca "Aeris… please."
    "She stands with her arms crossed. Her eyes gleam with unshed tears."
    "Caelan arrived before anyone was hurt, but Aeris still witnessed the moment when the flames burst forth. She's shaking."
    "They try to close the gap but for each step forwards, Aeris takes one back."
    "They give up."

    voice "<from 203 to 210>audio/astra/astra_caelan.ogg"
    ae "You said the Sanctuary was safe. You… you promised."
    voice "<from 53 to 58>audio/caelan/caelan_good.ogg"
    ca "I know. Aeris, I am sorry— I did not know—"

    voice "<from 230 to 235>audio/astra/astra_caelan.ogg"
    ae "I came to tell you about my engagement."
    voice "<from 241 to 243>audio/astra/astra_caelan.ogg"
    ae "I bet you knew that, huh?"
    voice "<from 59 to 61>audio/caelan/caelan_good.ogg"
    ca "...I assumed."
    voice "<from 274 to 287>audio/astra/astra_caelan.ogg"
    ae "...I think we can't be friends anymore. I want to start a family soon. I wanted you to be there… but now I think it's too dangerous."
    "In the over three-hundred years they've been alive, they've never felt their heart break so sharply."
    "And there was no one to blame but their own inadequacy."
    "Too small, too weak, too shy, too awkward."
    "All of it led to this moment. To the moment when even their closest friend, the only one who wasn't obligated to serve, chose to leave."
    ca "..."
    "Aeris' tears flow freely now. She sounds just as broken as Caelan feels,"
    voice "<from 289 to 291>audio/astra/astra_caelan.ogg"
    ae "I'm sorry…"
    voice "<from 68 to 69.8 >audio/caelan/caelan_good.ogg"
    ca "I… I understand."
    voice "<from 73.5 to 81>audio/caelan/caelan_good.ogg"
    ca "Congratulations on your engagement, Aeris. You will raise a beautiful family. I am sure of it."
    "She nods."
    voice "<from 294.5 to 296>audio/astra/astra_caelan.ogg"
    ae "Thank you."
    "And then, she leaves. It isn't dramatic or loud. Caelan can barely hear the sound of her walking unceremoniously out of the forest, flanked by two guards."
    "They stand, watching the path she'd disappeared down long after she's gone."
    "NAIAD" "Your Grace—"
    "They interrupt."
    voice "<from 91 to 98>audio/caelan/caelan_good.ogg"
    ca "Tell the council that the Sanctuary is closed. Permanently. We are no longer open to the public."
    "NAIAD" "But, Saint Caelan… what about—"
    voice "<from 115 to 122>audio/caelan/caelan_good.ogg"
    ca "Halis will be safe. We will continue our work with the Sanctuary as our base."
    
    voice "<from 129 to 135>audio/caelan/caelan_good.ogg"
    ca "My appearances have made people bold. They believe I am weaker than the other Saints."
    
    voice "<from 150 to 156>audio/caelan/caelan_good.ogg"
    ca "So, I will stop showing up. People are more afraid of what they can not see."
    "NAIAD" "...Yes, Your Grace." 

    #CAELAN POV END

    window hide
    show astra_pov with squares
    window auto
    pause (2.0)

    play music "Caelan.ogg" fadeout 2.0 fadein 2.0
    scene market_night 
    with squares

    #CAELAN CG HERE

    "Suddenly, I'm pulled into a fierce hug. Caelan presses me close, whispering low so that only I can hear."

    show Caelan_S:
        zoom 1.5
        xoffset 400
        yoffset -60
    with dissolve  

    ca "I am so glad you are okay."
    "My arms wrap around them. The weight of tonight's events crash down on me all at once."
    "We hold each other tightly, uncaring for the people around us."
    "Somewhere though the fog of relief I can faintly make out Qwynn and Albion's voices explaining the situation, subtly taking attention away from me and Caelan."
    aside "(All of this was worth it. Everything was worth it, if it means I get to have this.)"

    scene cafe_interior with dissolve
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadein 2.0

    "The day of the launch party arrives."
    "The scent of coffee fills the air before the doors even open—warm, rich, familiar. Outside, a small crowd has already gathered, their chatter blending with the soft hum of the city."
    "Flowers in soft, pastel tones adorn each table, their petals catching the light from the café windows and casting gentle color across the polished counters and gleaming cups."
    "Tonight's efforts were mainly organized by me. Things like coordinating deliveries and reaching out to other local businesses for collaboration."
    "Sylphia thought it would be a good chance to work on my management skills. She was thrilled when I told her that I wanted to accept her offer." 
    aside2 "(Being here now, I can't imagine a world where I turn her down.)"
    "Things went back to normal pretty shortly after the near disaster last month. Of course, word had gotten out about Caelan's appearance but the excitement died down quickly."
    "The Sanctuary is still off limits to the public. Though Caelan had been making small appearances in the city. Mostly to Café Bloom."
    "I smooth down the front of my apron and glance toward Albion and Sylphia. They stand together near the new display board, ready to welcome people as they come in."
    "The sign reads 'Café Bloom Launch Party' written neatly in chalk, the edges adorned with little coffee beans and sunflowers that Felix helped design."
    "Below the large font, there is a smaller subtitle: {i}Come try our new signature blend!{/i}."
    "Sylphia unlocks the front door, her smile bright and welcoming."
    s "Alright, everyone. Let's make this day one to remember!"
    "The first guests to arrive are familiar faces: our regulars."
    "There's the elderly couple who always share a single slice of cake and two cups of cappuccino; the group of students who fill the corner table with laughter—"
    "—even the dwarven courier who insists on getting his coffee 'to go' but always ends up staying anyway."
    "Felix settles at a table near the mural across from Velvet. Both of them are smiling wide enough to make my own cheeks twinge in empathy."
    "Each customer greets us warmly, their eyes wide as they see all the new changes."
    cus "Ooh, this smells amazing! You've outdone yourself this time, Sylphia."
    
    show Sylphia with dissolve  
    
    s "Thank you~ But all credit goes to my team."
    "She gestures toward us, and for a moment, the café feels alive in a way that words can't quite capture. It is full of chatter, clinking cups, and the comforting rhythm of brewing coffee."
        
    hide Sylphia with dissolve
    
    "Somewhere between brewing and plating desserts, a familiar voice calls from the doorway."

    show Qwynn_S at half_size with dissolve

    q "Hey, superstar! Look at this place! It's incredible."
    asidee2 "Qwynn! You made it!"
    q "Wouldn't miss it for the world. You pulled this off, huh?"
    aside2 "We all did. Here. Our signature blend, in latte form. On the house."
    q "Oh, dangerous. You trust me with this?"
    aside2 "You deserve it. As thanks for all your help."

    hide Qwynn_S with dissolve

    "As more guests arrive, the café hums with life. The lights seem warmer, the air richer with laughter and soft conversation."
    "For a moment, it feels like everything has fallen into place—the culmination of every sleepless night, every trial, every ounce of effort."
    aside2 "(Sylphia was right. The café really did need this.)"

    play audio "<from 0 to 3>bell.mp3"
   
    scene cafe_interior_evening with dissolve
    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0    

    "I watch the party from a quiet corner, needing time to soak everything in, when the door swings open again."
    "In walks Caelan. Not the Saint, just Caelan. I can tell by the way they carry themselves, hesitant and with darting eyes." 
    "They wave politely to people as they move through the room, and I watch in amusement as they do their best to ward off the extra attention."
    "Finally, our eyes meet from across the café. Caelan's shoulders drop in relief." 
    "A few seconds later, they're standing in front of me."
    
    show Caelan_S with dissolve

    ca "Here you are."
    ca "...Are you hiding? I thought that was my thing."
    asidesp "Oh? You make jokes now?"

    hide Caelan_S
    show Caelan_F
    with dissolve

    ca "...Did you like it?"
    aside "Haha, yes Caelan. It was a good one."

    hide Caelan_F
    show Caelan_B
    with dissolve

    #"They blush."

    asidesm "To answer your question, I wanted to watch the party from afar for a minute."

    hide Caelan_B
    show Caelan_S
    with dissolve

    ca "It is wonderful… I can not remember the last time I went to a party."
    ca "I am honored to be a guest at this one."
    asideb2 "And I'm honored to have you."

    stop ambient fadeout 3.0

    window hide
    pause (2.0)
    show black with dissolve

    play music "Caelan.ogg" fadeout 2.0 fadein 2.0
    scene forest 
    show voiced
    with dissolve

    "Caelan and I sit by the Sanctuary's lake. It's summer, but the shade of the forests' trees shield us from the worst of the heat."
    "Caelan was kind enough to offer me an open invitation to the Sanctuary. I'm free to come and go whenever I want."
    "It's become one of my favorite places. After Café Bloom of course."
    "Caelan clears their throat."

    show Caelan_EM:
        zoom 1.4
        xoffset 450
        yoffset -60
    with dissolve  

    voice "<from 6 to 12>audio/caelan/caelan_good2.ogg" 
    ca "I have been thinking… it is not a sure thing but—"
    voice "<from 22 to 25>audio/caelan/caelan_good2.ogg" 
    ca "Perhaps I should open the Sanctuary again."
    "I lean back to stare at them incredulously."

    voice "<from 299 to 301>audio/astra/astra_caelan.ogg" 
    asidesp "Seriously?"

    hide Caelan_EM
    show Caelan:
        zoom 1.4
        xoffset 450
        yoffset -60
    with dissolve  

    voice "<from 27 to 32.5>audio/caelan/caelan_good2.ogg" 
    ca "Yes… I think I was wrong to hide myself away before."

    hide Caelan
    show Caelan_A:
        zoom 1.4
        xoffset 450
        yoffset -60
    with dissolve  

    voice "<from 46 to 53.9>audio/caelan/caelan_good2.ogg" 
    ca "I have missed seeing the people of Halis up close. Even though I am still unsure of how to act around them."
    voice "<from 55 to 61>audio/caelan/caelan_good2.ogg" 
    ca "I am not like the other Saints. I fear I do not live up to their expectations."
    "I can't help but laugh."

    hide Caelan_A
    show Caelan_B:
        zoom 1.4
        xoffset 450
        yoffset -60
    with dissolve  

    voice "<from 306 to 318>audio/astra/astra_caelan.ogg" 
    aside "Caelan, the papers are always talking about you. Every time you set foot in the city, there are at least a dozen reporters hovering, hanging on your every word."
    voice "<from 337 to 340>audio/astra/astra_caelan.ogg" 
    asidesm "You just don't notice because you're always staring at your feet."

    hide Caelan_B
    show Caelan_EM:
        zoom 1.4
        xoffset 450
        yoffset -60
    with dissolve  


    voice "<from 69 to 74>audio/caelan/caelan_good2.ogg" 
    ca "I am… observing the state of the city streets. Making sure no repairs are needed."
    voice "<from 347 to 350>audio/astra/astra_caelan.ogg" 
    asidesm "Uh huh. Sure."
    "..."
    "I shift closer, leaning my head against their shoulder."

    voice "<from 353 to 358>audio/astra/astra_caelan.ogg" 
    aside "What did you say to me before? When I was worried about managing Bloom?"

    hide Caelan_EM
    show Caelan_F:
        zoom 1.4
        xoffset 450
        yoffset -60
    with dissolve  

    voice "<from 89 to 91.6>audio/caelan/caelan_good2.ogg" 
    ca "I… do not remember."

    voice "<from 370 to 374>audio/astra/astra_caelan.ogg" 
    asidesm "You told me to have more faith in myself."
    voice "<from 375 to 378>audio/astra/astra_caelan.ogg" 
    asidesm "I think you should follow your own advice."
    voice "<from 382 to 386>audio/astra/astra_caelan.ogg" 
    aside "The people love you, you just need to look up to see it."

    hide Caelan_F
    show Caelan_EM:
        zoom 1.4
        xoffset 450
        yoffset -60
    with dissolve  

    voice "<from 93 to 98>audio/caelan/caelan_good2.ogg" 
    ca "You have become very good at lecturing me."
    voice "<from 394 to 396>audio/astra/astra_caelan.ogg" 
    asidesh "Only when you need it."

    hide Caelan_EM
    show Caelan_S:
        zoom 1.4
        xoffset 450
        yoffset -60
    with dissolve  

    "Caelan shifts to look at me straight on. There's a shine of happiness in their eyes that makes me want to…"

    hide Caelan_S with dissolve

    #CHOICE 

    menu:

        "Kiss them.":
            show black with dissolve
            "I close the distance slowly, giving them more than enough time to pull away."
            "They don't."
            "Our lips meet. It's a soft and gentle thing that changes everything and nothing at all."
            scene forest with dissolve
            show Caelan_EM:
                zoom 1.5
                xoffset 450
                yoffset -60
            with dissolve  
            voice "<from 102 to 106>audio/caelan/caelan_good2.ogg" 
            ca "Thank you… for staying."
            voice "<from 400 to 404>audio/astra/astra_caelan.ogg" 
            asideb "I'll be here as long as you'll have me."
            "They rest a cold palm on my cheek."
            hide Caelan_EM
            show Caelan_S:
                zoom 1.5
                xoffset 450
                yoffset -60
            with dissolve        
            voice "<from 116 to 119>audio/caelan/caelan_good2.ogg"      
            ca "What if I say 'forever'?"
            "I giggle."
            voice "<from 404 to 408>audio/astra/astra_caelan.ogg" 
            asideeb "Then forever it is."

        "Hug them.":
                "I wrap my arms around them in a tight hug, using all of my strength as if that alone will be enough to convey how much I appreciate them."
                "They return the gesture, and I can feel their grin stretch along the side of my cheek."
                show Caelan_S:
                    zoom 1.5
                    xoffset 450
                    yoffset -60
                with dissolve       
                voice "<from 122 to 125>audio/caelan/caelan_good2.ogg"               
                ca "Thank you… for staying."
                voice "<from 412 to 417>audio/astra/astra_caelan.ogg" 
                aside "That's what friends are for. I'm not so easy to get rid of."
                voice "<from 131 to 133>audio/caelan/caelan_good2.ogg"  
                ca "Good."
                "We stay like that for a long time. Content just to hold one another under the encompassing warmth of the sun." 

    window hide
    $ renpy.pause (2.0)

    stop music fadeout 3.0

    play sfx "sfx_watermagic.ogg"

    window hide
    pause (1.0)
    show endcard_night with dissolve
    $ renpy.pause(5.0)

    # This ends the game.

    return
    

#########################################
# BAD END
#########################################


label caelan_bad:
  
    window hide
    show caelan_bad with squares
    window auto
    pause (2.0)


    play music "tension.ogg" fadeout 2.0 fadein 2.0
    scene market_night with squares

    $ persistent.status_button = True


    "Caelan steps up to me. Their eyes are bright and glossy." 

    show Caelan_ST with dissolve

    ca "You put yourself in danger even when I asked you not to!" 
    asidesp "(Huh?)"
    asidean "I was helping! You couldn't handle it, Caelan."
    ca "I had it under control."
    ca "I have been protecting this city for {i}hundreds{/i} of years, Astra."
    ca "I—"
    "They sigh"

    hide Caelan_ST
    show Caelan_A
    with dissolve

    ca "I can not do this again."
    asidea "What part?"

    hide Caelan_A
    show Caelan_ST
    with dissolve

    ca "...All of it."
    ca "It was a mistake to reveal myself to you. Getting involved with the people of the city—it only leads to nights like this one."
    "My eyes prickle with tears. I was expecting something a bit less accusational after everything that happened."
    asidean "What did you want me to do then? Leave you there?!"
    ca "Yes!"
    asidea "..."
    ca "I—"
    ca "Apologies."

    hide Caelan_ST
    show Caelan_A
    with dissolve

    "I shrug. No longer caring about their excuses."
    ca "You were hurt because of me. I will… ask Nimue to make sure all of your expenses are covered."
    asidea "...So you're leaving. Disappearing again?"

    hide Caelan_A
    show Caelan_ST
    with dissolve

    ca "Those smugglers are still active. This will not be their final attempt to cause chaos."
    ca "I will continue to protect Halis. Like always. I was not careful enough this time."
    ca "I will make sure this does not happen again." 
    "Caelan scans the crowd. After making eye contact with every individual, they shift into their dragon form and launch into the sky."

    hide Caelan_ST with dissolve

    "In any other situation, seeing their true form would be exciting. Now it only fills me with the cold sting of regret."
    asidesa "(Where did I go wrong?)"

    scene cafe_interior with dissolve
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadein 2.0

    "The day of the launch party arrives."
    "The scent of coffee fills the air before the doors even open—warm, rich, familiar. Outside, a small crowd has already gathered, their chatter blending with the soft hum of the city."
    "Flowers in soft, pastel tones adorn each table, their petals catching the light from the café windows and casting gentle color across the polished counters and gleaming cups."
    "Tonight's efforts were mainly organized by me. Things like coordinating deliveries and reaching out to other local businesses for collaboration."
    "Sylphia thought it would be a good chance to work on my management skills. She was thrilled when I told her that I wanted to accept her offer." 
    aside2 "(Being here now, I can't imagine a world where I turn her down.)"
    "Things went back to normal pretty shortly after the near disaster last month. Of course, word had gotten out about Caelan's appearance but the excitement died down quickly."
    "The Sanctuary was still off limits to the public. The Saint was being careful, even more so than before. News of a smuggling ring being dismantled hit the papers only a couple weeks after the last incident."
    "There wasn't a single mention of Saint Caelan being behind it, but I knew the truth."
    "I shake my head."
    asidesa2 "(Tonight is about Bloom.)"
    "I smooth down the front of my apron and glance toward Albion and Sylphia. They stand together near the new display board, ready to welcome people as they come in."
    "The sign reads 'Café Bloom Launch Party' written neatly in chalk, the edges adorned with little coffee beans and sunflowers that Felix helped design."
    "Below the large font, there is a smaller subtitle: {i}Come try our new signature blend!{/i}."
    "Sylphia unlocks the front door, her smile bright and welcoming."
    s "Alright, everyone. Let's make this day one to remember!"
    "The first guests to arrive are familiar faces: our regulars."
    "There's the elderly couple who always share a single slice of cake and two cups of cappuccino; the group of students who fill the corner table with laughter—"
    "—even the dwarven courier who insists on getting his coffee 'to go' but always ends up staying anyway."
    "Felix settles at a table near the mural across from Velvet. Both of them are smiling wide enough to make my own cheeks twinge in empathy."
    "Each customer greets us warmly, their eyes wide as they see all the new changes."
    cus "Ooh, this smells amazing! You've outdone yourself this time, Sylphia."
    
    show Sylphia with dissolve  
    
    s "Thank you~ But all credit goes to my team."
    "She gestures toward us, and for a moment, the café feels alive in a way that words can't quite capture. It is full of chatter, clinking cups, and the comforting rhythm of brewing coffee."
    
    hide Sylphia with dissolve
  
    "Somewhere between brewing and plating desserts, a familiar voice calls from the doorway."

    show Qwynn_S at half_size with dissolve

    q "Hey, superstar! Look at this place! It's incredible."
    asidee2 "Qwynn! You made it!"
    q "Wouldn't miss it for the world. You pulled this off, huh?"
    aside2 "We all did. Here. Our signature blend, in latte form. On the house."
    q "Oh, dangerous. You trust me with this?"
    aside2 "You deserve it. As thanks for all your help."

    hide Qwynn_S with dissolve

    "As more guests arrive, the café hums with life. The lights seem warmer, the air richer with laughter and soft conversation."
    "For a moment, it feels like everything has fallen into place—the culmination of every sleepless night, every trial, every ounce of effort."
    aside2 "(Sylphia was right. The café really did need this.)"
    asidesh2 "(I only wish Caelan would have come to see it.)"

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior_dawn with dissolve

    "Two months pass in the blink of an eye. Sylphia's management training had started as soon as I accepted her offer, and it keeps me plenty busy."
    "For the most part, everything is the same as it was before Caelan stepped through Cafe Bloom's doors."
    "However, now the cafe has more business and a few new faces who are sure to become regulars soon enough."
    "Qwynn, Felix, and I hang out regularly. We go out to different restaurants about every two weeks to catch up. And, sometimes, Albion deigns to join us."
    "Things are going well enough that I can almost forget the flashes of fire and the sound of glass breaking."
    "Then, there are the nights when I can help but to replay the events of that night."
    "Saint Caelan's sudden departure still stung. Understanding why they chose to leave didn't make it hurt any less."

    play audio "<from 0 to 3>bell.mp3"

    asidesh2 "(Not that I have much time to dwell on it anyways.)"

    show Qwynn_S at half_size with dissolve

    q "Miss me?"
    asidesm2 "I saw you an hour ago."
    q "That's not what I asked~"
    "I sigh fondly."
    aside2 "Yes, I missed you, Qwynn."

    hide Qwynn_S with dissolve
   
    play audio "<from 0 to 3>bell.mp3"

    "Felix follows, not too far behind. The sound of the bell ringing again pulls Albion from the break room."

    show Felix at left 
    show Albion_SC at right
    with dissolve

    al "Did I miss something? What are they doing here?"
    f "Good morning, Albion!"
    "I turn to Albion."
    asidesh2 "I'm… actually not sure."
    f "We aren't allowed to get coffee before work?"
    al "{i}You{/i} don't like coffee."

    scene cafe_interior_dawn with dissolve

    "A smile tugs at my lips as I watch the exchange."
    "Bloom is as warm as ever."
    aside2 "(And it will be here, open to all as long I have anything to say about it.)" 
    "That would have to be good enough." 

    play sfx "sfx_watermagic.ogg"

    window hide
    pause (1.0)
    show endcard_night with dissolve
    $ renpy.pause(5.0)

    # This ends the game.

    return
    
