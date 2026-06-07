﻿ # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define p = Character("President")
define vc = Character("Vice President")
define n = Character("Narrator")

default education = 60
default national_budget = 1000
default welfare = 60
default inhabitants = 40000000
default corruption = 5
default popularity = 60
default ideology = "Democracy"
default power = 60
default taxes = 20

default leader = 0
default militia = 0
default military = 0
default royal_army = 0
default royal_navy = 0
default Alliance_germany = 0
default Alliance_steel = 0
default austria_invasion = 0

default days = 0
default playthroughs = 0

default ach_first_decision = False
default ach_assassin = False
default ach_state_owned_business = False
default ach_rich_taxation = False
default ach_secret_police = False
default ach_united_iberia = False
default ach_democratic_return = False
default ach_anarchist_vision = False
default ach_monarchy_emperor = False
default ach_victory_spain = False
default ach_people_reformer = False
default ach_welfare_state = False
default ach_militarist = False
default ach_diplomatic_victory = False
default ach_merciful_king = False
default ach_completionist = False
default ach_secret_five_runs = False
default ach_secret_every_death = False
default ach_secret_caretaker = False
default ach_caretaker_education = False
default ach_caretaker_housing = False
default ach_caretaker_shelters = False
default ach_caretaker_healthcare = False
default ach_caretaker_social_security = False
default ach_caretaker_nutrition = False
default ach_secret_death_assassination = False
default ach_secret_death_accident = False
default ach_secret_death_natural = False

default ach_open_bakery = False


init python:
    achievement_defs = {
        "first_decision": "First Decision",
        "assassin": "Assassin",
        "state_owned_business": "State-Owned Business",
        "rich_taxation": "Rich Taxation",
        "secret_police": "Secret Police",
        "united_iberia": "Iberian Unifier",
        "democratic_return": "Democratic Return",
        "anarchist_vision": "Anarchist Vision",
        "monarchy_emperor": "Monarchy Emperor",
        "victory_spain": "Victory in Spain",
        "people_reformer": "People's Reformer",
        "welfare_state": "Welfare State",
        "militarist": "Militarist",
        "diplomatic_victory": "Diplomatic Victory",
        "merciful_king": "Merciful King",
        "completionist": "Presidential Legacy",
        "secret_five_runs": "Seasoned President",
        "secret_every_death": "Grim Archivist",
        "secret_caretaker": "Caring Steward",
        "open_bakery": "Bakery Owner",
    }

    def award_achievement(name):
        variable = "ach_" + name
        if not getattr(renpy.store, variable, False):
            setattr(renpy.store, variable, True)
            renpy.notify("Achievement unlocked: " + achievement_defs.get(name, name))

            if name != "completionist":
                completion_achievements = [
                    "first_decision",
                    "assassin",
                    "state_owned_business",
                    "rich_taxation",
                    "secret_police",
                    "united_iberia",
                    "democratic_return",
                    "anarchist_vision",
                    "monarchy_emperor",
                    "victory_spain",
                    "people_reformer",
                    "welfare_state",
                    "militarist",
                    "diplomatic_victory",
                    "merciful_king",
                    "secret_five_runs",
                    "secret_every_death",
                    "secret_caretaker",
                ]
                if all(getattr(renpy.store, "ach_" + a, False) for a in completion_achievements):
                    award_achievement("completionist")

    def maybe_award_caretaker():
        if not getattr(renpy.store, "ach_secret_caretaker", False):
            keys = [
                "ach_caretaker_education",
                "ach_caretaker_housing",
                "ach_caretaker_shelters",
                "ach_caretaker_healthcare",
                "ach_caretaker_social_security",
                "ach_caretaker_nutrition",
            ]
            if all(getattr(renpy.store, key, False) for key in keys):
                award_achievement("secret_caretaker")

    def maybe_award_secret_death():
        if not getattr(renpy.store, "ach_secret_every_death", False):
            if (
                getattr(renpy.store, "ach_secret_death_assassination", False)
                and getattr(renpy.store, "ach_secret_death_accident", False)
                and getattr(renpy.store, "ach_secret_death_natural", False)
            ):
                award_achievement("secret_every_death")

init -2 python:
    # Fallback defaults for variables that may be missing from older saves or broken state.
    # The normal Ren'Py defaults are declared above with the `default` statements.
    defaults = {
        "education": 60,
        "national_budget": 1000,
        "welfare": 60,
        "inhabitants": 40000000,
        "corruption": 5,
        "popularity": 60,
        "ideology": "Democracy",
        "power": 60,
        "taxes": 20,
        "leader": 0,
        "militia": 0,
        "military": 0,
        "days": 0,
        "playthroughs": 0,
        "royal_army": 0,
        "royal_navy": 0,
        "Alliance_germany": 0,
        "Alliance_steel": 0,
        "austria_invasion": 0,
        "ach_first_decision": False,
        "ach_assassin": False,
        "ach_state_owned_business": False,
        "ach_rich_taxation": False,
        "ach_secret_police": False,
        "ach_united_iberia": False,
        "ach_democratic_return": False,
        "ach_anarchist_vision": False,
        "ach_monarchy_emperor": False,
        "ach_victory_spain": False,
        "ach_people_reformer": False,
        "ach_welfare_state": False,
        "ach_militarist": False,
        "ach_diplomatic_victory": False,
        "ach_merciful_king": False,
        "ach_completionist": False,
        "ach_open_bakery": False,
        "achievement_defs": renpy.store.achievement_defs if hasattr(renpy.store, "achievement_defs") else {
            "first_decision": "First Decision",
            "assassin": "Assassin",
            "state_owned_business": "State-Owned Business",
            "rich_taxation": "Rich Taxation",
            "secret_police": "Secret Police",
            "united_iberia": "Iberian Unifier",
            "democratic_return": "Democratic Return",
            "anarchist_vision": "Anarchist Vision",
            "monarchy_emperor": "Monarchy Emperor",
            "victory_spain": "Victory in Spain",
            "people_reformer": "People's Reformer",
            "welfare_state": "Welfare State",
            "militarist": "Militarist",
            "diplomatic_victory": "Diplomatic Victory",
            "merciful_king": "Merciful King",
            "completionist": "Presidential Legacy",
            "secret_five_runs": "Seasoned President",
            "secret_every_death": "Grim Archivist",
            "secret_caretaker": "Caring Steward",
            "open_bakery": "Bakery Owner",
        },
    }

    for name, value in defaults.items():
        if not hasattr(renpy.store, name):
            setattr(renpy.store, name, value)

