# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("ASTRA", color="#3a0f0c")
define q = Character("QWYNN", color="#e45472")
define al = Character("ALBION", color="#d897e0")
define f = Character("FELIX", color="#66ab95")
define s = Character("SYLPHIA", color="#3a0f0c")
define c = Character("CAELAN", color="#51abe4")
define n = Character("NIMUE", color="#3a0f0c")
define v = Character("VELVET", color="#3a0f0c")
define who = Character("???", color="#3a0f0c")
define cli = Character("CLIENT", color="#3a0f03")


label chp1:

    $ persistent.status_button = False

    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0
   
    window hide
    pause (1.0)
    window auto
    show prochp1 with squares
    $ renpy.pause(3.0)
    

    scene bedroom_dawn with squares


#WILL CHANGE ABOVE BG LATER

############################################################
# THINKING
############################################################
 
    "Warm sunlight filters through the nearby window, the bright rays forcing me to finally get out of bed to confront the day ahead."
    "I sit up and reach my arms up, which sends a pleasant shiver down my spine."
    "For a moment, everything is calm as I let myself slowly adjust to being awake."
    "The conversation I had with Sylphia is slowly coming back into focus, and the weight of what I've been asked to do is starting to sink in."
    "I lean forward to rest my elbows on my thighs with my hands laced together on my lap, thinking."
    aside "(Drawing in more customers…)"
    "{i}All{/i} of the options Sylphia gave sounded great."
    asidesp"(Ahhh! How am I supposed to pick just one?)"
    "If I'm going to choose, then I have to make sure I consider each idea carefully."
    asidesh "(I've got a week to decide... I wonder if Sylphia told Albion already.)" 
    asidesh "(He works at the café too, maybe I could ask him if he has any ideas.)"
    "Albion has been working at Café Bloom for a little longer than me, and while he is amazing at making coffee, his social skills are some of the worst I have ever seen."
    aside "(Still, it's worth asking for his opinion.)" 
    "At the very least, I'm not going to make any decisions just sitting around in bed." 


