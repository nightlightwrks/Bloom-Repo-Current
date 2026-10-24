# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



#########################################
# QWYNN CHAPTER 1 
#########################################

label Qwynn_chp2:
  
    $ persistent.status_button = True
    
    window hide
    show qwynn_chp2 with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0
    scene kitchen with squares

    "It's been a few days since I started working on the marketing campaign."
    "Today, Qwynn and I are sitting on the living room floor surrounded by half-finished designs and coffee mugs."
    "Qwynn is due for one of their excursions out of the city soon, so I'm trying to make the most of their expertise while they're still here."
    
    show Qwynn_S at half_size with dissolve
    
    q "Okay, hear me out. What if we go with a vintage look? You know, those old café posters with the dramatic lighting?"
    asidesh "That sounds expensive to commission."
    q "Not if we do it ourselves! I can draw them, add a little flair, and bam! Instant charm."
    q "I believe in the power of flair. It's the unsung hero of marketing."

    hide Qwynn_S with dissolve

    "They grin and lean over their sketchpad, sweeping a quick outline of a coffee cup with swirling steam. Their lines are confident and quick, a big contrast to mine."
    "My own rough draft pales in comparison: plain, practical, black text on white paper. Frankly, mine looks more like an invoice than anything."
    aside2 "I'm not sure if Sylphia would want something super dramatic. Maybe we could meet in the middle?"
    
    show Qwynn_N3 at half_size with dissolve

    q "You want something that feels like Bloom."
    asidesp "Exactly."
    "Just as Qwynn is about to reach for the lighter colors—"

    hide Qwynn_N3 with dissolve
    play sfx "sfx_shake.ogg"

    "{i}SMASH.{/i}"
    asidesp "Oh my gosh, Midna!"
    "The pencils scatter across the floor. I reach out, only to be met with the swipe of a paw."

    show midna with dissolve

    #TODO insert meow sfx
    "MIDNA" "miaow~"

    hide midna with dissolve

    "Midna is a stray kitten Qwynn and I adopted recently. Qwynn found her in their boutique last week, rummaging through the stock."
    "She darts across the floor, batting the exact brown pencil Qwynn needs all the way under the couch."
    
    show Qwynn_S at half_size with dissolve
    
    q "Midna is so spoiled."
    asidesm "…Kinda like you."

    hide Qwynn_S 
    show Qwynn_B at half_size 
    with dissolve

    q "I'm not spoiled!"
    asidesm "Whatever you say!"

    hide Qwynn_B with dissolve

    "It's true though—Midna reminds me of Qywnn. I love that they're both so free-spirited and nimble, and say and do whatever is on their minds."
    "It also helps that Midna's fur colour is the same as Qwynn's ears."
    "Qwynn pouts as they get back to work, gently shading the outline of a mug."

    show Qwynn_N3 at half_size with dissolve

    q "Y'know, Bloom is more than coffee, right? It's got a certain atmosphere. That 'I could stay here forever' feeling."
    asidesh "You make it sound like a dream."
    q "That's the point. We're in Halis; there's good coffee everywhere. So, let's sell to people looking for that second home."
    
    hide Qwynn_N3 with dissolve

    "Their words echo something they told me a couple of days ago… 'You don't just sell things. You sell emotions – the feeling behind them.'."
    "I look at Qwynn, bent over the page, the afternoon light brushing against their hair."
    "I find myself thinking..."

    menu:
        "Qwynn looks pretty.":
            $ qwynn_pts += 10
            show screen choice_indicator(QWYNN_COLOR) 
            "I catch myself watching them a little too long, tracing the way the light catches on their hair, and blue eyes. My face feels a little warm."
        "Qwynn is so reliable.":
            "I smile quietly. Qwynn always knows how to make things feel manageable no matter how chaotic they are."
        
    # BRANCHES CONVERGE HERE
    "A beat later, Qwynn looks up from their sketchpad, a small grin tugging at their lips. I realize too late that I've been staring."

    show Qwynn_S at half_size with dissolve    
    
    q "You've been staring at me for a while now. Have you fallen for me?"
    "I scoff."
    asideem "Please. If I fell for you, who would keep you humble?"
    q "Fair point. Though, for the record, I'm very humble."
    asidesm "Says the person who just called themselves the 'unsung hero of marketing.'"
    q "Hey, someone's gotta sing about it eventually."
    "They laugh, the sound light and easy, and I can't help but smile too."
    q "Alright, Ms. Marketing Manager, how about a break? You've been frowning at those flyers for an hour."
    asidep "I was focusing."
    q "Same thing, different face."
    
    hide Qwynn_S with dissolve
    
    "I roll my eyes, but I follow Qwynn out of the door regardless."
    "We always have to check before we close the door now so Midna doesn't escape."

    #SCENE: Qwynn and Astra begin working together
    #[MORNING]

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior with dissolve

    asidesp "Pick a color palette."
    "I hold up two striped cards. Qwynn and I spent half the night mixing paints in our living room, narrowing it down to these two. My fingertips still smell faintly of gouache."
    "Sylphia leans forward, thumb on her chin."

    show Sylphia with dissolve

    s "I think the pastels are brilliant~ Did Qwynn help with this? I'm going to have to put them on our payroll!"
    asideeb2 "(Qwynn would love to hear that.)"
    "Sylphia tilts her head, squinting at the left card."
    s "Though, hmm. I'm not quite sure about this one..."
    "She taps the striped palette on the left. It's the one Qwynn mixed more than I did."
    s "The colors are very different. Bold on bold. They're beautiful alone, but together... they overwhelm each other."
    "My breath catches in surprise. Did I somehow make a better palette than Qwynn?"
    s "Maybe you should get a second opinion."
    "I turn to Albion."

    hide Sylphia
    show Albion_SC 
    with dissolve

    asidesm2 "Pick a color palette."
    "Albion narrows his eyes at me."
    asidep2 "Okay, fine. I'll find someone with an eye for color."

    hide Albion_SC with dissolve

    "Behind us, Sylphia laughs."

    #SCENE: Astra asks for Felix's opinion
    # outside

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    stop ambient fadeout 2.0
    play music "city_day.ogg" fadeout 2.0 fadein 2.0
    scene market with dissolve

    "Block 5, Block 5..."
    "I weave through the familiar stretch of the market. It's noisy and alive, every voice overlapping with the next. I wave to a few vendors I've gotten to know."
    "I spot Felix exactly where he was the first time I met him, perched on a small stool, painting bright flowers along the window frame of that same shop. Brush in hand, concentration etched on his face."
    aside "Looks like the garden is growing."
    
    show Felix with dissolve
    
    f "Astra! Good to see you again! Out shopping?"
    "The corners of my mouth lift. Felix's smile is as bright as his paint palette—it's incredibly infectious."
    asidesp "I was actually looking for you."
    "Felix puts a hand to his heart dramatically, widening his eyes in mock shock."
    f "Oh no. What ever shall I do? Seems I've attracted an admirer."
    asidesm "Please. I don't admire people who brag about their popularity."
    f "You wound me. I would only brag a little. Maybe paint your portrait as thanks."
    "We both laugh. Felix's teasing has a way of lightening the air around him."
    aside "Anyway, I wanted your opinion on these colors—"

    hide Felix with dissolve

    q "Astra!"

    show Qwynn at half_size 
    with dissolve

    "I turn. Qwynn stands a few steps away, hands planted on their hips. They look a little exasperated."

    hide Qwynn
    show Qwynn_N3 at half_size
    with dissolve

    q "I was waiting for you in front of Bloom! I thought we were working on the posters tonight."
    asidesp "I thought you'd be waiting back at the apartment?"

    hide Qwynn_N3
    show Qwynn_N3 at half_size, left:
        xpos 200
    with ease
    show Felix at right:
        xpos 900
    with dissolve

    f "Oh? Are you Astra's friend?"
    asidesp "This is Qwynn. They're my best fr—"
    
    hide Qwynn_N3
    show Qwynn_S at half_size, left:
        xpos 200
    with dissolve

    q "Astra's my roommate!"
    "Qwynn loops their arm around mine before I can finish the sentence. Felix raises an eyebrow, amused, then chuckles softly."
    f "You two seem close. Anyway, I should finish these flowers before my meeting. I'll see you around!"
    "He waves a paint-speckled hand and returns to his work."

    hide Felix with dissolve
    hide Qwynn_S
    show Qwynn_S at half_size:
        xpos 500
    with ease

    "As Qwynn and I step away from the flower shop, their arm stays linked with mine."
    asidesp "Weren't Felix's paintings pretty?"

    hide Qwynn_S
    show Qwynn_N3 at half_size:
        xpos 500 
    with dissolve

    "Qwynn shrugs."
    q "They look like regular flowers to me."
    asidesp "Really? I thought they were pretty. Maybe it's Felix himself then. He kinda feels like sunshine."
   
    hide Qwynn_N3
    show Qwynn at half_size:
        xpos 500 
    with dissolve    
    
    q "That's his job, Aste. People commission friendly artists. I'm like that with my customers too."
    aside "I meant that Felix has a nice smile."

    hide Qwynn
    show Qwynn_S at half_size:
        xpos 500 
    with dissolve    

    q "So do I!"
    asidesm "Yours is different. Less... blinding?"

    hide Qwynn_S
    show Qwynn_N3 at half_size:
        xpos 500 
    with dissolve

    q "Less blinding? Wow. Amazing compliment. Thank you so much."
    asidep "You know what I mean."
    q "Do I?"
    "They nudge my shoulder with theirs playfully, but there's a faint edge under it. Something prickly. They're trying very hard not to sound bothered."

    hide Qwynn_N3
    show Qwynn_S at half_size:
        xpos 500 
    with dissolve  

    q "Whatever. Let's get out of the market. We have posters to make, right?"
    "I think for a moment."   

    hide Qwynn_S with dissolve
    
    menu:

        "Are you jealous?":
            $ qwynn_pts += 10
            show screen choice_indicator(QWYNN_COLOR) 
            asidesm "Qwynn... are you jealous?"
            "Qwynn chokes on their own breath. They stand a little straighter, eyes wide."
            show Qwynn_B at half_size with dissolve
            q "Me? Jealous? Of what?"
            aside "Um. Of Felix's paintings?"
            hide Qwynn_B
            show Qwynn_S at half_size
            with dissolve
            "They laugh way too quickly."
            q "Absolutely not. I'm much better. I have my own boutique."
            hide Qwynn_S with dissolve
            "I almost point out Felix has his own studio too."

        "I think your collection is better.":
            asidesp "Don't worry, Qwynn. I think your collection is much cooler."
            show Qwynn_S at half_size with dissolve
            q "Well. Obviously. I have my own boutique."

    asidesp "Speaking of the boutique, did you close early?"

    hide Qwynn
    show Qwynn_N3 at half_size
    with dissolve

    q "Hm?"
    aside "Well, you said you were waiting at Bloom for me. And it would've taken time for you to get from there to here."
    q "Ah, yeah. I did close early. I don't get much foot traffic around this time anyway. I'm thinking of hiring another part-timer to cover the slow hours, or when I go on a trip."
    asidesp "What about your current employees? You said they're the only ones you'd trust with your store. What changed?"
   
    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve
   
    q "Y'know, the business grew. Something, something, the power of marketing. My baby is all grown up now."

    hide Qwynn_S with dissolve
    show qcutin1 with easeinleft 

    q "Besides, you need me!"

    hide qcutin1 with easeoutright

    asidesa "(A part-timer, huh?)"
   
    menu:
        "That sounds like a good idea.":
            asidesp "That sounds like a good idea."
            show Qwynn_S at half_size with dissolve
            "Qwynn brightens immediately. Their arm tightens around mine with an excited squeeze."
            q "Right? I figured it'd help me focus on the busy hours, the creative stuff. And maybe keep the boutique open more consistently."
            hide Qwynn_S with dissolve

        "Isn't it better to be there yourself?":
            $ qwynn_pts += 10
            show screen choice_indicator(QWYNN_COLOR) 
            show Qwynn_N3 at half_size with dissolve
            q "You think so?"
            asidesh "Well... people come to Voyage Étoilé because of you. Your eye, your style. That's what makes it special."
            hide Qwynn_N3
            show Qwynn_B at half_size
            with dissolve
            "Color touches their cheeks faintly. They look down, then back at me, eyes softer than before."
            hide Qwynn_B 
            show Qwynn_M at half_size
            with dissolve
            q "You always know how to say things like that. Makes it hard not to try a little harder."
            hide Qwynn_M with dissolve

    "I grin as  we continue to amble together down the cobblestone street, market noise fading behind us."
    hide Qwynn_M
    show Qwynn_S at half_size
    with dissolve
    q "Oh, you're still wearing your bracelet, Aste!"
    asidee "Of course! I never take it off. Though maybe I should when I'm eating something messy."
    asidesp "Which reminds me—do you want to grab some ice cream before we head home?"
    "Qwynn flashes a devilish look."
    q "Sure. But it's your turn to treat."

    #SCENE: Qwynn goes above and beyond

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0
    scene kitchen_evening with dissolve
    
    "When we get home—still licking the last of the ice cream from our lips—I catch a whiff of paper and ink."
    "Qwynn drops their bag by the door and clears their throat."

    show Qwynn_N3 at half_size with dissolve
    
    q "Hey, before you say anything, I want to show you something."
    asidesp "Oh?"

    hide Qwynn_N3 with dissolve

    "They disappear into their room and come back almost immediately, arms full."
    "They set everything down on the table with a flourish:"
    "Poster boards. Stacks of flyers. Carefully labeled envelopes. A whole mock display stand folded neatly under one arm."

    show Qwynn_S at half_size with dissolve
    
    q "Ta-da."
    "I stare. Midna also jumps on the table to stare with me."
    "There are at least six different flyer designs, fully inked and finished. Variations in color, layout, typography. One even has a hand-drawn border that mirrors Bloom's window frames."
    aside "Qwynn… when did you do all this?"
    q " I couldn't sleep, so I thought I'd get ahead of things. Consider them all a starting point."
    asidesa "('Starting point,' they say.)"
    "I pick one up. The paper is thick and expensive-looking."
    asidesp "This is days of work!"
    asidesh "You didn't have to do all this."
    q "I know. I wanted to."
    asidesh "It's incredible. Really. Thank you."
    asidesa "(It's just—a lot.)"
    "I look down at the sheer amount of material again."
    aside "What am I supposed to tell Sylphia?!"
    q "That you have an extremely competent marketing assistant?"
    asidesp "She's going to think I hired a whole agency."
    "They laugh, and I do too, but something in my chest twists."

    hide Qwynn_S with dissolve

    "I imagine the hours this must have taken. The late nights. The quiet apartment while I slept."
    "A thought flickers: how much of this did Qwynn do because they wanted to..."
    "and how much because they felt they had to?"
    asidesa "(Why am I even thinking like this?)"

    show Qwynn_B at half_size with dissolve

    "I reach out and squeeze their hand. My bracelet glints under the ceiling lamps."
    aside "I appreciate it. I really do. But please don't push yourself. This is {i}my job.{/i}"

    hide Qwynn_B
    show Qwynn_S at half_size
    with dissolve
    "Their smile softens at that, eyes flicking away for just a second."
    q "I wanted to. Anything for my best friend, right?"

    #SCENE: Qwynn cooks for Astra
    # scene black

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0
    scene kitchen with dissolve
    
    "For the next couple of days, Qwynn and I settle into a routine."
    "I work my shift at Bloom, and Qwynn picks me up after closing."
    "We walk home together, talking about nothing and everything, then spend the evening spread out across the apartment floor with posters, flyers and unfinished campaign plans."
    "Some nights we give in and get takeaway. Other nights we eat out. But most of the time, Qwynn insists on cooking."

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0
    scene kitchen_night with dissolve
        
    "Tonight, they have a sauce simmering gently on the stove, thick and glossy and speckled with herbs. The smell of garlic and butter fills the kitchen."
    asidee "It smells really good. You're making pasta?"
    
    show Qwynn_S at half_size with dissolve
    
    q "I'm curating pasta. Big difference."

    hide Qwynn_S
    show Qwynn at half_size
    with dissolve

    "They taste the sauce, frown, then add another teaspoon of seasoning."
    asidesm "Didn't you say too much seasoning ruins everything?"

    hide Qwynn
    show Qwynn_S at half_size
    with dissolve

    q "For steak, yes! Pasta is more forgiving. Also, I have learned from my mistakes."
    asidesm "Have you?"
    q "I choose to believe I have."

    hide Qwynn_S with dissolve

    "I lean against the counter, petting Midna, watching Qwynn move around the kitchen."
    "Their apron's a little crooked, and there's sauce on their sleeve. They don't notice."
    asideeb "I'm going to miss you when you go on your trip."
    "The words slip out before I think about them. I was supposed to say 'your cooking', but somehow my brain replaced it with 'you'."
 
    hide Qwynn_S
    show Qwynn_B at half_size
    with dissolve

    q "That's the first time you've said that."
    "Qwynn is blinking at me, ladle paused mid-stir."

    hide Qwynn_B
    show Qwynn at half_size
    with dissolve

    "I hesitate, then add more quietly."
    asidesh "I feel a bit bad. I haven't really been cooking much lately."

    hide Qwynn
    show Qwynn_N3 at half_size
    with dissolve

    q "Don't sweat it. You're busy, Aste."
    "I bite my lip."
    asidesa "(So are they.)"

    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve

    q "Besides, the best way to thank me is to give me completely honest, unfiltered feedback."
    asidesm "Last time you almost burst into tears when I said you added too much salt."
    q "The risotto was perfect. You just don't have a palate."
    "They plate the pasta with a flourish—sliding one dish toward me like it's a grand reveal."
    q "Moment of truth."
    asidesm "If this is too salty, I'm saying nothing."
    q "Coward."

    hide Qwynn_S with dissolve

    "I laugh as I take a bite. The sauce is rich and comforting and goes well with the chicken, exactly what I needed after a long day."
    asidee "It's good. Really good."

    show Qwynn_S at half_size with dissolve

    q "See? Trust the process."
    "Qwynn chucks Midna a piece of plain chicken."

    hide Qwynn_S
    show midna 
    with dissolve

    "MIDNA" "Miaow~"

    hide midna with dissolve

    "Later, while Qwynn cleans up, I drift back into my bedroom."

    scene bedroom_night with dissolve

    "I sit on the edge of the bed, staring at nothing in particular."
    asideem "(There has to be something I can do to thank Qwynn for everything they've done these past few days.)"
    
    #SCENE: Astra thinks about a gift
    #SCENE: BLOOM

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior with dissolve

    "CUSTOMER" "—and a cortado. With a chocolate croissant."
    asidesp2 "Excellent choice!"
    "I reach for the portafilter, muscle memory taking over as I tamp the grounds and lock it into place. The espresso machine hums to life, steam curling up into the air."
    aside2 "(Cortado. Equal parts espresso and milk. Balanced.)"
    "My hands move automatically as my thoughts drift—to the present for Qwynn."
    asidesa2 "(What do you gift to someone who's already seen the world? Who comes home with suitcases full of souvenirs?)"
    aside2 "(Qwynn has trinkets from all over Feldoria. And they run a boutique. They're literally a walking gift shop.)"
    "The milk steams. I pour carefully, watching the crema settle just right."
    "I slide the cup across the counter, leaning forward a little so the dwarven woman can reach it."
    asidesp2 "Here you go!"
    "CUSTOMER" "...Did you forget my croissant?"
    "My stomach drops."
    asidesp2 "Oh—! I'm so sorry!"
    "I turn quickly, heart sinking as I open the oven. The smell hits me immediately."
    asidesa2 "(Burnt.)"
    "The last chocolate croissant is blackened at the edges."
    asidesh2 "I'm really sorry. That was the last one. I can offer you something else on the house if you'd like."
    "The customer waves a hand."
    "CUSTOMER" "It's alright, dear. I'll take something simple instead."
    "As I rush to fix the order, Albion walks closer, lowering his voice."

    show Albion with dissolve

    al "You don't usually burn pastries."
    asidesh2 "Yeah. Sorry. I just got lost in thought for a second."
    "He stares at me for a second, looking like he's questioning what he's about to do next."

    hide Albion
    show Albion_SC
    with dissolve

    al "...About?"
    aside2 "Qwynn. I'm trying to figure out a gift for them, but it's impossible. They travel constantly. They already have everything."
    
    hide Albion_SC with dissolve

    "The customer chuckles softly as she accepts her replacement pastry."
    "CUSTOMER" "Oh, my husband's the same. Travels all the time. Can never get him a thing."
    "She smiles, warm and knowing."
    "CUSTOMER" "The most important gift for him isn't something you can wrap. It's quality time."
    aside2 "Quality time?"
    "CUSTOMER" "Yep."
    aside2 "My friend did say that the feeling behind something matters more than the product."
    asidesh2 "But maybe they were talking about Voyage Étoilé."
    "The customer's face scrunches a little."
    "CUSTOMER" "Oh, you know the owner? I ordered a few things from there last week for myself. Lovely owner. Shame that my stuff has still not been delivered."
    "I chuckle."
    aside2 "Qwynn must've missed the order."
    asidesa2 "(Odd. They're usually so attentive.)"
    "CUSTOMER" "I've been having bad luck with my purchases, haven't I? Perhaps it's the Saints' way of telling me I'm spending too much."
    "CUSTOMER" "Anyway, I have to run to work. Thanks for the coffee."
    asidesp2 "No, thank {i}you{/}. Sorry about the croissant again."
    "She gives a small wave before exiting the café."
    aside2 "(Quality time…)"
    asidesa2 "(Is that what would make Qwynn happy? We live together.)"
    "I watch the steam rise from the espresso machine, my thoughts finally clicking into place—and I get an idea."

    #SCENE: Dinner

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0
    stop ambient fadeout 2.0
    scene kitchen_night with dissolve

    "At dinner, I enact my plan."
    asidesp "I have tomorrow off."
    
    show Qwynn_N3 at half_size with dissolve
    
    q "Oh?"

    hide Qwynn_N3 
    show Qwynn_S at half_size
    with dissolve

    "Their eyes light up immediately."
    a "And you need to keep tomorrow evening free. Like... actually free. No coming home early."
    q "Wow. Is Astra the planner extraordinaire finally making an appearance?"
    asidea "(That's because you never give me a chance to plan anything for us.)"
    q "I knew it. The world really is ending."
    "They grin at me, clearly enjoying this."
    asidesp "Just don't ask questions! Trust me."
    q "Ooooh. Mysterious. Do I need to dress up? Or be emotionally prepared?"
    aside "Emotionally prepared, probably."
    q "Dangerous words."
    "They laugh and take another forkful of leftover pasta."
    q "I'm looking forward to it. Honestly, my regulars will probably be glad Voyage Étoilé is closing at a normal time for once."
    hide Qwynn_S with dissolve

    menu:
        "Agree with Qwynn":
            asidesm "You and your endless charm with your customers."
            show qcutin1 with easeinright
            q "Keeping the economy flowing."
            asidesm "Well, we're doing that by blowing too much on takeaway and late-night snacks."
            q "That's not true! We've been keeping our takeouts cheap!"
            asidesm "—and we'd definitely spend it on dessert too."
            hide qcutin1 with easeoutleft
            "Qwynn rolls their eyes."

        "Pause.":
            $ qwynn_pts += 10
            show screen choice_indicator(QWYNN_COLOR) 
            asidesh "...If helping me with my marketing campaign is affecting your business, you should've told me, Qwynn."
            show Qwynn_N3 at half_size with dissolve
            q "What? No, no—it's completely fine. We're getting that part-timer soon, remember? This is just a transitionary period."
            asidean "My marketing campaign doesn't take priority over your entire boutique."
            q "And it doesn't! It's fine, Aste. Really."
            hide Qwynn_N3
            show Qwynn at half_size 
            with dissolve
            "Their smile is still there, but it's thinner now."
            "Neither of us speaks."
            "Finally—"
            hide Qwynn
            show Qwynn_N3 at half_size 
            with dissolve
            q "Anyway. Tomorrow's good. Let me know if you need me to bring anything back for your grand surprise."
            "They shove a big forkful of pasta into their mouth."
            q "And, really, everything's fine. It's my shop, you know. You worry too much."
            asidesh "If you say so."
            q "I do."
            hide Qwynn_N3 with dissolve
    
    "We keep eating. The pasta on my plate has cooled a little."
    "My plan runs through my head again."
    "Ten courses. All of Qwynn's favorites. Cooked at our apartment—thoughtfully, with all my heart. A special dinner experience for someone who never lets themselves just {i}be the guest.{/i}"
    asideem "(I hope this will convey to Qwynn how much these past couple weeks meant to me.)"

    #SCENE: Shopping for ingredients

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "city_day.ogg" fadeout 2.0 fadein 2.0
    scene market with dissolve

    aside "(Qwynn loves sweet things. Anything rich, with cream or milk. Comfort food.)"
    "I stroll through the busy market, basket in hand. I pause at a pastry stall first."
    aside "(I could start off with milk bread rolls... glazed with honey butter.)"
    aside "(They're small enough to be eaten in a few bites, soft and appetizing. A good beginning.)"
    "Further down, a cheesemonger offers samples. I add a small round of triple-cream cheese to my basket, already imagining it paired with something sweet. Maybe figs. Maybe pear."
    "By the time I reach the fruit stand, my basket is heavy."
   
    show Felix with dissolve

    f "Astra!"
    "I turn and laugh as Felix steps into view, paint smudged faintly on his knuckles like always."
    f "Still looking for that opinion of mine?"
    asidesp "Not about colors anymore. But... are you open to opinions on a ten-course dinner?"
    f "Ten courses? Someone's becoming a chef!"
    aside "I'm just cooking it at home. I'm trying something a little fancier than the regular dinner."
    "He peers into my basket with exaggerated focus."
    f "You know, Velvet runs a degustation course at the restaurant. He spent a whole three months learning how to decorate and plate those small plates in a fine-dining type of way."
    asidesp "(Three months!?)"
    f "Each dish has to stand on its own but still feel like part of a whole meal. Texture, temperature, color... it all matters when it's a degustation course."
    f "Or so they say. I've never actually been."
    "We start walking together, weaving through the stalls. Felix grabs a bag of sugar-dusted almonds and hands it to me."
    f "For crunch!"
    asidesm "I'll trust the expert."
    "As we walk, he glances at me sideways, casual but curious."
    f "So. Is this dinner for your roommate?"
    asideem "(He put extra emphasis on the last word.)"
    aside "Yeah."
    aside "We met when we worked at the same restaurant, and they kind of took me under their wing."
    "I smile without realizing it, and explain to Felix how we met."
    "Felix hums thoughtfully as I explain."

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    scene market
    show Felix 
    with dissolve

    a "...They've always been there for me. From my job back then to my job now... I just want to do something for them."
    f "You know, from the way you talk about them, it sounds like Qwynn would move the world for you if you asked."
    "I stop for a moment, fingers tightening around the basket handle."
    asidesh "Sometimes I wish they'd be a little more selfish."
    "The words surprise me as they leave my mouth. I want Qwynn to be more selfish?"
    aside "But they're going on a trip soon."

    hide Felix
    show Felix_C 
    with dissolve

    f "Ah."

    hide Felix_C
    show Felix
    with dissolve

    "He smiles gently, like he understands more than I've said."
    f "Well, distance makes the heart fonder. Is that why you're doing all this?"
    aside "Yes—"
    "I hesitate, then shake my head."
    asideb "—and no. I'm doing this because I want to."
    "Felix's smile widens, softer now."
    f "Then it'll be a good dinner."

    #SCENE: Special dinner

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0
    scene kitchen_evening with dissolve

    "The apartment is baked in the smell of butter and sugar."
    "I move from stovetop to counter to stovetop. My hands are busy; my mind is racing. There's a lot to do. Sauces to check, plates to warm, timing to watch."
    "On top of that, I need to keep Midna from stealing bites of food she can't eat."
    "My heart thumps every time I glance at the clock."
    asideem "(It'll all be worth it.)"
    "I picture Qwynn's reaction when they see the dishes. When they taste them— The way their eyes always light up over something sweet, the way they—"
    "I stop myself."
    asideem "(Focus, Astra!)"

    play audio "dooropenclose.mp3" #open and close

    "I wipe my hands on my apron just as the door clicks open."
    "Qwynn steps inside, stopping a bit abruptly in the entryway. Midna scuttles to greet them."
    asidesm "Were you waiting outside until it was exactly the right time?"
    "They throw their hands up in surrender."
    
    show Qwynn_S at half_size with dissolve

    q "Alright, you got me."
    "I laugh despite myself, tension easing just a little."
    asideeb "Go sit down. No peeking."
    q "Ooo, commands now? What happened to my mild-mannered roommate?"
    asidesm "You think I'm mild-mannered?"
    q "You're right. I take that back."
    "Qwynn does as they're told, settling into their usual spot at the table. I follow a moment later, placing a folded card in front of them."
    "It looks like a menu. Because it is."
    q "...Is this a degustation list?"
    asideeb "Maybe."
    q "Wow. So this is it. You're leaving Bloom for the fine dining industry."
    asideem "Don't be dramatic."

    hide Qwynn_S with dissolve
    show qcutin2 with easeinright

    q "Too late, Aste. I'm already telling people I knew you before the reservations were impossible to get."
    
    hide qcutin2 with easeoutleft

    play music "Qwynn.ogg" fadeout 2.0 fadein 2.0
    "I bring out the first dish: soft milk bread rolls, still warm, nestled in a small basket. Beside them sits a slab of garlic butter, cut into careful ridges like petals."
   
    show Qwynn_S at half_size with dissolve

    q "When did you learn how to sculpt butter?"
    asidesh "(Albion taught me, but for some reason, I don't want to mention him.)"
    aside "It won't affect the taste."
    q "I disagree. It tastes better {i}because{/i} it looks fancy."
    "They tear into the bread immediately, eyes lighting up as the butter melts into it."
    q "This is dangerous. You can't start like this. I'm supposed to pace myself."
    asidesm "You'll survive."
    "They do more than survive. By the time the basket is empty, Qwynn is already licking butter from their fingers without shame with a contented look on their face."
    
    hide Qwynn_S with dissolve

    "I clear the plates and return with the second course: slow-braised fennel with a burnt honey glaze, plated delicately with almonds and a small drizzle of sauce."
    
    show Qwynn_S at half_size with dissolve

    q "Okay. I know the order of the dishes from the menu, but this presentation is blowing my mind."
    "They take a bite, then another, slower this time."
    asideem "(I need to look away. I'm staring at Qwynn's mouth too much. Why am I doing this?)"
   
    hide Qwynn_S with dissolve

    "The plates are cleared again. My nerves hum under my skin, but Qwynn's smile keeps me on my feet."
    "{i}I'm doing this because I want to.{/i} That's what I said to Felix."
    "So I shouldn't be watching Qwynn so closely. I don't need their approval."
    asidesa "(...do I?)"
    "My dating experience is limited, but I know enough to recognize this feeling. I shouldn't be surprised. I'm attracted to people of any gender—it's just that…"
    "Qwynn is my best friend. Do I really—"
    asideem "(Okay Astra, stop. This isn't even remotely relevant.)"
    "I set down the next dish—hard."
    "The third dish is hand-rolled pasta. Creamy, rich, familiar in the best way. Comfort food dressed up just enough to feel special."
    q "…Hey."
    asidesp "What?"
    
    hide Qwynn_B
    show Qwynn_S at half_size
    with dissolve
    
    q "This tastes kind of like the pasta from that restaurant we used to work at."
    "I freeze for half a second. Then I straighten, hands on my hips, the way Qwynn always stands."
    asidea "{i}Wow. Amazing compliment. Thank you so much.{/i}"
    q "Hey! That was a genuine observation."
    asidesm "Uh huh. I could hear the awe dripping from it."
    q "We should visit that place next week for old times sake."
    "They grin."
    q "Maybe brag a little about how much better we are now."

    hide Qwynn_S with dissolve

    "I laugh and turn toward the kitchen."
    aside "Qwynn, stop baiting me. I know you'll be on your trip next week."
    "They wave a hand, casual."
   
    show qcutin1 with easeinleft
   
    q "Oh, about that. I decided to push my trip back until Bloom's marketing campaign is done."
   
    hide qcutin1 with easeoutright

    #play music "tension.ogg" fadeout 2.0 fadein 2.0
    stop music fadeout 3.0

    "Something in me finally snaps."
    asidean "{w}{i}What?{/i}"

    show Qwynn_S at half_size with dissolve

    q "It was a bit of a pain having to reschedule with the coach I'm taking, but the driver was about to swap me with some other guy. It all worked out in the—"
    asidesp "Wait. Time out, Qwynn."
    "I turn fully to face them."
    asidesp "Why are you rescheduling your trip? You were looking forward to it! You {i}love{/i} travelling!"
    q "I just told you. Bloom's marketing campaign isn't done."
    asidean "That's too much, Qwynn! You can't drop everything just to help me."

    hide Qwynn_S
    show Qwynn at half_size 
    with dissolve

    asidean "You're abandoning the boutique, staying up late, cancelling a trip—is this what you really want?"
    asidean "You don't need to go this far! I was actually looking forward to a bit of alone time."
    "Qwynn's expression falters."

    hide Qwynn
    show Qwynn_M at half_size
    with dissolve

    q "Aste… what do you mean? If you want some alone time, I can still go. I'll find another coach tomor—"
    asidean "That's not the problem! You're still doing it for {i}me{/i}."
    
    hide Qwynn_M
    show Qwynn_N3 at half_size
    with dissolve
    
    play music "tension.ogg" fadeout 2.0 fadein 2.0

    q "I'll do anything for you! I'm {i}happy{/i} to move back the trip. You're important to me! Isn't Bloom important to you?"
    asidea "(This is frustrating.)"
    "I swallow. I need to explain my rationality somehow."
    aside "Look. I'm really, really grateful for all you've done for me these past few weeks." 
    aside "Working on something together with you has been the most fun I've had in a long time. But I was talking to Felix, and he said that distance makes the heart grow fon—"
    
    hide Qwynn_N3
    show Qwynn_A at half_size
    with dissolve
    
    q "Oh. So this is because of {i}Felix?{/i}"
    asidean "Wait, what? Why are you focussing on that?"
    q "Uh, maybe because he's been flirting with you, and now he's trying to get me to leave the city? Totally nothing suspicious about that!"
    asidean "{i}Felix is not flirting with me!{/i} How can you even say that? He helped me plan all this!"
    q "Excuse me, come again?"
    "Their fork drops, clattering against the plate."
    q "So I'm not even eating {i}your{/i} dinner?"
    "This conversation is taking a turn I don't like."
    asidean "Of course you are! He only leant me advice because he knows Velvet."
    "Qwynn takes a deep breath."

    hide Qwynn_A
    show Qwynn_M at half_size
    with dissolve

    q "Okay. I'm sorry, Aste. It's just—you're my best friend. I want to look out for you."
    "{i}You're my best friend.{/i} Again with that convenient excuse?"
    asidesa "(For some reason, that makes me… sad.)"
    "The words come out before I can stop them."
    asidea "Then maybe we should stop being friends."
    "The words hang between us."

    hide Qwynn_M
    show Qwynn_N3 at half_size
    with dissolve

    "For a moment, Qwynn just stares at me, mouth open slightly. They're waiting for me to laugh—to say I'm joking."
    "I don't."
    
    hide Qwynn_N3
    show Qwynn at half_size
    with dissolve

    "Then there's silence."
    "The silence is suddenly too loud. The table between us is still set with half-finished plates, the food growing cold."
    
    hide Qwynn
    show Qwynn_M at half_size
    with dissolve   
   
    q "…You don't mean that."
    "Their voice breaks."
    q "You're upset, right? We can talk about this. We always talk about things."
    "I open my mouth. Nothing comes out."
    "The certainty drains from their face."

    hide Qwynn_M
    show Qwynn_N3 at half_size
    with dissolve

    q "Aste?"
    "They swallow."

    hide Qwynn_N3
    show Qwynn_M at half_size
    with dissolve  

    q "I-I'm sorry. Okay? I'm sorry. I didn't mean to make you feel like that."
    asidea "...And how do I feel, Qwynn?"
    "I ask because I'm not sure they get it." 
    "And my fears are confirmed in the next moment."

    hide Qwynn_M
    show Qwynn_N3 at half_size:
        zoom 1.5
        xpos 350
        ypos -200
    with dissolve

    "They step closer, hands half-raised, like they're afraid of touching me without permission."
    q "I'll fix it. I won't cancel the trip. I'll stay open later. I'll stop helping with Bloom if that's what you want. Just—"
    "{i}If that's what you want.{/i}"
    "I shake my head. No, that isn't what I want."
    asidean "Just stop, Qwynn, stop."

    hide Qwynn_N3
    show Qwynn at half_size
    with dissolve

    "The sentence lands softly. Pathetic, almost."
    asidea "(I just want it all to stop.)"

    hide Qwynn with dissolve

    "Before I realize what I'm doing, before I even think to take off my apron, I grab my keys."
    "I walk out of our apartment."
    "Alone."
    
    stop music fadeout 3.0  
    #play audio "<from 0 to 3>bell.mp3"

    jump Qwynn_chp3

#########################################
# END
#########################################









