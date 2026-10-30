# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Astra", color="#3a0f0c")
define q = Character("Qwynn", color="#e45472")
define al = Character("ALBION", color="#e297b2")
define f = Character("Felix", color="#a06bca")
define s = Character("Sylphia", color="#3a0f0c")
define c = Character("Caelan", color="#51abe4")
define n = Character("Nimue", color="#3a0f0c")
define v = Character("Velvet", color="#3a0f0c")
define who = Character("???", color="#3a0f0c")
define vnd = Character("Vendor", color="#3a0f0c")
define sf = Character("SPIFFY ELF", color="#3a0f0c")

define alside = Character ("ALBION", color="#df6f98", image="albion")
define alsidesc = Character ("ALBION", color="#df6f98", image="albionsc")
image define alside = "side albion"
image define alsidesc = "side albionsc"

define Dryad = Character ("Dryad Girl", color="#3a0f0c")
define Doggy = Character ("Dog Eared Boy", color="#3a0f0c")
define Girl = Character ("Short-Haired Girl", color="#3a0f0c")



init:
    image rain:
        "rain1.webp"
        0.09
        "rain3.webp"
        0.09
        "rain2.webp"
        0.09
        repeat

init:
    image rain2:
        "rain1.webp"
        0.5
        "rain3.webp"
        0.5
        "rain2.webp"
        0.5
        repeat


#########################################
# ALBION CHAPTER 2 
#########################################