############################################################
# MORNING COFFEE
############################################################

    play audio "knock.mp3" fadeout 2.0
    #play audio "<from 0 to 3>bell.mp3"

    show voiced with dissolve
    "A light knock sounds at my bedroom door."

    voice "<from 0 to 3.2>audio/Qwynn/qwynn_intro.ogg" 
    q "Astra! You up? I made us some coffee!"
    aside "(Guess that's my cue.)"
    voice "<from 4.3 to 8>audio/Astra/astra_prologue_2.ogg" 
    asidesp "I'm up! I'll be out in a minute."
    voice "<from 9.5 to 12.5>audio/Qwynn/qwynn_intro.ogg" 
    q "You'd better be, don't let my hard work go to waste!"
    voice "<from 13 to 17>audio/Astra/astra_prologue_2.ogg" 
    asidesp2 "Okay, okay! One minute, I promise!"
    voice "<from 12.6 to 13.8>audio/Qwynn/qwynn_intro.ogg" 
    q "1!"
    voice "<from 17.6 to 19>audio/Qwynn/qwynn_intro.ogg" 
    q "2!"
    voice "<from 22 to 23.6>audio/Qwynn/qwynn_intro.ogg"     
    q "3..."
    voice "<from 26 to 27>audio/Qwynn/qwynn_intro.ogg" 
    q "4..."
    "The sound of Qwynn counting down fades into the background as they walk away from my bedroom door and into the kitchen."
    "I chuckle to myself knowing that Qwynn will seriously count for the full 60 seconds."
    aside "(I should hurry, Qwynn will be sad if I let their coffee go cold.)"
    "Recently, Qwynn asked for help in learning how to make coffee, though I'm not quite sure why, seeing as they don't seem to like it very much."
    "In the beginning, the results were disastrous. Every cup was either seriously watered down or horribly bitter, but... they've {i}slowly{/i} been improving."
    "The thought of fresh, warm coffee (no matter how mediocre) fills me with just enough energy to get dressed in record time."

    play music "Qwynn.ogg" fadeout 2.0 fadein 2.0
    scene kitchen_dawn 
    show voiced 
    with dissolve

    "The window over the kitchen sink is open, letting in the fresh spring breeze. Outside I can see cobbled streets and hear the birds chattering in the trees."
    
    scene qwynncg0 
    show voiced
    with dissolve
    
    "My eyes catch on Qwynn, who stands at the counter with two mugs in front of them."
    
    scene qwynncg1 
    show voiced
    with dissolve
    $ persistent.qwynn1 = True

    voice "<from 30 to 33.7>audio/Qwynn/qwynn_intro.ogg" 
    q "And... 60! Here come sit."
    voice "<from 46 to 51.7>audio/Qwynn/qwynn_intro.ogg" 
    q "I think you'll like this one, I followed all your many {i}many{/i} instructions to the letter."
    "Qwynn pushes one of the two mugs closer and gestures at it with an open palm."
    
    scene kitchen_dawn 
    show voiced 
    with dissolve

    "I grab the mug with both hands, letting the warmth of the coffee seep into my palms. The feeling is so relaxing that my eyes start to fall shut."
    aside "(...)"
 
    scene black 
    show voiced
    with wipedown
    hide coffee1 with dissolve

    voice "<from 55 to 58.6>audio/Qwynn/qwynn_intro.ogg" 
    q "Hey! Don't fall asleep, you have work soon."
    "The tap of Qwynn's pointed nails against the countertop beckons me back to the present."
   
    scene kitchen_dawn 
    show voiced     
    with wipeup
    show coffee1 with dissolve
   
    asidesh "(Right…Coffee. Work. No sleeping.)"
    "I focus on the drink before me, taking a deep breath to really hone in on the scent of the coffee."
    aside "(It's nutty... and a little smoky.)"
    asidee "(Ah, this is the dark roast that I picked up from the market after work a few days ago.)"
    "For a brief moment, I allow myself to feel a bit of pride at being able to recognize the notes so readily."
    asidee "(My research is paying off!)" 
    "The corners of my mouth turn up. As usual, the smell of coffee alone is enough to lift my spirits."
  
    hide coffee1
    show Qwynn at half_size 
    with dissolve

    voice "<from 58 to 62.6>audio/Qwynn/qwynn_intro.ogg" 
    q "Astra {i}please{/i}, just take a sip and tell me how it tastes."
    voice "<from 30 to 36>audio/Astra/astra_prologue_2.ogg" 
    asidesp "Sorry Sorry! But, you know, the aroma is important too."
    voice "<from 38 to 43>audio/Astra/astra_prologue_2.ogg" 
    asidesp "I can tell a lot just by smelling it, and the—"
    voice "<from 58 to 62.6>audio/Qwynn/qwynn_intro.ogg"
    voice "<from 65.8 to 77.1>audio/Qwynn/qwynn_intro.ogg"
    q "Yes, I know. The aroma tells you things that your tongue can't. {i}Blah Blah Blah{/i}. Trust me, with my sense of smell, I get it. I really do, but you're taking {i}forever{/i}."
   
    hide Qwynn with dissolve
   
    "A fond smile breaks across my face but I refrain from saying anything else, finally bringing the mug to my lips."
    "I take a second sip, partially because I'm trying to get a better grasp on the flavor… but mostly just to mess with them."
    "I make sure to keep eye contact as I take long, drawn out sips."
  
    show Qwynn_S at zoom_in, Transform (ypos=-40) 
    with dissolve

    voice "<from 96.7 to 101>audio/Qwynn/qwynn_intro.ogg"  
    q "Ha. Ha. You're very funny. Seriously though, how is it?"
    voice "<from 52.3 to 57>audio/Astra/astra_prologue_2.ogg" 
    asidesm "{i}Much{/i} better than last time... a little watery, but that's no big deal."
    voice "<from 67 to 72>audio/Astra/astra_prologue_2.ogg" 
    asidesm "With the way things are going, I'm actually starting to worry for my job."
  
    show Qwynn_S at half_size with dissolve
   
    voice "<from 101.6 to 106>audio/Qwynn/qwynn_intro.ogg"
    q "Watch out! I'm going to run Café Bloom outta business!"

    hide Qwynn_S 
    show Qwynn at half_size
    with dissolve


    "Qwynn finally takes a sip from their own mug, but in contrast to my own sigh of contentment, their eyebrows pinch together and they open the ice box."
    voice "<from 110.8 to 115.4>audio/Qwynn/qwynn_intro.ogg"
    q "{i}Urgh{/i}... Actually, on second thought, I think you should keep your job."
    voice "<from 121.8 to 127>audio/Qwynn/qwynn_intro.ogg"
    q "I don't know how you drink this stuff black. It's like drinking tar."
    voice "<from 84 to 89>audio/Astra/astra_prologue_2.ogg" 
    aside "And yet you try it black every time."

    hide Qwynn
    show Qwynn_S at half_size
    with dissolve

    voice "<from 136.7 to 139>audio/Qwynn/qwynn_intro.ogg"
    q "Because I think maybe one day it'll be good!"
    "Qwynn takes another sip of their drink, which is now more milk than it is coffee."
    voice "<from 141.4 to 143.8>audio/Qwynn/qwynn_intro.ogg"
    q "Ahh... much better."
    aside "(I can't help but wonder why they even drink coffee in the first place if they're just going to drown it in milk and sugar.)"
  
    hide Qwynn_S 
    show Qwynn at half_size
    with dissolve

    voice "<from 147 to 149>audio/Qwynn/qwynn_intro.ogg" 
    q "Hey, isn't it almost time for you to go?"
    voice "<from 94 to 96>audio/Astra/astra_prologue_2.ogg" 
    asidesm "Trying to get rid of me?"

    hide Qwynn
    show Qwynn_S at half_size
    with dissolve

    voice "<from 150 to 153>audio/Qwynn/qwynn_intro.ogg"
    q "Never! Who'd pay the other half of the rent?"
    voice "<from 104.5 to 108>audio/Astra/astra_prologue_2.ogg" 
    asidesm "Wow. Is that all I'm good for?"
    voice "<from 160 to 166>audio/Qwynn/qwynn_intro.ogg"
    q "Kidding! ...But you really will be late if you don't leave soon."
    "A glance at the nearby clock shows that Qwynn is right. If I want to be on time, I should leave now."
    voice "<from 113.4 to 116>audio/Astra/astra_prologue_2.ogg" 
    aside "Ok ok, I'll get going."
  
    hide Qwynn_S with dissolve
  
    "I gather my things which are all conveniently located next to the front door."
    asidesa "(Keys... backpack...)"
    voice "<from 120 to 124>audio/Astra/astra_prologue_2.ogg" 
    asidesp "Hey, Qwynn have you seen my—"
    "Before I can even finish my sentence, Qwynn's hand appears in front of me holding exactly what I was about to ask for."
    voice "<from 132.5 to 136>audio/Astra/astra_prologue_2.ogg" 
    aside "...coffee thermos."
   
    show Qwynn_S at half_size with dissolve

    voice "<from 168.8 to 170.6>audio/Qwynn/qwynn_intro.ogg"  
    q "Already filled with fresh coffee."
    voice "<from 146 to 151>audio/Astra/astra_prologue_2.ogg" 
    asidee "You're amazing. Alright, I'm off! Thanks again!"
    voice "<from 171 to 173.1>audio/Qwynn/qwynn_intro.ogg"  
    q "You're welcome! Have a good day at work!"
    "Qwynn closes the door behind me, likely going to get ready for their own day at work."
   
    hide Qwynn_S
    scene market_dawn 
    with dissolve

   
