# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#########################################
# CAELAN CHAPTER 1 
#########################################

label Caelan_chp1:
  
    window hide
    show caelan_chp1 with squares
    window auto
    pause (2.0)

    $ persistent.status_button = True
    
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadein 2.0
    scene cafe_interior_dawn with squares

    "After Sylphia accepted my proposal, she tasked me with defining some of the more intricate details of the project."
    "And what better place to make a game plan than the café itself? With Albion and Sylphia taking care of things at the bar I can spend my time brainstorming."
    "I'm hunched over my notebook at my favorite table—one of the ones that line the large glass windows. I tap my pen lightly on my lips, rhythmic and absentminded."
    "Ideas float in and out of my mind, but nothing sticks. Words start to blur together into meaningless shapes."

    play audio "<from 0 to 3>bell.mp3"

    "The bell rings. The mysterious cloaked stranger from the previous week wanders in as Sylphia's voice calls out."
   
    show Sylphia with dissolve
   
    s "Welcome in!"

    hide Sylphia with  dissolve

    "Their trajectory changes the second they spot me."
    "They carry themselves with a sense of uncertainty. A downturned head, a hand clutched to the sleeve of their cloak, and eyes that haven't settled on any one thing since they entered."
    "Even once they reach me, they hesitate."
    
    show Caelan2 with dissolve

    asidesp2 "Good morning! Here for your 'offering'?"
    who "...Yes, however, you appear busy."

    hide Caelan2
    show Caelan_ST2
    with dissolve

    "Their gaze flits up to meet mine. In contrast to their body language, at least their voice seems sure of itself."
    who "I can come back some other time."
    asidesp2 "No, it's okay! Give me a moment and I'll prepare it for you."
    
    hide Caelan_ST2 with dissolve

    "Pushing myself up from my seat, I head behind the bar to start on their order. When I pass by, the corner of Sylphia's mouth twitches."
    
    show Sylphia with dissolve

    s "Ah, do we have a new regular?"
    aside2 "Looks that way. I'll have to write down the recipe in case they come by when I'm not here."
    
    show Sylphia at Transform (xpos=600) with ease
    show Albion_SC at right with dissolve

    al "...Something about them feels off."
    "Albion says it quietly, but we all hear it."
    s "Always so suspicious Albion. You don't even know them."
    al "I didn't say it was a bad feeling. Just—not {i}good{/i} either."
    "My gaze slides over to where the new regular stands. If they heard what Albion said, they show no sign of it."
    aside2 "I don't know, they seem nice."
    al "Mm."

    play audio "<from 0 to 3>bell.mp3"

    s "I'll take care of it."

    hide Sylphia with dissolve
    hide Albion_SC with easeoutright

    "Albion glides away too, leaving me to begin working on the order."
    "Making the drink is like second-nature."
    "While it steeps, I snag a sheet of paper from the break room to jot down the ingredients and measurements used to make it."
    aside2 "(There. Now they can come anytime.)"
    "It's warm in my hands as I carry it over to the customer. It smells nostalgic. I'm almost tempted to take a sip for myself."
    "They haven't taken a seat; instead they hover right where I left them."
    aside2 "Here you go."
    
    show Caelan2 with dissolve

    who "Thank you."
    "Our fingers brush as I hand over the drink."
    "The contact sends goosebumps up my arms. Their skin is startlingly cold, like they've stuck their hands into snow."
    "I move to settle back into my previous seat. The stranger doesn't move in either direction."
    aside2 "You can take a seat— If you like."

    hide Caelan2
    show Caelan_ST2
    with dissolve

    who "Oh. Okay—"
    "The chair across from mine is pulled out."

    hide Caelan_ST2
    show Caelan2:
        zoom 1.5
        xoffset 400 
        yoffset -100
    with dissolve

    asidesh2 "(Oh. I meant they could take a seat at another table.)"
    asidesh2 "(Well, it's not the first time I've sat with a customer.)"
    aside2 "By the way, you know my name but— I don't know yours."

    hide Caelan2
    show Caelan_B2:
        zoom 1.5
        xoffset 400 
        yoffset -100
    with dissolve

    who " Ah—"
    c "You may call me… Cal."
    aside2 "In that case, it's nice to meet you Cal."
    aside2 "...So, are you from here? From Halis?"

    hide Caelan_B2
    show Caelan_ST2:
        zoom 1.5
        xoffset 400 
        yoffset -100
    with dissolve

    c "Yes. I have lived here all of my life."
    asidesp2 "Really? I thought you might be from somewhere else in Feldoria."

    hide Caelan_ST2
    show Caelan_H2:
        zoom 1.5
        xoffset 400 
        yoffset -100
    with dissolve

    "They suddenly appear self-conscious. One of their hands reaches to tug their hood down further."
    c "Oh… Is it the way I speak? Or my state of dress?" 
    c "I am not trying to stand out."

    hide Caelan_B2 with dissolve

