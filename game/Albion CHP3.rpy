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
define sf = Character("SPIFFY ELF", color="#3a0f0c")


define Dryad = Character ("Dryad Girl", color="#3a0f0c")
define Doggy = Character ("Dog Eared Boy", color="#3a0f0c")
define Girl = Character ("Short-Haired Girl", color="#3a0f0c")


#########################################
# ALBION CHAPTER 3 
#########################################

label Albion_chp3:

    $ persistent.status_button = True

    window hide
    show albion_chp3 with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    scene cafe_interior_evening:
        zoom 2.0
        xoffset -100
        yoffset -550
    with squares

    #TODO change music
    play music "cafebloom_night.ogg" fadein 2.0

    "I fling open the door. Albion sits slumped in a chair in the corner, one elbow propped on the armrest, his posture heavy."
    asidesp2 "Albion!"
    "He looks up slowly. His eyes are tired and shadowed."

    show Albion_N2 with dissolve

    al "Astra, I'm on my break. You should be out front."

    hide Albion_N2 with dissolve

    asidesp2 "What do you want me to say to you? I know I showed up to your house uninvited. I touched something that was important to you. For that, I'm sorry."
    asidean2 "But I'm tired of you being so cold to me. Was what I did so bad that you can't even look me in the eye?"
    "Albion is quiet for a beat. Then he pushes his head into his palms."

    show Albion_SC with dissolve

    al "That's not it, I—"
    "His voice falters, barely audible."

    hide Albion_SC
    show Albion_Shy2
    with dissolve

    al "...It's not you."
    "I push forward."
    asidesp2 "Then what is it, Albion? Whatever it is, I—"

    hide Albion_Shy2 with dissolve

    #TODO make screen shake
    play sfx "sfx_windmagic.ogg"

    "But just before I reach him, I'm hit with a burst of wind."
    asidesp2 "(What is this?)"
    "The air howls, fierce and unrelenting, like I've stepped into a wind tunnel. My hair lashes across my face. My clothes tug and snap in the current."
    asidesp2 "(Is this... Albion's magic?)"

    show Albion_Shy2 with dissolve

    al "Astra, please leave."

    hide Albion_Shy2 with dissolve

    play sfx "sfx_windmagic.ogg"
    "Albion doesn't move from his chair. The air coils around him, bending and twisting like it belongs to him—an invisible wall of storm pushing me back."
    asidea2 "(He's serious this time.)"
    "My hand drops to my side, but I meet his gaze all the same, hair whipping around my face."
    asidesh2 "...if that's what you want."
    "The words are bitter. I turn, step into the calmer air by the door, and leave the storm behind me."

    #TODO change track
    scene kitchen_night with dissolve
    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0

    asidesa "(Qwynn isn't back yet...)"
    "I stand alone in the kitchen, my nightly baking session ended."
    "My notebook lies open on the counter, pages crowded with sketches, scribbles, and half-erased notes."
    "Bowls, measuring spoons, and bags of flour clutter the space like the aftermath of a battle."
    "I stare at the sugar spilled across the counter… the cracked egg I never cleaned up… the unfinished tart that's been sitting there for hours."
    asidesa "(How many times have I tried now? Ten? Twenty? And still nothing feels right.)"
    "I flip through my notebook, my previously neat recipe titles turned messy with revisions."
    "Berry Compote Tart."
    "Citrus Shortcake."
    "Honeyed Pear Galette."
    "Every one of them crossed out, every one a failed attempt to match his blend."
    asidea "('Match the blend.' That's all it was supposed to be. Simple.)"
    "I drag my fingers down the page until they stop on the blank line at the bottom. The silence of the kitchen presses in thick, almost heavy."
    asidea "Maybe I should just pick a dessert. Any dessert. Even if it doesn't go with Albion's stupid blend, it'll have to do."
    "I laugh under my breath, but it comes out shaky. The sound just hangs there, hollow and small."

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    scene cafe_interior with dissolve
    #TODO change track?
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg"

    aside2 "Here is the signature blend, and here is the dessert."
    "I push the plate—berry compote tart—across the table towards Sylphia. Albion does the same with his latte, the signature blend."
    "I can't help but glance at Albion from the corner of my eye."
    "He truly looks like death—nearly worked himself to it, as Sylphia predicted."
    "All day, he had been using his wind magic constantly, cooling down drinks faster than they could steam. All to speed up the process of replicating his parents' signature blend."
    "Based on his expression, the mug he has set in front of Sylphia isn't even close."
    "Sylphia simply stares at the table, not making a move to pick up either. Eventually, she sighs."

    show Sylphia with dissolve

    s "Maybe this will have to do. The launch party is only days away. We need to finalise the menu soon so they can be printed on time."
    
    hide Sylphia
    show Albion_SC
    with dissolve
    
    al "..."

    hide Albion_SC with dissolve


    play audio "<from 0 to 3>bell.mp3"

    "A customer walks in, and Albion leaves the table to serve him. I'm left sitting alone with Sylphia."
    "She rises from her seat, smoothing out her apron. As she turns, her gaze catches on a basket resting on the far table."
    "The basket from that rainy day with my gingerbread cookies still in it, untouched, which Albion had brought to return to me."
    "She lifts the cloth."

    show Sylphia with dissolve

    s "Astra, did you make these? They look adorable~"
    asidesh2 "Yes. Don't touch them, they're almost a week old. They're not for the launch party, they were for—"
    "—Albion."
    s "Astra, I'm over a hundred years old. Cookies that are a few days old aren't going to kill me."

    hide Sylphia with dissolve

    "Before I get another chance to protest, she takes a big bite from a gingerbread man. She chews for a second, then her eyes widen."
   
    show Sylphia with dissolve
   
    s "Astra, this is delicious!"
    asidesp2 "You're joking, right? They're a mess! They don't even look the same!"
    s "They're not perfect, no. But that's the beauty of it. The fact they all have slightly different faces? It's adorable. I can tell they were made with love."

    hide Sylphia with dissolve  
   
    "I bristle at the word. 'Love'?"
    "Sylphia takes another cookie, then winks at me, smiling like she's figured out something I haven't."

    show Sylphia with dissolve

    s "I think you're really close, Astra."

    hide Sylphia with dissolve  

    "She disappears into the break room, leaving me staring at the basket of cookies."
    "I think of the shopping trip. The catering order. And now, this."

    menu:

        "Confront him directly.":
            "My shift's already over, but I can't sit still. The words Sylphia said keep circling in my head, louder each time."
            asidea "(Enough waiting. I'm just going to talk to him.)"
            "I find him behind the counter, rinsing out the milk steamer with that same calm precision that makes me want to scream."
            asidesp "Albion. We need to talk."
            "He doesn't look up right away. The quiet hiss of steam fills the space between us."

            show Albion with dissolve

            al "I'm in the middle of my shift."
            asidea "This won't take long."
            "Finally, he turns. His expression is unreadable, but his eyes flick briefly toward the clock before settling on me."

            hide Albion 
            show Albion_SC 
            with dissolve

            al "You always say that."
            asidean "Because you never let me say anything!"
            "The words come out sharper than I intend. He blinks, but doesn't respond. I lower my voice."
            asidesh "I just want to talk. Properly. About us. About the blend. About... everything."
            al "Not everything can be fixed by talking through it immediately. Now's not the time."
            asidean "When is the time, then? After the launch party? After another week of pretending everything's fine?"

            hide Albion_SC with dissolve

        "Leave him a note.":
            $ albion_pts += 20
            show screen choice_indicator()
            "My shift is already over, but it doesn't matter. I grab a pen and tear a sheet from the memo pad. The words come quickly, before I can overthink them."
            "{i}'Albion. Can we please talk after your shift? I promise, it will only be about work.'{/i}"
            "When he turns to clean the milk steamer, I slip the note onto the counter beside his station."
            "For a moment, I think that's enough." 
            "But before I can stop myself, I write another."
            "{i}'If you truly, truly don't want to talk to me, then it's okay. I won't hold it against you.'{/i}"
            "I set it down next to the first, the two scraps of paper side by side like a pair of open hands. Then, I sit myself at a far table to wait."
            "..."
            "......"
            "Finally, Albion picks up the memo."
            "I realise I'm holding my breath."
            "He looks up, rounding the counter. Then, he comes to a stop at my table."

            show Albion_N2 with dissolve

            al "You realise my shift doesn't end for another three hours?"
            asidee "(Music to my ears. That means he's agreeing to talk.)"
            aside "It's fine, I'll wait."

            hide Albion_N2
            show Albion_SC 
            with dissolve

            al "You're going to wait here. For three hours?"
            aside "Yes."

            hide Albion_SC with dissolve

            asideb "(For you, anything.)"

            show Albion_Shy2 with dissolve

            al "...Okay."


    play sfx "sfx_windmagic.ogg"
    "For a second, I think he's about to walk off without another word—but then he turns back to the counter, pours a cortado, and brings it over. The surface ripples slightly, cooled by his magic."
    
    show Albion_N2 with dissolve
    
    al "We'll talk after work."
    "I can't help the smile that spreads across my face. That's Albion for you: stubborn, frustrating, impossible to read... and yet somehow still so quietly, unexpectedly kind."

    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0
    stop ambient fadeout 2.0
    scene cafe_interior_evening with dissolve

    "I lose count of how many cups of coffee I've had. Sylphia has gone home for the day, and the café quieted hours ago."
    "Three hours later, Albion finally walks over. He looks as composed as ever, but there's something in the set of his shoulders that tells me he's exhausted."
   
    show Albion_N2 with dissolve
   
    al "So, what do you want to talk about?"
    aside "Do you know why Sylphia kept assigning us all those tasks together?"

    hide Albion_N2
    show Albion_SC
    with dissolve

    al "It's obvious. She wants to improve our teamwork."
    asidesp "That's not it!"
    "The words come out faster than I mean them to, but I can't stop now."
    aside "What she's been trying to tell us is that we were making the blend and the dessert separately. We've been trying to force them to match after the fact, instead of creating them together."
    "Albion's eyes widen. Then, he shakes his head."

    hide Albion_SC
    show Albion_Shy2
    with dissolve

    al "Working separately is fine. I'll keep trying your desserts, Astra. We'll pick the one that compliments the signature blend the most, even if it's not perfect. Once I recreate the blend—"
    asidesp "That's exactly the problem!"
    asidean "All I've been doing is trying to match your blend, Albion. But you should be trying to match my desserts too! We should be meeting in the middle!"
    
    hide Albion_Shy2
    show Albion_SC
    with dissolve   
    
    al "We can't."
    "I freeze. His voice isn't sharp. It's heavy. Final."

    hide Albion_SC with dissolve

    "And in that moment, looking at him, I finally see it: the exhaustion etched into his features, the weight behind his calm."
    "It was never about a menu upgrade. Never about Bloom."
    "Recreating that blend... is Albion's purpose."
    "A faint draft brushes against my arm. At first, I think nothing of it—just a breeze slipping through the cracks of the old café windows."
    asidesa "(Did someone leave the door open?)"

    play ambient "windblow.mp3"

    "But the air shifts again, sharper this time. The napkins on the counter lift, fluttering like startled birds."
    asidesp "(No. It's—)"
    asidesp "Albion!"
    
    show Albion_SC with dissolve  
        
    "He doesn't respond. The wind coils around him, fast and chaotic."
    "Chairs scrape, papers scatter, and the sugar jar tips over, spilling across the floor. It's like a miniature storm has come alive inside the café."
   
    hide Albion_SC with dissolve
   
    aside "(Not again!)"
    "This time, the current is stronger, wilder. Everything light enough to move spins into the air, swirling in a dizzying cyclone. The air roars in my ears, cold and biting."
    
    play sfx "sfx_shake.ogg"
    
    "A loud thump." 
    "Albion's knees hit the ground."

    show Albion_Shy3 with dissolve

    al "Astra, just go. It'll stop soon."
    "His voice is strained, roughened by effort. He's trying to pacify his breathing, but it's no use. The winds only grow harsher."

    hide Albion_Shy3 with dissolve

    asidesa "(He can't control it?)"
    asidean "(Is it because he's been using his magic too much?)"
    
    menu:

        "Stay.":
            $ albion_pts += 40
            show screen choice_indicator()
            "I take a step toward him, wind whipping at my hair, my eyes stinging from the force."

            show Albion_Shy1 with dissolve

            al "Astra, go!"

            hide Albion_Shy1 with dissolve

            "He's kneeling in the middle of the storm, one hand braced on the floor, the other clenched tight as if he could hold the air still by sheer will."
            "His hair and clothes whip wildly around him, caught in the cyclone he's struggling to contain."
            asidesp "I'm not going anywhere!"

            show Albion_Shy1 with dissolve

            al "You don't understand! I'm a mess—"
            asidean "Make me understand!"
            "The storm howls louder, tugging at the chairs, rattling the glass. I dig my heels into the floor, one arm shielding my face as I take another step forward."
            
            hide Albion_Shy1
            show Albion_Shy1 at truecenter:
                zoom 1.5 
                yoffset 150
            with dissolve
            
            asidesp "You think I'm scared of wind? You think I'll just run away because it's messy, or because you can't control it right now?"
                           
            "He lifts his head. The anguish in his eyes cuts sharper than the wind."
            asidesp "I'm not going to leave you alone, Albion. I'll stay with you no matter what happens!"
            "For a heartbeat, everything stops—the roar, the chaos, the sound of my own heartbeat. Albion stares at me like I've said something impossible."
            
            hide Albion_Shy1 with dissolve
            
            stop ambient fadeout 2.0
            "Then, slowly, the wind begins to ease. The swirling napkins fall. The papers drift down like tired snow."
            
            show Albion_Shy1 at truecenter:
                zoom 1.8 
                yoffset 350
            with dissolve

            "I take one final step forward and rest a trembling hand on his shoulder."


        "Back off.":
            asidesa "(If I stay, I'll just make it worse.)"
            "I take a step back. Then another. My hair whips across my face, and the sound of the storm swallows my heartbeat."
            "Albion doesn't look at me. He's too focused, his hands braced against the floor, every muscle straining as if he's fighting the air itself."
            asidesa "(He said it'll stop soon... he can handle this on his own. He has to.)"
            "I back toward the door, the air pushing me like an unseen hand. The moment I step outside, the roar dulls to a muffle behind the glass."
            
            scene market_evening with dissolve
            
            "The streets are quiet. I press my back to the wall beside the window and watch through the swirling dust and papers inside."
            "The café lights flicker. The storm continues for what feels like forever, minutes that stretch and stretch, until finally, the movement inside begins to still."
           
            stop ambient fadeout 3.0
           
            "I wait until the last current fades before opening the door again. The café is a mess: overturned chairs, sugar scattered like snow, napkins clinging to the walls."
            "Albion is still kneeling in the center of it all, breathing hard, shoulders trembling."
            scene cafe_interior_evening with dissolve
            "I rush forward and rest a trembling hand on his shoulder."

    "He exhales, long and unsteady, but he doesn't move away. Or he doesn't have the strength to."

    hide Albion_Shy1
    show Albion_Shy3
    with dissolve

    aside "Let me take you home."
    al "But... the café... we have to clean—"

    hide Albion_Shy3
    show Albion_N2
    with dissolve

    asidesp "We'll come in early to clean it tomorrow. For now, let's go home."
    "He doesn't argue. The fight drains from his voice, leaving only quiet exhaustion. When he finally nods, it feels like the storm has ended for both of us."

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "Albion.ogg" fadeout 2.0 fadein 2.0
    scene albionapt_night with dissolve

    "The inside of Albion's apartment smells faintly of roasted beans. Everything is as immaculate as I remember, though tonight, the orderliness feels less like pride and more like a shield."
    "Albion crosses to the couch and sinks into it, his posture still rigid. I close the door behind us and take a cautious seat beside him, leaving just enough space to not be intrusive."
    asidesa "(He looks so tired. I've never seen him like this before.)"
    "His head tilts back against the cushion. The dim light catches the edges of his face, softening the sharp lines I'd always associate with him."
    asidesh "Albion..."
    "He turns slightly, eyes half-lidded but attentive, waiting."
    aside "You don't have to tell me everything. I just want to understand."
    "For a moment, the only sound is his quiet breathing. Then, finally, he speaks, his voice low and hesitant, like he's learning how to use it again."
    
    show Albion_Shy2 with dissolve
    
    al "You want to understand?"
    asidesh "Yes."

    hide Albion_Shy2
    show Albion_N2
    with dissolve

    al "..."
    al "I wasn't born among elves, but they're the only family I've ever known."
    al "I was found when I was young. I was barely old enough to walk. A pair of elves took me into their village. They were the ones who gifted me the stopwatch."
    asidesa "(The stopwatch I tried to touch...)"
    al "They were kind to me. But... there was always a distance."
    al "Elves are born with deep connections to the elements. Some can summon storms, others can command the forests to bloom. Elven magic flows as easily as breath."
    al "But I..."

    hide Albion_N2
    show Albion_Shy2
    with dissolve

    "He takes a slow breath before continuing."

    hide Albion_Shy2
    show Albion_N2
    with dissolve

    al "I studied really hard. I worked for years to perfect my magic. But even then, it wasn't enough. All I could do was bend the wind a little."

    hide Albion_N2
    show Albion_SC
    with dissolve   
   
    al "For an Aurea, that's normal. In an Elven village, it's shameful."
    "I swallow, unsure what to say."

    hide Albion_SC
    show Albion_Shy3
    with dissolve

    al "My parents and I would make coffee together in the mornings. There, in the kitchen... the difference didn't matter."

    hide Albion_Shy3
    show Albion
    with dissolve

    "He finally meets my eye."
    al "In the kitchen, we were equals. Every morning, they'd make coffee, and I'd watch the steam curl. Eventually I learnt how to do it myself. That was the one place I didn't feel different."
    al "They had a special blend. Sweet, rich, perfectly balanced. The others in the village came by just to taste it. It was theirs—and for a while, mine too."
    al "But I could never quite make it the way they did. No matter how many times I tried, it never tasted the same."

    hide Albion with dissolve

    asidesa "(That's why he works so hard recreating that blend... it's a reminder of his childhood. He's been chasing something he never quite got. Perfection... and belonging.)"
    asidesa "..."

    show Albion with dissolve

    asidesp "You've spent all this time chasing something perfect. But... maybe it was never meant to be perfect in the first place."

    hide Albion
    show Albion_SC
    with dissolve  

    "His brows draw together, hurt, but he doesn't interrupt."
    asidesp "I've been doing the same thing, you know. Trying to make desserts that match your blend exactly."
    asideeb "Changing them over and over, thinking if I just worked hard enough, I'd make something good enough for you."

    hide Albion_SC with dissolve

    "I think of the gingerbread men I made not to impress anyone, but simply because I wanted to see him smile and share them with him."
   
    show Albion_N2 with dissolve
   
    asideb "But maybe... the little flaws are what make things special. Maybe that's true for your blend, too."
    aside "What if what made your parents' blend so perfect wasn't the flavor, but the moment? The mornings you spent together. The people who drank it. The warmth."
    "I smile faintly, even though my voice wavers."
    asidesp "Maybe you've been trying to recreate something that was never about coffee to begin with."
    "Albion stares at me for a long time, like he's turning my words over in his mind. Then, finally, he looks away, scoffing softly."

    hide Albion_N2
    show Albion_Shy2 
    with dissolve

    al "You always make things sound simpler than they are."
    asidesm "Maybe things don't have to be as complicated as you make them."

    hide Albion_Shy2 with dissolve

    "A silence settles between us again, but this time it's different. Lighter. Not a wall, but a quiet space we're both standing in."

    show Albion_Shy2 with dissolve

    asidesp "Let's make something together, Albion. The blend, the dessert. All of it."
    
    hide Albion_Shy2 with dissolve

