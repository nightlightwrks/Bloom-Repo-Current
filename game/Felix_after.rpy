 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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

define fn = Character('FELIX', kind=nvl, color="#3c9b7c")
define an = Character('ASTRA', kind=nvl, color="#7e6fd6")
define na = Character(None, kind =nvl)


label felix_after:
 
    $ persistent.status_button = False
    
    show felix_after
    $ renpy.pause(1.0)
    window hide
    pause (5.0)
    window auto

    play music "felix.ogg" fadeout 2.0 fadein 2.0
    scene studio with dissolve

label felix_after2:

    "Which of Felix's after stories would you like to play?"

    menu: 

        "After Story #1 - Body Heat (Felix POV)":
            jump felix_content_warning1
        "After Story #2 - Dinner (Astra POV)":
            jump felix_content_warning2

label felix_content_warning1:

    scene studio_night with dissolve
    play music "city_night.ogg" fadeout 2.0 fadein 2.0

    "This after story contains some written NSFW content."

    menu: 

        "Continue":
            jump felix_afterstart
        "Go Back":
            jump felix_after2
        "Return to the main menu.": 
            return

label felix_content_warning2:

    scene studio_evening with dissolve
    #play music "city_night.ogg" fadeout 2.0 fadein 2.0

    "This after story contains some heavier written kissing/making out."

    menu: 

        "Continue":
            jump felix_afterstart2
        "Go Back":
            jump felix_after2
        "Return to the main menu.": 
            return

