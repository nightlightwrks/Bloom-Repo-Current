# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define ven = Character ("VENDOR", color="#3a0f0c")

define Dryad = Character ("DRYAD GIRL", color="#3a0f0c")
define Doggy = Character ("DOG-EARED BOY", color="#3a0f0c")
define Teen = Character ("ELVEN TEEN", color="#3a0f0c")


label chp2:

    $ persistent.status_button = False

    window hide
    pause (1.0)
    window auto
    show prochp2 with squares
    $ renpy.pause(3.0)
    
########################################
# DAY OFF 
########################################

    scene bedroom_dawn with squares
    #play music "astraapartment.ogg" fadein 2.0
    
    "I wake up naturally, no alarms, no knocking, no surge of adrenaline caused by the idea of being late."
    "I take a few long, deep breaths, enjoying the lack of responsibility ahead." 
    "The last two days have introduced exciting new developments into my life, but I'm desperately looking forward to having a full day to do whatever I want."
    "It's still fairly early. Only 7 AM according to the clock next to me."
    aside "(Plenty of time for what I have in mind.)"
    "But first, a quick stop at Café Bloom for coffee."
    "It's inevitable that I'll run into Albion, but..."
    "Despite working there, it's only on my days off that I truly get to enjoy the atmosphere of the café without worrying about customers."
    asidep "(I refuse to change my routine over a little disagreement.)"
    "Of course, Albion doesn't really get it. He doesn't understand why someone would want to see their coworkers outside of work."
    aside "(The café is like a second home to me, so it's natural to want to spend time there... even on days off.)"
    "After that, the plan is to go to Qwynn's boutique to check out the new product they got recently before going to the markets for lunch."
    "Their shop is in Block 1 right by the southern gate which, of the four gates, is the busiest due to it being connected to a major trade route."
    "So, all in all, I could see Qwynn, eat some good food, {i}and{/i} get in some good exercise."
    aside "(A good plan if I ever heard one.)"

#SHOW NEW BG#
    show kitchen_dawn with dissolve

    "The kitchen is empty when I enter and a glance down the hallway reveals that Qwynn's light is still off."
    aside "(I'll try to be quiet.)"
    "I gather my things quietly and slip out the front door, doing my best to avoid waking Qwynn."


########################################
# RUMORS
########################################
    
    scene market_dawn with dissolve
    play music "city_day.ogg" fadeout 2.0 fadein 2.0
   
    "The sun has risen, but the streets aren't crowded quite yet. {i}That{/i} will come in the next few hours." 
    "And so, I stroll slowly—basking in the atmosphere of the early morning..."
    "I decide to take the ferry to the café again this morning. It's faster and more relaxing than taking a carriage."
    "Plus, on a morning as nice as this, I could sit back, relax, and take in the view from the deck."
    "The sounds of rushing water grow louder, signaling my arrival at the dock."
    aside "(Perfect timing! The ferry's already here.)"
    "The ferry looks to be about halfway full leaving plenty of open seating."
    "It only takes a few moments for me to settle into a seat near the railing."
    "To my right, I hear excited chatter coming from a group of young teenagers."
    Dryad "{i}I{/i} heard my friend say she caught a glimpse of Saint Caelan the other day!"
    Doggy "Seriously?! Man, I wish I could've seen them!"
    Teen "I bet she made it up, the Saint never leaves the Sanctuary..."
    Dryad "But wouldn't it be cool if she did see them? Imagine getting to meet the great Saint Caelan— {i}in the flesh!"
    Doggy "Or better yet, see them flying over the city!"
    Teen "...Apparently other cities' Saints make appearances all the time."
    Doggy "Lucky~"
    "They continue, gossiping about other various 'sightings' related to the Saint, but nothing they say is new information."
    "There's a constant stream of rumors regarding Saint Caelan, but at the end of the day no one had really seen them with their own eyes."
    "It's always 'My friend said—' or 'I heard from so and so that—'."
    "Each of the Integrative Cities has a Dragon Saint who lives among them, but {i}our{/i} Saint, the Water Saint, hasn't been spotted in over two decades—after access to the Sanctuary was cut off." 
    asidesh "(I won't lie and say I'm not curious myself, but whatever reason the Saint has for keeping to themselves is their own.)"
    aside "(Though not an all-powerful being, it feels wrong to spread rumors about the Saint considering it's their power that keeps Halis' waters clean and safe.)"
    
    menu:

        "It would be nice to see Saint Caelan. At least once.":
                show screen choice_indicator(CAELAN_COLOR) 
                $ persistent.saint1 = True
                jump chp2_choice

        "There's no point in playing into rumors.":
                jump chp2_choice

    scene market_dawn with dissolve
    
    label chp2_choice:

    "The ferry rocks slightly as it comes to a stop, jolting me from my train of thought. Quickly, I stand up to disembark before making my way to Café Bloom."


