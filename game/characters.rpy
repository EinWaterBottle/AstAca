# Declare characters used by this game.

label character:

    #Romanceables

    define edd = Character("Eddy", who_color="#FF2400")
    define fai = Character("Fai", who_color="#ADD8E6")
    define far = Character("Farlaine", who_color="#50C878")
    define mal = Character("Malachai", who_color="#C0C0C0")
    define mat = Character("Mathilde", who_color="#FFC0CB")
    define ina = Character("Ina", who_color="#1B1212")
    define tem = Character("Tempest", who_color="#8F00FF")
    define war = Character("Warden", who_color="#FFD700")
    define htw = Character("Heartwine", who_color="#1B1212")
    define iro = Character("Ironbottom", who_color="#ADD8E6")

    #Non-romanceables

    define nnk = Character("Nanook")
    define mur = Character("Murcerios")
    define cha = Character("Chambers", who_color="#50C878")
    define lux = Character("Estellux", who_color ="#C0C0C0")
    define gro = Character("Grognard", who_color="#FFC0CB")
    define nym = Character("Nym", who_color="#FFD700")
    define sim = Character("Simulera", who_color="#8F00FF")
    define wic = Character("Wickle", who_color="#FF2400")
    define mng = Character("Mingus")

## Character Relationships
###
###

# Romanceables

default edd_like = 0
default fai_like = 0
default far_like = 0
default mal_like = 0
default mat_like = 0
default ina_like = 0
default tem_like = 0
default war_like = 0
default htw_like = 0
default iro_like = 0

# Non-romanceables

default mur_like = 0
default cha_like = 0
default lux_like = 0
default gro_like = 0
default nym_like = 0
default sim_like = 0
default wic_like = 0
default mng_like = 0

###

image daniel_large:
    "images/characters/02_Default_Daniel_larger.png"
    zoom 0.7
    yalign 0
image mingus_large:
    "images/characters/02_Neutral_Mingus_larger.png"
    zoom 0.7
    yalign 0

define dan_large = Character("Daniel Large")
define mingus_crop = Character("Mingus Crop")