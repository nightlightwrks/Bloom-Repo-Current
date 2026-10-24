
init python:
    def text_scroll_sound(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/sfx_text.ogg", channel="sound", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")

# Apply this callback to dialogue
define config.all_character_callbacks = [text_scroll_sound]

define qn = Character('QWYNN', kind=nvl, color="#e45472")
define an = Character('ASTRA', kind=nvl, color="#7e6fd6")
define min = Character('MIDNA', kind=nvl, color="#3a0f0c")
define na = Character(None, kind =nvl)

label qwynn_after:
    
    $ persistent.status_button = False
    
    show qwynn_after
    $ renpy.pause(1.0)
    window hide
    pause (5.0)
    window auto

    play music "city_day.ogg" fadeout 2.0 fadein 2.0
    scene market with dissolve
  
    "This after story contains some mild written kissing/making out."

    menu: 

        "Continue":
            jump qwynn_afterstart
        "Return to the main menu.": 
            return

label qwynn_afterstart: 

    na "Stepping back into Halis is an instant relief. The air is cooler, and the sounds of merchants bustling back and forth bring a smile to my face."
    na "Traveling to Valanche, meeting Saint Seraphina, and getting to see the ocean every day—it was bliss. I'm happy I went on the trip."
    na "But I miss Astra… I miss our little apartment and Midna."
    na "My steps echo across the cobblestone path until I reach the apartment."
    qn "(Huh?)"
    na "Sitting on the stoop, is a small cat statue. It looks suspiciously like Midna."
    na "My grin grows wider."
    na "Looking back up, I knock on the door. Just because I want to see the look on Astra's face when she opens it."
    na "If she's even home."
    na "..."

    nvl clear

    na "The seconds seem to stretch out into minutes. Anxiety starts to creep in."
    na "The unreasonable side of my mind begins to ask questions… 'What if Astra moved out while you were gone?' … 'What if she doesn't love you anymore?' … 'What if—"

    play audio "<from 0 to 2>dooropenclose.mp3" #open

    nvl clear

    an "Qwynn?!"
    na "Every 'what if' comes to a grinding halt—replaced with a painful squeeze at seeing the pure surprise and joy on Astra's face."
    na "What she felt— What they {i}both{/i} felt was unmistakable."
    qn  "Surprise!"
    na "A blur rushes past my legs."
    an  "Saints— Midna!"
    an "Sorry, babe. Just— help me real quick, please."
    na "Astra takes off after their cat."
    na "Before Astra can get too far, I've overtaken her and caught Midna. The feisty thing squirms in my arms as Astra catches up—panting and out of breath."
    an "Hah— Thanks. I'm usually better about watching the door but…"

    nvl clear

    na "Astra shrugs and catches my gaze again. If I didn't know better I'd say her eyes had real stars in them."
    qn "It's okay, I should've thought about that."
    na "I press my face into Midna's fur."
    qn "Looks like {i}someone{/i} hasn't changed, huh?"
    an "Not at all."
    qn "C'mon, let's go back in."

    nvl clear
    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0
    scene kitchen with dissolve

    na "I can only watch Astra struggle to drag my suitcase inside for so long before I take over. I know she wants to help, but she also has terrible upper body strength."
    an "Thanks…"
    qn "No problem."
    na "After setting the bag inside my room, I step back into the living room to find Astra already sitting on the couch."
    na "She glances up and, with a smile, she spreads her arms wide—expectant."
    na "It's all too easy to throw myself into her arms."
    na "She smells like coffee and oranges. a combination that invaded my dreams near every night in Valanche."
    qn "I love you."
    an "I love you too."
    qn "I missed you."

    nvl clear

    na "She giggles."
    an "I missed you too."
    na "My arms tighten around her waist and bury my face deeper into the crook of her neck—inhaling more of her addicting scent."
    an "I can't smell that good. I've been outside all day. I just got home."
    qn "Well you do. I love it. Even when you've been out all day."
    na "One of her hands settles on my head and brushes down in a soothing motion."
    an "If you say so…"
    na "She's pouting. I can hear it in her voice."
    na "I press a kiss to her collarbone."
    an "...How was the trip? Tell me everything."
    qn "It was amazing! I've been before but only for a few days. Having three full months there? I got to experience so much more of the city!"
    
    nvl clear
    
    qn "I'd like to take you there one day."
    an "Yeah?"
    qn "Yeah. You'd like it there. You've never seen the ocean right? Well, Valanche is surrounded by it. It's hard to go anywhere and {i}not{/i} see it."  
    qn "I'd love to see the look on your face when you realize how big it is." 
    an "It sounds so peaceful…"
    qn "It's practically built to be that way."
    qn "Oh! You'll never believe this but, I met the Fire Saint!"
    na "Astra pushes me up to search my face. She can tell when I'm lying."
    an "You're telling the truth…!"
    qn "Of course I am! Saint Seraphina isn't a recluse like Saint Caelan. She runs guided tours around the city and I got to participate."
    an "It's hard to imagine…"

    nvl clear

    qn "Right? I'm so happy I went~"
    na "Her face softens as she watches me speak."
    an "Me too. You look lighter… more like yourself."
    qn "...I feel it too."
    qn "Thank you for encouraging me to go. I almost forgot how much I love to travel."
    an "You wouldn't be 'Qwynn' if you didn't."
    na "I lean in to brush a kiss over her lips—she chases me when I pull away and I'm more than happy to let her catch me."
    na "Her lips are soft… and she tastes like coffee. It's bitter, the exact opposite of the sugary sweetness I like—but I wouldn't have it any other way."
    na "I grasp her hips and roll to the side, flipping our positions so she's the one on my lap."
    na "The motion makes her smile, and our teeth clack together."

    nvl clear

    na "She recovers quickly though—Astra dives in again, pressing our lips together with more force."
    na "A warm hand slips beneath my blouse. The bracelet I gave her all those months ago is cold against my stomach."
    na "I reach to pull her in further. To have her so close that we can't be told apart anymore."
    na "Astra leans back."
    an "I'm so happy you're back."
    min "meow~"
    na "Midna jumps into the small space between them. Her purrs rumble against my chest."
    an "Apparently, so is Midna."
    qn "I'm happy to {i}be{/i} back. Oh! Speaking of Midna, where did you get that statue? The one out front."
    
    nvl clear

    an "It's cute right? Actually, one of the employees at Voyage Étoilé found it and gave it to me."
    qn "You've been going to the boutique while I've been gone?"
    an "Of course... I know how important it is to you. I only stop by once a week or so to make sure everything's okay."
    qn "Aste—"
    an "They miss you though. Even when you're gone, it's still your place—your heart—that keeps it alive."
    qn "You're gonna make me cry, Aste. You didn't have to do that."
    an "I wanted to. Besides, it was easy. Your team's been doing a great job, there's new stuff in there all the time."
    an "And I'm sure you have more in your bag. That thing felt like it had bricks in it!"
    qn "It's full of gifts—for you. Remember? Girlfriend privileges."
    an "I don't remember that…"

    nvl clear

    qn "Yes you do. You have a great memory."
    na "Astra slumps against my chest to hide her face. She grumbles something so unintelligible that—even with my sense of hearing—I can't make it out."
    qn "Aww, c'mon, don't pout. I thought it was cute!"
    an "You think everything I do is cute…"
    na "I give her a squeeze. Midna meows in protest."
    qn "Exactly!"

    nvl clear

    play music "Qwynn.ogg" fadeout 2.0 fadein 2.0
    scene kitchen_evening with dissolve

    na "Hours pass by like that. Us—together—cuddled up on the couch with our cat who snores loudly nearby."
    na "I don't want to move. I don't want to disturb this peace, this softness ns that I thought was out of reach."
    na "My fingers trace nonsensical patterns over Astra's back. However, unlike Midna, she's still awake—barely."
    qn "Still with me?"
    an "Mhm…"
    qn "We should get up soon."
    an "Mhm."
    qn "We can have dinner, and then cuddle in bed. Doesn't that sound nice?"
    an "But— You're so warm."
    na "She yawns."
    an "I want to stay here. Just a little longer…"

    nvl clear

    na "Saying no to Astra when she's {i}not{/i} clinging to me is a challenge. Which means she absolutely gets her way. No one's moving from this spot unless Astra gets up first."
    na "So, I continue my work tracing shapes over Astra."
    na "A thought pops into my head."
    qn "I want to go to Grav next. Maybe in a few months."
    na "I watch her blink, eyes heavy with exhaustion. Then, she smiles."
    an "I'll miss you."
    qn "I always come back."
    na "Astra's the one to lean in this time. When she pulls away she whispers—"
    an "And I'll be waiting for you."
    
    stop music fadeout 2.0
    window hide
    $ renpy.pause(2.0)
    return


   