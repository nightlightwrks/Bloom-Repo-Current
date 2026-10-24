# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



#########################################
# QWYNN CHAPTER 1 
#########################################

label Qwynn_chp1:
  
    window hide
    show black with dissolve
    window auto
    pause (2.0)

    $ persistent.status_button = True
    
    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0
    scene kitchen with dissolve

    asidesp "Hey, Qwynn, I have a question for you."
    
    show qcutin2 with easeinleft

    q "Anything for you!"

    hide qcutin2 with easeoutright

    "I can't help but grin. Such a Qwynn thing to say. Always cheerful, always ready to help."
    asidesp "We need to do some marketing at Bloom. Since you have your own boutique, I was wondering how you managed to get its name out there."
    
    show Qwynn_S at half_size with dissolve
    
    q "Oh, marketing! Fun one. Well... when I first opened, we didn't really have the funds for conventional marketing. I had to get creative."
    asidesp "Creative how?"
    q "I started simple." 
    q "I made sketches of our window displays and convinced a local printing press to make lots of copies to hand out, hosted a few pop-ups, and handed out free tea samples with the boutique's name on them."
    q "Oh, and I made {i}sure{/i} to talk to everyone who stopped by. Word of mouth travels fast when people like you."
   
    hide Qwynn_S with dissolve
   
    asidesh "(I do remember Qwynn being really busy around that time.)"
    "Disappearing at odd hours and hauling in more boxes than usual. I was so busy with Café Bloom then, that I guess I didn't notice."
    aside "So... you're really just marketing yourself?"
   
    show Qwynn_S at half_size with dissolve   
   
    q "I guess so! You don't just sell things. You sell emotions – the {i}feeling{/i} behind them... And people certainly remember the warmth of a smiling face."

    hide Qwynn_S
    show Qwynn_N3 at half_size 
    with dissolve

    q "Basically, people are more inclined to buy stuff from someone they like."
    "I write that down, even though I'm not sure how I'm supposed to apply it. Qwynn makes it sound easy. Maybe that confidence is their secret."
    asidesp "It clearly worked for you. Everyone knows your boutique."

    hide Qwynn_N3
    show Qwynn_S at half_size 
    with dissolve

    q "Heh. Maybe. But it wasn't just about the shop. It's about connection."
    "I look up from my notes. Qwynn is staring out the window, eyes soft and distant."
    aside "It sounds like it means a lot to you."
    
    hide Qwynn_S
    show Qwynn_M at half_size 
    with dissolve
    
    q "It does. The boutique's kind of... me, in a way."

    hide Qwynn_M with dissolve

    "I nod. I know what that feels like. Bloom is my piece of the world too."
    asidee "Maybe that's what we need: more heart."

    show Qwynn_S at half_size with dissolve   
   
    q "Exactly! And hey, if you want, I can help. We can brainstorm together!"
    asidesp "You'd really do that? Don't you have work?"
    q "Of course I have work, but I can always make time. You're my best friend!"
    "I smile. The way they say it, so casually, like it's obvious, makes my chest flutter just a little."
   
    hide Qwynn_S with dissolve
   
    asideb "(You're my best friend.)"
    "Those words take me back to where it all started."

    #CHAPTER 1: PAST 
    window hide
    show qwynn_chp1 with squares
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    scene vels 
    show voiced
    with squares

    "I met Qwynn a year out of school. I had just gotten a job at a popular chain restaurant as a waitress—my first job ever."
    "The restaurant smelt like grease and coffee that's been reheated too many times. It wasn't exactly the dream job, but it paid the bills."
    "COWORKER" "Can you please serve Table 4?"
    
    voice "<from 1 to 4>audio/astra/astra_qwynn.ogg"
    asidesp2 "Ah! Yes! Coming!"
    "The plates rattled on my tray as I hurried across the floor. My shoes squeaked against the tiles, and my smile felt too tight."
    "CUSTOMER" "Took you long enough!"
    "I bowed quickly, muttered an apology, and set the dishes down. They didn't look at me."
    asidesh2 "(No one really does here. Most customers just want to eat and leave. It's okay. I don't mind. I don't mind...)"
    who "Customer giving you a hard time?"
    asidesp2 "(Huh? Who's this?)"
   
    show Qwynn_S at half_size with dissolve

    voice "<from 4 to 8.4>audio/qwynn/qwynn_1.ogg"
    q "I'm Qwynn. I was on leave for a bit, but I'm finally back. Are you the new girl?"
    
    voice "<from 13 to 15>audio/astra/astra_qwynn.ogg"
    asidesp2 "Yes! I'm Astra!"
    voice "<from 9 to 15.4>audio/qwynn/qwynn_1.ogg"
    q "They didn't train you properly, did they? You're not even holding the plates right. Here, do it like this!"
    
    show Qwynn_S at half_size:
        zoom 1.5
        xpos 350
        ypos -200
    with dissolve

    "Qwynn stepped closer, carefully adjusting the tray in my hands. Their movements looked confident."
    "The tray steadied instantly, and for the first time all day, I didn't feel like I was about to drop something."

    voice "<from 16.5 to 20>audio/astra/astra_qwynn.ogg"
    asidee2 "Oh... that actually helps."
   
    hide Qwynn_S
    show Qwynn_S at half_size
    with dissolve

    voice "<from 21 to 25>audio/qwynn/qwynn_1.ogg"
    q "Told ya. I've been here for a few months now. I could balance three trays if I wanted to."

    voice "<from 30.6 to 34.5>audio/astra/astra_qwynn.ogg"
    asidesm2 "Three? That sounds impossible."
    voice "<from 31 to 32.8>audio/qwynn/qwynn_1.ogg"
    q "Maybe... but you'll get there."
    "Their grin was so easy and natural that I found myself smiling back. I didn't even really know them yet, but something about their presence felt like a calm in the noise."

    hide Qwynn_S with dissolve

    "Later that afternoon, I found Qwynn in the breakroom, sitting on the counter and humming softly as they counted their tips."
    voice "<from 38.6 to 41>audio/astra/astra_qwynn.ogg"
    asidee2 "You're really good at this."
  
    show Qwynn_N3 at half_size with dissolve
  
    voice "<from 36 to 38.6>audio/qwynn/qwynn_1.ogg"
    q "Thank my reflexes. I {i}am{/i} Were-folk."
    "That's right. Were-folk are more attuned to physical skills like strength and speed." 
   
    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve    

    voice "<from 41.3 to 46>audio/qwynn/qwynn_1.ogg"
    q "But it's not what I want to do forever. I'm saving up to open my own boutique someday."
    voice "<from 44 to 45>audio/astra/astra_qwynn.ogg"
    asidesp2 "A boutique?"
    voice "<from 52 to 63.5>audio/qwynn/qwynn_1.ogg"
    q "Yeah. Not just clothes, but all kinds of things! Handmade things, teas, little trinkets, the works! I want it to feel like you're walking into a memory. Really drum up the nostalgia."
    "I could almost see it: shelves lined with glass jars and soft colors, the air filled with the smell of tea and wood polish."
    voice "<from 50 to 52>audio/astra/astra_qwynn.ogg"
    asidee2 "That sounds nice."
    voice "<from 79 to 81>audio/qwynn/qwynn_1.ogg"
    q "It will be, Aste. You'll see."
    "That was the first time I believed someone could build something just because they cared enough to try. And somehow, that belief started to take root in me too."

    hide Qwynn_S with dissolve
    
    window hide
    show black with dissolve
    window auto
    pause (2.0)

    #change music
    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0
    scene vels_evening 
    show voiced
    with dissolve

    "The next evening, the dinner rush hit us hard. The air smelled like oil and burnt toast, and the kitchen buzzed with the sound of clattering pans and shouting orders. I could barely keep up."
    "I mixed up two orders and forgot to refill a drink at Table 7. By the time I realized, it was already too late."
    "MANAGER" "Astra! What's going on? That table's been waiting for twenty minutes!"
    voice "<from 57 to 61>audio/astra/astra_qwynn.ogg"
    asidesh2 "I'm sorry! I thought I—"
    "MANAGER" "You thought? No, no, no, you need to KNOW. We can't afford mistakes during peak hours. Get it together, or I'll have to have someone else take your section."
    "My throat went dry. I nodded, biting back another apology that probably wouldn't have helped anyway."
    "Then Qwynn appeared beside me, holding a tray of drinks and flashing that trademark easy smile."
   
    show Qwynn_S at half_size with dissolve   

    voice "<from 88.1 to 96>audio/qwynn/qwynn_1.ogg"
    q "Hey, sorry about the delay, boss. That one's on me. I told Astra to grab the side orders while I handled the mains. Guess I mixed up the timing."
    "Qwynn's tone was calm, but confident enough to sound believable. The manager blinked, thrown off for a moment."

    #play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0  
  
    "MANAGER" "...You did?"
    voice "<from 96 to 102.6>audio/qwynn/qwynn_1.ogg"
    q "Yeah. My bad. But the customers are fine now. I already checked in and offered them a free dessert. You know how the regulars love that chocolate mousse."
    "The manager's expression softened just a little. I watched him sigh and wave it off."
    "MANAGER" "Fine. But those free desserts are coming out of your pay."
    voice "<from 113.5 to 116>audio/qwynn/qwynn_1.ogg"
    q "Of course. Thanks for understanding."
    "As soon as the manager walked away, I exhaled a breath I didn't realize I was holding."
    voice "<from 61 to 66>audio/astra/astra_qwynn.ogg"
    asidesh2 "You didn't have to do that."
    voice "<from 117 to 122.8>audio/qwynn/qwynn_1.ogg"
    q "Do what? Save a coworker from being scolded to death? Consider it a team effort."
    "I tried to frown, but my relief must have been a bit too obvious because Qwynn just grinned wider."
    voice "<from 72 to 75>audio/astra/astra_qwynn.ogg"
    asideb2 "Still... thank you."
    voice "<from 136.5 to 146>audio/qwynn/qwynn_1.ogg"
    q "Hey, I can handle the manager. He just needs someone to talk to him nicely. A smile and a few kind words go a long way."
    "They said it so easily, like it was second nature. Maybe it was. Qwynn had a way of softening people, of turning tension into something almost gentle."
    voice "<from 80 to 82>audio/astra/astra_qwynn.ogg"
    aside2 "You're really good at that."

    hide Qwynn_S
    show Qwynn_N3 at half_size
    with dissolve  

    voice "<from 148.6 to 150.5>audio/qwynn/qwynn_1.ogg"
    q "What, lying?"
    voice "<from 86 to 89>audio/astra/astra_qwynn.ogg"
    asidesh2 "I was going to say 'diffusing.'"

    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve   

    voice "<from 150.6 to 152>audio/qwynn/qwynn_1.ogg"
    q "Two sides of the same coin."
   
    hide Qwynn_S with dissolve
   
    "I laughed before I could stop myself. The sound got lost under the bustle of the restaurant, but for a moment, it didn't matter. The weight in my chest was lifted. That night, I went home tired, but not defeated."
   
    window hide
    show black with dissolve
    window auto
    pause (2.0)

    scene vels_night with dissolve
    #play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0  

    "Qwynn and I grew closer during our time at the restaurant."
    "They became my unofficial mentor, the person who taught me the difference between surviving a shift and somewhat enjoying it."
    "Being the only Were-folk on the waitstaff team, Qwynn was stronger and faster than all of our coworkers. And they used their speed to their advantage—a lot."
    "Whenever things got chaotic, Qwynn always seemed to know what to do." 
    "If the fryer broke, they'd joke about starting a campfire in the kitchen. If a customer complained, they'd swoop in with a charm that could turn irritation into laughter in seconds."
    "Their presence made the long hours lighter somehow."
    "On slow days, we'd stack napkins into elaborate towers behind the counter, betting on whose would collapse first before the manager noticed. Qwynn always won, claiming it was 'architectural talent.'"
    "We shared fries when no one was looking, scribbled doodles on order slips, and took turns sneaking out early for fresh air in the alley behind the building."
    "The job was still exhausting, but with Qwynn around, it started to feel less like a grind and more like... something we were surviving together."
    "Outside of work, we began hanging out more often: grabbing late-night ice cream after closing (Qwynn loved anything full of dairy) or sitting by the river and talking about anything that wasn't restaurant related."
    "Sometimes we didn't talk at all. We just sat there, listening to the hum of the Halis. It felt easy."
    "Qwynn had this way of making the ordinary feel like a break from everything else."

    scene vels_evening with dissolve

    "One evening, after a long shift, we were sitting in the breakroom eating cold fries from a takeout box when Qwynn mentioned it in passing."
    
    show Qwynn at half_size
    with dissolve       
        
    q "My housemate's moving out next month."
    asidesp2 "Oh? That's soon."

    hide Qwynn
    show Qwynn_M at half_size
    with dissolve

    q "Yeah. They got a job out of town. Which is great for them, but not so great for me. Rent's a nightmare on my own. Not to mention, I'm trying to save up for my boutique!"
    "They frowned at the fries like they were the ones responsible for their situation."
    q "Guess I'll have to start looking for a new housemate. But Aste... it's hard. You never know what kind of person you'll end up living with."
    aside2 "...What if it was me?"
 
    hide Qwynn_M
    show Qwynn_N3 at half_size
    with dissolve

    q "Huh?"
    asidesh2 "I mean, we already get along. And I've been thinking about moving out anyway. My parents want to retire and settle in the outskirts. The timing is perfect!"
    "There was a brief pause. Then Qwynn's face lit up like someone had just told them the best news of their life."
  
    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve
  
    q "You'd move in with me?"
    asidesp2 "Sure! Why not?"
    "Before I could say anything else, they jumped up from their chair and threw their arms around me."

    hide Qwynn_S
    show Qwynn_S at half_size:
        zoom 1.5
        xpos 350
        ypos -200
    with dissolve
   
    q "Astra, you're the best! I promise, I'll keep the place spotless, and you can have the bigger room, and—"
    asideeb2 "Okay, okay! We'll figure it out later."

    hide Qwynn_S
    show Qwynn_S at half_size 
    with dissolve   

    "They pulled back, still grinning from ear to ear. Their joy was so genuine, so open, that it was hard not to catch a little of it myself."
   
    hide Qwynn_S with dissolve

    "That was how we ended up deciding to live together."

    #[A FEW WEEKS LATER]
    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "Qwynn.ogg" fadeout 2.0 fadein 2.0
    scene kitchen with dissolve

    aside "...That's a lot of stuff."

    show Qwynn_S at half_size with dissolve

    q "Of course! But most of it's for the boutique! I swear, I'll keep it out of your way."
    
    hide Qwynn_S with dissolve
    
    "Moving day was chaos. Cardboard boxes everywhere, half-labeled and stacked like a miniature city. The smell of fresh paint still lingered in the air."
    "We found the apartment through a small poster advertisement: ‘a cozy place that isn't fancy, but it'll be yours!'"
    "I raised an eyebrow as Qwynn pulled out another box labeled {i}Fabric: Misc (Do Not Ask){/i}."
    asidesm "How many 'misc' boxes do you have?"

    show Qwynn_N3 at half_size with dissolve

    q "...Define 'many.'"
    asidesm "Anything over three."

    hide Qwynn_N3 
    show Qwynn_S at half_size 
    with dissolve

    q "Then none at all!"

    play sfx "sfx_shake.ogg"
    hide Qwynn_S 

    "They grinned, setting the box down in the corner before graciously tripping over another one."
    asidesp "Careful!"

    show Qwynn_S at half_size

    q "I meant to do that."
    asidesm "Sure you did."
    "They crouched beside a heavier box and tore the tape open, pulling out something wrapped in old towels. A moment later, they set a shiny espresso machine onto the counter with a soft thunk."
    asidesp "You like coffee?"

    hide Qwynn_S 
    show Qwynn_N3 at half_size 
    with dissolve

    q "Hmm? Oh, not really. It's from my parents. Looked too expensive to just chuck out."
    "They shrugged, placing it on the counter  and dusting it off like it was just another piece of clutter."

    hide Qwynn_N3 with dissolve

    aside "Well, maybe we can get some use out of it."
    "They shot me a playful glare, then sat cross-legged on the floor, tugging at the tape on a box of mugs."
   
    show Qwynn_S at half_size 
    with dissolve

    q "Oh, look! I forgot I had these."
    aside "You forgot about mugs?"
    q "Not just any mugs. These have personality."
    "They held one up: a chipped blue one with a faded smiley face."
    asidesm "That one looks like it's been through a lot."
    q "It has. It survived three moves and one very dramatic sink accident."
    asidesm "Aren't you supposed to have good reflexes?"
    q "I'll take that as a compliment."

    hide Qwynn_S with dissolve

    "We spent the rest of the afternoon unpacking like that. We traded jokes, compared the strangest items we owned, and tried to decide whose taste in décor was worse."

    scene kitchen_evening with dissolve
    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0

    "By the time we were done, the apartment looked halfway like a home. Our boxes were still open, but the place felt... lived in."
    "Qwynn flopped onto the couch, letting out an exaggerated sigh."
    
    show Qwynn_N3 at half_size with dissolve 

    q "You know, I think we did pretty good."
    aside "We did okay."

    hide Qwynn_N3 
    show Qwynn_S at half_size 
    with dissolve

    q "Oh, come on, admit it's perfect."
    asidesm "It's mostly perfect."
    q "I'll take it."
    "Their laughter filled the room. For a second, I forgot about the exhaustion settling in my arms."
    "They turned to me, still smiling."
    q "I'm really glad you moved in, Astra. You make this place feel real, somehow."
    asideb "That's sweet of you to say."
    q "No, seriously. You're my best friend!"
    "The words came out so naturally that I almost missed them at first. Then they hung there, soft and certain, between us."

    hide Qwynn_S with dissolve

    "I blinked."
    "I'd never had a best friend before. Not really. People came and went, but no one had ever said that about me."
    asideeb "...Your best friend?"

    show Qwynn_S at half_size with dissolve

    q "Yeah! Of course. Who else puts up with me bringing home six boxes of random teacups?"
    "They were teasing, but their tone had that same warmth as always. That made it hard to doubt their sincerity."
    "I felt something stir in my chest."
    asideeb "You're my best friend too, Qwynn."
    "Qwynn's grin widened, soft at the edges."
    q "Good. Then it's official."
    "They stretched their hand out for a high five, which turned into a lazy half-hug shaking with laughter when we both missed."
   
    hide Qwynn_S with dissolve
   
    "Outside, the light shifted golden through the windows, catching the dust in the air. For a moment, the whole room glowed."
    "And that was the day I realized home wasn't always a place. Sometimes, it was a person."

    #[A MONTH LATER]

    window hide
    show black with dissolve
    window auto
    pause (2.0)

  
    #play music "city_night.ogg" fadeout 2.0 fadein 2.0
    scene kitchen with dissolve

    "A month later, both Qwynn and I had quit our jobs at the restaurant. We were sick of the management. (I mean, who wouldn't be?) Our savings slowly started to dwindle, but between the two of us, we made do."
    "One afternoon, I came home to Qwynn pacing across the living room, muttering under their breath."
    "Their usual bright expression was gone, replaced by a crease between their brows and an uncommon restless energy."
    asidesp "You're wearing out the floor. What's going on?"

    show Qwynn_M at half_size with dissolve

    q "Oh... nothing."
    aside "Doesn't seem like nothing."
    "They stopped mid-step and looked down, fingers pulling at the hem of their blouse."
    q "It's— it's the boutique. I don't know if I can keep doing it."
    asidesp "What do you mean?"
    q "I didn't realize how much work it would take. The sourcing, the rent, the marketing, the bookkeeping... Saints, it's just so much. I don't know, maybe too much."
    aside "You've already come this far, though."
    q "Yeah, but maybe it's time to admit it's just a child's dream."
    "Their voice trembled a little. I could tell they hated saying it out loud."
    asidesp "You've always said it's what you love! That has to mean something."
    q "Love doesn't pay rent."
    aside "No, but neither will giving up."
    "They gave a small laugh, soft and tired."

    hide Qwynn_M
    show Qwynn at half_size
    with dissolve

    q "You always know how to make my failures sound poetic."
    asidesm "It's a skill."

    hide Qwynn with dissolve

    "We shared a knowing smile, though theirs faded quickly. The air between us felt pressing again."
    "I hesitated, then said the first thing that came to mind."

    show Qwynn at half_size
    with dissolve   

    asidesh "...I got the job."
    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0

    hide Qwynn
    show Qwynn_S at half_size
    with dissolve

    q "What? No way. For Bloom? I thought you said they weren't hiring!"
    asidesh "They weren't. The manager, Sylphia, was going to turn me away since I had no barista experience."
    q "Then how did you convince her?"
    asidesm "Like you said. Diffusing."

    hide Qwynn_S
    show Qwynn_N3 at half_size
    with dissolve

    q "What do you mean? You lied about your experience?"
    aside "No, literally. Diffusion. It's a coffee word. The water passes through the grounds, takes what it needs, leaves the rest behind. Same idea..."
    q "You do realize that makes absolutely no sense?"
    "I laugh under my breath. Maybe not, but it felt right when I said it."
    asidesm "I told Sylphia that I'd prove I could make coffee... soooooo I made a cortado."
    q "When did you even learn how to make coffee or a corblando?"
    asidesm "*snicker* It's a cortado."
    "I pointed toward the espresso machine on the counter."
    asidesh "Where do you think all the beans kept going?"

    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve

    "Qwynn stared at me for a long second before breaking into laughter, bright and sudden like a rose opening after rain."
    q "You're unbelievable."
    asidesm "And employed."
    q "Touché."
    "Their laughter lingered, soft and real. I wasn't sure if I'd changed their mind about the boutique, but the heaviness in their eyes seemed to ease."
    
    hide Qwynn_S
    show Qwynn_N3 at half_size 
    with dissolve   
    
    q "No, really... It's one of the things I love about you, Astra. You never give up."

    #[EVENING]

    window hide
    show black with dissolve
    window auto
    pause (2.0)


    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0
    scene kitchen_night with dissolve

    "The weeks after I started at Bloom passed faster than I expected. Between shifts and cleaning, and learning to pull a perfect shot of espresso, I barely had time to breathe."
    "Sometimes, when I came home late, Qwynn would already be asleep on the couch, surrounded by half-finished sketches and stray bits of fabric."
    "That night though, they seemed to be waiting for me to come home."

    show Qwynn_S at half_size with dissolve

    q "Hey, Aste, you want to hang out tonight?"
    asidesp "Sorry, Qwynn! Sylphia has me on close!"

    hide Qwynn_S 
    show Qwynn_N3 at half_size
    with dissolve

    q "I see... that's okay!"

    hide Qwynn_N3 with dissolve

    "I felt bad every time I had to say no. But what could I do?"
    "Bloom had become my second home."
    "It was a place full of light and warmth. I loved everything about it, from the scent of roasted coffee beans, to the faint hum of soft music, to the sound of people talking quietly over steaming mugs." 
    "I loved the way the sun poured through the front windows in the morning, painting the tables with a golden hue."
    "Even if I was exhausted, I wanted to be there."
    "Sylphia, though intimidating at first, had a strange way of believing in me. I was still trying to figure Albion out. Him and his unreadable expression… I wondered what his story was."
    "Still, a small part of me missed the simplicity of home. Missed Qwynn's laughter, their smile… their rose and leather scent…"


    #[AFTERNOON]

    window hide
    show black with dissolve
    window auto
    pause (2.0)

    play music "astraapartment.ogg" fadeout 2.0 fadein 2.0
    scene kitchen with dissolve

    "One afternoon, as I was putting on my shoes for another late shift, Qwynn appeared in the doorway."

    show Qwynn_S at half_size with dissolve

    q "Okay, Astra. We {i}have{/i} to hang out tonight. No excuses."
    asidesm "Oh? Why's that?"
    q "Because I've gotta show you something. It's important."

    hide Qwynn_S with dissolve

    "They looked so excited that I couldn't bring myself to say no."

    #[EVENING]

    #TODO change below bg

    play music "Qwynn.ogg" fadeout 2.0 fadein 2.0
    scene market_evening with dissolve

    "After my shift ended, Qwynn met me outside Bloom, practically bouncing on the tips of their toes."
    "We walked together through the quiet streets until we reached a corner shop I'd never noticed before."
    "A delicate wooden sign hung above the door, carved with stars and faintly painted letters: Voyage Étoilé."
    asidesp "Voyage... Étoilé?"

    show Qwynn_S at half_size with dissolve

    q "Nice, right?"
    "They unlocked the door and waved me inside."

    hide Qwynn_S with dissolve

    #TODO change bg later

    "The boutique was small but felt never ending. Every corner was filled with soft color and careful detail." 
    "Shelves crammed with glass jars, silk ribbons, little trinkets, and jewellery made from stones that shimmered faintly under the light."
    "It smelled like roses and that natural earthy scent of the outdoors."
   
    show Qwynn_S at half_size with dissolve  
   
    q "I started it last month. It's not much yet, but it's getting there."
    asidee "Qwynn... this is amazing."
    q "I've always loved traveling, meeting people, and learning about different cultures. You'd be surprised how much you can learn from a Nymph about going with the flow, or an Elf about the beauty of detail."
    asidesp "You really made this happen. I'm so proud of you."
 
    show Qwynn_N3 at half_size with dissolve
 
    q "You are?"
    aside "Of course. You're my best friend."

    hide Qwynn_N3
    show Qwynn_M at half_size 
    with dissolve

    "For a moment, something in Qwynn's expression shifted. It was small, almost imperceivable, but it made me pause. Then, as quickly as it came, it was gone."
    
    hide Qwynn_M 
    show Qwynn_S at half_size 
    with dissolve

    q "You're my best friend too, Astra."
    "They smiled again, wide and bright, the kind of smile that could light up a room."

    jump Qwynn_chp2

#########################################
# END
#########################################