############################################################
# ALBION INTRO
############################################################
  
    play music "Albion.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadein 2.0
    scene cafe_interior with dissolve
    
    "The first thing I see when I walk into Café Bloom is Albion." 
    "He's standing at the counter in the middle of what I assume is the order for the only customer currently in the café."
    
    scene albioncg1 with dissolve
    $ persistent.albion1 = True

    "Albion looks like he's concentrating deeply. His eyebrows are furrowed, a common feature for him."
    "If he weren't a Nymph blessed with eternal youth I'd worry that his face might get stuck like that."
    "He's perfectly manicured, clothes crisp, and unwrinkled. His hair is soft and expertly styled, showing off the Aurea's signature bright hair."
    aside "(Everything he does looks effortless... and everything about him is perfect...)"
    asidesh "(Except...)"

    #CG variation
    scene cafe_interior 
    show voiced
    with dissolve
    show Albion_SC with dissolve

    voice "<from 8 to 11>audio/Albion/albion_intro.ogg" 
    al "Well, look what the cat dragged in."
    asidep "(...Except for when he opens his mouth.)"

    hide Albion_SC with dissolve

    "I walk closer, moving behind the counter towards the break room to put my stuff away."
    "As I pass Albion, my gaze drifts to the ribbon of his apron which is tied neatly into a bow. In a split second decision, I decide to play a small prank on him."
    "Albion absolutely {i}hates{/i} being perceived as anything less than pristine and perfect."
    asidesm "(No harm in poking a little fun...)"
    "I make sure to catch Albion's gaze, and once I have it, I point towards my stomach, where my own apron would be tied if I were wearing it, and whisper—"
    voice "<from 156.3 to 158>audio/Astra/astra_prologue_2.ogg" 
    asidesm "{i}Your ribbons come loose.{/i}"

    hide voiced 
    show Albion_SC 
    with dissolve

    "For a moment, Albion looks genuinely distressed as he looks down to feel for the bow before realizing that he'd been tricked, sending a withering glare in my direction."
    
    hide Albion_SC with dissolve
    stop ambient fadeout 3.0

    "Anything else he might have to say in response is stolen by the air as I quickly enter the break room and close the door behind me with a smile."

############################################################
# BREAK ROOM
############################################################

    #BREAKROOM BG
    

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0

    show cafe_interior:
        zoom 2.0
        xoffset 800
        yoffset 600
    
    with dissolve

    "I hang my bag on one of the hooks and turn to write my name on our timesheet."
    aside "(Made it right on time.)"
    "Sign in complete, I reach to grab my apron, but just before I can snag it off the hook I'm startled by a sudden voice."
    s "Good afternoon Astr—"
    
    play sound "sfx_shake.ogg"
    show cafe_interior with hpunch

    asidesp "Ah!"
    "My sudden shout interrupts her attempted greeting and she laughs softly."
    
    show Sylphia with dissolve
    
    s "Hahaha, sorry Astra. I didn't mean to startle you."
    asidesa "...Are you {i}sure{/i} about that?"
    "Sylphia laughs, shrugging her shoulders."
    s "Think of it as training. You're too easily startled."
    asidea "Training for {i}what{/i}?"
    "My question is ignored as Sylphia deftly changes topics—something she's {i}quite{/i} adept at."
    s "How was your morning? Was Qwynn's coffee serviceable today?"
    asidee "Yes actually! They did a really good job." 
    asidesm "In fact, if things keep going like this, you might have a new employee soon."
    s "Please, you and Albion are all I need. I have the best baristas in Halis~"
    "A laugh escapes me, and I grin widely."
    "Sylphia is always kind, and while I know that she would never replace me or Albion, it is nice to hear it out loud."
    asidee "{i}Aww{/i}... you mean it?"
    s "Of course I do! ...Speaking of, you should go join Albion at the bar. I'm sure he's getting lonely out there by himself. "
    asidesm "Oh yes. I bet he's {i}dying{/i} for some attention."
    "Sylphia and I lock eyes, our poker faces only holding for a brief moment before breaking into twin grins."
    s "Have fun~ I'm about to head out for a supply run, and Albion's leaving after lunch. So, you'll be closing alone tonight."
    aside "No problem! It's nothing I haven't done before."
    
    hide Sylphia with dissolve

    "I turn to grab my apron {i}again{/i}, which I had forgotten after Sylphia startled me, tying the ribbon tightly."
    "I also make sure to tuck my pen, paper, and stopwatch into the front pocket before heading back into the café."
   
