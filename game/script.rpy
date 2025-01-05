# The script of the game goes in this file.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "Astralis Academy."

    "The pinnacle of magical study, the final frontier of arcane study gathered all in one place."

    "And I was going to study there."

    "insert character creator here :)"

    call screen character_creator

    ed "My name is Eddy."

    fa "My name is Fai."

    # This ends the game.

    return