screen stats():

    tag menu

    frame:
        xalign 1.0
        yalign 0.05
        padding (20, 20)

        vbox:
            spacing 10

            text "Stats" size 30

            text "Education: [store.education]" size 20
            text "[store.national_budget >= 1000 and 'National Budget: ' + '{:.1f}'.format(store.national_budget/1000) + ' trillion' or 'National Budget: ' + '{:.1f}'.format(store.national_budget) + ' billion']" size 20
            text "Welfare: [store.welfare]" size 20
            text "Inhabitants: [store.inhabitants]" size 20
            text "Corruption: [store.corruption]" size 20
            text "Popularity: [store.popularity]" size 20
            text "Ideology: [store.ideology]" size 20
            text "Power: [store.power]" size 20
            text "Taxes: [store.taxes] billion" size 20
            text "Playthroughs: [store.playthroughs]" size 20
            textbutton "Achievements" action ShowMenu("achievements") xalign 0.0
            textbutton "Close stats" action Return() xalign 1.0

screen achievements():

    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        xsize 800
        ysize 500

        vbox:
            spacing 10

            text "Achievements" size 30

            for name, label in achievement_defs.items():
                if name.startswith("secret_") and not getattr(store, "ach_" + name, False):
                    text "Secret Achievement - Locked" size 18 color "#888"
                else:
                    if getattr(store, "ach_" + name, False):
                        if name.startswith("secret_"):
                            text "[label] - Unlocked" size 18 color "#800080"
                        else:
                            text "[label] - Unlocked" size 18 color (getattr(store, "ach_completionist", False) and "#ffd700" or "#fff")
                    else:
                        text "[label] - Locked" size 18 color (getattr(store, "ach_completionist", False) and "#ffd700" or "#888")

            textbutton "Close" action Return() xalign 0.5


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

    play music "audio/Hearts of Iron IV - Axis Theme.mp3"
    queue music "audio/Hearts of Iron IV - Bring Forth the Tanks.mp3"
    queue music "audio/Hearts of Iron IV - Comintern Theme.mp3"
    queue music "audio/Hearts of Iron IV - End of the Tour.mp3"
    queue music "audio/Hearts of Iron IV - Hearts of Men.mp3"
    queue music "audio/Hearts of Iron IV - Heavy Water 4.mp3"
    queue music "audio/Hearts of Iron IV - Krakow.mp3"
queue music "audio/Hearts of Iron IV - Luftwaffe Strikers Again.mp3"
queue music "audio/Hearts of Iron IV - Main Theme.mp3"
queue music "audio/Hearts of Iron IV - Morning of D-day.mp3"
queue music "audio/Hearts of Iron IV - Mother Russia.mp3"
queue music "audio/Hearts of Iron IV - Operation Barbarossa 4.mp3"
queue music "audio/Hearts of Iron IV - Song For the Children of WW2.mp3"
queue music "audio/Hearts of Iron IV - Soviet Victory.mp3"
queue music "audio/Hearts of Iron IV - The Great Patriotic War 4.mp3"
queue music "audio/Hearts of Iron IV - The Might of Soviet Union.mp3"
queue music "audio/Hearts of Iron IV - The Red Army 4.mp3"
queue music "audio/Hearts of Iron IV - The Royal Airforce.mp3"
queue music "audio/Hearts of Iron IV - The War Ends.mp3"
queue music "audio/Hearts of Iron IV - The Attack.mp3"

    n "You have been elected by the people to be the president of listenbourg"
    call screen stats
    n "In the next few years, you will have to make decisions that will affect the country and its people"
    n "These decision will be presented by your vice president and will have real consequences on the country and on how the country will develop"
    
    show vccap
    vc "Hello Mr. President, I am your vice president and I will be presenting you the first decision of your presidency"
    p "Hello Vice President, I am ready to listen to your proposal"

    $ roll = renpy.random.randint(1, 100)
    if roll <= 1:
        jump israel
    else: 
        jump begin

label begin:
    vc "Would you like to invest in education?"
    show vccap
    menu:
        "Approve":
            $ education += 5
            $ national_budget -= 10
            $ ach_caretaker_education = True
            $ maybe_award_caretaker()
            vc "You have decided to invest in education. This will increase the education level of the country but will also decrease the national budget."
        "Decline":
            vc "You have declined to invest in education."

    $ award_achievement("first_decision")
    
    vc "Would you like to invest in infrastructure?"
    
    menu:
        "Approve":
            vc "You have invested in infrastructure."
            $ national_budget -= 25
            $ welfare += 5
        "Decline":
            vc "You have declined to invest in infrastructure."
    
    vc "Would you like to promote equal rights?"

    menu: 
        "Approve":
            vc "You have decided to promote equal rights, this will increase the welfare of the country but will also decrease the national budget."
            $ popularity += 10
            $ national_budget -= 15
            jump cap
        "Decline":
            vc "You have declined to promote equal rights."
            jump ass
    

