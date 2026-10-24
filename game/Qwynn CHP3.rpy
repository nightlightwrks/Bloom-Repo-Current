# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#########################################
# QWYNN CHAPTER 1 
#########################################

label Qwynn_chp3:
  
    window hide
    show qwynn_chp3 with squares
    window auto
    pause (2.0)

    $ persistent.status_button = True

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior with squares

    al "It smells like soot in here."
    "I wrench open the oven and find yet another burnt pastry inside. That makes three today."
    asidesh2 "Sorry. I'm... very out of it."

    show Albion_SC with easeinright

    "Albion slips on his apron and moves into his section beside me—ignoring me."

    hide Albion_SC with easeoutleft
    show Sylphia with dissolve

    s "Astra! Your shift is over."
    asidesp2 "Do you need me to stay for the afternoon too?"
    "Sylphia's eyes flick briefly to the burnt pastry still sitting on the counter. I forgot to throw it out."
    s "You should probably go home and rest, before you burn the place down."

    hide Sylphia with dissolve

    asidesa2 "(I don't want to go home.)"
    "Going home means facing Qwynn. And I don't want to be near them right now."
    "I'm not even sure what's worse—finding Qwynn there with another meaningless apology, or finding the apartment empty."
    "This is the first time Qwynn and I have ever fought. I don't have a template for what to do."
    asidesp2 "Albion... what if I come over tonight?"

    show Albion_SC with dissolve

    "Albion looks like he just bit into a lemon."
    al "Why in Feldoria would you want to come over?"
    asidee2 "It could be fun. We could cook together."
    asidee2 "Or—I could cook for you. I promise I'm really g—"
    al "No. Don't ask again."

    hide Albion_SC with dissolve

    "The words land harder than I expect, even from Albion."
    "And in that moment, I realize a fact I've been avoiding: I don't have anyone I can call a friend but Qwynn."
    "I've been relying on them for so long, taking their company for granted."

    show Sylphia with easeinright

    s "Astra, you can stay back for another hour. I do want your opinion on something."
    asidee2 "Thank you so much, Sylphia!"
    "I say it a bit too loud. Every customer in the café turns their heads to me."
    "Sylphia sighs, like she knows exactly what's going on in my head."
    s "If you have a problem at home, you'll need to face it eventually."
    asidesh2 "I know."

    hide Sylphia with dissolve

    asidesa2 "(But I don't want to do it right now.)"
    "We take a seat at the furthest table at the back of the café, tucked away from the hum of customers and the hiss of the espresso machine."
    
    show cozy with dissolve

    "Sylphia sets down her mug and a clipboard."

    show Sylphia:
        zoom 1.8
        xoffset 350 
        yoffset -250
    with dissolve

    s "I'm playing around with the idea of Bloom having a mascot."
    "I blink."
    asidesp2 "A mascot?"
    s "Mhm~ You know. A little friendly animal guy~ Something people see once and immediately think of Bloom!"
    s "The restaurant chain next door has one, and people love that thing."
    s "I don't want something too obnoxious, though. The mascot should fit with our vibe."
    asidesm2 "So... not a dancing coffee cup, then."
    s "Definitely not. I was thinking something softer, maybe a small creature. A cat? Maybe a bunny?"
    "I think about the café. The light, the plants, the quiet corners where people linger."
    aside2 "Maybe an animal that nests? You know, something that suggests staying awhile."
    s "Exactly."
    s "See? That's why I wanted your opinion."
    "She smiles, tapping her pen against the clipboard."
    s "Actually... I was hoping you'd design it too."
    asidesp2 "Me?"
    s "You have a good eye. And you understand what Bloom is trying to be. It'll form part of our marketing strategy."
    "I can already picture the shapes and colors in my head."
    asidee2 "Okay. I can design it!"
    s "Fantastic~ Take your time with it. I can't wait to see what you come up with!"

    hide Sylphia with dissolve

    #SCENE: Tension after the fight


    stop music fadeout 2.0
    scene kitchen_evening with dissolve

    "The dining table is covered in sketches."
    "I sit hunched over it, pencil smudges on my fingers, surrounded by half-finished sketches."
    "I've tried a bunny with round cheeks, a small bird perched on a coffee cup, and a turtle carrying a mug on its shell. Even a coffee cup with eyes, smiling a little too enthusiastically (Sylphia is right; it's too juvenile)."
    "I tap my pencil against the page, staring at the blank space in front of me."
    "I'm painfully aware of every sound in the apartment. The hum of the fridge. The small licks of Midna grooming herself."
    "It's so quiet, being alone."
    "I let my thoughts wander."
    "{i}You don't just sell things. You sell emotions—the feeling behind them.{/i}"
    "My hand moves without thinking, sketching softer lines this time."

    play sfx "sfx_shake.ogg" 

    "A gust of wind rattles the front door. My heart jumps."
    "..."
    "...Nothing."
    asidesa "(Qwynn is usually home by now.)"
    "They're avoiding me. I know they are. The thought sits heavy in my chest, unwelcome."
    "I keep drawing anyway, even though Midna has now moved closer to distract me." 
    "Midna, who has given me an idea."
    "Slowly the image of the mascot materializes."

    window hide
    show black with dissolve
    window auto
    pause (2.0)
    scene kitchen_night with dissolve

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0

    "Then, finally—the lock turns."
    "The door opens. Qwynn steps inside."
    "They pause for half a second when they see me at the table, not quite meeting my eyes."

    menu:
        "Break the tension.":
            aside "H-How was work?"
            "The words tumble out awkwardly, like I grabbed the first normal thing I could find."
            show Qwynn_N3 at half_size with dissolve
            q "Oh. Good. Yeah... Good."
            "I nod at them."
            hide Qwynn_N3 with dissolve
            asidesh "(Did that help? It feels like it should have helped.)"
        "Let the silence linger.":
            $ qwynn_pts += 10
            show screen choice_indicator(QWYNN_COLOR) 
            "My reflex is to make small talk and smooth things over. Make sure no one feels bad."
            asidea "(But do I really want to pretend everything is fine?)"
            "I shoot Qwynn a small, tight-lipped smile, then quickly return to my sketch."

    "Qwynn moves toward their room, pausing briefly at the doorway."
    
    show Qwynn_N3 at half_size with dissolve    
    
    q "We don't have to talk right now. I just... want you to know I'm here."

    hide Qwynn_N3 with easeoutleft
    play audio "<from 2 to 4>dooropenclose.mp3" #close

    "Their door closes softly behind them."
    "I look down at my finished sketch: a coffee bean with closed eyes sitting in a mug of coffee, as if taking a bath."
    #TODO add mascot image 

    #SCENE: Astra shows sketch to Sylphia

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior with dissolve

    "When I show the mascot sketch to Sylphia, her eyes light up immediately."

    show Sylphia with dissolve

    s "Oh my gosh, I love the little coffee bean mascot~"
    s "Are you going to name him?"
    aside2 "Hmm..."

    hide Sylphia with dissolve

    "I look around the café, my eyes sweeping over the tables, pastry case and the espresso machine..."
    "Albion stands behind the bar, polishing the counter."
    asidesp2 "What about Albert?"

    show acutin with easeinleft
    "Albion shoots me a look that could curdle milk."

    hide acutin with easeoutright
    show Sylphia
    with dissolve

    s "Mm, tempting—but I was thinking Cortado. After your favorite drink."
    asidee2 "That's a great name! We can use him to promote the cortados as a menu item!"
    "Sylphia snaps her fingers, delighted."
    s "Alright! Then we'll debut Cortado for the launch event. We'll make it a celebration, something people remember."
    asidesp2 "A launch event? That sounds... big."
    s "It should be. Café Bloom deserves it. And so does Cortado!"
    asidee2 "Sounds like a plan!"

    hide Sylphia with dissolve

    "I imagine the café filled with people, posters on the windows, Cortado smiling from every corner. Something I made—something mine—bringing people in."

    menu:
        "It feels nice that this is my own project.": 
            $ qwynn_pts += 20
            show screen choice_indicator(QWYNN_COLOR) 
            "I look back down at the sketch in my hands. There's a strange pride that settles in my chest that feels unfamiliar, but not unwelcome."
            "I think about how often I lean on Qwynn."
            "How easy it is to let them take the lead, to let them smooth things over when something got hard, when something is wrong."
            "It isn't healthy."
            "For either of us."
            "This feels different. I'm standing on my own, even just a little. It's a step in the right direction."

        "I don't know if I can do this without Qwynn.":
            "The thought twists in my chest, taking root."
            "A launch event dependent on my marketing strategy... a marketing strategy Qwynn is no longer a part of."
            asidesa2 "(Can I really do this on my own?)"
            "What happens if something goes wrong and Qwynn isn't there to catch me?"
            "The weight of it all presses down on me."
            asidesa2 "(How much I've come to rely on someone else to keep me steady…)"

    play audio "<from 0 to 3>bell.mp3"

    "The bell above the door jingles. I glance up from the mascot sketch to see a familiar face walk in, paint-stained satchel bouncing against his hip."

    show Felix with dissolve

    f "Aha! I thought this place sounded familiar."
    asidesp2 "Felix!? How did you find me?"
    f "I saw the poster down the street. I didn't know I'd find you here!"

    show Felix at Transform (xpos=600) with ease
    show Sylphia at right with dissolve

    s "Well, would you look at that. Seems the marketing is working."

    hide Sylphia with dissolve
    show Felix at truecenter
    with ease 

    aside2 "Would you like to order something?"
    "I take Felix's order. To my horror, Felix orders a vanilla latte with {i}three{/i} sugars. Albion doesn't look happy to make the order either."
    asidesh2 "I'm not sure you'll be able to taste the vanilla."
    f "I absolutely will."
  
    window hide
    show black with dissolve
    window auto
    pause (2.0)

    scene cafe_interior with dissolve

    "After a few minutes, Albion hands him the cup. Felix takes a sip, smiling the entire time."

    show Felix with dissolve

    f "Perfect. Ten out of ten. No notes. Thank you."
    aside2 "Actually, I should be thanking you for all your advice for the dinner. I ended up using all the almonds."
    f "So? Did it go well?"
    asidesh2 "It started well. But… I kind of accidentally mentioned that {i}you{/i} helped plan it. Let's just say things snowballed from there."
  
    hide Felix
    show Felix_N2
    with dissolve

    f "Mhm. Qwynn got jealous?"
    asidesh2 "Well… yeah."

    hide Felix Felix_N2
    show Felix_C
    with dissolve

    f "I had a feeling something like that was going to happen."
    f "Maybe I should stay away from Bloom from now on? You know, just to stay on Qwynn's good side?"
    "He says it lightly, but there's something careful in the way he watches me now."
    
    scene cafe_interior with dissolve 

    menu:
        "No. You're important to me too.":
            $ qwynn_pts += 30
            show screen choice_indicator(QWYNN_COLOR) 
            aside2 "No. You're important to me too, Felix."
            "The answer comes out before I even think about it, but it feels right."
            show Felix with dissolve
            f "…Well… I was fishing for validation, but that was nicer than I expected."
            asidesm2 "You're not just part of some weird love triangle I didn't sign up for."
            hide Felix
            show Felix_U
            with dissolve
            f "Oh, uh—."
            hide Felix_U
            show Felix_C
            with dissolve
            f "Astra, I don't want to make things harder between you and Qwynn. We barely know each other right now."
            asidean2 "You shouldn't have to disappear to keep the peace either! You're my friend."
            asidesa2 "(My first friend outside of Qwynn in a long time.)"
            asidesp2 "So you're stuck with me, sorry."
            hide Felix_C
            show Felix 
            with dissolve
            f "Haha, sure. I'll valiantly suffer through it!"

        "Maybe it's better if we take some space.":
            asidesh2 "Maybe it's better if we take some space."
            "The moment I say it, I want to take it back."
            asidesh2 "(It's better this way. I don't want further conflict with Qwynn.)"
            "Felix shrugs, the hand not holding his coffee sliding into his pocket. He looks sad, but not overly so."
            show Felix_C with dissolve
            f "If that's what you want. I get it. I'm the outside variable here."
            asidesh2 "I'm sorry, Felix."
            hide Felix_C
            show Felix 
            with dissolve
            f "It was nice meeting you though, Astra. Have a good shift!"
            hide Felix with dissolve
            play audio "<from 0 to 3>bell.mp3"
            "The bell jingles behind him. Then he's gone."

    #SCENE: Midna starts a fire

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0
    scene kitchen_evening with dissolve

    "The apartment smells like vanilla and orange. I've lit all the candles we own to freshen up the air in the apartment."
    "Qwynn and I have been very slack with cleaning since the fight, and having a cat who is proud of leaving a trail of chaos in her wake increases the mess tenfold."
    "I'm alone tonight, wiping down the table, stacking plates."
    "Qwynn isn't here; they must still be avoiding me."
    "Or I'm avoiding them. I can't tell anymore."
    "The bin under the sink is full. I tie off the bag and lift, feeling the pull in my shoulders as I exit the apartment."
    "Just before the door clicks shut, I hear a soft crash from inside. Midna probably decided something on the table offended her and knocked it over."
    
    play music "city_night.ogg" fadeout 2.0 fadein 2.0
    scene market_evening with dissolve
    
    "Taking out the trash takes longer than it should. The big bags live in the outside bin, and they're heavy. Qwynn usually handles them—{i}'I'm stronger than you, so better I do it.'{/i}"
    "Tonight, I'm glad to do it though. The weight is grounding. Throwing away trash that's lingered since the fight feels oddly therapeutic, like I'm finally clearing out something stagnant."
    "I breathe in the cool air. Count to five. Count again."
    asidesa "(I do want to make up with Qwynn.)"
    asideeb "(I love Qwynn, after all, as more than a friend.)"
    asideem "(When I see them again, I need to at least tell them how I feel, even if it won't work between us.)"
    "When I get back to the front door, something feels wrong."
    "Something smells like it's burning."
    "My heartbeat spikes as I fumble with the lock."
    "The second the door opens, the heat hits my face."

    scene kitchen_evening
    play music "tension.ogg" fadeout 2.0 fadein 2.0 
    show fire2 with dissolve
    play sfx "fire.mp3" fadein 2.0 volume 0.3 loop

    "The kitchen is on fire."
    asidesp "Saints—!!"
    "A candle lies knocked over on the counter. The flames have already caught the wood, racing up the cabinets and walls."
    asidean "(I've got to put out the fire!)"
    "It's too late though. I've been outside too long. Smoke already fills the living room, rolling across the ceiling in thick curls."
    "More importantly—"
    asidesp "Midna! Midna, come out!"
    "I wedge the front door open, praying she'll dart for safety."
    asidean "Midna, please! We have to get out of here!"
    
    #TODO add mewo sfx

    "MIDNA" "miaow~"
    asidesp "Midna!"
    "I race to the sofa. Midna is crouched under there, eyes terrified."
    asidesp "Please come out!"
    "The air is growing thicker, hotter. It's getting harder to breathe. I try to move the couch, but it won't budge—I'm not strong enough."
    asidea "(I can't leave. I've got to save Midna!)"
    "I brace my feet against the floor and heave with everything I have. The sofa shifts—barely—just enough to scrape against the wood."
    "Then, suddenly, it lifts."
    asidesp "Qwynn!"  
    "They're standing over me, half-silhouetted in the thickening smoke, holding the frame up like it weighs nothing."

    show Qwynn_A at half_size with dissolve

    q "Astra! Grab Midna!"

    hide Qwynn_A with dissolve

    "I don't think. I dive under the couch and reach for the trembling Midna."

    show midna2 with dissolve

    "MIDNA" "miaow~!!!"

    hide midna2 with dissolve

    "Before Midna could run into the bedroom, I grab her—almost pulling her by the tail. She thrashes wildly, leaving scratches on my arms."
    "Qwynn drops the sofa."

    show Qwynn_A at half_size with dissolve

    q "Hold onto Midna."

    hide Qwynn_A
    show Qwynn_A:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve

    "In the next breath, Qwynn locks one arm behind my shoulders and the other behind my legs. With a single fluid motion, I'm off the ground, held against their chest."
    "I haven't seen Qwynn use their Were-folk strength and speed like this since the restaurant. They cut through the smoke with precision, twisting just enough to shield us both as the flames spit at their heels."
    "The second we're outside, Qwynn kicks the door shut with their heel, trapping the fire inside."

    stop sfx fadeout 2.0
    scene market_evening with dissolve

    "The three of us crumple to the floor as the fire force arrive."
    "We watch the group of Elves and Naiads put out the fire."
    
    show Qwynn_M:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve

    q "A-Aste… are you alright?"
    asidesa "...Yeah. I am."
    "Qwynn's face twists, pained and relieved all at once. Before I can react, they pull me into a tight hug—Midna squeaking in protest between us."
    q "I—I'm sorry. I won't touch you again after this, I just—"
    "MIDNA" "miaow?"

    hide Qwynn_M
    show Qwynn:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  
    
    q "You too, Midna."
    "A weak laugh escapes me despite everything."
   
    hide Qwynn
    show Qwynn_S:
        zoom 1.5
        xpos 400
        ypos -180
    with dissolve  
   
    q "Saints, I'm so glad you're okay."
    "Qwynn's breath is uneven. They shouldn't be out of breath from a little running. Something deeper is trembling under the surface."
  

label qwynn_ending:
    if (qwynn_pts >= 70):
        jump qwynn_good
    else:
        jump qwynn_bad

    #jump Qwynn_chp3

#########################################
# END
#########################################