############################################################
# LOST IN THOUGHT
############################################################
    scene cafe_interior with dissolve
    play ambient "sfx_cafenoise.ogg" fadein 2.0
    
    "Albion is still at the bar, though it seems he's finished making the lone customer's coffee and has moved to doing some light cleaning."
    "I see a few dishes in the sink, so I move to get a start on those while Albion continues to wipe down the countertops."
    
    show voiced
    show Albion_SC 
    with dissolve
    
    voice "<from 22 to 28>audio/Albion/albion_intro.ogg"     
    al "And here I thought I might make it through an entire shift in peace."
    voice "<from 163.4 to 166>audio/Astra/astra_prologue_2.ogg" 
    asidesm2 "Peace is overrated."
    voice "<from 31 to 34>audio/Albion/albion_intro.ogg" 
    al "You {i}would{/i} say that."
    
    hide Albion_SC with dissolve
    play audio "<from 0 to 3>bell.mp3"
    
    "Behind me, I hear the bell and the sound of Albion welcoming in the next customer."
   
    show cafe_interior:
        zoom 2.0
        xoffset 900
        yoffset 500
   
    "I make it to the sink and pull on a pair of bright pink gloves to begin my work on the dishes that piled up before I arrived."
    "I fall into a rhythm, one that frees up my mind enough to travel along the same path that it had tread this morning."
    asidesa2 "(What's the best way to appeal to more customers...?)"
    "As it stands, we have a fairly loyal and consistent customer base. Whichever of Sylphia's options I go with, I should keep in mind the core experience that our regulars come back for."
    "I could feel a hint of anxiety start to form in the back of my mind."
    asidesa2 "(No. Sylphia asked me to do this for a reason.)" 
    aside2 "(...I just have to trust her judgement.)"
    "Eventually, the dishes in the sink start to disappear, but I continue to be lost in thought."
    voice "<from 0 to 1>audio/Albion/albion_intro2.ogg" 
    al "...Astra."
    voice "<from 2.8 to 3.8>audio/Albion/albion_intro2.ogg" 
    al "Astra?"
    voice "<from 8.8 to 10.3>audio/Albion/albion_intro2.ogg" 
    al "Hey. Astra."
    "I feel a sharp pain on my cheek."
    voice "<from 171.5 to 175>audio/Astra/astra_prologue_2.ogg" 
    asidean2 "Ow! ...You pinched me!"
    
    scene cafe_interior 
    show voiced
    with dissolve
    show Albion_SC with dissolve

    voice "<from 71.5 to 79>audio/Albion/albion_intro.ogg" 
    al "I called your name three times. There's no more customers, and all the dishes are done."
    voice "<from 81 to 83>audio/Albion/albion_intro.ogg" 
    al "What else was I supposed to do?"
    voice "<from 185 to 194>audio/Astra/astra_prologue_2.ogg" 
    asidean2 "I don't know, maybe tap me on the shoulder, snap your fingers, or {i}something{/i}. Y'know, like a {i}normal{/i} person would."
    
    hide Albion_SC with dissolve
    
    "I cross my soapy gloved hands over my chest, making a face which lets Albion know of my disapproval."
    voice "<from 199 to 201>audio/Astra/astra_prologue_2.ogg" 
    aside2 "So? What's up?"

    hide Albion
    show Albion_SC 
    with dissolve

    "Albion stares at me for a few seconds, like he's reconsidering this entire interaction before his face screws up and he lets out a loud sigh."
    voice "<from 91 to 94>audio/Albion/albion_intro.ogg" 
    al "...What's wrong?"
    voice "<from 203 to 204>audio/Astra/astra_prologue_2.ogg" 
    asidesp2 'Huh?'

    hide Albion_SC with dissolve

    "It's not that I didn't hear him, but rather that Albion rarely asks anyone anything."
    "He isn't really interested in the lives of other people outside of what he is required to know about them for work." 
    "At least, that's what I'd thought."

    show Albion_SC with dissolve

    voice "<from 108 to 116>audio/Albion/albion_intro.ogg" 
    al "...You were spacing out. Just staring at an empty sink. It was starting to get annoying."
    voice "<from 205 to 207>audio/Astra/astra_prologue_2.ogg" 
    asidesp2 "...Huh?"
    "Albion's permanent scowl grows more intense—if that's even possible. The strain of asking me 'what's wrong?' clearly short circuiting his brain."
    "Despite my efforts to stay strong, his expression makes me smile, clearing away any annoyance I previously had."
    voice "<from 139 to 142>audio/Albion/albion_intro.ogg" 
    al "...Why are you smiling like that?"
    voice "<from 214 to 218>audio/Astra/astra_prologue_2.ogg" 
    asidesm2 "No reason. Thanks for checking on me."
    voice "<from 142 to 145>audio/Albion/albion_intro.ogg" 
    al "{i}Huh{/i}? I wasn't—"
    voice "<from 223 to 226>audio/Astra/astra_prologue_2.ogg" 
    asidesm2 "Yeah yeah, whatever. Thanks anyway."
    #TODO add bark
    "Albion clicks his tongue, turning away from me."
  
    hide Albion_SC with dissolve

    voice "<from 168.3 to 171>audio/Albion/albion_intro.ogg" 
    al "I'm going back to work."
    "Albion starts to walk towards the seating area, first reaching into a cabinet to grab more cleaning supplies."
    voice "<from 236.4 to 244>audio/Astra/astra_prologue_2.ogg" 
    asidesp2 "Wait— I... actually wanted to talk to you about something."
    "He pauses, not yet turning around. He doesn't say anything, but from his stillness, I can assume he's listening."
    voice "<from 250.8 to 258>audio/Astra/astra_prologue_2.ogg" 
    aside2 "Yesterday, Sylphia told me that she wanted to do something to bring in more customers." 
    voice "<from 258 to 264>audio/Astra/astra_prologue_2.ogg"   
    aside2 "...And she asked me to choose how we go about it."
    "It's subtle, but I see Albion's body twitch and he turns back around to face me."
    
    show Albion_SC with dissolve

    voice "<from 179 to 182>audio/Albion/albion_intro.ogg" 
    al "Okay. So?"
    voice "<from 272 to 283>audio/Astra/astra_prologue_2.ogg" 
    asidesp2 "{i}Haaah{/i}, you're impossible... {i}So{/i}, I was wondering if you had any ideas, y'know, since you've worked here longer than me."
    voice "<from 296 to 304>audio/Astra/astra_prologue_2.ogg"     
    aside2 "Is there anything you've wanted to change or something you think that I should know?"
    voice "<from 186 to 190>audio/Albion/albion_intro.ogg" 
    al "Not really. Things run pretty smoothly around here."
    voice "<from 320 to 324>audio/Astra/astra_prologue_2.ogg" 
    asidea2 "So there's {i}nothing{/i} you can think of?"
    voice "<from 31.5 to 32.2>audio/Albion/albion_intro2.ogg" 
    al "Nothing."
    voice "<from 333 to 337>audio/Astra/astra_prologue_2.ogg"    
    asidesm2 "...Are you {i}sure?"
    voice "<from 20 to 25>audio/Albion/albion_intro2.ogg" 
    al "{b}Saints{/b}, yes, Astra. I'm sure."
    voice "<from 356 to 366>audio/Astra/astra_prologue_2.ogg" 
    asidesm2 "I find it hard to believe that someone as meticulous as you can't think of a single thing you'd like to change."
    al "..."
    voice "<from 225 to 229>audio/Albion/albion_intro.ogg" 
    al "...Actually there is one thing I've noticed."
    voice "<from 368.8 to 371>audio/Astra/astra_prologue_2.ogg"     
    asidee2 "Really?"
    voice "<from 235 to 236>audio/Albion/albion_intro.ogg" 
    al "Yeah." 
    voice "<from 236 to 240>audio/Albion/albion_intro.ogg" 
    al "That you always stick your nose where it doesn't belong."

    hide voiced with dissolve
  
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    
    #play music "tension.ogg" fadeout 2.0 fadein 2.0
    
    asidea2 "..."

    hide Albion_SC with dissolve

    asidea2 "(Ouch.)"
    asidean2 "That wasn't funny."

    show Albion_SC with dissolve

    al "It wasn't supposed to be."
  
    hide Albion_SC with dissolve
   
    "I feel a spike of anger in my chest. Here I am, seriously asking for Albion's opinion, for him to give me something, {i}anything{/i} helpful and this is how he responds?"
    asidean2 "What do you mean by that? I belong here as much as you do!"
    asidesp2 "...I don't believe that there's nothing that comes to mind when you think about improving Café Bloom. It's not possible."
   
    show Albion_SC with dissolve
   
    al "Well {i}consider{/i} it possible. Go pester somebody else with your questions."
    asidean2 "There's nobody else I {i}could{/i} ask, Albion. We're the only ones here."
    al "Astra please, {i}enough{/i}! I gave you my answer already."
    al "I—"
    "For a brief moment, Albion looks shocked at himself, but it doesn't last long before he's back to his usual scowl."
    asidean2 "{i}What?{/i}"
    al "Nothing. Nevermind."
    asidea2 "...Fine. Forget I asked. I'll figure it out on my own. I don't know what I expected."
    al "...Me neither."
   
    hide Albion_SC #with dissolve
  
    "Albion turns away sharply, grabbing the cleaning supplies once more and moving off towards the seating area, as far from me as possible."
    "The next few hours are spent in tense silence, only broken when either me or Albion are forced to interact to serve customers."
    "When Albion finally leaves, he does so without even saying goodbye."
    asidea2 "(...)"
  