label ass:
    show vccap
    vc "Would you like to Assinate people that fight for equal rights?"
    menu:
        "Approve":
            vc "You have decided to assinate people that fight for equal rights, this will decrease the popularity of the government."
            $ popularity -= 10
            $ award_achievement("assassin")
            jump fas
        "Decline":
            vc "You have declined to assinate people that fight for equal rights."
            jump cap
label cap:  
    show vccap
    vc "Would you like to invest in better housing?"
    menu:
        "Approve":
            vc "You have decided to invest in better housing, this will increase the welfare of the country but will also decrease the national budget."
            $ welfare += 15
            $ national_budget -= 50
            $ ach_caretaker_housing = True
            $ maybe_award_caretaker()
            $ award_achievement("people_reformer")
        "Decline":
            vc "You have declined to invest in better housing."
            $ popularity -= 2

    vc "Would you like to make the buisness state-owned?"

    menu:
        "Approve":
            vc "You have decided to make the buisness state-owned, this will increase the national budget of the country but will also decrease the popularity of the government."
            $ national_budget += 75
            $ popularity -= 10
            $ welfare += 3
            $ award_achievement("state_owned_business")
            jump com
        "Decline":
            vc "You have declined to make the buisness state-owned."
            $ popularity += 2
   
    vc "Would you like to increase taxes on the rich?"
    menu:
        "Approve":
            vc "You have decided to increase taxes on the rich, this will increase the national budget but will also decrease the popularity of the government."
            $ taxes += 5
            $ national_budget += 25
            $ popularity -= 5
            $ award_achievement("rich_taxation")
            vc "Use the money to improve homeless shelters and public transportation."
            menu:
                "Approve":
                    vc "You have decided to use the money to improve homeless shelters and public transportation, this will increase the welfare of the country but will also decrease the national budget."
                    $ welfare += 5
                    $ national_budget -= 10
                    $ ach_caretaker_shelters = True
                    $ maybe_award_caretaker()
                    $ award_achievement("welfare_state")
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
            $ taxes -= 5
            $ national_budget -= 25
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
                            $ national_budget -= 50
                            jump mon
                           
                        "Unite under one nationality":
                            vc "You have decided to stand under the banner of fascism, this will increase the popularity of the government but will also decrease the national budget."
                            $ popularity += 10
                            $ national_budget -= 50
                            jump fas

                "Decline":
                    vc "You listened to the angry citizens and apologized for not reducing taxes on the poor, this has increase the popularity of the government."
                    $ popularity += 2
                    vc "invest in better healthcare"
                    menu:
                        "Approve":
                            vc "You have decided to invest in better healthcare, this will increase the welfare of the country but will also decrease the national budget."
                            $ welfare += 3
                            $ national_budget -= 100
                            $ ach_caretaker_healthcare = True
                            $ maybe_award_caretaker()
                        "Decline":
                            vc "You have declined to invest in better healthcare."
                            $ popularity -= 2
                    vc "inveest in better social security"
                    menu:
                        "Approve":
                            vc "You have decided to invest in better social security, this will increase the welfare of the country but will also decrease the national budget."
                            $ welfare += 3
                            $ national_budget -= 75
                            $ ach_caretaker_social_security = True
                            $ maybe_award_caretaker()
                        "Decline":
                            vc "You have declined to invest in better social security."
                            $ popularity -= 2
                    vc "invest in better nutrition for the poor"
                    menu:
                        "Approve":
                            vc "You have decided to invest in better nutrition for the poor, this will increase the welfare of the country but will also decrease the national budget."
                            $ welfare += 3
                            $ national_budget -= 50
                            $ ach_caretaker_nutrition = True
                            $ maybe_award_caretaker()
                        "Decline":
                            vc "You have declined to invest in better nutrition for the poor."
                            $ popularity -= 2
                    vc "you got outvoted and you have to resign, you have lost the game."
                    jump end

label com:
    show vccap
    vc "Would you like to promote equality?"

    menu:
        "Approve":
            vc "You have decided to promote equality, this will increase the welfare of the country but will also decrease the national budget."
            $ education += 15
            $ national_budget -= 20
            jump soc
        "Decline":
            vc "You have declined to promote equality."

    vc "Would you like to withold leader elecations?"
    
    menu:
        "Approve":
            vc "You have decided to withold leader elecations, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 20
            jump com2
        "Decline":
            vc "You have declined to withold leader elecations."

    vc "Would you like to give power to the people?"
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
    show vccap
    vc "Would you like to give power to the workers?"
    menu:
        "Approve":
            vc "You have decided to give power to the workers, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 20
        "Decline":
            vc "You have declined to give power to the workers."
    hide vccap
    show vccom
    $ ideology = "Communism"
    vc "you are now a communist country"

    vc "Would you like to make the media state-owned?"
    menu:
        "Approve":
            vc "You have decided to make the media state-owned, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 10
            $ power -= 10
            $ national_budget -= 3

        "Decline":
            vc "You have declined to make the media state-owned."
    
    vc "Would you like to promote a one leader mentality?"
    menu:
        "Approve":
            vc "You have decided to promote a one leader mentality, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 20
            $ leader = 1
            $ national_budget -= 0.5
        "Decline":
            vc "You have declined to promote a one leader mentality."
    
    vc "Would you like to introduce a secret police?"
    menu:
        "Approve":
            vc "You have decided to introduce a secret police, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 20
            $ national_budget -= 1.5
            $ award_achievement("secret_police")
            
            vc "would you like remove political opponents?"
            menu:
                "Approve":
                    vc "You have decided to remove political opponents, this will increase the power of the government but will also decrease the popularity of the government."
                    $ power += 10
                "Decline":
                    vc "You have declined to remove political opponents."
        "Decline":
            vc "You have declined to introduce a secret police."

    if leader == 1:
        vc "You have promoted a one leader mentality, now the country has been united under your face."
        $ power += 10
        $ popularity += 10
   
    vc "Would you like to unite a national council"
    menu:
        "Approve": 
            vc "You have decided to unite a national council."
            $ power -= 5
            $ popularity += 5
            $ national_budget -= 5
            jump com4 
        "Decline":
            vc "You have declined to unite a national council."
            jump com3


