# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


init:
    image blackspots:
        "blackspots1.png"
        1.0
        "blackspots2.png"
        1.0
        "blackspots3.png"
        1.0
        repeat

#########################################
# FELIX CHAPTER 2
#########################################


label Felix_chp2: 

    $ persistent.status_button = True

    window hide
    show felix_chp2 with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    scene kitchen with squares
    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0

    aside "(I have another meeting with Felix today.)"
    "For the first time in days, it feels like I can breathe."
    asidesh "(I love this project, but overseeing so many different things at once is more difficult than expected.)"
    "Luckily, my shift at Café Bloom doesn't begin until after lunch."
  
    stop music fadeout 3.0
   
    asidee "(Which means I have time to stop for coffee before I have to go to Felix's studio.)"
  
    show cafe_interior_dawn with dissolve
   
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg"

    aside "Hey Albion, do you remember that meeting I had here the other day?"

    show Albion_N2 with dissolve

    al "You've been having a lot of meetings recently."
    asidesp "The first one! With Felix."
    al "Who?"
    asidesh "You made him a drink, something off the menu. Super sweet, definitely not coffee."
    al "Ugh, that abomination?"
    asidesm "That's the one. Think you could do it again?"
    "Albion makes a face. A small grimace, like he just bit into a lemon."

    hide Albion_N2 
    show Albion_SC
    with dissolve

    asidesh "(Trust me, Albion. I feel the same way. But, I want to do something nice for him… for being so dedicated to this project.)"
    "I cross my fingers in hopes that Albion will agree."
    al "He likes sugar, not coffee. But… fine."
    asidee "Thanks! You're the best. Also, a cortado for me. The usual."
    aside "Please."

    hide Albion_SC with dissolve

    "As is typical for Albion, I get no verbal response, only action. The bubbling of brewing coffee and the sounds of metal fill the void."
    "While I wait, I sit at a table to look at my notes one last time before the meeting. Then, when Albion finishes the order, he sets it in front of me without so much as a glance."
   
    show Albion_N2 with dissolve 
   
    al "Done."
    aside "Thanks, will you be here later?"
    al "After lunch? No, Sylphia's coming in."
    asidesp "Ah okay, then I'll see you next time!"

    hide Albion_N2 with dissolve 

    "Albion nods."  
    "With coffee in hand, I begin to second guess myself. It's just coffee—nothing more. Right?"   
    asidesh "(I hope it's not too much.)"

    stop ambient fadeout 3.0

    scene studio with dissolve
    play music "Felix.ogg" fadeout 2.0 fadein 2.0
    play audio "<from 0 to 3>bell.mp3"

    "The sign to Studio Alizeti is flipped to 'open'. I step inside, one hand carefully holding two drinks in a tray, which, unfortunately, are no longer hot." 
    "Within the studio, a large canvas dominates the room. Felix sits on a stool before it, brush in hand, concentrating intensely."
    "From where I stand, I can see splashes of color and vague shapes that don't quite form anything yet—a half-formed thought waiting to bloom."

    asidesp "Felix?"
    f "Oh Astra! Good morning!"
    aside "Morning! I come bearing gifts."
    f "For me?"
    asidesp "For you!"
    "I set both drinks on the nearby table. Behind me, I hear the clatter of Felix's brushes, then the quick shuffle of footsteps."
    "As I turn, he's already reaching for the cup. At the same moment, I move to hand it to him—and our hands collide." 
    "A smear of bright pink paint streaks across the back of my hand. The contact is brief, but it's enough to send a spark up my arm."

    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    play sfx "sfx_heartbeat.ogg"

    f "Ah— Sorry—"
    asideeb "N-no, it's alright."
    "I pull my hand back, staring at the paint like it's something alive. It's still wet, glossy in the light. My heartbeat's louder than it should be." 

    hide Felix
    show Felix_E:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve


    f "Oh, Saints— did I do that? I'm so used to getting paint everywhere, I didn't even— here, hold on a sec."

    hide Felix_E with dissolve

    "He turns away, moving towards the small sink in the back. I hear the faucet run, water rushing over something... maybe a cloth." 

    show Felix_B:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "I'll wipe it off for you."
    "Felix's hand reaches for mine. Softly, he hooks his fingers under mine—pulling it towards him to wipe the paint away."
    "His movements are practiced… gentle in their own way." 

    hide Felix_B with dissolve

    asideem "(His hands are rougher than I expected. Calluses have formed where he holds his brushes.)"
    "Before I can even process what's happening—"

    show Felix
    with dissolve

    asidep "(Oh… He's done.)"
    f "There, all better! Sorry about that."
    asideeb "Thanks."

    hide Felix with dissolve

    "I glance down at my hand. My hand is now paint-free, but I still feel marked somehow."
    "There's a faint warmth clinging to where his fingers touched, like my skin hasn't realized the moment's passed yet."
    "Felix on the other hand, seems entirely unfazed. He stands, sipping his coffee with a grin on his face."

    show Felix with dissolve

    f "You remembered my coffee order?"
    asidesp "How could I forget it? I hesitate to even call it coffee."
    f "Hey, if it has coffee in it, then it's coffee!"
    asidean "...I-I mean, that's {i}technically{/i} true. But, what you have completely disregards the integrity of—"
    "I look up only to see a mischievous grin sitting on Felix's face. I realize that I'm being baited into discussing the schematics of coffee, which I do {i}not{/i} have time for."
    f "No, no, keep going. Tell me about the 'sacred integrity' of coffee making."
    asidean "I won't let you distract me! We have a meeting to get through, and you have a painting to work on."
    f "Alright, alright, you caught me. But, some other time, I would actually like to hear your coffee rant."
    "My cheeks flush."
    asideem "M-Maybe later. Right now, I have an important update for you."
    "Felix feigns exaggerated excitement."
    f "I love important updates!"
    aside "It's nothing bad, promise… I want to host a launch party, to celebrate our new concept. Sylphia's on board already, but I wanted to run it by you. See what you think."
    f "Sure, why not? What better way to get people excited than to hold a party. Count me in!"
   
    hide Felix with dissolve
   
    asidesh "(That was easy… Though, everything feels easy with Felix.)"
    asidee "Great!"

    show Felix_N2 with dissolve

    f "Oh, before I forget. I compiled a list of things that you'll need to consider for the renovations. Lighting concerns, temperature, and materials."
    "He hands me a set of carefully hand-written notes."

    hide Felix_N2
    show Felix_C 
    with dissolve

    f "Is… are you handling all this yourself?"
    "I flip through the pages."
    aside "Sylphia helps where she can, but for the most part—yes."
    "Felix nods absentmindedly."

    hide Felix_C
    show Felix_N2 
    with dissolve

    f "I see."
    aside "Thank you. This must have taken you a long time."
    f "It was nothing… I just hope you find it useful."
    asidesp "Oh, no worries there. This is exactly what I needed."

    hide Felix_N2
    show Felix_B
    with dissolve

    "When I look back at him, a faint red blush is splashed across his cheeks. His eyes won't meet mine."
    f "Glad to hear it."
    asideeb "(...)" 

    hide Felix_B with dissolve

    "The rest of the meeting goes smoothly. We stray off-topic a few more times, but I don't mind." 
    "Time spent with Felix is easy. As natural as breathing."
    asidesa "(I only hope it stays that way.)"


    #morning
    #bg Felix's Studio