label Albion_chp2:

    $ persistent.status_button = True

    window hide
    show albion_chp2 with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    #TODO comedic music. uncomment below line when added
    #play music "cafebloom_day.ogg" fadeout 2.0 fadein 3.0 
    
    scene cafe_interior with squares

    asidesp2 "Hey Albion, try this!"

    show Albion_N2 with dissolve

    al " …Alright, sure."


    hide Albion_N2 
    window hide
    show black 
    with dissolve
    $ renpy.pause(1.0)
    
    window auto
    scene cafe_interior with dissolve

    asidesp2 "Albion, I made these cookies last night."

    show Albion_N2 with dissolve

    al "Oh. Thanks."

    hide Albion_N2 
    window hide
    show black 
    with dissolve
    $ renpy.pause(1.0)
    
    window auto
    scene cafe_interior with dissolve
  
    asidee2 "These macarons didn't turn out very good—but the flavor is there, I promise!"
    "Albion grabs one offhandedly, putting it to his mouth to eat and quickly running his hands under water to wash off any residue."

    show Albion_N2 with dissolve

    al "…Not bad."
 
    hide Albion_N2 
    window hide
    show black 
    with dissolve
    $ renpy.pause(1.0)
    
    window auto
    scene cafe_interior with dissolve
 
    asideeb2 "Hey, Albion! Cheesecake bites! Don't ask how many failed before these worked! Here, take a fork."
   
    hide Albion 
    window hide
    show black 
    with dissolve
    $ renpy.pause(1.0)
    
    window auto
    scene cafe_interior with dissolve
   
    asidee2 "Brownies! Fruit tarts! Muffins! Oh, don't eat that one, it's burnt!"
    "Day after day, the pattern repeats. I bake, I bring, I insist. He resists. Or tries to. But every time, he takes a bite."
    asideb2 "(And every time, I watch him for the smallest flicker of approval.)"
   
    hide Albion 
    window hide
    show black 
    with dissolve
    $ renpy.pause(1.0)
    
    window auto
    scene cafe_interior with dissolve
   
    
    asidesp2 "Hey Albion—"

    show Sylphia with dissolve
    #TODO uncomment after new track is added above
    #play music "cafebloom_day.ogg" fadein 2.0

    s "Astra~ How's it going with the menu upgrades?"
    asidesp2 "Oh! It's going fine! I've been trying a lot of different recipes, and Albion is trying to make a signature blend."
    s "Perfect. That'll be our highlight for the launch event: your desserts paired with his coffee. We'll make it a celebration, something people remember."
    asidee2 "A launch event? That sounds… big."
    s "It should be. Café Bloom deserves it."
    asidesh2 "(So does Albion… though I doubt he'd ever admit it.)"
    s "By the way, before I forget, here."
    "She pulls a small shopping bag from behind the counter and sets it down in front of me. The handles crinkle softly."
    s "Thought these might be useful."

    hide Sylphia with dissolve

    asidesa2 "(Did we get new stock? It's a bit early in the week.)"
    "I peek inside the bag. My eyes widen."
    "Inside are neat bundles and jars, carefully packed." 
    "Soft white flour tied with string, sugar glinting faintly through a paper bag, plump berries still cool from storage, even fresh lemons and a small jar of honey tucked in at the bottom."
    asidee2 "(There's so much here... flour, sugar, fruit, even the good vanilla. I was almost out of half of these!)"
    "Nestled between the ingredients is a folded piece of paper. I fish it out carefully."
    "{i}It's not like I got them for you or anything. They were on sale.{/i}"
    asideem2 "(Well. That's not Sylphia's handwriting.)"
    "The corners of my mouth lift."
    asideb2 "(I'll take it. Albion's version of 'you're doing great.')"
    "I tuck the note back in the bag, my heart feeling just a little lighter than before."
    asidesp2 "Speaking of Albion, where is he?"

    show Sylphia with dissolve

    s "I've given him the rest of the day off. He seemed a bit overworked."
    s "It's a bad habit of his."
    aside2 "What do you mean?"
    "Sylphia's gaze drifts to the counter where Albion was working earlier, her voice softening."
    s "Albion… pushes himself harder than most. He always has. It's as if he's carrying a weight no one else can see. If he isn't careful, he'll work himself to death before he ever admits he needs help."
    s "I don't think he even realises when he's gone too far. He grew up in a place where he felt like he had to prove himself constantly. Old habits like that don't disappear overnight."
    "She offers me a small smile, but there's a hint of sadness in it."
    s "All I can do is remind him this café is different. Here, he doesn't need to prove anything."

    hide Sylphia with dissolve

    asidesa2 "(He doesn't talk about any of that with me… but hearing it from her makes me want to know more.)"
    "Sylphia's eyes flick to the tray of my latest desserts, still sitting on the counter, and her expression softens."

    show Sylphia with dissolve

    s "These look wonderful. Even if they're not quite the same every time… that's part of the charm."
    "She picks up a cookie, turning it over in her hand."
    s "People remember the ones that feel genuine."
    "She takes a small bite, smiling faintly."
    s "Keep at it. I think you're closer than you realize."

    hide Sylphia with dissolve

    "Closer… even if I don't know what 'perfect' is supposed to look like yet."

    scene kitchen with dissolve

    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0

    asidea "I feel restless…"
    "I frown as I pick up a gingerbread man cookie that I had baked and decorated. I stare at it distastefully while its little white smile taunts me."
    asidesa "(I hope Albion's okay…)"

    show Qwynn_S at half_size with dissolve

    q "I think your desserts are really good! You're definitely improving at a scary rate."
    "I shake my head."
    aside "That's not it. Albion was sent home early because he was overworking himself. So I haven't had the chance to make him try this batch."
    q "Could you get Sylphia to do it? Though, if my experience is anything to go by, she's probably had more sugar this week than the rest of her life combined."
    aside "My desserts need to pair well with Albion's blend. So he has to be the one to taste it."
    asidesa "(…)"
    asidesp "I think I'm going to go to his house."

    hide Qwynn_S
    show Qwynn_N3 at half_size
    with dissolve

    q "Huh!? Are you sure that's a good idea? He should probably be left alone to recover."
    asidesp "All the more reason to check on him. I'll cook him something to make him feel better, then give him these cookies for dessert."

    hide Qwynn_N3 with dissolve

    asideeb "(Besides, I just want to see him.)"

    show Qwynn_M at half_size
    with dissolve

    "For a second, Qwynn's smile falters. Their hand tightens slightly on the mug they're holding, bracing against words they want to say but can't."

    hide Qwynn_M
    show Qwynn_S at half_size
    with dissolve

    "But a heartbeat later, the easy grin is back, polished smooth, as though nothing had cracked through at all."
    "Their voice is nonchalant, but softer than before."
    q " …Okay. Take care out there. It looks quite windy."

    hide Qwynn_S
    with dissolve

    asidesp "Got it! I'll see you tonight!"
    "I hurry off, my mind already spinning with recipes and plans. Behind me, I think I hear Qwynn exhale, but when I glance back they're smiling as usual."

    scene market_evening with dissolve
    play music "city_night.ogg" fadeout 2.0 fadein 2.0

    asidesp "Albion, open up!"
    "It's the third time I've rung the doorbell. The lights are on inside—I know Albion is in there. Is he really going to leave me out here?"
    asidesp "(Ah…)"

    show rain2 with dissolve

    play ambient "rain.ogg" volume 0.2

    "The first raindrop falls on me. Then the second. Within moments, the drizzle turns into a pour."

    show rain with dissolve

    asidesa "(My cookies are getting wet.)"
    asidesa "(Albion…)"
    "I think about what Albion had said to me not too long ago—words that didn't mean much back then, but suddenly prickle now."
    "'…you always stick your nose in where it doesn't belong.'"
    asidesa " (…)"
    asidesh "(Maybe I should go home.)"
    "The rain has already soaked through the cloth I laid over the cookies, turning it dark and heavy. The cheerful gingerbread faces inside blur and smear under the drops."
    "I turn to leave, the weight of the ruined basket pulling at my arm. Then—"
    "The door creaks open."
    asidee "Albion!"
    "His signature scowl is framed by the dim light of his entryway. But it's not quite as sharp as usual."
    al "…Come on in."
    
    stop ambient fadeout 3.0

    window hide
    show albion_pov with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    stop audio 
    scene albionapt_evening with squares
    play music "Albion.ogg" fadeout 2.0 fadein 2.0

    "Albion wants to say—no, scream—{i}Why are you here{/i}?"
    "She should've warned him. He didn't have enough time to clean his apartment before she arrived."
    "He did the best he could, of course, as fast as he could. By the time the doorbell rang for the third time he knew he had left her out there for too long."
    "Not that his apartment isn't already clean—everything in its place, every surface wiped."
    "But it's Astra. Meddling, insufferable, Astra… who somehow deserves to see his apartment in the best condition possible."
    "She steps inside, her wet hair clinging to her cheeks, clothes damp from the rain."
    "The basket in her arms looks pitiful now, the cloth sagging with water. She moves straight to the kitchen counter and sets it down, as if she owns the space already."
  
    show Astra_E with dissolve
  
    a "Wow…"
    "Her voice is soft, surprised. She wanders slowly, fingertips brushing along the shelves, the table, the edges of the counter as though she's in a museum."
    
    hide Astra_E
    show Astra
    with dissolve
    
    a "It's… so neat. I didn't know you lived like this. Though, I guess I should've known."
    
    hide Astra with dissolve
    
    "Albion stiffens, heat rising at the back of his neck. It's not praise—it shouldn't feel like praise—but the way she says it makes something twist in his chest."
    "Of course it's neat. It has to be."
    "But watching her look around, wide-eyed and impressed, makes him realize something he hadn't considered: to her, this space might look like more than just 'neat'." 
    "It might look like a piece of him he never intended to show."
    "He clenches his fists, swallowing the words still threatening to spill out: Why are you here?" 
    "Instead, he stays silent, watching her move through the apartment with that same careless energy that always manages to unbalance him."
    
    show Astra_SH with dissolve
    
    a "I couldn't catch you at work, and Sylphia said you left early, so I thought I'd check on you."
    "She takes a deep breath. Her eyes sweep the countertops."
    
    hide Astra_SH
    show Astra_B 
    with dissolve    
    
    a "...I was worried about you, I guess."

    hide Astra_B with dissolve

    "Albion's chest tightens. For a moment, the world feels unnervingly still, then warm—an almost unfamiliar warmth spreading through him."
    "How long had it been since anyone had said those words to him? Since someone had worried about him?"
    "He's just about to form the words to express how much that means to him—when her eyes snag on something glinting nearby."

    show Astra_E with dissolve

    a "Oh, what's this? It's beautiful."

    hide Astra_E with dissolve

    show astopwatch with dissolve

    "Her hand reaches toward the stopwatch resting on the shelf."

    stop music fadeout 2.0

    alsidesc "DON'T TOUCH THAT!"

    window hide
    show astra_pov with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    scene albionapt_evening with squares
    
    play music "tension.ogg" fadeout 2.0 fadein 2.0
    
    "I don't know what happened."
 
    "One moment, I was telling Albion I was worried about him. I had struggled to find the words—tripped over them, even—but I was about to say more."
    "Something that conveyed, '{i}Your opinion matters to me more than it should, and I don't know why{/i}.' Something that made me so nervous that I had to do something with my hands."
    "Something that made Albion snatch the stopwatch I was reaching for, his glare a dagger to my throat."

    show Albion_SC with dissolve

    al "DON'T TOUCH THAT!"
    asidesp "I… I'm sorry. I was just—"
    al "You were just {i}what{/i}, Astra?"
    asidesh "I—"
    al "Showing up to my house uninvited, tracking in rainwater, messing with my things—just to fish for compliments for your desserts?"
    al "Didn't I tell you to {i}stop sticking your nose in where it doesn't belong{/i}?"

    hide Albion_SC with dissolve

    asidesa "(How am I supposed to answer that…?)"


    menu:
        "Respond angrily.":
            asidean "Fine! Maybe I {i}do{/i} stick my nose in. But at least I care enough to try! Do you know how exhausting it is to keep worrying about someone who only pushes me away?"
            "The words burst out before I can stop them. His eyes widen slightly, but he doesn't interrupt."
            "My heart hammers in my chest. The air is thick with everything I said aloud."
        "Respond calmly.":
            $ albion_pts += 10
            show screen choice_indicator() 
            aside "…I wasn't fishing for compliments, Albion. I just wanted to see if you were okay. That's all."
            "My voice is quiet, much steadier than I expect. For a moment, the anger in his face falters, replaced by something unreadable. He looks away, jaw tight, but doesn't say anything more."

    asidesa "(…I should go.)"
    "The air in the apartment is stifling now, almost suffocating. I force myself to turn toward the door, both my heartbeat and steps echoing in my brain far louder than they should."
    "Just before I cross the threshold, I risk one last glance over my shoulder. He hasn't followed me. He hasn't even looked up."
    asidesa "(If I stay another second, I'll break.)"
    "So I leave, pulling the door shut behind me before I fall apart."

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    scene cafe_interior with dissolve

    #TODO maybe change music emotional idk
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0 

    show Sylphia with dissolve

    s "The blend and the dessert clash. They're both strong in different ways, but together… they cancel each other out."
    "The words sting, though I can't tell if it's because she's criticizing my dessert or because Albion's work is being dismissed right alongside mine."
    "Either way, neither of us looks at the other. The silence between us is thick."
    "Seeing this, Sylphia's expression softens."
    s "Don't worry. This is what testing is for. You'll find the right balance."

    hide Sylphia with dissolve

    "I force a laugh that sounds far too brittle. My hands twist in my lap beneath the table, sticky with sugar from the last failed batch."
    asidesa2 "(Of course it doesn't work. Why would it? We can't even look at each other, let alone create something that belongs together.)"
    "Out of the corner of my eye, I see Albion's jaw tighten, his knuckles pale around his cup. Still, he says nothing."
   
    show Sylphia with dissolve
   
    s "Astra, maybe you can try a lighter dessert next time. Albion, perhaps consider rounding the edges of the bitterness. It's a partnership, after all."
    "Her smile lingers on us for a moment, gentle but firm, before she rises from her seat."
    s "I'll leave you two to think about it."

    hide Sylphia with dissolve

    play audio "<from 0 to 3>bell.mp3"

    "And just like that, she's gone. The bell above the café door jingles faintly as she steps out, leaving only the low hum of silence behind."
    "I keep my eyes on the crumbs scattered across my plate. The weight of the air between us is unbearable, pressing down heavier than Sylphia's critique ever could."
    "Albion stands slowly, collecting his cup with a deliberate calm that feels more like armor than habit." 
    "Without a word, he turns back toward the counter, slipping behind it as though the distance could shield him from me."
    "I stay where I am, fingers curling tight in my lap."
    asidea2 "(What am I supposed to say? Sorry I almost touched something precious? Sorry I came to your house? Sorry I made things worse?)"
    "My throat aches with words I can't shape. He doesn't look at me, and I don't dare look at him."
    "The silence stretches..."
    asidesh2 "(Should I say something… or just leave it alone?)"

    menu:
        "Stay silent.":
            "I press my lips together, forcing myself still. If he doesn't want to talk to me, then maybe silence is the only answer left."
            "Albion continues at his station, the indifferent sound of the grinder filling the air. The words die in my throat, and the distance between us lingers."

        "Break the silence.":
            $ albion_pts += 10
            show screen choice_indicator() 
            asidesh2 "So… what Sylphia said about balancing flavors… Do you think she's right?"
            "The words come out lighter than I expect, almost casual. My heart thumps anyway, waiting for a response."
            "Albion doesn't turn, but his movements slow. He sets the tamper down with more care than usual, his voice low."

            show Albion_Shy3 with dissolve

            al "…Maybe. She notices things others don't."

            hide Albion_Shy3 withh dissolve

            "It's not much. But it's more than silence."
    
    window hide
    show black with dissolve
    window auto
    pause (2.0)
    
    scene kitchen_evening with dissolve
   
    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0

    show Qwynn_A at half_size with dissolve

    q "Albion said what?"
    asidesh "It was my fault. Like you said, I shouldn't have gone to his house."
    q "I don't care. I'm gonna kill him."
    "Qwynn slams their mug down a little too hard on the table, liquid sloshing over the rim. Their eyes flash with a fire I've rarely seen aimed at anyone but me." 
 
    hide Qwynn_A with dissolve
 
    asidesa "I just… don't understand why it made him break down like that. Especially when he's usually so… so… Albion."
    "The word feels clumsy on my tongue, but it's the only way to describe him. Cold, precise, untouchable. Until suddenly, he wasn't."
    asidesh "And Sylphia… she trusted me with this task. I don't think she's happy with our progress so far. I can't let her down."

    show Qwynn_M at half_size
    with dissolve

    "Qwynn's expression softens, but the tension doesn't quite leave their shoulders. They lean forward,  grasping my hand in theirs."
   
    show Qwynn_M at zoom_in, Transform (ypos=-40)
    with dissolve
   
    q "Astra… don't carry all of this by yourself! You're not the only one Sylphia's relying on."
    q "And Albion? If he's too stubborn to admit it, that's on him. Not you."

    hide Qwynn_M with dissolve

    "My best friend's words settle over me like a blanket. I want to believe them, but the image of Albion's glare, the sharpness of his voice, still lingers in my chest."
    asidesa "(Even so… I can't stop thinking about it. About him. About why it felt like I'd touched something more fragile than glass.)"
  
    show Qwynn_N3 at zoom_in, Transform (ypos=-40)
    with dissolve
  
    q "Just promise me one thing, okay? Tell me if he hurts you again. {i}I mean it.{/i}"
    "Their eyes lock with mine, fierce and unwavering."
    "My heart skips, but I laugh it off quickly, deliberately reaching for the nearest cookie to give me an excuse to stop talking."
    aside "You'll eat me out of house and home before that happens."

    hide Qwynn_N3
    show Qwynn_S at zoom_in, Transform (ypos=-40)
    with dissolve
    "Qwynn snorts, the edge of their anger softening into something gentler. But even as they reach for their own cookie, their gaze doesn't stray far from me."
   
    hide Qwynn_S with dissolve
   
    asidesa "(What's up with Qwynn?)"
    asidesa "(For a second, it felt like they were about to say something they'd regret.)"
    asidesa "(But… no, Qwynn wouldn't hide things from me. Would they?)"
    "I shake it off. Still, even as I turn back to my recipe notes, the look in their eyes lingers in the back of my mind."

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    scene cafe_interior with dissolve

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0 
    play ambient "sfx_cafenoise.ogg" fadein 2.0
 
    asidesp2 "A market run? Together?"
    "There is no way this isn't intentional."

    show Sylphia with dissolve

    s "Yes. Together."
    "I glance at Albion. He doesn't even look up from the grinder, but I catch the faint shift of his shoulders, like he's holding back a sigh."
    asidesh2 "Wouldn't it be faster if we split the list?"
    s "This isn't about speed. If you can't manage a simple trip to the market together, how are you going to host a launch event side by side?"
    "Her smile is gentle, but her tone leaves no room for argument. I feel a flutter in my chest—part nerves, part something I don't want to name."
    "Albion finally sets the tamper down and glances at her."

    show Sylphia at Transform (xpos=1250) with ease
    show Albion_N2 at Transform (xpos=300) with dissolve

    al "If that's what you want."
    "No protest, no complaint, but no warmth either, just that unreadable calmness."
    s "Good. The market opens soon. Take this list, and don't come back until you've gotten everything."
    "She presses the parchment into my hands, as if sealing the deal. I tuck it close, trying to ignore the heat in my face."
   
    hide Albion_N2
    hide Sylphia 
    with dissolve

    stop ambient fadeout 2.0

    asidea2 "(Shopping… together. This is going to be awkward.)"

    play music "city_day.ogg" fadeout 2.0 fadein 2.0

    show market with dissolve

    "We walk side by side, though 'side by side' feels generous. Albion's gaze remains on the road ahead. The tension between us stretches like a rope pulled too tight."
    asidesh2 "(Okay… someone has to say something.)"
    aside2 "Alright, so we need… pears, figs, and a few crates of berries. Plus citrus. That's everything on the list, right?"

    show Albion_N2 with dissolve
    
    al "I know. I've read the list."
    "His tone is calm, flat. It leaves nowhere for the conversation to go. The silence falls again, thicker than before."

    hide Albion_N2 with dissolve

    "We pass a stall—that stall. My stomach knots."
    asidea2 "(…This is where it happened. When I was accused of stealing.)"
    "My hand tightens on the basket handle as the memory flashes back: voices rising, the crowd pressing in, and then Albion's voice cutting through, steady and certain."
    asidesa2 "(He saved me. I almost wish he hadn't, because that's what kickstarted all this funny heart business.)"
    "I shake the thought off quickly and step toward the fruit stall. Albion follows without a word, scanning the produce with his usual calm precision."
    aside2 "These figs look good."

    show Albion_N2 with dissolve

    al "Too ripe. They'll spoil before the week is out."

    hide Albion_N2 with dissolve

    "I pout, but put them back. We move down the line, picking over berries and pears, a clumsy rhythm forming: me reaching, him correcting, me sighing. It's not exactly teamwork, but it's something."
    "By the time we reach the citrus stall, the list is nearly complete. The vendor sets down a particularly large crate, oranges stacked high."
    ven "One box, as ordered."
    "I bend down to lift it, hooking my hands under the edges. It doesn't budge."
    asidea2 "(It's too heavy...)"
    "Albion watches for a beat before stepping beside me."

    show Albion_N2 with dissolve

    al "On three."
    "His hands grip the other side of the box. We lift together. My arms strain, the weight biting into my palms—"
    "—and his fingertips brush against mine."

    hide Albion_N2
    show Albion_Shy2 
    with dissolve

    "Again. And again. Each time we adjust our grip, his fingers graze mine like sparks I can't shake off."

    hide Albion_Shy2 with dissolve

    asideem2 "(Why does this feel more impossible than the box itself?)"
    "We heave the crate onto the cart, both of us a little out of breath. Albion steps back, adjusting his gloves like nothing happened."
    "But my fingertips are still tingling."

    show Albion_Shy1 with dissolve

    al "…Careful. You almost dropped it."
    "The words are so simple. Yet something in the way he says them softens the edges. Not a rebuke or a dismissal—but concern."
    
    hide Albion_Shy1 with dissolve
    
    asidean2 "(Don't be nice to me! It makes this all harder!)"
    "I look down quickly, pretending to fuss with the cart handles so he won't see the heat rising in my cheeks."
    asideeb2 "Well, we didn't drop it. So… victory, I guess."
    "The words tumble out, awkward and thin. Too light, too fast, like I'm trying to laugh away the weight in my chest."
    "Albion doesn't answer. He just grips the cart handle and starts pushing, his pace even, eyes forward."
    "I fall into step beside him, clutching the list tighter than I need to. The echoing sounds of wheels on cobblestone makes my chest ache."
    asideem2 "(Curse you, Sylphia.)"
  
    scene cafe_interior with dissolve

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg"
    play audio "<from 0 to 3>bell.mp3"

    "By the time we haul the last crate through the café doors, my arms are sore and my cheeks are still warm." 
    "Albion helps slide the cart into place without a word, then straightens his gloves with his usual composure."

    show Sylphia with dissolve

    s "Well, look at that. You two made it back in one piece."
    "Her eyes sparkle with something between satisfaction and mischief. I narrow mine at her, but she just smiles innocently, as though she hadn't sent us out like that on purpose."
    s "And the list?"
    aside2 "We got everything."
    "I hand her the parchment, a little crumpled now from how tightly I'd been holding it. Sylphia nods, clearly pleased."
    s "Good. Then this partnership might not be so hopeless after all."

    hide Sylphia with dissolve

    "I can't tell if she's teasing, testing us, or both. Beside me, Albion is silent, but I catch the faintest twitch of his brow."
    "Sylphia leans back against the counter, watching us with a small, knowing smile."
    asidep2 "(She's definitely amused. Great. Just what I needed—an audience for my misery.)"
    "I reach for the broom, about to do the usual round of sweeping I always do in the afternoon."
    
    play audio "<from 0 to 3>bell.mp3"
   
    "Just then, the bell above the café door jingles. A tall elf in a sharp waistcoat strides in, briefcase clutched tightly in one hand. His gaze sweeps the counter, then lands on me."
    sf "Good morning. I'm here for my business' catering order."
    "Catering? My heart jumps into my throat."
    aside2 "Uh, catering? I don't think…"
    "I glance at Sylphia, who simply shrugs and points her head at the counter before making herself scarce."
    "Then I spot it: a slip of paper half-crumpled on the floor by the register. I snatch it up, and my stomach twists at the bold letters at the top: 'Catering Order'."
    "The broom in my hand clatters to the floor."
    asidesp2 "(Oh no.)"
    asidesp2 "Yes! Right. We… we have your order. Just give us a few minutes to prepare it."
    "Albion looks at me sharply, but I'm already moving."

    show Albion_SC with dissolve

    al "Coffee. I'll handle it."
    "His voice is brisk, businesslike."
    aside2 "Food and packaging on me."

    hide Albion_SC with dissolve

    "And we're off."
    "Albion stations himself at the espresso machine, the hiss and sputter of steam already filling the air."
    "I duck into the kitchen, pulling trays of pastries, slicing sandwiches with hurried precision, sliding them into boxes."
    
    show Albion_SC with easeinright
    
    al "How many cups?"
    aside2 "Twenty. Ten black, five macchiatos, five cappuccinos."
    al "Got it."

    hide Albion_SC with easeoutleft

    "He moves like clockwork, every motion sharp and sure. The dark liquid streams into cups, completely controlled."
    aside2 "I'll need those milk ones first. The sandwiches are nearly done, and they'll go on the top layer."

    show Albion_SC with dissolve

    al "Coming."
    "He passes two steaming cups across the counter. I slide them into a carrier without missing a beat, balancing a tray of sandwiches with my other hand."
   
    hide Albion_SC with dissolve
   
    asidesp2 "Watch your left. I'm coming through!"
    "Our shoulders brush as I cross past him. He doesn't flinch, doesn't falter. Just keeps working, steady as stone."
    "I load pastries into a box, then reach for the next stack of tarts." 
    "Then, my grip slips—the box wobbles dangerously."
    asidesp2 "Ah!"
    "Before I can panic, a hand steadies it from below. Albion's."

    show Albion_N2 at zoom_in, Transform (ypos=-40) with dissolve

    al "Focus."
    "His eyes flick up to mine for the briefest second before he withdraws and turns back to the machine."
   
    hide Albion_N2 with dissolve

    asidea2 "(Right. Focus. No mistakes.)"

    show Albion_N2 with dissolve

    al "Cappuccinos are done. Long blacks are next."

    hide Albion_N2 with dissolve   

    aside2 "Good. Pastries sealed. Passing them over."
    "I slide the finished boxes toward him; he checks the slip, marking them off with quick precision."

    show Albion_N2 with dissolve

    al "We're missing two fruit trays."
    asidesp2 "I'm on it. Berries, pears, figs—just keep the coffee coming."

    hide Albion_N2 with dissolve 

    "I dart back into the kitchen, assemble the trays with trembling fingers, and set them down just as Albion finishes the last pour."

    show Albion_N2 with dissolve

    al "All twenty, lined up."
    aside2 "Food's ready too. Start packing."

    hide Albion_N2 with dissolve

    "We fall into rhythm again: lifting, stacking, securing boxes. He ties knots in the twine while I slide parchment between layers." 
    "When one carrier wobbles, he braces it without needing me to ask. When my hands are full, he wordlessly passes tape across the counter."
    "No wasted motions. No hesitation."
    aside2 "(For now, it's like the fight never happened. Just two people working in sync.)"
    "The last box clicks shut. The final cup slides into place. Together, we step back, breathless, facing the completed order stacked neatly by the counter."
    "The café is quiet again, save for the faint hiss of the cooling machine."
    asidee2 "We… did it."

    show Albion_N2 with dissolve

    al "Of course we did."
    "No warmth in his tone, but no sharpness either. Just facts. My heart skips anyway."
  
    play audio "<from 0 to 3>bell.mp3"
  
    "The bell above the café door jingles again. The business elf returns with two coworkers in tow, their hands already outstretched to take the boxes and carriers."
   
    hide Albion_N2 with dissolve
   
    sf "Excellent. Thank you very much."
    "They divide the order quickly, murmuring their gratitude as they load everything into their arms."
    "Then they leave, door swinging shut behind them, and the sound of their voices fade down the street. The café is quiet again."
    asidesm2 "That was intense."
    asidesp2 "Albion—"

    stop music fadeout 3.0

    "I turn toward him, but he's no longer at the counter. A faint creak from the back tells me the break room door has already shut."
    asidea2 "(…)"
    asidean2 "(Am I really just going to let him shut me out again?)"
    "For the first time since our fight, it isn't sadness that grips me—it's something hotter, sharper."
    "A spark that feels like adrenaline… like anger."
    "Before I can second-guess myself, I tear off my damp gloves and march toward the break room after Albion."

    stop ambient fadeout 2.0
   
    jump Albion_chp3

#########################################
# END
#########################################









