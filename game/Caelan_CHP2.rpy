# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



#########################################
# CAELAN CHAPTER 2
#########################################

label Caelan_chp2:
  
    window hide
    show caelan_chp2 with squares
    window auto
    pause (2.0)

    $ persistent.status_button = True

    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0    
    scene kitchen_dawn with squares

    aside "(Managing Café Bloom huh?)"
    asidesh "(So much responsibility…)"
    "I stand in my kitchen, nursing a now lukewarm cortado." 
    "It's hard to think of anything besides what Sylphia asked of me."
    "Of course I want nothing more than to accept. But doing so means acknowledging how much things will change afterwards."
    asidesh "Haaaaaah…"
    asidesa "(Maybe a walk will help clear my head.)"

    play music "city_day.ogg" fadeout 2.0 fadein 2.0
    scene market_dawn with dissolve
    #footsteps sfx

    "With no specific destination in mind, I simply pick a direction and wander."
    "There's a light breeze, the ever-present sound of rushing water, and the smell of flowers drifting through the air."
    "Not just any flower though—lavender."
    aside "(Wait…)"

    #footstep sfx stop

    "My footsteps slow to a halt. Without giving it too much thought, I begin looking around for a certain someone."
    "Then, there, in the shadows of an alley, I spot them. They lean against the wall as their eyes scan the streets, watching people go about their daily routines."
    "They don't seem to notice me."

    #footsteps resume 
    scene market2_dawn 
    show voiced
    with dissolve

    "When I step into the alley, Cal's eyes lock onto me immediately."

    show Caelan_ST2 with dissolve

    voice "<from 3 to 5>audio/caelan/caelan_1.ogg"
    c "Astra. Hello."

    voice "<from 0 to 5>audio/astra/astra_caelan.ogg"
    aside "Good morning, Cal! What are you doing?"

    hide Caelan_ST2
    show Caelan2
    with dissolve

    voice "<from 5.6 to 7>audio/caelan/caelan_1.ogg"
    c "Observing."
    voice "<from 16 to 19>audio/astra/astra_caelan.ogg"
    aside "Oh. Are you looking for something?"

    voice "<from 10 to 12>audio/caelan/caelan_1.ogg"
    c "Not particularly."
    voice "<from 21 to 22>audio/astra/astra_caelan.ogg"
    asidesh "Oh."

    hide Caelan2 with dissolve

    "Maybe it's the new location, but they look guarded in a way they weren't when visiting the café."

    #CHOICE #3
    menu:

        "Sorry, I'll let you get back to your… observations.":
            "Cal shakes their head."
            show Caelan_ST2 with dissolve
            voice "<from 16 to 20>audio/caelan/caelan_1.ogg"
            c "Apologies, I did not mean to make you uncomfortable."
            voice "<from 20 to 23.4>audio/caelan/caelan_1.ogg"
            c "You can stay… If you like."

        "...Want some company?":
            $ caelan_pts += 20
            show screen choice_indicator(CAELAN_COLOR) 
            "Cal's eyes widen—shocked—and then their brows furrow in confusion."
            show Caelan_C2 with dissolve
            c "..."
            voice "<from 35 to 38>audio/caelan/caelan_1.ogg"
            c "You {i}want{/i} to stay?"
            voice "<from 28 to 31>audio/astra/astra_caelan.ogg" 
            asidesm "If you'll let me, yes."
            hide Caelan_C2
            show Caelan_B2 
            with dissolve
            voice "<from 42 to 46>audio/caelan/caelan_1.ogg"
            c "Oh. Then— please, be my guest."
 
    #BRANCHES CONVERGE HERE

    hide Caelan_ST2
    hide Caelan_B2
    with dissolve

    voice "<from 34 to 35>audio/astra/astra_caelan.ogg"
    asideb "Thanks."

    hide Caelan2 with dissolve
    
    play music "Caelan.ogg" fadeout 2.0 fadein 2.0

    "My back hits the wall right next to Cal."
    "It's subtle, but they flinch when our shoulders brush." 
    "I try to follow Cal's lead and people watch, but there's nothing all that interesting to look at."
    "Minutes pass by like this until Cal sees me shifting from foot to foot restlessly."
    "They laugh."

    show Caelan_S2 with dissolve

    "The sound is soft, and so light that it catches me off guard and stops my fidgeting. Sharp teeth flash before getting covered by a hand."
    
    hide Caelan_S2
    show ccutin1 with easeinleft

    asidep "(A Were-folk? Definitely not human. And I've never seen an Elf or Nymph with sharp teeth.)"
    
    hide ccutin1 with easeoutright

    "Cal appears surprised by their own emotions, tugging their hood down and looking away to hide their expression before I can study it further."      
    asideb "(Cute.)"

    voice "<from 56 to 57>audio/caelan/caelan_1.ogg"
    c "*Ahem*"

    show Caelan_A2
    with dissolve

    voice "<from 61 to 78>audio/caelan/caelan_1.ogg"
    c "Ignore me… You do not have to force yourself to keep me company. I am used to completing this task alone."
    "I want to ask 'What kind of task is people-watching?' but stop myself."
    "In any case, it's my own thoughts making me restless more than standing still."
    voice "<from 42 to 46.6>audio/astra/astra_caelan.ogg"
    asidesh "It's not that. I just have a lot on my mind."
    "As soon as the words leave my lips, a grave expression overtakes Cal's embarrassment."
    
    hide Caelan_A2
    show Caelan_ST2 
    with dissolve

    voice "<from 81 to 84>audio/caelan/caelan_1.ogg"
    c "Is it something serious? Can I help?"
    "I giggle."
    voice "<from 47 to 54>audio/astra/astra_caelan.ogg"
    aside "It's nothing alarming, I've just been offered a bigger position at the café. The manager, specifically."
   
    hide Caelan_ST2 
    show Caelan2 
    with dissolve

    voice "<from 90 to 92>audio/caelan/caelan_1.ogg"
    c "Ah— That is good."
    "They pause briefly, then their brows pinch together."

    hide Caelan2
    show Caelan_C2
    with dissolve

    voice "<from 94.2 to 98>audio/caelan/caelan_1.ogg"
    c "Do you not want that?"

    voice "<from 65 to 71>audio/astra/astra_caelan.ogg"
    asidesh "No, I do. I'm only thinking about how much responsibility it is."

    hide Caelan_C2 
    show Caelan2 
    with dissolve

    voice "<from 102 to 103>audio/caelan/caelan_1.ogg"
    c "I see."

    hide Caelan2 
    show Caelan_ST2 
    with dissolve

    voice "<from 105 to 108>audio/caelan/caelan_1.ogg"
    c "...Accepting new responsibility is a serious thing."

    voice "<from 91 to 93>audio/astra/astra_caelan.ogg"
    aside "Have you been in my shoes before?"
    "They look down."

    hide Caealn_ST2
    show Caelan_C2 
    with dissolve

    voice "<from 117 to 120>audio/caelan/caelan_1.ogg"
    c "Your… shoes?"
    "Right."
    voice "<from 104 to 109>audio/astra/astra_caelan.ogg"
    aside "I mean, have you been in a similar situation as me?"

    hide Caelan_C2
    show Caelan_B2
    with dissolve

    voice "<from 123 to 124>audio/caelan/caelan_1.ogg"
    c "Oh."
    voice "<from 127 to 130>audio/caelan/caelan_1.ogg"
    c "You could say that."
    voice "<from 111 to 113>audio/astra/astra_caelan.ogg"
    asidesp "What did you do then?"
    "..."
    "After taking a deep breath, they speak."

    hide Caelan_B2
    show Caelan2 
    with dissolve

    voice "<from 142 to 150>audio/caelan/caelan_1.ogg"
    c "I felt as if I did not have much choice. Declining would have disappointed many people, so I accepted."
    "I ask the first question that comes to mind."

    voice "<from 116.2 to 118>audio/astra/astra_caelan.ogg"
    asidesh "Do you regret it?"
    
    hide Caelan2
    show Caelan_ST2
    with dissolve

    voice "<from 151 to 153>audio/caelan/caelan_1.ogg"
    c "No. Never."
    "Just then, another figure enters the alley. One that I faintly recognize."

    show Caelan_ST2 at Transform (xpos=650) with ease
    show Nimue at right with dissolve

    n "Your Grace—"
    "She cuts herself off upon spotting me."
    n "Ah, hello. Astra, correct?"
    voice "<from 123.7 to 126>audio/astra/astra_caelan.ogg"
    aside "Yes… Nimue?"
    "The trace of a smile crosses her face." 
    n "Yes, what a surprise to see the two of you together."

    hide Caelan_ST2
    show Caelan_B2 at Transform (xpos=300)
    with dissolve

    voice "<from 161 to 163>audio/caelan/caelan_1.ogg"
    c "We met by chance."
    n "Of course, Your Grace. I wasn't trying to imply otherwise."
    
    hide Caelan_B2
    show Caelan_ST2 at Transform (xpos=300)
    with dissolve

    voice "<from 163 to 167>audio/caelan/caelan_1.ogg"
    c "Nimue, I thought I asked you to stop calling me that."
    n "My apologies. Force of habit."
    voice "<from 175 to 179>audio/caelan/caelan_1.ogg"
    c "Yes, and what a stubborn habit it is."
    "Despite their tone, Cal's gaze is soft. Maybe even fond."

    hide Caelan_ST2
    show Caelan_A2 at Transform (xpos=300)
    with dissolve   

    "Opposite them, Nimue stands—not looking apologetic in the slightest."
    "My eyes bounce back and forth between the two of them. The exchange feels like something that's happened hundreds of times before." 
    "I feel like I'm interrupting… even though I was here first."
    "I think of a plausible excuse to leave."

    voice "<from 131 to 136>audio/astra/astra_caelan.ogg"
    asidesh "I should go. I want to have a look around the market before lunch."
    n "Sorry Astra. I didn't mean to interrupt, but I do need to borrow them for something."
  
    hide Caelan_A2
    show Caelan_ST2 at Transform (xpos=300)
    with dissolve   
  
    "Cal looks over, meeting my eyes and looking truly sorry."

    voice "<from 192 to 197>audio/caelan/caelan_1.ogg"
    c "It seems our time is up… We can finish our talk another time."
    
    hide voiced with dissolve
    #show Nimue surprised
    
    "A small flicker of warmth ignites in my chest."
    voice "<from 144 to 145>audio/astra/astra_caelan.ogg"
    asidesp "Sure!"
    "The two of them turn away and walk with haste back to the main street."

    hide Caelan_ST2
    hide Nimue 
    with dissolve

    "Guess I should do the same."

    play music "city_day.ogg" fadeout 2.0 fadein 2.0
    scene market with dissolve

    "I walk without a particular destination in mind, the same way I did before running into Cal."
    "The scent of lavender still clings to me. Even after parting from Cal."
    asidesh "(Something about them makes it easy to open up.)"
    asidesa "(Being the manager, huh?)" 
    "A question plagues my mind."
    "Will I regret saying yes?"

    scene market with dissolve

    "In the minutes after I part from Cal, I wander through the city without a destination in mind."
    "The streets are full of life." 
    "Some people stroll slowly, like me, talking about the weather or what they're going to have for dinner tonight. Some move with purpose, weaving through the crowds with laser focus."
    "I come to a stop at an empty bench and collapse into it with a heavy sigh."

    show black with wipedown

    "Internally, I review my thoughts again. I close my eyes and sift through them in hopes of finding a concrete answer."
    a "(Despite Cal feeling like they had no choice in taking on more responsibilities… they said they had no regret with such confidence.)"
    a "(But me… I have a choice.)"
    a "{i}sigh{/i}"
    "My brain is fried. I don't want to think anymore."
    who "That was a big sigh."

    play sfx "sfx_shake.ogg"
    scene market
    show Velvet 
    with vpunch 

    asidesp "Vel?? What are you doing here?"

    hide Velvet
    show Velvet:
        zoom 1.5
        xoffset 400
        yoffset -80

    "They shrug, plopping down next to me on the bench."
    v "The same as you I assume."
    asidep "What? Overthinking?"
    v "Something like that."
    "Velvet doesn't offer any more information, rather they simply stare at me expectantly."
    asidesh "It's nothing."
    v "I heard your brain imploding from across the street. It can't be nothing."
    asidesh "...It's just. I already know what I want to do. I'm just hesitating."
    v "Why?"
    asidesa "(A good question.)"
    "Still, I say nothing. Partially because I'm unsure of the reason myself, and partially because I'm not sure if I want to confide in Velvet. I barely know them."
    "Velvet nods once and tilts their head back, getting comfortable."
    v "In that case, mind if I talk?" 
    asidesh "(Yes. Anything. I need a break from my own thoughts.)"
    aside "Sure."
    "He smirks."
    v "Thanks."
    "He takes a deep breath in preparation."
    v "I like Felix… Probably."
    asidea "(Oh.)"
    asidesp "Oh."
    v "Yeah."
    "Their eyes are closed the same way mine were earlier. Likely thinking through countless scenarios."
    aside "Why 'probably'?"
    v "...I don't think I like him in the way that most people would describe as 'romantic'. But it's not necessarily {i}un{/i}-romantic either."
    v "..."
    v "We've been friends for years now. I like it that way."
    "I lean back too, settling in for a long conversation."
    aside "So, what do you want to change?"
    v "Nothing—not really. That's the problem. I want to be with him… but I don't want to {i}be{/i} with him."
    v "I know it doesn't make any sense."
    aside "(It's not the first time I've heard someone talk about their feelings this way.)"
    aside "You like your friendship with him… do you think it means more to you than it does to him?"
    "Velvet grimaces."
    v "Just punch me in the face next time, yeah?"
    asidesh "Sorry."
    "I watch their face closely and I catch the glimpse of a smile, though it fades quickly."
    v "You're right though. It's not my place to say too much, but Felix is prone to isolating himself. He's let me in more than most… and I appreciate that but—"
    aside "You want more."
    "It's a statement, not a question. Velvet nods."
    v "I want us to be equals. I want him to tell me when things are hard. If something happens, I want to be the first to know."
    aside " Have you told him that?"
    v "Ha! Of course not …I'm afraid he'll run away."
    v "And ...I don't want to be the one who keeps him from falling in love again."
    asidesa "(Again?)"
    aside "Do {i}you{/i} love him?"
    v "...Not the way he wants to be loved. Felix, whether he realizes it or not, craves romance. The sickly sweet kind of romance you see in stories."
    asidesh "(I could see that.)"
    v "I can't offer him that. My love is different."
    "As he speaks, Velvet becomes tense. Their loose, relaxed posture slowly bundles up into an unnatural coil."
    asidesm "How do you know if you won't talk to him?"
    v "I can assume. I'm very good at that."
    aside "...I think, if you want Felix to lean on you then you have to lean on him first. How else is he supposed to know? Maybe he wants the same thing."
    v "Now there's a thought."
    "They open their eyes to stare at me. All of a sudden, the tension drains and they grin wide. The way I'm used to."
    v "...I've never said it out loud before."
    aside "Do you feel better?"
    v "A bit. But, I don't pay you enough to be my therapist. I'll figure the rest out on my own."
    asidesm "You don't pay me at all."
    v "Exactly."
    v "Thanks though. I needed that."
    "Their eyes are brighter now and they wink at me."
    v" And here I thought I was coming to save {i}you{/i}."
    "He continues."
    v "You sure I can't lend you an ear?"
    asidesh "But, I didn't even help you solve anything."
    v "That's not the point."
    "Talking with Velvet would probably help. But— I can't help but think of Cal. About the sincere look on their face when they said we could finish our talk later."
    asideeb "I said I'd share the rest of my thoughts with someone else."
    "Velvet smirks, looking smug."
    v "No pressure, I'll repay you some other way. Your next meal is on me. Cash in whenever you want."
    aside "Thanks, Vel."
    v "No, thank you. I'll get out of your hair now, good luck!"
    asidesp "You too! Talk to him, he might surprise you."
    v "...I just might. See you around~"

    hide Velvet with dissolve

    "And then they're gone, walking away looking a lot lighter than he did when he first sat down."
   
    window hide
    show black with dissolve
    window auto
    pause (2.0)

    #TODO fix music later

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior_dawn with dissolve

    "The next morning, Café Bloom is suffused with early morning light. I flip the sign on the front door to 'open'."
    "As I go around to finish the rest of my opening tasks, I wonder what it would be like to manage Bloom full-time."
    aside "(I want to be one-hundred percent positive before saying yes.)"
    "I don't do things halfway. And I won't start now."

    play audio "<from 0 to 3>bell.mp3"

    "When I look up, I'm greeted by a welcome sight. One that releases a cage of butterflies in my stomach."

    show Caelan2 with dissolve

    c "Good morning, Astra."
    asidesp2 "Good morning, Cal!"
    asidesm2 "Here for your offering?"

    hide Caelan2
    show Caelan_B2
    with dissolve

    "They walk up to the counter with a faint flush on their cheeks."

    hide Caelan_B2
    show ccutin2 with easeinleft

    c "I have been informed that calling it an offering is… incorrect."
    aside2 "Aw, but I like it! Besides, it's not like it has a different name. What am I supposed to call it?"
    
    hide ccutin2 with easeoutright
    show Caelan_B2
    with dissolve

    c "...You do  not think it is strange?"
    asidesp2 "Not at all, that's what I wrote down on the recipe card anyways."
    "Cal looks away towards the windows, almost petulant."
    c "Call it what you like."
    asidesm2 "I will."
    aside2 "Is that all you came for? I can get started right away."
    "Their eyes lock back onto mine."
    
    hide Caelan_B2
    show Caelan_ST2
    with dissolve
    
    c "Actually,  I came to speak with you."
    c "Our conversation yesterday was cut short."
    asideb2 "Oh."
    "My face warms."
    c "Is now a bad time? I know you are working, but I do not know how else to reach you."
    asideeb2 "N-no, now is good. We can talk until another customer comes in."
        
    hide Caelan_ST2
    show Caelan_S2
    with dissolve
    
    "They nod."
    "It's a bit awkward, both of us watching the other with nervous smiles."
    aside2 "Let's take a seat."

    hide Caelan_S2 with dissolve

    "I move out from behind the counter and take a seat facing the door. Cal follows, pulling out the chair across from me."
    
    show Caelan_ST2:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve

    c "I want to apologize again for yesterday. Nimue and I had something important to discuss."
    aside2 "Is everything okay now?"
    c "I have it under control. You do not need to worry about it."
    c "...Have you noticed anything… strange recently?" 
    asidesp2 "Strange? No, everything's been normal."
    "They meet my eyes."

    hide Caelan_ST2
    show Caelan_S2:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve

    c "Good. I am glad."

    hide Caelan_S2
    show Caelan_A2:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve

    "Their fingers play with the edges of their cloak. It's subtle, but the deep blue fabric is faded at the point where their fingers worry over it."
    
    hide Caelan_A2 with dissolve

    #CHOICE #4

    menu: 
        "Make them a soothing drink.": 
            $ caelan_pts += 20
            show screen choice_indicator(CAELAN_COLOR) 
            "Wordlessly, I push out of my seat and back behind the bar to make them their signature drink."
            "I can feel Cal's eyes on me but they do nothing to break the silence."
            "Crafting their offering takes no time at all."
            aside2 "Here. On the house."
            show Caelan_C2:
                zoom 1.3
                xoffset 450
                yoffset -80
            with dissolve
            c "On… the house?"
            asidesm2 "It means it's free. A gift."
            hide Caelan_C2
            show Caelan_ST2:
                zoom 1.3
                xoffset 450
                yoffset -80
            with dissolve
            "Cal stares at it like it might suddenly explode. Then, they take it while wearing an expression I can't pinpoint."
            c "...Can kindness be inherited?"
            asidesp2 "Inherited?"
            "They shake their head."
            c "It is nothing. Thank you." 

            hide Caelan_ST2
            show Caelan_A2:
                zoom 1.3
                xoffset 450
                yoffset -80
            with dissolve            
            c "Your kindness knows no bounds."
            "My heart clenches. What they call kindness feels normal to me. Not like anything worth mentioning."
            asideeb2 "No need to thank me. Honestly, you just… looked like you could use something warm."

            hide Caelan_A2
            show Caelan_S2:
                zoom 1.3
                xoffset 450
                yoffset -80
            with dissolve     

            "They smile. A slight thing."                 
            c "I run cold."
            "We slip into another stream of silence. There's no rush, no tension, just a companionable quiet."
            "It lasts until Cal finishes off the last of their offering with a faint smile."

        "Change the subject.":
            aside2 "So, are you always up this early? Whenever I see you it's basically the crack of dawn."
            show Caelan_ST2:
                zoom 1.3
                xoffset 450
                yoffset -80
            with dissolve            
            c "Mornings are quiet. The city and the people are at peace."
            aside2 "Halis does feel the most peaceful in the morning."
            hide Caelan_ST2
            show Caelan_S2:
                zoom 1.3
                xoffset 450
                yoffset -80
            with dissolve
            c "I am glad to hear that."
 
    #BRANCHES CONVERGE HERE

    aside2 "You said yesterday that you don't regret taking on more responsibility."
    
    hide Caelan_S2
    show Caelan_ST2:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve
    
    c "I do not. I would do it again if I had the chance."
    asidesp2 "Why?"
    c "Because I think what I do is very important. The work is difficult, and I am not well-suited for it… but it is something only I can do."
    asidesh2 "...Can I ask what you do? Or is it a secret?"

    hide Caelan_ST2
    show Caelan2:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve   
   
    "Cal's fingers tighten over their cloak again, and they look off to the side."
    aside2 "You don't have to tell me."

    hide Caelan2
    show Caelan_ST2:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve  

    c "No—I want to. I am just… afraid."
    "Their eyes float back to mine."
    aside2 "It's okay. I don't need to know."
    asideb2 "I only asked because I admire how sure you are. I'm scared of making a choice I'll regret."

    hide Caelan_ST2
    show Caelan2:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve        

    "Cal's gaze softens in understanding."
    c "Yes. I know that feeling very well."

    window hide
    show _pov with squares
    window auto
    pause (2.0)

    play music "caelan.ogg" fadeout 2.0 fadein 2.0
    scene black with squares

    who "Caelan? Are you here?"
    "Caelan keeps their eyes shut, unwilling to stir from their nap just yet."
    "The owner of the voice is welcome anytime. She knows where to find them."
    "They coil themselves tighter, letting the rush of water from the nearby fall drown out their worries."
    who "Here you are."
    who "I know you can hear me, Caelan."
    ca "..."
    who "Fine. Be stubborn. I guess I'll just have to eat your share along with mine~"

    scene forest with dissolve

    "The dragon's eyes crack open. Aeris stands directly in front of their snout, pouting."
    who "I thought so. Come on, shift so we can go have lunch together. Little Nimue's very proud of her table setting skills, and you don't want to disappoint her do you?" 
    "Barely ten years of age and Nimue has already perfected her glare."
    ca "(The humans and nymphs grow so quickly.)" 
    ca "(...How old is Aeris again?)" 
    "Better not to think about it."
    "Aeris begins an incessant tapping of her foot that echoes throughout the cave." 
    "Caelan gives in, and in a flash they're in a form more conducive to conversation."
    ae "Took you long enough."
    ca "Apologies, Aeris."
    ca "You said you brought lunch?"
    "She lights up."
    ae "Yes! I've been experimenting." 
    ca "...Experimenting?" 
    ae "Oh don't be like that. You'll like it… probably. It's a new drink I thought of!"
    "Aeris' 'experiments' range from otherworldly to inedible."
    ca "(I can only hope that today is the former.)"
    ae "You're always so cold. I thought I would make you something warm."
    ca "...I run cold."

    window hide
    show astra_pov with squares
    window auto
    pause (2.0)

    #play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior_dawn with dissolve

    hide Caelan2
    show Caelan_EM2:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve  

    "Their distant gaze refocuses and they look at me seriously." 
    c "Change is almost always scary. I am sure you know this."
    c "But, I do not think you have anything to worry about." 
    c "You may have noticed, but I have trouble in social situations. Being in public, making conversation… it is not my strong suit."
    c "I'm afraid."
    c "But here— My fears are so much quieter. {w} I believe that is because of you, Astra."
    asideem2 "...!"

    hide Caelan_EM2
    show Caelan_S2:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve    
   
    c "I can not imagine someone more suited to managing Café Bloom. Especially when that someone is so generous and open-minded."
    c "I am confident customers love you… and from what I have experienced, I am confident you love them too."
    c "Have faith in yourself."
    asideb2 "I—"

    hide Caelan_S2 with dissolve

    "Their words feel familiar. Sylphia said something similar the other day when she first brought up the idea of making me the manager…"
    "It starts with a squeeze in my chest and a heat in my cheeks that snowballs into hot tears slipping down my cheeks."
    asideem2 "S–sorry, I don't—"
    "Wood scrapes against the floor as Cal stands abruptly from their seat and rushes to my side."
    "My tears hardly have time to hit the floor before they've reseated themselves into the chair directly next to mine."
    "In their panic, the hood of their cloak slips off. Shock takes over even as 'Cal' starts to fuss over me."
    
    show Caelan_B:
        zoom 1.5
        xoffset 400
        yoffset -90
    with dissolve    
    
    c "I said too much. I apologize, Astra. I thought it would help— Please do not cry."
    "Even though I probably shouldn't, I choke out a laugh at their sincerity."
    asideb2 "It's okay, really. These are happy tears!"
    asideeb2 "Thank you… Caelan."
    $ persistent.caelanname = True

    hide Caelan_B
    show Caelan_C:
        zoom 1.5
        xoffset 400
        yoffset -90
    with dissolve    

    "That finally gets them to freeze. One of their hands reaches up to where their hood should be."
    "Caelan's mouth opens and closes a few times, but nothing comes out."
    asideb2 "Has anyone ever told you how pretty your horns are?"

    hide Caelan_C
    show Caelan_ST:
        zoom 1.5
        xoffset 400
        yoffset -90
    with dissolve   

    ca "I—"
    ca "What? No— I—"


    hide Caelan_ST
    show Caelan_B:
        zoom 1.5
        xoffset 400
        yoffset -90
    with dissolve

    "A tentative hand reaches to wipe my remaining tears. The touch is as light as a feather, and their skin is just as cold as it was the last time I felt it."
    ca "You are not upset with me?"
    asidesm2 "Why would I be?"
    ca "I-I lied to you."
    asidesm2 "Leaving out a few details is hardly lying, I think I can forgive you."
    asidea2 "(Wait a minute.)"
    asidesp2 "I can't believe you were comparing protecting the entire city to managing a café!"
   
    hide Caelan_B
    show Caelan_C:
        zoom 1.5
        xoffset 400
        yoffset -90
    with dissolve

    "Caelan's expression shifts to confusion. It's so much easier to read them without the hood in the way. Being this close helps too."  
    ca "Both are very important jobs, Astra. I was being serious."
    ca "You will be the perfect manager. It was not a joke."
    "I giggle."
    asidesm2 "I don't think I can argue if the Saint themself says so."

    hide Caelan_C
    show Caelan_ST:
        zoom 1.5
        xoffset 400
        yoffset -90
    with dissolve

    "Their hand removes itself from my face, they grab my hand, pleading—grave."
    ca "No. I am just Caelan. There is no Saint here. {w}Not with you."
    "My smile becomes fond."
    aside2 "No matter what you're called. If you say it then it must be true."
    "I can't be sure, but I think I catch a flicker of relief in their eyes. At the very least, the tension in their shoulders loosens."

    stop music fadeout 2.0 

    hide Caelan_ST
    show Caelan_EM:
        zoom 1.5
        xoffset 400
        yoffset -90


    ca "You should—"

    play audio "<from 0 to 3>bell.mp3"

    hide Caelan_EM
    show Caelan_ST


    "Caelan shoots up at the sound of the bell."
    ca "Saints—"

    show Caelan_ST at Transform (xpos=600) with ease
    show Albion_SC at right with dissolve
    
    al "..."
    al "I don't think you're allowed to say that."
    "Paused in the doorway looking like he had just taken a sip of the world's most bitter coffee, is Albion."
    asidesp2 "Caelan. Your hood."

    hide Caelan_ST
    show Caelan_ST2 at Transform (xpos=250)

    "I stand up from my seat while Caelan sheepishly tugs the hood back over their horns."
    
    hide Caelan_ST2 with dissolve
    show Albion_SC at truecenter with ease

    asidep2 "(I barely got enough time to look at them.)"
    asidesp2 "Albion—"
    al "No. I don't care, don't involve me in… whatever this is. Wrap it up quickly, customers will probably start arriving soon."
    asidesp2 "Albion wait—"
    
    hide Albion_SC with easeoutleft 
    
    "Albion disappears into the break room without another word."

    show Caelan_ST2 with dissolve

    ca "I upset him."
    asidea2 "No. He's always like that."
    aside2 "Don't worry about it. He won't tell anyone you were here. Albion avoids anything that might cause drama like the plague."
    
    hide Caelan_ST2
    show Caelan2 
    with dissolve
    
    "Caelan nods but they look far away."
    asidesh2 "Caelan? I promise neither of us will say anything."
    "Their gaze is downcast, starting at nothing."
    "I step in front of them."
    aside2 "You okay?"

    hide Caelan2
    show Caelan_ST2 
    with dissolve

    ca "I trust you."
    asidea2 "That's not a real answer."
    "Caelan's jaw is clenched so tight that I can practically hear their teeth grinding together."
    ca "I trust you. I am simply nervous."  
    ca "People… I can not be found out. It would… cause problems. For both of us."
    asidesa2 "Neither of us will tell. I promise."
    ca "I know. I am fine."
    "It comes out in a whisper. Unconsciously, I lower my voice to match."
    aside "It's okay if you're not."
    ca "I am."

    hide Caelan_ST2
    show Caelan_S2 
    with dissolve

    "They steel themselves and look at me with a smile."
    ca "I have kept you for too long… again. Thank you for today."
    ca "You will make the best decision for yourself. I truly believe that."
    asidesh2 "And you? You're not leaving forever are you?"
    "Then, playfully, I add."
    asidesm2 "I'll hunt you down in your Sanctuary if I have to. I'm sure the guards will understand—"

    hide Caelan_S2
    show Caelan_ST2
    with dissolve

    ca "No— I will be back."
    asidea2 "..." 
    ca "I would not want to trouble you. The Sanctuary is deep in the forest."
    ca "You will see me again, Astra. Here. In the city."
    ca "...I promise." 
    ca "I just have a few things to take care of."
    asidea2 "That sounds ominous."
    ca "It is not."
    asidesm2 "You promise?"

    hide Caelan_ST2
    show Caelan_S2
    with dissolve

    "Their shoulders relax as they let out a soft and hesitant laugh."
    ca "Yes, I promise."
    asideb2 "Okay then. Good luck."

    hide Caelan_S2
    show Caelan_B2
    with dissolve

    "I'm not sure what I'm wishing them luck for, but it feels like the right thing to say."
 
    hide Caelan_B2
    show Caelan_EM2
    with dissolve   
    
    
    ca "Thank you. Goodbye, Astra."

    hide Caelan_EM2
    show Caelan_ST2
    with dissolve   
    
    "They pause at the door."
    ca "If you must be out at night, take someone with you."
    aside2 "Okay…?"
    "Caelan nods once, satisfied, and exits the café."
  
    scene cafe_interior_dawn with dissolve

    aside2 "(Saint Caelan. They're nothing like I imagined.)"
    asideb2 "(They're even better.)"

    window hide
    show caelan_pov with squares
    window auto
    pause (2.0)

    play music "caelan.ogg" fadeout 2.0 fadein 2.0
    scene forest with squares

    "The Sanctuary is delightfully peaceful. As always."
    "Though the forest is open to all, Halis is a merchant city before anything else. The people prefer the crowded streets and bustling markets over the almost unsettling quiet of Caelan's home."
    "That and most of their visitors stopped coming once the novelty of meeting a dragon wears off." 
    "Not many were impressed by Saint Caelan—a dragon barely bigger than carriage—not after hearing stories of the majestic Saint Aeolus and the charming Saint Seraphina."
    ca "(Those two are much more suited to the title of Saint.)"
    n "Your Grace! I found you!"
    "The young Nimue comes scrambling towards them."
    "She was raised here, along with the Saint's other attendants. Thus, she never shows any hesitation when approaching them."
    "Though she looks uncharacteristically frantic today."
    "Caelan stands quickly to meet her, already in human form."
    ca "Nimue. Why the yelling? What is wrong?"
  
    play sfx "sfx_shake.ogg"
    scene forest with hpunch
    
    play music "tension.ogg" fadeout 2.0 fadein 2.0

    "The young girl crashes into them, tugging their robes."
    n "Someone— someone snuck an elemental in!"
    "Their brain short circuits. But it doesn't last long as they remind themselves of their role."
    ca "Where?"
    n "T-the entrance."
    ca "Go to my cave. You will be safe there. Take any nymphs you see on the way with you."  
    n "But…"
    ca "Nimue, please. Listen to me."
    n "O-okay but— Aeris… I thought I saw her…"
    "...Of course. They were scheduled for lunch again today. She had mentioned that she had exciting news."
    "Caelan had been looking forward to it. Aeris was terrible at keeping secrets. So, they'd already figured out that Aeris was finally going to propose to her boyfriend."
    "Their heart twists at the thought of losing their closest friend. Fear threatens to overwhelm them." 
    "Caelan notes the tight grip of little Nimue's fingers on their cloak."
    ca "(If I'm afraid, she must be terrified.)"
    "They crouch down, and do their best to hide the shaking of their own hands."
    ca "It will be okay, Niume. Go hide with the others, alright?" 
    n "..."
    ca "Nimue? I need you to be strong for me right now. I will protect everyone, and that includes Aeris." 
    n "Okay…"
    "She nods."
    n "Okay. I'll go."
    n "Bye, Your Grace…"
    "Her hands unclenching, she takes off, towards the cave just like they asked."
    "The second she's turned from them, Caelan lets the mask of calm fall away."
    "It takes less than a second to shift forms and launch themself into the air, speeding towards the Sanctuary's entrance." 
    
    window hide
    show astra_pov with squares
    window auto
    pause (2.0)
    
    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadein 2.0
    scene cafe_interior_evening with dissolve

    "As much as I like working the morning shifts, there's something special and intimate about the evening shifts."
    "With most people finishing up their work for the day, most of this evening's guests move with less urgency. They flip through books, scribble notes onto parchment, and engage in quiet conversation."
    "A cozy warmth permeates the air, and even Albion's cold shoulder does nothing to dampen it." 
    "I check the clock."
    aside2 "We've got two more hours."

    show Albion_SC with dissolve

    al "Waiting for someone?"
    asidesp2 "...No, just making an observation." 
    al "What? Your 'friend' isn't coming back today?"
    asidean2 "Why did you say it like that?"
    al "I don't know what you mean."
    asidea2 "...Whatever. They usually come in the mornings. Actually— I don't think I've seen them at night before."
    al "That's not suspicious to you?"
    asidesp2 "No? I'm sure they're really busy doing… whatever Sain—"
    "I stop myself, realizing that there are too many customers with sensitive hearing still in the café."
    asidesh2 "Doing whatever they do." 
    al "Hm."
    
    hide Albion_SC with dissolve
    
    "Albion glances away, breaking eye contact."
    asidesm2 "What's with all the questions? Don't tell me you're {i}worried{/i}??"

    show Albion_SC with dissolve

    al "I'm not worried." 
    asidesm2 "Sounds like you are." 
    al "Then you need to get your ears checked."
    asidesm2 "You're a terrible liar, Albion. I don't think I knew that about you~"
    al "Shut up. Go— Check on the customers or something. I have cleaning to do."
    aside2 "Fine, fine. I'm going."
    "I make a mental note to myself that if—no, when—I become the manager of Bloom, I need to learn to stand up to Albion."

    hide Albion_SC with dissolve

    "From where I stand, I can see the tips of Albion's ears are red. I didn't even know they could do that."
    "With a smirk, I do as he suggested and make my rounds to the remaining guests. Asking if they'd like refills, bringing more baked goods, and closing out tabs."

    stop ambient fadeout 3.0
    scene cafe_interior_night with dissolve

    "The final hours pass by in a flash. Albion and I fly through closing tasks with practiced precision, and we finish up right as the sun sets."

    play music "city_night.ogg" fadeout 2.0 fadein 2.0
    scene market_night with dissolve

    asidesp "See you tomorrow, Albion!"

    show Albion_SC with dissolve

    "He shrugs."
    al "Bye, Astra."

    hide Albion_SC with dissolve

    "Albion and I live in opposite directions, so he turns away to head into Block 7. He'd been quieter than usual ever since I called him out for being worried."
    "Still, it feels like he's finally warming up to me… in his own way."
    "The night envelops me like a blanket. Most of the activity in the streets has gone from a boil to a simmer."
    "The sun is gone, but only just."
    asidesh "(Caelan mentioned something about taking someone with me at night, but I've never been in danger here before.)"
    "Halis has guards who take care of the bulk of the city's safety and besides that, I've never felt unsafe in Halis."
    asidesa "(Thinking about it too hard will only make me paranoid.)"
    "At the same time, Caelan wouldn't have said anything if there wasn't at least some reason to be careful."
    asidesh "(I'll take a carriage tonight.)"
    "I spot one sitting slightly further down the block and signal to the driver where I want to go with my fingers held up to show the number 6."

    #footsteps sfx 

    show market_night with hpunch

    "A blur moves past me, checking my shoulder along the way."
    asidean "(Seriously?)"
    "It's nowhere near crowded enough to bump into someone."
    "I shake my head and watch as the stranger disappears into the night with hurried footsteps."
    asidea "(Guess there are some people still in a rush.)"
    "I step into the carriage and rest my head rest against the window, letting the rhythmic clopping of the horses' hooves relax me all the way home."

    jump Caelan_chp3

#########################################
# END
#########################################