############################################
#GOOD TIMES
############################################
    window hide
    show black with dissolve
    window auto
    pause (2.0)

    scene studio with dissolve 
    play music "Felix.ogg" fadeout 2.0 fadein 2.0

    "Felix and I lounge in Studio Alizeti again, sunlight spilling across half-finished canvases. Our conversation drifts as easily as the morning breeze, ideas bouncing between us back and forth."

    show black with wipedown

    f "Okay, okay, my turn. Close your eyes and imagine {i}this{/i}. That empty wall near the front door, what if—and stick with me here—you let me paint a mural of Saint Caelan, riding a unicorn."
    "As requested, my eyes are closed. But the image of the noble Water Saint riding {i}anything{/i} causes me to giggle uncontrollably."
    "Felix's voice joins my own, time stops, and for a moment, nothing else matters. Nothing but unbridled joy."
    
    scene studio with wipeup    

    asidesp "You don't even know what the Saint looks like!"

    show Felix with dissolve

    f "I'll make something up! That'll be what draws people in."
    f "It's not like they'll be able to prove me wrong."
    asidesm "You're ridiculous." 

    hide Felix with dissolve

    "The meeting has absolutely gone off course, but the warmth in my chest that I feel when Felix smiles—a mini sun all on its own—makes it worth it."
    asideem "(My heart's been doing that thing again. Skipping. I really need to get that under control…)" 

    show studio with dissolve

    "Time blurs again. Attempts are made to get us back on track, but for the most part Felix and I spend most of the meeting talking about anything and everything."
    "I'm starting to think he does it on purpose. But I have to admit his tangents give me a much-needed break from thinking about work."
    asidesp "You're not originally from Halis?"

    show Felix with dissolve

    f "Nope, I was born in a human settlement about a day's journey from here. But, Halis has been my home for the past seven years."

    hide Felix with dissolve


    menu:
            "Ask why he left his hometown.": #Affection up
                $ felix_pts += 10
                show screen choice_indicator(FELIX_COLOR)
                asidesp "What made you leave your hometown?"
                "Felix's face falls for a split second, but enough for me to catch it."
                asidesa "(Oh, maybe it's a touchy subject.)"
                show Felix_Sad with dissolve
                f "...Oh. Well. Y'know, just—the usual. There's more opportunities here. Especially for me and my art."  
                hide Felix_Sad
                show Felix 
                with dissolve
                f "Opportunities like this one!"
                "I pretend not to notice the way he jumps on the chance to deflect the attention away from himself."
            "Dont pry any further.":
                asidesa "(I shouldn't be nosy.)"
  