############################################################
# FELIX INTRO
############################################################

    ###################################
    #ZOOM IN TRANSFORM THING
    ###################################

    transform zoom_in:
        zoom 1.3  # Adjust zoom level as needed
        xpos 500  # Center horizontally
        ypos 50
        

    #########################################

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0
    show cafe_interior_evening with dissolve

   
    "The rest of my shift passes by uneventfully until sooner or later, it's time to close up. I head into the break room to hang up my apron and sign out before leaving for the day."
    "I lock the doors behind me before making sure to tug on them, double checking that they're locked properly."
    
    play music "city_night.ogg" fadeout 2.0 fadein 2.0
    show market_evening with dissolve
  
    aside "(Alright, time to go... I think there's time to stop by the market on the way.)"
    asidesh "(I deserve a little pick me up after this morning.)"
    aside "(It is just about time to stock the apartment anyways. Plus, I want to buy Qwynn a treat in return for the coffee this morning.)"
    "It really {i}had{/i} been much better than their previous attempts."

    show market_evening with dissolve

    "The sounds of voices grow louder and more concentrated as I walk, leading me right to the center of the market."
    "I spot a few familiar vendors, but as usual, there are plenty of merchants and traders that I've never seen before who must have traveled from outside of the city to be here."
    "Though, one thing stands out to me..."
    "Or rather, a {i}person."

    scene felixcg0 with dissolve

    "Over by one of the storefronts, a man is crouched on the ground, painting on the front windows of a flower shop."
    "Intrigued, I walk closer to try and get a better look at what he's working on."
    asidee "(It's beautiful...)"
    "They're just simple flowers, but the colors and details are so life-like that it looks like someone captured real flowers and pasted them onto the window."
    "I move even closer, and before I know it, I'm crouching next to the painter himself."
    "I glance over at him thinking that I should ask him about his work, but he hasn't realized that I'm here at all."
    "The first thing I notice is that..."
    asidesm "(His overalls are absolutely {i}covered{/i} in paint.)"
    
    show felixcg1 with dissolve
    $ persistent.felix1 = True

    "When he finally turns to look at me, I find myself looking into the richest, deepest eyes I've ever seen."
    "The color found in the center of a sunflower."
    asidesp "(Ah. Caught red-handed.)"
    
    play music "Felix.ogg" fadeout 2.0 fadein 2.0
    
    scene market_evening
    show voiced 
    with dissolve
      
    show Felix:
        zoom 2.0
        xoffset 200 
        yoffset -200
    with dissolve

    voice "<from 10.5 to 18>audio/Felix/felix_intro.ogg"
    who "Are we having a staring contest? Cause if that's the case you gotta tell me first, otherwise it's not fair."
    "The man grins wickedly and I realize that I had {i}definitely{/i} been staring, and not just at the painting."
    voice "<from 18.2 to 24>audio/Felix/felix_intro.ogg"
    who "Ok! I'm ready now, three, two, one... go!"
    "I can't help but laugh at his delivery, causing my eyes to close instinctively."
    scene black 
    show voiced
    with dissolve

    voice "<from 24 to 28>audio/Felix/felix_intro.ogg"
    who "Ha! I win. You weren't even trying!"
  
    scene market_evening 
    show voiced
    show Felix:
        zoom 2.0
        xoffset 200 
        yoffset -200
    with dissolve

    voice "<from 377 to 382>audio/Astra/astra_prologue_2.ogg"  
    asidesp "I wasn't ready! One more time, c'mon."
    voice "<from 28 to 35>audio/Felix/felix_intro.ogg"
    who "{i}Hmmm{/i}... Fine. But! If I win, you tell me what you were doing. Deal?"
    voice "<from 382 to 385>audio/Astra/astra_prologue_2.ogg" 
    asidesm "...Deal."
    "The stranger counts down once more, and the staring contest begins in earnest."
    "However, any hope I have of winning is quickly dashed when I feel a quick puff of air hit my face."

    show market_evening 
    show voiced
    with hpunch

    voice "<from 392 to 394>audio/Astra/astra_prologue_2.ogg" 
    asidesp "Hey! That's cheating!"
    voice "<from 37 to 41>audio/Felix/felix_intro.ogg"
    who "Woah, the winds are pretty strong today huh?"
    voice "<from 394.9 to 399>audio/Astra/astra_prologue_2.ogg"     
    asidesp "That wasn't the wind. You blew into my eyes!"
    voice "<from 41 to 44>audio/Felix/felix_intro.ogg"
    who "I have no idea what you mean."
    asidep "..."
    voice "<from 4 to 8>audio/Felix/felix_intro2.ogg"
    who "So? I won, what were you doing?"
    "I grumble and glare unseriously at the stranger, but I decide to be honest. Despite the fact that he obviously cheated."
    voice "<from 404 to 413>audio/Astra/astra_prologue_2.ogg"     
    asideeb "I just— I mean, I saw you as I was passing through the market and I wanted to get a closer look."
    "I nod my head towards the window."
    voice "<from 422.2 to 428>audio/Astra/astra_prologue_2.ogg" 
    asideeb "Your painting I mean, not... you."
    voice "<from 441 to 447>audio/Astra/astra_prologue_2.ogg" 
    asideb "Well, I mean, not {i}not{/i} you. I just mean that..."
    voice "<from 447 to 455>audio/Astra/astra_prologue_2.ogg" 
    asidesp "...Anyways! Your work is really good. I wanted to see the details up close. That's all."
    voice "<from 467 to 468>audio/Astra/astra_prologue_2.ogg" 
    asideeb "Promise."
    "The whole time I explain, the man's face doesn't shift at all from the grin he wears. If anything, his smile only grows wider."
    "After I finish speaking, he takes his right hand and wipes it roughly against his overalls before sticking it out for me to shake."

    scene market_evening
    show voiced
    show Felix 
    with dissolve

    voice "<from 44.7 to 47>audio/Felix/felix_intro.ogg"
    f "My name's Felix. You?"
    voice "<from 475 to 483>audio/Astra/astra_prologue_2.ogg" 
    aside "Astra. It's nice to meet you Felix. Sorry for sneaking up on you."
    voice "<from 47 to 54>audio/Felix/felix_intro.ogg"
    f "No worries! I'm flattered, honestly. I'm happy to hear you like my work."
    "He gestures at the windows behind him."
    voice "<from 489 to 493>audio/Astra/astra_prologue_2.ogg" 
    asidee "I {i}love{/i} it! Do you do this full-time?"
    voice "<from 61 to 74>audio/Felix/felix_intro.ogg"
    f "Yep! I have my own studio over in Block 2. I take commissions to do just about anything. Murals, portraits, windows, if it's got anything to do with painting, then I'm your man."
  
    hide Felix with dissolve
  
    "Maybe it is the way Felix is still grinning, or maybe it's the way he seems so approachable, but I dredge up enough confidence to ask him another question."
    voice "<from 498 to 503>audio/Astra/astra_prologue_2.ogg" 
    aside "So... where can I find you?"
   
    show Felix with dissolve

    voice "<from 74 to 76>audio/Felix/felix_intro.ogg"
    f "Hoping to see me again?"
    voice "<from 503 to 505>audio/Astra/astra_prologue_2.ogg" 
    asidesm "Is that a crime?"
  
    hide Felix
    show Felix_E 
    with dissolve

    voice "<from 78 to 85>audio/Felix/felix_intro.ogg"  
    f "Ah, I— I dunno, it depends. Are you gonna follow me around watching me work all the time?"
    voice "<from 510 to 513>audio/Astra/astra_prologue_2.ogg" 
    asidesp "It was an accident!"

    hide Felix_E with dissolve

    "Felix laughs heartily."
  
    show Felix with dissolve

    voice "<from 85 to 93>audio/Felix/felix_intro.ogg"     
    f "Hahaha. Okay okay, I won't tease you anymore. Here. I'll give you my card."
    voice "<from 93 to 98>audio/Felix/felix_intro.ogg"  
    f "It's... in here... somewhere."
    "Felix begins patting himself down and digging through the various pockets of his overalls to find the card."
    voice "<from 98 to 102>audio/Felix/felix_intro.ogg"  
    f "Aha! Here you go."
    voice "<from 110 to 115>audio/Felix/felix_intro.ogg"     
    f "I also sell paintings at different markets. You should keep an eye out!"
    voice "<from 518.5 to 520>audio/Astra/astra_prologue_2.ogg" 
    aside "Thank you."
    voice "<from 116 to 117.4>audio/Felix/felix_intro.ogg"  
    f "No problem."
    voice "<from 118 to 123>audio/Felix/felix_intro.ogg"  
    f "Well, I better get back to work. Gotta wrap this up before I lose the light y'know?"
    voice "<from 123.8 to 128>audio/Felix/felix_intro.ogg"  
    f "Maybe I'll... see you around, yeah?"
    
    hide Felix 
    hide Felix_B 
    with dissolve

    voice "<from 525 to 530>audio/Astra/astra_prologue_2.ogg" 
    aside "Yeah! See you around Felix."

    hide voiced with dissolve
  
    play music "city_night.ogg" fadeout 2.0 fadein 2.0
   
    asidesm "(...Felix huh?) "

    show felixcard with dissolve

    "I look down at the card in my hands."
    aside "(...Something to consider.)"

    hide felixcard with dissolve

    aside "(Alright. Back to running errands.)"

    scene market_night with dissolve

    "The rest of my time at the market passes uneventfully, and after an hour or so, I'm weighed down by various bags of produce, meat, and a special jar of honey for Qwynn."