label albion_ending:
    if (albion_pts >= 70):
        jump albion_good1
    else:
        jump albion_bad

########################################
# GOOD END
########################################
label albion_good1:
    window hide
    show albion_good with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    scene albionapt_night 
    show voiced
    with squares

    "For a moment, he just watches me. The air between us is still, quiet. Then slowly, Albion makes a sound that's half a sigh, half a laugh."
   
    show Albion_H with dissolve

    voice "<from 6 to 9>audio/Albion/albion_good.ogg" 
    al "Together, huh?"

    voice "<from 195 to 200>audio/Astra/astra_albion.ogg" 
    asidee "Yes. We don't have to get it right the first time. We just try."

    hide Albion_H
    show Albion_Shy1 
    with dissolve

    "His lips twitch into an almost-smile."

    voice "<from 11 to 13>audio/Albion/albion_good.ogg" 
    al "You make it sound easy."

    voice "<from 210 to 215>audio/Astra/astra_albion.ogg" 
    aside "It doesn't have to be easy. It just has to be ours."
    "That seems to catch him off guard. For a heartbeat, the wall he's so carefully built around himself finally cracks."

    hide Albion_Shy1
    show Albion
    with dissolve

    voice "<from 24.5 to 28>audio/Albion/albion_good.ogg"
    al "Alright. We'll try it your way."

    hide Albion with dissolve

    "I blink, unsure if I heard him right."

    show Albion with dissolve

    voice "<from 223.3 to 226>audio/Astra/astra_albion.ogg" 
    asidee "You mean it?"

    voice "<from 33 to 38>audio/Albion/albion_good.ogg"
    al "I do. But if it fails, you're telling Sylphia."
    voice "<from 229.5 to 231>audio/Astra/astra_albion.ogg" 
    asidesm "Deal."

    hide Albion with dissolve

    "The tension that's hung over us for so long finally starts to melt. He leans back slightly, his gaze softening."

    show Albion_H with dissolve

    voice "<from 49.5 to 52.8>audio/Albion/albion_good.ogg"
    al "You really don't give up, do you?"
    voice "<from 238.8 to 241>audio/Astra/astra_albion.ogg" 
    asideb "Not on things worth fighting for."
    "He looks at me for a long moment, something unreadable in his eyes... and then, quietly, he reaches over and tucks a stray strand of hair behind my ear."
            
    hide Albion_H        
    show Albion_H at truecenter:
        zoom 1.8 
        yoffset 350
    with dissolve

    voice "<from 64 to 66>audio/Albion/albion_good.ogg"
    al "Then I suppose I'll just have to keep up with you."

    window hide
    $ renpy.pause (2.0)
    
    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "Albion.ogg" fadeout 2.0 fadein 2.0
    scene albionapt 
    show voiced
    with dissolve

    voice "<from 242.7 to 250>audio/Astra/astra_albion.ogg" 
    asidesp "Okay, so maybe if you use... less dark roast? The one that smells like burnt toast?"

    show Albion_SC with dissolve

    voice "<from 71 to 74>audio/Albion/albion_good.ogg"
    al "It's not burnt. It's bold."

    voice "<from 263 to 265>audio/Astra/astra_albion.ogg" 
    asidesm "It's bitter."

    hide Albion_SC with dissolve

    "The soft hum of the oven fills the kitchen, mingling with the gentle crackle of the beans roasting nearby. The air smells like sugar and coffee, sweet and alive."
    "Despite Albion's best efforts to ‘clean as we go', flour dusts the counter. Coffee cups clutter the table, each one marked with notes in my messy handwriting."
    "Somewhere between the second and third blend attempt, I've lost track of which mug belongs to which recipe."

    show Albion_N2 with dissolve

    voice "<from 82 to 85>audio/Albion/albion_good.ogg"
    al "You added honey to the last one."

    voice "<from 269 to 272>audio/Astra/astra_albion.ogg" 
    asidee "Exactly! I'm saving your taste buds."
    "He gives me a look of exasperation before returning to the grinder."

    voice "<from 93 to 96.5>audio/Albion/albion_good.ogg"
    al "You can't just throw ingredients together and call it research."

    voice "<from 282 to 285>audio/Astra/astra_albion.ogg" 
    asidesm "Actually... I can."
    "He pauses mid-pour."

    hide Albion_N2
    show Albion_SC 
    with dissolve

    voice "<from 109 to 111>audio/Albion/albion_good.ogg"
    al "...What?"

    voice "<from 297.6 to 310>audio/Astra/astra_albion.ogg" 
    asidesm "I did some reading the past couple of days. About blending ratios, acidity, and how temperature affects extraction. Look at me, using coffee words."
    "He raises an eyebrow, clearly skeptical but intrigued."

    hide Albion_SC
    show Albion
    with dissolve

    voice "<from 123 to 125>audio/Albion/albion_good.ogg"
    al "Go on, then. Impress me."

    voice "<from 315 to 328>audio/Astra/astra_albion.ogg" 
    asidesm "Well, maybe if we mixed the lighter roast with a pinch of the darker one, it could balance out the sharpness? Not too sweet, not too bitter. Kind of like—"
    
    voice "<from 133.6 to 136>audio/Albion/albion_good.ogg"
    al "—your berry compote tart."

    hide Albion
    show Albion_Shy2
    with dissolve

    "He says it before I can, then looks faintly surprised at himself."

    hide Albion_Shy2 with dissolve

    asidee "(...Did he just compare my dessert to his coffee?)"

    show Albion with dissolve
    voice "<from 149 to 157.8>audio/Albion/albion_good.ogg"
    al "...If you're asking, then yes, that works. The lighter roast will open up the flavor, while the darker notes anchor it."
    "He glances at me, that unreadable calm giving way to something temperate."

    voice "<from 349 to 353>audio/Astra/astra_albion.ogg" 
    asidee "So you're saying my idea wasn't terrible?"

    hide Albion
    show Albion_Shy2 
    with dissolve
   
    voice "<from 170 to 175>audio/Albion/albion_good.ogg"
    al "I'm saying I've already tried that—but decent effort."
    "I chuckle."

    voice "<from 357 to 361>audio/Astra/astra_albion.ogg" 
    asideb "That's a compliment coming from you."

    hide Albion_Shy2
    show Albion_H
    with dissolve

    "He shakes his head, but there's a quiet smile tugging at the corner of his mouth as he measures out the beans."

    hide Albion_H with dissolve

    "The oven timer dings. The smell of baked sugar and fruit fills the kitchen. Albion and I exchange a look that's half challenge, half excitement."

    voice "<from 365 to 368>audio/Astra/astra_albion.ogg" 
    asidesh "Moment of truth."
    "I pull on the mitts and open the oven door. A wave of hot air rolls out, carrying the scent of caramelized berries and buttery crust."
   
    play sfx "sfx_windmagic.ogg"
    
    "Before the searing heat can hit me, a current of air rushes past and diverts it away—Albion's magic. Instinctive. Effortless. I can't help but smile."
    "The tart gleams faintly in the light, edges golden, filling bubbling gently."

    show Albion with dissolve

    voice "<from 190 to 192>audio/Albion/albion_good.ogg"
    al "Looks good."

    voice "<from 372 to 374>audio/Astra/astra_albion.ogg" 
    asidesm "You sound surprised."
    voice "<from 12 to 17>audio/Albion/albion_missing.ogg"
    al "Given your last attempt nearly set my oven on fire, yes, a little."
    voice "<from 374 to 377>audio/Astra/astra_albion.ogg" 
    asidesp "That was an accident!"

    hide Albion with dissolve

    "I slide the tart onto the counter. Albion fetches two forks while I cut a slice, the crust flaking perfectly beneath the knife. We each take a bite at the same time."
    asidesh "(...Oh.)"
    "As Albion would say, it's not bad, but it's different. Not the soft sweetness I expected. There's something deeper, slightly tangy, with an unexpected heat at the end."
  
    voice "<from 381.7 to 386>audio/Astra/astra_albion.ogg" 
    aside "Did you... add something new?"

    show Albion_SC with dissolve

    voice "<from 208.5 to 213>audio/Albion/albion_good.ogg"
    al "No. I followed the recipe. Exactly."

    voice "<from 404.8 to 414>audio/Astra/astra_albion.ogg" 
    asidesm "Really? Because {i}this{/i} tastes like there's spice in it. Like, um... cinnamon?"
    "He freezes. Just for a second."

    hide Albion_SC
    show Albion_Shy2
    with dissolve

    voice "<from 214 to 215>audio/Albion/albion_good.ogg"
    al "Wait."
    "He glances toward the small collection of jars and tins neatly arranged in a row. Then he exhales, pressing a hand to his forehead."
  
    hide Albion_Shy2
    show Albion_N2
    with dissolve

    voice "<from 225 to 228.3>audio/Albion/albion_good.ogg"
    al "I think... I used the wrong tin."

    voice "<from 415.6 to 416.9>audio/Astra/astra_albion.ogg" 
    asidesp "What?"

    voice "<from 240 to 247>audio/Albion/albion_good.ogg"
    al "That wasn't nutmeg. It was cinnamon. I've been blending spiced roast recently. It must've gotten mixed in."
   

    #asidesm "You accidentally added {i}coffee spice{/i} to the tart?"

    hide Albion_N2
    show Albion_SC
    with dissolve

    #al "It seems so."

    hide Albion_SC with dissolve

    asidesh "(...That explains it.)"

    voice "<from 423.6 to 429>audio/Astra/astra_albion.ogg" 
    asidesm "I can't believe it. Mr. Perfect went rogue in the middle of baking."

    show Albion_SC with dissolve

    voice "<from 272 to 275>audio/Albion/albion_good.ogg"
    al "You're exaggerating."

    voice "<from 437 to 442>audio/Astra/astra_albion.ogg" 
    asidesp "You spiced my tart! That's basically rebellion!"

    hide Albion_SC
    show Albion_B
    with dissolve

    "His ears tint red."
    voice "<from 282 to 286>audio/Albion/albion_good.ogg"
    al "If it's terrible, I'll remake it."

    voice "<from 442 to 446>audio/Astra/astra_albion.ogg" 
    asidean "Don't you dare. It's unique. Ours."
    "For a long moment, neither of us speaks. The oven hums softly behind us, the scent of sugar and spice still hanging in the air."

    hide Albion_B with dissolve

    voice "<from 457.3 to 462.7>audio/Astra/astra_albion.ogg" 
    asidee "Mhm! I think this is it. The one."
    "I take another bite, savoring the new flavor: the warmth of cinnamon folding into the tart sweetness of berries. It's unlike anything we've made before."
    
    show Albion_Shy2 with dissolve

    voice "<from 295 to 302>audio/Albion/albion_good.ogg"
    al "It's not bad. The flavor's unexpected... but balanced."

    voice "<from 470 to 473>audio/Astra/astra_albion.ogg" 
    asidesm "Kind of like us, then."

    hide Albion_Shy2 
    show Albion_H
    with dissolve

    "He looks at me, and for the first time, he doesn't look away."
    "The quiet stretches between us, wrought with everything we've never said. The hum of the oven fades into the background; even the air seems to still."
    asideem "(He's impossible. Infuriating. And right now, he's the most perfect thing I've ever seen.)"

    hide Albion_H 
    show Albion_B at truecenter:
        zoom 1.8 
        yoffset 350
    with dissolve

    #TODO CG here!
    play music "Albion.ogg" fadeout 2.0 fadein 2.0

    "Before I can talk myself out of it, I lean forward and press my lips to his."

    scene black 
    show voiced
    with dissolve

    "The touch is like the first sip of coffee in the morning: warm, a little hesitant, and gone too quickly."

    scene albionapt
    show voiced
    show Albion_B at truecenter:
        zoom 1.8 
        yoffset 350
    with dissolve

    "When I pull back, he's staring at me, wide-eyed and utterly frozen."
    asideb "(I've broken Albion.)"

    hide Albion_B

    "I wait a beat, then say:"

    voice "<from 476.3 to 480>audio/Astra/astra_albion.ogg" 
    asidesm "First time?"

    show Albion_Shy1 at truecenter:
        zoom 1.8 
        yoffset 350
    with dissolve

    "His ears turn pink instantly."
    voice "<from 314 to 316>audio/Albion/albion_good.ogg"
    al "N-no."
    asidesm "(That sounds like a lie.)"
    "My own heart is pounding."
    #play sfx "sfx_heartbeat.ogg"

    voice "<from 480.2 to 484>audio/Astra/astra_albion.ogg" 
    asideem "Then prove it."

    hide Albion_Shy1
    show Albion at truecenter:
        zoom 1.8 
        yoffset 350
    with dissolve   

    "Something in his expression changes—hesitation replaced by intemperance."
    "He steps forward, closing the space between us in one sure motion."

    scene black with dissolve

    "The world tilts. My back hits the counter, the breath catching in my throat as his mouth meets mine again."
    "The world outside the kitchen disappears. There's only the scent of cinnamon and sugar, the low hum of the oven, and the warmth of him, closer than he's ever been. The rest of reality falls away."

    $ renpy.pause (2.0)
    jump albion_good2











