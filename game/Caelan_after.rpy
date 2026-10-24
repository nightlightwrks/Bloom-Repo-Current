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

define aen = Character('AERIS', kind=nvl, color="#3a0f0c")
define cn = Character('CAELAN', kind=nvl, color="#5187e4")
define an = Character('ASTRA', kind=nvl, color="#7e6fd6")
define na = Character(None, kind =nvl)


label caelan_after:

    $ persistent.status_button = False
    
    show caelan_after
    $ renpy.pause(1.0)
    window hide
    pause (5.0)
    window auto

    play music "city_day.ogg" fadeout 2.0 fadein 2.0
    scene market with dissolve

    "How do you define Caelan and Astra's relationship?"

    menu: 

        "Caelan and Astra are a couple.":
            jump caelan_afterstart1
        "Caelan and Astra are friends.": 
            jump caelan_afterstart2

label caelan_afterstart1:

    an "Caelan? What are you so nervous for, we're just having lunch."
    cn "Yes. Lunch. With your mother."
    an "She doesn't bite."
    na "I shoot Astra a pitiful glare."
    na "Anxiety has been clawing at me ever since Astra told me that her mother was planning to visit."
    na "Astra takes after Aeris in a lot of ways."
    na "It was a series of small coincidences that led me to realize they were related. The final nail in the coffin being this very visit, when Astra mentioned her mother's name."
    na"My fingers wear the edge of my sleeve thin."
    an "Caelan. Hey—"
    cn "It is nothing. I am sure your mother is lovely."
    na "Astra looks unconvinced by my reassurance so I add onto it—"

    nvl clear

    cn "Like you."
    an "...Unfair."
    na "She pouts, and I smile."
    na "The weight lifts, just a little. Enough to release my sleeve and take Astra's hand instead."
    cn "We have had many dates in the last few months, I have trained for this."
    an "Are you sure?"
    cn "Positive."
    na "She hums."
    an "Well good, cause we're here."
    na "We come to a stop just outside of the restaurant. Inside, Aeris is waiting."
    na "My heart races and there's an urge to run, simmering just beneath my skin. From the corner of my eye I see Astra reach for the handle."

    nvl clear

    cn "(If Aeris didn't want to see me she could have told Astra to come alone.)"
    an "You know, mom insisted I bring you along. I tried to tell her that you were busy but she wouldn't hear it."
    cn "..."
    na "Astra shakes her head in exasperation and pushes the door open."

    nvl clear

    play music "caelan.ogg" fadeout 2.0 fadein 2.0
    scene vels with dissolve

    na "I follow Astra inside the restaurant on autopilot. My eyes stay trained on the floor in fear of what I'll find if I look up."
    na "Astra walks ahead of me, carving the path to where Aeris sits."
    na "Finally, when her step comes to a halt, I lift my head."
    na "Astra is speaking, probably giving introductions, but all Caelan can focus on is the bright smile on Aeris' face." 
    aen "Caelan. You look well."
    na "Astra makes a confused noise as I take a hesitant step forward." 
    cn "Aeris… I am—"
    na "Aeris stands to meet me, and my heart soars with hope."
    aen "No. Don't finish that sentence. {i}I'm{/i} sorry, Caelan."
    aen "As your friend, I shouldn't have abandoned you like that."
    cn "...You were afraid. I do not blame you for that." 

    nvl clear

    aen "You always do that. Don't minimize your own pain. I left you at a time when you needed a friend the most."
    aen "I regret that now."
    na "They sit with that sentiment for a moment, letting the truth of it sink in."
    cn "Then… I accept your apology."
    na "Next to me Astra seems to come to a realization. Her eyes dart back and forth between Aeris and I until her eyebrows raise in understanding."
    an "Wow, I think that's the first time I've heard you actually accept an apology!"
    na "They can't stop the fond smile that takes over their features."
    cn "A result of your influence."
    aen "She's very convincing. Somehow, she always ends up getting what she wants."
    na "Instead of answering directly, Astra only grins and tangles her hand with mine to pull me into the seat across from Aeris."
    an "So… you two are friends?"

    nvl clear

    aen "Before the sanctuary closed, yes."
    cn "Aeris visited often to share meals. I always looked forward to it."
    na "Aeris chuckles."
    aen "They have a horrible sweet tooth."
    an "So I've discovered."
    cn "Dragons can eat whatever they want."
    an "That might be true, but us humans need a bit of variety. I can't have pastries for dinner every night."
    cn "Just the nights when we eat together?"
    an "...That's basically every night."
    aen "I'm glad to see you so happy, Caelan."
    cn "...I am. Very happy."
    na "Astra squeezes my hand from beneath the table."

    nvl clear

    cn "And you? …Are you happy, Aeris?"
    na "She laughs."
    aen "Estatic. Knowing you're happy, knowing that Astra is happy… I couldn't be more thrilled."

    na "..." 
    
    nvl clear

    play music "city_night.ogg" fadeout 2.0 fadein 2.0
    scene market_evening with dissolve

    na "Outside, Aeris pulls me into a hug so tight and familiar that it brings tears to my eyes."
    aen "I'll come back to visit again soon. And next time I'll bring my husband—the two of you never did get to meet."
    cn "I look forward to it."
    cn "I will grant you an open invitation to the sanctuary. I can tell Nimue and the others to allow you in."
    aen "Oh little Nimue! How is she? Not so little anymore I should think."
    cn "Not quite. She has become my most capable aid, and also a good friend."
    na "Aeris' eyes flick to Astra who's currently pretending to study the wares of a nearby market stall."
    aen "It sounds like you have many friends now. And Astra of course. You two make a cute couple~"
    cn "T-thank you."
    na "Astra's head whips towards her mother."

    nvl clear

    aen "What? Is that a secret? You know you're terrible at keeping secrets, Astra."
    an "It's not a secret—I just, we just didn't tell you…"
    aen "Well either way, I'm happy for you both."
    na "Astra sighs, reaching out to tug her mother into a hug."
    an "Safe travels back home. I'll send you and dad a letter soon."
    aen "I can't wait."
    na "She turns to me."
    aen "I'll send you letters of my own. If you don't mind…"
    cn "Of course. I would love that."
    na "The sincere smile I receive in return clears away any lingering regrets. There is nothing I can do to change the past, {w}but there's always hope for the future."
    na "Seeing Aeris again decades later... getting to meet Astra... it's all the proof I need to believe in that hope."

    nvl clear

    na "Together, Astra and I walk back to her apartment."
    na "Still shaken from the incident, Astra almost never walks anywhere alone. If she does it's only in broad daylight on crowded streets."
    cn "(One day, I will be able to restore Astra's trust in this city.)"
    cn "(Until then, I am happy to be her guardian.)"
    na "I lose myself in the silence so much so that the next time Astra speaks, I almost flinch."
    an "Were you afraid to tell me that you knew my mother?"
    cn "A little… but I only realized the truth recently. Before, I had only suspected it."
    na "Astra nods."
    an "...She used to tell me stories about an old friend of hers. She talked about them with so much warmth, though there was always a sadness in her voice that I could never place."
    an "I never got the courage to ask either."

    nvl clear

    an "Your offering, the one I always make for you... my mother used to make that drink for me whenever I was feeling down."
    an "She said it was a special drink that fills your heart with good memories."
    cn "..."
    na "I stop abruptly."
    an "Caelan?"
    na "In my chest there's a tight squeeze of overwhelming love threatening to send me into cardiac arrest."
    na "At the very least, Astra seems to recognize that it's a good feeling and so she simply guides me to a quiet section of the street."
    na "Her hands come up to wipe away my tears."
    an "Maybe I should have waited to tell you that story."
    cn "I will consider it more training."
    an "I don't think anyone noticed… or if they did they're being really nice about it."

    nvl clear

    na "Her hands fall away from my face and come to rest at my waist."
    an "Okay now?"
    cn "Yes, thank you."
    an "You're very welcome."
    an "Come on, let's keep going. I want to stop at Bloom and get some coffee!"
    cn "You had coffee this morning."
    an "And now I want some more~"
    na "She steps away with a bounce in her steps and a grin on her lips."
    na "Happily, I follow behind her."




    stop music fadeout 2.0
    window hide
    $ renpy.pause(2.0)
    return