label com3:
    show vccom
    vc "Would you like to reinstate elections?"
    menu:
        "Approve":
            vc "You have decided to reinstate elections."
            $ power -= 20
            $ popularity += 10
            jump co1

label com4:
    show vccom
    vc "Would you like to unite the country under one banner?"
    menu:
        "Approve":
            vc "You have decided to unite the country under one banner, this will increase the popularity of the government."
            $ popularity += 3
            $ national_budget -= 10
        "Decline":
            jump co1

    
    vc "Would you like to reinstate the militia?"
    menu:
        "Approve":
            vc "You have decided to reinstate the militia, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 10
            $ national_budget -= 5
            $ militia = 1
        "Decline":
            vc "You have declined to reinstate the militia."

    vc "Would you like to militarise the goverment?"
    menu:
        "Approve":
            vc "You have decided to militarise the goverment, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 12
            $ popularity -= 15
            $ national_budget -= 10
        "Decline":
            vc "You have declined to militarise the goverment."
            jump co1

    vc "Would you like to SPREAD THE REVOLUTION?"
    menu:
        "Approve":
            vc "You have decided to spread the revolution, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 5
            $ power += 5
            jump com5
        "Decline":
            vc "You have declined to spread the revolution."
            jump co1
label co1:
    show vccom
    vc "You are about to coup the goverment would you like to proceerd?"
    menu:
        "Approve":
            vc "You have decided to coup the goverment."
            jump co2
        "Decline":
            vc "You have declined to coup the goverment. you will be ccommunist for the rest of your presidency."
            jump com5

label com5:
    show vccom
    vc "SIR, YOU FREED THE WORKERS OF PORTUGAL"
    $ inhabitants += 10104552
    $ welfare += 10
    $ national_budget += 500
    $ corruption += 10
    
    vc "Would you to promote an iberian unification?"
    menu:
        "Approve":
            vc "You have decided to promote an iberian unification, this will increase the popularity."
            $ popularity += 3
            $ education += 2
            $ national_budget -= 30
        "Decline":
            vc "You have declined to promote an iberian unification."
    vc "Would you like to expand military."
    menu:
        "Approve":
            vc "You have decided to expand the military, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 10
            $ national_budget -= 50
            $ military = 1
            $ award_achievement("militarist")
        "Decline":
            vc "You have declined to expand the military."
    vc "Would you like to invest in the workers of iberia?"
    menu:
        "Approve":
            vc "You have decided to invest in the workers of iberia, this will increase the welfare of the country but will also decrease the national budget."
            $ welfare += 10
            $ national_budget -= 20
        "Decline":
            vc "You have declined to invest in the workers of iberia."

    vc "Would you like to INVADE SPAIN?"
    menu:
        "Approve":
            $ popularity += 3
        "Fight":
            $ popularity += 4

    vc "You started a war with spain"
    if military == 0:
        vc "While fighting the spanish army, you send everyone to the frontlines and had nobody left to protect you, so spain was able to assassinate you, you died."
        $ ach_secret_death_assassination = True
        $ maybe_award_secret_death()
        jump end

    if military == 1:
        vc "While fighting the spanish army, you had a strong military and you were able to defend yourself, but the war was long and costly, you lost a lot of popularity and power but you were able to annex spain."
        $ popularity -= 5
        $ power -= 5
        $ national_budget -= 100
        $ welfare -= 7
        $ inhabitants += 37147532
        $ award_achievement("victory_spain")
    
    vc "Would you like to demand Gilbraltar from the UK?"
    menu:
        "Approve":
            vc "You have decided to demand Gilbraltar from the UK."
            $ roll = renpy.random.randint(1, 10)
            if roll == 1:
                vc "The Uk has decided to protect Gilbraltar from you, would you like to declare war on the UK?"
                menu:
                    "Approve":
                        vc "You have deicided to declare war on the Uk and it ended up in you losing the war, because of their naval dominance and you have been seized by the SAS."
                        jump end
                    "Decline":
                        vc "You have declined to declare war on the UK."
            else:
                vc "The UK has decided to concede Gilbraltar to you."
                $ popularity += 5
                $ national_budget += 5
                $ inhabitants += 300000
                $ welfare += 2
                $ award_achievement("diplomatic_victory")
        "Decline":
            vc "You have declined to demand Gilbraltar from the UK."
    vc "Would you like to stomp on Andorra?"
    menu:
        "Approve": 
            vc "You have decided to stomp on Andorra, this will increase the popularity of the government."
            $ popularity += 3
            $ national_budget -= 1
            $ inhabitants += 65115
            $ welfare += 1
        "Decline":
            vc "You have declined to stomp on Andorra."

    vc "You have successfully unified the iberian peninsula, the people are happy and you are now the most powerful leader in the Europe good job."
    $ award_achievement("united_iberia")
    jump end 
    
    
    
