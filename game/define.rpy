###################################
#CHARACTER DEFINE
###################################
define a = Character("ASTRA", color="#3a0f0c")
define q = Character("QWYNN", color="#e45472")
define al = Character("ALBION", color="#b66fc0") ##d897e0
define f = Character("FELIX", color="#66ab95")
define s = Character("SYLPHIA", color="#3a0f0c")#, callback = name_callback, cb_name = "sylphia", image = 'Sylphia')
define c = Character("CAELAN", color="#4f5394")
define n = Character("NIMUE", color="#3a0f0c")
define v = Character("VELVET", color="#3a0f0c")
define who = Character("???", color="#3a0f0c")
define ven = Character ("VENDOR", color="#3a0f0c")
define Dryad = Character ("DRYAD GIRL", color="#3a0f0c")
define Doggy = Character ("DOG-EARED BOY", color="#3a0f0c")
define Teen = Character ("ELVEN TEEN", color="#3a0f0c")
#albion route
define Girl = Character ("SHORT-HAIRED GIRL", color="#3a0f0c")
define vnd = Character("VENDOR", color="#3a0f0c")
#Felix route
define dwa = Character ("DWARF", color="#3a0f0c")
define elf = Character("ELF", color="#3a0f0c")

###################################
#IMAGE DEFINE
###################################
image Felix = "Felix_N.png"
image Felix_B = "Felix_Blush.png"
image Albion = "Albion_N.png"
image Albion_B = "Albion_Blush.png"
image Sylphia = At("Sylphia_N.png")#, sprite_highlight('Sylphia'))
image Sylphia = At("Sylphia_N.png")#, half_size, sprite_highlight('Sylphia'))
image Qwynn = At("Qwynn_N.png", half_size)
image Velvet = "Velvet_N.png"
image Qwynn = "Qwynn_N.png"
image Qwynn_B = "Qwynn_Blush.png"
image Caelan = "Caelan_N.png"
image Caelan2 = "Caelan_N2.png"
image Caelan_ST = "Caelan_ST.png"
image Caelan_ST2 = "Caelan_ST2.png"
image Caelan_EM = "Caelan_EM.png"
image Caelan_EM2 = "Caelan_EM2.png"
image Caelan_B = "Caelan_B.png"
image Caelan_B2 = "Caelan_B2.png"
image Caelan_C = "Caelan_C.png"
image Caelan_C2 = "Caelan_C2.png"
image Caelan_S = "Caelan_S.png"
image Caelan_S2 = "Caelan_S2.png"
image Caelan_A = "Caelan_A.png"
image Caelan_A2 = "Caelan_A2.png"
image Caelan_B = "Caelan_B.png"
image Caelan_SA2 = "Caelan_SA2.png"
image Caelan_SA = "Caelan_SA.png"
image Caelan_H2 = "Caelan_H2.png"
image Caelan_H = "Caelan_H.png"
image Caelan_F2 = "Caelan_F2.png"
image Caelan_F = "Caelan_F.png"
image Caelan_N12 = "Caelan_N12.png"
image Caelan_N1 = "Caelan_N1.png"
image Nimue = "Nimue_N.png"


###################################
#HALF SIZE TRANSFORM THING
###################################

transform half_size:
    zoom 1.1  # Adjust zoom level as needed    
    xpos 600
    ypos -50

###################################
#ZOOM IN TRANSFORM THING
###################################

transform right:    
    xpos 900

###################################
#ZOOM IN TRANSFORM THING
###################################

transform left:    
    xpos 300

###################################
#ZOOM IN TRANSFORM THING
###################################

transform zoom_in:
    zoom 1.3  # Adjust zoom level as needed
    xpos 500  # Center horizontally
    ypos 50


#gallery lock
$ persistent.felix1 = False
$ persistent.felix2 = False
$ persistent.albion1 = False
$ persistent.albion2 = False
$ persistent.qwynn1 = False
$ persistent.qwynn2 = False
$ persistent.caelan1 = False
$ persistent.caelan2 = False

#qwynn route unlock
$ persistent.qwynn_route_unlocked = False
$ persistent.bracelet = False

#caelan full name unlock
$ persistent.caelanname = False

#meet caelan
$ persistent.saint1 = False