############################################################
# DECOMPRESS
############################################################

    scene kitchen_night with dissolve
    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0

    "The apartment is quiet when I walk in, meaning that Qwynn must not be home yet."
    asidesa "(They're probably staying late... again.)"
    "As the owner of their own boutique, Qwynn makes their own schedule, and often stays late either making sure everything is running smoothly or just talking with customers and coworkers."
    aside "(Guess I'll make us some dinner. Qwynn {i}should{/i} be home by then.)"
    "With that thought, I start preparing to make dinner... and by dinner I actually mean breakfast, since that's Qwynn's favorite meal."
    "I'm hoping to show Qwynn how much I appreciate their serious interest in making coffee." 
    "Especially because I can't think of any other reason for them to do so, other than to make me happy."
    aside "(...Qwynn has a way of making people feel truly loved.)"
    "Trying to one-up Qwynn in that respect is an impossible game, but making breakfast for dinner feels like a good start."
    "After thinking about it for a few moments, I settle on making something simple that still uses the sweet ingredient I bought."
    asidesm "(Honey pancakes it is.)"
    "I fall into a comfortable rhythm, finding myself lost in the motion of whisking and flipping 6 perfect pancakes."
    "As I cook, I use the time to reflect on my day, knowing that when Qwynn comes home, they'll want to hear everything."
    "It's a sort of tradition that whenever we have dinner together, Qwynn and I'll take turns telling each other about our days."
    aside "(It didn't happen today, but I should tell Qwynn about Sylphia's proposal. I didn't get the chance last night.)"
    "...But, thinking about the café inevitably makes me think of Albion."     

