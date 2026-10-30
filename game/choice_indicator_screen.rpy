### Choice Indicator Screen ############################################################
##
## Screen that pops up then you make a good choice for that love interest.
## Why use a screen instead of an image?
# - Pauses user interaction
# - one line: i'm lazy



############################################################
### DEFAULTS/DEFINES ###
############################################################

define FELIX_COLOR = "#88e59a"

image f01 = "gui/flowers/f01.webp"
image f02 = "gui/flowers/f02.webp"
image f03 = "gui/flowers/f03.webp"
image f04 = "gui/flowers/f04.webp"
image f05 = "gui/flowers/f05.webp"
image f06 = "gui/flowers/f06.webp"

# Change ts_speed to adjust speed.
# Remeber to also adjust the screen timer.
transform ts_indicator_anim(ts_speed=3.0):
    alpha 0.0
    xoffset 60
    parallel:
        linear ts_speed/3 alpha 1.0
    parallel:
        linear ts_speed xoffset -20 # Change xoffset to adjust speed. 
    parallel:
        pause ts_speed - 1.5
        linear ts_speed/3 alpha 0.0

transform ts_rotate(ts_speed=4.0):
    anchor (0.5, 0.5)
    subpixel True # Enables smooth movements
    rotate 0
    linear ts_speed rotate 360
    repeat

# This is used to recolor the flower
# The default is a transparent color: e.g. Nothing.
transform ts_recolor(color):
    matrixcolor TintMatrix(color)


############################################################
### CHOICE INDICATOR SCREEN ###
############################################################
## Simply show this screen under the correct choice

screen choice_indicator(color="#FFFFFF00"):
    #modal True # disable user interaction when this screen shows; you can comment this out if you don't like it

    zorder 100 # So that it appears on top of textbox.

    frame: # To keep everything together
        background None
        
        xysize (300, 307)
        pos (1400, 880) # CHANGE THIS: if you want to reposition where the flowers appear

        ## Images ##
        add "f01":
            at ts_rot(0), ts_indicator_anim(), ts_recolor(color)
            pos (46, 36)

        add "f02":
            at ts_rot(0), ts_indicator_anim(), ts_recolor(color)
            pos (0, 0)

        add "f03":
            at ts_rot(0), ts_indicator_anim(), ts_recolor(color)
            pos (5, 65)

        #add "f04":
            #at ts_acFloat(30), ts_indicator_anim(), ts_recolor(color)
            #pos (37, 87)

        #add "f05":
            #at ts_acFloat(40), ts_indicator_anim(), ts_recolor(color)
            #pos (52, 14)

        #add "f06":
            #at ts_acFloat(20), ts_indicator_anim(), ts_recolor(color)
            #pos (74, 28)

        # hides screen after 3.0 seconds, re-enabling user interaction
        timer 3.0 action Hide()



############################################################
### LABELS FOR TESTING ###
############################################################



#label choice_testing:
    #"Blah Blah blah"
    #"The current route is [str(route)]."
    #menu choice_test1:
        #"Choose a route."
        #"Felix":
            #$ route='felix'
           # show screen choice_indicator(FELIX_COLOR) 
            #"Felix route."

        #"Albion":
            #$ route = 'albion'
           # show screen choice_indicator() 
            #"Albion route."

        #"End":
            #return
   # "End test."
   #jump choice_test1
