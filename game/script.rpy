# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define p = Character("President")
define vc = Character("Vice President")
define n = Character("Narrator")

default education = 60
default GDP = 1000000000000
default welfare = 60
default inhabitants = 40000000
default corruption = 5
default Education = 60
default Popularity = 60
default ideology = 60
default power = 60
default taxes = 20000000000

default days = 0




screen stats():

    tag menu

    frame:
        xalign 1.0
        yalign 0.05
        padding (20, 20)

        vbox:
            spacing 10

            text "Stats" size 30

            text "Education: [education]" size 20
            text "National Budget: [national_budget]" size 20

            textbutton "Close" action Return() xalign 1.0


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
    call screen stats
    n "In the next few years, you will have to make decisions that will affect the country and its people"
    n "These decision will be presented by your vice president and will have real consequences on the country and on how the country will develop"
    
    vc "Hello Mr. President, I am your vice president and I will be presenting you the first decision of your presidency"
    p "Hello Vice President, I am ready to listen to your proposal"
    vc "Would you like to invest in education?"

    menu:
        "Approve":
            $ education += 5
            $ GDP -= 10000000000
            vc "You have decided to invest in education. This will increase the education level of the country but will also decrease the national budget."
        "Decline":
            vc "You have declined to invest in education."
    
    vc "Would you like to invest in infrastructure?"
    
    menu:
        "Approve":
            vc "You have invested in infrastructure."
            $ GDP -= 25000000000
            $ welfare += 5
        "Decline":
            vc "You have declined to invest in infrastructure."
    
    vc "would you like to promote equal rights?"

    menu: 
        "Approve":
            vc "You have decided to promote equal rights, this will increase the welfare of the country but will also decrease the national budget."
            $ popularity += 10
            $ GDP -= 15000000000
        "Decline":
            vc "You have declined to promote equal rights."
            
    vc "Would you like to invest in better housing?"

label ass:
    vc "Would you like to Assinate people that fight for equal rights?"
    menu:
        "Approve":
            vc "You have decided to assinate people that fight for equal rights, this will decrease the popularity of the government.
            $ popularity -= 10
        jump fas
        "Decline":
            vc "You have declined to assinate people that fight for equal rights."
    

    menu:
        "Approve":
            vc "You have decided to invest in better housing, this will increase the welfare of the country but will also decrease the national budget."
            $ welfare += 15
            $ GDP -= 50000000000
        "Decline":
            vc "You have declined to invest in better housing."'
            $ popularity -= 2

    vc "Would you like to make the buisness state-owned?"

    menu:
        "Approve":
            vc "You have decided to make the buisness state-owned, this will increase the GDP of the country but will also decrease the popularity of the government."
            $ GDP += 75000000000
            $ popularity -= 10
            $ welfare += 3
            jump com
        "Decline":
            vc "You have declined to make the buisness state-owned."
            $ popularity += 2
    vc "Would you like to increase taxes on the rich?"

label com:
    vc "communism"

label fas:
    vc "uh"
    # This ends the game 

    return
