# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define fside = Character ("FELIX", image="felix")
image define fside = "side felix"

label route_split:

"Who should I ask for help?"
menu:

    "Albion": 
        $ route = 'albion'
        $ albion_pts += 10
        jump Albion_Route
    "Felix":
        $ route = 'felix'
        $ felix_pts += 10
        show screen choice_indicator(FELIX_COLOR) 
        "Yey Felix!"
            
        jump Felix_Route
    "Qwynn":
        $ route = 'qwynn'
        jump Qwynn_Route
        $ qwynn_pts += 10
    #"Caelan":
        #$ route = 'caelan'
        #show screen choice_indicator(CAELAN_COLOR)
        #jump Caelan_Route


#########################################
# HAVE CONFIDENCE
#########################################


label Felix_chp1: 

    $ persistent.status_button = True

    window hide
    show felix_chp1 with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    scene cafe_interior_evening with squares


    "Immediately after making my decision, my hands gravitate towards each other like magnets."
    "I feel the weight of Felix's card in my pocket. Even just thinking of his calm, assured voice makes my pulse race faster."
    asidesa2 "(It's too late to backtrack now.)" 
    "It takes all my effort to pry my hands apart and rest them against my back. Even then, my body keeps fidgeting, rocking up and down on my toes. Up and down, up and down."
    "Sylphia instantly takes notice of my nervous fidgeting. Her eyes soften, and she reaches out, running a hand down my arm in a gentle, grounding gesture."
    
    show Sylphia with dissolve
    
    s "I think this is a great choice, Astra. Truly." 
    s  "...Do you have an idea of where to start?"
    "Sylphia's gentle countenance brings me back into focus, and I finally let out the breath I've been holding."
    aside2 "...I think so."
    s "You should reach out to them. We could use as many people as we can get our hands on." 
    asidesp2 "I can?"
    s "Of course! You'll be taking more of a management role for this project. It's a perfect chance for you to gain some experience."
   
    hide Sylphia with dissolve
   
    "No matter how often it happens, I'll always be grateful for the way Sylphia reassures me."
    asidesa2 "(But, management?)" 
    "I've never considered taking on that kind of responsibility before. I guess I just assumed Sylphia would handle it… but if she's asking me, that must mean she believes I can."
    asidesh2 "(Right?)"

    show Sylphia with dissolve

    asidesh2 "...You're so sure of everything."
    asidesp2 "You think if I lived as long as you, I'd feel that way too?"
    "She laughs out loud, startling me with the sudden intensity." 
    s "You humans think everything comes with age."
    "Once her giggles subside, Sylphia opens her eyes, a serious look forming within them."
    s "You have wonderful ideas, Astra. Ideas that are formed in moments of vulnerability and hesitance. Sometimes, I need that perspective." 
    s "I have every confidence in you."
    aside2 "Alright, then… Thank you." 
    s "No worries. Now— Let's get back to work shall we?"

    hide Sylphia with dissolve

    "She turns back to the counter, leaving me with her words still echoing in my chest."
    asidesa2 "(Trust yourself, Astra. Just like you did when you chose this path.)"
    "My hand rests over my pocket where Felix's card lay, like it's a treasure."

    show felixcard with dissolve

    "The card is simple yet striking: off-white stock, the name of Felix's studio scrawled in bold brushstrokes across the center, as though painted by hand." 
    "Sunflowers are stamped in the corner, their yellow ink just a little smudged—like it was pressed in haste, or with affection."
    asidesh2 "(He {i}did{/i} tell me to come find him if I needed him for a job.)"

    hide felixcard with dissolve

    aside2 "(Okay. After my shift tomorrow, I'll visit Studio Alizeti.)"
    asidesm2 "(I can do this.)"

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    #CAFFINE

    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0
    show kitchen_dawn with dissolve

    "The kitchen is cold this early in the morning. A cup of coffee sits between my palms—heating them—the contrast causing little shivers to snake up my spine."
    "Last night, I {i}tried{/i} to sleep, but my itch to write down all my ideas drove me out of bed."
    "As I sip on my brew, I stare at my worn notebook. A mess of notes are scrawled across the page."
    "How often should we rotate artists? Where should work be displayed? Is there room for a mural somewhere?"
    asidesa "(Lots of questions… but not many answers.)"
    "Setting my mug down sends a small splash of coffee onto my notes."
    asidesp "Oh, oops." 
    "I slide the notebook away, reaching for a nearby towel to wipe up the small mess when Qwynn steps into my line of sight."

    show Qwynn_N3 at half_size with dissolve

    q "That poor notebook. With all the coffee you spill on that thing, I'm surprised it's still legible."  
    "Qwynn yawns as they settle into the stool next to mine."
 
    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve
 
    q "Good morning."
    aside "Morning!" 

    hide Qwynn_S
    show Qwynn_N3 at half_size
    with dissolve

    "They point to my notes, sharp nails tapping on the open pages with curiosity."
    q "Whatcha workin' on?"
    aside "Well, I told Sylphia that we should focus on creating community by partnering with local artists. It'll be my first managerial role. I'm jotting down some ideas."
    asideem "(And maybe… imagining what Felix would think of them… But only because he can answer my questions!)"
    q "Damn, management?"
    asidesm "You have your own boutique that you manage, Qwynn. This is my chance to do the same thing. I can't waste this opportunity."
  
    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve

    q "Congratulations. I'm happy for you, Aste."
    "They look towards the window at the rising sun, and then at the cup of coffee resting beside me."
    
    hide Qwynn_S
    show Qwynn at half_size
    with dissolve
    
    q "Please tell me you haven't been up all night."
    asidesh "Uhhhhhh…"
    "Qwynn groans."

    hide Qwynn
    show Qwynn_M at half_size
    with dissolve

    q "...Aste. Really? How many cups of coffee have you had?"
    asidesh "...Two?"

    hide Qwynn_M
    show Qwynn at half_size
    with dissolve   

    "Their eyes narrow."
    asideeb "Ok, ok, fine! ...It's my third."

    hide Qwynn
    show Qwynn_N3 at half_size
    with dissolve

    q "Do you at least have time to nap before work?"
    asidesp "Nope. Speaking of, I've actually got to head out now."
    asidesh "Besides, I don't think I could sleep even if I tried. My mind keeps running at a million miles a minute. I might as well be productive."
    
    hide Qwynn_N3 with dissolve
    
    asideem "(Or maybe it isn't just my mind. Maybe it's the way my chest feels lighter whenever I think about Felix's card, waiting in my bag... as silly as that sounds.)"
    asideb "(And Felix. I can picture him so clearly. The way his locs catch the light when he pulls them back, or the way his overalls are always stained with colors I can't name.)" 
    asideeb "(He looks like he carries a piece of the sun with him.)"
    
    show Qwynn_N3 at half_size
    with dissolve
    
    q "Uh huh. You know you're gonna crash later."
    asidee "Oh absolutely! But I've decided that's a future Astra problem!"
    "Qwynn sighs fondly, shaking their head and pushing my notebook back towards me."

    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve

    q "What am I gonna do with you?"
    aside "I'll be fine!"
    "Their tail swishes low behind them, brushing the floor, but they give me a smile of encouragement."

    hide Qwynn_S with dissolve

    "I down the rest of my coffee and stand up, but not without also grabbing my notes—which I make sure to toss into my work bag."
    asidesp "Okay! I'm off!"
    "With all of my things gathered, I walk straight to the front door and turn the handle. I hear Qwynn call out to me just as I take the first step outside." 
    q "At least eat breakfast when you get there!"
    aside "I will!" 
    "Caffeine runs through my veins, filling me with enough vigor to tackle the day ahead."

    #MR. Ellwood

    scene cafe_interior with dissolve
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg"

    "Today, it's just Sylphia and I." 
    "Customers flow steadily into the café. Never really too busy or too crowded. A nice middleground." 
    "Off to the side, Sylphia sits with a business advisor discussing my proposal for the café."
    asidea2 "(I wish I could hear them better.)"
    "Over time, I've gotten used to making coffee to the point that I don't have to think too hard about it. Right now, I'm using those hard earned skills to multitask and listen in on Sylphia's conversation."
    "Not that I plan to make a habit of eavesdropping, but it's times like these where I envy Qwynn and Velvet's sensitive hearing."
   
    show Sylphia with dissolve
   
    s "Astra?"
    asidesp2 "Yes?"
    "She smiles."
    s "When you have a second, why don't you come join us?"
    asidee2 "Really?!"
    "I clear my throat."
    asideb2 "Yes, of course. I'll be there in a moment."

    hide Sylphia with dissolve

    "Right now, I've got to finish this customer's order. I pour milk into the cup carefully to create my signature flower before finally serving it to the waiting customer."

    show latte1 with moveinbottom

    "After I finish, I head to their table." 

    hide latte1 with moveoutright

    "Stifly, I seat myself next to Sylphia. There's a rigidity to my movements that I can't quite shake."

    show Sylphia with dissolve

    s "Mr. Ellwood, this is Astra. She's the one who'll be managing this project alongside me. When I'm not around, she'll be your point of contact." 

    hide Sylphia with dissolve 
 
    aside2 "Nice to meet you, sir. I look forward to working with you." 
    e "As do I. Now, back to what we were discussing before…"
    e "A word of caution... I think that we should consider reevaluating the scope of this project."
    e "The proposal certainly {i}sounds{/i} wonderful, but I worry about what we risk in making so many changes at once."
    asidesa2 "(I understand the logic… but how are we supposed to transform anything without taking risks?)" 
    e "I suggest removing the part that requires renovation. The upstairs area for community events, and the mural."
    e "Just the addition of a rotating gallery is enough to put a fresh coat of paint on things." 

    menu:

        "Keep quiet, and listen.":
            asidesa2 "(Maybe he's right.)"
            "I should probably listen to the professional."  
            "Sylphia pauses, as if waiting for something. When neither me nor Mr. Ellwood speak, Sylphia fills the gap."
            show Sylphia with dissolve
            s "We're going for a full transformation here."
            s "Let's continue with the plan as is. If something comes up later, then we can discuss cutting it down."

        "Bring up concerns.":
            $ felix_pts += 10
            show screen choice_indicator(FELIX_COLOR)
            asidea2 "(We have to take risks in order to grow.)"
            asidesp2 "Excuse me? Mr. Ellwood?"
            e "Yes?"
            aside2 "Concerning what you just said… I think we should aim to make all the changes originally listed in the proposal."
            "He looks to Sylphia, defaulting to her seniority over mine. However, Sylphia only gestures between him and myself."
            e "Are you sure? It's quite ambitious."
            asidesp2 "I'm positive. The goal is to create something brand new, something that builds on our foundations. I feel that reducing the scope would leave this project feeling half-baked."
            "Sylphia nods. And, is that... pride on her face?"
            aside2 "(It's hard to tell with her.)"
            show Sylphia with dissolve            
            s "I agree with Astra. Let's continue with the plan as is. If something comes up later, then we can discuss cutting it down."
    
    hide Sylphia with dissolve

    "With a course of action decided, the rest of our talk goes smoothly. I leave with a mountain of new work to tackle." 
    "Meetings with suppliers, artists, and designers see my schedule packed with things to do."
    "But at the edges of my mind is a wave building, threatening to overwhelm me."
    asidea2 "(This is no time to be anxious… I can do this.)"

    #WAITING

    aside2 "(There's only one more task for today.)"
    asidesa2 "(...)"
    asidesh2 "(My heart keeps stuttering. Too much coffee?)"
    "I pull my timepiece out from my apron, smoothing my thumb across the glass."
    asidesh2 "(One more hour. Maybe I could ask to leave early?)"
    asidesa2 "(…)"
   
    show Sylphia with dissolve    
  
    s "You seem distracted. What's on your mind?"

    hide Sylphia with dissolve

    menu:

        "Ask to leave early.":
            $ felix_pts += 10
            show screen choice_indicator(FELIX_COLOR)
            aside2 "Actually, I was wondering if I could leave early? I set up a meeting for this afternoon."
            show Sylphia with dissolve
            s "Oh? I was actually about to suggest the same myself. I figured it might be something like that."
            s "Of course you can leave early. I can take care of things here. Consider it part of your shift."
        "Don't risk it.":
            asidesa2 "(I'm on the schedule for one more hour. I should just stay.)"
            "Next to me, Sylphia appears quietly. I flinch— but only slightly and I turn to face her fully."
            show Sylphia with dissolve
            aside2 "When I leave today, I'm going to reach out to my contact to discuss partnering with us."
            s "Oh? How exciting!"
            s "You know, if you need to leave early to work on the proposal, all you have to do is let me know."
            s "In fact, if you like, you can go ahead and leave now. I can take care of things here. Consider it part of your shift."

    asidesp2 "Really? Are you sure?" 
    s "I insist." 
    s "Work you do on the outside of the café—is still work."
    s "Now, go on."

    hide Sylphia with dissolve

    "Before I can think it over further, Sylphia is already ushering me towards the break room."

    show cafe_interior:
        zoom 1.5
        xoffset -400
        yoffset 300
    
    asidesp2 "(Wait. Now? Already? I thought I'd have more time to… to prepare myself.)"
    asideem2 "(What if he isn't there? What if he {i}is{/i} there? What if I say something ridiculous?)"

    show cafe_interior:
        zoom 1.8
        xoffset -500
        yoffset 400

    asidesh2 "(Oh Saints, what if he doesn't even remember giving me his card…?)"
    asidesa2 "(No—stop it. This is just… work. That's all it is.)"
    asidesh2 "(And… since Sylphia herself suggested it…)"
    aside2 "I {i}guess{/i} it won't hurt to get it out of the way."
    "Still pushing me along, Sylphia laughs."

    show Sylphia with dissolve

    s "Exactly, don't worry about the café. I think I'll manage."
    "After removing my apron and grabbing my belongings, Sylphia follows me to the front door."

    scene cafe_interior with dissolve

    asidep "(What if he says no? Then what?)"
    asideem "(My heart won't slow down. Why does it feel like I'm about to walk into something completely different from work?)"
    asidesp "Maybe I should just stay here. What if there's a rush while I'm out?"

    show Sylphia with dissolve   

    s "{i}Go{/i} Astra, stop stalling. What do you think is gonna happen?"
    "I could think of numerous things that could happen, but I choose to keep those thoughts to myself."
    asidep "…Right. Okay."
    s "You're just standing by the door."
    asidesh "I'm just—bracing myself for the cold."
    s "…It's not cold."
    asideeb "Fine, you caught me… I'm going." 
    asidesp "…Thanks for covering for me!"
    s "Yes, yes, you're very welcome. Bye now~"
    asidesp "Bye!"

    hide Sylphia with dissolve
    stop ambient fadeout 2.0
    scene market with dissolve

    play music "city_day.ogg" fadeout 2.0 fadein 2.0

    "As I step out, the air hits my face. It's not cold, but certainly sharp enough to make me reactively take in a breath." 
    "My pulse refuses to settle. Every step forward feels like I'm ticking down the clock on a timer, quickening with each breath."

    #Afternoon	

    "One hour later, I've made it to Block 2. Located on the corner, Studio Alizeti stands out with its bright green door and windows adorned with sunflowers." 
    "It's hard to miss among the other shops lining the street."
    "The studio's name is painted boldly onto the window and an open sign hangs invitingly on the front door."

    show studio with dissolve
    play audio "<from 0 to 3>bell.mp3"

   
    #possible CG here

    play music "Felix.ogg" fadeout 2.0 fadein 2.0

    "Inside, it's cluttered, but in a way that feels alive. Canvases lean against walls in uneven rows, brushes rest in cloudy jars of water, and paint-streaked tarps cover the floor." 
    "There's barely enough space to walk, but somehow it doesn't feel suffocating. It kind of feels like stepping into a thought, however vague that might sound."
    "There is one clear spot however, a small seating area tucked by the front window—assumedly for clients and consultations. It's awash in sunlight."
    "Bathed in that light, Felix lounges on a couch with a sketchbook open across his lap. He taps a pencil against his lips absentmindedly, eyes unfocused, like he's a million miles away."
    "He doesn't look up, and he gives no indication that he's noticed me slip in." 
    "I think back to last week, when Felix startled me at the market, and an idea starts to form."

    menu:

        "Sneak up on him.":
            $ felix_pts += 10
            show screen choice_indicator(FELIX_COLOR)
            asidesm "(Payback time.)"

            jump sneak
        "Call out to him.":
            asidesh "(I probably shouldn't scare him on purpose.)"
            jump dont_sneak


    label sneak:
        
    "I tiptoe forward, careful not to let my shoes squeak against the paint-streaked floor."
    "…"
    "…"
    aside "(Almost there…)"
    "I take a breath, readying myself to scare him—"
    "—when his head suddenly lifts, dark eyes locking onto mine."
    "Caught."

    show fcutin2 with easeinleft

    f "Oh hey! How long have you been standing there?"

    hide fcutin2 with easeoutright

    asidep "…"
    "His eyebrows rise in amusement as a grin spreads across his face, and he tilts his head to the side."

    show Felix with dissolve

    f "…What?"
    asidep "...Nothing. "
    f "…Were you trying to scare me?"
    asideeb "N—no. ‘Course not. W—why would I do that?"
    f "Uh huh. Well, {i}if{/i} you were trying to scare me, you'll have to do better than that." 
    asidesm "Keyword 'if'." 
    f "Whatever you say." 
    "Felix sits up on the couch properly, setting his sketchbook down on the table in front of him as he does so. With his free hand, he gestures towards the seat opposite his own."

    jump felix_choice1

    label dont_sneak:
    "I make it a point not to quiet my steps when approaching Felix. Sure enough, he looks up from his sketchbook and his eyebrows raise in surprise."
    
    show Felix with dissolve
    
    f "Oh hey! What are you doing here?"

    #BRANCHES CONVERGE HERE

    label felix_choice1:
        
    f "Please, have a seat. Sorry, I didn't greet you when you came in."
    f "What can I do for you?" 

    hide Felix with dissolve

    "I sit across from him, crossing my legs, trying anything to get the least bit comfortable. Unfortunately, no amount of shifting seems to settle my nerves."
    asidesa "(I'm just stalling…)"
    "In his seat, Felix sits waiting patiently. He's leaning forward, elbows resting on his knees. The sunlight catches in his locs, turning them the color of polished copper." 
    aside "Last week, you said you'd be open to displaying your work in other places."
    aside "Is that still true?"
    "A flicker of recognition sparks in his eyes. His lips curve, thoughtful."

    show Felix with dissolve

    f "If I remember correctly, I said I {i}might{/i} be interested in it. But you've got my attention. So... what exactly are you asking?"
    asidesh "(Great start Astra…)"

    hide Felix with dissolve

    asidesh "Right, sorry, I guess I should start at the beginning." 
    aside "I work at a café. Café Bloom. Recently, we decided to 'spice things up' by adding a rotating artists gallery and a community space." 
    asidesh "It's my job to manage the project, and… I thought your work would look beautiful there."
    "My fingers twist in my lap, and I uncross my legs, only to cross them again."
    aside "I want you to be our first feature artist... and to paint a mural."
    asideem "(My throat's drying up.)"
    "Felix doesn't answer right away. Instead, he watches me with an arched brow, a laugh tugging at the corner of his mouth."
   
    show Felix with dissolve  
   
    f "You always this fidgety, or do I just make you nervous?"
    asidesp "W—what?! I'm not—! I mean—this is just important, that's all!"
    f "Mhm. Important. Got it." 
    "He smiles, tapping his pencil against his knee." 
    f "For the record, I don't bite."
    asideeb "(Oh saints, he's teasing me. And worse— I think I'm blushing.)"
    "Finally, he leans back, gaze softening as he regards me more seriously. He begins to tap his pencil against the table softly." 
    f "I think that's a great idea! Honestly, I've never seen a café in Halis with a concept like that."
    f "I'd love to help, truly."
    asidee "Really?!"
    f "Really, really."
    "Without being able to stop myself, I leap up from my seat. My palms meet the table between us and I lean towards Felix in excitement." 
    asidee "I can't believe you said yes! I was so nervous."

    hide Felix 
    show Felix_E 
    with dissolve

    "Felix blinks at me, then laughs softly, pencil still balanced between his fingers."
    f "I know I'm the one who said you should come to me if you needed art, but— I don't know, I guess I didn't {i}actually{/i} expect you to come by."

    hide Felix_E
    show Felix_N2
    with dissolve

    f "...But I'm glad you did."
    "The corners of my mouth turn up into an involuntary smile."
    asidesm "I {i}said{/i} I'd see you around."
    "His gaze lingers on me for a moment, warm and intent."

    hide Felix_N2
    show Felix
    with dissolve

    f "Yeah…you did."
    "The silence between us stretches, the tension growing. When Felix finally breaks it, it's with a small clearing of his throat, seemingly grounding himself again."

    hide Felix 
    show Felix_E 
    with dissolve

    f "S-so, what do you need from me?"
    aside "Why don't we set up a meeting? Now that I have you on board, I can work on brainstorming some more ideas. Maybe a few days from now would be good?"
    "Felix nods, picking up his sketchbook and flipping it open to a blank page. He scribbles down a few basic notes, speaking up again while he writes."

    hide Felix_E
    show Felix_N2
    with dissolve

    f "…We should set up a meeting at the café—if you don't mind. I'd like to see the space myself."
    "His voice is light, but there's a flicker of hesitation in his eyes, as if expecting to be turned down before I've said anything."
    asidesp "Of course!"
    f "Hmmm, alright, gimme a sec."

    hide Felix_N2 with easeoutleft

    "He rises, moving with careful ease through the jumble of canvases and paint cans, stepping around them expertly like he's walked this path a thousand times before."
    aside "(Practice makes perfect I guess.)"
    "Across the room, I can see Felix flipping through yet another notebook and mumbling to himself."
    "After a minute or two, he sits back down in front of me, holding the new notebook."
       
    show Felix with easeinleft

    f "How's this Tuesday? Looks like I have an opening around lunchtime. That sound okay?"
    asidesa "(Tuesday huh? I have another meeting that day, but it should be over by lunchtime… it should be fine... more than fine.)"
    asidesp "Absolutely! …Thanks for agreeing to help, Felix."
    f "Haha, you don't have to thank me for taking on a job y'know, but—you're welcome."
    "He flashes me a grin so bright, it nearly knocks the air from my lungs. He stretches out a hand towards me."
    f "Looking forward to working with you, Astra!"
    asideem "(Saints— that's lethal.)"

    hide Felix with dissolve

    "My heart pounds in my chest, so loud I'm afraid he might hear it."
    asideeb "(Maybe Qwynn was right. I think I {i}did{/i} have too much coffee this morning.)"
    "I shake Felix's hand. His grip is firm, and his palm is pleasantly warm… I have to suppress the shiver that threatens to run through me."
    asideb "...My pleasure!"

    play audio "<from 0 to 3>bell.mp3"

    "The sudden chime startles us both. Felix releases my hand quickly, an apologetic smile tugging at his lips."

    show Felix with dissolve 

    f "Ah, that would be my next client. Sorry Astra."
    aside "It's okay. I have a meeting with a supplier soon anyway, which I need to get ready for. Sorry for dropping by without notice."
    f "You're welcome anytime… See you Tuesday?"
    asidesp "Yeah, see you then! Bye Felix!"
    f "Bye Astra, be careful on your way back."
    asidesp "I will!"

    play audio "<from 0 to 3>bell.mp3"
    
    hide Felix with dissolve

    "I step out of Studio Alizeti with my heart still hammering and excitement bubbling in my chest." 
    
    show market_evening with dissolve

    asidesa "(Tuesday feels so far away. I wish it would come sooner.)"
   
    window hide
    show felix_pov with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    scene studio with squares
    
    "His eyes follow Astra as she walks out the door. Unconsciously, Felix's fingers start drumming against his thigh."
    fside "(…)"
    cli "Sir?" 
    "His focus snaps back to the client in front of him."
    fsideu "(Pay attention Felix.)" 
    "Felix lets a smile take over, trying to put himself back into work mode—something he feels guilty for even having to do."
    "His pencil hovers over the page, though, refusing to move. That spark she carried with her, the way she said his name…"
    "The feeling creeping in is one that he hasn't dared to let himself feel in a very long time. Still…"
    fside "(Astra's just another client, exactly like everyone else. You'll do the job, and then…)"
    fsidesad "(And then— go back to normal.)"
    fside "...Sorry about that, let's take a seat shall we?"


    window hide
    show astra_pov with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    scene market with squares
    play music "city_day.ogg" fadeout 2.0 fadein 2.0


    "Streams bubble through pathways underneath my feet, and the wind stirs a nearby windchime."
    "Today, I have yet another meeting. Though, this time with a potential supplier."
    aside "(They asked to meet somewhere around here...)"
    "I pull my pocket watch out."
    asidesp "(Oh! I'm 10 minutes early. Perfect.)"
    "I'm plenty caffeinated, ready for another full day. It does a great job at keeping me awake, though it helps that I'm still riding the high of Felix accepting my offer."

    scene vels2 with dissolve

    "Ten minutes later, the supplier walks in. Right on time."
    "I stand to meet her at the table."
    aside "Miss Verac. Thank you for meeting with me."
    ver "Pleased to meet you, Miss Vale~" 
  
    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "city_night.ogg" fadeout 2.0 fadein 2.0

    show vels2_night with dissolve
    "When the meeting is finally over, I let out a grand sigh. My body slumps back into my seat, drained."
    show black with wipedown
    asidep "(That was a lot more involved than I thought.)"


    who "Hello there~"
    asidesp "Ah—!"

    play sfx "sfx_shake.ogg"
    scene vels2_night with vpunch

    aside "(Wait... I recognize that voice.)"
    asidesp "Velvet? What are you doing here?"
    "They chuckle." 
   
    show Velvet with dissolve

    v "I should be the one asking you that. This is my restaurant."
    aside "Oh. Huh."

    hide Velvet with dissolve

    "The Were-fox sets a menu down in front of me with a self-satisfied grin. In big, bold letters, the word 'Vel's' is written across the top."     
    "I point at the menu indignantly, letting out a playful scoff."
    asidesm "This could be anyone."

    show Velvet with dissolve

    v "Sure, if that makes you feel better."
    asidesm "It does."
    v "I saw you come in earlier, but you seemed busy. A business meeting?"
    aside "Mhm. I'm managing a project for work. I had no idea this was your place. It was the client's request."
    v "Oh yeah. I thought I saw Juliet come in."
    aside "(Juilet. As in Juliet Verac)."
    asidesm "Do you know everyone in Halis?"
    "Velvet laughs, and then winks."
    v "Irrelevant."
    v "...I heard you hired Felix for your café's new venture? Tell me more."
    asidesp "Don't you have to work?"
    "They shrug."
    v "It's my place. Besides, it was almost time for my break anyways."
    aside "I guess I can't stop you then."
    v "How kind of you~"
    v "So you saw Alizeti, huh. It's a bit of a wreck in there, isn't it? You didn't trip on anything there did you?"
    asidesp "Surprisingly, no."
    v "I keep telling him that he should at least clear a path for clients, but, as you saw, that hasn't happened."
    aside "He seemed pretty used to it."
    v "Of course he did! He's been living there for over 7 years now, but I still think he could stand to organize."
    v "I tried to do it myself not so long ago, but it was back to square one within a week!"
    "Velvet laughs, and there's a fond smile on their face that shines even through the exasperation in his voice." 
    aside "How long have you known Felix?"
    v "Hmmm, a little over two years now? Feels like forever though."
    "He turns his attention to me, and smirks." 
    v "I'm happy he seems to have found a new friend… I don't think I've seen him so comfortable with another person since we met."

    hide Velvet with dissolve

    asidesa "(So Felix really doesn't have many friends. Even though he seems so sociable.)"
    asideb "Yeah. Me too."
    "Velvet and I chat intermittently until his break is over, about our jobs, the weather, and his finishing adventures."
    "After an hour, Velvet stands up from his seat."

    show Velvet with dissolve

    v "Time's up. Thanks for letting me chat, Astra! I'll see you around, yeah?" 
    asidesp "Definitely, thanks for the chat Vel!"
    
    hide Velvet with dissolve

    "They smile at the use of their nickname, waving to me as I leave the restaurant to begin heading back home."

    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0
    scene kitchen_night with dissolve

    aside "(I'm exhausted. But, that was a pleasant surprise.)"