########################################
# CAFE ENCOUNTER
########################################

    
    "When I reach the café, Sylphia is standing outside unfolding chairs and setting them up on the patio for the day." 
    "After a moment, she spots my approach, pausing her work to call out a greeting."
    
    show Sylphia with dissolve
   
    s "Oh, good morning Astra!"
    asidesp "Good morning!"
    s "Are you working today? I could have sworn today was your day off."
    aside "No, you're right. I just came for some coffee."
    s "Well, you came to the right place! Go on in, I need to finish setting up out here, but Albion's inside. He can help you out."
   
    hide Sylphia with dissolve
   
    asidesh "...Alright."


    scene cafe_interior_dawn with dissolve
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0
    play audio "<from 0 to 3>bell.mp3"

    "The bell rings when I enter and Albion looks up from what he's doing. The furrow of his brow becoming more obvious once he sees who it is."
    aside "Morning. Am I the first customer today?"
   
    show Albion_SC with dissolve
   
    al "Well, we did {i}just{/i} open."
    asidesh "Right..."
    al "..."
   
    hide Albion_SC with dissolve
    
    "Tension hangs in the air, filling it up like a balloon."
    "I know I should say something. If anything just to get rid of this horrible atmosphere."
    asidesa "(But I have no idea what I should say...)"
    asidesa "(Maybe... sorry?)"
    asidesh "(Sorry for {i}what{/i} though I'm not really sure...)"
    asidesm "(Maybe I can just pretend nothing happened.)"
   
    play audio "<from 0 to 3>bell.mp3"
    
    "I don't have time to think about it too much more as the bell rings again and Sylphia comes striding in, dusting her hands off."
    "One thing to note about Sylphia?  She's a master of reading the room."
    
    show Sylphia with dissolve
   
    s "...What is this?"
    asidesa "..."
    
    show Sylphia at Transform (xpos=1250) with ease
    show Albion_SC at Transform (xpos=300) with dissolve

    al "..."
    asidesh "It's nothing."  
    s "Hmmmm, alright then."
    s "Astra? Did you order yet?"
    asidesh "Ah no, not yet."
    "Sylphia's eyes flick over to Albion."
   
    hide Albion_SC with dissolve
    show Sylphia at truecenter with ease
   
    s "Well we can't have that, what can I get for you today? Do you want your usual, or something else?"
    aside "The usual is fine, thanks Sylphia."
    s "No problem."
   
    hide Sylphia with dissolve
   
    "Sylphia walks away, moving further behind the counter, leaving me alone with Albion again."

    play ambient "sfx_cafenoise.ogg" fadein 2.0
    aside "(I guess it's up to me to start up a conversation.)"
    asidep "(Unless I want to sit in awkward silence for the next few minutes.)"
  
    show Albion_SC with dissolve
   
    al "..."
    asidesh "..."
    aside "So... what's up?"
    al "How long did it take you to come up with that one?"
    asidesm "Less time than it took you to come up with nothing."

    hide Albion_SC 
    show Albion
    with dissolve

    "Albion doesn't respond to that, but he does appear less tense. Falling back into our usual ribbing seems to alleviate some of the anxiety gnawing at us."
    aside "How's your morning going?"
    al "As well as it could be."
    asidesm "I'm... not sure if that's good or bad."
    al "It's neutral."
    aside "Neutral."
    al "Yes."
    asidesh "..."
    aside "Right."
    asidesp "Okay then, I guess it's my turn!"
    al "For...?"
    aside "Now you ask me. 'How was {i}your{/i} morning?'"
    al "You know, you act just like a little kid sometimes."
    asidesp "I'm older than you!"
    al "Doesn't feel like it."
    "I lean my head into my left hand."
    asidesm "You jealous~?"
    "Albion raises his eyebrows."
    al "Jealous? Of {i}you{/i}? Saint's no."
    "I chuckle at Albion's insistence. He takes everything so seriously..."
    "It's nice to be able to joke with him."
   
    hide Albion with dissolve

