label felix_good:
    #morning
    #astra's apartment

    window hide
    show felix_good with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    

    scene kitchen_dawn with squares
    play music "astraapartment.ogg" fadein 2.0      
    asidee "(The launch party is tomorrow.)"
    "As excited as I am, I still find it hard to focus."
    asidesh "(Felix said he'd be there but—)"
    "After being avoided for the past week, I've come to accept that Felix will probably vanish after the party."
    asidesa "(I understand his hesitance… even if I don't agree with it.)"
    
    show Qwynn at half_size with dissolve

    q "Astra. How many times are you going to sigh like that before you tell me what's wrong?"

    play sfx "sfx_shake.ogg"
    show kitchen_dawn with vpunch

    asidesp "Saints— How long have you been standing there?"
    q "Uh. The whole time."
    "They lean against the counter, an eyebrow raised."
    
    hide Qwynn 
    show Qwynn_N3 at half_size
    with dissolve
    
    q "So? Talk to me. I already know it's about Felix."
    asidesh "...I didn't want to bug you. You don't even like him."
    q "What I don't like is how you always seem to be upset after you talk to him."
    asidesa "(I guess it would look that way to Qwynn.)"
    asidesa "Well, no need to worry. After the launch I doubt I'll be seeing Felix again."
    "Qwynn softens, crossing the room to stand next to me."
    q "I'm sorry, Aste. Honest. I know you really liked him."
    asidesh "...It's alright."
    asidesa "(It has to be.)"

    play audio "knock.mp3" fadeout 2.0

    q "I'll get it."

    hide Qwynn_N3 with dissolve
    
    aside "(It must be Qwynn's deliveries for their boutique. They always have boxes of stuff coming in.)"
    "I hear Qwynn say something. Then, a reply." 
    "My heart quickens. Stuttering when I hear that achingly familiar voice."
    asideb "(...Felix?)"
    "Their voices leak into the kitchen, but I'm glued to my seat."
    "A beat later, Qwynn returns, not quite meeting my eye."
    
    show Qwynn_M at half_size with dissolve
    
    q "It's for you." 

    #heartbeat sfx

    q "I'll be in my room if you need me."
    aside "...Thank you."

    hide Qwynn_M with dissolve

    "They retreat quietly, leaving me alone with the sudden, nervous thrum in my chest."
    "The spark of hope that I tried to snuff out reignites, blazing stronger than ever before."
    asideeb "(Why else would he be here?)"

    show felixcg2 
    show voiced
    with dissolve
    $ persistent.felix2 = True
    play music "Felix.ogg" fadeout 2.0 fadein 2.0

    "The door has been left open. Framed in the soft morning light stands Felix, holding a large bouquet of white tulips."

    voice "<from 115 to 119>audio/astra/astra_felix.ogg"
    asideb "Felix? W-What is this?"

    voice "<from 6 to 11.6>audio/felix/felix_good.ogg"
    f "I've been thinking a lot this past week. Couldn't stop thinking actually."
    "His voice wavers slightly, but his smile is genuine—warm, a little shaky, and entirely him. He takes a step closer, the sunlight brushing gold across his face."

    voice "<from 12 to 18>audio/felix/felix_good.ogg"
    f "...I'm still scared, but I'm also tired of letting my fear keep me from being happy."
    voice "<from 26 to 33>audio/felix/felix_good.ogg"
    f "For the first time in a long time, I'm willing to accept those fears, instead of letting them hold me back."
    voice "<from 49 to 56>audio/felix/felix_good.ogg"
    f "I'm sorry, Astra. For pushing you away when all you've ever done is share your joy with me."
    voice "<from 60 to 68>audio/felix/felix_good.ogg"
    f "Watching you chase your dreams these past few weeks… Let's just say you gave me the push I need to chase my own."
    "My mind races on a chariot of emotion. Of course, just as I came to terms with the situation, Felix decides to show up with that contagious grin of his."
    asideem "(A ridiculous grin and awkward charm that makes it hard to breathe. And the flowers? Brutal.)"
    "I'm not upset, far from it. My giddiness is only held back by the abruptness of his appearance, and the lingering question reverberating in my head."
    asideb "(Does this mean what I think it does?)"
    voice "<from 77 to 79>audio/felix/felix_good.ogg"
    f "Am I too late?"
    "The nervous warble in his voice brings me back to earth."
   
    #end CG
    scene kitchen_dawn 
    show voiced
    with dissolve
    show Felix_EX 
    with dissolve

    voice "<from 131.4 to 137>audio/astra/astra_felix.ogg"    
    asidesp "N-no. I only— I was just thinking."

    show Felix_EX 
    with dissolve

    voice "<from 82 to 84>audio/felix/felix_good.ogg"
    f "You do that a lot."

    voice "<from 141 to 143>audio/astra/astra_felix.ogg"
    asidesm "Someone has to." 
    "He laughs, and the sound hits something tender in me. It's like coming home again, the way we fit together like puzzle pieces. Like we were never apart to begin with."
    voice "<from 148 to 151>audio/astra/astra_felix.ogg"
    asideb "I don't want to assume, but—"
    voice "<from 159 to 163>audio/astra/astra_felix.ogg"
    asideeb "Are you asking me out?"

    hide Felix_EX
    show Felix_E
    with dissolve

    voice "<from 94 to 101>audio/felix/felix_good.ogg"
    f "Ah, yes. I should've been more clear. Here, I'll start over."
    "He steps back away from the door frame, clearing his throat like he's about to give a speech."

    hide Felix_E
    show Felix
    with dissolve

    voice "<from 108 to 110>audio/felix/felix_good.ogg"
    f "Close the door."
    voice "<from 171 to 173>audio/astra/astra_felix.ogg"
    asidesp "Felix—"
    voice "<from 114 to 117>audio/felix/felix_good.ogg"
    f "It'll be worth it, please?"
    voice "<from 177 to 180>audio/astra/astra_felix.ogg"
    asideb "Fine, fine. Closing the door now."

    hide Felix with dissolve

    play audio "<from 2 to 4>dooropenclose.mp3" #close

    asideem "(Like I said… Ridiculous.)"
    "And yet… the butterflies in my stomach refuse to settle down."

    play audio "knock.mp3" fadeout 2.0

    "I chuckle internally, but play along, feigning surprise."
    
    scene felixcg3 
    show voiced
    with dissolve
    
    voice "<from 180 to 183>audio/astra/astra_felix.ogg"
    asidesp "Felix, what are you doing here?"
    voice "<from 120 to 122>audio/felix/felix_good.ogg"
    f "Astra! There you are!"
    "It's difficult to look at him directly. I focus on the flowers in his hands, hoping to distract Felix from the obvious heat creeping across my cheeks."

    voice "<from 191 to 195>audio/astra/astra_felix.ogg"
    asidesp "Saints~ Are those for me?"
    voice "<from 122 to 128>audio/felix/felix_good.ogg"
    f "Actually these are my emotional support flowers, but I can share."
    "A callused hand worn from years of holding brushes takes hold of my own. It pulls me in closer to softly press a bundle of snow white tulips into my chest." 
    asideem "(!!!)"
    voice "<from 134 to 137>audio/felix/felix_good.ogg"
    f "Astra. Will you go out with me?"
    asideeb "(His smile is sweet and blinding… How could I even consider saying no to that?)"

    voice "<from 198 to 201>audio/astra/astra_felix.ogg"
    asideb "Of course I will."

    scene kitchen_dawn 
    show voiced
    with dissolve

    hide Felix_EX
    show Felix_B 
    with dissolve

    "There's a moment of silence. The rest of the world had long since faded, leaving only the scent of tulips and the everpresent smell of acrylic which clings to Felix." 
    
    hide Felix_B
    show Felix_B at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve
       
    "He steps even closer."

    hide Felix_B
    show Felix_E at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve

    voice "<from 145 to 148>audio/felix/felix_good.ogg"
    f "...I want to kiss you." 
    "I lean in, enough that I can feel his breath soft and warm against my lips. His hands rest on my waist, tentative but steady, tightening slightly when I move to meet him halfway. "

    voice "<from 206 to 208>audio/astra/astra_felix.ogg"
    asidesm "I won't stop you."
    "His forehead pushes into mine. The space between us hums."

    hide Felix_E
    show Felix_EX at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve

    voice "<from 152 to 156>audio/felix/felix_good.ogg"
    f "I like you—{i}a lot{/i}—Astra."
    voice "<from 209 to 210>audio/astra/astra_felix.ogg"
    asideb "I like you too."
    voice "<from 157 to 158>audio/felix/felix_good.ogg"
    f "A lot?"
    voice "<from 214 to 217>audio/astra/astra_felix.ogg"
    asideb "Yes, very much."
    voice "<from 160 to 162>audio/felix/felix_good.ogg"
    f "That's good."
    voice "<from 165 to 169>audio/felix/felix_good.ogg"
    f "…Then, I'm going to kiss you now."
    voice "<from 221 to 223>audio/astra/astra_felix.ogg"
    asidesm "I sure hope s—"
    "The rest of my words are cut off as Felix {i}finally, blissfully{/i}, closes the gap between us."

    scene black 
    show voiced 
    with dissolve

    "My eyes flutter shut. One of my hands reaches for Felix's cheeks—the other clutches the flowers closer—and his hands slide from my waist to my back, drawing me even closer."
    "Our first kiss is gentle, playful, and {i}mostly{/i} teeth. Felix smiles, which makes me smile, ruining any chances to kiss him deeper."
    "Our second, third, and fourth kiss are even shorter. Some land on my lips, but some are placed along the curve of my jaw, or right beneath my eyes."
    "By the fifth, I've lost my breath."

    scene kitchen_dawn 
    show voiced
    with dissolve

    show Felix_EX at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve

    "Felix breaks away with a laugh."
    voice "<from 172 to 176>audio/felix/felix_good.ogg"
    f "Sorry, sorry. I can't help it."
    "My heart threatens to burst."
    voice "<from 227.8 to 231>audio/astra/astra_felix.ogg"
    asideb "It's okay, neither can I." 

    scene black with dissolve
    $ renpy.pause (2.0)

