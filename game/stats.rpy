## all the stats for the game

default scarlet = 10
default cobalt = 10
default obsidian = 10
default argent = 10
default viridian = 10
default rose = 10
default violet = 10
default aurum = 10

## Stat Groups
# a combination of two magic stats to describe a less-specific skill and general approach for the player

default force = 20
default judgement = 20
default mystique = 20
default artistry = 20

## Goodwill
# describes reputation among teacher body
# currency for skipping classes and general favors from teachers
# 0 = expelled; 100 = really not expelled

default goodwill = 50

## Merits
# currency system

default merits = 10

## House
# defines which house player is in
# house_color will change some ui elements based on the house the player chooses

default house = "Unknown"
default house_color = "#fff"

##
## Traits
##

## Homeland
## 0 = none, 1 = drifthelm, 2 = ekuze, 3 = gyllene, 4 = khun, 5 = ostonia, 6 = reshana, 7 = truwyn, 8 = zeskuba

default trait_homeland = 0

## Origin
## 0 = none, 1 = guildmage, 2 = prodigy, 3 = old money, 4 = underdog

default trait_origin = 0

## Talent
## 0 = none, 1 = alchemaster, 2 = charming, 3 = fairyland, 4 = ironcon, 5 = haunted, 6 = olympian, 7 = rogue, 8 = truthsayer

default trait_talent = 0

##
## Text Shortcuts
##

## Stats
## [obsidian_text] will type it out Bold and in a black color.

default scarlet_text = "{color=#BA0909}{b}Scarlet{/b}{/color}"
default cobalt_text = "{color=#56A3E4}{b}Cobalt{/b}{/color}"
default obsidian_text = "{color=#333333}{b}Obsidian{/b}{/color}"
default argent_text = "{color=#BBBBBB}{b}Argent{/b}{/color}"
default viridian_text = "{color=#2CAA00}{b}Viridian{/b}{/color}"
default rose_text = "{color=#FFA5DF}{b}Rose{/b}{/color}"
default violet_text = "{color=#5738C2}{b}Violet{/b}{/color}"
default aurum_text = "{color=#FFCB65}{b}Aurum{/b}{/color}"

## Pronouns
##

default pronouns = "they/their"

init python:
    class pronoun():
        def __init__(self, neutral, masculine, feminine):
            self.neutral = neutral
            self.masculine = masculine
            self.feminine = feminine
        def __str__(self):
            global pronouns
            if pronouns == "she/her":
                return self.feminine
            elif pronouns == "he/him":
                return self.masculine
            elif pronouns == "they/them":
                return self.neutral
            else:
                return self.neutral

define they = pronoun("they", "he", "she")
define them = pronoun("them", "him", "her")
define their = pronoun("their", "his", "her")
define attractive = pronoun("attractive", "handsome", "beautiful")
define be = pronoun("are", "is", "is")

define They = pronoun("They", "He", "She")
define Them = pronoun("Them", "Him", "Her")
define Their = pronoun("Their", "His", "Her")

#############################################################################
### FUNCTIONS ###############################################################
#############################################################################

init python:

    def change_scarlet(num):
        global scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum, force, judgement, mystique, artistry
        scarlet += num
        force += num
        new_stat_values = (scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum)
        stat_chart.values = new_stat_values
        return

    def change_cobalt(num):
        global scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum, force, judgement, mystique, artistry
        cobalt += num
        force += num
        new_stat_values = (scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum)
        stat_chart.values = new_stat_values
        return

    def change_obsidian(num):
        global scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum, force, judgement, mystique, artistry
        obsidian += num
        judgement += num
        new_stat_values = (scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum)
        stat_chart.values = new_stat_values
        return

    def change_argent(num):
        global scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum, force, judgement, mystique, artistry
        argent += num
        judgement += num
        new_stat_values = (scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum)
        stat_chart.values = new_stat_values
        return

    def change_viridian(num):
        global scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum, force, judgement, mystique, artistry
        viridian += num
        mystique += num
        new_stat_values = (scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum)
        stat_chart.values = new_stat_values
        return

    def change_rose(num):
        global scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum, force, judgement, mystique, artistry
        rose += num
        mystique += num
        new_stat_values = (scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum)
        stat_chart.values = new_stat_values
        return

    def change_violet(num):
        global scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum, force, judgement, mystique, artistry
        violet += num
        artistry += num
        new_stat_values = (scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum)
        stat_chart.values = new_stat_values
        return

    def change_aurum(num):
        global scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum, force, judgement, mystique, artistry
        aurum += num
        artistry += num
        new_stat_values = (scarlet, cobalt, obsidian, argent, viridian, rose, violet, aurum)
        stat_chart.values = new_stat_values
        return

