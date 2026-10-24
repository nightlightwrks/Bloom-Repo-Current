# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



#########################################
# CAELAN CHAPTER 3
#########################################

label Caelan_chp3:
  
    window hide
    show caelan_chp3 with squares
    window auto
    pause (2.0)

    $ persistent.status_button = True

    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior_evening with squares
    
    "A few days later, I wait for everyone helping me with my proposal to gather in the café."
    "Well, everyone save for Albion who's been here for the last few hours meticulously tweaking his blend for what feels like the hundredth time." 
    "I'd decided to host an after hours meeting to make sure everything was still on track. Sylphia's absent, and I have a feeling she planned it that way."
    "I peek up at Albion, eying him warily from my station at one of the tables."
    aside2 "How many times have you adjusted the recipe now?"
    
    show Albion with dissolve

    al "32."
    asidesh2 "That seems a little… excessive."

    hide Albion
    show Albion_SC 
    with dissolve

    al "You can't complain when you're the one who begged me to help you."
    asidean2 "I did not {i}beg{/i}, Albion. I don't beg."
    al "Sounded like begging to me."
    asidesp2 "You said—"

    play audio "<from 0 to 3>bell.mp3"
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0

    show Albion_SC at Transform (xpos=600) with ease
    show Qwynn_N3 at right with dissolve

    q "Albion, long time no see! Bullying Astra again I see."
    al "Qwynn."
    q "I could hear you guys as I was walking up. A year of knowing each other and you still don't get along."
    
    hide Qwynn_N3
    show Qwynn_S at right
    with dissolve
    
    q "You could be friends—if you put your minds to it. Not best friends though. That spot's taken I'm afraid."
    "I chuckle."
    al "Maybe if she stopped asking obvious questions—"
    asidean2 "My questions aren't obvious, you just hate explaining things!"

    hide Albion_SC with dissolve
    hide Qwynn_S with easeoutright

    "Qwynn appears behind me and places both of their hands on my shoulders."

    show qcutin2 with easeinleft 
    q "It's okay Aste, I'm here to protect you from him now~"
    
    hide qcutin2 with easeoutright
    show Albion_SC with dissolve
    
    "Albion scoffs."
    al "She hardly needs {i}your{/i} protection."

    show Albion_SC at Transform (xpos=600) with ease
    show Qwynn_A at right with dissolve

    q "What's that supposed to mean?"
    al "Exactly what I said."
    "Qwynn opens their mouth to respond but I jump in first." 
    asidesp2 "Cut it out, both of you. Felix will be here any second and this is supposed to be a {i}professional{/i} meeting."
   
    hide Qwynn_A
    show Qwynn_N3 at right
    with dissolve

    q "Fine."
    al "..."
    asidesh2 "...Great."

    play audio "<from 0 to 3>bell.mp3"
    hide Qwynn_N3
    hide Albion_SC
    with dissolve

    asidee2 "(Saved!)"
    "Felix steps in carrying a sketchbook under one arm but he pauses at the threshold."

    show fcutin2 with easeinleft
    f "Woah, what's with all the tension?"

    hide fcutin2 with easeoutright
    show Felix with dissolve

    asidesh2 "It's nothing."

    hide Felix with dissolve

    "Felix waves as he walks the rest of the way in and takes the seat directly across from me. Qwynn follows suit but with the seat to my left."
    
    show Qwynn_S at Transform (xpos=200)
    show Felix at right
    with dissolve
   
    aside2 "Felix, meet Qwynn and Albion. Qwynn's here to help with our new marketing campaign, and Albion is my coworker who's been tasked with creating a signature coffee blend for us."
    aside2 "Qwynn, Albion, this is Felix. He's painting a mural on the wall up front."
    
    hide Qwynn_S
    hide Felix
    with dissolve
    
    "I start to shuffle my notes into a more comprehensible order while they exchange more greetings."
    asidesp2 "Albion, you should come sit too."
    al "..."

    show Albion with dissolve

    "Albion complies, though he stops to grab a tray of drinks which he brings with him to the table."
    asidee2 "Oh! Is this one of your samples?"

    hide Albion
    show Albion_SC
    with dissolve

    al "It's not perfect. But— yes."
    aside2 "I'm sure it's delicious. Honestly, they've all been good."
    "However, Qwynn and Felix look a bit less enthused."
    
    show Qwynn_N3 at Transform (xpos=50)
    show Felix_N2 at Transform (xpos=1200)
    with dissolve
    
    q "Can I add milk?"
    f "Or sugar?"
    "Albion's face scrunches up."
    al "Why are they here again?"
    asidesp2 "Because they're valuable members of this team."

    hide Qwynn_N3
    hide Felix_N2
    show Qwynn_S at Transform (xpos=50)
    show Felix at Transform (xpos=1200)
    with dissolve

    al "Your team."
    asidee2 "{i}Our{/i} team."

    scene cafe_interior_evening with dissolve
    show acutin with easeinleft

    "Albion stares blankly."

    hide acutin with easeoutright
    show Felix with dissolve

    f "I'll go first! Do I just drink it straight?"

    show Felix at Transform (xpos=1300) with ease
    show Albion_SC at Transform (xpos=200)
    with dissolve

    al "No. First you have to do a dance."
    f "If you insist—"
    al "Please don't."
    "Felix just grins and takes the mug into his hands."

    show Felix at Transform (xpos=1600) 
    show Albion_SC at truecenter 
    with ease
    show Qwynn_N3 at Transform (xpos=30) with dissolve

    "Qwynn reluctantly grabs their own mug."
    q "I do this for you, Astra."
    aside2 "And I appreciate it."
    "Albion and I take our cups last. I look up at Albion."
    aside2 "Tell me about it."

    hide Albion_SC
    show Albion at truecenter 
    with dissolve

    al "This one's a medium roast with floral and citrus notes. More floral than citrus."
    
    hide Felix 
    show Felix_C at Transform (xpos=1245)

    f "You put fruit in here?"
    q "I didn't know you could do that."

    hide Albion
    show Albion_SC 
    with dissolve

    "Albion sucks in a deep, frustrated breath." 
    al "Astra—"
    asidesp2 "There's no fruit in it. Or flowers for that matter. The notes should just remind you of those things."
    
    hide Qwynn_N3
    show Qwynn at Transform (xpos=30)
    with dissolve

    q "Uhhh… okay?"

    hide Felix_C
    show Felix_N2 at Transform (xpos=1245)
    with dissolve

    f  "If you say so."
    al "I won't be taking your opinions into account anyways."
    asidean2 "Albion—"
    al "What?"
    aside2 "Not all of our customers are coffee experts like you, they'll be able to give us some good insight."
    al "..."
    aside2 "Now, c'mon lets try it."
    "..."
    
    scene cafe_interior_evening with dissolve
    
    "The reactions are mixed. Felix looks confused. Qwynn has an eyebrow raised in surprise. And Albion, well, he's scowling harsher than usual."
    "Qwynn speaks up first."

    show Qwynn_N3 at truecenter with dissolve

    q "I can smell the notes you're talking about. Taste them too. Though, I still don't know that I'd drink it without milk."

    hide Qwynn_N3
    show Felix_C 
    with dissolve

    f "Really? I'm not getting citrus or floral anything… If I'm being  honest, all coffee kinda tastes the same to me."
    
    hide Felix_C
    show Albion_SC
    with dissolve

    al "It's not right. Something's off about it."

    hide Albion_SC 
    show Qwynn at Transform (xpos=50 )
    show Felix_N2 at Transform (xpos=1200) 
    show Albion at Transform (xpos=580)
    with dissolve

    asidesp2 "I think it tastes good! But, I do wish the floral notes were a bit stronger. It'd fit with our branding better, right Qwynn?"
    
    hide Qwynn 
    show Qwynn_S at Transform (xpos=50)
    with dissolve

    q "Definitely. Promoting a blend that reflects the name 'Bloom' is almost too easy. There's no real reason not to."
    al "...I can make it more floral."
    "I glance between Qwynn and Felix, who haven't touched their cups after their first sip."
    asidesh2 "And could you make a latte version as well? Maybe one using honey as the sweetener?"
    
    hide Felix_N2
    show Felix at Transform (xpos=1200)
    with dissolve
    
    "Albion follows my gaze to where Qwynn and Felix smile innocently."

    hide Albion
    show Albion_SC at Transform (xpos=580)
    with dissolve

    al "...Fine."
    "He stands up, taking the two fuller mugs with him."

    hide Albion_SC with dissolve
    show Qwynn_S at Transform (xpos=200)
    show Felix at Transform (xpos=900)
    with ease

    asidesp2 "Okay, next order of business."
    aside2 "Felix, did you bring the sketches?"
    f "Yep! I made a few so you can just pick the one you like best. Or, if you hate them all, we can come up with something new together."
    asidesm2 "I'm sure it won't come to that."
    
    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior_night with dissolve
    
    "We spend another hour discussing plans and logistics." 
    "Everyone falls into a comfortable rhythm of proposing and discussing ideas. Even Albion starts to lighten up after Qwynn and Felix praise his latte making skills."
    aside2 "(I never thought I'd see everyone working together to create something new.)"
    "The sight causes something in my chest to squeeze. It's so simple, just a meeting with the team I'd gathered—but it feels like so much more than that."
    "It feels like enough to push me to one-hundred percent."
    aside2 "I'll be right back."
    "Qywnn looks up first."
    
    show Qwynn_N3 at truecenter with dissolve
    
    q "Everything okay?"
    asidesp2 "Yep! Just going to get some air. I'll be back in a few minutes." 
    
    hide Qwynn_N3 
    show Qwynn_N3 at Transform (xpos=200) 
    with ease
    show Felix_N2 at right with dissolve

    f "Be careful! It's getting a bit dark."
    "Albion doesn't say anything, but I feel his watchful gaze follow me out the door." 

    play music "city_night.ogg" fadeout 2.0 fadein 2.0
    scene market_night with dissolve

    "There's so many feelings swirling around in my chest. An overwhelming wave of emotion washes over me with surprising force."
    "I walk away from Bloom, away from the intimate lighting pouring through the windows and the muffled voices coming from inside."
    "I stroll until I stand on the opposite street, until I can see my friends from the perspective of a stranger."
    aside "They look so happy."
    "For the past few days, so much of my time has been spent worrying over logistics and the stress that comes with accepting more responsibility."
    "Looking at Café Bloom from the outside feels wrong."
    "The feelings that have been rising up hit me with startling clarity."
    aside "I belong there."
    "The window of the café becomes a porthole to the future." 
    aside "(I can see myself there, in Sylphia's shoes. Talking with customers, coming up with more overzealous plans to build the cafe up even more…)"
    aside "(Sylphia's offered me everything I've been dreaming of.)"
    "The question I posed to myself not too long ago repeats itself."
    "Will I regret saying 'yes'?'"
    "And this time, the answer is a resounding 'no'."
    aside "(Which means, I know exactly what I want to do.)"
    "I nod to myself as I step to cross the street. A bridge back to where I belong—when a whiff of lavender halts me in my tracks."
    "I turn around with an excited smile."
    asidee "Caelan—!"

    play music "tension.ogg" fadeout 2.0 fadein 2.0

    scene market_night with hpunch
    play sfx "sfx_shake.ogg" 

    "A shadow, one that is very distinctly {i}not{/i} Caelan,  moves swiftly and with frightening precision to grab my arm."
    "I don't have time to react before they drag around the corner and out of sight from Café Bloom to push me forcefully against the wall of an alley."
    
    show black with dissolve
    show market2_night with easeinleft

    "It's the first time I've ever felt afraid in Halis."
    "Hooded Figure" "Caught you."
    asidean "W-what?"
    "The cloaked figure presses my shoulders to the stone behind me with even more force."
    "Hooded Figure" "The runt. The one you've been hanging around with."
    "Something clicks. A dozen little puzzle pieces coming together to form one complete picture." 
    "My eyes shut as they lean in."
    asidesa "I-I don't—"
    "It's getting hard to breathe through my panic— What am I supposed to do?"
    asidesa "..."
    "Hooded Figure" "Silent treatment huh?"
    "Hooded Figure" "It doesn't matter either way."
    "Hooded Figure" "Your little 'Saint' has been appearing in the city more often. Interrupting our operations. It's becoming a problem."
    "I suck in a deep breath, trying to regain control of my beating heart before I pass out."
    asidesh "I have no idea what you're talking about."
    "And it's true. As far as I'm aware, Caelan is just a friend. I don't know anything about what's happening."
    "Even if I did, I wouldn't tell."
    "Hooded Figure" "Now isn't the time to play dumb. I've watched them go out of their way to see you. That means you're important to the Saint. Very convenient for me."

    #chain sfx? 

    "Something moves within the man's cloak, and it's then that I notice a dim light shining through the inky black cape."
    "Anything else the man says afterwards is lost. My attention is now fixed on the light. Any control I had regained over my breathing is lost as I realize what I'm really dealing with."
    asidesp "Elemental…"
    "He smirks and—still keeping one hand pressed to my shoulder—pulls the fabric aside to reveal a flickering fire elemental trapped inside of a cage."
    "Hooded Figure" "Useful little things, if you know how to properly deal with them."
    asidean "They're nature itself—"
    "A shiver runs down my spine."
    asidean "Y-you can't contain them. Everyone knows that—!"
    "The man leans forward, crowding my personal space and blocking my view of the cage again."
    "Hooded Figure" "Afraid it's going to explode?"
    "Yes. Of course I am. Even a human like me with no affinity for magic can sense how powerful the spirit on the man's hip really is."
    "I have to do something. Now."
    asidesh "I don't have the information you want."
    "Hooded Figure" "I don't need information from {i}you{/i}.{w} You're just bait." 
    "I shake my head frantically."
    "Bait???" 
    asidesa "Caelan doesn't even know I'm here right now."
    "Hooded Figure" "Oh, but they do."
    "It's said with a self-assured grin. One that slices through my already-thin front of calm."
    asidea "...What did you do?" 
    "He tilts his head in the way you do when regarding a lost puppy."
    "Hooded Figure" "I only left a little gift at the Sanctuary."
    "The Sanctuary. Located at the center of the city in the heart of a forest. It's off-limits to everyone besides Saint Caelan and their attendants."
    asidean "W-what kind of gift?"
    "Hooded Figure" "I'm sure you can guess."
    "My gaze drops back to the flickering light." 
    asidea "..."
    asidesa "...Is the plan just to wait here until someone shows up?"
    "Hooded Figure" "Not 'someone'. Saint Caelan."
    asidesh "How do you know they'll show up. And even if they do, how do you know someone else won't stumble across us first?"
    "Hooded Figure" "Go ahead. Scream if you want."
    "He nods his head towards the cage on his hip."
    "Hooded Figure" "Let's see how this little guy reacts to loud, piercing noises."
    asidea "..."
    "Hooded Figure" "Thought so."
    asidesh "My friends are waiting for me. They're going to wonder why I've been gone for so long."
    "He shrugs."
    "Hooded Figure" "The little Saint will be here first. I'd bet money on it."
    "..."
    "Part of me wants Caelan to come. The other wishes there was a way to end this myself and pretend like nothing happened."
    "I pull my bottom lip in between my teeth, biting it hard to keep the panic at bay."
    "The stranger's grip is tight. Every small move I make is rewarded with an extra ounce of pressure."
    "I can already feel bruises forming along my back where the bricks of the building press into my skin."
    "The sound of hurried footsteps echo in the night." 
    "A spark of hope ignites in my chest, quickly extinguished by dread when I see the hooded man's ecstatic smile."
    "Hooded Figure" "See? What did I tell you?" 
    "I have no response to that. Not that it matters, because not a second later a wad of cloth is being stuffed into my mouth and secured with a strip of fabric."
    asidean "(?!)"
    "A shocked noise attempts to leave me, only to be consumed by the gag." 
    "Hooded Figure" "There. That'll rile them up." 
    ca "Astra?!" 
    "The footsteps, which had been getting closer and closer, finally find us."
    "Caelan stands ragged at the end of the street. Their clothes are scuffed and dirty, and their chest heaves with the effort of simply breathing." 
    "What hurts me the most is their expression. A mix of horror and anger as they take in the scene before them." 
    "Their hood has long since fallen off. Their tail, normally safe within the shadows of their cloak, now whips wildly back and forth."

    show Caelan_ST with dissolve

    ca "She has nothing to do with this—"

    hide Caelan_ST with dissolve

    "Hooded Figure" "No, but she got you here." 
    "Caelan takes a step forward." 
    "The man, clutching my wrists together with a painful one-handed grip, reveals the fire elemental from within the folds of his cloak."
    "Caelan's eyes narrow."

    show Caelan_ST with dissolve

    ca "What do you want?"
    "Hooded Figure" "What I want is for you to stay out of our business."
    "Their eyes flick to me, then back to the stranger. The smuggler."
    ca "Your 'business' puts {i}all{/i} of Halis in danger. Elementals are not tools. They are living creatures."
    ca "You think you can control them—but it is a fool's errand."

    hide Caelan_ST woth dissolve

    "Hooded Figure" "Let's skip the grand speeches—"

    scene market2_night with vpunch
    play sfx "sfx_shake.ogg" 

    "My knees hit the ground as I'm pushed to the ground towards Caelan."
    "I blink rapidly to try and stop the incoming tears. Saliva builds up in my mouth uncomfortably."
    "I want nothing more than to break down."
    "Hooded Figure" "All this time trying to pin down your movements, trying to escape you and your Nymphs' operations… to think all we had to do was wait for you to compromise yourself."
    "Hooded Figure" "I guess I should have realized your weakness sooner… Considering what happened last time." 
   
    show Caelan_ST with dissolve   

    c "You—"

    hide Caelan_ST with dissolve

    "Hooded Figure" "I guess I should be thanking you— Here. Take her."
    "Embarresmant, pain, anger, and guilt swirl in my gut, they form a confusing cocktail of emotion that finally frees the tears I'd been holding back since being dragged into this alley."
    "Caelan rushes forward then, falling to their knees before me."
           
    show Caelan_SA:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve   

    ca "Astra—"
    "Through blurred vision I can just barely make out the look on Caelan's face. It's one I've never seen before, like their whole world has collapsed right in front of them. Devastation unfiltered."  
    "Gentle hands remove the fabric from my mouth, and I nearly choke on my next inhale. Even with the ability to speak again, words fail me."
    "Caelan's voice cuts through the ringing in my ears. It takes a moment to realize they aren't speaking to me."  

    hide Caelan_SA
    show Caelan_ST:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve   

    ca "You want my cooperation? Allow me to take her somewhere safe first."
    ca "You used her to lure me here. It worked. Now she can go home."
    "Hooded Figure" "No need. You're both exactly where I want you."
    
    #TODO come back with new expressions

    hide Caelan_ST
    show Caelan_H:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve   

    "Hooded Figure" "Some lessons need to be taught twice."
    "The unclipping of metal. A burst of light and a sudden blazing heat that seems to suck all of the air from my lungs."
    "When I look up towards the man who threatened me I'm met instead with the sight of a—now free—fire elemental hurtling towards us."

    hide Caelan_H
    show Caelan_ST:
        zoom 1.3
        xoffset 450
        yoffset -80
    with dissolve   

    ca "Fuck—"
    "Their name shakes loose from my throat."
    asidesp "Caelan!"
    "They react faster than I could ever hope to."

    hide Caelan_ST with dissolve
    play sfx "sfx_watermagic.ogg" 

    "Hastily, they throw out a hand and a wall of water materializes between us and the ball of fire."
    "Hissing steam fills the air as the two forces meet. The elementals' unrelenting flames vaporize Caelan's water magic—but it seems to be enough to stop the fire from consuming us completely."
    
    show Caelan_ST with dissolve

    ca "Astra—you have to go."

    hide Caelan_ST with dissolve

    "I would love to leave. Fear still clings to me like glue. My jaw aches and my knees are definitely bleeding."
    asidea "(But I can't run away yet.)"
    "I wipe my face and suck in a deep, steadying breath."
    asidean "...Not yet."

    show Caelan_ST with dissolve

    ca "I can not unleash the full force of my magic if there is anyone in the area. Please—"
   
    play sfx "sfx_watermagic.ogg"  
    hide Caelan_ST with dissolve


    "They throw up another wave, and I notice that none of the water reaches me. That they're taking care to guide their magic around me—even in such a dire situation."
    asidea "…"
    "I consider my options."
    asidesp "I'll go find help."
    "If nothing else, I can at least gather others who are willing to help."
    "I think about Sylphia's words again."
    "'Before you are a leader, success is about relying on yourself. When you become a leader, success is all about relying on others when needed.'"
   
    show Caelan_ST with dissolve

    ca "No— Just go somewhere safe. I can handle this alone."

    hide Caelan_ST with dissolve

    "Their stubbornness strikes a cord of anger within me."
    asidesh "(Don't they realize that doing this alone will make things worse?!)"

    show Caelan_SA with dissolve

    asidean "But you don't have to!"
    asidean "You're barely containing it right now, more people will be hurt if—"

    show Caelan_ST with dissolve

    ca "No! I refuse to put anyone else in danger." 
    ca "I am sorry, Astra."

    hide Caelan_ST with dissolve

    "Caelan tries to focus on the elemental before them, brows furrowed in concentration, but their gaze keeps flicking back over to me. It's carefully contained by water magic—for now." 
    
    show Caelan_SA with dissolve

    ca "I never should have come back." 
    "Their voice wavers."
    ca "I should have stayed in the shadows— I…"
   
    hide Caelan_SA
    show Caelan 
    with dissolve
   
    ca  "Please… just go. I will take care of this." 
    asidesp "You need help!"

    hide Caelan
    show Caelan_ST
    with dissolve

    ca "This is {i}my{/i} job, Astra!"
    asidean "Halis' guards are capable. This is exactly the kind of thing they train for!"
    ca "This only happened because of me. It is my concern alone."
    asidesh "...You had to put out another elemental in the Sanctuary right?"
    "The 'gift' that the smuggler left."
    "Caelan's hands start to shake with the effort of keeping the elemental contained." 

    hide Caelan_ST
    show Caelan_SA 
    with dissolve

    ca "I calmed it down and ordered Nimue to take it away." 
    asidean "My point is that you're already tired. How much more magic can you use?"

    hide Caelan_SA
    show Caelan
    with dissolve

    "Their face looks grim."


    ca "Enough."
    "They aren't listening."
    asidesp "Cael—"

    hide Caelan with dissolve

    who "Astra?!"
    "I recognize the voice instantly. Qwynn." 
    "I turn just as Qwynn and Felix round the corner looking out of breath."

    show Qwynn_A at Transform (xpos=200) 
    show Felix_C at right 
    with dissolve

    f "Is that—"
    q "What—"
    asidesp "Qwynn! Felix! Perfect timing."

    scene market2_night with dissolve

    "I cross the distance between us on slightly shaky legs." 

    show Qwynn_A at Transform (xpos=500) with dissolve

    q "Saints, Astra! What happened?!"


    "I hear a sigh of relief sound from behind me. It's followed by a commanding voice. One that decidedly belongs to the Water Saint and not Calean."
    
    show Qwynn_A at Transform (xpos=200)
    with ease
    show Caelan_ST at right with dissolve 
    
    ca "All of you need to leave. Now." 
    asidean "I'm going to find help."
    ca "I told you I—"

    show Qwynn_N3 at Transform (xpos=200) with dissolve

    asidean "Qwynn. You're the fastest. I need you to alert the city guard and let them know what's happening."

    scene market2_night

    "I look to Felix, ready to delegate another task only to find him rooted to the ground. His eyes are round with terror and fixed squarely on the wild flame centered within Caelan's magic."
    asidea "...And take Felix with you." 

    show Qwynn_M at half_size with dissolve

    q "Wait—Astra, you're hurt—"
    asidea "Qwynn, please."

    hide Qwynn_M with dissolve

    "I spare a glance to Caelan who's losing more and more control by the second."
    asidea "We're running out of time. Alert the guard."

    #add effect here? 

    "Water starts to form in fat droplets around me. Caelan must have started pulling water from the air."

    show Qwynn_N3 at half_size with dissolve

    q "...What about you? I won't leave you here."
    asidea "I'm going to start evacuating the area. One less thing for the guard to do."
    "Qwynn seems to hesitate for a second, their gaze sliding over my shoulder for a moment until they shake themselves, fixing me with a sharp look."
    
    hide Qwynn_N3
    show Qwynn at half_size 
    with dissolve

    q "Fine, but I don't try to be a hero." 
    "I can't help but smirk."
    asidesm "No need. I think my friend here already has that covered." 

    hide Qwynn with dissolve

    "The air warms by a few degrees." 

    show Caelan_ST with dissolve

    ca "Astra! All of you, leave here immediately."
    "Before I can protest, Qwynn picks me up with one arm and grabs Felix's arm with the other."

    scene market2_night with vpunch
    play sfx "sfx_watermagic.ogg"

    asidesp "Ah—"
    f "..."  

    #speed lines on screen? idk
    scene market_night with dissolve

    "As soon as we've made it to a safer distance—just outside Café  Bloom—Qwynn sets me down gently and releases Felix."
    aside "Thank you, Qwynn. You know where the nearest guard station is, right?"

    show Qwynn_S at half_size with dissolve

    q "Yep! No worries."

    hide Qwynn_S 
    show Qwynn at half_size
    with dissolve

    "Their tone turns serious."
    q "I'll be running straight back to find you as soon as I'm done."
    aside "...Sure, be careful alright?"
    q "You too."

    hide Qwynn with easeoutright

    "After that, Qwynn sprints off." 

    #play audio "<from 0 to 3>bell.mp3"

    "The café door swings open."

    show Albion_N2 with dissolve

    al "That was a long wal—"

    hide Albion_N2
    show Albion_SC
    with dissolve

    al "What happened?"
    asidea "No time."
    asidea "You can help me evacuate the area or you can go with Qwynn to alert the guard." 
    "Albion doesn't even flinch." 
    al "...And him?"
    "Albion points distantly at Felix who, at some point, had backed himself up against the café wall and has started rubbing his arms roughly."
    asidesh "We… don't have time to help him right now."

    show Albion_SC at Transform (xpos=550) with ease
    show Felix_U at right with dissolve

    f "...Don't talk like I'm not here…."
    aside "You should head home. Your studio is far enough away that you'll be safe."
    who "I thought you guys were having a meeting? Why are you all outside?" 
    "It's hard not to recognize {i}that{/i} voice. Always entirely too at ease." 

    hide Albion_SC 
    show Velvet at Transform (xpos=200)
    with dissolve

    asidesp "Vel! This is great, you can take Felix home." 
    "Their steps speed up until they stand next to me."
    v "That's what I came to do anyways… What's going—"
    "Velvet's eyes land on Felix."

    scene market_night with dissolve

    v "Fe?" 
    "I ignore the rest of that exchange. More concerned with all the time we waste standing around making plans." 

    #explosion sfx

    "As if to prove my point, the sound of windows imploding sounds off in the distance." 
    " My heart jumps into my throat. I swallow, unwilling to let my anxieties take hold."
    "There will be time for that later."
    asidea "...New plan. Albion, help me evacuate the area." 

    show Albion_SC with dissolve

    al "Okay."

    hide Albion_SC with dissolve

    asidea "Vel, you should both leave as soon as you can. Out of Block 5 entirely just to be safe."
    "They don't turn to look at me."
    v "Thanks for the heads up." 
    v "Careful out there, yeah?" 
    aside "Yeah. We will be."

    scene market_night with dissolve

    "Albion and I split up almost immediately to cover more ground."
    "The bright side about explosions is that they're pretty loud. Most of the people nearby are already on their way to safety after hearing it."
    "Some stay to help guide people away from where Calean is attempting to keep the damage to a minimum after the elemental escaped their magic bubble."
    "Fortunately, no one let the shock of seeing Saint Caelan break their decades long seclusion stop them from helping with the evacuation efforts."
    "I do my best to direct people as best I can, shouting directions over the noise."
    "Eventually, the guard arrives. A slew of Elves and Naiads lead them, ready to assist Caelan in any way they can." 
    "They don't hesitate to stand beside their Saint. Large amounts of water are diverted from the canals, which eases Caelan's burden." 
    "A gentle hand touches my arm."
    
    show Qwynn at half_size with dissolve

    q "Hey. The guards are here now, let them handle this."
    asidesh "But…"
    "Qwynn traces my line of sight."

    hide Qwynn
    show Qwynn_N3 at half_size
    with dissolve

    q "They'll be fine. See? It looks like they have it under control now. The elemental seems much calmer."
    play music "city_night.ogg" fadeout 2.0 fadein 2.0


    hide Qwynn_N3 with dissolve

    "And it's true. Its fire is dimmer and its movements are less erratic."
    "I watch Caelan raise a hand, signaling the guards to stand down."
    "This time when the magic fades there isn't an accompanying blast of heat. Instead the elemental flame flickers softly as Caelan approaches."
    "After some time, Caelan and the flame seem to reach an understanding and it's encased again in a bubble of water and handed off to a nearby Naiad."
    "The Naiad is one of Caelan's attendants—who must have shown up while I was distracted—takes the creature gently into his palm and begins to walk in the direction of the east gate."
    "The assorted crowd sighs in collective relief."
    "The silence lasts maybe a second before all eyes come to rest on Caelan. People and guards alike start whispering. Caelan looks uncomfortable, shoulders tense and eyes downcast." 
    "Ignoring them, I walk right to the center of the stares."
    asidesp "Caelan?" 
    "They whip towards me." 
    
    show Caelan_C with dissolve

    ca "Astra! I asked you to escape—"
    asidesm "I did. Temporarily."

    hide Caelan_C with dissolve

    label caelan_ending:
    if (caelan_pts >= 80):
        jump caelan_good
    else:
        jump caelan_bad

    #jump Qwynn_chp3

#########################################
# END
#########################################









