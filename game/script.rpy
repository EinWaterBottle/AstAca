# The script of the game goes in this file.

# The game starts here.

default mouse_xy = (0,0)

init python:
    def get_mouse():
        global mouse_xy
        mouse_xy = renpy.get_mouse_pos()

# dialogue positions
define left2 = Position(xalign=0.1, yalign=0)
define right2 = Position(xalign=0.9, yalign=0)

label start:

    scene astralis_wide

    show screen player_stats

    "Astralis Academy."

    "The pinnacle of magical study, the final frontier of arcane study gathered all in one place."

    "And I was going to study there."

    "insert character creator here :)"

    show daniel_large at left2

    show mingus_large at right2

    call screen character_creator

    "Evaluating chosen traits..."

    ###

    if trait_homeland == 1:

        "You're from Drifthelm."

    if trait_homeland == 2:

        "You're from Ekuze."

    if trait_homeland == 3:

        "You're from Gyllene."

    if trait_homeland == 4:

        "You're from Khun Lodar."

    if trait_homeland == 5:

        "You're from Ostonia."

    if trait_homeland == 6:

        "You're from Reshana."

    if trait_homeland == 7:

        "You're from Truwyn."

    if trait_homeland == 8:

        "You're from Zeskuba."

    ###

    if trait_origin == 1:

        "You're a guildmage."
        $ change_scarlet(-3)
        $ change_cobalt(-3)
        $ change_obsidian(-3)
        $ change_argent(-3)
        $ change_viridian(-3)
        $ change_rose(-3)
        $ change_violet(-3)
        $ change_aurum(-3)

    if trait_homeland == 2:

        "You're a prodigy."

    if trait_homeland == 3:

        "You're rich."
        $ change_scarlet(-3)
        $ change_cobalt(-3)
        $ change_obsidian(-3)
        $ change_argent(-3)
        $ change_viridian(-3)
        $ change_rose(-3)
        $ change_violet(-3)
        $ change_aurum(-3)
        $ merits += 100
        $ goodwill += 15

    if trait_homeland == 4:

        "You're poor."
        $ change_scarlet(-3)
        $ change_cobalt(-3)
        $ change_obsidian(-3)
        $ change_argent(-3)
        $ change_viridian(-3)
        $ change_rose(-3)
        $ change_violet(-3)
        $ change_aurum(-3)
        $ merits -= 50
    
    ###

    if trait_talent == 1:

        "You're an alchemist."
        $ change_aurum(+5)

    if trait_talent == 2:

        "You're pretty."
        $ change_rose(+5)

    if trait_talent == 3:

        "You see dead people."
        $ change_obsidian(+5)

    if trait_talent == 4:

        "Your head is in the clouds."
        $ change_viridian(+5)

    if trait_talent == 5:

        "You've got an iron liver."
        $ change_cobalt(+5)

    if trait_talent == 6:

        "You're the peak of athleticism."
        $ change_scarlet(+5)

    if trait_talent == 7:

        "You're stinky."
        $ change_violet(+5)

    if trait_talent == 8:

        "You're a mystic."
        $ change_argent(+5)

    ###

    "Evaluated! Check your stats!"

    edd "My name is Eddy."

    fai "My name is Fai."

    # This ends the game.

    return