############################################################################
## SCREENS #################################################################
############################################################################

## Character Creator Screen

init:
    style my_input:
        is default
        color "#000"
        hover_color "#3399ff"
        size 28
        
    style input_button:
        is button
        yalign 1.0
        key_events True
        xysize (250, 25)
        
    python:
        class MyInputValue(InputValue):
            def __init__(self, var, default=""):
                self.var = var
                
                if not hasattr(store, var):
                    setattr(store, var, default)
                    
            def get_text(self):
                return getattr(store, self.var)
                
            def set_text(self, s):
                setattr(store, self.var, s)
                
            def enter(self):
                renpy.run(self.Disable())
                raise renpy.IgnoreEvent()


default firstname = "Jane"
default lastname = "Doe"

screen character_creator():
    #DONE BOX
    frame:
        xalign 0.95
        yalign 0.95
        xpadding 10
        ypadding 10

        vbox:
            textbutton "Done":
                action Return()
    
    #NAME BOX
    frame:
        xalign .1
        yalign 0.02
        xpadding 30
        ypadding 30

        vbox:
            spacing 5
            
            hbox:
                text "Name:"

                $ input = Input(value=MyInputValue("firstname", "Name"), style="my_input", length=10, size=25)
                button:
                    yalign 0
                    style "input_button"
                    action input.enable
                    add input
        
            hbox:
                text "Surname:"

                $ input = Input(value=MyInputValue("lastname", "Surname"), style="my_input", length=10, size=25)
                button:
                    yalign 0
                    style "input_button"
                    action input.enable
                    add input
    
    #PRONOUNS BOX
    frame:
        xalign .5
        yalign 0.02
        xpadding 30
        ypadding 30

        hbox:
            textbutton "He/Him":
                action SetVariable("pronouns", "he/him")
            textbutton "They/Them":
                action SetVariable("pronouns", "they/them")
            textbutton "She/Her":
                action SetVariable("pronouns", "she/her")

    #MAGIC FRAME
    frame:
        xalign .8
        yalign .95
        xpadding 30
        ypadding 30

        add "images/ui/astralis_logo.png" zoom 0.6

    #BIG BOX
    frame:
        xalign .05
        yalign .9
        xpadding 30
        ypadding 30

        vbox:
            spacing 5

            text "Homeland"

            hbox:

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_drifthelm.png"
                    hover "gui/button/cc_drifthelm_hover.png"
                    selected_idle "gui/button/cc_drifthelm_hover.png"
                    action SetVariable("trait_homeland", 1)

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_ekuze.png"
                    hover "gui/button/cc_ekuze_hover.png"
                    selected_idle "gui/button/cc_ekuze_hover.png"
                    action SetVariable("trait_homeland", 2)

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_gyllene.png"
                    hover "gui/button/cc_gyllene_hover.png"
                    selected_idle "gui/button/cc_gyllene_hover.png"
                    action SetVariable("trait_homeland", 3)

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_khunlodar.png"
                    hover "gui/button/cc_khunlodar_hover.png"
                    selected_idle "gui/button/cc_khunlodar_hover.png"
                    action SetVariable("trait_homeland", 4)

            hbox:
                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_ostonia.png"
                    hover "gui/button/cc_ostonia_hover.png"
                    selected_idle "gui/button/cc_ostonia_hover.png"
                    action SetVariable("trait_homeland", 5)

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_reshana.png"
                    hover "gui/button/cc_reshana_hover.png"
                    selected_idle "gui/button/cc_reshana_hover.png"
                    action SetVariable("trait_homeland", 6)

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_truwyn.png"
                    hover "gui/button/cc_truwyn_hover.png"
                    selected_idle "gui/button/cc_truwyn_hover.png"
                    action SetVariable("trait_homeland", 7)

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_zeskuba.png"
                    hover "gui/button/cc_zeskuba_hover.png"
                    selected_idle "gui/button/cc_zeskuba_hover.png"
                    action SetVariable("trait_homeland", 8)

            text "Origin"

            hbox:
                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_guildmage.png"
                    hover "gui/button/cc_guildmage_hover.png"
                    selected_idle "gui/button/cc_guildmage_hover.png"
                    action SetVariable("trait_origin", 1)

                    tooltip ("Like many of your other peers, you got into Astralis with years of study and hard work.", "+Stats", "")

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_prodigy.png"
                    hover "gui/button/cc_prodigy_hover.png"
                    selected_idle "gui/button/cc_prodigy_hover.png"
                    action SetVariable("trait_origin", 2)

                    tooltip ("Your talent for a particular school of magic caught the eye of an Astralis professor.", "++Specific Stat", "++Professor Relationship")

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_oldmoney.png"
                    hover "gui/button/cc_oldmoney_hover.png"
                    selected_idle "gui/button/cc_oldmoney_hover.png"
                    action SetVariable("trait_origin", 3)

                    tooltip ("Perhaps a little spoiled, your family arranged your admission into Astralis Academy.", "++Merits -Stats", "+Goodwill")

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_underdog.png"
                    hover "gui/button/cc_underdog_hover.png"
                    selected_idle "gui/button/cc_underdog_hover.png"
                    action SetVariable("trait_origin", 4)

                    tooltip ("With no money for schooling, you were just barely admitted with your lack of skills.", "--Merits -Stats", "+Relationship Multiplier")

            text "Talent"

            hbox:
                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_alchemaster.png"
                    hover "gui/button/cc_alchemaster_hover.png"
                    selected_idle "gui/button/cc_alchemaster_hover.png"
                    
                    action SetVariable("trait_talent", 1)

                    tooltip ("Innate knack or long-practiced hobby, you have an expertise with alchemy.", "+[aurum_text]", "")

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_charming.png"
                    hover "gui/button/cc_charming_hover.png"
                    selected_idle "gui/button/cc_charming_hover.png"
                    
                    action SetVariable("trait_talent", 2)

                    tooltip ("Whether it's your looks or demeanor, something about you is enchanting.", "+[rose_text]", "")

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_haunted.png"
                    hover "gui/button/cc_haunted_hover.png"
                    selected_idle "gui/button/cc_haunted_hover.png"
                    
                    action SetVariable("trait_talent", 3)

                    tooltip ("You've seen spirits all your life and can communicate with them.", "+[obsidian_text]", "")

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_fairyland.png"
                    hover "gui/button/cc_fairyland_hover.png"
                    selected_idle "gui/button/cc_fairyland_hover.png"
                    
                    action SetVariable("trait_talent", 4)

                    tooltip ("You're touched by another realm and extraplanar creatures tend to like you.", "+[viridian_text]", "")
            
            hbox:
                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_ironcon.png"
                    hover "gui/button/cc_ironcon_hover.png"
                    selected_idle "gui/button/cc_ironcon_hover.png"
                    
                    action SetVariable("trait_talent", 5)

                    tooltip ("Sticks and stones won't break you, and neither will words. You're tough in flesh and spirit.", "+[cobalt_text]", "")

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_olympian.png"
                    hover "gui/button/cc_olympian_hover.png"
                    selected_idle "gui/button/cc_olympian_hover.png"
                    
                    action SetVariable("trait_talent", 6)

                    tooltip ("Your passion comes through in your physicality. Few are your athletic equals.", "+[scarlet_text]", "")

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_rogue.png"
                    hover "gui/button/cc_rogue_hover.png"
                    selected_idle "gui/button/cc_rogue_hover.png"
                    
                    action SetVariable("trait_talent", 7)

                    tooltip ("Sometimes a lockpick and deft fingers make more difference than a well-practiced spell.", "+[violet_text]", "")

                imagebutton:
                    xalign 1.0
                    yalign 0.0
                    idle "gui/button/cc_truthsayer.png"
                    hover "gui/button/cc_truthsayer_hover.png"
                    selected_idle "gui/button/cc_truthsayer_hover.png"
                    
                    action SetVariable("trait_talent", 8)

                    tooltip ("Some say you have an old soul, wise of judgement and quick to insight.", "+[argent_text]", "")

    $ tooltip = GetTooltip()

    if tooltip:
        timer 0.02 repeat True action Function(get_mouse)
        $ mx = mouse_xy[0] - 30 # LR
        $ my = mouse_xy[1] + 30 # UD
        frame:
            pos(mx,my)
            vbox:
                spacing 5
                text tooltip[0]:
                    color "#1B1212"
                    size 25
                text tooltip[1]:
                    size 25
                text tooltip[2]:
                    size 25

###
## Player Stats UI 
###

screen player_menu_button():
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "gui/placeholder_stats.png"
        hover "gui/placeholder_stats_hover.png"
        action [ShowMenu(astralis_handbook.list_screen, astralis_handbook)]
    
    # textbutton "Open Handbook":
        # action ShowMenu(astralis_handbook.list_screen, astralis_handbook)