#CHOICE #1
    menu: 

        "Be honest.":
            $ caelan_pts += 20
            show screen choice_indicator(CAELAN_COLOR) 
            asidesh2 "Honestly, maybe a bit of both? Lots of travelers wear cloaks—that paired with your speech pattern—I just thought maybe you were from outside the city."
            show Caelan_H2:
                zoom 1.5
                xoffset 400 
                yoffset -100
            with dissolve    
            c "I see."
            asidesp2 "It's not a bad thing! In fact, I'm happy to hear that you're from around here."

        "Lie":
            asidesa2 "(I don't want to hurt their feelings.)"
            asidesh2 "Ah— No, we just get a lot of tourists."
            "I bite my lip at the lie. We do get a lot of tourists, but that isn't what made me question their origins."
            "Hopefully they don't notice."
            show Caelan_ST2:
                zoom 1.5
                xoffset 400 
                yoffset -100
            with dissolve
            c "I suppose Halis does get many tourists."
            hide Caelan_ST2 with dissolve
            aside2 "(Saved!)"
            asidesp2 "Exactly, but I'm glad—"

#BRANCHES CONVERGE HERE

    asidesp2 "It means you'll come around more often!"
    hide Caelan_H2
    show Caelan_B2:
        zoom 1.5
        xoffset 400 
        yoffset -100
    with dissolve
    "Cal's face turns red, enough that it's visible through the shadows of their hood."
    asidesp2 "Ah, only if you want to. I wrote down the recipe for your drink. So even if I'm not here, you can still order your usual."
    
    hide Caelan_B2
    show Caelan_ST2:
        zoom 1.5
        xoffset 400 
        yoffset -100
    with dissolve
    
    c "…You would go so far for a stranger?"
    asidesm2 "Are we still strangers? I think we could at least be considered acquaintances, don't you think?"

    hide Caelan_ST2
    show Caelan_EM2:
        zoom 1.5
        xoffset 400 
        yoffset -100
    with dissolve    

    "They crack a small smile, and for some reason, it feels like I've won a prize."  
    c "Acquaintances… I accept your proposal."
    asidesp2 "(Proposal?)"
    "I laugh internally. That makes it sound much more serious than I intended."
    asidee2 "Great!" 
    "I flash them a grin."
    aside2 "(As always, interacting with our customers is my favorite part of this job. It hardly feels like work.)"
    
    hide Caelan_EM2
    show Caelan2:
        zoom 1.5
        xoffset 400 
        yoffset -100
    with dissolve
            
    c "I should go soon. I have kept you for long enough."
    c "Your company was appreciated, Astra."
    asidesp2 "Oh, sure! Come again soon!"

    hide Caelan2
    show Caelan_SA2:
        zoom 1.5
        xoffset 400 
        yoffset -100
    with dissolve

    "Their eyes suddenly lock with mine, their dark eyes like pools of deep water. My heart pounds… and I can't look away."
    "After a few moments, they nod. What they confirmed I have no clue, but it must be positive because Cal speaks up again." 
  
    hide Caelan_SA2
    show Caelan_S2:
        zoom 1.5
        xoffset 400 
        yoffset -100
    with dissolve  
  
    c "Yes, I will return."
    asideem2 "(Why do I feel like I just passed a test? …And why am I so happy about it?)"
    asidesp2 "Okay!"

    stop ambient fadeout 3.0

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "city_day.ogg" fadeout 2.0 fadein 2.0
    scene market with dissolve

    "With my course decided, all that's left to do is to put it in action."
    aside "(First, to Studio Alizeti.)"

    show felixcard with dissolve

    "I stare down at the card in my hands and then back at the door in front of me."
    aside "(This is it.)"

    hide felixcard 
    scene studio 
    with dissolve

    play audio "<from 0 to 3>bell.mp3"

    "The door pushes in easily and a bell rings to mark my entry."
    aside "(Oh good, he's here.)"
    "A man stands in front of a large canvas with a furrow in his brow, but his face brightens in recognition when I step fully into the studio."

    show fcutin2 with easeinleft

    f "Oh hey, Astra!"

    hide fcutin2 with easeoutright
    show Felix with dissolve

    asidesp "Hi Felix!"
    f "What brings you here?"
    asidee "A commission. If you accept, of course."
    f "Oh? Sounds interesting. Go ahead and take a seat. I'll grab my notebook."

    hide Felix with dissolve

    "He points to a grouping of couches that are bas in sunlight. I take him up on the offer, lowering myself onto one of the plush seats."

    show Felix_N2 with dissolve

    "Felix joins me soon after, now equipped with a pen and notebook."
    f "Alright, so, what can I do for you?"
    asidesp "Well, I went with your suggestion to make my own plan. …Which involves asking you to paint a mural for the café."
    
    hide Felix_N2
    show Felix
    with dissolve
    
    f "Your boss approved? That's amazing!"
    asidee "Right? You really helped me out."
    f "I just leant an ear. Anyways, I'd love to help out. You have the measurements?"
    aside "Yeah, I wrote it all down here."
    
    hide Felix with dissolve

    play music "city_night.ogg" fadeout 2.0 fadein 2.0
    show studio_evening with dissolve

    "By the time we've finished hashing out all the details, it's time for me to head to my next stop for the day."
    "Felix walks me to the door. He leans casually against the open frame until I pass through safely." 
    
    show Felix with dissolve
    
    f "I'll bring you the sketches before the end of next week."
    asidee "That's perfect. Thanks again Felix!"
    f "No problem. Stay safe out there!"
    aside "Will do!"

    scene market_evening with dissolve

    asidesm "(Alright, one down. Two to go.)"

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0
    scene kitchen_evening with dissolve

    "Warmth surrounds me the second I step into my apartment. All of the lanterns are lit, casting everything in a comforting orange glow."
    "To top it all off, the delightful smell of something herbal reaches my nose."
    aside "(Qwynn must be making dinner.)"
    "I call out to them even though I'm sure they heard me come in."
    asidesp "I'm back!"
    "Qwynn peaks their head into the living room with a dazzling grin."

    show Qwynn_S at half_size with easeinleft

    q "Welcome home! Dinner's almost done."

    hide Qwynn_S at half_size with easeoutleft

    "As fast as I can manage, I drop my things by the door and slip off my shoes to follow Qwynn back into the kitchen."
    aside "(I'm starving.)"
    asidee "What is it? Smells delicious."

    show Qwynn_S at half_size with dissolve

    q "Nothing special. Just roasted chicken and vegetables."
    asidesp "Really? I wouldn't have guessed."
    q "Hehe, praise me more why don't you! Maybe I should close the boutique and open a restaurant?"
    asidep "No, that would be too sad. You worked so hard for your shop after all."
    q "I know, I know, just kidding~" 
    q "Have a seat, it's ready now." 
    aside "Thanks."

    hide Qwynn_S with dissolve

    "A dish slides in front of me, steam still curling off of it."
    "Shortly after, Qwynn slips into the stool next to mine."
    aside "Hey, Qwynn. Question."

    show Qwynn_N3 at half_size with dissolve

    q "Answer."
    asidesp "You did all the marketing for Voyage Étoilé yourself. Would you mind sharing some of that expertise for Bloom?"
  
    hide Qwynn_N3 
    show Qwynn_S at half_size
    with dissolve
  
    q "Of course! Anything for you."
    asideeb "Hehe, great!"
    aside "Then, after dinner, can I pick your brain?"
    q "Absolutely. I'll tell you anything and everything you need to know to push Bloom into the spotlight!"
    
    hide Qwynn_S with dissolve

    "With Qwynn's help secured I ready myself for a night of note taking, because Qwynn is nothing if not detailed."

    window hide
    show black with dissolve
    window auto
    pause (2.0)
    
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg" fadein 2.0
    scene cafe_interior with dissolve

    "Lunch time is busy at Café Bloom, especially on weekends. In between making drinks and chatting with customers, my mind runs through the list of things I still need to accomplish."
    "The first of which requires talking with Albion."
    "Having his help to develop a signature drink would save me a lot of trouble."
    "The problem is getting him to agree…"
    aside2 "Albion?"
    "He doesn't turn to face me, but that's normal."

    show Albion with dissolve

    al "What?"
    asidesp2 "After the rush, I need to talk to you."
    "I see his shoulders drop."

    hide Albion
    show Albion_SC
    with dissolve

    al "…Can't wait."

    hide Albion_SC with dissolve

    asidesh2 "(He probably knows what I want.)"
    "I do feel a little bad about pushing him when he doesn't want to participate… but it's part of his job."
    asidesh2 "(Hopefully he won't be too mad.)"
    "After the rush, Albion meets me behind the counter with his arms crossed."
   
    show Albion_SC with dissolve

    al "Is this about your new plan? Sylphia told me about it."
    asidesp2 "Yes, look, I know you don't want—"
    al "I'll help."
    asidesp2 "…What?"
    al "I'll. Help."
    asidee2 "Really?!"
    al "Yes. Sylphia's not stupid, if she trusts you then…"
    "He shrugs."
    asidee2 "Perfect! Thank you Albion. You won't regret it."
    asidee2 "(Thank you Sylphia!)"
   
    hide Albion_SC
    show Albion 
    with dissolve
   
    al "Whatever. Let's just get this over with, what do you need?"
    "A small smirk takes over."
    asidesm2 "(Oh Albion, never change.)"
    aside2 "We need a signature drink. Since we're being more intentional about our image, I thought we should have a specialty coffee to match. One you can only get here."
    "Albion's expression doesn't change, but at the very least, he looks to be considering what I said."
    al "…I can do that. Making coffee blends is easy enough."
    asidesp2 "Amazing! Thanks."
    al "Mmm. Sure."
    al "I'm gonna take my break now."

    hide Albion with dissolve

    "It's a weight off of my shoulders to have Albion's help. I feel light as a feather."
    asidesp2 "Okay! Have fun~"

    stop ambient fadeout 3.0
  
    window hide
    show black with dissolve
    window auto
    pause (2.0)
    
    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0
    show cafe_interior_evening:
        zoom 2.0
        xoffset 0
        yoffset -500
    
    with dissolve

    "Felix, Qwynn, and Albion…"
    "Today the break room is my office. It's a quiet evening that I'm using to plan out my next steps."
    "Felix is coming next week to start the mural… Qwynn's helping me make flyers and improve our image… and Albion said he'd have a blend complete by the start of summer."
    "It's almost concerning how easily things are falling into place."
    "I let my head tip into my hand, propping it up as I study my notes."
    asidesh2 "(I never imagined myself doing something like this—having so much responsibility.)"
    asidesm2 "(But I think I like it.)"

    play audio "knock.mp3" fadeout 2.0

    show Sylphia:
        zoom 1.5
        xoffset 460 
        yoffset -150
    with dissolve

    play audio "dooropenclose.mp3" #open and close
    
    "The door opens to reveal Sylphia smiling softly on the other side. She steps in, shutting the door behind her. It closes with a soft click."
    s "I've just finished closing for the night."
    asidesp2 "Already? Sorry Sylphia, I lost track of time."
    s "No need to apologize, what you're doing is just as important."
    s "I wanted to talk to you about something. Do you have a few moments?"
    "I look up, a little worried."
    aside2 "I have time, how can I help?"
    "She smiles kindly."
    s "How would you feel about becoming Bloom's manager?"
    "..."
    asidesp2 "(Huh?)"
    asidesp2 "W-what do you mean? {i}You're{/i} the manager."
    s "I am. But I won't be the manager forever. I've been thinking about it—about what this place needs—and about what I need."
    s "Before you are a leader, success is about relying on yourself. When you become a leader, success is all about relying on others when needed."
    "Sylphia's gaze meets mine."
    s "If I must confess, I started this place on a whim."
    s "Café Bloom is dear to me, of course, but in the beginning it was less so about passion and more so about opportunity."
    s "I did it simply because I could."
    "Frankly, I'm still reeling from what Sylphia asked. But I do my best to focus my full attention on the elf before me. What she's about to say… feels important."
    s "Of course, that was over a hundred years ago now."
    "Sylpha's eyes open. Not for the first time, I'm struck by how many multitudes she must contain after having lived so many years."
    "It's something I won't ever fully understand in my short, human lifespan."
    s "It's only after I brought in you and Albion that I truly started to appreciate this place. It's so much warmer here with the two of you working alongside me."
    aside2 "Sylphia… I—"
    s "You've taken on so much responsibility since starting here and shown me how even just a little passion can light the brightest flames."
    "Her eyes bore holes into mine. It's her serious look. It's one of sincerity, usually hidden under layers of mischief."
    s "Café Bloom could use a little human touch. A little human heart."
    "Sylphia's earnest confession threatens to bring tears to my eyes, but—"
    asidesp2 "You're serious… me? The manager?"
    s "It wouldn't be right away." 
    s "Should you agree, then I'll start mentoring you. I'm also not planning to suddenly disappear. I don't plan on leaving you or Albion for some time yet, so you don't need to be concerned about that either."
    "Right. There's also Albion. How is he gonna feel about this?"
    asidesp2 "Why me? Why not Albion? He has more experience."
    s "I considered it. Albion is very organized and extremely practical. He could run this place well."
    s "But you, you're more in tune with what our customers want. It's your people skills that many of our regulars come looking for."
    s "I plan to mentor Albion as well. He can help with the more technical aspects of running a business. But being the manager? Albion won't go for that."
    "I tried to imagine Albion in Sylphia's place. Meeting with the business council, fielding customer complaints…"
    "A laugh escapes me."
    asidesm2 "You're right. He would absolutely hate it."
    s "But you, Astra? You have the right disposition for it. Your initiative on the development plan is more than enough proof."
    "Becoming the manager is a big step. It's not a temporary role like what I'm doing now."
    "I should consider her offer carefully."
    
    hide Sylphia with dissolve

#CHOICE #2

    menu:
        "Can I have some time to think about it?":
            $ caelan_pts += 20
            show screen choice_indicator(CAELAN_COLOR) 
            show Sylphia:
                zoom 1.5
                xoffset 460 
                yoffset -150
            with dissolve
            s "Of course! It's a lot to spring on you, take all the time you need."
            s "Like I said, I'm not going anywhere anytime soon."
            "Either way, I have faith in yourself Astra."
            aside2 "Good. Café Bloom needs you too, you know?"
            s "Well aren't you sweet~"

        "I don't know…":          
            show Sylphia:
                zoom 1.5
                xoffset 460 
                yoffset -150
            with dissolve
            s "Have a bit more faith in yourself Astra."
            asidesa2 "(Easy for her to say. This is a big deal for me!)"
            s "You don't have to decide right away, why don't you take some time to think about it?"
            "I breathe a sigh of relief."
            aside2 "Okay!"
    

    s "Now, it's getting late. Let's get out of here before it gets too dark."
    aside2 "Good idea."

    hide Sylphia with dissolve

    jump Caelan_chp2

#########################################
# END
#########################################