#GOOD END: LAUNCH PARTY

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadein 2.0
    scene cafe_interior 
    with dissolve

 
    "The day of the launch party arrives."
    "The scent of coffee fills the air before the doors even open—warm, rich, familiar. Outside, a small crowd has already gathered, their chatter blending with the soft hum of the city."
    "Flowers in bright, vibrant tones adorn each table, their petals catching the light from the café windows and casting gentle color across the polished counters and gleaming cups."
    "By the counters, the main attraction of the night awaits. A section of the café that's been transformed to display Felix's artwork." 
    "Alongside this, an extra table has been added to the floor. One large enough to host bigger gatherings and game nights." 
    "I smooth down the front of my apron and glance toward Felix."
    "He's standing next to Albion, adjusting and readjusting the new display board, the words 'Café Bloom Launch Party: Featuring Artwork by Felix Tailor' written neatly in chalk."
    "Sylphia unlocks the front door, her smile bright and welcoming."
    
    show Sylphia with dissolve

    s "Alright, everyone. Let's make this day one to remember!"

    hide Sylphia with dissolve

    "The first guests to arrive are familiar faces: our regulars."
    "There's the elderly couple who always share a single slice of cake and two cups of cappuccino; the group of students who fill the corner table with laughter—" 
    "—even the dwarven courier who insists on getting his coffee 'to go' but always ends up staying anyway."
    "Along with the regulars, Mr. Ellwood, Miss Verac, and Velvet also make their appearance. They mill around, excitedly mingling with the other guests."
    "Each customer greets us warmly, their eyes wide as they see the new mural and extra displays."
    cus "This is amazing! You've outdone yourselves this time, Sylphia."
  
    show Sylphia with dissolve
  
    s "Thank you~ But all credit goes to my team."
    "She gestures toward us, and for a moment, the café feels alive in a way that words can't quite capture. It is full of chatter, clinking cups, and the comforting rhythm of brewing coffee."

    hide Sylphia with dissolve    
   
    "Somewhere between brewing and plating desserts, a familiar voice calls from the doorway."

    show Qwynn_S at half_size with dissolve

    q "Hey, superstar! Look at this place! It's incredible."
    asidesp2 "Qwynn! You made it!"
    q "Wouldn't miss it for the world. You pulled this off, huh?"

    hide Qwynn_S with dissolve

    "I can't help but steal a glance at Felix." 
    "He stands by the display table, surrounded by a small cluster of customers. His posture is relaxed now, one hand loosely at his side, the other gesturing animatedly as he talks about his art. "
    "Just behind him is the mural he'd painted. It's then that I notice something different."
    asidesp2 "(He changed it…)"
    "For the most part, it was exactly what we'd agreed on. A depiction of every race, all dining in Café Bloom." 
    "But—the colors are brighter, and within the image, there are figures that look suspiciously like myself, Albion, Sylphia, Qwynn, Velvet, and finally… Felix himself."
    "He went out of his way to paint all of us together… proof of our connection."
    asideb2 "(It's perfect.)"
    "He must sense my gaze, as his eyes flick over to me. He doesn't say anything, but he flashes a small, conspiratorial smile. Then a wink, so fleeting it could've been imagined..."
    asideb2 "(But I know it wasn't.)" 
    "Of course he'd still find a way to make my heart race, even in the middle of work."
    asideeb2 "Yeah… we did." 
    "As more guests arrive, the café hums with life. The lights seem warmer, the air richer with laughter and soft conversation."
    "For a moment, it feels like everything has fallen into place—the culmination of every sleepless night, every trial, every ounce of effort."
    aside2 "(Sylphia was right. The café really did need this.)"

    stop ambient fadeout 2.0

