
#########################################
# LAUNCH - GOOD
#########################################    

label albion_good2:


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
    "I smooth down the front of my apron and glance toward Albion." 
    "He's adjusting and readjusting the new display board, the words 'Café Bloom Launch Party' written neatly in chalk, the edges adorned with little coffee beans and sunflowers that a local artist helped design."
    "Below the large font, there is a smaller subtitle: {i}Come try our cinnamon-kissed berry tart with the new signature blend: First Bloom{/i}."
    asideb2 "(Albion looks calm... but I can tell he's nervous too.)"
    "Sylphia unlocks the front door, her smile bright and welcoming."

    show Sylphia with dissolve

    s "Alright, everyone. Let's make this day one to remember!"

    hide Sylphia with dissolve

    "The first guests to arrive are familiar faces: our regulars."
    "There's the elderly couple who always share a single slice of cake and two cups of cappuccino; the group of students who fill the corner table with laughter—" 
    "—even the dwarven courier who insists on getting his coffee 'to go' but always ends up staying anyway."
    "Each customer greets us warmly, their eyes wide as they see the new display of desserts and the menu highlighting the signature blend."
   
    #TODO add silhouette 
    cus "Ooh, this smells amazing! You've outdone yourself this time, Sylphia."

    show Sylphia with dissolve

    s "Thank you~ But all credit goes to my team."
    "She gestures toward us, and for a moment, the café feels alive in a way that words can't quite capture. It is full of chatter, clinking cups, and the comforting rhythm of brewing coffee."
   
    hide Sylphia with dissolve  

    "Somewhere between brewing and plating desserts, a familiar voice calls from the doorway."

    show Qwynn_S at half_size with dissolve

    q "Hey, superstar! Look at this place! It's incredible."
    asidesp2 "Qwynn! You made it!"
    q "Wouldn't miss it for the world. You pulled this off, huh?"
    asidesm2 "We all did. Here. First Bloom, on the house."
    q "Oh, dangerous. You trust me with this?"

    hide Qwynn_S with dissolve

    "They grab the cream dispenser immediately and start pouring. A splash turns into a stream, and the rich brown coffee lightens with every swirl until it's nearly white."
    aside2 "(Typical Qwynn.)"
    "Then the door swings open again, and in strides a familiar, well-dressed Elf, with his sharp suit, polished shoes, and an unmistakably self-satisfied grin."
    
    #TODO add silhouette 
    sf "Ah, Café Bloom! I knew I smelled success from halfway down the street."
    "I can't help but smile."
    aside2 "Welcome back! Are you here for the catering review, or just the free samples?"
    sf "Can't it be both?"
    "He winks before accepting a small plate of pastries and a cup of coffee from Albion. Despite everything, Albion serves him with precision, his movements professional."
    sf "Brilliant as always. Truly, your coffee has no rival."
    "He takes a sip, then leans back, satisfied. I glance at Albion. He nods once in acknowledgement, the faintest hint of pride crossing his features."
    "As more guests arrive, the café hums with life. The lights seem warmer, the air richer with laughter and soft conversation."
    "For a moment, it feels like everything has fallen into place—the culmination of every sleepless night, every trial, every ounce of effort."
    aside2 "(Sylphia was right. The café really did need this.)"
    "I wipe my hands on my apron and turn towards Albion, who's finishing up another pour at the counter. He looks more relaxed today. The usual tension in his shoulders is gone."
    asideb2 "(He's smiling. Just a little... but it's there.)"

    #TODO add footsteps sfx
    "I turn back to restocking the display, trying to hide my own grin. Before I can say anything, I hear his footsteps approaching from behind."
    "He stops just behind me, close enough that I can feel the faint brush of his sleeve against my arm."
    asideeb2 "Albion?"
    "He doesn't answer. My heart skips."
    asideem2 "(Is he going to—? Right here? In the middle of the café?)"
    "He lifts his hand, and I steel myself. Instead, he takes hold of the back of my apron, spins me gently around, and ties the loose ribbon in one smooth motion."
    asidep2 "(He's just tying my apron. Of course he is.)"
    "He gives the ribbon a neat tug, the knot snug and perfectly centred. Then, as he steps back, his fingers brush mine—light, deliberate."
    asideeb2 "(He did that on purpose.)"

    show Albion_H at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve

    "When I glance up, he's already smiling, soft and knowingly, before he turns and walks back toward the counter."
   
    hide Albion_H with dissolve
    show Sylphia with easeinright

    s "You two seem to be working well together these days."
    asideb2 "What? Oh—uh, of course! We're just... just coworkers. That's all."
    s "Really? Because it looked like he was about to kiss you a moment ago."
    "Heat floods my face."
    asideeb2 "O–of course not! We're not— I mean, not officially—"
    "I stop mid-sentence. Right. We never made it official."
    asideb2 "(Wait... does that mean we actually—?)"
    asideeb2 "Let's say, hypothetically, we were. Would that be a problem?"
    s "A problem? Hardly. That would be a breakthrough for him."
    "She chuckles, glancing toward Albion, who's handing a plate of berry tarts to a customer with surprising ease."
    s "If anything, it might even help the café."
    asideeb2 "(Sylphia, please...)"
    "But she just winks at me, her laughter blending with the soft music and chatter of the crowd."

    hide Sylphia with dissolve

    "I let myself laugh too—quietly, freely, without the weight of worry. The café feels brighter than ever."
    asidee2 "(We did it. Together. At last.)"
    stop ambient fadeout 2.0

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "Albion.ogg" fadeout 2.0 fadein 2.0
    scene albionapt_night 
    show voiced
    with dissolve

    "It's late—past closing time, past the hour when either of us should still be awake. The lights in Albion's apartment are low, the air thick with the faint scent of roasted beans and cinnamon clinging to our clothes."
    "We're sitting side by side on the couch, flushed and breathless from the kind of kiss that leaves you dizzy and giddy all at once." 
    "Albion's hair is slightly mussed, and he's breathing a little unevenly, his usual composure replaced by something softer, more human."
    "Right now, neither of us is thinking about ratios, recipes, or roasting times."
    asideem "(He's sitting so close. I can still feel the warmth of his hand on mine.)"
    "The words slip out before I can think twice."

    voice "<from 491.7 to 496>audio/Astra/astra_albion.ogg" 
    asidesp "I like you. Will you go out with me?"

    show Albion_B at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve

    voice "<from 0 to 3>audio/Albion/albion_good2.ogg"
    al "We're doing this out of order."

    voice "<from 503.6 to 509>audio/Astra/astra_albion.ogg" 
    asideb "Oh? What's the proper order, then? Coffee first, then confession?"

    voice "<from 12 to 18>audio/Albion/albion_good2.ogg"
    al "Usually, people go on dates before they…k–kiss."
    "I snicker."

    voice "<from 509.5 to 514>audio/Astra/astra_albion.ogg" 
    asidesm "Getting shy on me now? It's too late for that."

    voice "<from 532 to 536>audio/Astra/astra_albion.ogg" 
    asidesm "We're innovators. We do things differently here."
    "He shakes his head, but he's smiling now. {i}Really{/i} smiling. The kind that softens everything about him."

    hide Albion_B
    show Albion_H at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve

    voice "<from 32 to 38>audio/Albion/albion_good2.ogg"
    al "Then yes. I'd be honored to go out with you."
    "I can't help the grin that spreads across my face."

    voice "<from 536.5 to 542>audio/Astra/astra_albion.ogg" 
    asidep "You make it sound like you're agreeing to a business proposal."

    voice "<from 56 to 58>audio/Albion/albion_good2.ogg"
    al "I'm trying to be thorough."

    voice "<from 550.5 to 552>audio/Astra/astra_albion.ogg" 
    asidesm "Of course you are."
    "He leans back against the couch, his arm brushing against mine. The silence between us feels warm, easy. A week ago, that silence was uncertain, brutal. Now, it feels like home."
    
    hide Albion_H
    show Albion at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve    

    voice "<from 67 to 72>audio/Albion/albion_good2.ogg"
    al "...I've been thinking about something."

    voice "<from 553.8 to 556>audio/Astra/astra_albion.ogg" 
    asidesm "You always are."

    voice "<from 79 to 82>audio/Albion/albion_good2.ogg"
    al "About... the blend."

    voice "<from 559 to 561>audio/Astra/astra_albion.ogg" 
    aside "Our blend."

    voice "<from 93 to 98>audio/Albion/albion_good2.ogg"
    al "Right. Our blend. First Bloom."
    "Hearing him say the name still sends a small thrill through me."

    hide Albion
    show Albion_Shy2 at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve    

    voice "<from 118 to 129>audio/Albion/albion_good2.ogg"
    al "I was worried what we made wouldn't last. That the... balance would fade. But it hasn't."
    asidesh "(It's clear he isn't talking about the blend.)"

    voice "<from 563 to 570>audio/Astra/astra_albion.ogg" 
    aside "Maybe that's because balance isn't something you keep. It's something you keep finding."
    "He hums softly at that, thoughtful. Then, after a moment:"

    voice "<from 135 to 138>audio/Albion/albion_good2.ogg"
    al "I think I'm still finding mine."
    
    voice "<from 580.4 to 582.8>audio/Astra/astra_albion.ogg" 
    asidesm "Good thing I'm here to help."

    hide Albion_Shy2
    show Albion_H at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve    

    "He glances at me, amused, then reaches over to take my hand. His fingers are warm."

    hide Albion_H with dissolve

    "Outside, the city wind brushes against the windowpane, soft and gentle like a lullaby."
    aside "(If this is what imperfection looks like... I wouldn't trade it for anything.)"

    voice "<from 582.6 to 585>audio/Astra/astra_albion.ogg" 
    asidesm "...You have flour on your shirt."

    show Albion_H at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve   

    "He huffs, sending a half-lidded and playful glare in my direction."

    voice "<from 145 to 147.4>audio/Albion/albion_good2.ogg"
    al "And whose fault is that?"

    voice "<from 588 to 590>audio/Astra/astra_albion.ogg" 
    asidesm "Mine, probably."
    "His fingers tighten around mine."
    "I rest my head on his shoulder, and for a long, quiet moment, we just sit there—two people who are finally learning how to stop chasing perfection, and simply be."

    scene black with dissolve

    "The air smells like sugar and coffee again. Ours."

    window hide
    $ renpy.pause (2.0)

    stop music fadeout 3.0

    play audio "<from 0 to 3>bell.mp3"