########################################
# HOMEY
########################################

    stop ambient fadeout 3.0

    "The sounds of the coffee maker come to a stop and Sylphia makes her way back towards the bar with a mug in hand."
    "Soon, my usual is placed in front of me." 
    
    show coffee1 with dissolve
    
    "A hot and steaming cortado. Equal parts espresso and milk, and the perfect way to kick-start my day."
    
    hide coffee1 with dissolve
    show Sylphia with dissolve
   
    asidee "Thanks Sylphia!"
    s "You're quite welcome."
   
    hide Sylphia with dissolve
   
    "I reach for the cup, ready to take my first sip when a plate slides into my periphery."
    "I look up to find Albion avoiding eye contact with me. Still avoiding my gaze, he speaks up."
    
    show Albion_Shy1 with dissolve
   
    al "Breakfast. My treat."
    aside "(It's true that I haven't eaten yet.)"
    aside "...Thank you, Albion."
    "He nods before walking away, disappearing around the corner of the bar." 
    
    hide Albion_Shy1 with dissolve
    
    "As soon as he leaves, Sylphia leans down next to me and whispers conspiratorially."
    
    show Sylphia with dissolve

    s "{i}I've learned that when Albion does things like this, it's better to just accept it and then pretend like nothing happened. "
    aside "Haha, understood."
    asidesp "It looks delicious! But, I haven't seen this one before, are you trying new recipes?"
    s "Not really. We were running low on some of our usual stuff so I used some of the fresh fruits I picked up this morning."
    "Blueberries and strawberries are baked into the scone, and when I take the first bite, the berries are so juicy that my cheeks twinge in response."
    "The menu at Café Bloom is pretty basic, offering classic coffee, tea, and scones. What keeps customers coming back is the high quality and the people."
    s "It's just something I threw together this morning, I didn't even try it myself first."
    asidesm "Oh, so I'm your guinea pig then?"
    s "Hey, Albion's the one that brought it out."
    "Like a ghost, Albion appears now holding a glass of water, which he sets next to my coffee."
    
    show Sylphia at Transform (xpos=1250) with ease
    show Albion at Transform (xpos=300) with dissolve

    al "I tried one already. They're good."
    "Sylphia smiles at Albion, swatting at his arm softly."
    s "Oh? High praise coming from you."
    asidee "This would be a great addition to the menu. Customers would love it… I'll keep it in mind for our final proposal."
    s "Sounds like a plan! I can't wait."
    al "..."

    hide Albion
    hide Sylphia 
    with dissolve

    "With no other customers in the café, there's a sense of comfort and intimacy that permeates the air."
    "It reminds me of what I hope to achieve with the new development plan."
    "...Café Bloom should be a place that {i}everyone{/i} feels like going to. A reflection of the city itself, diverse and filled with warmth."
    asidesa "(...)"
    "Conversation flows for a while longer. Eventually, my coffee and scone disappear, and in the blink of an eye, it's time for me to leave."
   
    show cafe_interior with dissolve
   
    asidesp "Oh! It's almost time for Qwynn's shop to open up. So, I have to get going."
    asidesp "I'll see you guys later, thanks for the chat!"
    
    show Sylphia with dissolve

    s "Anytime!"

    hide Sylphia 
    show Albion 
    with dissolve

    al "..."

    hide Albion with dissolve

#######################################
# BOUTIQUE 
########################################

    scene market with dissolve
    play music "city_day.ogg" fadeout 2.0 fadein 2.0
   
    aside "(Okay, now to go see Qywnn.)"
    "Qwynn's shop is located right near the southern gate, making it a prime location for an accessory and clothing boutique."
    "When Qwynn and I first moved in together, we were working in the same restaurant, but their goal had always been to open a boutique."
    "Almost a year ago now Qwynn had finally opened their own store in a good location, quickly becoming a local favorite."
    asidesm "(Though I suspect a large part of their customer base are just trying to get Qwynn to notice them.)"
    "Between their positive attitude and knack for getting people to open up, Qwynn was quite popular."
    aside "(Hopefully they're free enough to chat for a bit...)"
  
    scene market with dissolve
  
    "Standing in front of Voyage Étoilé, I catch glimpses of new items in the shop that weren't there the last time I came."
    "Qwynn travels roughly once a season, going to various cities and towns to source new accessories and clothing from vendors."
    "It's what makes their shop stand out, as Qwynn is often able to establish relations with all kinds of people, keeping the shop stocked with unique products."
    "It doesn't take long before I hear a familiar voice calling my name."
    q "Astra! You made it!"
    "Qwynn jogs towards me, grinning widely and waving."
    asidesp "Of course I did! Are you busy?"
    
    show Qwynn_S at half_size with dissolve
    
    q "For my best friend? Never."
    q "C'mon! I have so much cool stuff to show you!"

    show Qwynn_S at zoom_in, Transform (ypos=-40)
 
    "Qwynn takes my hand and starts dragging me inside. Along the way, I wave to the other staff members as I pass by. Most of whom I recognize from previous visits."

    hide Qwynn_S
 
    asidesm "(Good thing I stopped for coffee, Qwynn seems extra excited today. They must have gathered some really interesting items this time.)"
   
    play music "Qwynn.ogg" fadeout 2.0 fadein 2.0
    show boutique with dissolve
   
    "The inside of the shop is busy, but not so much that it's difficult to move around in."
    "Still holding my hand tightly, Qwynn pulls me around, pointing excitedly at all the new items."
    "They come to a stop in front of a display. On it are a variety of jewelry pieces, all constructed from shining pearls, glass, and shells."
    
    show Qwynn_S at half_size with dissolve
    
    q "You remember that trip I took to Sholair last month, right? Well, I was lucky enough to be there while Mermaids were visiting the city."
    asidee "Mermaids? Really?! How rare."
    q "Right?! I found out that they occasionally come up to the surface to trade things along the shore."
    asidee "I had no idea! So then, these are..."
    q "All handcrafted pieces, made from deep sea pearls and colored glass."
    asidee "(I've never seen anything like these before...)"
    aside "So, what did you trade for it?"
    q "That's the best part! They love regular, everyday items that we use on the surface, like forks and dishes."
    q "Plus, once I mentioned that I sell my finds, a few of them gave me extra pieces. All of ‘em seemed really interested in surface culture."
    q "That's why they do trades. Since it's not like we use the same currency."
    q "We get to learn about their culture, and they get to learn about ours. It's a win win!"
    "This pattern continues for the next hour, get pulled along to a new display, hear Qwynn's travel story, repeat."
    "Once we reach the last display Qwynn lets go of my hand."
    q "Aaaand done. Until I find some more stuff of course."
    aside "When's your next trip?"
    q "I'm not sure yet! There's some things I want to sort out here before I make any final decisions."
    aside "What about where? Have you decided that?"
    q "Mmmm, wherever the wind takes me!"
    q "Maybe I'll go see one of the Dwarven settlements. They're constantly coming up with new stuff, so I'm sure I'll see {i}something{/i} inspiring if I go there."
    aside "The Dwarves huh? They do make the best tools."
    aside "(In fact, most of the ones we use at Bloom were made by Dwarves.)"
    "The Dwarves do have their own settlement underneath Halis, but it's much smaller than the ones that are built into the mountains."
    aside "It's hard to even imagine the scale of that, you'll definitely find some cool stuff there."
    "Qwynn smiles."
    q "{i}Haha{/i}, I'm glad you see my vision!"

    hide Qwynn_S with dissolve

    "We stand in the shop for a while longer, chatting. At some point, some of Qwynn's employees join the conversation."
    "When the sun hits its peak, I take that as my cue to start heading out."
    "I'm about to say my goodbyes, hoping to get to the Block 1 market in time for lunch when Qwynn grabs my hand one last time."
    
    show Qwynn at zoom_in, Transform (ypos=-40) with dissolve
    
    q "Ah! Wait—"
    q "...I, uh set aside one of the pearl bracelets for you. It's yours... if you want it."

    hide Qwynn with dissolve

    menu: 

        "Yes please!":
            jump Yes_Please
        "No, thank you.": 
            jump No_Thanks