#CHOICE #1

    asidesa "(The way he brushed me off was hurtful, but he was angry too...)"
    menu: 

        "I wonder why.":
            jump Thought_Albion
        "It's not worth worrying about.": 
            jump Cortado_1

label Thought_Albion:

    "Now that I've had some time to calm down, I {i}am{/i} curious about Albion's reaction earlier."
    asidea "(I mean, sure, he's stubborn, inflexible, horribly blunt, easily annoyed, and {i}constantly{/i} scowling.)"
    asidesa "(Even so, the way he reacted earlier seemed out of character.)"
    aside "(Back when I first started working at Café Bloom, I made plenty of mistakes, but I had never heard Albion raise his voice like he did today.)"
    asidesa "(I've known Albion for almost a year now... And yet it seems that I still know next to nothing about him.)"

label Cortado_1:
 
    asidesa "(...I'll have to talk to him sooner or later. So I suppose there's no use thinking about it too hard.)"

############################################################
# DINNER?
############################################################

    play audio "dooropenclose.mp3"

    "The door swings open, and Qwynn walks into the apartment."
    
    show Qwynn_S at half_size with dissolve
   
    q "Oh wow! It smells amazing in here Astra!"
    "They gasp, quickly shutting the door and dropping their bags to run up behind me."
    q "Pancakes?!"
    "I laugh, placing the final one on their plate."
    asidee "Your timing is perfect, we can eat together!"
    asidesp "I found a really nice jar of honey at the market this evening, and I wanted to make you something in return for this morning."

    show Qwynn at half_size with dissolve

    q "This morning?"
    aside "The coffee."

    hide Qwynn
    show Qwynn_S at half_size 
    with dissolve

    q "Ohhhhh right. Well, in that case I accept!"
    q "You're the best!"

    hide Qwynn with dissolve

    "With the pancakes finished, Qwynn and I stand at the kitchen counter talking about our respective work days, and indulging in sickly sweet pancakes."
    "Qwynn talks about the new items in their boutique, and gives me updates on the latest gossip they heard from clients."
    "The next few minutes are filled with stories about various clients and whispered rumors. Nothing I haven't heard from them before."
    asidesm "You're a fiend for drama aren't you."

    show Qwynn_S at half_size with dissolve

    q "It's not {i}my{/i} fault that I can hear practically everything going on in there. "
    q "But... yeah, I am."

    show Qwynn_S at half_size

    q "...Hey, you have the day off tomorrow right? Why don't you stop by Voyage Étoilé so I can show you the new product?"
    asidee "Alright! I can stop by after I get coffee in the morning."
    q "At Bloom?"
    asidesh "...Maybe."
    q "You know what you like, that's for sure."
    aside "I'll take that as a compliment."
    q "It is!"
    q "Ok, your turn. Tell me about your day."
    aside "Well, this didn't happen today but yesterday Sylphia actually asked me to help her in deciding on a plan to get more customers into Café Bloom."
    q "Really? Astra, that's great news!"
    q "I think this is right up your alley. You love Café Bloom! If anyone can do this, it's you." 
    q "Will Albion be helping you?"
    asidesa "(Considering his reaction earlier... I doubt it.)"
    asidesh "No, I— I don't think so. I tried to talk to Albion about it to see if he had any ideas but he didn't seem to want to talk about it."
    q "Well, I don't know Albion too well, but he doesn't seem to be very good with that kind of thing. Maybe he just needs time."
    q "Regardless, I have every confidence that you can do this! With or without Albion's help." 
    q "And of course, you can always come to me if you need anything."
    aside "Haha, thanks Qwynn. I'll keep that in mind."

    hide Qwynn_S with dissolve

    aside "(If Albion changes his mind later then that would be great, but if not... then that's okay too.)"
    "I tell Qwynn about the rest of my day, regaling them with the story of how I met a painter at the market." 
    "Somehow, I only have to deal with some light teasing regarding our encounter."
    "By the time the two of us are done chatting, our plates have long since been empty, and the sun is well and truly gone."

    show Qwynn_S at half_size with dissolve
    
    q "Alright, I think I'm gonna call it a night here Astra. Thanks again for the pancakes, they were delicious as always!"
    aside "Of course. I'm glad you enjoyed it. Night Qwynn."
    q "Night night!"
  
    hide Qwynn_S with dissolve
   
    aside "(I should get some sleep too. Tomorrow's a day off but there's no harm in being well rested.)"
    asidesh "(...The dishes can be done in the morning.)"
   
    show bedroom_night with dissolve
    
    "Sleep claims me quickly and quietly, marking an end to the day."
  
    jump chp2