label felix_afterstart:

    na "I study her intensely, taking in every detail that I can."
    na "Astra's eyes are closed, she's warm—almost hot—and she shivers whenever I kiss her jaw."
    an "{i}F-Felix…{/i}"
    na "I notice that she's trying to keep her breathing steady—but she fails by gasping softly each time I thrust into her."
    na "I'm briefly distracted from my study as Astra's hand slips down to her lower abdomen." 
    na "Sudden, intense, pleasure zips through me—" 
    na "Cotton sheets slide underneath my shin as my right leg slips—A knee-jerk reaction."
    fn  "{i}Mm! Astra…{/i}"
    na "(Saints… She did that on purpose.)"
    na "It's impossible to miss the small smirk that pulls at her lips. "

    nvl clear

    fn "Ah— I'll get you back for that."
    an "Ohh nooo. I'm so scared—"
    na "She's interrupted by my fingers grazing her lips. With just a small bit of pressure—and no resistance from Astra—I push them into her mouth."
    na "Her hand moves from her stomach to my wrist. Careful fingers circling it loosely."
    fn "Alright?"
    na "She hums, the tone positive and the vibration distracting."
    na "I kiss her forehead."
    fn  "Good."
    na "Steadily, I increase my pace."
    na "My legs and arms burn, my teeth nip at Astra's ear… and Astra's fingers release my wrist in favor of scraping along my back."
    fn "Close?"

    nvl clear

    an "Mhm~"
    na "I extract my fingers from her mouth in preparation."
    na "Then, I shift my legs, adjusting the angle of our hips so I can better control my thrusts. My hand—the now one coated with Astra's spit—reaches down past her stomach, trailing down to—"
    an "F-Felix?"
    na "My hand pauses. I hum, pushing my nose against her neck in acknowledgement, but I don't stop pushing into her."
    an "Can I—"
    na "My teeth graze her along the top of her right shoulder."
    na "Astra groans, and I can tell by the sound that she's biting her lip in an attempt to keep from crying out."
    an "{i}Ah{/i}— You're terrible."
    fn "Am I?"
   
    nvl clear

    an "Yes!"
    na "I lift my head away from the crook of her neck. Not even trying to hide the wild grin on my face." 
    na "However, I do slow down enough for her to catch her breath, sensing that she has something else to say."
    na "Astra's eyes open, iris' flitting across my face. Upon capturing my expression, she smiles."
    na "(So bright…)"
    na "(If only I could bottle up that smile and keep it.)"
    na "(Though I guess it wouldn't be fair for me to monopolize such a beautiful thing.)"
    an  "Fe—"
    na "It's all too easy to get lost within that train of thought."
    na "One thing leads to another until I'm thinking about all the happiness that Astra's shared with me…"
    
    nvl clear

    an "Felix?"
    na "A gentle palm on my cheek and a fond laugh pulls me back to the present."
    na "I blink, eyes refocusing."
    an "There you are."
    fn "Sorry. I was just—"
    na "She shakes her head."
    an "Don't apologize. I just have a question."
    fn "Anything."
    an "Can I have my arm back now? It's starting to fall asleep."
    na "All at once, I realize the tight grip I have on her left wrist; holding it above her head."
    fn "Oh. Sorry."
    na "My hold loosens, and Astra lowers her arm with a sigh of relief."

    nvl clear

    na "Looking at her wrist shows that it's a little red."
    na "My teeth worry at my bottom lip."
    fn  "Astra, I—"
    na "I start to worry that I've actually hurt her, but when she looks up at me she has a large grin on her face."
    na "Not a moment after that, hands are wrapping around the back of my neck, pulling me into a heated kiss."
    fn "Mmm..."
    na "( I think kissing is my favorite.)"
    na "Like Astra before, my own eyes close in pleasure. Our tongues dance together."
    na "When I suck in a sharp breath, Astra takes it as her chance lick a wide stripe across my teeth before diving right back in for more." 
    na "She's passionate… and every shift of her body pushes me closer to the edge."

    nvl clear

    na "Heated pants leave my mouth, further warming Astra's already hot cheeks. Unconsciously, my hips cant forwards—now flush against the backs of her thighs."
    na "My eyes feel heavy, though they crack open when I feel the pull of lips away from mine."
    na "A trail of split still connects us, broken when Astra's tongue sweeps over her lips."
    an "I'm okay. Keep going."
    na "I touch my forehead to hers."
    fn "That, I can do."

    nvl clear

    play music "Felix.ogg" fadeout 2.0 fadein 2.0
    scene studio_dawn with dissolve

    na "The first sensation I feel when I wake up is cold."
    na "Rather, what bothers me is the distinct lack of warmth."
    na "My eyes snap open."
    na "(She's not here.)"
    na "A slight panic infects my voice."
    fn "Astra?"
    na "In a flash, my legs are swinging off the bed—the floor is icy under my feet."
    na "Next, I descend the stairs leading from the loft."
    fn "Astra??"
    na "Before I can call out again, Astra intercepts me. She appears from the kitchen with a worried look on her face."
    an "I'm here. I was trying not to wake you."
    an "I didn't mean to scare you. Are you okay?"

    nvl clear

    na "Just seeing her face causes my heart rate to slow back down."
    fn "Yeah… I'm okay."
    an "Was I too loud?"
    fn "No, I was just—the bed was cold."
    na "She nods and the furrow of her brow soothes."
    an "Ah, sorry. Want me to wake you next time?"
    na "My heart constricts at her consideration."
    na "(I don't want to burden her but—)"
    na "(She'll probably end up doing it either way.)"
    fn "...If you want to. I—"
    fn "It would help."
    na "One. Two. Three steps… and Astra covers the distance between us."
    
    nvl clear

    na "Her arms wrap around me, and I mirror her, with the addition of a kiss on her cheek."
    an "Consider it done."
    na "(She does it so easily. Stepping over gaps that I once thought were too wide to cross.)"
    na "I tighten my arms around her." 
    na "She smells like coffee."
    fn "Thank you."
    fn "...How are you feeling?"
    na "Her laughter reverberates against my chest."
    an "I feel amazing… How do {i}you{/i} feel??"
    fn "Like we should crawl back into bed. It's still early."
    an "I have to work soon."

    nvl clear

    na "I glance to the window to see that the sun has only just started to rise."
    na "A three-step plan begins to form in my mind."
    na "Step one. Pleading."
    na "I give her my best puppy dog eyes."
    fn "You still have a couple hours left, yeah?"
    fn "Just enough time for a quick nap."
    na "Astra states blankly."
    na "(Damn. I really thought that would work.)"
    fn "...Please?"
    an "But— We just woke up."
    na "(That's not a no. I can work with that.)"
    na "Alright… step two. Negotiation."

    nvl clear

    fn "One hour."
    fn "Just one hour… You don't even have to sleep."
    na "This time, she hums."
    na "(Almost there.)"
    na "Time for step three. Act cute."
    na "A dirty tactic? Maybe."
    na "(But if this is what it takes to get her to relax for just a bit longer…)"
    fn "...I just want to hold you for a while. You have to go back to your place tonight right? I'm going to miss you."
    an "..."
    na "(If this fails, I'll let it go.)"
    an "That does sound nice…"
    na "(Yes!)"

    nvl clear

    na "I pepper kisses across her face until she starts giggling."
    fn "Then what are we waiting for? Let's go!"
    na "I take her hand, and together we climb the stairs back to the loft."
    na "My eyes rove over the bed, and I take a moment to appreciate myself for changing the sheets before passing out last night."
    na "(Thank you past Felix.)"
    na "The backs of my legs hit the mattress as I sit down at the edge of the bed. I pull Astra into my lap, and she goes easily."
    na "Once I have her secured, I lean us both backwards until we hit downy sheets."
    fn "Ahhh~ Perfect."
    na "A kiss is placed under my jaw."
    an "Your master plan worked."
    fn "Ah— You knew?"

    nvl clear

    na "She chuckles."
    an "Of course I did… but—"
    an "I wanted you to hold me too."
    na "(!!!)"
    na "If my arms weren't full of my favorite person…  I would be clutching dramatically at my chest."
    na "(I'm so glad she can't see my face right now.)"
    na "I clear my throat."
    fn "...Well. Isn't that convenient."
    na "Instead of responding, Astra tucks her head more firmly against my chest."
    na "..."
    na "We settle into a peaceful silence. And—eventually—I notice her breaths even out."
    
    nvl clear

    na "(She's asleep.)"
    na "(...Good.)"
    na "She still worries me sometimes… After all, bad habits don't change overnight."
    na "(Though, that goes for both of us.)"
    na "My hand stokes her hair as I think."
    na "(I still have my own things to work through.)"
    na "There are still days where fear grips my heart, and I isolate myself."
    na "(...But between Astra and Velvet, I'm never allowed to stray too far.)"
    na "Similarly, it's easier to pull myself out of a spiral."
    na "My palms runs over Astra's back, and I whisper—"
    fn "{i}Thank you…{/i}" 
    na "Shortly after, I drift peacefully into the land of dreams. {w} A place that no longer scares me as much as it did before." 

    stop music fadeout 2.0
    window hide
    $ renpy.pause(2.0)
    return
    