label Yes_Please:

    $ persistent.bracelet = True
    
    show Qwynn_S at half_size with dissolve

    q "Okay! I'll go get it."

    hide Qwynn_S with dissolve

    "Qwynn moves into the back to grab the bracelet and then comes back to stand in front of me again."

    show pearls with dissolve

    "They hold the bracelet out in the palm of their hand."

    hide pearls
    show Qwynn_S at half_size 
    with dissolve
  
    q "One of the Mermaids, Aerwyna, told me that in their culture, wearing pearls is believed to help you overcome hardships..."
    q "You're working on that proposal for Sylphia right?"
    asidesp "Yes, but—"
    q "Anyways! I thought this might help."
    "Before I can say anything Qwynn slides the bracelet over my wrist, tapping it with a sense of finality once they're done."
    asideeb "(Always so thoughtful...)"
    aside "Hey, seriously. Thank you. You're always bringing me back gifts from your travels."
    q "Don't worry about it too much. Now, get outta here. You're gonna miss it."
    asidesp "Huh? Miss what?"
    q "Don't 'huh?' me. You wanna catch the lunchtime food stalls don't you? If you leave now, you can get there before everything sells out."
    asidesp "Ah, right! I almost forgot, see you later!"   
    q "See you at home!"
   
    hide Qwynn_S with dissolve
    
    jump Market_Felix

label No_Thanks:
   
    play music "city_day.ogg" fadeout 2.0 fadein 2.0
    show Qwynn at half_size with dissolve
    
    q "No problem, I just thought you might like it and didn't want someone else to get to it first, so I put it in the back."
   
    hide Qwynn
    show Qwynn_S at half_size 
    with dissolve
   
    q "But! Now, I can sell it. Everybody wins."
    asidesp "Thank you for thinking of me though! I always appreciate your gifts."
    "Qwynn raises their hand in front of them, as if waving away my thanks."
    q "It's nothing."
    q "...Hey, shouldn't you be going? You're gonna miss it."
    asidesp "Huh? Miss what?"
    q "Don't 'huh?' me. You wanna catch the lunchtime food stalls don't you? If you leave now, you can get there before everything sells out."
    asidesp "Ah, right! I almost forgot, see you later!"
    q "See you at home!"
   
    hide Qwynn with dissolve
  
    jump Market_Felix

########################################
# MARKET 
########################################