label co2: 
    hide vccom
    show vccap
    $ ideology = "Democracy"
    vc "Your country has become a democracy once more"
    vc "woould you want to reform the military"
    menu:
        "Approve":
            vc "You have decided to reform the military, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 5
            $ national_budget -= 50
        "Decline":
            vc "You have declined to reform the military."
            $ military = 1
    vc "Would you like to introduce a capitalist economy?"
    menu:
        "Approve":
            vc "you have decided to introduce a capitalist economy, this will increase the national budget, welfare and popularity"
            $ national_budget += 100
            $ welfare += 10
            $ popularity += 10
        "Decline":
            vc "You have declined to introduce a capitalist economy."
    vc "Would you like to introduce a free press?"
    menu:
        "Approve":
            vc "You have decided to introduce a free press, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 10
            $ power -= 8
            $ national_budget -= 5
        "Decline":
            vc "You have declined to introduce a free press."
            $ popularity -= 2
    vc "do you want to re-introduce elections and the parliament?"
    menu:
        "Approve":
            vc "You have decided to re-introduce elections and the parliament, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 10
            $ power -= 20
            $ award_achievement("democratic_return")
            vc "your country is once again a full democracy, but sadly the first thing they wanted to do is hold new elections and they have voted you out of office, you have lost the game."
            jump end
        "Decline":
            vc "You have declined to re-introduce elections and the parliament."
            $ popularity -= 5
            $ power += 10
            if military == 1:
                vc "The military has decided to support you and they have helped you to coup the goverment, you are now a military regime."
                jump milr
            else:
                vc "there is no military  so you got overthrown, you have lost the game."
                jump end
label milr:
    show vcmil
    if militia == 1:
        vc "The militia has saved you from being assinated"
    else:
        n "you got assinated because you didn't have a militia to protect you, you have lost the game."
        $ ach_secret_death_assassination = True
        $ maybe_award_secret_death()
        jump end
    vc "you executed the conspiritators making the people hate and fear you, but you are still in power."
    $ power += 20
    $ popularity -= 20
    vc "after countless of assasination attempts they finally succeeded and you got assinated, you have lost the game."
    $ ach_secret_death_assassination = True
    $ maybe_award_secret_death()
    jump end



label arch:
    show vcarc
    $ ideology = "Anarchist"
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
    hide vcarc

    n "You achieved total Anarchy, the people are now in control of the country and you have no more power, good luck."
    $ award_achievement("anarchist_vision")

    n "A couple days later, while you are walking home, you get hit by a car and die."
    $ ach_secret_death_accident = True
    $ maybe_award_secret_death()

    na "The end."
    jump end

label soc:
    show vccap
    vc "More people started working."
    $ national_budget += 50
    $ welfare += 5
    vc "Would you like to nationalise the major industries?"
    menu:
        "Approve":
            vc "You have decided to nationalise the major industries, this will increase the national budget but will also decrease the popularity of the government."
            $ national_budget += 100
            $ popularity += 5
            $ welfare += 5
        "Decline":
            vc "You have declined to nationalise the major industries."
    hide vccap
    show vcsoc
    vc "Would you like to introduce a universal healthcare system?"
    menu:
        "Approve": 
            vc "You have decided to introduce a universal healthcare system, this will increase the welfare of the country but will also decrease the national budget."
            $ welfare += 10
            $ national_budget -= 50
        "Decline":
            vc "You have declined to introduce a universal healthcare system."

    vc "Would you like to introduce an increase in worker ownership?"
    menu:
        "Approve":
            vc "You have decided to introduce an increase in worker ownership, this will increase the welfare of the country but will also decrease the national budget."
            $ welfare += 5
            $ national_budget -= 25
        "Decline":
            vc "You have declined to introduce an increase in worker ownership."

    vc "Would you like to guarantee housing for all citizens?"
    menu:
        "Approve":
            vc "You have decided to guarantee housing for all citizens, this will increase the welfare of the country but will also decrease the national budget."
            $ welfare += 10
            $ national_budget -= 50
        "Decline":
            vc "You have declined to guarantee housing for all citizens."
    vc "Would you like to introduce a 4 day work week?"
    menu:
        "Approve":
            vc "You have decided to introduce a 4 day work week, this will increase the welfare of the country but will also decrease the national budget."
            $ welfare -= 5
            $ national_budget -= 25
        "Decline":
            vc "You have declined to introduce a 4 day work week."
            jump socgood
    
    vc "Would you like to introduce a 3 day work week?"
    menu:
        "Approve":
            vc "You have decided to introduce a 3 day work week, this will increase the welfare of the country but will also decrease the national budget."
            $ welfare -= 10
            $ national_budget -= 50
            jump socshit
        "Decline":
            vc "You have declined to introduce a 3 day work week."
            jump socgood

label socshit:
    show vcsoc
    vc "You have made the people happy,but your economic growth has flatlined."
    jump end

label socgood:
    show vcsoc 
    vc "The democrats and the socliast are both happy with your decisions and they have decided to work together to make the country better, this has increased the popularity of the government and the welfare of the country."
    $ popularity += 10
    $ welfare += 10
    vc "You have made the people happy and your economic growth is booming."
    jump end

