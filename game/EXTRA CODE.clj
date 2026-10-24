




style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    color "#fff"
    yalign .995
    size 18
    kerning -1
    xoffset 290

style main_menu_version:
    variant "small"
    xoffset 365




    style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 0.5
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

    size 40
    kerning -1
    xoffset 100
    yoffset 300

style main_menu_version:
    properties gui.text_properties("version")


ALTERNATE PROLOGUE

     scene cafe_alley
    "Warm sunlight filtered through the nearby window, I felt warm all over  as I groggily opened my eyes to greet the new day." 
    "My arms reached up and over my head, sending a pleasant shiver down my spine."
    "For a moment everything was calm. Splayed out in warm sheets, soaking up the morning sun instead of rushing off to work. It felt nice..."
     "Maybe a little too nice."
     a "(Wait a minute.)"
     "I inhaled suddenly and with a burst of sudden energy, I reached clumsy hands out to snag the calendar on my nightstand."
    "Upon seeing the date I breathe a sign of relief."
    a "(I'm saved)"
    "Recently, things have been slower than usual. Which meant less early mornings for me."
    "On one hand, sleeping in was great, but on the other…I loved my job. Fewer customers was bad for business no matter how you cut it."
    "I move to sit on the edge of the bed and reach sun warmed fingers to clutch at strands of hair as a heavy sigh leaves my body."
    a "(There had to be some way to bring in more customers, this is Halis! Thousands of Humans and Magical Races lived here.)" 
    a "(That’s not even including the flood of tourists who wanted to see for themselves what was so great about the Integrative Cities.)"
    "Thinking of new ways to boost patronage had become a common occurrence. My roommate, Qwynn, had caught me staring into space on multiple occasions."
    "It’d even started happening at work. Last week, Albion even scolded me for flooding a poor customer's pour over before shooing me away to \"go sulk elsewhere\"."
    a "(…All this thinking wasn’t going anywhere…maybe I should just-)"
    "{b}knock knock knock{/b}"
    "Three distinct knocks sounded at your bedroom door...there was only one person it could be."
    "A muffled voice reaches my ears."
    q "Astra! You up? I made us some coffee!"
    a "I’m up! I’ll be out in a minute."
    q "You better, don’t let my hard work go to waste!"
    "I laugh, but I stop them before they can say anymore."
    a "Okay, okay! One minute, I promise!"
    q "I’m holding you to it!"

    #INSERT FOOTSTEPS SOUND

    a "(Well then, I guess it’s time to get ready. Qwynn will kill me if I let their coffee go cold.)"

    #FIX
    "About two months ago now Qwynn asked me to help them learn how to make better coffee. They said they felt bad since I was always making it for them and they wanted to be able to return the favor sometimes."

    "In the beginning, the results were disastrous. Every cup was either seriously watered down or horribly bitter, but they'd slowly been improving."

    a "(I don’t want to keep them waiting, Qwynn has been practicing a lot these days.)"

    "Pushed by the thought of warm coffee I got dressed in record time."

    show cafe_interior_dawn

    "The window over the kitchen sink was open, letting in the fresh spring breeze. Outside I could see cobbled streets and hear the rush of water from the canals that ran through Halis."

    "My eyes eventually broke away from the idyllic scene and caught on Qwynn, who stood at the counter with a mug in each hand. They looked up with a smile."

    show eileen 
   
    q "I think you’ll like this one, I followed all your {i}many{/i} many instructions to the letter."

    "Qwynn pushed one of the two mugs closer to me and gestured at it with an open palm."

    "I grabbed the mug with both hands. It was still pleasantly warm, taking me back to that very morning when I was still enveloped in toasty sheets."

    "I took a deep breath and really smelled the coffee. The aroma was nutty and a little smoky."

    a "(Ah, they used the dark roast that I picked up from the market after work a few days ago)"

    "My eyes closed and the corners of my mouth turned up. As usual, the smell of coffee alone is enough to lift my spirits."

    q "Astra {i}please{/i}, just take a sip and tell me how it tastes."

    "My eyes crack open and I see that Qwynn is waiting for me to try it first."

    a "Sorry, but the aroma is important too, I can tell a lot just by smelling it and you know the-"

    q "Yes I know, the aroma tells you things that your tongue can’t. {i}Blah Blah Blah{/i}. Trust me, with my sense of smell, I get it, I really do, but you’re taking {i}forever{/i}."

    "I smile fondly but refrain from saying anything else as I bring the mug to my lips."

    "I take a second sip, partially because I’m trying to get a better grasp on the flavor but mostly just to mess with Qwynn as I know their patience is wearing thin."

    q "Well? How is it?"

    a "Much better than last time, a little watery but that’s no big deal. Your efforts are paying off!"

    "Qwynn grins wickedly."

    q "Watch out! I’m going to run Cafe Bloom outta business!"

    "Qwynn finally takes a sip from their own mug. Their eyebrows pinch together and I hear the sound of the fridge opening."

    q "I don’t know how you drink this stuff black. No thank you."
    
    "For these taste testing sessions we always try the coffee black first. It’s the easiest way for me to check the overall quality of the brew, but Qwynn always gives in after the first sip."

    "A few minutes pass as Qwynn and I have an easy conversation about the nice weather and our plans for the day. "

    "Before long it's time to head out for work."

    scene cafe_street_dawn

    "It takes a little over 30 minutes to get to work, first a short walk to the central canal. From there she would ride the ferry until reaching the block where Cafe Bloom was. Though living closer would be nice, I had come to enjoy the commute to the cafe."

    "I passed by different shops, restaurants, and merchants on my walk to the ferry. If I had more time I would do a little shopping, but as it was there was no time for detours."

#THERE IS DIALOUGE MISSING HERE 

    "The first thing I see when I walk into Bloom & Bean is Albion. He’s standing at the counter in the middle of what I assume is the order for the only customer currently in the cafe, tucked over in one of the corners looking at a stack of papers."

#ALBION 1st CG GOES HERE 

    show male_neutral

    "Albion looks like he’s concentrating deeply. His hair is so light that the subtle lilac color is difficult to catch, but here bathed in the natural light of the cafe it shines through."
     
    "His eyebrows are furrowed, a common feature for Albion. If he wasn’t a Nymph blessed with eternal youth, I’d worry that his face might get stuck like that."

    "He’s perfectly manicured, as usual, his tight ponytail is adored with his signature white bow. His clothes are crisp and unwrinkled." 
    
    "He makes controlled, yet graceful movements as he pours water into the filter. Everything about him is perfect…except…"

    "Albion glances up at the sound of cafe's bell."

    al "Your ties’ crooked. Knots loose"

    a "(...Except for when he opens his mouth.)"

    a "And {i}your{/i} shoelaces have come undone"

    al "What?...No they haven’t, I always-"

    "Anything else he says is stolen by the air as I enter the break room and the door closes behind me. I hang my bag on one of the hooks and turn to write my name on our timesheet."

    a "(Made it right on time.)"




    label Chapter2:


    play music "BlitheA.ogg" loop
   
    window hide
    pause (5.0)
    window auto
    show prochp2
    $ renpy.pause(5.0)