label Market_Felix: 

    scene market with dissolve
    play music "city_day.ogg" fadein 2.0
    
    "After I leave Qwynn's shop, I decide to walk around the rest of Block 1, which has more shops than the other blocks."
    "The main road is lined with market stalls, taking advantage of the increase in tourists that the city experiences every weekend."
    aside "(I could wander here for hours...)"
    "With so many different races from both inside and outside of Halis, the selection at the markets is limitless."
    "With my mind set on finding lunch, I simply follow the smells of food to find where vendors have set up shop for the afternoon."
    "I end up in a cluster of stalls selling various local specialties from nearby villages." 
    "Lines are already starting to form, so I quickly scan the area, though it's hard to really see anything."
    "I stand on my tip toes, attempting to see over the crowds to get an idea of what looks the tastiest when a hand on my shoulder makes me jump."
    
    play sound "sfx_shake.ogg"
    show market with vpunch
  
    asidesp "Ah— Saints! Wha—"
    who "Woah—sorry, sorry! Didn't think I'd scare you that bad."
    "They reach out and grab me by the shoulders, steadying me."
    who "You okay?"
    asidesh "Y-yeah. I'm okay."
    "When I look up from my feet I find myself face to face with none other than Felix."

    show Felix at zoom_in with dissolve

    f "Well this feels familiar~"
    "He takes a step back."

    hide Felix
    show Felix 


    f "Although, I guess it's more my fault this time."
    f "You here for lunch?"
    aside "Yes actually, what about you?"
    f "The same. Well, sort of. I'm actually here selling some paintings."
    f "Buuuut, I was getting hungry so here I am!"
    f "My studio is getting a bit cluttered, so I'm selling a bunch of paintings to make some room."
    asidee "Really? I'd love to see more of your work."
    f "Sure! I can show you after we get something to eat."
    f "Actually, I happen to know where to get the {i}best{/i} grilled salmon. How about I take you there?"
    asidesm "The {i}best{/i} you say? That's some high praise."
    f "It's the truth! C'mon, I'll show you."
    f "...Only if you want to of course. I don't want to ruin your plans."
    aside "Hmmm. I wasn't really planning on anything in particular if I'm being honest."
    asidesh "(I don't see why not.)"
    asidesm "(Not to mention that this could be the perfect chance to get to know Felix better.)"
    asidesp "Sure! Lead the way."
    f "Great! Then, follow me."

    hide Felix with dissolve

    "Felix weaves through the crowd with a sense of familiarity."
    "He moves around people with ease, while also occasionally glancing back at me with a smile to make sure that I'm keeping up."

########################################
# LUNCH AT VEL'S
########################################


    "It doesn't take long to reach Felix's destination. There, I see a Were-fox making some final adjustments to his stall."
    "He looks up as we approach and smiles in recognition when he spots Felix."
    ven "{i}Well, well, well.{/i} If it isn't my favorite customer."
    "The Were-fox moves out in front of the stall with his arms crossed, looking at Felix playfully. After a moment, his hands move to rest in his pockets, and his eyes flick over to me."
   
    show Velvet
    with dissolve
   
    ven "Oh? Who's this?"
   
    show Velvet at Transform (xpos=600) with ease
    show Felix at right with dissolve
   
    f "This is Astra. She was looking for a good place to eat so..."
    ven "Wow, free advertising! Thanks man."
   
    hide Felix with dissolve
    show Velvet at center with ease
   
    "The Were-fox's attention then shifts fully over to me, and I get the feeling that I'm being scrutinized."
    "Finally, they stick their right hand out towards me, initiating a handshake."
    v "Nice to meet you Astra, I'm Velvet. Or just 'Vel' for short."

    hide Velvet
    show Velvet 
    with dissolve

    v "Felix doesn't usually meet up with people when it's not related to work, so forgive me for being shocked."
   
    show Velvet at Transform (xpos=600) with ease
    show Felix at right with dissolve
    
    f "Woah, hey! I hang out with people outside of work."
    v "Oh yeah? Who?"
    f "Y—"
    v "And don't say me. I don't count."
    f "...That's not fair."
    v "Point proven."
    "Velvet takes his attention off of Felix, shifting his focus back to me while pointing back at Felix with his thumb and rolling his eyes."
    "Felix makes a wounded noise."

    hide Felix with dissolve
    show Velvet at center with ease
   
    v "So anyways, Astra! I assume you were promised some food?" 
    asidee "Yeah! Felix told me you make the best grilled salmon."
    v "I sure like to think so. Give me some time to get everything going and then you can see for yourself."
    v "Keep Felix company in the meantime, yeah?"
    
    hide Velvet with dissolve
   
    "Velvet walks back towards the stall again, patting me on the shoulder as he walks away."
    aside "(They seem nice, a little overfamiliar maybe... but nice.)"
    "Felix glances over at me, looking only mildly put out."
    
    show Felix with dissolve
   
    f "I need you to know that I {i}totally{/i} hang out with other people."
    f "...Though— I suppose Vel is the only one I'd consider a real friend."
    asidesm "Sure... I believe you."
    f "It's true!"

    hide Felix with dissolve

    "The both of us dissolve into laughter, the scene resembling something very similar that happened just the day before."
    "It feels natural to be around Felix, like we've known each other for much longer rather than a single day."
   
    hide Felix
    
    asidesh "(Could I consider us friends? After just a day?)"

    menu: 

        "Yeah... definitely!":
            jump Friends
        "Maybe not yet.": 
            jump Leave_it_be