#GOOD END: EPILOGUE
#evening

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "Felix.ogg" fadeout 2.0 fadein 2.0
    scene studio_night 
    show voiced
    with dissolve

    "The shop is closed for the night, but the faint scent of paint and varnish still lingers in the air." 
    "I unlock the door and step inside Studio Alizeti, greeted by the quiet hum of the city outside and the faint creak of the old wooden floorboards."
    "I know Felix is home. He always is, around this time."

    voice "<from 240 to 245>audio/astra/astra_felix.ogg"
    asidesm "Felix? …I know you're here."
    "Nothing." 
    "Unfortunately, I know exactly what is coming."
    asidesh "(I'm getting a bad feeling about this.)"
    "Sparks of anticipation crawl up my spine as I slow my steps, trying to spot the telltale shadow that always gives him away."

    voice "<from 251 to 256>audio/astra/astra_felix.ogg"
    asidesm "Felix— You won't get me this time, I know your tricks by now!"
    "It's a bluff, and an obvious one at that. But it's worth a shot."
    "I make my way toward the loft stairs, moving carefully between easels and half-finished canvases." 
    "The air smells faintly of turpentine and something floral, probably the bouquet from the launch party he refuses to throw out." 
    "Just as I reach the steps, arms snake around my waist from behind."

    play sfx "sfx_shake.ogg"
    show studio_night
    with vpunch

    voice "<from 1 to 2>audio/felix/felix_good2.ogg"
    f "Boo."

    voice "<from 258 to 259>audio/astra/astra_felix.ogg"
    asidesp "Ah!"
    "He bursts into laughter, his chest shaking lightly against my back." 
    voice "<from 3 to 7>audio/felix/felix_good2.ogg"
    f "I'll never get tired of doing that."
    "He hooks his chin over my shoulder and places a soft kiss on my cheek."
    "And because I can't help it, I melt into the embrace without a fight." 
    asideem "(Always so warm.)"

    voice "<from .5 to 3>audio/astra/astra_felix2.ogg"
    asideeb "...One day, I'll get my revenge."
    voice "<from 15 to 18>audio/felix/felix_good2.ogg"
    f "Uh huh. I'm sure you will." 
    "I turn around in his hold, indignant." 

    show Felix_EX at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve

    voice "<from 25 to 30>audio/astra/astra_felix2.ogg"
    asidean "You don't believe me at all!"

    hide Felix_EX
    show Felix at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve

    "Felix hums, that familiar self-satisfied grin on his face."
    voice "<from 21 to 24>audio/felix/felix_good2.ogg"
    f "I believe that you'll certainly {i}try{/i}." 
    asidep "..."
    "My pout is rewarded with another chaste kiss. This time on my forehead."

    hide Felix
    show Felix_EX at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve

    voice "<from 25 to 27>audio/felix/felix_good2.ogg"
    f "Missed you."

    hide Felix_EX with dissolve

    "I hear it everyday, but it never fails to make my heart clench. His sincerity, his care, will never grow old."
    "Everyday with Felix is full of laughter. Days are brighter and more colorful than before, painted with colors that I can now name."

    show Felix_EX at truecenter:
        zoom 1.8 
        yoffset 350 
    with dissolve

    voice "<from 34 to 38>audio/astra/astra_felix2.ogg"
    asidesm "I missed you more."

    hide voiced with dissolve 
    
