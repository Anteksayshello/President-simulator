# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define p = Character("President")
define vc = Character("Vice President")
define n = Character("Narrator")

default education = 65
default national_budget = 1000000000000

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # The ai generation is amazing

    # These display lines of dialogue.
    
    n "You have been elected by the people to be the president of listenbourg"
    n "In the next few years, you will have to make decisions that will affect the country and its people"
    n "These decision will be presented by your vice president and will have real consequences on the country and on how the country will develop"
    
    vc "Hello Mr. President, I am your vice president and I will be presenting you the first decision of your presidency"
    p "Hello Vice President, I am ready to listen to your proposal"
    vc "Would you like to invest in education?"

    menu:
        "Approve":
            $ education += 5
            $ national_budget -= 10000000
            vc "You have decided to invest in education. This will increase the education level of the country but will also decrease the national budget."
        "Decline":
            vc "You have decided not to invest into education, this resulted in you not decreasing the national budget but also not increasing the education level of the country."
    
    vc "Would you like to invest in infrastructure?"
    
    menu:
        "Approve":
            vc "You have invested in infrastructure."
        "Decline":
            vc "You have declined to invest in infrastructure."
    
    # This ends the game 

    return
