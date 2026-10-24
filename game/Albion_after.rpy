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

init python:
    config.nvl_paged_rollback = True

# Apply this callback to dialogue
define config.all_character_callbacks = [text_scroll_sound]

define aln = Character('ALBION', kind=nvl, color="#df6f98")
define an = Character('ASTRA', kind=nvl, color="#7e6fd6")
define ln = Character('LILY', kind=nvl, color="#eb8b33")
define na = Character(None, kind =nvl)

label albion_after:

    $ persistent.status_button = False
    
    show albion_after
    $ renpy.pause(1.0)
    window hide
    pause (5.0)
    window auto

    play music "albion.ogg" fadeout 2.0 fadein 2.0
    scene albionapt with dissolve

label albion_after2:
   
    "Which of Albion's after stories would you like to play?"

    menu: 

        "After Story #1 - Love (Albion POV)":
            jump albion_content_warning1
        "After Story #2 - Family (Astra POV)":
            jump albion_after_family
  

label albion_content_warning1:

    "This story contains some mild written NSFW content."

    menu: 

        "Continue":
            jump albion_afterlove
        "Go Back":
            jump albion_after2
        "Return to the main menu.": 
            return


label albion_afterlove:
   
    play music "cafebloom_night.ogg" fadeout 2.0 fadein 2.0
    
    scene cafe_interior_night with dissolve

    na "(…)"
    na "I glance over to Astra from where I stand next to the sink holding her things as we're about to close. She's almost done washing the dishes."
    na "The warm lighting of the café bounces off of her cheeks, making her skin glow."
    na "A soft smile rests on her face when she turns to me. Something in my chest skips a beat at the sight."
    an "Albion?"
    na "She takes off bright pink gloves and glances over her shoulder at the empty café."
    na "I hum in acknowledgement, afraid of what I might say if I open my mouth."
    an "Was this the last of the closing tasks?"
    aln "Yeah."
    na "She huffs, the way she does when she realizes one word is all she's going to get from me."
    
    nvl clear

    na "I step closer to her. She puts a hand on my arm and runs it down to my wrist, finally stopping to grab my hand. Warm—"
    na "(Distracting.)"
    an "Alright then, shall we go?" 
    aln "Mhm."
    an "You're quiet today."
    na "I raise an eyebrow."
    an "Quieter than usual."
    na "I meet her worried gaze, a smile tugging at my lips."
    aln "Just thinking."
    an "All good thoughts I hope."
    aln "Very good thoughts."

    nvl clear

    na "My hand is squeezed tightly as Astra beams."
    an "If you say so... Thanks for grabbing my bag."
    na "She leans up for a kiss, which I grant. When she pulls away, her cheeks are dusted pink."
    na "(...Distracting.)"
    an "See you tomorrow?"
    na "I sigh."
    na "To be honest, I'm getting tired of seeing her tomorrow. I wanted… I want to take her home with me."
    aln "No."
    an "No? Oh, sorry, are you not on the schedule tomorrow? I thought you were."
    aln "I am."
    na "Her brows furrow. She looks confused."

    nvl clear

    an "Okay…?"
    na "(She's going to kill me with cuteness one day… And I just might let her.)"
    aln "Stay at my place tonight."
    an "H–huh?"
    aln "You always say 'see you tomorrow'. When you can just come home with me."
    an "I— I guess that's true."
    na "I try not to let it show, but my heart is currently trying to beat out of my chest. Though, I know Astra can probably tell. She always sees right through me."
    aln "Will you?"
    an "...Lead the way."

    nvl clear

    play music "Albion.ogg" fadeout 2.0 fadein 2.0
    scene albionapt_night with dissolve

    na "The walk home is filled with Astra's excited chatter about her latest dessert trials. With winter on the horizon, Café Bloom is gearing up to launch a new seasonal menu."
    na "The spring launch had been so successful that Sylphia had tasked us with creating a new pairing for each season. Astra had commandeered my kitchen more than once… Apparently mine is bigger."
    na "(I'm still getting used to it. Letting her in, but—)"
    na "I look to my right. At her bright smile. At the sparkle in her eyes as she talks about her latest creations—"
    na "(she never fails to quell my lingering anxieties.)"
    na "In no time, we reach the door to my apartment, and as soon as we step inside I let my influence over the wind drop—allowing the chilly breeze to flow uninterrupted once more."
    na "Still at the entrance, Astra stops to remove her shoes. Then, reaches past me to grab the purple slippers I'd bought for her from where they sit neatly on the shoe rack."
    
    nvl clear

    na "I do the same."
    aln "Are you hungry?"
    an "...Maybe later."
    na "Now that we're inside, the atmosphere seems heavier. The possibilities for tonight are their own Pandora's box."
    na "Astra speaks next."
    an "Shower?"
    na "We haven't moved away from the door. I shift my weight to my other foot… but it does nothing to distract from the building heat."
    aln "Together?"
    na "She looks up at me. "
    an "Is that okay?"
    na "I think about it for a moment. {i}Is{/i} it okay?"

    nvl clear

    na "(Who am I fooling?)"
    aln "Of course." 
    an "Then—"
    aln "I'll just—"
    na "She giggles. Then motions for me to continue."
    aln "...I'll go set up the bathroom. Wait in the living room?"
    an "Copy."
    na "I shake my head, but some of the tension falls away."
    na "Before she can step away, I plant one more kiss on her lips. Longer than the last one… more passionate."
    na "There should be no question of what I want to do tonight."
    na "(And— I hope she wants the same.)"

    nvl clear

    na "She sighs, and the heat of her breath puffs against my lips. She tastes like cinnamon—leftover from Bloom's signature fall blend that I came up with. The thought sends a shiver of possessiveness down my spine."
    na "My hands grasp for her waist, holding fast to the fitted turtleneck she's wearing today."
    na "In response, her fingers reach up into my hair. She pulls at the base of my ponytail forcing a gasp to escape."
    na "(Saints.)"
    na "(I'm supposed to be paitent—!)"
    na "Instead, my leg moves forwards pushing to make space between hers."
    na "She hums lowly into my mouth. Her body goes limp—as evidenced by the way I suddenly have to brace my arms against her added weight."
    na "(Wait— We're still in the doorway.)"
    na "It's no use. Each coherent thought is interrupted by Astra. A nip to my bottom lip, her tongue against the roof of my mouth, her fingers scrapping lightly over my scalp..."
   
    nvl clear
    
    aln "Astra—"
    an"Hmm?"
    aln "We should—"
    na "Cold fingers push underneath my sweater."
    aln "Mm—"
    na "It's all I can do to keep any embarrassing noises from escaping. However, I fear my attempts are futile if the smirk sliding across my cheek is anything to go by."
    na "In retaliation I walk her into the wall next to the door. At the same time pulling her down—hard—against my thigh."
    na "She gasps—and the hand that's snaked its way up my back curls into a fist."
    na "The other one tugs the ribbon out of my hair. Distantly, I notice that she makes sure to tuck it into my back pocket rather than dropping it onto the floor."
    an "Ah— You're playing a dangerous game, Albion."

    nvl clear

    aln "Good. That's exactly what I want."
    na "I lean down to kiss her again, a little softer but no less enthusiastic."
    na "After a few moments she breaks it off to say—"
    an "Mmm, we really should shower first though."
    na "So she says. Yet she makes no attempts to break free. Something she could easily do if she wanted."
    na "Her hand twirls one of my loose locks around her finger. Occasionally tugging."
    na "(Menace.)"
    aln "Yeah…"
    an "Yeah? Why don't you move then?"
    aln "Why don't you?"
    an "Touché."

    nvl clear

    na "We stare at each other, neither wanting to be the one who breaks first."
    na "(So competitive… even now.)"
    na "I loosen my grasp on her hips, easing her off my thigh gently. Try to ignore the lingering heat—and fail."
    na "My eyes close, and I take a few deep breaths."
    na "When I open them again, Astra is smiling at me softly."
    an "I'll wait in the living room, okay?"
    aln "Okay."
    na "Setting aside towels and clothes doesn't take me very long. Before long, the bathroom mirror starts to fog up—signaling that it's time to call for Astra."
    aln "Astra, you can come in now."
    na "Within seconds Astra appears looking eager as ever."
    na "(It's hard to be nervous when she looks like that.)"

    nvl clear

    na "The door clicks shut and Astra steps into my personal space once again."
    na "I can't keep my eyes off of her—every movement she makes has me falling deeper in love."
    na "(Love?)"
    na "I freeze."
    an "Albion?"
    na "(I love her?)"
    na "A tentative hand caresses my cheek."
    na "(Saints. I love her.)" 
    na "Her eyes search mine."
    an "…Do you want to stop? We can just take turns in the shower— Or, I can go home?"
    na "That snaps me out of it— There's no way I'm letting her leave now. At least, not like this."
   
    nvl clear

    aln "No— I'm alright."
    an "You're positive?"
    aln "Yes."
    na "I cover the palm on my cheek with my own."
    aln "Stay."
    na "I lift the bottom edge of her turtleneck. A question."
    aln "We're wasting water just standing here. Can I?"
    na "It's a poor deflection, and we both know it."
    na "It's impossible to waste water in Halis. Every drop is unable to be contaminated in any way, and thus, every drop is recycled."
    na "It seems to be enough to convince Astra that I'm alright since she raises her arms above her head. Her face is beet red, but the wild grin on her face is more than enough reassurance." 
    
    nvl clear

    na "I pull her shirt over her head, kissing her once in the lips after successfully removing the garment."
    na "A palm, now warm, slips carefully under my own shirt."
    an "Your turn?"
    na "I could do it myself, but just as I enjoyed doing it for her, I'm sure she thinks it's more fun to return the favor."
    aln "Go ahead."
    na "Astra pushes her fingers under the edge of my sweater and tugs it off."
    na "After that's taken care of, Astra wraps her arms around me."
    na "Her face pushes into my chest and the fabric of her bra tickles my skin pleasantly." 
    na "I fold her into my arms. I hold her until she leans back—satisfied."
    na "Next, I hook a finger into her bra."
    aln "Can I take this off?"

    nvl clear

    an "We can't get in the shower unless you do."
    aln "Just checking."
    na "The undergarment unclaps with ease. I set it on the small pile of clothes forming in a corner of the bathroom."
    an "Done that before have you?"
    aln "I have some personal experience. At least it's good for something."
    an "Handy~"
    na "She combs her fingers through my hair reverently."
    an "I think this is the first time I've seen your hair down."
    aln "I prefer it up. Otherwise it just gets in the way."
    an "Then why not cut it?"
    aln "Maybe because I like how it feels when you pull it."
    an "O-oh."

    nvl clear

    na "Now it's my turn to smirk."
    na "(...Beautiful.)"
    na "She doesn't miss a beat in leaning up to kiss me. I suspect it's a ruse to cover up her embarrassment. Not that I care either way."
    na "She pulls away first."
    an "Pants?"
    aln "Mhm."
    na "She huffs, but starts to pull off the rest of her clothes. With one leg out of her slacks, she glances up at me."
    an "You're staring."
    aln "Want me to look away?"
    an "No. I want you to take your pants off." 
    na "(How direct.)"

    nvl clear
 
    na "In the end, both of us stand naked surrounded by steam. One step closer to the shower."
    na "Astra's eyes don't betray a hint of uncertainty."
    an "Still good?"
    na "My mouth feels dry."
    aln "Mhm."
    an "Come on then. In we go."
    na "She pulls me into the shower and, somehow, the two of us manage to fit. Astra stands further away from the water, trying not to get her hair wet."
    na "Which means that my hair gets soaked instead."
    na "It occurs to me that I've never allowed anyone to see me like this. Make-up rinsed off. Hair undone. Quite literally—naked, in every sense of the word."
    na "Unconsiously I grab for Astra hand."
    na "Without a word, like she can read my thoughts, she reassures me."

    nvl clear

    an "You don't have to be perfect with me, Albion."
    aln "Well I'm certainly not perfect right now. I feel like a wet cat."
    na "She hums and smiles softly."
    an "And I love you all the same."
    aln "..."
    aln "...!"
    aln "What was that?"
    an "What was what?"
    an "..."
    an "Her face cycles through a series of emotions. Confusion, shock, embarrassment, and finally… fear. I feel her hand jerk, trying to pull away."
    an "I hold it tighter."
    an "Albion, I—"

    nvl clear

    aln "Say it again."
    an "W-what? No way. It's embarrassing!"
    an "I mean, we've only been dating for a few months! It just slipped out—"
    na "(Again.)"
    aln "Say it again—"
    na "I let some of my desperation seep into my voice."
    aln "Please."
    an "..."
    na"She looks down at our feet."
    an "I love you."
    aln "Hm?"
    an "I love you, Albion."

    nvl clear

    an "There... Happy now?"
    aln "..."
    na"She looks back up."
    na "Surprise overcomes hesitance. Her eyes dart across my face, and I know it's because of the grin I wear. Unlike usual, I can't quite keep my lips together."
    na "Quickly—but carefully—I turn her body to face away from me. She doesn't fight it, but her head cranes over her shoulder in an attempt to catch another glimpse."
    na "I push her face forward again. Then, I pick up a cloth and lather it with soap."
    na "Gently, I run the cloth over the skin of her back. Sometimes reaching around to wash her arms and chest."
    na "She doesn't say a word."
    na "When I have control of my facial muscles again, I lean down to kiss the back of her neck."
    aln "...I love you too."

    stop music fadeout 2.0
    window hide
    $ renpy.pause(2.0)
    # ... some actions ...
    # Clear the return stack so the next 'return' goes to the main menu
    return
   

