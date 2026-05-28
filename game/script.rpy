# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define p = Character("President")
define vc = Character("Vice President")
define n = Character("Narrator")

default education = 60
default national_budget = 1000000000000
default welfare = 60
default inhabitants = 40000000
default corruption = 5
default Education = 60
default Popularity = 60
default ideology = 60
default power = 60
default taxes = 20000000000

default leader = 0

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
            $ national_budget -= 10000000000
            vc "You have decided to invest in education. This will increase the education level of the country but will also decrease the national budget."
        "Decline":
            vc "You have declined to invest in education."
    
    vc "Would you like to invest in infrastructure?"
    
    menu:
        "Approve":
            vc "You have invested in infrastructure."
            $ national_budget -= 25000000000
            $ welfare += 5
        "Decline":
            vc "You have declined to invest in infrastructure."
    
    vc "would you like to promote equal rights?"

    menu: 
        "Approve":
            vc "You have decided to promote equal rights, this will increase the welfare of the country but will also decrease the national budget."
            $ popularity += 10
            $ national_budget -= 15000000000
            jump cap
        "Decline":
            vc "You have declined to promote equal rights."
            jump ass
    

label ass:
    vc "Would you like to Assinate people that fight for equal rights?"
    menu:
        "Approve":
            vc "You have decided to assinate people that fight for equal rights, this will decrease the popularity of the government."
            $ popularity -= 10
        jump fas
        "Decline":
            vc "You have declined to assinate people that fight for equal rights."
            jump cap
label cap:  
    vc "Would you like to invest in better housing?"
    menu:
        "Approve":
            vc "You have decided to invest in better housing, this will increase the welfare of the country but will also decrease the national budget."
            $ welfare += 15
            $ national_budget -= 50000000000
        "Decline":
            vc "You have declined to invest in better housing."'
            $ popularity -= 2

    vc "Would you like to make the buisness state-owned?"

    menu:
        "Approve":
            vc "You have decided to make the buisness state-owned, this will increase the national budget of the country but will also decrease the popularity of the government."
            $ national_budget += 75000000000
            $ popularity -= 10
            $ welfare += 3
            jump com
        "Decline":
            vc "You have declined to make the buisness state-owned."
            $ popularity += 2
   
    vc "Would you like to increase taxes on the rich?"
    menu:
        "Approve":
            vc "You have decided to increase taxes on the rich, this will increase the national budget but will also decrease the popularity of the government."
            $ taxes += 5000000000
            $ national_budget += 25000000000
            $ popularity -= 5
            vc "Use the money to improve homeless shelters and public transportation."
            menu:
                "Approve":
                    vc "You have decided to use the money to improve homeless shelters and public transportation, this will increase the welfare of the country but will also decrease the national budget."
                    $ welfare += 5
                    $ national_budget -= 10000000000
                "Decline":
                    vc "You have declined to use the money to improve homeless shelters and public transportation."
                    $ popularity -= 2
        "Decline":
            vc "You have declined to increase taxes on the rich."
            $ popularity += 2
    vc "reduce the taxes on the poor?"
    menu:
        "Approve":
            vc "You have decided to reduce taxes on the poor, this will increase the popularity of the government but will also decrease the national budget."
            $ taxes -= 5000000000
            $ national_budget -= 25000000000
            $ popularity += 5
        "Decline":
            vc "You have declined to reduce taxes on the poor."
            $ popularity -= 2
            vc "ingnore the angry citizens and continue with your presidency"
            menu:
                "Approve":
                    vc "You have decided to ingnore the angry citizens and continue with your presidency, this will decrease the popularity of the government."
                    $ popularity -= 5
                    vc "the citizens start a revolution choose the banner you will stand under"
                    menu:
                        "Unite under a monarchy":
                            vc "You have decided to unite under a monarchy, this will increase the popularity of the government "
                            $ popularity += 10
                            $ national_budget -= 50000000000
                            jump mon
                           
                        "Unite under one nationality":
                            vc "You have decided to stand under the banner of fascism, this will increase the popularity of the government but will also decrease the national budget."
                            $ popularity += 10
                            $ national_budget -= 50000000000
                            jump fas

                "Decline":
                    vc "You listened to the angry citizens and apologized for not reducing taxes on the poor, this has increase the popularity of the government."
                    $ popularity += 2