label caelan_afterstart2:

    an "Caelan? What are you so nervous for, we're just having lunch."
    cn "Yes. Lunch. With your mother."
    an "She doesn't bite."
    na "I shoot Astra a pitiful glare."
    na "Anxiety has been clawing at me ever since Astra told me that her mother was planning to visit."
    na "Astra takes after Aeris in a lot of ways."
    na "It was a series of small coincidences that led me to realize they were related. The final nail in the coffin being this very visit, when Astra mentioned her mother's name."
    na"My fingers wear the edge of my sleeve thin."
    an "Caelan. Hey—"
    cn "It is nothing. I am sure your mother is lovely."
    na "Astra looks unconvinced by my reassurance so I add onto it—"

    nvl clear

    cn "Like you."
    an "...Unfair."
    na "She pouts, and I smile."
    na "The weight lifts, just a little. Enough to release my sleeve and take a deep breath."
    cn "We have had many outings in the last few months, I have trained for this."
    an "Are you sure?"
    cn "Positive."
    na "She hums."
    an "Well good, cause we're here."
    na "We come to a stop just outside of the restaurant. Inside, Aeris is waiting."
    na "My heart races and there's an urge to run, simmering just beneath my skin. From the corner of my eye I see Astra reach for the handle."

    nvl clear

    cn "(If Aeris didn't want to see me she could have told Astra to come alone.)"
    an "You know, mom insisted I bring you along. I tried to tell her that you were busy but she wouldn't hear it."
    cn "..."
    na "Astra shakes her head in exasperation and pushes the door open."

    nvl clear

    play music "caelan.ogg" fadeout 2.0 fadein 2.0
    scene vels with dissolve

    na "I follow Astra inside the restaurant on autopilot. My eyes stay trained on the floor in fear of what I'll find if I look up."
    na "Astra walks ahead of me, carving the path to where Aeris sits."
    na "Finally, when her step comes to a halt, I lift my head."
    na "Astra is speaking, probably giving introductions, but all Caelan can focus on is the bright smile on Aeris' face." 
    aen "Caelan. You look well."
    na "Astra makes a confused noise as I take a hesitant step forward." 
    cn "Aeris… I am—"
    na "Aeris stands to meet me, and my heart soars with hope."
    aen "No. Don't finish that sentence. {i}I'm{/i} sorry, Caelan."
    aen "As your friend, I shouldn't have abandoned you like that."
    cn "...You were afraid. I do not blame you for that." 

    nvl clear

    aen "You always do that. Don't minimize your own pain. I left you at a time when you needed a friend the most."
    aen "I regret that now."
    na "They sit with that sentiment for a moment, letting the truth of it sink in."
    cn "Then… I accept your apology."
    na "Next to me Astra seems to come to a realization. Her eyes dart back and forth between Aeris and I until her eyebrows raise in understanding."
    an "Wow, I think that's the first time I've heard you actually accept an apology!"
    na "They can't stop the fond smile that takes over their features."
    cn "A result of your influence."
    aen "She's very convincing. Somehow, she always ends up getting what she wants."
    na "Instead of answering directly, Astra taps my shoulder and motions for me to take a seat across from Aeris."
    an "So… you two are friends?"

    nvl clear

    aen "Before the sanctuary closed, yes."
    cn "Aeris visited often to share meals. I always looked forward to it."
    na "Aeris chuckles."
    aen "They have a horrible sweet tooth."
    an "So I've discovered."
    cn "Dragons can eat whatever they want."
    an "That might be true, but us humans need a bit of variety. I can't have pastries for dinner every night."
    cn "Just the nights when we eat together?"
    an "...That's basically every night."
    aen "I'm glad to see you so happy, Caelan."
    cn "...I am. Very happy."
    na "Astra smiles."

    nvl clear

    cn "And you? …Are you happy, Aeris?"
    na "She laughs."
    aen "Estatic. Knowing you're happy, knowing that Astra is happy… I couldn't be more thrilled."

    na "..." 
    
    nvl clear

    play music "city_night.ogg" fadeout 2.0 fadein 2.0
    scene market_evening with dissolve

    na "Outside, Aeris pulls me into a hug so tight and familiar that it brings tears to my eyes."
    aen "I'll come back to visit again soon. And next time I'll bring my husband—the two of you never did get to meet."
    cn "I look forward to it."
    cn "I will grant you an open invitation to the sanctuary. I can tell Nimue and the others to allow you in."
    aen "Oh little Nimue! How is she? Not so little anymore I should think."
    cn "Not quite. She has become my most capable aid, and also a good friend."
    na "Aeris' eyes flick to Astra who's currently pretending to study the wares of a nearby market stall."
    aen "It sounds like you have many friends now."
    cn "I think Astra should get credit for that."
    cn "She includes me in so many things."


    nvl clear

    an "I'm just trying to convince them that being in public isn't that scary."
    an "They end up making friends all on their own." 
    na "I hum instead of pushing back." 
    na "Astra looks me up and down in suspicion before giving up and reaching out to tug her mother into a hug."
    an "Safe travels back home. I'll send you and dad a letter soon."
    aen "I can't wait."
    na "She turns to me."
    aen "I'll send you letters of my own. If you don't mind…"
    cn "Of course. I would love that."
    na "The sincere smile I receive in return clears away any lingering regrets. There is nothing I can do to change the past, {w}but there's always hope for the future."
    na "Seeing Aeris again decades later... getting to meet Astra... it's all the proof I need to believe in that hope."

    nvl clear

    na "Together, Astra and I walk back to her apartment."
    na "Still shaken from the incident, Astra almost never walks anywhere alone. If she does it was only in broad daylight on crowded streets."
    cn "(One day, I will be able to restore Astra's trust in this city.)"
    cn "(Until then, I am happy to be her guardian.)"
    na "I lose myself in the silence so much so that the next time Astra speaks, I almost flinch."
    an "Were you afraid to tell me that you knew my mother?"
    cn "A little… but I only realized the truth recently. Before, I had only suspected it."
    na "Astra nods."
    an "...She used to tell me stories about an old friend of hers. She talked about them with so much warmth, though there was always a sadness in her voice that I could never place."
    an "I never got the courage to ask either."

    nvl clear

    an "Your offering, the one I always make for you... my mother used to make that drink for me whenever I was feeling down."
    an "She said it was a special drink that fills your heart with good memories."
    cn "..."
    na "I stop abruptly."
    an "Caelan?"
    na "In my chest there's a tight squeeze of overwhelming love threatening to send me into cardiac arrest."
    na "At the very least, Astra seems to recognize that it's a good feeling and so she simply guides me to a quiet section of the street."
    na "Her hands come up to wipe away my tears."
    an "Maybe I should have waited to tell you that story."
    cn "I will consider it more training."
    an "I don't think anyone noticed… or if they did they're being really nice about it."

    nvl clear

    na "Her hands fall away from my face."
    an "Okay now?"
    cn "Yes, thank you."
    an "You're very welcome."
    an "Come on, let's keep going. I want to stop at Bloom and get some coffee!"
    cn "You had coffee this morning."
    an "And now I want some more~"
    na "She steps away with a bounce in her steps and a grin on her lips."
    na "Happily, I follow behind her."

    stop music fadeout 2.0
    window hide
    $ renpy.pause(2.0)
    return
    

   
   