label after_end:

    stop music fadeout 2.0

    window hide
    $ renpy.pause (2.0)

    play audio "<from 0 to 3>bell.mp3"

    window hide
    pause (1.0)
    show endcard_night with dissolve
    $ persistent.qwynn_route_unlocked = True
    $ renpy.pause(5.0)

    # This ends the game.

    return


label felix_bad:

    window hide
    show felix_bad with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    scene cafe_interior with squares
    #play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    #play ambient "sfx_cafenoise.ogg" fadein 2.0

    "The day of the launch party arrives."
    "The scent of coffee fills the air before the doors even open—warm, rich, familiar. Outside, a small crowd has already gathered, their chatter blending with the soft hum of the city."
    "Flowers in bright, vibrant tones adorn each table, their petals catching the light from the café windows and casting gentle color across the polished counters and gleaming cups."
    "By the counters, the main attraction of the night awaits. A section of the café that's been transformed to display Felix's artwork." 
    "Alongside this, an extra table has been added to the floor. One large enough to host bigger gatherings and game nights." 
    "I smooth down the front of my apron and glance toward Felix."
    "He's standing next to Albion, adjusting and readjusting the new display board, the words 'Café Bloom Launch Party: Featuring Artwork by Felix Tailor' written neatly in chalk."
    "I try to catch his gaze, but it seems like Felix is actively avoiding me. Any attempt to get closer is rebuffed with disarming politeness."
    "He's drawn a firm line between us. Never to be crossed again."
    "Sylphia unlocks the front door, her smile bright and welcoming."

    show Sylphia with dissolve

    s "Alright, everyone. Let's make this day one to remember!"

    hide Sylphia with dissolve

    "The first guests to arrive are familiar faces: our regulars."
    "There's the elderly couple who always share a single slice of cake and two cups of cappuccino; the group of students who fill the corner table with laughter—" 
    "—even the dwarven courier who insists on getting his coffee 'to go' but always ends up staying anyway."
    "Along with the regulars, Mr. Ellwood, Miss Verac, and Velvet also make their appearance. They mill around, excitedly mingling with the other guests."
    "Each customer greets us warmly, their eyes wide as they see the new mural and extra displays."
    cus "This is amazing! You've outdone yourselves this time, Sylphia."

    show Sylphia with dissolve

    s "Thank you~ But all credit goes to my team."
    "She gestures toward us, and for a moment, the café feels alive in a way that words can't quite capture. It is full of chatter, clinking cups, and the comforting rhythm of brewing coffee."
   
    hide Sylphia with dissolve  
   
    "Somewhere between brewing and plating desserts, a familiar voice calls from the doorway."

    show Qwynn_S at half_size with dissolve

    q "Hey, superstar! Look at this place! It's incredible."
    asidesp2 "Qwynn! You made it!"
    q "Wouldn't miss it for the world. You pulled this off, huh?"
    aside "Yeah… we did." 

    hide Qwynn_S with dissolve

    "As more guests arrive, the café hums with life. The lights seem warmer, the air richer with laughter and soft conversation."
    "For a moment, it feels like everything has fallen into place—the culmination of every sleepless night, every trial, every ounce of effort."
    aside2 "(Sylphia was right. The café really did need this.)"
    "Yet, paired with the joy of the evening's success is the distracting pull of grief."
   
    stop music fadeout 5.0
   
    "I glance at the mural that Felix painted. It's beautiful, of course, a depiction of every race dining here together in Café Bloom. But— I can't help but feel that something is missing."
    "The hollow echo of what might have been…"

    stop ambient fadeout 3.0

    #BAD END: EPILOGUE
    #evening
    #studio alizeti

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    scene studio_night with dissolve
    play music "city_night.ogg" fadeout 2.0 fadein 2.0

    "The shop is closed for the night, but the faint scent of paint and varnish still lingers in the air." 
    "I open the door and step inside Studio Alizeti, greeted by the quiet hum of the city outside and the faint creak of the old wooden floorboards."
    "I know Felix is home. He always is, around this time."
    aside "Felix? ...I know you're here."
    f "Evening, Astra."
    "His voice carries from somewhere near the easels, familiar, calm and polite. I find him tidying brushes, the motion methodical, almost rehearsed."
    "He turns when I approach, smiling. It's the same smile he uses for clients who visit the studio. Measured. Painless."
    
    show Felix with dissolve    
    
    f "I wasn't expecting you tonight. How've you been?"
    asidesh "...Fine. Bloom has been busier. I've just come to thank you for the art. And, for this—"
    
    hide Felix with dissolve
    
    "I hold up the small bouquet in my hands before setting them down on the nearest surface. I want to remove myself from them as soon as possible. The scent threatened to choke me the whole way here."
    asidesh "Sylphia asked me to drop this off for you… I'm not trying to disrespect your wishes. I— tried to have Albion do it."
    "He pauses, the sounds of him organizing brushes halting for a beat. Then, he continues. Glossing over it like a coat of varnish."
    
    show Felix with dissolve
    
    f "...No worries. Tell Sylphia I appreciate it."
    aside "The place looks nice. You've been keeping it tidy."
    "The conversation feels too stiff. I try to smile, but it comes out disingenuous."
    f "Figured I should try to keep up appearances. Especially with more commissions coming in. All thanks to Bloom."

    hide Felix
    show Felix_N2
    with dissolve

    f "Was there anything else? Sylphia said everything had been squared away."
    asidesa "(He says it lightly, but his tone never wavers from that professional cadence. The tone meant for strangers, not for someone he once let in.)"
    "The silence stretches thin, like canvas pulled too tight over a frame. I want to ask him if he ever thinks about our time together, the fun we had, the warmth—but I already know the answer."
    
    hide Felix_N2 with dissolve
    
    "He's painted over it. Layer by layer, until nothing of us remains."
    asidesa "(I can only pray that one day, he'll see the cracks beneath the surface. That he'll realise what he's lost, {i}beyond{/i} Sophie... and what he's pushed away.)"
    "But for now, I shake my head, matching his smile with a hollow, practiced one of my own."
    aside "Just the flowers, and my thanks. Take care, Felix."

    show Felix with dissolve

    f "You too, Astra."

    hide Felix with dissolve

    scene black with dissolve
    play audio "<from 2 to 4>dooropenclose.mp3" #close

    "I leave the studio before the weight in my chest can pull me down completely. The door shuts behind me with a soft click."
    "The echo fades faster than I expect."

    stop music fadeout 3.0

    window hide
    $ renpy.pause (2.0)
    
    play audio "<from 0 to 3>bell.mp3"
    
    window hide
    pause (1.0)
    show endcard_night with dissolve
    $ persistent.qwynn_route_unlocked = True
    $ renpy.pause(5.0)

    return