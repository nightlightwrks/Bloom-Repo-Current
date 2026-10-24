# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define fside = Character ("FELIX", color="#4faa8d", image="felix")
define fsides = Character ("FELIX", color="#4faa8d", image="felixs")
define fsidesad = Character ("FELIX", color="#4faa8d", image="felixsad")
define fsideu = Character ("FELIX", color="#4faa8d", image="felixu")
define fsidec = Character ("FELIX", color="#4faa8d", image="felixc")
image define fside = "side felix"
image define fsides = "side felixs"
image define fsidesad = "side felixsad"
image define fsideu = "side felixu"
image define fsidec = "side felixc"


#########################################
# FELIX CHAPTER 3
#########################################

label Felix_chp3:
   
    $ persistent.status_button = True

    window hide
    show felix_chp3 with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    window hide
    show felix_pov with dissolve
    $ renpy.pause(2.0)
    window auto

    scene market2 with squares

    "Astra goes limp in his arms, and Felix panics. The weight of her body jolts him into motion almost instantly." 
    "He quickly changes his grip, lifting her into his arms while his eyes check her face for signs of distress."
    "His heart hammers desperately—walls closing in on every side, threatening to suffocate him. He looks down at Astra, unconscious in his hold."
    fsidec "(Calm down, Felix. Focus. This isn't like last time.)"
    "Her chest rises and falls steadily. He exhales in relief."
    fsides "(She's just asleep.)"
    "Felix adjusts his grip, making sure Astra won't fall from his arms on the way back to her apartment."
    fsideu "(Although, now I don't have anyone to tell me exactly where to go…)"
    fsideu "(I'll have to figure that out later. For now, getting her somewhere safe is the most important thing.)"
    
    scene market with dissolve
  
    "Felix walks as fast as he can while carrying Astra. At last, he enters Block 4 where he's finally forced to face the issue at hand."
    fsideu "(I have no idea where she lives.)"
    "Astra's head rests against Felix's shoulder, emanating a concerning warmth." 
    "Just then, he hears a panic-stricken voice calling Astra's name. He turns on his heel."
    who "Astra?!" 
    fsidesad "(A friend?)"
    fside "Over here!" 

    show Qwynn_M at half_size with easeinright
    
    "A figure rushes towards him: a Were-wolf if the ears are anything to go by. On meeting, they completely ignore him, focusing only on Astra."
    "Their hands press over her forehead."
    who "Is she okay?"
    fside "I think so. She just fell asleep."
    "Their shoulders visibly relax at his reassurance."

    hide Qwynn_M
    show Qwynn_N3 at half_size
    with dissolve

    who "I swear, she's too stubborn for her own good. I took my eyes off of her for one second and—"
    "They stop themselves, gaze softening."

    hide Qwynn_N3
    show Qwynn_M at half_size
    with dissolve

    who "Well, it doesn't matter. You found her. Thanks…"
    fside "Felix."
    who "Right… Felix." 
    q "Thank you. I'm Qwynn."

    hide Qwynn_M with dissolve

    fside "(Qwynn? I think Astra's mentioned them before. Her roommate.)"
    "Qwynn's hands reach out to take Astra from Felix's hold. He finds himself subtly shying away from Qwynn to keep Astra held closely to his chest."
    fside "Ah— I can keep carrying her." 

    show Qwynn_M at half_size with dissolve

    fsideu "(What am I saying?)"
    "Pain flickers across the Were-wolf's face. Their hands retreat and their eyes shut."
    
    hide Qwynn_M
    show Qwynn at half_size 
    with dissolve   
    
    q "Fine… Follow me."

    hide Qwynn with easeoutright

    "Felix is led to the outskirts of Block 4, to an apartment with a wreath of spring flowers hanging out front. Bright and inviting, just like Astra."
    "Qwynn opens the door and holds it aside for Felix to step through. Clearly, it's a reluctant invitation. He crosses the threshold and pauses, waiting for more direction. "
    
    scene kitchen 
    show Qwynn at half_size 
    with dissolve
    
    q "Astra's room is straight ahead. We can lay her down there." 

    hide Qwynn with dissolve

    "They open the door. Astra's space is calm and lived-in: scattered trinkets, a notebook open to a page labelled 'Bloom Revitalisation Plan', and the faint scent of flowers in the air." 
    "Felix hesitates at the threshold, feeling like he's intruding."
    
    show bedroom with dissolve

    "It's odd to be walking into Astra's space after he tried so hard to distance himself. Each step he takes is one step too far… After ensuring her safety, he would extract himself from her life once and for all."
    "Carefully, Astra is set into her bed. Felix spots a wayward blanket covered with vibrant floral blooms and draws it over her." 
    "With the motion, he makes a wish."
    fsides "Sleep well, Astra." 
    "She doesn't stir."
    "Felix straightens, pulling himself back into focus. He turns back towards the living room to where Qwynn stands waiting near the door."
   
    show Qwynn at half_size with dissolve
   
    fside "Thank you for letting me in."
    "Qwynn shrugs, their arms folded loosely."
    q "You don't have to thank me. You did what I couldn't."
    "Felix steps forward, extending his hand to shake Qwynn's."
    fside "Still. I appreciate it."
    "Qwynn glances at Felix's outstretched hand, their mouth a straight line. They extend their hand… then reach past Felix for the door handle behind him, pulling it open."
  
    hide Qwynn
    show Qwynn_M at half_size 
    with dissolve
    
    q "...Astra really cares about you. That's why she tries so hard."
    q "Once she decides to pursue something, {b}nothing{/b} will get in her way."
    q "If your only plan is to wait around until she decides to give up, then you're in for a rude awakening."
    fsideu "..."

    hide Qwynn_M
    show Qwynn_N3 at half_size 
    with dissolve

    q "You should go. She'll be safe now."
    "Felix blinks, then lets out a quiet, tired chuckle."
    fside "Right. Look after Astra."
    "He steps outside, and the door closes quietly behind him."

    window hide
    show astra_pov with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto


    scene bedroom_evening with squares

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0


    "The pounding in my head has faded to a dull ache. My thoughts clear, bit by bit, as I become lucid once more. Memories resurface; a warm embrace, a feeling of safety, and most of all, a softly made wish."
    f "(Sleep well…)"  

    play sfx "sfx_shake.ogg"

    show bedroom_evening with vpunch

    "I jerk upright, ignoring how my body protests the sudden movement. The scent of acrylic lingers in the air."
    asidesp "Felix?"
    "A dimly lit form rests against my bedframe. Qwynn, head tilted forward, fast asleep while sitting upright. The faint rhythm of their breathing blends with the soft ticking of the clock."
    "When I whisper their name, they jolt awake, eyes wide with disoriented worry."

    show Qwynn_N3 at half_size with dissolve

    q "Aste! You're awake, how do you feel? Do you need anything?" 
    "I rub the sleep from my eyes."
    aside "I feel much better now… I'm sorry for worrying you."

    hide Qwynn_N3
    show Qwynn_A at half_size
    with dissolve

    q "You should be!"
    "Their voice cracks—for a second, I see the exhaustion they've been holding back seeping through. It's rare to hear anger from Qwynn, but the kind that hides care always stings the most."
    q "I told you that you could rely on me! I could've— I would've gone to get Felix myself, if it meant keeping you safe." 
 
    hide Qwynn_A with dissolve

    "They turn their head away, the line of their shoulders tense."
    asidesa "(They've been doing that a lot recently. Avoiding my eyes.)"
    asidesh "Qwynn… I—"

    show Qwynn_M at half_size with dissolve

    q "No. It's okay. Sorry for yelling."
    "They look up again—resigned. To what, I can't quite tell."
    q "Even if you're feeling better, you should still take something."
    "A bundle of herbs, and a glass of water. Qwynn reaches for them, plucking them off the bedside table."
    q "Here."
    aside "Thanks."
    "Qwynn hums in acknowledgement, the sound between relief and fatigue."

    hide Qwynn_M with dissolve

    "I take the herbs, the bitterness catching on my tongue. Warmth spreads through me, slow and steady."
    asidesa "(I wanna ask about Felix, but… is now the time?)"
    "Qwynn must've noticed my expression, because they let out a short, unexpected laugh—the kind that slips out before they can hold it in."
   
    show Qwynn_S at half_size with dissolve
       
    q "Your knight in shining jumpsuit went home, Aste."

    hide Qwynn_S with dissolve

    "I mentally stumble at the mention of him and I look away instinctively, pretending to study the water glass instead."
    asideem "(Of course he left. Why wouldn't he?)"
    asidea "(Still… he could've woken me up.)"
    "When I look up, Qwynn is staring at me, an eyebrow raised."

    show Qwynn_S at half_size with dissolve

    asideb "I wasn't—"
    q "Yes, you were."
    asideeb "Fine, you caught me… Did he say anything?"
    q "After making sure you were safe, no, he didn't say much."
    asidea "(Great… back to square one then.)" 
    q "You should get some more rest. If you need me just call for me. I'll hear it."
    aside "Thanks, Qwynn."

    hide Qwynn_S with dissolve

    "They nod and move toward the door, the faint sound of their steps fading into the quiet. I lie back, staring at the ceiling until the shadows blur."


    window hide
    show black with dissolve
    window auto
    pause (2.0)


    scene bedroom with dissolve

    "The next time I wake up, it's to the sounds of eager birdsong. The sunlight spilling across the room paints everything in soft gold. It must be late morning."
    "Compared to yesterday, I feel much better. Not perfect, but steady enough to breathe without the world spinning."
    aside "(Small victories count too.)"
    "I sit up slowly, pressing a hand against my forehead. The faint dizziness fades after a moment, replaced by a hollow tug in my stomach."
    asideb "(More than anything, I want to talk with Felix. Preferably without passing out this time.)"
    asideeb "(Also… I'm starving.)"
    "I push the blanket aside and make my way toward the kitchen. The faint scent of herbs and something earthy meets me halfway down the hall."

    show kitchen with dissolve
    play audio "<from 0 to 2>dooropenclose.mp3" #open

    "Qwynn is perched by the counter and the image of a diligent sentry guarding their stubborn charge flashes in my mind."
    
    show Qwynn_S at half_size with dissolve
    
    q "Morning. How're you feeling?"
    asidesm "Hungry."
    "That earns me a small, sympathetic smile."

    hide Qwynn_S
    show Qwynn_N3 at half_size 
    with dissolve

    q "You haven't eaten for a full day. I bought you some mushroom soup. One sec, I'll warm it for you."
    "Qwynn rises, the stool sliding back against wooden floors."

    hide Qwynn_N3 with dissolve

    aside "I can do it."

    show Qwynn_S at half_size with dissolve

    q "Too late, I'm already up. Take my seat." 

    hide Qwynn_S with dissolve

    "Before I can argue, Qwynn is in the kitchen preparing a bowl of mushroom soup—the one from my favorite restaurant."
    "I take Qwynn's seat, as instructed. The sound of the spoon clinking against the pot Qwynn is stirring is steady, almost rhythmic. It fills the quiet like a lullaby." 
    "All the while, I can't help but think about how I want to see Felix as soon as I can."
    asidea "(We have a lot to discuss.)"
    "The thought is so distracting I almost miss it when Qwynn sets the bowl of soup in front of me."
    asidesm "(But first—soup.)"

    window hide
    show black with dissolve
    window auto
    pause (2.0)


    scene market with dissolve
    play music "city_day.ogg" fadeout 2.0 fadein 2.0

    "Another full day of rest later, I find myself standing in front of a bright green door. Behind it are the answers I need."

    play audio "<from 0 to 3>bell.mp3"

    #TODO change/add track?

    scene studio with dissolve

    "The bell jingles overhead. This time, Felix looks up immediately, mid conversation with Velvet." 

    show Velvet with dissolve

    v "Speak of the fiend—" 
    "A nervous laugh escapes my lips."

    hide Velvet with dissolve

    asidesm "And she shall appear…"
    asidesp "Surprise!" 

    show Felix_C with dissolve

    f "Astra? What are you doing here?"
    aside "We still have things to discuss. The launch is next week."
    f "You should be resting, you collapsed on me two days ago!" 
    aside "I've rested more than enough. I'm fine."

    hide Felix_C
    show Felix_N2
    with dissolve

    f "...For some reason I don't believe you." 

    hide Felix_N2
    show Felix_S
    with dissolve

    "Felix's eyes roam over me, perhaps searching for proof that I'm telling the truth."

    hide Felix_S
    show Felix_N2
    with dissolve


    f "You don't even have your notes." 
    asidesp "Of course I do, they're right—"

    hide Felix_N2 with dissolve

    "I reach into my bag, poking around blindly. My fingers brush fabric, a wallet, a pen… no notebook."
    asidesh "…Okay, maybe not right now."

    show Felix_N2 with dissolve

    f "You never forget your notes… You haven't fully recovered." 
    "Velvet's eyes flicker back and forth between Felix and I." 
 
    hide Felix_N2
    show Felix_N2 at Transform (xpos=250) 
    with ease
    show Velvet at Transform (xpos=950) with dissolve
   
    v "Oh man, I just remembered I have errands to run. You two have fun, yeah?" 

    hide Felix_N2
    show Felix_Sad at Transform (xpos=250)
    with dissolve

    f "Vel—"
    v "Suuuper busy, Fe. Gotta go. See you later Astra!" 
    "As they pass Felix, Velvet leans into his space. They mutter something that causes Felix's brows to furrow." 

    hide Velvet with easeoutright
    hide Felix_Sad
    show Felix_Sad at truecenter 
    with ease

    "Felix looks away, hand tugging at his locs. Velvet backs away, stepping over art supplies as he heads for the door." 

    hide Felix_Sad
    show Felix_N2
    with dissolve

    f "Be—"
    v "Careful. Always am. Bye now!" 

    play audio "<from 0 to 3>bell.mp3"

    "The door shuts, and Velvet is gone. Felix sighs and turns to face me. He grins, but it's forced. Tense. A wall deterring me from the truth."
   
    show Felix with dissolve
   
    f "Tea?"
    "I play along. For now."
    asidesm "No coffee?" 
    f "I'm starting to think you have a problem."
    asidesm "How else can I get all my work done?"

    hide Felix
    show Felix_S
    with dissolve

    "I say it in jest, but Felix doesn't look impressed."
    asidesh "...Tea sounds great." 

    hide Felix_S
    show Felix_N2
    with dissolve

    f "...Wait for me in the lounge?"
    aside "Okay."

    hide Felix_N2 with easeoutright

    "The large windows of the studio let in embers of fading warmth. Pink and orange hues paint the studio in pleasant hues."
    "Qwynn made me wait until the afternoon before leaving. Just to make sure I was feeling better."
    "The air feels heavier with the scent of clay and paint thinner. It's familiar, grounding. I breathe it in, steadying myself."
    "Despite everything that's happened, being in Felix's studio still soothes me."
    "Just as I feel myself drifting off, the soft clinking of mugs brings me back to reality."

    show Felix_C with dissolve

    f "You sure you're okay?"
    aside "Positive." 

    hide Felix_C
    show Felix_N2
    with dissolve

    f "You were about to fall asleep."
    "I shrug."
    aside "I've been doing nothing but sleep for the past two days."
    "His fingers play along the rim of his mug."

    hide Felix_C
    show Felix_Sad
    with dissolve

    f "Maybe you need a third."
    asidea "It's fine."

    hide Felix_Sad
    show Felix_U
    with dissolve

    "He looks at me seriously, without a trace of his usual playfulness."

    hide Felix_U
    show Felix_C 
    with dissolve

    f "...No, Astra. It's not."
    f "You seriously scared me."
    aside "Look, if this is about the other day, I've already promised to be more careful."
    f "It's not that. I mean—it's partially that. But, no."

    hide Felix_C
    show Felix_N2
    with dissolve

    f "...You love what you do. And you're really good at it… your passion, it's infectious."
    "He cuts himself off with a self-deprecating laugh."
    f "But— That kind of passion… it's dangerous.."
    f "You said it yourself. 'Life is risky'.{w} If that's the case, then why tempt it?"

    hide Felix_N2 with dissolve

    "I pretend to mull over his words, but the answer is simple—and comes to me easily."

    show Felix_N2 with dissolve

    asidesp "Why not?"
    asidesm "Why should I sit around letting life happen to me, when I can influence it myself?"
    f "Influencing it is exactly what I'm afraid of. How do you know it won't turn out horribly?"
    aside "I don't."

    hide Felix_N2
    show Felix_C
    with dissolve

    f "Doesn't that terrify you?"
    aside "Sometimes. But, Felix. I'm much happier when I try and fail, than when I don't try at all."
    asidesp "Sure, I love when things go well, and I always do my best in order to make that happen. But, if things don't work out… well then it's time to try something else."
    "Felix shakes his head."
    f "I— I don't know if I agree."
    "I look him over—he sits with elbows propped up on his knees, leaning forward in contemplation. He tugs at his locs again, the way I notice he does when he's nervous."
    asidesa "(Something else is bothering him.)"
    "For a moment, the silence stretches thin. Our mouths open at the same time."

    hide Felix_C
    show Felix_N2
    with dissolve

    asidesp "Felix."
    f "Astra."
    aside "Sorry. You first."
    f "About the other day. I'm sorry."
    f "I should've given you a proper explanation. Instead, I ran away."

    hide Felix_N2
    show Felix_Sad
    with dissolve

    "His gaze drops before locking onto mine again. Conflict rages war in his features before he finally exhales, appearing to make a decision."
   
    hide Felix_Sad
    show Felix_N2
    with dissolve

    play music "Felix.ogg" fadeout 2.0 fadein 2.0
   
    f "Can I tell you something?"
    aside "Always."
    "He nods."

    hide Felix_N2
    show Felix_C
    with dissolve

    f "...I lost someone really close to me. Seven years ago."

    hide Felix_C with dissolve

    "It's subtle, but he glances over to a corner of the studio… and I realize the painting I saw last time hasn't moved."
    asidesa "(So it's not a commission.)"
    "He catches where my eyes have drifted to, and he smiles sadly."
   
    show Felix_C
    with dissolve
   
   
    f "She was shy, but she always went out of her way to ask me about my paintings. Almost everyday, she would show up at my house holding a bundle of flowers—asking me to paint them for her."
    f "And I always said yes."
    f "...We made big plans… Moving to Halis, me opening an art studio, her opening a flower shop. I thought we would be more successful in the city. I wanted to paint things that we couldn't find in our village—"
    "He clears his throat, and it looks like he's trying to gather himself."

    hide Felix_C with dissolve

    menu:
        "Move closer.":
            $ felix_pts += 20 
            show screen choice_indicator(FELIX_COLOR)
            "Felix watches me approach. There's space on the couch next to him, and I take it carefully."
            "His breath catches. Mine does too." 

        "Wait for him to say something.":
            "I choose to stay quiet. Unsure of how to comfort him."
            "And clearly, Felix doesn't know either, because he stays silent for a long while. Unmoving."
            "Eventually, he continues."


    show Felix_N2 with dissolve

    f "When we turned 18, we set off for Halis. Joined a small caravan of merchants headed to the city. But—"

    hide Felix_N2
    show Felix_U
    with dissolve

    "He grimaces."

    hide Felix_U
    show Felix_Sad
    with dissolve

    f "One of the merchants had smuggled a fire wisp on board."
    "I inhale sharply."

    hide Felix_Sad with dissolve

    "While not intentionally harmful, wisps of all elements are wild by nature. It's illegal to keep them as pets or remove them from their natural habitats. It's a well known fact that they aren't easily contained." 
    "Small, but extremely volatile."

    show Felix_Sad
    with dissolve

    f "It got loose. Obviously. Anyone could predict that."
    "I catch a flash of anger rarely seen from him."
    f "...Sophie—she realized what was happening before I did, and she pushed me out of the cart just before it went up in flames."
   
    hide Felix_Sad
    show Felix_C
    with dissolve
   
    "He looks up, eyes glistening with unshed tears." 
    f "{b}That's{/b} where my passion led me."

    hide Felix_C with dissolve

    "He laughs darkly. There's no humor in it."

    show Felix_Sad 
    with dissolve

    f "I stopped having dreams after that."
    asidesa "Felix—"

    hide Felix_Sad
    show Felix_N2
    with dissolve

    f "I love your company, Astra. You're bright and determined. I've never met anyone like you."

    hide Felix_N2
    show Felix 
    with dissolve

    f "When I'm with you, I feel like I can dream again."
    "He pauses."

    hide Felix
    show Felix_N2
    with dissolve

    f "...That's what terrifies me. That's the real reason why I rejected you."
    f "Because I can't shake the fear that as soon as I let myself be happy again—it'll be ripped away from me."
    "I watch him as I search for the right words to say. He looks so worn down, and for the first time I wonder if he's been having trouble sleeping too."
    asidesp "Felix, I—"
    "He shakes his head." 
    f "I'm sorry, Astra. And— Thank you. For everything."
    "But before I can say anything more,  he rises suddenly, taking staggering steps towards the door."

    hide Felix_N2 with dissolve

    f "It's getting late. You should be taking it easy, not—sitting here dealing with—"
    "He gestures to himself with a hand. A loose, sweeping movement."

    show Felix_N2 with dissolve

    f "With me."
    "He tries for a smile, but it falters halfway. A goodbye."
    f "Go get some rest, yeah?"
    asidea "You're kicking me out."
    "It's a statement. Not a question."
    asidesa "(My heart is pounding.)"
    "Felix shakes his head 'no', but the way he stands guarded by the door says otherwise."
    asidesh "...Okay. Then, I guess I'll go home."

    hide Felix_N2 with dissolve

    "My voice cracks, sounding much smaller than I'd like it to."
    "It's hard to say what emotion I'm feeling. It's sharp, like anger. It's suffocating, like sadness. It's so many things at once, and I can't tell which one is winning."
    asidesh "...See you at the launch?"

    show Felix_N2 with dissolve

    f "I'll be around for a bit longer. I still have to paint the mural. As promised."
    "I stand at the precipice just outside Studio Alizeti for what seems like the very last time."
    aside "And after that?"

    hide Felix_N2
    show Felix_C 
    with dissolve

    f "...Be safe out there."

    hide Felix_C with dissolve

    "The door shuts. The sound feels final."
    "I stay still, the echo of the latch ringing louder than it should. Then, finally, I allow the tears that I've been holding back to flow. Hot streaks trace down my face. My steps are unsteady all the way home."
    
    scene kitchen:
        blur 20
    with dissolve

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0

    "When I reach my apartment, my vision blurs completely. The grief doesn't explode; it seeps, coming in shuddering breaths."
    "More than anything else he'd said, the knowledge that Felix was afraid to chase happiness hurt the most."
    asidesa "(For all the joy he's given to me, he won't accept any of it back...)"

    window hide
    show black with dissolve
    window auto
    pause (2.0)
   
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadein 2.0
    scene cafe_interior with dissolve


    "Things are hectic at Cafè Bloom. The usual calm interrupted by countless deliveries and the sounds of drilling."
    "Sylphia and Albion help where they can, but as the one who's been coordinating everything, they often have to defer back to me anyways."
    "Next to me, Albion lets out a frustrated breath."

    show Albion_SC with dissolve

    al "This is too much."
    aside2 "It's not even done yet, at least wait until we finish to start complaining."
    "He crosses his arms."
    al "I liked how the cafè was before."
    aside2 "So did I, but now we'll be able to share it with more people."
    al "...Great."

    hide Albion_SC with dissolve

    play audio "<from 0 to 3>bell.mp3"

    "A dwarf and a dryad walk in, each carrying one side of one of our new custom tables. The pair spot me, and call out."
    dwa "Where do you want these, Miss Vale?"

    show Albion_SC with dissolve

    "Albion shakes his head, walking towards the break room without a word."

    hide Albion_SC with dissolve

    asidesp2 "Right there is fine for now. I'll bring you the new floorplan in a moment."
   
    play audio "<from 0 to 3>bell.mp3"
 
    "The bell rings again. This time Mr. Ellwood walks in."
    e "Good morning Miss Astra."
    aside2 "Morning, Mr Ellwood."
    e "I must admit, I wasn't sure you'd be able to pull it off, but everything is looking wonderful!"
    "Pride fills my heart at his words."
    asidee2 "Thank you! Will I be seeing you at the launch party?"
    e "Absolutely. I'll be there."

    play audio "<from 0 to 3>bell.mp3"

    "I smile, and open my mouth to call out to him before he turns away when the door opens yet again."
    "Seeing who it is causes my breath to catch."
    "Felix walks in, carrying a few small buckets of paint."
    "Surprisingly, Velvet trails behind him carrying even more buckets."

    show Felix_N2 with dissolve

    f "Hey."
    asidea2 "Hi."
    "Felix nods his head towards the empty wall where the mural is going to be."

    hide Felix_N2
    show Felix
    with dissolve

    f "You won't even notice I'm here."
    "He winks."
    f "Quiet as a mouse."
    "I feel my lips purse."
    asidesp2 "That's—"

    hide Felix with dissolve

    asidea2 "(Aaannd he's gone.)"
    asidesa2 "(Great.)"
    "I stare after Felix—weighing my options—when Velvet speaks up."

    show Velvet with dissolve

    v "I know it's not ideal, but he's working through things in his own way."
    v "Enough about Felix, though. How much do you have left to do before the launch?"
    "I sigh, breaking my gaze away from where Felix has started to work to make eye contact with Vel."
    aside2 "It's going really well actually. With the delivery of the tables, and the mural in progress, the only things left is coordinating the last few deliveries. Decorations, new tablecloths, and dishware..."
    v "That sounds like a lot."
    asidesp2 "It's not! Trust me, compared to all those meetings, this is much more manageable."
    "Vel laughs."
    v "I'll take your word for it."
    "Whatever Vel might say next is interrupted by a call from the front of the cafè."

    hide Velvet with dissolve

    f "Vel? You're holding my paint hostage."

    show Velvet with dissolve

    v "Oh. Right—"
    v "Sorry, Astra. I'll see you around, yeah?"
    asidesp2 "Yeah. See you!"

    hide Velvet with dissolve

    aside2 "(...There's no time to waste.)"
    "I told Felix myself. It's better to try and fail than to not try at all."
    aside2 "(I tried... and now, I wait to see what comes of it.)"
    "Dryad" "Miss Vale? Do you have a moment?"
    asidesp2 "I'll be right there."
    asidesh2 "(...I wonder how it will turn out.)"
    stop ambient fadeout 2.0

label felix_ending:
    if (felix_pts >= 70):
        jump felix_good
    else:
        jump felix_bad