label mon:
    hide vccap
    $ ideology = "Monarchy"
    show vcmon
    vc "would you like to build a palace for yourself?"
    menu:
        "Approve":
            vc "the people like your palace but a few people lost their lives due to poor working conditions."
            $ power += 5
            $ national_budget -= 50
            $ popularity += 5
            $ inhabitants -= 100
        "Decline":
            vc "You have declined to build a palace for yourself."

    vc "Would you like to legalize incest to keep the power in the family?"
    menu:
        "approve":
            vc "You have decided to legalize incest to keep the power in the family."
            $ welfare -= 20
            $ inhabitants += 2000000
            $ taxes += 2
        "Decline":
            vc "nothing happens because nothing changes"
    
    vc "Would you like to bring back the guillotine?"
    menu:
        "Approve":
            vc "You have decided to bring back the guillotine."
            $ power += 20
            $ national_budget -= 0.0005
        "decline":
            vc "You have declined to bring back the guillotine."

    vc "Do you want to force religion on the population?"
    menu:
        "Approve":
            vc "You have decided to force religion on the population."
            $ power += 10
            $ popularity -= 10
            jump mon1
        "Decline":
            vc "You have declined to force religion on the population." 
            jump mon2

label mon1:
    show vcmon
    vc "You have made good first use of your guillotine by organizing a public execution for the people that refused to follow the religion."
    $ inhabitants -= 1000

    vc "The people have accepted the religion and you become emperor."

    vc "Do you want to make the people worship you as a god?"
    menu:
        "Approve":
            vc "You have become untouchable and you have become a god in the eyes of the people."
            $ award_achievement("monarchy_emperor")
            
        "Decline":
            vc "You have declined to make the people worship you as a god."
            
    vc "Would you like to invest in the royal army?"
    menu:
        "Approve":  
            vc "you continue to start prepaing for war"
            $ power += 20
            $ national_budget -= 50
            $ royal_army = 1
        "Decline":
            vc "You have declined to invest in the royal army."
            $ royal_army = 0    

    vc "Do you want to start a war with Portugal?"
    menu:
        "Approve":
            jump mon_war
        "Yes":
            jump mon_war
label mon_war:
    show vcmon
    scene bg mon
    if royal_army == 1:
        vc "You started a war with Portugal and you won because of your strong royal army."
        $ inhabitants += 10400000
        $ taxes += 7
    else:
        $ roll = renpy.random.randint(1, 10)
        if roll <= 4:
            vc "you started a war with Portugal and won because of your tactics and the support of the people."
            $ inhabitants += 10400000
            $ taxes += 7
        else:
            vc "You started a war with Portugal and you lost because your army wasn't good"
            vc "Portugal annexed Listenbourg and you don't have any more power, you decided to open a bakery and you lived a happy life"
            $ award_achievement("open_bakery")
            jump end

    vc "would you like to start a war with spain?"
    menu:
        "Approve":
            if royal_army == 1:
                $ roll = renpy.random.randint(1, 10)
                if roll <= 7:
                    vc "You started a war with Spain and you won because of your strong royal army."
                    $ inhabitants += 47900000
                    $ taxes += 15
                else:
                    vc "You started a war with Spain and you lost because Spain was already prepared for war"
                    vc "Spain annexed Listenbourg and you don't have any more power"
                    jump end
            else:
                $ roll = renpy.random.randint(1, 10)
                if roll <= 4:
                    vc "You started a war with Spain and you won because of your tactics and the support of the people."
                    $ inhabitants += 47900000
                    $ taxes += 15
                else:
                    vc "You started a war with Spain and you lost because your army wasn't good"
                    vc "Spain annexed Listenbourg and you don't have any more power,"
                    jump end

    vc "would you like to annex Andorra?"
    menu:
        "Approve":
            $ roll = renpy.random.randint(1, 100)
            if roll <= 1:
                vc "You started a war with Andorra and you lost because Andorra had a strong army of 10 soldiers"
                vc "Andorra annexed Listenbourg and you don't have any more power"
                jump end
            else:
                vc "Andorra surrendered to you without a fight and you annexed Andorra."
                $ inhabitants += 83000
                $ taxes += 1
    vc "Would you like to demand Gilbraltar from the UK?"
    menu:          
        "Approve":
            vc "You have decided to demand Gilbraltar from the UK."
            $ roll = renpy.random.randint(1, 10)
            if roll == 1:
                vc "The Uk has decided to protect Gilbraltar from you, would you like to declare war on the UK?"
                menu:
                    "Approve":
                        vc "You have deicided to declare war on the Uk and it ended up in you losing the war, because of their naval dominance and you have been seized by the SAS."
                        jump end
                    
            else:
                vc "The UK has decided to concede Gilbraltar to you."
                $ popularity += 5
                $ national_budget += 5
                $ inhabitants += 300000
                $ welfare += 2
                $ award_achievement("diplomatic_victory")

    vc "You have successfully reunited the iberian peninsula"
    $ award_achievement("united_iberia")

    vc "How do you want to expand your empire?"
    menu:
        "Expand into europe":
            jump imp
        "Build colonies":
            jump col
    
label mon2:
        show vcmon
        vc "The people liked your decision to not force religion on them and they have accepted you as their king."
        $ award_achievement("merciful_king")
        $ ach_secret_death_natural = True
        $ maybe_award_secret_death()
        vc "You have become a beloved king and you died surrounded by your family and friends."
        jump end
label fas:
    hide vccap
    $ ideology = "Fascist"
    call screen stats
    show vcfas
    vc "Do you accept to have one man in power?"

    menu:
        "Approve":
            vc "You have decided to have one man in power, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 10
            jump fasc2
        "Decline":
            vc "You have declined to have one man in power."
            jump fasc1

