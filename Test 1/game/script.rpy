﻿# The script of the game goes in this file.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show steven_casual_neutral at right

    # These display lines of dialogue.

    steven "Hi! My name is Steven!"

    #show eileen_casual_neutral

    eileen "You've created a new Ren'Py game."

    eileen "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return