label felix_afterstart2:

    
    na "The studio is dim, lit only by the flickering flames swinging overhead. I sit in one of the bar stools watching Felix stir a pot of mushroom soup, listening to him hum softly."
    na "He asked me to clear an evening a few days ago. All in preparation for tonight."
    na "Earlier, he'd come in laden with fresh ingredients and the valiant declaration that he was going to make my favorite dish for dinner… Apparently he's been having 'secret lessons' with Vel. Not because he's a bad cook, but because he wants it to be perfect."
    na "At least, that's the reason I've been given. I have a feeling that he's simply jealous that I might like some random restaurant's food more than his."
    an "Are you sure you don't want help?"
    na "Felix turns around with a grin."
    fn "You {i}are{/i} helping. You're my moral support."
    an "Alright then."

    nvl clear

    na "Pushing myself off of the counter, I sweep up into the space beneath his arm. The one not holding the ladle."
    na "Felix may not be very tall compared to others, but he's the perfect height for me to snuggle into."
    na "I feel, more than hear, the content sigh he lets out as he squeezes me tight. Together, he turns us back to the bubbling pot."
    an "It smells delicious."
    fn "I hope it tastes good too."
    an "I have no doubt."
    na "Tucked up close to Felix like this, I can smell faint wisps of his favorite colonge—a mix of florals—underneath the scent of mushrooms and acrylic."
    na "Unconsciously, I begin to relax. I let more of my weight press into Felix's side."
    na "He huffs out a laugh, but doesn't say anything."
    na "We watch in comfortable silence for a time, until Felix shifts his arm from around my shoulders." 
    
    nvl clear
    
    fn "Sorry, I need both of my hands now."
    an "*sigh* Do you really?"
    fn "Haha! Yes, I do. Just for a few minutes, then the soup will be done and we can eat."
    na "Reluctantly, I pull away and step towards the cooler."
    an "I'll make us drinks. What do you want?"
    fn "I—"
    an "Fe. I can pour a couple drinks. Do you want tea? Water?"
    fn "...Tea. Iced, please."
    an "On it!"
    na "(...)"
    an "Oh, you restocked! …There's a strawberry tea here that sounds really good—should we try it together?"
    
    nvl clear
    
    na "Felix chuckles knowingly in my periphery."
    fn "I thought you might like that. Two strawberry teas then."
    na "(...)"
    na "In the time it takes me to brew the tea and then add ice to Felix's, he's finished up the soup. Two bowls are set at the bar. A matching set bought after I discovered Felix's sad arrangement of tableware."
    na "When they aren't in use, they're kept on the most visible shelf in the kitchen. Like decoration."
    na "I sit down first."
    an "Thank you for making dinner."
    na "Felix slides into the remaining stool, but not without placing a soft kiss to my cheek."
    fn "You're welcome. If you like it, I can make it whenever you want."
    an "(Wait for it…)"

    nvl clear

    fn "Then you won't need to go over to Onyx all the time."
    an "Aha! I knew it! You {i}are{/i} jealous!"
    fn "People don't get jealous over restaurants."
    an "Denying your own existence?"
    na "His lips twitch. The facade is cracking."
    fn "...You go there multiple times a week!"
    an "Because they make great soup!"
    na "The mask falls off. Felix breaks into a full grin, and starts laughing."
    fn "Fine, I've been caught red-handed. I made you, hopefully delicious, mushroom soup as part of my secret plan to monopolize more of your time."
    fn "Happy?"
    an "Extremely."

    nvl clear

    na "We sit there, smiling like fools instead of eating. Felix scoots his chair across the floor until he's close enough to kiss me. Which is exactly what he does."
    na "He pulls away and bumps my shoulder playfully."
    fn "Let's eat."
    an "Wait—"
    na "Felix raises an eyebrow, hand halfway to his spoon, waiting."
    an "Even if this is the worst soup I ever eat, I'll still prefer it over Onyx's."
    an "Because you made it for me."
    an "I love watching you cook… I love {i}you{/i}. You don't have to make the perfect meal to get me to come over. You just have to ask."
    na "We still sit facing each other. Our knees brushing together. Felix moves his hand from where it had almost grabbed a spoon, and tangles it with mine."
    fn "...You're going to kill me one day."
    an "With kindness?"

    nvl clear

    fn "Yeah."
    na "He looks up then."
    fn "I love you too. I know I don't have to work to keep you here… That you stay because you want to."
    na "His grip tightens. His other hand comes to tug at his locs."
    fn "...Sometimes I just have trouble believing it. It was a silly thought—that if I master your favorite meal, I could use it like a spell." 
    fn "My own special magic to call my wonderful girlfriend to my side."
    an "It's not silly, Felix. If I could create a spell to call you over whenever I wanted, I'd do it in a heartbeat."
    an "So— Why don't we make one?"
    fn "...Huh?"
    an "Let's make a spell. Right now."
    fn "But— Neither of us have magic? Unless you've been keeping secrets~"

    nvl clear

    an "Haha, no secrets. Why don't we agree on our own secret password? One we can use whenever we need some extra love and care. No questions asked." 
    fn "...Like a safeword?"
    an "N-no! …Wait. Yes?"
    an "I guess it {i}is{/i} the same idea… but that's not what I meant!"
    na "Felix shines like a star on a cloudless night. He beams, any melancholy which had lingered there before has now washed away."
    fn "I'm messing with you. It's a great idea, Astra. I love it."
    fn "Do you have something in mind?"
    an "What about 'sunflower'? It's your favorite flower."
    fn "...It is."
    an "No good? …I can pick something else."
    fn "I do love sunflowers, but why don't we go with something that represents both of us? Not just me."
    
    nvl clear

    an "(Both of us?)" 
    na "I glance around the studio in search of inspiration when my eyes catch on something."
    an "Strawberry?"
    na "Felix's eyes narrow, and he looks to his left."
    fn "You know I only bought that tea for you, yeah?"
    an "Yes… but I only drink tea because of you to begin with! I think it counts."
    na "A reverent kiss is placed on my knuckles as Felix pulls our joined hands to his lips."
    fn "Saints, I love you so much."
    an "Does that mean you like it?"
    fn "Yes. 'Strawberry' is a perfect safeword."
    an "Don't call it that!"

    nvl clear
    scene studio_night with dissolve

    na "(...)"
    na "The night winds down after that. Dinner is cold by the time we finally start eating, not that it matters. Every bite is delicious."
    na "Felix collects the dishes to pile them in the sink before carefully storing the leftovers in the cooler."
    na "Once again, I've been asked not to help. Relegated to watching, I remain perched at a counter stool."
    an "(At least the view is nice.)"
    na "I want him to finish faster. The sooner the better."
    an "The dishes can be done in the morning Fe. You don't have to clean everything tonight."
    na "He responds without turning to face me, but I can hear the teasing lit of his voice just fine."
    fn "Getting impatient?"
    an "And you're not?"

    nvl clear

    fn "I'll be able to relax better if I clean now."
    an "No offense. But this place is a wreck."
    fn "I can't do anything about the paint, babe. It's an occupational hazard. But these dishes? That's something I can deal with."
    na "I begin to trace nonsensical patterns along the counter. Felix leaves dishes in the sink all the time. Which could only mean one thing."
    an "(He's being slow on purpose.)"
    an "It'd be a lot faster if I helped you."
    fn "No can do."
    na "Dishes clatter together in the sink as he washes. He takes his time with it, and I swear I watch him wash the same bowl a second time."
    an "Felix."
    fn "Hmm~"
    an "..." 

    nvl clear

    na "Just as I had earlier, I slip off my seat and into the kitchen. Hugging Felix from behind is easy with both his hands occupied. I hook my chin over his shoulder to get a better view of what he's doing."
    fn "I'm almost done, promise."
    na "I squeeze him as hard as I can, until he wheezes dramatically."
    na "Finally, {i}finally{/i}, the last dish is washed and set aside. Felix dries his hands on a stray cloth and turns around to embrace me properly. He punctuates the gesture with a kiss to my forehead."
    fn "Alright, all done."
    an "Yeah? Sure you don't need to wash that pot a second time?"
    na "He hums, noncommital."
    fn "I could, but I think I've teased you long enough."
    an "At least you admit it."
    fn "It's just too fun, but I'm all yours now. Anything you want, just say the word."

    nvl clear

    na "Instead of words, I put my desires into action. A tilt of my head, a lingering kiss to his lips."
    na "He sighs into it. Hands slide down to my hips while my own hands sneak up his back to grasp at a few of his locks."
    na "The kiss deepens, someone's mouth opens—I'm not sure whose—a gasp, another sigh. Felix pulls and I tug."
    na "My eyes are closed. All of my senses are heightened. Everything between us is amplified, the groans Felix makes everytime I nip at his bottom lip, the rustling of our clothes, the floral scent of cologne."
    na "Gently, and without breaking our kiss, I guide Felix to a clear section of countertop and press him into it."
    na "He pulls away for a second—lips and hands—taking in deep breaths to make up for what was lost."
    na "Quick on the uptake, Felix places his hands to the counter behind him and uses it as leverage to pull himself up onto it. As soon as he's comfortable, he drags me into the space between his legs and leans down to reconnect our lips."
    
    nvl clear
    
    na "The feeling of being boxed in by Felix's warmth sends a thrill up my spine."
    na "I break away next, needing to catch my breath. Felix takes the opportunity to flutter kisses anywhere he can reach from his perch."
    na "The next time he makes it to my lips is when he dives back in."
    na "It feels right. It feels perfect."
    na "(...)"
    na "Around my waist, Felix's thighs tighten. Then—he lets out what I can only describe as a whine."
    na "Our lips part again. Felix smiles cheekily. I smile back."
    an "Should we take this upstairs?"
    na "His reply is a breathless:"
    fn "After you."
    na "I take both of Felix's hands in mine, keeping them held tight as he slips off the counter. Together, we climb the steps to the loft."
    
    nvl clear
    
    na "The bed is piled with blankets like usual. Felix says it's because he enjoys the weight of them and, after so many nights spent here, I have to agree."
    na "Now though, the blankets are set aside to make room for more pressing activities."
    na "With the bed clear, Felix is free to fall onto it. His arms spread out wide spanning the width of the mattress."
    na "I laugh, and climb happily into bed with him. Our limbs tangle together like vines."
    na "For a few minutes, we simply hold each other. The rise and fall of his chest is soothing and the circles he rubs over my back start to lull me to sleep."
    na "It's not the turn of events we had planned, but it's just as satisfying."
    na "More time passes, I'm not sure how much, but eventually Felix's hand stops moving. I steal a peek at his face which has gone slack with sleep."
    na "I curl up closer, and tug a stray blanket over the both of us. Sleep has been hard for Felix to come by the last few days, so it's a relief to see him finally get some rest."
   
    nvl clear

    na "With only the sounds of Felix's deep breaths, I close my own eyes."
    na "..."
    an "(Good night, Felix.)"

    stop music fadeout 2.0
    window hide
    $ renpy.pause(2.0)
    return