label fasc1:
    show vcfas
    n " you have been assassinated by a diffrent power in the government, you have lost the game"
    $ ach_secret_death_assassination = True
    $ maybe_award_secret_death()
    jump end

label fasc2:
    show vcfas
    vc "Would you like to invest in a secret police?"

    menu:
        "Approve":
            vc "You have decided to invest in a secret police, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ national_budget -= 0.2
            $ award_achievement("secret_police")
        "Decline":
            vc "You have declined to invest in a secret police."
    
        vc "Do you want to exterminate the opposition?"

    menu:
        "Approve":
            $ roll = renpy.random.randint(1, 10)
            if roll == 1:
                n "The opposition has been able to fight back and you have been assassinated, you have lost the game"
                $ ach_secret_death_assassination = True
                $ maybe_award_secret_death()
                jump end
            elif roll == 2:
                vc "People have found out about the extermination"
                $ popularity -= 30
                $ power += 15
                jump fasc3
            else: 
                vc "You have assassinated the opposition in their sleep by slicing their throats."
                $ power += 20
                jump fasc3

        
        "Decline":
            vc "You have declined to exterminate the opposition."
            n "Your political opponents didn't like you and they have been able to assassinate you, you have lost the game"
            $ ach_secret_death_assassination = True
            $ maybe_award_secret_death()
            jump end
label fasc3:
    show vcfas
    vc "Do you want to introduce propaganda in the media?"

    menu: 
        "Approve":
            vc "You have decided to introduce propaganda in the media, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity += 15
            jump fasc4
        "Decline":
            vc "You have declined to introduce propaganda in the media."
            n "The media has been able to criticize you and you have been assassinated, you have lost the game"
            $ ach_secret_death_assassination = True
            $ maybe_award_secret_death()
            jump end


    

label fasc4:

    vc "You have brainwashed the population with propaganda, what do you want them to do?"



    menu:

        "let them work more":
            jump fasc_work

        "build infrastructure":
            jump fasc_infa

        "increase population":
            jump fasc_pop

        "do nothing":
            jump fasc_end

    

    label fasc_work:

        vc "You have decided to let the population work more, this will increase the national budget but will also decrease the popularity of the government."

        $ national_budget += 50000000000

        $ popularity -= 10

        jump fasc_end

       



    label fasc_infa:

        vc "You have decided to build infrastructure, this will increase the welfare of the country but will also decrease the national budget."

        $ welfare += 10

        $ national_budget -= 50000000000

        jump fasc_end



    label fasc_pop:

        vc "would you like to force population growth?"

        menu:
            "Approve":

                vc "You have decided to force population growth, this will increase the inhabitants of the country but will also decrease the popularity of the government."

                $ inhabitants += 10000000

                $ popularity -= 10

                jump fasc_end

            "Decline":

                vc "You have declined to force population growth this still increases the population but with less impact."

                $ inhabitants += 5000000

                jump fasc_end



    label fasc_end:

        if popularity >= 50:

            $ roll = renpy.random.randint(1, 10)

            if roll <= 4:

                n "you have gained full control of your country and you have been able to win the game"

                jump end

            else:

                n "The population has revolted against you and you have been assassinated, you have lost the game"

                jump end



        else:

            $ roll = renpy.random.randint(1, 10)

            if roll <= 1:

                n "you have gained full control of your country and you have been able to win the game"

                jump end

            else:

                n "The population has revolted against you and you have been assassinated, you have lost the game"

                jump end

label imp:
    vc "You have decided to expand into Europe you have to prepare for war"
    $ power += 20
    $ national_budget -= 50

    vc "Would you like to trade with Germany to get more resources for the war?"
    menu:
        "Approve":
            vc "You have decided to trade with Germany"
            $ Alliance_steel = 1

        "Decline":
            vc "You have declined to trade with Germany"
            $ Alliance_steel = 0

    if Alliance_steel == 1:
        vc "Would you like to have an alliance with Germany?"
        menu:
            "Approve":
                vc "You have decided to have an alliance with Germany, this will increase the power of the government but will also decrease the popularity of the government."
                $ alliance_germany = 1
                jump imp2
            "Decline":
                vc "You have declined to have an alliance with Germany."
                $ alliance_germany = 0
                jump imp2
    else:
        jump imp2