label Friends:
    asidesh "Well... You could add {i}me{/i} to that list."

    #TODO add emotional music?

    show Felix_S with dissolve
 
    "Suddenly, the easy atmosphere that has been building up between us vanishes, and Felix's grin falters for a split second."

    hide Felix_S
    show Felix 
    with dissolve

    f "...Y-yeah. I guess I can!"

    hide Felix_S with dissolve

    "Though he technically agreed, there's a look in Felix's eyes that gives him away."
    "I don't have too much time to think about it as Velvet approaches holding a bowl in each hand."

    jump on_track

label Leave_it_be:
    "I decide not to say anything, instead letting the conversation continue." 
    "We talk freely for a few minutes more before Velvet approaches holding a bowl in each hand."

    jump on_track

label on_track:
   
    hide Felix 
    show Velvet 
    with dissolve
    
    v "Here you go, freshly caught salmon grilled and served over rice. Be careful though, it's still hot."
    "That much is obvious. Steam curls off of the bowl as Velvet hands it to me carefully, making sure I don't burn my fingers."
    asidee "It looks amazing, thank you."
    v "No sweat, enjoy~"

    hide Velvet with dissolve
      
    "Inside, the salmon is artfully sliced and laid neatly over rice, covered in a thin glaze of something that smells faintly sweet."
    "Felix starts eating the moment the bowl is placed in his hands, but I take a moment to appreciate the freshly cooked meal and let it cool down."
    "Once I deem it cool enough, I take my first bite."
    "Despite its unassuming appearance, the flavors are beautifully balanced. The fish is tender and breaks apart easily—pair that with the glaze and it practically melts in my mouth."
    "It isn't too sweet either as the rice absorbs any extra glaze, mellowing out the flavor."
    aside "(How comforting...)"
    "I turn my head to Felix, but he's no longer sitting next to me. Although, I don't have to search very hard to find him."
    "Standing next to Velvet, Felix's bright clothes are easy to spot. I can see them speaking, but I'm not quite close enough to hear exactly what it is that they're talking {i}about{/i}."
    "Felix catches me looking over at them and turns back to Velvet, saying something that I can't make out before he walks back over towards me, plopping back down in his seat."
    asidesm "...Well Felix, you were right. I think this {i}is{/i} the best grilled salmon I've ever had."
    aside "It's exactly what I needed."
   
    show Felix at zoom_in with dissolve
    
    "Felix smiles and leans closer to me, lowering his voice."
    f "{i}Right? They may not look it, but Vel is one of the most hardworking people I know. He spent a lot of time perfecting this recipe."
    f "{i}He really wanted to make it feel like an authentic home cooked meal from his hometown. So it took some time."
    "From behind his stall, Velvet lifts his head up, ears swiveling in our direction. He makes a face and points towards the top of his head, clearly indicating that he can hear us."
    f "{i}Seriously?{/i} They still heard that?"
    asidesp "Hahaha! Tell me about it. My roommate is Were-folk too, and nothing escapes their senses."
    f "How am I supposed to spill his secrets now?"

    hide Felix with dissolve

    "Velvet shakes their head in resignation before going back to work."
    "At this point, the smell of Velvet's cooking has started attracting enough people to start forming a line. Now that they're fully set up, it's clear that Velvet's food is really quite popular."
    "I finish up the rest of my meal with a satisfied exhale and since Felix has already finished, it seems like we're about ready to leave."
    "Felix stands up and looks down at me."
  
    show Felix with dissolve

    f "Well, I should head back to my own stand now. You still coming?"
    aside  "Yeah, of course. Just give me a moment to go pay Velvet first."

    show Felix_U with dissolve

    "Felix makes a face and sighs loudly."
    f "No need. They said it was their treat."
    f "I believe their exact words were 'Tell your new friend that her lunch is on the house. In exchange, let's hang out again.'"

    hide Felix_U
    show Felix_N2 
    with dissolve

    asidesp "What? When did that happen?"
    f "After I finished eating."
    aside "...Huh. Well, alright."
    f "You don't have to hang out with him though if you don't want to. It's not like he's gonna force you."
    aside "I'm not against it. In fact, I'm a little curious too."
    f "…If you say so."

    hide Felix_N2
    show Felix 
    with dissolve

    f "...Let's get going."
    
    hide Felix with dissolve

    "As we turn to leave, I catch Velvet's eye as they're dealing with customers and I wave. His hands are busy, but he winks with a smile before getting right back to work."