label com:
    vc "Would you like to promote equality?"

    menu:
        "Approve":
            vc "You have decided to promote equality, this will increase the welfare of the country but will also decrease the national budget."
            $ education += 15
            $ national_budget -= 20000000000
            jump soc
        "Decline":
            vc "You have declined to promote equality."
    
    "Would you like to withold leader elecations?"
    menu:
        "Approve":
            vc "You have decided to withold leader elecations, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 20
            jump com2
        "Decline":
            vc "You have declined to withold leader elecations."
    
    "Would you like to give power to the people?"
    menu:
        "Approve":
            vc "You have decided to give power to the people, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 20
            $ power = 0
            jump arch
        "Decline":
            vc "You have declined to give power to the people."
            jump com2

label com2:
    vc "Would you like to give power to the workers?"
    menu:
        "Approve":
            vc "You have decided to give power to the workers, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 20
         "Approve":
            vc "You have decided to give power to the workers, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 20
    
    vc "Would you like to make the media state-owned?"
    menu:
        "Approve":
            vc "You have decided to make the media state-owned, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 10
            $ power -= 10
            $ national_budget -= 3000000000

        "Decline":
            vc "You have declined to make the media state-owned."
    
    vc "Would you like to promote a one leader mentality?"
    menu:
        "Approve":
            vc "You have decided to promote a one leader mentality, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 20
            $ leader = 1
            $ national_budget -= 500000000
        "Decline":
            vc "You have declined to promote a one leader mentality."
    
    vc "Would you like to introduce a secret police?"
    menu:
        "Approve":
            vc "You have decided to introduce a secret police, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 20
            $ national_budget -= 1500000000
            
            vc "would you like remove political opponents?"
            menu:
                "Approve":
                    vc "You have decided to remove political opponents, this will increase the power of the government but will also decrease the popularity of the government."
                    $ power += 10
                "Decline":
                    vc "You have declined to remove political opponents."
        "Decline":
            vc "You have declined to introduce a secret police."

    vc "Would you like to unite the country under one face?"

label arch:
    vc "You are now an Anarchist, you have given all the power to the people and you have no more power, you can only watch as the country develops without you, good luck."

    na "Get rid of the political parties."
    menu:
        "Approve":
            na "You got rid of politcical parties."
        "Approve":
            na "You got rid of politcical parties."
    
    na "Strip the royal family of their power."
    menu:
        "Approve":
            na "You strip the royal family of their power."
         "Approve":
            na "You strip the royal family of their power."
    na "Discontinue the state military."
    menu:
        "Approve":
            na "You discontinue the state military."
        "Approve":
            na "You discontinue the state military."

    na "Remove the state owned emergency responders."
    menu:
        "Approve":
            na "You remove the state owned emergency responders."
        "Approve":
            na "You remove the state owned emergency responders."
    
    na "Disband any and all goverment bodies."
    menu:
        "Approve":
            na "You disband any and all goverment bodies."
        "Approve":
            na "You disband any and all goverment bodies."

    Na "You achieved total Anarchy, the people are now in control of the country and you have no more power, good luck."

    na "A couple days later, while you are walking home, you get hit by a car and die."

    na "The end."
    jump end

label soc:
    vc "More people started working."
    $ national_budget += 50000000000

label mon:
    vc "monarchy"

label fas:
    vc "fascism"
    vc "uh"

label end:
    na "Would you like to play again?"
    menu:
        "Yes":
            jump start
        "No":
            return
        "Look at statscreen":
            call screen stats
            jump end
            
    # This ends the game 


    return