label albion_after_family:

    scene albionapt_dawn with dissolve
    #play music "albion.ogg" fadein 2.0

    an "(...?)"
    na "I distinctly remember falling asleep in Albion's arms, which usually shield me from the morning chill. And yet..."
    na "A shiver runs through me."
    na "I shift under the sheets, maneuvering until I face Albion's side of the bed."
    an "(Oh.)"
    na "I can't stop myself from grinning."
    na "Taking up Albion's usual spot is Lily, tucked safely within her father's arms and drooling onto his shirt."
    na "Albion's eyes are open, watching me."
    aln "Morning."
    an "Good morning."
    na "My eyes fall to Lily."

    nvl clear

    an "Is she drooling?"
    aln "Yeah."
    aln "...She snuck in here a few hours ago. A nightmare, I think."
    na "I reach out a hand to clear Lily's uncombed hair away from her face."
    na "They had adopted the young elf two years ago. Her life beforehand is a mystery, but the nightmares tell them all they need to know."
    an "She doesn't like the dark. Maybe we should light a lamp for her at night."
    aln "Her magic is too unpredictable right now. She might accidentally start a fire."
    na "Albion presses a kiss to Lily's forehead."
    aln "If she's afraid she can just sleep here with us."
    an "Being a dad has made you all soft... It suits you."
    na "Albion's face scrunches up in a poor attempt at feigning disgust."
    aln "Whatever."

    nvl clear

    na "When he relaxes again, his eyes gleam with fondness."
    aln "...Come here."
    na "He lifts the blankets with his free hand."
    an "I don't want to wake her..."
    aln "You see her don't you? She's not waking up anytime soon."
    na "It's the clearest invitation I'll get, so I take the chance to cuddle up close. Lily doesn't stir."
    na "Soft pink light spills into our bedroom. Still a couple hours before the sun truly rises. More than enough time to catch a bit more sleep."
    na "Closer now, I lower my voice."
    an "We don't have anywhere to be right?"
    aln "Mm, no. But I thought we could take Lily to the park."

    nvl clear

    an "A picnic?"
    aln "Sure."
    an "Okay."
    na "Snuggled back in Albion's warm embrace and soothed by Lily's soft snores, my eyes start to fall closed again."
    na "I feel Albion squeeze the two of us tighter just before I drift off."

    nvl clear
    scene albionapt with dissolve
    play music "cafebloom_day.ogg" fadeout 2.0 fadein 2.0

    na "The bed is empty when I wake up again. My family's absence is highlighted by a bright patch of sun coming through the open window and pools over the spot where they had been just a couple hours ago."
    na "Albion always opens all the windows as soon as he wakes up. The breeze that comes in makes him feel calmer. At least, that's what he says whenever I bring it up."
    na "From the kitchen I can hear the excited chipper tones of Lily's voice sometimes broken by Albion's occasional hums of acknowledgement." 
    ln "All done?"
    aln "Not yet."
    ln "Oh."
    ln "How long?"
    aln "Five more minutes, Lily."
    ln "Okay!"
    ln "..."

    nvl clear

    ln "...all done?"
    na "Albion may have infinite patience for his daughter, but I feel I should save him anyways."
    na "I slip out of bed and down the short hallway to the kitchen." 
    an "What are you two making?"
    ln "Pancakes!"
    na "Lily rushes over to me, and I scoop her up into my arms out of habit. She squeals in delight as I lift her up high before settling her against my hip."
    na "I walk us over to where Albion stands by the stove pouring speckled batter into a pan. Some of it sticks to his cheek, which can only mean he let Lily help with the mixing."
    na "I grab a stray towel to wipe the batter from his face."
    aln "Thanks."
    an "Mhm—What did I miss?"

    nvl clear

    aln "Not much. Lily wanted pancakes for breakfast."
    na "He shrugs."
    aln "Just something to tide us over until later."
    na "He specifically avoids mentioning the park. Lily will get too excited if we bring it up now. Better to focus on one thing at a time."
    na "First and foremost—breakfast."
    an "Do you need me to help with anything?"
    aln "I've got it. You're helping enough by keeping Lily away from the stove."
    na "Albion looks at me and then at Lily pointedly."
    aln "She wanted me to hold her and cook at the same time."
    ln "I wanna watch!"
    aln "You can watch now that your mother has you. I need both of my hands to make your food, Lily."
    
    nvl clear
    
    na "I readjust Lily in my arms so she can see Albion better. I try not to get too emotional about how fast she's growing."
    an "You're spoiled, you know that little Lily?"
    ln "Spo-eld?"
    an "Mhm, it means we love you so much that we want to make you happy, even when it's a little impractical."
    na "Albion chimes in."
    aln "Like when you want your pancakes to be pink."
    an "Pink?"
    aln "Yes." 
    an "(They {i}do{/i} seem to have a bit of a pink hue to them.)"
    an "How did you do that?"
    aln "Raspberries."

    nvl clear

    ln "I like razzberry!"
    na "A swirl of wind blows a gentle puff of air against Lily's face sending her into a fit of giggles."
    na "Still cooking, Albion fights a smile."
    na "I hug our daughter closer and nuzzle my cheek against hers."
    an "Sounds delicious~ Now I'm excited too."
    na "Careful to mind the flames, I press a kiss to Albion's cheek."
    an "Thank you."
    na "He does his best to look unaffected, but I can clearly see the tips of his ears turn red."
    aln "Mm."
    na "Albion lifts the final pancake off the pan and adds it to the stack next to him. The stove shuts off with a click, and Albion pokes at Lily's cheek."
    aln "Okay, {i}now{/i} all done."

    nvl clear

    ln "All done!"
    na "He carries everything over to the dining table. A neat stack of raspberry pancakes set at the center along with a small container of maple syrup. I put Lily down and guide her to her usual seat."
    na "Like a well-oiled machine, I start to plate Lily's food and cut it into bite-sized pieces while Albion heads back into the kitchen for drinks."
    na "He returns a few minutes later with a sippy cup of watered down juice for Lily, and coffee for us."
    na "First Bloom has been the staple blend in the Vale household for the past seven years. Even after making a whole catalogue of seasonal blends for Café Bloom, the first one remains his favorite."
    na "With Lily situated and already digging in, I take the seat next to Albion across the table."
    na "As soon as I take my seat, Albion reaches for my hand. He tangles our fingers together with a content sigh."
    an "Albion?"

    nvl clear

    aln "Hm?"
    na "I lift our joined hands."
    aln "You can eat with one hand."
    na "My heart clenches."
    an "(When did he learn to be this cute?)"
    an "...I love you."
    aln "I love you too."
    na "Lily interrupts, mouth full of pancakes."
    ln "Me too?"
    na "The corners of Albion's mouth tugs upwards. He tilts his head down towards the table to hide it. I reach my free hand over to pinch at Lily's cheek gently."
    an "Yes, we love you too."

    nvl clear

    an "Right, Albion?"
    na "Albion lifts his head up, then clears his throat."
    aln "Of course. We love you the most."
    na "Lily nods, apparently satisfied and stuffs another mouthful of food into her mouth."
    na "Albion squeezes my hand once before letting go."
    aln "Let's eat."
    
    nvl clear

    na "By the time breakfast ends, Lily has made a mess of herself. He's gotten used to it over the last two years, but I still notice the slight grimace that crosses Albion's face at the sticky syrup on Lily's hands, and the crumbs littering the table."
    an "I'll clean up. Why don't you go change?"
    aln "...Are you sure?"
    na "A quick glance over Albion is enough to make me double down. He's holding the center of his shirt, pinching to keep it from touching his skin."
    an "I'm sure. I'll have this all cleaned up by the time you get back."
    aln "I won't take long. Just—a quick shower."
    an "Take your time."
    na "He softens a little, leaning in for a chaste kiss."
    aln "I love you."
    an "Love you too."

    nvl clear

    na "Albion pets over Lily's hair as he passes by."
    aln "Be right back."
    na "Lily waves to Albion's retreating figure like he's going on a long trip and not the bedroom."
    na "I watch the small interaction with a fond gaze because, no matter how many of them I see, I never get tired of them."
    na "No one could have predicted how much Café Bloom would change my life. That because of that one decision I would end up here, with a family of my own."
    na "It takes all my willpower to shake off my encroaching tears and throw myself into cleaning."
    na "When Albion returns, everything will be back to how it was before. The three of us will start preparing for our picnic later, and I'll witness a dozen more of these precious moments before the day is over."
    an "(I can't get emotional {i}every{/i} time.)"
    an "(Gotta save it for the extra special moments...)"

    nvl clear

    an "Right! Let's get started, Lily. Help me clean up okay?"
    ln "Okay!"

    stop music fadeout 2.0
    window hide 
    $ renpy.pause(2.0)
    # ... some actions ...
    # Clear the return stack so the next 'return' goes to the main menu
    return
   