########################################
# FLOWER FIEND
########################################
 
    "Together, we wander towards where Felix had set up his things."

    show market with dissolve

    "Once we arrive, Felix immediately starts to pull out his covered paintings, setting them out properly once more."
    "Looking around, Felix's stall shows a wide range of paintings in various sizes and subjects."
    aside "(Although…most of these are of different flowers.)"
   
    show Felix with dissolve
   
    f "Whenever I find my studio getting a little too cluttered, I come here and sell some of them off at a discount."
    asidesm "I can't imagine what your studio looks like, if this is just the 'clutter'."
    f "Haha! You don't wanna know. It's a madhouse in there. "
    f "..."
    asidesh "So you... uh, like flowers?"
   
    hide Felix
    show Felix_E
    with dissolve
  
    f "Ah... haha... yeah. Just a little bit."
    "For some reason, Felix's voice gets quieter—different from the louder, more excited way that he usually speaks."
    asidesm "Haha. Right, just a little bit then."
   
    hide Felix_E
    show Felix_N2 
    with dissolve
   
    f "...I find myself painting them more than anything else."

    hide Felix_N2 with dissolve

    "He said he'd paint anything if asked but..."
    asidesh "(There's a clear bias here...)"
    "Each of the paintings are beautiful in their own right. And, just like the ones I'd seen yesterday, they feel full of life."
    asidee "Felix, these are amazing. When I look at them... it almost feels like you've captured a moment in time."
    
    show Felix_Sad with dissolve
    
    f "Thanks... I enjoy painting flowers the most when they're in full bloom, but it's difficult. I have to try and catch them at the right time. "
    
    hide Felix_Sad
    show Felix  
    with dissolve
    
    "Felix looks sad when he says this, though when he catches me staring, he smiles."
    asidee "(It'd be amazing if more people could see these.)"
    aside "...Have you thought about displaying these somewhere? Like, in a gallery or... let's say... a café?"
    f "Hmmmm..."
    f "No, never really had the need to if I'm being honest. I get enough commissions as is. And the markets fill in the gaps well enough."
   
    hide Felix with dissolve
   
    "Truthfully, I was thinking that some of these would look beautiful on display in Café Bloom."
    asidesa "..."
    aside "Would you be open to it?"

    show Felix with dissolve

    f "Why? Got something in mind?"
    asidesh "...Maybe."
    f "Hahaha, alright then. Well then, {i}maybe{/i} I'd be open to it."
    asidesm "Fair enough."
    asidesa "(I should give this some more thought...)"

    hide Felix with dissolve

    play music "city_night.ogg" fadeout 2.0 fadein 2.0
    scene market_evening with dissolve

    asidesa "(I should start going back soon.)"
    asidesp "I've got to start heading home, but thank you for letting me see your work!"

    show Felix with dissolve

    f "No problem! I'm always happy to show off."
    f "If you need me for any projects in the future... well, you have my card."
    aside "{i}Haha!{/i} Right. If I need any paintings, then I'll reach out to you first."
    "Felix grins at that, sounding genuinely interested in hearing from me."
    f "Bye Astra!"

    show Felix_N2 with dissolve

    f "...Get home safe, okay?"
    aside "I will!"
    asidesp "See you around!"

    hide Felix_N2 
    show Felix 
    with dissolve

    f "Yeah. See you!"

    hide Felix with dissolve

########################################
# BACK HOME
########################################

    scene kitchen_evening with dissolve
    play music "astraapartment_night.ogg" fadeout 2.0 fadein 2.0
   
    "The door to my apartment shuts quietly behind me. Though I wasn't out for the full day, I can still feel a satisfying exhaustion settling into my bones."
    asidesa "(I still have a handful of hours before I have to worry about dinner.)"
    aside "(Guess I could get some chores done. Might as well keep going while I have the motivation.)"
    "Qwynn and I tend to keep the apartment pretty neat. Whenever one of us has the time, we try to do a little cleaning."
    "It ends up working well, but if one of us {i}does{/i} ever need help, we would just ask."
    "I spend the next couple hours cleaning. It's soothing, and something I actually enjoy doing, even though it's a day off."
    "It feels good to be doing something with my time instead of relaxing..."
    asidesh "(What can I say— I like to be busy.)"
    
    scene kitchen_night with dissolve
    play audio "dooropenclose.mp3"

    "The front door clicks open as I'm finishing up the last of the chores, and Qwynn steps into the kitchen, exhaling loudly."
    q "{i}Ahhhh{/i}, home sweet home."
    asidesp "Welcome back."
    "Qwynn sets their bags down and walks up to me."
    
    show Qwynn_N3 at half_size with dissolve
    
    q 'Need some help?'
    aside "I'm pretty much done already. Thanks though."
    aside "How was the rest of your day? Busy?"

    hide Qwynn_N3
    show Qwynn_S at half_size
    with dissolve

    q "Just a bit, but it was a good kind of busy. You won't find me complaining about good business!"
    aside "Glad to hear it!"
    q "Have you had dinner yet? I brought back some food if you're hungry."

    hide Qwynn_S with dissolve

    "They reach down, and from the bags on the floor, Qwynn brings out a container of food." 
    "My stomach growls loudly in response."
    "...I'd gotten so absorbed in cleaning that I didn't realize how late it'd gotten."

    show Qwynn_S at half_size with dissolve

    q "I'll take that as a no. Here, while it's still warm."
    "Qwynn places a portion of food in front of me. It looks like a creamy mushroom soup, which just so happens to be one of my favorites."
    asidee "Are you psychic?"

    show Qwynn_S at half_size with dissolve

    q "Not psychic, you're just predictable."
    asidep "{i}Hmph{/i}. I don't think I'm {i}that{/i} obvious..."
    aside "Thanks though..."
    q "Haha, you're welcome."
    "I dig into the food that Qwynn brought while the two of us alternate between eating and talking."
    q "What did you do after you left the shop? Did you make it to lunch?"
    asidesp "I did! I actually ran into Felix and he took me to a friend of his who happens to be a chef— And {i}Saints{/i}, their food was delicious!"
    
    hide Qwynn_S 
    show Qwynn_N3 at half_size
    with dissolve
    
    "Qwynn raises an eyebrow in confusion."
    q "Felix? Who's that?"
    asidesh "...Ah. Right."
    aside "Remember how I went to the markets after work yesterday? Felix is the painter that I ran into."

    hide Qwynn_N3 
    show Qwynn_S at half_size
    with dissolve

    q "{i}Ahhh yes.{/i} The handsome and mysterious painter."
    asidesh "...I don't think I said all that."
    q "I {i}might{/i} be embellishing."
    "Qwynn puts a hand to their chin and smirks subtly."
    asidean "I don't like that look. What are you thinking?"
    q "It's nothing. Just deciding if I should tease you {i}now{/i}... or later."
    asidea "..."
    q "You're right. Let's go with later. I need more information..."
    asidea "...?"
    q "So? You ran into him again today? How was that?"
    aside "Good, I think. He seems like a fun guy. I'm... hoping we can hang out more."
    asidesm "In fact, I think you'd like him a lot. I feel like you guys might get along."
    q "Wellll, they do say you can never have too many friends."
    aside "Who's they?"
    q "Me. Obviously."
    asidesm "Riiiiight."
    
    hide Qwynn_S with dissolve
   
    "The rest of the night continues like this. We eat, talk, and laugh until, eventually, it's time for both of us to turn in."

    show bedroom_night with dissolve

    "The exhaustion of the day's events seeps into my bones." 
    "I feel content, and I let that feeling deliver me swiftly into the land of dreams."
    
    if persistent.saint1 == True:
        jump chp3

