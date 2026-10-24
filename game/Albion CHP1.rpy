# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Astra", color="#3a0f0c")
define q = Character("Qwynn", color="#e45472")
define al = Character("Albion", color="#e297b2")
define f = Character("Felix", color="#a06bca")
define s = Character("Sylphia", color="#3a0f0c")
define c = Character("Caelan", color="#51abe4")
define n = Character("Nimue", color="#3a0f0c")
define v = Character("Velvet", color="#3a0f0c")
define who = Character("???", color="#3a0f0c")
define vnd = Character("Vendor", color="#3a0f0c")

define Dryad = Character ("Dryad Girl", color="#3a0f0c")
define Doggy = Character ("Dog Eared Boy", color="#3a0f0c")
define Girl = Character ("Short-Haired Girl", color="#3a0f0c")


#########################################
# ALBION CHAPTER 1 
#########################################



label Albion_chp1:

    $ persistent.status_button = True

    window hide
    show albion_chp1 with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto
    
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior with squares

    "The moment I bring up 'revitalising the café', Albion's expression hardens like I've just insulted his ancestors."

    show Albion_SC with dissolve

    al "The café is already perfect. We don't need any gimmicks."
    "I roll my eyes. Of course he'd say that."
    asidea2 "Come on, Albion. I'm not saying we tear down the walls and rebuild it as a circus."
    al "Good. Because the café isn't a stage. It doesn't need any tricks."
    al "Change too much, and it becomes something else. Our regulars come here because they like it as it is. Don't play with fire."
    "He folds his arms, gaze sharp and unyielding. If stubbornness were a weapon, he'd be untouchable."
    asidesm2 "(Alright. Time to try another angle.)"
    aside2 "Look, I'm not asking you to change anything that already works. Your coffee is still the star, and the café keeps its soul."
    aside2 "But if we add a few new ideas—just add, not replace—we might attract people who wouldn't step inside otherwise."
    asidesh2 "(Of course, I don't necessarily plan on sticking to this.)"
    "For a moment, silence. His jaw tightens, his brow furrows."
    al "...Adding, not changing."
    asidee2 "Exactly! Think of it as... polishing a gem that's already beautiful. We're not reshaping it, just letting more people see it shine."
    aside2 "And remember: Sylphia is on board."
    "His eyes narrow, but the steel in them softens by a fraction."

    hide Albion_SC
    show Albion 
    with dissolve

    al "I'm… not a fan of this idea. But seeing as Sylphia is championing this, I'll listen."
    "I grin, triumphant. Convincing Albion isn't easy—it's like trying to coax a cat into a bath. But when it works, oh, it feels good."
    asidee2 "Great. Then we should do some proper brainstorming."
    al "Here?"
    aside2 "Mm… no. Too many distractions at the café. Let's do it at my place. Saturday."
    al "You're really pushing your luck."
    asidesm2 "(That's not a no…)"

    hide Albion with dissolve
    show acutin2 with easeinleft

    "I flash him a grin. He sighs—the sound of a man already regretting his life choices—but he doesn't back out. That's as close to a 'yes' as I'm ever going to get."
  
    hide acutin2 with easeoutright
    show Albion with dissolve
  
    asidee2 "Perfect. It's a date."

    hide Albion
    show Albion_SC 
    with dissolve

    "His glare could probably burn holes in stone, but I pretend not to notice."

    hide Albion_SC with dissolve

    scene kitchen 
    show voiced
    with dissolve
    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0

    "Albion shows up right on time."
    "Of course he does. If he ever arrived late, I think the sun would stop rising and the world would end."
    "I throw the door open with a grin, only to realize I forgot to, well… do my share of the cleaning around the house. Qwynn is out on one of those excursions, and I was researching late into the night."
    "There's a towel on the floor, books stacked like unstable towers, and a plate from breakfast still sitting on the table."
    "Albion steps inside, his eyes scanning the room. His gaze is scrutinizing, not unlike a judge."

    voice "<from 0 to 4>audio/Astra/astra_albion.ogg" 
    aside "Oh, don't mind the mess. I wasn't expecting royalty."

    show Albion_SC with dissolve

    voice "<from 2 to 4>audio/Albion/albion_1.ogg" 
    al "Couldn't we have done this at work?"
    "I gesture to the spread of sketchpads, papers, pens and highlighters on the table."

    voice "<from 15.5 to 19>audio/Astra/astra_albion.ogg"  
    asidesp "Here is a much better place to make a mess!"

    show Albion_SC at ts_acJump(10)
    pause(1.0)
    
    asidesa "(Did Albion just flinch at that?)"
    "He doesn't even answer me. He just picks the towel off the floor, hangs it back on the rack, and heads to the sink to wash his hands."
    "I can't help it—I laugh. The way he moves is so stiff, so deliberate, like he's performing a sacred ritual and my house is the unholy temple."
   
    voice "<from 19.3 to 26>audio/Astra/astra_albion.ogg" 
    aside "You really can't help yourself, can you? Come sit down, let's get started!"
    "He mutters something under his breath, but comes over anyway. He clears away a space for himself at the table."

    voice "<from 35 to 40>audio/Astra/astra_albion.ogg" 
    aside "So, about the café. I've been thinking…"
    "His shoulders tense instantly. I almost laugh—again."
    "I begin listing off my ideas."

    #TODO add comedic music

    voice "<from 46.6 to 53>audio/Astra/astra_albion.ogg" 
    asidesp "What if we give everyone free coffee for a week? People will come running!"

    voice "<from 11 to 13>audio/Albion/albion_1.ogg" 
    al "...that's financial suicide."

    voice "<from 60.3 to 66>audio/Astra/astra_albion.ogg" 
    asidesp "We could dress you up in a coffee bean costume and parade through the city markets!"
    
    voice "<from 19 to 22>audio/Albion/albion_1.ogg" 
    al "Adults drink coffee, not children."

    voice "<from 81.6 to 89>audio/Astra/astra_albion.ogg" 
    asidesp "What about coffee fortune-telling? They drink, I read the future in the coffee mug stains."
    
    hide Albion_SC with dissolve
    show acutin with easeinleft

    "Albion doesn't even respond to that."

    hide acutin with easeoutright
    show Albion_SC with dissolve

    voice "<from 90 to 101>audio/Astra/astra_albion.ogg" 
    asidee "What if we use your magic to make the drink smoke when it's served? Something theatrical, like a magic trick! People would crowd around just to see—"

    voice "<from 37.3 to 41>audio/Albion/albion_1.ogg" 
    al "This is a waste of time. I'm going home."
    "Albion stands up, reaching for his things."

    voice "<from 124 to 133>audio/Astra/astra_albion.ogg" 
    asidesp "Wait! What if the café has a 'signature blend' that no one else has? Something unique."

    hide Albion_SC
    show Albion_N2
    with dissolve

    "For the first time, Albion's expression shifts. It's subtle: just a flicker in his eyes, a tightening at the corner of his mouth as if he's uncomfortable—enough to make me pause."
    
    hide Albion_N2 
    show Albion_Shy3 
    with dissolve
    
    "The silence stretches long enough that I start to fidget with one of the loose papers on the table." 
    "His face is unreadable, and for a second, I wonder if I've finally said something to actually upset him."
    asidesa "(Did I push too far?)"
    "Then, at last, Albion exhales. His voice is quieter than I expected, almost thoughtful."

    voice "<from 49 to 52.8>audio/Albion/albion_1.ogg" 
    al "...That could work."
    "I blink, caught off guard. Of all the things I threw at him, it's the one I didn't think he'd even consider."

    hide Albion_Shy3
    show Albion_N2
    with dissolve

    voice "<from 68 to 74>audio/Albion/albion_1.ogg" 
    al "In saying that, you don't have any experience with creating coffee blends, do you?"

    voice "<from 138.8 to 143>audio/Astra/astra_albion.ogg" 
    asidesh "Well... not really, but I could learn."

    voice "<from 85 to 87>audio/Albion/albion_1.ogg" 
    al "No need. I can do it."

    voice "<from 146 to 149>audio/Astra/astra_albion.ogg" 
    asidee "What, really?"

    voice "<from 100 to 106>audio/Albion/albion_1.ogg" 
    al "If I can replicate the blend my parents made by the end of the campaign, it will work."

    hide Albion_N2 with dissolve

    menu:
        "Ask more about his parents' blend":
            $ albion_pts += 10
            show screen choice_indicator() 
            voice "<from 157 to 160>audio/Astra/astra_albion.ogg" 
            asidee "Oh? What kind of blend is it?"

            show Albion_Shy2 with dissolve

            voice "<from 118 to 125>audio/Albion/albion_1.ogg" 
            al "The notes are... magical. The flavour blooms slowly."
            voice "<from 148 to 156>audio/Albion/albion_1.ogg" 
            al "Gentle sweetness at first, followed by a soft, lingering bitterness—together creating a harmony so complete it feels alive. "
            voice "<from 190 to 194>audio/Albion/albion_1.ogg" 
            al "One taste, and you'll spend the rest of your life chasing it."

            hide Albion_Shy2
            with dissolve

            "I chew on his words, trying to imagine a flavor like that. Something so vivid, so untouchable. The thought makes my fingers itch for a pen."
        "Looks like Albion has it sorted":
            voice "<from 165.6 to 173>audio/Astra/astra_albion.ogg" 
            aside "I see, looks like you have it sorted. I trust you!"
            "Albion gives a brief nod."

    # BRANCHES CONVERGE HERE

    "Without thinking, I lean forward across the table, dragging a scrap of paper closer to scribble down ideas before they slip away."
    "My hand brushes against his. Just for a second—barely a touch—but enough to notice the warmth of his skin."

    show Albion_Shy2
    with dissolve

    "Albion flinches, pulling back sharply as if burned."
    
    voice "<from 171.8 to 174>audio/Astra/astra_albion.ogg" 
    asidesp "Ah. Sorry."
    
    hide Albion_Shy2
    show Albion_E
    with dissolve

    "I glance up at him, but his face gives nothing away. His gaze is averted, fixed on the far wall."
    
    hide Albion_E with dissolve
    
    "I force myself to focus back on the page, scribbling down: 'Create a signature blend.' But the tension hangs in the air, sharp and quiet, like the echo of a string pulled too tight."
    asidesa "(He spends all day touching scalding hot steam wands without flinching, but the moment I brush against him, he shuts down completely...)"
    "I bite the inside of my cheek, considering the contradiction. He's complicated, difficult even. But maybe that's what makes him so hard to ignore."
    asidesa "..."
    
    voice "<from 186.3 to 195>audio/Astra/astra_albion.ogg" 
    asidesh "Albion... if you're creating the signature blend, what should I do?"

    show Albion with dissolve

    voice "<from 211 to 220>audio/Albion/albion_1.ogg" 
    al "My parents always served that signature blend with dessert. If we could combine the signature blend with the perfect dessert..."
    "His voice trails off, but for once there's no cold dismissal in it. Just a trace of curiosity."
    "I sit up straighter. A challenge. An opening. Something Albion is actually offering me, instead of shutting me out."

    hide Albion 
    hide voiced
    with dissolve

    asidee "(Perfect dessert, huh? That's something I can do.)"
    "A smile creeps across my face before I can stop it. Albion notices, but doesn't comment. His unreadable mask is still there, yet behind it, I catch the faintest spark of... anticipation?"
    "For the first time since I met him, it feels like we're not standing on opposite sides. Like maybe—just maybe—we're working toward the same thing."
    asidesm "(Watch me, Albion. I'll come up with the dessert that makes your magical blend unforgettable.)"
    "The thought excites me more than I expected. And for once, he doesn't look like he minds having me around."

    scene kitchen_night with dissolve
    play music "astraapartment_night.ogg" fadein 2.0
 
    "I spend the weekend making new recipes."
    "By Sunday night, the kitchen is a battlefield. Crumbs on the floor, butter smears on the cabinets, and me: slumped over the table, pen still in hand."
    "But there's progress. Two, maybe three recipes that feel promising. Nothing perfect yet, but enough to make me excited."
    asidep "(He'll probably tear them apart with that unreadable stare of his... but if I can get even a nod of approval, I'll count it as a victory.)"
    "I close the notebook with a sigh, staring at the scattered plates of half-finished desserts." 
    "My stomach churns at the thought of eating another bite, but my heart feels strangely light." 
    "That's when the door creaks open."
   
    play audio "dooropenclose.mp3"
    show Qwynn_S at half_size with dissolve
   
    q "Whoa. Did a flour elemental explode in here?"
    "I look up to see Qwynn in the doorway, eyebrows raised." 
    "Qwynn's gaze sweeps over the counters, the stacks of bowls, and the flour covering my clothes, before finally settling on me—looking every bit as messy as the kitchen."
    asidea "Very funny. It's called 'recipe development.'"

    hide Qwynn_S
    show Qwynn_N3 at half_size 
    with dissolve

    q "Mhm. Recipe development. Right. You sure you didn't just attempt to summon a demon?"


    hide Qwynn_N3 with dissolve

    "I grab one of the less disastrous attempts—a cupcake, golden and still warm—and shove it towards Qwynn."
    asidesm "Here. Eat. Then you can insult me properly."
    "Qwynn eyes the cupcake suspiciously, then flicks their eyes back at me."

    show Qwynn_N3 at half_size 
    with dissolve

    q "Questionable presentation, but I'll bite. If I die, I'm haunting you."
    "Still, Qwynn takes a bite. Their eyebrows shoot up, and they chew in silence for a moment longer than expected."

    hide Qwynn_N3
    show Qwynn_S at half_size 
    with dissolve

    q "...Okay, wait. {i}Mmm.{/i} That's really good!"
    "Relief rushes through me so quickly I almost laugh."
    asidesp "You better not just be saying that because I made it!"
    q "I'd never do that to you."
    asidesm "I knew it. I'm a genius."
    q "Yeah, yeah. Flour-covered, sleep-deprived genius."
    "Licking a stray crumb off their thumb, Qwynn smirks."
    q "Guess I'll cancel my plan to kick you out and open a bakery myself."
    asidesp "You were planning to kick me out?"
    q "Not anymore. You've proven your worth... barely."
    aside "Meaning you have feedback?"
    q "Mmmm... it's not very sweet. This is supposed to be paired with coffee, right? Then it needs to be much, much sweeter."
    aside "You might be right."
    "I glance at the empty tub of sugar on the kitchen counter."
    asidesh "(I need to do some shopping.)"
    q "Wow. You actually ran out of sugar? That's... impressive, in a terrifying kind of way. I thought {i}I{/i} was the sugar fiend."
    asidesh "I've been testing a lot of recipes."
    q "Clearly. I think half the city's supply is in your bloodstream now."
    "Qwynn chews slowly, thoughtful for a moment."

    hide Qwynn_S
    show Qwynn_N3 at half_size 
    with dissolve

    q "Y'know... maybe it doesn't just need more sugar. Try honey, maybe, or fruit. Something that adds sweetness without turning it into a brick of sugar."
    "I blink, caught off guard by the practicality hidden under the teasing tone."
    asidesm "(Not bad, Qwynn. Not bad at all.)"
    asidee "That might work."

    hide Qwynn_N3
    show Qwynn_S at half_size 
    with dissolve

    q "Of course it will. I'm a genius. And you get the fun job of cleaning all this up, so really, you're pulling all the weight here."

    hide Qwynn_S with dissolve

    "I laugh, but the thought sticks with me. Honey, fruit, balance... maybe there's something there."

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    scene market with dissolve
    play music "city_day.ogg" fadeout 2.0 fadein 2.0

    # [MARKET - if there's no background for this, could just use the corner of the street]
    "The market is already bustling by the time I arrive. Stalls line the street, each one bursting with color and noise." 
    "Fresh produce piled high, vendors call out their deals, and the smell of roasted nuts drift through the air."
    "I wander between the stalls, basket in hand, my eyes scanning rows of fruit."
    "Apples that are polished to a shine. Peaches soft as velvet and citrus bright enough to hurt my eyes."
    "My fingers trail over a stack of pears, cool and smooth beneath the market's awnings. Sweet, subtle, dependable. But is 'dependable' enough?"
    "I move on to berries. Strawberries, blackberries, blueberries. Tart and bright, bursting with flavour. Easy to love, but not for everyone."
    asidesa "(It's going to be hard, isn't it? Café Bloom isn't just one kind of place. Every day, I see different people walk through those doors—workers, travellers, Dwarves, Were-folk, Nymphs." 
    asidesa "(Everyone with their own tastes, their own favorites. How do you make one dessert that speaks to them all?)"
    "I pause at a display of figs, their dark skins split just enough to reveal the jewelled red inside. Unexpected. A little mysterious. The kind of fruit that surprises you if you give it a chance."
    asidesa "(Should I go for something safe, or something bold? What if I choose wrong?)"
    "I take a deep breath, then comb through my basket—berries for brightness, figs for depth, citrus for a spark of energy."
    asidep "(No idea yet what they'll become, but I know this much: the answer won't come easy. Not if I want to keep up with Albion.)"
    "A sharp voice cuts through my thoughts."
    vnd "Hey! You got to pay for that!"
    asidesp  "Huh? I already paid!"

    play music "tension.ogg" fadeout 2.0 fadein 2.0

    "The vendor steps out from behind the stall, eyes narrowed."
    vnd "Don't play dumb with me, missy. You think you can just walk off with my fruit?"
    "My heart skips. Heads turn. A few people stop to watch, and within moments a small crowd begins to gather."
    asidea "(Oh, great. Just what I needed. A public trial over figs.)"
    "I clutch the basket to my chest, heat creeping up my neck."
    asidean "I did pay! Check your coins!"
    "The vendor folds their arms, unconvinced. The murmurs of the crowd swell—some curious, some accusatory."
    "Then, a voice cuts through the noise."
    

    play music "Albion.ogg" fadeout 2.0 fadein 2.0
    
    al "She paid. I saw her."
  
    show Albion_SC with dissolve
  
    "The crowd parts slightly, and there he is. Albion, standing tall, his gaze level and unwavering."
    al "I was at the stall beside hers. She put the coins on your counter."

    hide Albion_SC with dissolve

    "The vendor falters, eyes flickering towards his counter. They glance between Albion's sharp expression and my own flustered face. The tension drains a little, though their frown remains."
    vnd "...Hmph. Maybe I missed it. Fine."
    "The crowd disperses with disappointed grumbles, robbed of their drama. My heartbeat slows, though my cheeks still burn."
    asidep "(Seriously? He shows up now of all times?)"
    "Albion steps closer, his expression unreadable as ever."


    show Albion_N2:
        zoom 1.5
        yoffset -100
        xoffset 350 
    with dissolve

    al "You should be more careful."
    "His tone is flat, but the way the crowd instantly quieted at his words... it's hard not to feel like he just pulled me out of the fire."

    hide Albion_N2 with dissolve

    menu:
        "Thank him seriously":
            $ albion_pts += 10
            show screen choice_indicator() 
            asideb2 "Thanks... for stepping in."

            show Albion:
                zoom 1.5
                yoffset -100
                xoffset 350
            with dissolve

            "His expression doesn't change, but I think, just for a second, there's the faintest flicker of acknowledgment in his eyes."

            hide Albion with dissolve

        "Tease him for being a hero":
            asidesm "Wow. Didn't know you had the whole 'knight in shining armor' thing in you."
            "His brow twitches, just slightly."

            show Albion_SC:
                zoom 1.5
                yoffset -100
                xoffset 350
            with dissolve

            al "...Don't be ridiculous."

            hide Albion_SC
            show Albion_Shy2:
                zoom 1.5
                yoffset -100
                xoffset 350
            with dissolve

            "He turns his head, but not before I catch the way his long, sloped ears go faintly red."
 
    # BRANCHES CONVERGE HERE
    "The moment passes, and Albion shifts the basket in his hand, looking as composed as ever."
    play music "city_day.ogg" fadeout 2.0 fadein 2.0

    hide Albion_Shy2
    show Albion_N2:
        zoom 1.5
        yoffset -100
        xoffset 350
    with dissolve


    al "If you're finished causing a scene, we should leave before the vendor changes their mind."

    hide Albion_N2 with dissolve

    "I bristle, but fall into step beside him anyway. My pulse is still racing, though I'm not sure if it's from the argument with the vendor... or from him."
    "We walk side by side, the sounds of the market pressing in around us. The crowd is loud enough to fill the silence, but it still feels heavy between us."
    aside "So... how was your weekend?"
    "Albion doesn't glance at me."

    show Albion_N2 with dissolve

    al "Wouldn't you like to know."

    hide Albion_N2 with dissolve

    asidesh "(...Uhh, yes?)"
    "I wait for him to add something, anything—but he doesn't. His attention is fixed on the path ahead, as if the cobblestones are infinitely more interesting than conversation."
    aside "Did you... do anything special?"

    show Albion_SC 
    with dissolve

    al "No."
    "I bite the inside of my cheek. Trying to get him to open up is needlessly difficult."
    asidesp "What about the blend? Have you worked on it at all?"
    al "It's been two days."
    "I raise a brow, not sure if he's scolding me for being impatient or just stating a fact. A brief silence follows, the kind that makes every step feel louder than it should."
   
    hide Albion_SC
    show Albion_N2 
    with dissolve
   
    al "...Yes."
    "The word hangs in the air, sharper than the rest, and I'm about to ask more when I hear him murmur something low, almost swallowed by the noise of the market."
    al "...I have to get it right."
    "I blink, not quite catching that. But Albion immediately straightens and glances at the basket in my arms, his expression unreadable once again."
    al "Seeing as your basket is full of dessert ingredients, you've started too."
    asidesm "What, are you spying on my shopping now?"
    al "If I wasn't, you would be getting charged for shoplifting right about now."
    aside "(He's not denying that he was spying... Whatever that means.)"
    asidesp "Well, if you must know, yes, I've started experimenting. {i}Somebody{/i} has to make sure your blend doesn't completely outshine everything else on the menu."

    hide Albion_N2
    show Albion 
    with dissolve

    "There's the faintest twitch at the corner of his mouth. Not quite a smile—but not quite nothing."
    al "Then we'll see whose work holds up."

    hide Albion with dissolve 

    asidesm "(He calls it 'work,' but it sounds an awful lot like a challenge.)"
    "We fall into silence again, though this one feels different; less heavy, less awkward. The market noise fills the space between us, and for once, it feels almost comfortable."
    "I shift the basket in my arms, glancing sideways at him. He doesn't notice—or maybe he does and just doesn't let on. Either way, I catch myself smiling before I can stop it."
    "We keep walking, the crowd thinning as the market road stretches on ahead."

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0 
    
    scene cafe_interior with dissolve
    stop audio fadeout 2.0

    "By the time I arrive at Café Bloom the next day, Albion is already there. As expected. The shop isn't even open yet, but he's behind the counter, sleeves rolled up, brewing like the world depends on it."
    "The hiss of the steam wand fills the air, and the scent of roasted beans clings to everything."
    "Towards the back of the shop, I hear Sylphia start a conversation with Albion. I can't help but listen in."
    s "Albion."
    "She speaks gently, but it still makes him pause. Sylphia leans on the counter, arms folded, her eyes soft but sharp in that way only she can manage."
    s "You'll wear yourself down if you keep this pace."
    al "I'm fine."
    s "You always say that."
    "For a moment, something flickers in her expression."
    s "I know where that drive comes from. Always trying to prove yourself, always afraid of being seen as less. But Albion, this is your home. You don't have to exhaust yourself to belong here."
    "He doesn't respond, only lowers his gaze back to the task at hand. Sylphia lets it drop, but not without a quiet sigh."
    "I step in then, making my presence known, balancing a tray covered with plates."
    asidesp2 "Special delivery."

    show Albion_N2 with dissolve

    "Albion glances up, brow raising slightly. I uncover the desserts one by one: tarts, cakes, and a batch of cupcakes I'd stayed up too late perfecting."
    aside2 "I need you to try one."
    "His expression doesn't change, but he obliges, taking a small forkful of a cupcake. He chews slowly, considering. I find myself holding my breath."
    al "...Not bad."
    "That's it. Two words. But for him, it might as well be a sonnet."

    hide Albion_N2 with dissolve

    asidee2 "(Wait—did he just... praise me?)"
    "I feel the heat rising in my cheeks, and quickly look away, pretending to straighten the tray."
    asideem2 "(Why is my heart beating so fast? It's just Albion.)"
    "I risk a glance at him from the corner of my eye. He's already back to work, as if my desserts—and his faint praise—were nothing more than a momentary detour in his routine."
    asideeb2 "(Just Albion... who barely talks, barely looks at me, and yet somehow makes my chest feel like it's about to burst.)"
    "I shake my head, trying to refocus. The last thing I need is Sylphia catching on. But when I glance her way, she's watching with a knowing smile tugging at the corner of her lips."
 
    show Sylphia with dissolve
 
    s "You two work well together."
    "Albion doesn't respond, just hums quietly, focused on tamping down the grounds in front of him. I force a laugh, too quick, too light."
    asideeb2 "Y-yeah. Something like that."
    "Sylphia's smile deepens, but she says nothing more, leaving me with the pounding of my heart and the stubborn warmth in my face."

    hide Sylphia with dissolve

    jump Albion_chp2

#########################################
# END
#########################################