#BRANCHES CONVERGE HERE

    show Felix with dissolve

    f "What about you? Are you from here?"
    aside "Yes, I've lived here my whole life. Though, my parents moved away some years ago to be somewhere quieter."
    f "Do you miss them?"
    aside "We send letters back and forth, but I do miss when it was easier to visit."
    asideeb "Now, Café Bloom is where I go when I need to feel like I'm with family."

    hide Felix
    show Felix_S 
    with dissolve

    "I look up with a melancholy smile as I say it. Felix's expression is pained—sympathy maybe?"

    hide Felix_S with dissolve

    asidesp "Anyways! I get to see my family often enough. Actually—" 
    "A yawn interrupts mid sentence. Felix's lips twitch, amused."

    show Felix with dissolve

    f "Astra? You ok?"
    aside "Yeah, yeah, I'm fine. Just—"
    "Another yawn breaks through."
    asidesh "...a little sleepy."

    hide Felix
    show Felix_C
    with dissolve

    "The second time it happens, Felix's brows pinch together in concern. The pencil in his hand stills, then he closes his sketchbook with a quiet snap."
    f "Tell you what, why don't we take a break?"
    asidee "Coffee?" 

    hide Felix_C
    show Felix
    with dissolve

    f "Got it in one. It's no Café Bloom, but there's a place I like not too far from here."
    asidesm "(I'm going to need something stronger than what Felix calls 'coffee'.)"
    asidea "Do they serve real coffee, Felix? Not those cups of sugar that you like to call coffee."
    f "Yes, they serve 'real' coffee. Promise."
    asidesh "Then… I could go for a break." 
    f "That's the spirit. C'mon then." 

    hide Felix with dissolve
    scene market with dissolve
    
    #TODO uncomment below track if above track is changed
    #play music "city_day.ogg" fadein 2.0
    #bg market or shopping street

    "Felix leads the way down the street, weaving through the market's quiet hum until we stop at a small coffee cart tucked between two flower stalls." 

    show Felix with dissolve

    f "A cortado right? Plain, no add-ins?"
    asideem "(I don't even remember telling him that. He must have picked it up from a previous meeting.)"
    aside "...Yeah."
    "Felix winks at me, setting off fluttering butterflies in my stomach, before he turns to the cart's attendant."

    hide Felix with dissolve

    f "One vanilla latte, iced, and one cortado, plain." 

    show Felix with dissolve

    "He looks back at me, eyes gleaming."
    f "Anything else? This place also has really good croissants." 
    asidee "Oh, sure!"

    hide Felix with dissolve

    f "Can you add two croissants to that?"
    "The attendant begins working on the order."

    show Felix with dissolve

    f "I come here whenever I need a pick-me-up while working. You looked like you could use one yourself."
    "His tone is light, but the worry behind it is impossible to miss. For a moment, I can't decide whether to be flattered or embarrassed."  

    hide Felix
    show Felix_N2
    with dissolve

    f "You're not overworking yourself are you?"
    asidesh "I didn't sleep well last night, that's all."
    asidesa "(Or, the past week.)"
    f "..."
    "If Felix wants to question me further, his chance is stolen by the attendant's cheery voice."
    att "Here's your order!"

    hide Felix_N2 with dissolve

    f "Thanks."
    "I stand off to the side since it seems like Felix has everything under control. As the woman hands everything over, I see her give Felix a sly grin. Her voice is just loud enough for me to hear what she says."
    att "...And can I just say, you and your girlfriend are the cutest! The two of you remind me of my own partner and I when we were younger."
    "Searing heat flares across my cheeks. My face burns at the notion, and I turn away, trying to pretend that I didn't hear anything."
    f "We're not together." 
    "His words leave no room for debate, and the usual teasing lilt in his voice is nowhere to be found."
    asidep "(...Not even an ounce of hesitation?)"
    asidesh "(Is the idea of us dating really that bad?)"
    "I knew the truth, we {i}weren't{/i} together. We had a working relationship. Nothing that Felix said was false." 
    "He had every right to correct her."
    asidesa "(So why does it feel like I'm being splashed with cold water?)"
    att "Oh— my apologies. You two seem so comfortable together, I just thought—"
    f "No worries! It was an honest mistake. Thanks again!" 
    "Felix's usual charm returns, light and polite. But when he turns back toward me, there's a subtle tension in his shoulders that wasn't there before."  

    show Felix_Sad with dissolve

    f "...Let's go back."

    hide Felix_Sad with dissolve

    "And just like that, Felix turns on his heel and starts toward the studio.  He keeps a fast pace, not even turning around to check if I'm following him."
    "I set off after him, trying to catch up. A brief jog brings me right next to Felix, though my legs burn a little at the effort it takes to keep up with his longer stride." 
    "The walk back is silent. Felix doesn't attempt to make conversation, and his expression is unnaturally neutral."

    play audio "<from 0 to 3>bell.mp3"
    scene studio_evening with dissolve
    play music "city_night.ogg" fadeout 2.0 fadein 2.0
    #TODO switch track
    
    "As soon as the door to Studio Alizeti closes behind me, I start to speak."
    aside "You okay?"

    show Felix with dissolve

    f "Yeah! Fine. Just… realized I forgot to deliver a commission."
    "He runs a hand over his head, eyes darting to his workspace. It's an excuse—one that sounds too neat, too ready."

    hide Felix with dissolve

    "I follow his gaze to a corner of the studio, to a small space suspiciously clear of clutter." 
    "In that space, an unframed canvas is propped up. Surprisingly, the painting is a portrait—not a landscape. It depicts  a young woman holding a sunflower almost as large as her face."
    asidesp "(I've only seen Felix paint flowers…)"
    "I knew he was capable of painting other things, but—"
    "I wonder if this delivery isn't an excuse at all."
    aside "(Is that the commission he's talking about?)"

    show Felix_N2 with dissolve

    f "...Mind if we end today's meeting early?"
    asidesp "Oh… Well, we still haven't decided on a direction for the mural yet—"
    f "Right… I'll sketch a few options based on what we've discussed so far and you can choose from one of those?"
    asidesa "Sure… That should work."
    asidesh "Do you… need help with the delivery?"

    hide Felix_N2
    show Felix
    with dissolve

    f "No need, you're busy enough as is. I'll take care of it."
    aside "Okay. Then, I'll see you at our next meeting?"
    f "Yep! Next meeting, Café Bloom right? I'll be there."

    stop music fadeout 3.0

    "His fingers tap rhythmically against his thigh, and his smile is strained. Seeing as I'm clearly being kicked out, I head to the door."

    hide Felix with dissolve

    asidesp "Bye, Felix."

    play audio "<from 0 to 3>bell.mp3"
    #TODO new bg and uncomment below if above track is changed
    #play music "city_night.ogg" fadeout 2.0 fadein 2.0
    scene market_evening with dissolve

    asidesa "(...No response.)"
    "I let the door slowly swing shut behind me as I exit the studio. For a moment, the quiet outside feels colder than before."  

    play audio "<from 0 to 3>bell.mp3"

    "Then a frantic voice calls out, startling me."
    
    scene market_evening 
    show Felix_N2 with dissolve

    f "Be careful going back!"
    "Felix stands in the doorway, looking apologetic."

    hide Felix_N2
    show Felix_C
    with dissolve

    f "...I'll see you next week."
    aside "Yeah, see you."

    hide Felix_C with dissolve
    play audio "<from 2 to 4>dooropenclose.mp3" #close

    "The door shuts again, leaving only the fading chime of the bell and the quiet thud of my heartbeat."  
    asidesa "(Somehow, it feels like I just left more behind than a meeting.)"
   
    window hide
    show black with dissolve
    window auto
    pause (2.0)
 
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    scene cafe_interior:
        xcenter 0.5
        ycenter 0.5
        zoom 2.0
        xoffset 800
        yoffset 50
    with dissolve

    "The next week arrives before I'm ready for it. The project has been progressing nicely—smooth, efficient, if not faster than expected. In all honesty, we would probably be able to wrap everything up soon."

    "The thought settles like a rock at the bottom of my stomach. Heavy and uncomfortable."
    "Amidst my spiraling train of thought—the door to the break room at Café Bloom opens and Felix peeks his head in, scanning the space until his eyes land on me sitting at the table."
    "Albion forced us to start having our meetings here after the first time. Said we were 'too loud' and 'bothersome'."

    show Felix with easeinleft

    f "Good afternoon!"
    "I can't help myself, I laugh, covering my grin with a hand."
    aside2 "Hey, Felix." 

    hide Felix with dissolve

    "He slides into the seat across from me."

    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "Got all your notes?"
    asidesp2 "Yep! Got 'em right here."
    f "Prepared as always, huh? Coffee first?"
    "I gesture at the table where two cups sit."
    asidesm2 "Already taken care of."
    f "Oh? Thanks!"

    hide Felix with dissolve

    "He smiles, but unlike before, it doesn't quite reach his eyes. It's distant, like something unspoken lingers just beneath the surface."    
    asidesa2 "(Is he still bothered about what happened last time?)"

    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "Well then, I guess we can get started right away."
    aside2 "Y-yeah, let's begin."
    
    hide Felix with dissolve

    asidesa2 "(I guess there won't be any distractions this time…)"

    "Time drifts by easily enough. We go through designs, logistics, and final details." 
    "But the closer we get to the end of the meeting, the more Felix fiddles with his pen, tapping it on the table and spinning it across his knuckles."

    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "Oh, I almost forgot! I brought the mural sketches." 


    hide Felix with dissolve

    "He flips through his sketchbook until he finds what he's looking for."
    "In front of me are three beautiful landscapes, each depicting a different scene in Halis."
    "Any one of them would look amazing in the café… but, for some reason, it felt like they were missing something."
    "All of Felix's paintings had something that made me feel alive, like I was standing in the paintings themselves."
    asidesa2 "(They're exactly what I asked for but—)"

    play audio "knock.mp3" fadeout 2.0

    "A knock sounds at the breakroom door. A split second later, Sylphia peeks her head in."

    show Sylphia with easeinright

    s "Sorry to interrupt, but I {i}might{/i} have overheard you guys discussing the mural~"
    s "Can I see?"
    
    hide Sylphia with dissolve

    "Her timing is perfect, a second opinion is exactly what I need right now."
    asidesp2 "Of course!"

    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "Be my guest."

    hide Felix with dissolve

    "Sylphia walks over, scanning the pages with intense interest."

    show Sylphia:
        zoom 1.7
        xoffset 400 
        yoffset -200
    with easeinright

    s "Felix, these are fantastic!" 
    "She points towards the second option."
    s "This one captures the community in Halis wonderfully." 
    s "What do you think, Astra?"

    #TODO emotional track

    aside2  "...It's hard to decide, I love them all. But— I agree with Sylphia. I think this one is the best."

    hide Sylphia with dissolve

    "Felix looks at me with a hint of confusion. I can't bring myself to meet his gaze."

    show Felix_N2:
        zoom 1.7
        yoffset -100
        xoffset 350
    with easeinleft

    f "...Sounds like it's settled then. I can get started next week." 
    asidesh2 "Great." 


    hide Felix_N2 with dissolve

    "Sylphia's eyes dart between us. Then, she claps her hands together loudly."


    show Sylphia:
        zoom 1.7
        xoffset 400 
        yoffset -200
    with dissolve

    s "Perfect! Well, that's all I needed. I'll leave you two alone now. Bye~"

    hide Sylphia with dissolve
    play audio "<from 2 to 4>dooropenclose.mp3" #close
    
    "The door shuts, leaving Felix and I alone again."

    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "...Do you really like the sketch? You know you can tell me if something's wrong with it, yeah?"
    asidesa2 "(How can I possibly tell him that? …I can't even explain why I don't like it.)"

    hide Felix_C with dissolve

    menu:

            "Something's off.": 
                $ felix_pts += 10
                show screen choice_indicator(FELIX_COLOR)
                asidesh2 "Nothing's 'wrong' with it. I truly do think it's beautiful."

                show Felix_C:
                    zoom 1.7
                    yoffset -100
                    xoffset 350
                with dissolve

                f "But?"
                asidesa2 "I— I don't know. It just doesn't feel the same as your other pieces."
                f "I don't think I did anything different from what I normally do."
                aside2 "It's really not a problem. Like Sylphia said, it's fantastic."

            "I love it.":
                "My nerves get the best of me, and so, I decide to keep my thoughts to myself."
                "Besides, Sylphia liked it, which means that I'm probably just overthinking it."

    #BRANCHES CONVERGE HERE

    hide Felix_C
    show Felix_Sad:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "Alright… then I'll move forward with this one."
    "I pull myself together enough to grin."
    aside2 "I can't wait!"

    hide Felix_Sad
    show Felix_N2:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve


    f "Was that everything?"
    "I go through the list in my mind."
    asidesp2 "Yep! At least, for today."
    "Though, there was one more thing… We only ever meet for work but—"
    "Our collaboration is almost over."
    "And what better way to celebrate than to invite him to dinner?"
    aside2 "Actually. I have one last question."
    "He pauses, hand halfway to his sketchbook."

    hide Felix_N2
    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "Sure! What's up?"

    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    "My heart beats faster, my body finally catching onto what I'm about to say."

    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    asideb2 "I was thinking… After the launch, would you like to go to dinner with me?" 

    hide Felix
    show Felix_B:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    "His eyes widen, his face reddening. Then, his eyebrows pinch together."

    hide Felix_B
    show Felix_S:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    asideeb2 "I want to celebrate us finishing this project. And— I also just want us to keep hanging out, without having to worry about work."
    f "That's— Astra, I—"
    "He shakes his head."
    f "That can't happen."

    hide Felix_S with dissolve

    play music "tension.ogg" fadeout 2.0 fadein 2.0

    "My heart drops."
    asidesa2 "I thought we were becoming friends? That we were—"
    "I don't dare to finish that thought."

    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "We are! We— we {i}were{/i}. But, Astra I can't—"
    "He cuts himself off suddenly, taking a deep breath before continuing." 

    hide Felix_C
    show Felix_U:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "...I just can't. I promised myself."
    asidesp2 "Promised yourself what?"
    "He starts to stand up. His hands fumble with his things, movements clumsy where they're usually precise."  

    scene cafe_interior 
    hide Felix_U
    show Felix_C
    with dissolve


    f "I have to go. Sorry—again."
    "He laughs under his breath, but there's no joy in it."
    f "I'm always apologizing— You're wonderful, Astra. I'm just… being selfish."

    hide Felix_C with dissolve

    "I start to stand up too, reaching towards him." 
    "I manage to grasp the sleeve of his jumpsuit—tightly—before I realize what I'm doing. He stills—then turns slowly to face me." 

    show Felix_N2
    with dissolve

    "For a heartbeat, neither of us moves. Then, with a soft, heartbreaking smile, he pries my hand free, squeezing it once before letting go."

    hide Felix_N2
    show Felix
    with dissolve

    f "I'll see you at our next meeting. {w}Be safe."

    hide Felix with dissolve

    play audio "dooropenclose.mp3" #open and close

    asidesp2 "Huh?"
    asidesa2 "(What just happened?)"
    "My hand prickles—the remnants of Felix's touch—but this time my heart races with panic."
    "After a moment's hesitation, I open the break room door hastily."

    scene cafe_interior
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg"

    "Albion stands by the counter, mid-clean. His gaze flicks up as I rush in, his face blank."

    show Albion_N2 with dissolve

    al "He left."
    asidesp2 "Maybe I can catch him."
    "Albion's face scrunches up."

    hide Albion_N2
    show Albion_SC 
    with dissolve

    al "Don't."
    "I look over at him, thrown by the firmness in his tone."
    asidean2 "You don't even know why he left."
    al "No, but I {i}do{/i} know that you're still on the clock."
    asidesa2 "..."

    hide Albion_SC with dissolve

    "I smooth my apron out nervously. Of course he'd say that."
    "I stare at the door, hoping that maybe Felix will come running back inside, hoping that I heard him wrong somehow."
    asidesh2 "(He's right though. I have work to do.)"
    asidesh2 "Okay… Then, I guess I'll get back to it."
    "My mind is still spiralling."
    asidesh2 "...It'll be okay, right?"

    show Albion_SC 
    with dissolve

    al "What are you asking me for?"
    asidean2 "It was a rhetorical question, Albion."

    hide Albion_SC with dissolve

    "I let out a breath, shaking my head in exasperation. Both at Albion, and at Felix's sudden departure." 
    asidesa2 "(This isn't over yet, right? I'll just have to talk to him next time.)"

    stop ambient fadeout 3.0

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    scene kitchen with dissolve
    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0
    #morning

    "Walking into the kitchen after running errands almost sends me into shock." 
    "Two people sit at the kitchen island. One of which I expect, Qwynn's ears swiveling towards the door as it opens, their head following immediately after."
    "The other is unexpected. Velvet's bright orange tail sweeps the floor beneath them. He, too, turns to face me as I walk into the room."
    asidesp "What's happening?"
   
    show Qwynn_S at half_size with dissolve
   
    q "Morning Astra! We were just having a chat."
    "Velvet lifts their cup in greeting, perfectly at ease." 

    show Qwynn_S at Transform (xpos=250) with ease
    show Velvet at right with easeinright

    v "Want some coffee? Qwynn made it this morning."
    q "I made it for you, but {i}someone{/i} went ahead and helped themselves."
    "Velvet shrugs, not looking apologetic in the slightest."
    aside "...Sure. Coffee would be great."
    "Qwynn stands, moving to pour me a cup while Velvet watches with a grin that feels a little too knowing."

    hide Qwynn_S with easeoutleft
    show Velvet at Transform (xpos=500) with ease

    asidesp "Vel?"
    v "That's me."
    asidesm "What are you doing here? Not that you're unwelcome or anything, but—"
    "I trail off, but what I really want to ask is 'How do you know where I live?'"
    v "Felix has been acting weird lately. Other than me, you're the only person he really talks to, so I figured you'd know something." 
    v "Long story short, I came looking for you and wound up here."
   
    show Velvet at right with easeinright
    show Qwynn at Transform (xpos=250) with dissolve
   
    q "I found him at Café Bloom this morning and overheard him asking about you. I put the puzzle pieces together pretty quickly after that."

    hide Velvet 
    show Qwynn at half_size with ease
    with dissolve

    "Qwynn sets a cup of hot coffee beside me. As they pass, their hand comfortingly brushes lightly across my shoulder."

    hide Qwynn
    show Qwynn_N3 at half_size
    with dissolve

    q "Doing alright? You look tired, did you even sleep last night?"
    "Honestly, between reading contracts, managing suppliers, deliveries, meetings, my regular shifts, and now—Felix. Sleep has been hard to come by."
    "But Qwynn doesn't need to know that."
    asidesh "I'm fine. Vel, you said Felix's been acting weird."

    hide Qwynn_N3
    show Qwynn_M at half_size
    with dissolve

    "I think I see Qwynn make a face at the mention of Felix's name, a trace of sadness making its way through—but after a blink, it's gone."
   
    hide Qwynn_M 
    with dissolve
   
    asidesa "(I must be seeing things. Why would Qwynn be sad?)"

    show Velvet with dissolve

    v "Yeah, he won't tell me what happened though. Was hoping you knew."
    "I consider the last time I saw Felix. The smile that didn't reach his eyes. The way he said goodbye without really saying it."
    asidesa "(I'm not sure I know what happened either…)"
    
    hide Velvet with dissolve
    show Qwynn_N3 at half_size with dissolve
    
    q "I thought things were going well?"
    asidesp "They are! Or, they were. I mean, the plan itself is fine but…"

    hide Qwynn_N3 with dissolve

    "But what? He rejected me?"
    asidea "(Though it felt less like rejection and more like dismissal. Like there's something else going on.)"
    "I've been trying not to think about it too much. Not too difficult considering my recent workload, but now that familiar sting comes back into focus."
    asidesh "I don't know what happened."

    show Qwynn_N3 at half_size with dissolve

    q "Huh? What sense does that make? From what I've heard, you guys were getting along great."
    asidesp "We were, I— I thought things were going well too. He's just become more distant than before, like he's avoiding me."
    "Vel puts their head into their hands."
   
    show Qwynn_N3 at Transform (xpos=150) with ease
    show Velvet at right with dissolve
   
    v "I thought it might be something like that… I was hoping this time would be different."
    aside "Different?"
    asidesa "(This has happened before?)"
    q "What do you know?"
    "Vel lifts his head up, appearing conflicted."
    v "He always does this—pushing the people who care away—thinking he's being helpful when in reality all it does is make everything worse."
    v "When things are going well, he starts pulling back."
    asidesa "(Why would he do that?)"
    aside "I'm planning to talk to him at our next meeting. He left so suddenly the other day, I didn't get the chance to really say anything."
    v "Sounds about right." 
    "Qwynn sighs, the sounds of their nails tapping the counter vaguely registering next to me."

    hide Velvet
    hide Qwynn_N3
    show Qwynn_M at half_size 
    with dissolve

    q "You've always been much more forgiving than me, Aste."
    asidesp "We don't have to agree, but I won't give up until I get a proper explanation."

    hide Qwynn_M
    show Qwynn_N3 at half_size 
    with dissolve

    "Qwynn smiles, a little bittersweetly."
    q "That's one of the things I love about you. You don't give up on people."
    asidesp "Not on the people who matter, I don't."

    show Qwynn_N3 at Transform (xpos=150) with ease
    show Velvet at right with easeinright

    v "How sweet~"

    show Qwynn_B at half_size, Transform (xpos=150) with ease

    play sfx "sfx_shake.ogg"
    show kitchen with vpunch

    asidesp "Saints— I forgot you were here."
    "Vel laughs, standing up and stretching their arms up overhead."
    v "Sorry, sorry, I'll make my way home now. Thanks for the coffee, Qwynn. And Astra, for the information." 

    hide Qwynn_B with dissolve
    hide Velvet with easeoutright
    show Qwynn_N3 at half_size with ease

    "And just like that, Velvet is gone—leaving me and Qwynn alone in the soft morning quiet."
    q "If this Felix guy says anything to you again just—"
    aside "You'll be the first to know. Promise."

    hide Qwynn_B
    show Qwynn_S at half_size 
    with dissolve


    q "Good. Don't you forget it either. I'm ready to go anytime."
    "I chuckle softly, warmth finally replacing the ache in my chest. Qwynn's protectiveness never fails at making me feel safe… and loved."
    
    hide Qwynn_S with dissolve
    
    asidesp "(Right. Then, next time. I'll make sure to get the full story, and I won't leave until I do.)"