label route_select:
    window hide
    show proend with dissolve
    $ renpy.pause(2.0)
    pause (2.0)
    window auto

    scene cafe_interior_evening with dissolve
    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0 

    "Five days later, Sylphia pulls me aside to ask for updates about the development plan."

    show Sylphia with dissolve

    s "Astra? Do you have a moment?"
    "Sylphia sits at the bar facing me. The café is empty, outside of Sylphia and myself, so her question isn't really necessary, but I answer it anyway."
    asidesp2 "Of course!"
    s "About what we discussed... It's time to make your choice—I want to hear what you think."

    hide Sylphia with dissolve

    "My heart skips a beat. This feels important, like the kind of choice that will shape not just the café, but the people tied to it."
    
    show Sylphia with dissolve
    
    s "As it was before, the first option is to focus on our menu. Add seasonal treats, new items, new coffees. Something to keep customers excited every time they visit."
    aside2 "(That sounds... very Albion. He {i}is{/i} always meticulously creating coffee blends.)"
    s "The second option is to turn the café into more of a community space. We could host events, bring in local artists, create something alive and ever-changing."
    aside2 "(Local artist... maybe someone like Felix?)"
    s "And finally... we could focus on marketing. Renovations, a stronger identity, and come up with something that makes us stand out from every other café in the district. A bold step forward."
    s "That last one might be a good choice if you know someone with experience in marketing, I admit it's not my strong suit."
    "My heart quickens. Each choice carries its own weight. I glance back at Sylphia, who watches me with quiet patience."
   
    #TODO add emotional music

    s "So, Astra... which vision speaks to you?"

    hide Sylphia with dissolve
label menu:
    
    menu:
        "Focus on adding new menu items and seasonal treats.":
            $ route = 'albion'
            $ albion_pts += 10
            show screen choice_indicator()
            asidesp2 "Let's focus on the menu. New items, seasonal treats, the works."
            show Sylphia with dissolve
            s "Very well. We'll make Bloom taste brand new!"
            hide Sylphia with dissolve
            jump Albion_chp1

        "Focus on creating a community space/artist gallery in the café":
            $ route = 'felix'
            $ felix_pts += 10
            show screen choice_indicator(FELIX_COLOR) 
            asidesp2 "I want Bloom to become a community space... to bring in local artists and keep it lively."
            show Sylphia with dissolve
            s "Bold, I like it! I'll reach out to a few contacts."
            hide Sylphia with dissolve
            jump Felix_chp1

        "Focus on marketing the café." if persistent.qwynn_route_unlocked == True and persistent.bracelet == True:
            $ route = 'qwynn'
            $ qwynn_pts += 10
            show screen choice_indicator(QWYNN_COLOR) 
            asidesp2 "Let's focus on marketing the café. If Bloom's going to grow, people need to know about it."
            show Sylphia with dissolve
            s "A sensible approach! We'll need to make Bloom stand out from the rest."
            asidesh2 "(I know someone who might know a thing or two about marketing...)"
            hide Sylphia with dissolve
            jump Qwynn_chp1