label end_after:

    window hide
    pause (1.0)
    show endcard_night with dissolve
    $ persistent.qwynn_route_unlocked = True
    $ renpy.pause(5.0)

    # This ends the game.

    return


########################################
# BAD END
########################################

label albion_bad:

    window hide
    show albion_bad with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    scene albionapt_night with squares

    "For a moment, he just watches me. The air between us is still, quiet. Then Albion's eyes lower, his expression closing off again, the softness from before slipping away."
    
    show Albion_N2 with dissolve
    
    al "Astra. I can't."
    asidesp "What? Why not?"

    hide Albion_N2
    show Albion_SC
    with dissolve

    al "Because no matter what I do, it won't be enough. The blend, the café, me—it'll all just fall short."
    "His voice is calm, but there's an ache underneath it that makes my heart drop."
    asidesp "That's not true—"
    al "You don't understand. I've spent my whole life trying to prove that I belong somewhere. That I can make something worthy of staying for. If I stop now—if I let it be imperfect—it means I failed."
    "He looks at me then, and for the first time, I see it clearly: the fear behind his pride."
    asidesh "Albion..."

    hide Albion_SC
    show Albion
    with dissolve

    al "You should focus on your desserts. They're already good as they are."
    "He stands slowly, turning away before I can stop him."
    al "The launch is in a few days. We'll use the desserts we have. I'll... keep trying to make the blend. It'll be fine."

    hide Albion with dissolve

    asidesa "(‘Fine', he says, like it's supposed to mean something. To me… it sounds like giving up.)"
    "He walks toward the kitchen, and the distance between us feels heavier than ever. I stay where I am, staring at the empty space he's left behind."
    asidesa "(You're wrong, Albion. You're enough. You always were. You just can't see it yet.)"
    "I exhale shakily, pushing a hand through my hair."

    
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
    "I smooth down the front of my apron and glance toward Albion." 
    "He's adjusting and readjusting the new display board, the words 'Café Bloom Launch Party' written neatly in chalk, the edges adorned with little coffee beans and sunflowers that a local artist helped design."
    asidesh2 "(Albion looks calm... but I can tell he's nervous too.)"
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

    "Somewhere between brewing and plating desserts, a familiar voice calls from the doorway."

    show Qwynn_S at half_size with dissolve

    q "Hey, superstar! Look at this place! It's incredible."
    asidesp2 "Qwynn! You made it!"
    q "Wouldn't miss it for the world. You pulled this off, huh?"
    asidesm2 "We all did. Here. Bloom's signature blend, on the house."
    q "Oh, dangerous. You trust me with this?"

    hide Qwynn_S with dissolve

    "They grab the cream dispenser immediately and start pouring. A splash turns into a stream, and the rich brown coffee lightens with every swirl until it's nearly white."
    aside2 "(Typical Qwynn.)"
    "Then the door swings open again, and in strides a familiar, well-dressed Elf, with his sharp suit, polished shoes, and an unmistakably self-satisfied grin."
    
    #TODO add silhouette
    sf "Ah, Café Bloom! I knew I smelled success from halfway down the street."
    "I can't help but smile."
    aside2 "Welcome back! Are you here for the catering review, or just the free samples?"
    sf "Can't it be both?"
    "He winks before accepting a small plate of pastries and a cup of coffee from Albion. Despite everything, Albion serves him with precision, his movements professional."
    sf "Brilliant as always. Truly, your coffee has no rival."
    "He takes a sip, then leans back, satisfied. I glance at Albion. He nods once in acknowledgment, the faintest hint of pride crossing his features."
    "As more guests arrive, the café hums with life. The lights seem warmer, the air richer with laughter and soft conversation."
    "For a moment, it feels like everything has fallen into place—the culmination of every sleepless night, every trial, every ounce of effort."
    aside2 "(Sylphia was right. The café really did need this.)"
    "And yet, when I turn to Albion, I notice he's quiet. His eyes are distant, thoughtful. The blend, though delicious on paper, still feels… off."
    
    stop ambient fadeout 3.0

    window hide
    show black with dissolve
    window auto
    pause (2.0)
    
    scene cafe_interior_evening with dissolve
    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0     
    
    "The night winds down slowly. The last few guests trickle out, leaving behind the faint aroma of roasted beans and sugar." 
    "I start stacking empty plates while Albion wipes down the counter, moving methodically."
    "Sylphia joins us at the front, her hands folded neatly in front of her."

    show Sylphia with dissolve

    s "You both did wonderfully tonight. The customers loved it. The launch was a success."

    hide Sylphia with dissolve

    "Her words are warm, but there's a tiny crack beneath them, a thin thread of something else. Regret, maybe. Or the faintest disappointment."
    asidesa2 "(She hasn't mentioned the blend, or my desserts, even once.)"
    "I thank her quietly, forcing a small smile. Albion doesn't respond, only continues to clean the espresso machine, his expression unreadable."
    
    show Sylphia with dissolve   
   
    s "Anyway. After you close, both of you, please. Rest. You've earned it."
    "She pats my shoulder before heading to the break room to pack her things, leaving us in the soft hum of the empty café."

    hide Sylphia with dissolve

    asidesh2 "It's over, huh?"

    show Albion_Shy3 with dissolve

    al "Yeah."

    hide Albion_Shy3 with dissolve

    "He doesn't look up. The silence between us feels irrevocable."
    asidesa2 "(We did it. I should feel accomplished.)"
    "Albion finishes wiping down the counter, sets the rag aside, and finally straightens up. The soft clink of porcelain is the only sound left in the café."
    "Outside, the streetlights cast streaks of gold across the windowpanes. The bouquets from the tables are starting to wilt, petals curling gently at the edges."
    asidesa2 "(They looked so beautiful earlier tonight. Now they just look tired. Maybe I do too.)"
    "Albion moves toward the door to flip the sign to 'Closed'. His reflection in the glass looks distant, blurred by the faint condensation clinging to the window."
    asidesh2 "You should head home. I'll finish the rest here."

    show Albion_N2 with dissolve

    al "It's fine. I'll stay until the floors are done."

    hide Albion_N2 with dissolve

    "We complete the closing duties in silence, the only sound is the quiet squeak of cloth against glass."
    
    show cafe_interior_night with dissolve
   
    "When the last table is cleared, Albion finally steps back, glancing around the café one last time."

    show Albion_N2 with dissolve

    al "It's done."
    asidea2 "Yeah."

    hide Albion_N2 with dissolve   

    "The word slips out softer than I meant it to. I set down the last cup and lean against the counter. My arms feel heavy."
    asidesa2 "(We did what we could. But we never really did it together.)"
    "Albion nods toward the back room."

    show Albion with dissolve

    al "Get some rest, Astra. You've done enough."
    "There's something gentle in his tone, but it's distant."
    asidesh2 "(He's trying to be kind. But kindness isn't the same as closeness.)"

    hide Albion with dissolve

    "I nod, forcing a smile he doesn't see as he turns away."
    "When the door shuts behind him, I stay a while longer, staring at the fading flowers and the empty cups."
    asidesa2 "(We made something good. Just not perfect. Maybe someday, he'll see that's okay.)"
    "The lights dim as I flip the switch, leaving the café bathed in a soft, natural glow."
    "The scent of coffee lingers in the air... both bitter and sweet, but quietly unfinished."
    
    window hide
    $ renpy.pause (2.0)

    stop music fadeout 3.0

    play audio "<from 0 to 3>bell.mp3"

    window hide
    pause (1.0)
    show endcard_night with dissolve
    $ persistent.qwynn_route_unlocked = True
    $ renpy.pause(5.0)

    # This ends the game.

    return
   