label imp2:
    $ ideology = "Imperialism"
    show vcimp
    scene bg imp
    vc "Do you want to start a war with France?"
    menu:
        "Approve":
            if alliance_germany == 1:
                $ roll = renpy.random.randint(1, 10)
                if roll <= 8:
                    vc "You started a war with France and you won because of your alliance with Germany and you could attack from two fronts."
                    vc "You and germany shared the land of France."
                    $ inhabitants += 30000000
                    $ taxes += 20
                    $ national_budget -= 25
                else:
                    vc "You started a war with France and you lost because France was too strong even with your alliance with Germany."
                    vc "France annexed Listenbourg and you don't have any more power."
                    jump end
    vc "Would you like to rebuild the economy of the country after the war?"
    menu:
        "Approve":
            vc "You have decided to rebuild the economy of the country after the war."
            $ national_budget += 25
         
        "Decline":
            vc "You have declined to rebuild the economy of the country after the war."

    vc "do you want to help Germany to invade Austria?"
    menu:
        "Approve":
            vc "You have decided to help Germany to invade Austria."
            $ austria_invasion = 1
        "Decline":
            vc "You have declined to help Germany to invade Austria."
            $ austria_invasion = 0
    vc "Do you want to invade Italy?"
    menu:
        "Approve":
            if austria_invasion == 1:
                $ roll = renpy.random.randint(1, 10)
                if roll <= 7:
                    vc "You started a war with Italy and you won because Germany was able to help you because they border Italy and you could attack from two fronts."
                    vc "You annexed Italy."
                    $ inhabitants += 60000000
                    $ taxes += 15
                    $ national_budget -= 15
                else:
                    vc "You started a war with Italy and you lost because Italy was too strong even with your alliance with Germany."
                    vc "Italy annexed Listenbourg and you don't have any more power."
                    jump end
            else:
                $ roll = renpy.random.randint(1, 10)
                if roll <= 4:
                    vc "You started a war with Italy and you won because of your tactics and the support of the people."
                    vc "You annexed Italy."
                    $ inhabitants += 60000000
                    $ taxes += 15
                    $ national_budget -= 15
                else:
                    vc "You started a war with Italy and you lost because Germany"
                    vc "Italy annexed Listenbourg and you don't have any more power,"
                    jump end
    vc "Do you want to take San Marino?"
    menu:
        "Approve":
            vc "You have decided to take San Marino, this will increase the popularity of the government."
            $ national_budget -= 1
            $ inhabitants += 34000

    vc "do you want to invade the balkans?"
    menu:
        "Approve": 
            $ roll = renpy.random.randint(1, 10)
            if roll <= 7:
                vc "You started a war with the Balkans and you won because of your strong army."
                vc "You annexed the Balkans."
                $ inhabitants += 50000000
                $ taxes += 10
                $ national_budget -= 25
            else:
                vc "You started a war with the Balkans and you lost because the Balkans were too strong."
                vc "The Balkans annexed Listenbourg and you don't have any more power,"
                jump end

    vc "would you like to invest in the air force?"
    menu:
        "Approve":
            vc "You have decided to invest in the air force."
            $ power += 10
            $ national_budget -= 50
        "Decline":
            vc "You have declined to invest in the air force."
    vc "Would you like to invade Türkiye?"
    menu:
        "Approve":
            $ roll = renpy.random.randint(1, 10)
            if roll <= 7:
                vc "You started a war with Türkiye and you won because of your strong air force."
                vc "You annexed Türkiye."
                $ inhabitants += 80000000
                $ taxes += 25
                $ national_budget -= 50
            else:
                vc "You started a war with Türkiye and you lost because Türkiye was too strong."
                vc "Türkiye annexed Listenbourg and you don't have any more power,"
                jump end
    vc "Would you like to invest in the navy?"
    menu:
        "Approve":
            vc "You have decided to invest in the navy."
            $ power += 10
            $ national_budget -= 50
        "Decline":
            vc "You have declined to invest in the navy."
    vc "Do you want to demand the north coast of Africa."
    menu:
        "Approve":
            $ roll = renpy.random.randint(1, 10)
            if roll <= 7:
                vc "They agreed to your demands because of your strong army."
                vc "You annexed the north coast of Africa."
                $ inhabitants += 100000000
                $ taxes += 5
            
            else:
                vc "You started a war with northern Africa and you lost because the north coast of Africa was too strong."
                vc "The northern Africa annexed Listenbourg and you don't have any more power,"
                jump end

    vc "Do you want to connect your territories in Europe and Africa by taking the middle east?"
    menu:
        "Approve":
            $ roll = renpy.random.randint(1, 10)
            if roll <= 7:
                vc "You started a war with the middle east and you won because of your strong army."
                vc "You annexed the middle east."
                $ inhabitants += 200000000
                $ taxes += 10
                $ national_budget -= 25
            else:
                vc "You started a war with the middle east and you lost because the middle east was too strong."
                vc "The middle east annexed Listenbourg and you don't have any more power,"
                jump end
    vc "How would you like to name your empire?"
    menu:
        "The Imperial Commonwealth of Listenbourg":
            vc "You have decided to name your empire The Imperial Commonwealth of Listenbourg."
            vc "You have successfully created an empire that spans across three continents, you are now the most powerful leader in the world."
            jump end
        "Imperium Romanum":
            vc "You have decided to name your empire Imperium Romanum."
            vc "Your lifelong dream of bringing back the Roman Empire has come true."
            vc "You have brought back old Roman values and culture."
            jump end
label israel:
    show vccap
    vc "Do you want to give money to Israel?"
    menu:
        "Approve":
            vc "You have decided to give money to Israel."
            $ national_budget -= 50
            $ corruption += 20
            jump begin
        "Decline":
            vc "You have been assaninated by the Mossad, you have lost the game."
            $ ach_secret_death_assassination = True
            $ maybe_award_secret_death()
            jump end
label end:
    hide vccap
    hide vccom
    hide vcfas
    hide vcmon
    hide vcmil
    hide vcarc
    hide vcsoc
    hide vctot
    
    na "Would you like to play again?"
    menu:
        "Yes":
            $ playthroughs += 1
            if playthroughs >= 5:
                $ award_achievement("secret_five_runs")
            $ education = 60
            $ national_budget = 1000
            $ welfare = 60
            $ inhabitants = 40000000
            $ corruption = 5
            $ ideology = "Democracy"
            $ power = 60
            $ taxes = 20
            $ leader = 0
            $ militia = 0
            $ military = 0
            $ days = 0
            $ popularity = 60
            jump start
        "No":
            return
        "Look at statscreen":
            call screen stats
            jump end
            
    # This ends the game 


    return