#####################################
#THE MEETING
#####################################

    window hide
    scene black with dissolve
    window auto
    pause (2.0)

    scene cafe_interior with dissolve
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play ambient "sfx_cafenoise.ogg"

    "Tuesday comes with little fanfare. Miss Verac left a few minutes ago."
    "Right in time for yet another meeting."
    asidesh2 "(Though talking with Felix hardly feels like work.)" 
    aside2 "(It's almost noon. Felix should be arriving soon.)"
    "Someone clears their throat loudly behind me."

    show Albion_SC with dissolve

    al "Astra, are you done with that?"
    asidesp2 "Done with what?"
    al "The creamer."

    hide Albion_SC with dissolve

    "I glance down to see the container clenched tightly in my hand. I didn't even notice I was still holding it."
    "I blink, trying to focus."
    asideem2 "(Saints, get it together.)"
    asidesh2 "Right… Here you go."
    "Albion takes the creamer from me and turns to walk away. As he does, he turns his head to the side to say—" 
    
    show Albion_N2 with dissolve
    
    al "...Why don't you prepare for your meeting in the break room." 
 
    hide Albion_N2  with dissolve

    "I look up at him in surprise."
    asidee2 "(Is this Albion being considerate?)"
    aside2 "No, I couldn't leave you out here alone. I'm fine, promise."

    show Albion_SC with dissolve

    al "You're not exactly helping me out here. Just go."

    hide Albion_SC with dissolve

    asidesm2 "(…Ah. There's the Albion I know.)"
    asidesh2 "Alright, I'll get out of your hair then. Thanks."
    "Albion ignores me, already back to work, and I take that as my cue to slip away."

    stop ambient fadeout 3.0

    show cafe_interior:
        zoom 2.0
        xoffset 900
        yoffset 500
    with dissolve

    "In the break room I take the time to gather all my notes, but it isn't long before Albion is opening the door to let me know that Felix has arrived."

    play audio "<from 0 to 2>dooropenclose.mp3"

    show Albion_SC:
        zoom_in 

    
    with dissolve

    al "Some guy covered in paint just showed up." 
    "My traitorous heart skips a beat."
    aside "Thanks, Albion. I'll be out in a minute. Can you direct him to a table towards the back?"

    hide Albion_SC with dissolve

    play audio "<from 2 to 4>dooropenclose.mp3"

    "Once again, Albion doesn't respond. He simply nods and shuts the door." 
    asideem2  "(Calm down. It's just like every other meeting you've had this week.)"
    asideb2 "(...)"
    aside2 "(Alright, I think I've got everything prepared.)" 

    show cafe_interior:
        xcenter 0.5  
        ycenter 0.5
        zoom 2.0
        xoffset -900
        yoffset -60
    with dissolve

    play ambient "sfx_cafenoise.ogg"

    "Felix is sitting at a table in the back of the café. In front of him are a few pencils and a pair of sketchbooks."
    "I sit across from him, joining my own notebook and pencils with his."

    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "You know, it feels different seeing you here instead of running into you by chance."
    aside2 "Hope I didn't keep you waiting." 
    f "Nope! All good. Your coworker even gave me this coffee—on the house!"
    asidesp2 "Albion did?"
    f "Tall, quiet guy, right? Yeah. Didn't say much, though."
    asidesm2 "Huh, okay then. Seems like we're all set then."
    "I open my coffee-stained notebook and slide it towards him, pointing to a set of circled notes." 
    aside2 "The general idea is that we partner with different artists, highlighting various businesses around Halis."
    "Felix leans in, resting his chin on one hand as his eyes scan my messy handwriting. He hums in quiet acknowledgement, fingers tapping absently at the edge of his sketchbook."
   
    hide Felix
    show Felix_N2:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve
   
    f "How often will you be rotating artists? 'Cause I'd recommend doing it once a month. It'd be too difficult to bring in someone new every week."
    f "A month gives the artist plenty of time to have their work displayed, and it gives you guys here at the café time to plan events around them."
    aside2 "Oh, I see. That's a good point. I was thinking the more the better, but your idea makes more sense."

    hide Felix_N2
    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    "He chuckles, low and warm, and I feel it settle in my chest like sunlight."
    f "Better safe than sorry."
    "Felix gestures at the café wall, casual but deliberate."

    hide Felix
    show Felix_N2:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "And about displays—the location you wrote here is good, but it'll depend on the artist. Me, I keep most of my paintings out of direct sunlight. Otherwise they'll fade faster."
    asidesp2 "Huh… I didn't even think about that. So you're saying each artist should have input on their setup?"
    aside2 "...Could you make a more detailed list of requirements by our next meeting? I'd like to use it as reference material for when I finally track down a contractor."
    f "Sure I can, but… You're really going all out aren't you."
    asidesp2 "Of course I am! What's the point in doing this if I don't give it my all?"
    f "You're not wrong."
    aside2 "But?"

    hide Felix_N2
    show Felix_C:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "...It's just risky. That's all."
    asidea2 "(This again.)"
    aside2 "Life is risky."
    "Felix sucks in a sharp breath."

    hide Felix_C
    show Felix_U:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "Exactly."

    hide Felix_U with dissolve

    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0
    show cafe_interior_evening:
        xcenter 0.5  
        ycenter 0.5
        zoom 2.0
        xoffset -900
        yoffset -60
    with dissolve

    "Our talk continues like this for the next hour or so, ideas scribbled between us in pencil and ink. Eventually, out of habit, I reach for the coffee on the table and take a sip."
    asidesp2 "(...Woah, that's sweet.)"
    asidesa2 "(...Sweet?)"
    "My brows furrow. This isn't mine. I glance up and find Felix watching me, his mouth twitching as he tries—and fails—to smother a laugh behind his hand."

    show fcutin with easeinleft
        
    f "By all means, help yourself." 
    "My face heats up immediately, across my cheeks and spreads outwards towards my ears."
    asidesp2 "...This is yours."
    f "Sure is."

    hide fcutin with easeoutright

    "Face aflame, I shove the glass back towards him."
    asideem2 "...It's {i}so{/i} sweet. I can't even tell what it's supposed to be."

    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve
    
    f "Oh I have no idea, I just asked for the sweetest thing you guys could make."
    "My eyes track his movements as Felix reaches for the glass and takes a sip. Uncaring that I had put my mouth on it."
    asideem2 "(...)"
    f "It's delicious."
    asideeb2 "...If you say so."

    hide Felix with dissolve

    "The silence between us buzzes with something unspoken until I tear my gaze back to my notebook, desperate to smother the warmth in my chest with something more practical."
    aside2 "I think that just about covers everything for today. I'll consult with the owner about what we discussed, and then we can set up another meeting."
    aside2 "If that sounds alright for you."

    show Felix:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    f "Sure, when do you want to meet?" 
    aside2 "...Friday? That would be enough time for me to talk to Sylphia."

    hide Felix
    show Felix_N2:
        zoom 1.7
        yoffset -100
        xoffset 350
    with dissolve

    "Felix opens his notebook, scanning the pages intently."
    f "We can do Friday, but can you come to the studio? I'm a little tight on time that day."
    aside2 "I think that's only fair."
    "The two of us stand and begin walking to the door." 

    scene cafe_interior_evening with dissolve

    hide Felix_N2
    show Felix
    with dissolve

    f "Great! Then, I'll see you Friday. Anytime is fine. I'll just be working on some paintings."
    "His grin is easy, but there's a glint in his eyes that makes my chest flutter."
    asideb2 "See you Friday."
    f "Be safe out there!"
    asidesp2 "Sure thing! Bye, Felix!"
    f "Bye, Astra."

    hide Felix with dissolve
    show cafe_interior_evening with dissolve
    play audio "<from 0 to 3>bell.mp3"

    "The bell jingles as Felix pushes the door open. For a moment, the setting sun's light spills in behind him, outlining him in gold before he steps outside." 
    "The sound of the door shutting feels louder than it should, final and soft all at once."
    "My hands play with the ties of my apron, untying and re-tying the ribbon as I stare at the door that Felix disappeared through." 
    asideb2 "(Just like every other meeting...)"

    stop music fadeout 6.0
    scene cafe_interior_evening with dissolve
    show Albion_SC with easeinright


    al "Astra. Work's not over."
    "Albion's voice jolts me back to reality."

    play sfx "sfx_shake.ogg"
    show cafe_interior_evening with vpunch

    asidesp2 "Sorry! Just… thinking about what we discussed."
    al "...Whatever. Come help me clean up."
    asidesp2 "Alright, alright. I'm coming. Gosh, you're such a grump." 

    stop ambient fadeout 3.0

    hide Albion_SC with dissolve

    jump Felix_chp2

#transition to the next scene/chapter 2