##############################################
#SICK DAY
##############################################

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    scene bedroom with dissolve

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0

    "I wake up later than normal to a soft knock on my door. Before I can respond, Qwynn slips in, careful not to make too much noise."

    show Qwynn at half_size with dissolve

    q "Astra? You don't have to work today do you?" 

    hide Qwynn with dissolve

    "My head pounds, but I turn my head slowly, where I can vaguely make out Qwynn's form moving closer."
    "A weight settles next to me on the bed. A hand comes to rest on my forehead. Worry creases Qwynn's brow upon feeling the heat."
  
    show Qwynn:
        zoom 1.6
        yoffset -100
        xoffset -250
    with dissolve
  
    q "You're sick."
    asideeb "It's just a headache. It'll pass." 

    hide Qwynn
    show Qwynn_N3:
        zoom 1.6
        yoffset -100
        xoffset -250
    with dissolve

    q "...You haven't been sleeping. I can hear you get up in the middle of the night, you know."
    asideeb "I've been waking you up?"  
    "Qwynn sighs softly." 
    q "Don't worry about it. You should rest, I'll let Sylphia know you can't come today."


    hide Qwynn_N3 with dissolve

    "The weight disappears. I reach out to grab for Qwynn's wrist, stopping them from leaving."
    asideb "I don't have work today, just that meeting with Felix."

    show Qwynn_S:
        zoom 1.6
        yoffset -100
        xoffset -250
    with dissolve
      
    q "Oh, even better, I'm sure he'll understand that you can't make it." 

    hide Qwynn_S with dissolve

    "I purse my lips. There's no way I can miss it."
    asideeb "(If I don't meet him today, I feel like I'll miss my chance to uncover the truth…)"
    asideb "We still have things to discuss. The launch party is coming up, this is the last chance I'll have to make sure everything is squared away."
    asideem "(Not to mention I want more answers about why he's distancing himself from me.)"

    show Qwynn_N3:
        zoom 1.6
        yoffset -100
        xoffset -250
    with dissolve

    q "Aste… You've been working non-stop for weeks. Your plan is solid. You can afford to rest for a couple days."
    asideb "I don't have days to spare, Qwynn."
    q "You do now. You're not going anywhere like this."

    hide Qwynn_N3 with dissolve

    asideeb "(It's just a headache.)"
    "As soon as I think about it— A sharp pain stabs through my skull. I press a hand to it, adding pressure."
    "I hear Qwynn suck air through their teeth and they lower their voice." 

    show Qwynn_M:
        zoom 1.6
        yoffset -100
        xoffset -250
    with dissolve

    q "Go back to sleep. I'll go out and buy you some tea and herbs, okay?"
    a "...Okay."
   
    hide Qwynn_M with dissolve  
   
    "I wait patiently, straining my ears for the moment when the front door clicks shut."
    asideeb "(Sorry Qwynn, I'll rest later. I have to see this through.)"

    #beat

    scene bedroom with dissolve:
        blur 10
    "When I finally hear that familiar click, I ease myself out of bed. My vision blurs, but only for a few seconds."
    
    scene bedroom with dissolve
    
    asideem "(I can do this.)"
    "I know I don't have much time until Qwynn returns, if they catch me sneaking out I'll be manhandled back into bed and my chances of seeing Felix will be zero."
    "I dress slowly, trying my best to ignore my headache and the persistent soreness in my limbs."
    "Each movement feels heavier than the last, but I keep going—because stopping means thinking, and I can't afford that right now."

    show kitchen with dissolve

    asideem "(Almost done. Just need to grab my bag.)"
    "The bag in question hangs conveniently by the door. Already packed."
    asideb "(Perfect!)"

    scene market with dissolve
    stop music fadeout 3.0

    "The cool air from outside goes straight through me."
    asideem "(Studio Alizeti's not far from here. I just have to cross through Block 3.)"


    show black with dissolve
    scene market2 with dissolve:
        blur 20
    #show blackspots with dissolve

    "I don't even know where I am when my vision blurs again, black spots dancing across my vision."
    asideem "(I'm so tired…)"

    show black with dissolve

    "My breathing gets heavier. My body tilts forward. Instinctively, I fling my arms out to brace for a fall."

    #black screen
    #TODO change music

    show voiced with dissolve
    play sfx "sfx_shake.ogg"
    "But, instead of hitting hard ground, someone catches me. Their grip is firm and solid."

    voice "<from 0 to 3>audio/felix/felix_1.ogg"
    who "Astra?! Are you okay?"

    #her eyes open, show bg again w/ Felix
    scene market2 with dissolve:
        blur 5
    show voiced with dissolve
    show Felix_S:
        zoom 1.7
        yoffset -100
        xoffset 350
        blur 5
    with dissolve

    play music "city_night.ogg" fadeout 2.0 fadein 2.0

    voice "<from 0 to 2>audio/astra/astra_felix.ogg"
    asideb "Felix?"
    "Felix's arms tighten around me. I must have started hallucinating."

    hide Felix_S
    show Felix_S:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve

    voice "<from 4 to 7>audio/astra/astra_felix.ogg"
    asideb "What are you doing out here?"

    hide Felix_S
    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve 

    voice "<from 4 to 13>audio/felix/felix_1.ogg"
    f "Me?? You were over an hour late! Saints Astra, I've been looking for you everywhere!"

    hide Felix_C with dissolve

    "In my fever induced haze, it takes some time for me to register what Felix just said."

    voice "<from 9 to 10>audio/astra/astra_felix.ogg"
    asideeb "An hour?"
    "He looks at me incredulously, and he seems to come to his own realization."
   
    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve 

    voice "<from 14 to 17>audio/felix/felix_1.ogg"
    f "Have you been wandering around the whole time?" 
    "His grip on me loosens, and he scans my face closely."
    voice "<from 17 to 20>audio/felix/felix_1.ogg"
    f "Are you sick?"


    voice "<from 14 to 16>audio/astra/astra_felix.ogg"
    asideeb "Just a headache." 
    "I hear Felix laugh, but the sound is broken and distressed."  

    hide Felix_C
    show Felix_Sad:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve 

    voice "<from 22 to 26.5>audio/felix/felix_1.ogg"
    f "Just a headache. Right."
    voice "<from 27 to 30>audio/felix/felix_1.ogg"
    f "Where do you live? I'm taking you home."


    voice "<from 21 to 23>audio/astra/astra_felix.ogg"
    asideem "...Block 4."

    hide Felix_Sad
    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve  

    voice "<from 30 to 37>audio/felix/felix_1.ogg"
    f "Saints— we're in Block 3 right now. How did you even—"

    show market2 with dissolve:
        blur 5
    hide Felix_C
    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350
        blur 5
    with dissolve  

    "A giggle escapes me."
    asideb "(Illness 0, Astra 1. I made it halfway there, {i}and{/i} ended up finding Felix.)"

    hide Felix_C
    show Felix_Sad:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve 

    voice "<from 38 to 43>audio/felix/felix_1.ogg"
    f "Astra, this isn't funny. What if something happened to you?"

    hide Felix_Sad
    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve  


    voice "<from 43 to 50>audio/felix/felix_1.ogg"
    f "I couldn't— I don't know what I would do."

    hide Felix_C
    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350 
        blur 5
    with dissolve  

    "The delirious part of my brain lights up in joy."
    asideb "(He {i}does{/i} care.)"
    "He exhales sharply, and if my vision weren't so hazy, I'd say his eyes were glistening with unshed tears."
    
    voice "<from 51 to 56>audio/felix/felix_1.ogg"
    f "...This is my fault. Isn't it?"
    "That, of all things Felix has said so far, clears my mind instantly."

    hide Felix_C
    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve

    voice "<from 35 to 42>audio/astra/astra_felix.ogg"
    asideeb "No! Not your fault.  I just— This is our last meeting before the launch."

    voice "<from 57 to 62>audio/felix/felix_1.ogg"
    f "See? That's exactly what I mean. You're here because of what happened last time."
    "Anger seeps into his voice."

    hide Felix_C
    show Felix_Sad:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve

    voice "<from 62 to 65>audio/felix/felix_1.ogg"
    f "You're so—"
  
    hide Felix_Sad
    show Felix_U:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve

    "The anger takes a backseat, and his voice wavers."

    hide Felix_U
    show Felix_Sad:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve  

    voice "<from 65 to 72>audio/felix/felix_1.ogg"
    f "Reckless! Taking on extra work, living off of coffee and dreams, and now—"

    hide Felix_Sad
    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350 
    with dissolve  

    voice "<from 72 to 76.2>audio/felix/felix_1.ogg" 
    f "Why? Why do you do this?"

    hide Felix_C with dissolve

    asidean "(Reckless???)"
    "I knew I was taking a risk leaving home like this, but… I only did it because I knew I'd regret not trying."
   
    voice "<from 42 to 47>audio/astra/astra_felix.ogg"
    asidean "Huh? Felix, I only—"
    "A wave of pain ripples through my skull. In vain, my hand reaches up to clutch at it. An attempt to ground myself. Felix's voice becomes frantic."

    show market2 with dissolve:
        blur 10
    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350 
        blur 10
    with dissolve

    voice "<from 77 to 81>audio/felix/felix_1.ogg" 
    f "Okay, okay, we're leaving now."
    "He pulls me into his side, tugging my arm to rest over his shoulders while his own arm wraps around my waist."

    voice "<from 82 to 87>audio/felix/felix_1.ogg" 
    f "Sorry, this is the best I can do for now. You okay?"

    voice "<from 56.4 to 60>audio/astra/astra_felix.ogg"
    asideem "I can walk on my own..."

    voice "<from 87 to 96>audio/felix/felix_1.ogg" 
    f "You can barely keep yourself upright. C'mon, one foot in front of the other, yeah? You got this."

    hide Felix_C with dissolve

    "It takes all my willpower not to bury myself in Felix's warmth, his body a natural shield against the chilly breeze." 
    asideem "(I feel guilty for thinking it, but… this is nice.)"
    "Now that I've accomplished my goal, it's easy to give into the overwhelming tiredness that I feel."
    
    show market2 with dissolve:
        blur 20
    
    "I barely register the journey home. It's not long before the world starts to blur again. My steps falter. Sleep pulls at me, heavy and irresistible, until finally—I let it."

    show black with dissolve

    jump Felix_chp3


#########################################
# END
#########################################

#window hide
#pause (2.0)
#show endcard with dissolve
#$ renpy.pause(5.0)









