﻿# The script of the game goes in this file.

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
default curfew = 0
default nuclear = 0
default warwinchance = 50
default workcamps = 0
default recource_exploitation = 0
default royal_army = 0
default royal_navy = 0
default Alliance_germany = 0
default Alliance_steel = 0
default austria_invasion = 0
default navy = 0
default uk = 0
default dock = 0
default generals = 0
default asia = 0
default africa = 0
default americas = 0
default aliances = 0

default days = 0
default playthroughs = 0
default choice_count = 0
default budget_warning_seen = False

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
default ach_secret_death_assassination = True
default ach_secret_death_accident = True
default ach_secret_death_natural = True
default ach_nuclear_program = False
default ach_war_champion = False
default ach_resource_exploiter = False
default ach_military_regime = False
default ach_peacekeeper = False
default ach_reclaim_cuba = False
default ach_the_iberian_company = False

default ach_open_bakery = False
default ach_tax_relief = False
default ach_corruption_crusader = False
default ach_municipal_reformer = False


init python:
    config.game_menu_action = ShowMenu("stats")
    config.keymap["game_menu"] = ["q"]
    config.overlay_screens.append("debug_hotkey")

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
        "nuclear_program": "Nuclear Program",
        "resource_exploiter": "Resource Exploiter",
        "military_regime": "Military Regime",
        "peacekeeper": "Peacekeeper",
        "open_bakery": "Bakery Owner",
        "tax_relief": "Tax Relief",
        "corruption_crusader": "Corruption Crusader",
        "municipal_reformer": "Municipal Reformer",
        "reclaim_cuba": "Cuban Reclaimer",
        "the_iberian_company": "The Iberian Company",
    }

    def record_choice():
        renpy.store.choice_count = getattr(renpy.store, "choice_count", 0) + 1
        if renpy.store.choice_count % 3 == 0:
            renpy.store.national_budget += renpy.store.taxes
            renpy.notify("Every 3 choices: national budget +{} billion".format(renpy.store.taxes))


    def reset_budget_warning_if_positive():
        if renpy.store.national_budget >= 0:
            renpy.store.budget_warning_seen = False

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
                    "nuclear_program",
                    "war_champion",
                    "resource_exploiter",
                    "military_regime",
                    "peacekeeper",
                    "open_bakery",
                    "tax_relief",
                    "corruption_crusader",
                    "municipal_reformer",
                    "reclaim_cuba",
                    "the_iberian_company",
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

    def set_debug_values():
        renpy.store.education = 1000
        renpy.store.national_budget = 100000
        renpy.store.welfare = 1000
        renpy.store.inhabitants = 50000000
        renpy.store.corruption = 0
        renpy.store.popularity = 1000
        renpy.store.power = 1000
        renpy.store.taxes = 500
        renpy.store.military = 1
        renpy.store.aliances = 1
        renpy.store.playthroughs = 5
        renpy.store.militia = 1
        renpy.notify("Debug values set to high test values.")

    def unlock_all_achievements():
        for name in achievement_defs:
            award_achievement(name)
        renpy.notify("Debug: all achievements unlocked.")

init -2 python:
    # Fallback defaults for variables that may be missing from older saves or broken state.
    # The normal Ren'Py defaults are declared above with the `default` statements.
    defaults = {
        "navy": 0,
        "uk": 0,
        "generals": 0,
        "dock": 0,
        "education": 60,
        "national_budget": 1000,
        "welfare": 60,
        "inhabitants": 40000000,
        "corruption": 5,
        "popularity": 60,
        "ideology": "Democracy",
        "power": 60,
        "taxes": 20,
        "curfew": 0,
        "nuclear": 0,
        "warwinchance": 0,
        "workcamps": 0,
        "recource_exploitation": 0,
        "leader": 0,
        "militia": 0,
        "military": 0,
        "aliances": 0,
        "days": 0,
        "playthroughs": 0,
        "choice_count": 0,
        "budget_warning_seen": False,
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
        "ach_secret_five_runs": False,
        "ach_secret_every_death": False,
        "ach_secret_caretaker": False,
        "ach_caretaker_education": False,
        "ach_caretaker_housing": False,
        "ach_caretaker_shelters": False,
        "ach_caretaker_healthcare": False,
        "ach_caretaker_social_security": False,
        "ach_caretaker_nutrition": False,
        "ach_secret_death_assassination": True,
        "ach_secret_death_accident": True,
        "ach_secret_death_natural": True,
        "ach_nuclear_program": False,
        "ach_war_champion": False,
        "ach_resource_exploiter": False,
        "ach_military_regime": False,
        "ach_peacekeeper": False,
        "ach_open_bakery": False,
        "ach_tax_relief": False,
        "ach_corruption_crusader": False,
        "ach_municipal_reformer": False,
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
            "nuclear_program": "Nuclear Program",
            "war_champion": "War Champion",
            "resource_exploiter": "Resource Exploiter",
            "military_regime": "Military Regime",
            "peacekeeper": "Peacekeeper",
            "open_bakery": "Bakery Owner",
            "tax_relief": "Tax Relief",
            "corruption_crusader": "Corruption Crusader",
            "municipal_reformer": "Municipal Reformer",
            "reclaim_cuba": "Cuban Reclaimer",
            "the_iberian_company": "The Iberian Company",
        },
    }

    for name, value in defaults.items():
        if not hasattr(renpy.store, name):
            setattr(renpy.store, name, value)

screen debug_hotkey():
    key "d" action ShowMenu("debug_prompt")

screen debug_prompt():
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)

        vbox:
            spacing 10

            text "Enter debug command:" size 24 xalign 0.5
            input value Variable("debug_command_text") allow "abcdefghijklmnopqrstuvwxyz"

            hbox:
                spacing 20
                textbutton "Submit" action If(PythonCondition("debug_command_text.lower() == 'debug'"), [SetVariable("debug_command_text", ""), Hide("debug_prompt"), ShowMenu("debug_menu")], Function(renpy.notify, "Invalid command"))
                textbutton "Cancel" action [SetVariable("debug_command_text", ""), Hide("debug_prompt")]

screen debug_menu():

    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        xsize 980
        ysize 620

        hbox:
            xfill True
            spacing 20

            vbox:
                xsize 420
                spacing 6

                text "Debug Menu" size 26 xalign 0.5
                text "Press D at any time to open this menu." size 14 xalign 0.5

                textbutton "Edit all values to high test values" action Function(set_debug_values)
                textbutton "Unlock all achievements" action Function(unlock_all_achievements)
                textbutton "Close" action Hide("debug_menu")

            vbox:
                xsize 420
                spacing 6

                text "Jump to" size 18 xalign 0.5
                textbutton "Start" action [Hide("debug_menu"), Function(renpy.jump, "start")]
                textbutton "Democracy " action [Hide("debug_menu"), Function(renpy.jump, "begin")]
                textbutton "Communism " action [Hide("debug_menu"), Function(renpy.jump, "com")]
                textbutton "Militarism " action [Hide("debug_menu"), Function(renpy.jump, "milr")]
                textbutton "Anarchism " action [Hide("debug_menu"), Function(renpy.jump, "arch")]
                textbutton "Socialism " action [Hide("debug_menu"), Function(renpy.jump, "soc")]
                textbutton "Monarchy " action [Hide("debug_menu"), Function(renpy.jump, "mon")]
                textbutton "Fascism " action [Hide("debug_menu"), Function(renpy.jump, "fasc1")]
                textbutton "Colonialismp" action [Hide("debug_menu"), Function(renpy.jump, "col")]
                textbutton "Final end screen" action [Hide("debug_menu"), Function(renpy.jump, "end")]

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
            textbutton "Close stats" action Hide("stats") xalign 1.0

screen achievements():

    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        xsize 1080
        ysize 620

        vbox:
            spacing 10
            xfill True

            text "Achievements" size 34 xalign 0.5

            hbox:
                xfill True
                spacing 18

                vbox:
                    xsize 320
                    spacing 6
                    text "Main Achievements" size 18 color "#cfe8ff" xalign 0.5
                    $ main_items = [
                        (name, label)
                        for name, label in achievement_defs.items()
                        if not name.startswith("secret_") and name != "completionist"
                    ]
                    $ main_mid = (len(main_items) + 1) // 2
                    for name, label in main_items[:main_mid]:
                        if getattr(store, "ach_" + name, False):
                            text "[label] - Unlocked" size 18 color (getattr(store, "ach_completionist", False) and "#ffd700" or "#fff")
                        else:
                            text "[label] - Locked" size 18 color (getattr(store, "ach_completionist", False) and "#ffd700" or "#888")

                vbox:
                    xsize 300
                    spacing 8
                    text "Completionist" size 18 color "#ffd700" xalign 0.5
                    if getattr(store, "ach_completionist", False):
                        text "[achievement_defs.get('completionist', 'Presidential Legacy')] - Unlocked" size 18 color "#ffd700"
                    else:
                        text "[achievement_defs.get('completionist', 'Presidential Legacy')] - Locked" size 18 color "#888"
                    null height 12
                    text "Secret Achievements" size 18 color "#d8b4fe" xalign 0.5
                    for name, label in achievement_defs.items():
                        if name.startswith("secret_"):
                            if not getattr(store, "ach_" + name, False):
                                text "Secret Achievement - Locked" size 18 color "#888"
                            else:
                                text "[label] - Unlocked" size 18 color "#800080"

                vbox:
                    xsize 320
                    spacing 6
                    text "Main Achievements" size 18 color "#cfe8ff" xalign 0.5
                    for name, label in main_items[main_mid:]:
                        if getattr(store, "ach_" + name, False):
                            text "[label] - Unlocked" size 18 color (getattr(store, "ach_completionist", False) and "#ffd700" or "#fff")
                        else:
                            text "[label] - Locked" size 18 color (getattr(store, "ach_completionist", False) and "#ffd700" or "#888")

            textbutton "Close" action Return() xalign 0.5 yalign 1.0


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

    scene bg dem
    n "You have been elected by the people to be the president of listenbourg"
    n "Just before you became president, all aliances were disbanded including the UN, EU and Bricks, because of mistrust after a gigantic data leak."
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
    scene bg dem
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
    scene bg dem
    show vccap
    vc "Would you like to assassinate people that fight for equal rights?"
    menu:
        "Approve":
            vc "You have decided to assassinate people that fight for equal rights, this will decrease the popularity of the government."
            $ popularity -= 10
            $ award_achievement("assassin")
            jump fas
        "Decline":
            vc "You have declined to assassinate people that fight for equal rights."
            jump cap
label cap:  
    scene bg dem
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

    vc "Would you like to make the business state-owned?"

    menu:
        "Approve":
            vc "You have decided to make the business state-owned, this will increase the national budget of the country but will also decrease the popularity of the government."
            $ national_budget += 75
            $ popularity -= 10
            $ welfare += 3
            $ award_achievement("state_owned_business")
            jump com
        "Decline":
            vc "You have declined to make the business state-owned."
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
    vc "Reduce the taxes on the poor?"
    menu:
        "Approve":
            vc "You have decided to reduce taxes on the poor, this will increase the popularity of the government but will also decrease the national budget."
            $ taxes -= 5
            $ national_budget -= 25
            $ popularity += 5
            $ award_achievement("tax_relief")
        "Decline":
            vc "You have declined to reduce taxes on the poor."
            $ popularity -= 2
            vc "Ignore the angry citizens and continue with your presidency"
            menu:
                "Approve":
                    vc "You have decided to ignore the angry citizens and continue with your presidency, this will decrease the popularity of the government."
                    $ popularity -= 5
                    vc "The citizens start a revolution choose the banner you will stand under"
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
                    vc "Invest in better healthcare"
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
                    vc "Invest in better social security"
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
                    vc "Invest in better nutrition for the poor"
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
                    vc "You got outvoted and you have to resign, you have lost the game."
                    jump end

label com:
    scene bg dem
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

    vc "Would you like to withhold leader elections?"
    
    menu:
        "Approve":
            vc "You have decided to withhold leader elections, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 20
            jump com2
        "Decline":
            vc "You have declined to withhold leader elections."

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
    scene bg dem
    show vccap
    vc "Would you like to give power to the workers?"
    menu:
        "Approve":
            vc "You have decided to give power to the workers, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 20
        "Decline":
            vc "You have declined to give power to the workers."
    hide vccap
    scene bg com
    show vccom
    $ ideology = "Communism"
    vc "You are now a communist country"

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
            
            vc "Would you like remove political opponents?"
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
    scene bg com
    show vccom
    vc "Would you like to reinstate elections?"
    menu:
        "Approve":
            vc "You have decided to reinstate elections."
            $ power -= 20
            $ popularity += 10
            jump co1

label com4:
    scene bg com
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

    vc "Would you like to militarise the government?"
    menu:
        "Approve":
            vc "You have decided to militarise the government, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 12
            $ popularity -= 15
            $ national_budget -= 10
        "Decline":
            vc "You have declined to militarise the government."
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
    scene bg com
    show vccom
    vc "You are about to coup the government would you like to proceeded?"
    menu:
        "Approve":
            vc "You have decided to coup the government."
            jump co2
        "Decline":
            vc "You have declined to coup the government. you will be communist for the rest of your presidency."
            jump com5

label com5:
    scene bg com
    show vccom
    vc "SIR, YOU FREED THE WORKERS OF PORTUGAL"
    $ inhabitants += 10104552
    $ welfare += 10
    $ national_budget += 500
    $ corruption += 10
    
    vc "Would you to promote an Iberian unification?"
    menu:
        "Approve":
            vc "You have decided to promote an Iberian unification, this will increase the popularity."
            $ popularity += 3
            $ education += 2
            $ national_budget -= 30
        "Decline":
            vc "You have declined to promote an Iberian unification."
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
    vc "Would you like to invest in the workers of Iberia?"
    menu:
        "Approve":
            vc "You have decided to invest in the workers of Iberia, this will increase the welfare of the country but will also decrease the national budget."
            $ welfare += 10
            $ national_budget -= 20
        "Decline":
            vc "You have declined to invest in the workers of Iberia."

    vc "Would you like to INVADE SPAIN?"
    menu:
        "Approve":
            $ popularity += 3
        "Fight":
            $ popularity += 4

    vc "You started a war with Spain"
    if military == 0:
        vc "While fighting the Spanish army, you send everyone to the frontlines and had nobody left to protect you, so Spain was able to assassinate you, you died."
        $ ach_secret_death_assassination = True
        $ maybe_award_secret_death()
        jump end

    if military == 1:
        vc "While fighting the Spanish army, you had a strong military and you were able to defend yourself, but the war was long and costly, you lost a lot of popularity and power but you were able to annex Spain."
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
                vc "The UK has decided to protect Gilbraltar from you, would you like to declare war on the UK?"
                menu:
                    "Approve":
                        vc "You have decided to declare war on the UK and it ended up in you losing the war, because of their naval dominance and you have been seized by the SAS."
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

    vc "You have successfully unified the Iberian peninsula, the people are happy and you are now the most powerful leader in the Europe good job."
    $ award_achievement("united_iberia")
    jump end 
    
    
    
label co2: 
    scene bg dem
    hide vccom
    show vccap
    $ ideology = "Democracy"
    vc "Your country has become a democracy once more"
    vc "Would you want to reform the military"
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
            vc "You have decided to introduce a capitalist economy, this will increase the national budget, welfare and popularity"
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
    vc "Do you want to re-introduce elections and the parliament?"
    menu:
        "Approve":
            vc "You have decided to re-introduce elections and the parliament, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 10
            $ power -= 20
            $ award_achievement("democratic_return")
            vc "Your country is once again a full democracy, but sadly the first thing they wanted to do is hold new elections and they have voted you out of office, you have lost the game."
            jump end
        "Decline":
            vc "You have declined to re-introduce elections and the parliament."
            $ popularity -= 5
            $ power += 10
            if military == 1:
                vc "The military has decided to support you and they have helped you to coup the government, you are now a military regime."
                $ award_achievement("military_regime")
                jump milr
            else:
                vc "There is no military  so you got overthrown, you have lost the game."
                jump end
label milr:
    scene bg mil
    show vcmil
    if militia == 1:
        vc "The militia has saved you from being assassinated"
    else:
        n "You got assassinated because you didn't have a militia to protect you, you have lost the game."
        $ ach_secret_death_assassination = True
        $ maybe_award_secret_death()
        jump end
    vc "You executed the conspirators making the people hate and fear you, but you are still in power."
    $ power += 20
    $ popularity -= 20
    vc "Do you establish military schools to train the next generation of soldiers?"
    menu:
        "Approve":
            vc "You have decided to establish military schools to train the next generation of soldiers, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 10
            $ national_budget -= 70
        "Decline":
            vc "You have declined to establish military schools to train the next generation of soldiers."
    vc "Do you invest in better weapons and equipment for the military?"
    menu:
        "Approve":
            vc "You have decided to invest in better weapons and equipment for the military, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 15
            $ popularity += 5
            $ national_budget -= 50
        "Decline":
            vc "You have declined to invest in better weapons and equipment for the military."
    vc "Do you take control of the media to spread propaganda and control the population?"
    menu:
        "Approve":
            vc "You have decided to take control of the media to spread propaganda and control the population, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 15
            $ national_budget -= 10
        "Decline":
            vc "You have declined to take control of the media to spread propaganda and control the population."
            $ popularity += 5
    vc "Do you introduce a curfew to control the population and prevent protests?"
    menu:
        "Approve":
            vc "You have decided to introduce a curfew to control the population and prevent protests, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 10
            $ national_budget -= 5
            $ curfew = 1
        "Decline":
            vc "You have declined to introduce a curfew to control the population and prevent protests."
            $ popularity += 5
    vc "Do you start a nuclear weapons program to intimidate other countries and increase your power?"
    menu:
        "Approve":
            vc "You have decided to start a nuclear weapons program to intimidate other countries and increase your power, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 30
            $ popularity -= 5
            $ national_budget -= 250
        "Decline":
            vc "You have declined to start a nuclear weapons program to intimidate other countries, this makes you vulnerable to foreign threats but the people like you more."
            $ popularity += 5
    vc "Do you change the national anthem to a more militaristic one to promote nationalism and increase the power of the government?"
    menu:
        "Approve":
            vc "You have decided to change the national anthem to a more militaristic one to promote nationalism and increase the power of the government, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 5
            $ national_budget -= 1
            $ nuclear = 1
        "Decline":
            vc "You have declined to change the national anthem to a more militaristic one to promote nationalism and increase the power of the government."
            $ popularity += 5
    vc "Buy old military equipment from other countries to increase your power, research for new ideas and save money?"
    menu:
        "Approve":
            vc "You have decided to buy old military equipment from other countries to increase your power, research for new ideas and save money, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 15
            $ popularity -= 5
            $ national_budget -= 20
        "Decline":
            vc "You have declined to buy old military equipment from other countries to increase your power, research for new ideas and save money."
            $ popularity += 5
    vc "Do you start a trade deal with China to get access to their cheap labor and increase your power?"
    menu:
        "Approve":
            vc "You have decided to start a trade deal with China to get access to their cheap labor and increase your power, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 2
            $ national_budget += 50
        "Decline":
            vc "You have declined to start a trade deal with China to get access to their cheap labor and increase your power."
            $ popularity += 5
    vc "Do you import cheap labor from China to increase your power and save money?"
    menu:
        "Approve":
            vc "You have decided to import cheap labor from China to increase your power and save money, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 5
            $ national_budget += 25
            $ population += 1000000
            $ taxes += 5
        "Decline":
            vc "You have declined to import cheap labor from China to increase your power and save money."
            $ popularity += 5
    vc "Do you collaborate  with China to make new military technology to increase your power?"
    menu:
        "Approve":
            vc "You have decided to collaborate with China to make new military technology to increase your power, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 30
            $ popularity -= 5
            $ national_budget -= 50
        "Decline":
            vc "You have declined to collaborate with China to make new military technology to increase your power."
            $ popularity += 5
    if nuclear == 1:
        vc "Where do you do your first nuclear test?"
        menu:
            "In the desert":
                vc "You have decided to do your first nuclear test in the desert this increased the popularity of the government but also damaged the environment"
                $ popularity += 5
                $ national_budget -= 10
                $ award_achievement("nuclear_program")
            "In the ocean":
                vc "You have decided to do your first nuclear test in the ocean this caused a radioactive raincloud to travel over your country and damaged the environment, this decreased the popularity of the government(shocking)"  
                $ popularity -= 15
                $ national_budget -= 10
            "on portugees soil":
                vc "You have decided to do your first nuclear test on Portuguese soil, this caused Portugal to attack you and start a war"
                jump milrwar
    vc "Do you want to start equipment production to increase your power and popularity?"
    menu:
        "Approve":
            vc "You have decided to start equipment production to increase your power and popularity, this will increase the power of the government."
            $ power += 20
            $ popularity += 5
            $ national_budget -= 40
        "Decline":
            vc "You have declined to start equipment production to increase your power and popularity."
            $ warwinchance -= 5
    vc "Do you want to increase conscription to increase your power and save money?"
    menu:
        "Approve":
            vc "You have decided to increase conscription to increase your power and save money, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 10
            $ national_budget -= 5
        "Decline":
            vc "You have declined to increase conscription to increase your power and save money."
            $ popularity += 5
    vc "Portugal has declared war on you, do you surrender or fight?"
    menu:
        "Surrender":
            vc "You have decided to surrender to Portugal, this will decrease the popularity of the government but will also save you from a costly war."
            $ popularity -= 20
            $ national_budget += 50
            $ inhabitants -= 500000
            $ welfare -= 5
            jump end
        "Fight":
            vc "You have decided to fight Portugal, this will increase the popularity of the government."
            $ power += 10
            $ popularity -= 10

label milrwar:
    scene bg mil
    show vcmil
    vc "You started a war with Portugal"
    vc "How do you want to fight the war?"
    menu:
        "Use your navy to blockade the ports and cut off their supply lines(this costs 50 billion dollars)":
            vc "You have decided to use your navy to blockade the ports and decrease their supplies,this will decrease the popularity of the government but give you a edge in the war."
            $ warwinchance += 10
            $ popularity -= 5
            $ national_budget -= 50
        "Use your air force to bomb their cities and infrastructure(this costs 70 billion dollars)":
            vc "You have decided to use your air force to bomb their cities and infrastructure, this will decrease the power of the Portuguese government but also decrease the popularity of the government."
            $ warwinchance += 15
            $ popularity -= 10
            $ national_budget -= 70
        "Use your ground forces to invade their territory and capture their capital":
            vc "Choose a strategy for your ground forces to invade their territory and capture their capital"
            $ national_budget += 20
            menu:
                "Use a blitzkrieg strategy to quickly overwhelm their defenses and capture their capital":
                    vc "You have decided to use a blitzkrieg strategy to quickly overwhelm their defenses and capture their capital, this will increase the popularity of the government but also decrease the power of the government."
                    $ warwinchance += 20
                    $ popularity += 5
                    $ power -= 10
                    $ National_budget -= 20
                "Use a siege strategy to slowly wear down their defenses and capture their capital":
                    vc "You have decided to use a siege strategy to slowly wear down their defenses and capture their capital, this will decrease the popularity of the government but also increase the power of the government."
                    $ warwinchance += 15
                    $ popularity -= 5
                    $ power += 10
                    $ National_budget -= 25    
                "Use a guerrilla strategy to harass their forces and capture their capital":
                    vc "You have decided to use a guerrilla strategy to harass their forces and capture their capital, this will decrease the popularity of the government but also increase the power of the government."
                    $ warwinchance += 10
                    $ popularity -= 10
                    $ power += 15
                    $ National_budget -= 30
    $ roll = renpy.random.randint(1, 100)
    if roll <= warwinchance:
        vc "You have won the war against Portugal, this will increase the popularity of the government and give you access to their resources."
        $ popularity += 20
        $ national_budget += 100
        $ inhabitants += 500000
        $ welfare += 5
        $ award_achievement("war_champion")
    else:
        vc "You have lost the war against Portugal, so your reign is over and you got assassinated by the Portuguese, you have lost the game."
        $ popularity -= 20
        $ national_budget -= 100
        $ inhabitants -= 500000
        $ welfare -= 5
        $ ach_secret_death_assassination = True
        jump end
    vc " do you want to annex Portugal or make it a puppet state?"
    menu:
        "Annex portugal":
            vc "You have decided to annex Portugal, this will increase the popularity of the government but will also decrease the national budget."
            $ popularity += 10
            $ national_budget -= 50
        "Make it a puppet state":
            vc "You have decided to make Portugal a puppet state, this will decrease the popularity of the government but will also increase the national budget."
            $ popularity -= 10
            $ national_budget += 50
            vc " do you demand subjugation of Portugal?"
            menu:
                "Approve":
                    vc "You have decided to demand subjugation of Portugal, this will increase the power of the government but will also decrease the popularity of the government."
                    $ power += 20
                    $ popularity -= 10
                    $ national_budget -= 50
                "Decline":
                    vc "You have declined to demand subjugation of Portugal."
                    $ popularity += 5
            vc "Do you demand the rights to Portugal's resources?"
            menu:
                "Approve":
                    vc "You have decided to demand the rights to Portugal's resources, this will increase the power of the government but will also decrease the popularity of the government."
                    $ power += 20
                    $ popularity -= 10
                    $ national_budget += 50
                    $ resource_exploitation = 1
                "Decline":
                    vc "You have declined to demand the rights to Portugal's resources."
                    $ popularity += 5
            vc "Do you want to introduce workcamps in Portugal to increase the power of the government and save money?"
            menu:
                "Approve":
                    vc "You have decided to introduce workcamps in Portugal to increase the power of the government and save money, this will increase the power of the government but will also decrease the popularity of the government."
                    $ power += 20
                    $ popularity -= 20
                    $ national_budget -= 10
                    $ workcamps = 1
                "Decline":
                    vc "You have declined to introduce workcamps in Portugal to increase the power of the government and save money."
                    $ popularity += 5
            vc "Do you want to demand central Portugal to be a military base to increase the power of the government and save money?"
            menu:
                "Approve":
                    vc "You have decided to demand central Portugal to be a military base to increase the power of the government and save money, this will increase the power of the government but will also decrease the popularity of the government."
                    $ power += 20
                    $ popularity -= 10
                    $ national_budget -= 15
                "Decline":
                    vc "You have declined to demand central Portugal to be a military base to increase the power of the government and save money."
                    $ popularity += 5
            vc "Do you demand to annex the entirety of Portugal?"
            menu:
                "Approve":
                    vc "You have decided to annex the entirety of Portugal, this results in you having total control over Portugal but also makes you very unpopular and it also decreases the national budget."
                    vc " however the people don't have enough recourses to rebel against you so you are still in power."
                    $ power += 30
                    $ popularity -= 30
                    $ national_budget -= 100
                "Decline":
                    vc "You have declined to annex the entirety of Portugal."
                    vc "They still have enough recourses to rebel and assassinate you so they tried."
                    vc "The attack was unsuccessful but you got injured and you died a few days later, you have lost the game."
                    $ ach_secret_death_assassination = True
                    jump end
            



    vc " do you want to invest in avionics?"
    menu:
        "Approve":
            vc "You have decided to invest in avionics, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 5
            $ national_budget -= 50
        "Decline":
            vc "You have declined to invest in avionics."
            $ popularity += 5
    vc "Do you want to indoctrinate the children with propaganda to increase the popularity of the government?"
    menu:
        "Approve":
            vc "You have decided to indoctrinate the children with propaganda to increase the popularity of the government, this will increase the popularity of the government but will also increase the power of the government."
            $ popularity += 10
            $ power += 10
            $ national_budget -= 10
        "Decline":
            vc "You have declined to indoctrinate the children with propaganda to increase the popularity of the government."
            $ popularity += 5
    vc "Do you want to exploit the resources of Portugal to increase the national budget and power of the government?"
    menu:
        "Approve":
            vc "You have decided to exploit the resources of Portugal to increase the national budget and power of the government, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ national_budget += 250
            $ popularity -= 10
            $ award_achievement("resource_exploiter")
        "Decline":
            vc "You have declined to exploit the resources of Portugal to increase  the popularity of the government."
            $ popularity += 5
    vc " do you want to crack down on corruption in the government to increase the popularity of the government?"
    menu:
        "Approve":
            vc "You have decided to crack down on corruption in the government to increase the popularity of the government, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 10
            $ power -= 10
            $ national_budget -= 5
            $ corruption -= 10
            $ award_achievement("corruption_crusader")
        "Decline":
            vc "You have declined to crack down on corruption in the government"
            $ popularity -= 5
    vc "Do you establish a corridor to France?"
    menu:
        "Approve":
            vc "You have decided to establish a corridor to France, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 5
            $ power -= 5
            $ national_budget -= 10
        "Decline":
            vc "You have declined to establish a corridor to France."
            vc "You are happy with what land you got and became peaceful"
            vc "After a few years of peace, you died of old age, after you died the country started to demilitarize, you have won the game."
            jump end
    vc "What do you want to do?"
    menu:
        "demand the subjugation of spain":
            $ roll = renpy.random.randint(1, 100)
            if roll <= 80:
                vc "They said yes and they are now your puppet state, this will increase the power of the government but will also decrease the popularity of the government."
                $ power += 20
                $ popularity -= 10
                $ national_budget -= 50
                vc "You are happy with what land you got and became peaceful"
                vc "After a few years of peace, you died of old age, after you died the country started to demilitarize, you have won the game."
                jump end
            else:
                vc "They said no and they declared war on you, this will decrease the popularity of the government but will also increase the power of the government."
                $ popularity -= 20
                $ power += 10
                vc "You have won the war against spain, this will increase the popularity of the government and give you access to their resources."
                $ popularity += 20
                $ national_budget += 100
                $ inhabitants += 500000
                $ welfare += 5
                vc "You got the entirety of spain as annexed territory, this will increase the power of the government but will also decrease the popularity of the government."
                $ power += 30
                $ popularity -= 30
        "go to war with spain":
            vc "They said no and they declared war on you, this will decrease the popularity of the government but will also increase the power of the government."
            $ popularity -= 20
            $ power += 10
            vc "You have won the war against spain, this will increase the popularity of the government and give you access to their resources."
            $ popularity += 20
            $ national_budget += 100
            $ inhabitants += 500000
            $ welfare += 5
            vc "You got the entirety of spain as annexed territory, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 30
            $ popularity -= 30
    vc "Do you want to extract resources from spain to increase the national budget and power of the government?"
    menu:
        "Approve":
            vc "You have decided to extract resources from Spain to increase the national budget and power of the government, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ national_budget += 250
            $ popularity -= 10
        "Decline":
            vc "You have declined to extract resources from Spain to increase  the popularity of the government."
            $ popularity += 5
    vc "Do you want to study the chinese air force to improve your own air force and increase the power of the government?"
    menu:
        "Approve":
            vc "You have decided to study the chinese air force to improve your own air force and increase the power of the government, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 5
            $ national_budget -= 50
        "Decline":
            vc "You have declined to study the chinese air force to improve your own air force and increase the power of the government."
            $ popularity += 5
    vc "Do you want to establish a modern air force to increase the power of the government?"
    menu:
        "Approve":
            vc "You have decided to establish a modern air force to increase the power of the government, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 30
            $ popularity -= 10
            $ national_budget -= 100
        "Decline":
            vc "You have declined to establish a modern air force to increase the power of the government."
            $ popularity += 5
    vc " do you want to increase conscription to a mandatory military service to increase your power and save money?"
    menu:
        "Approve":
            vc "You have decided to increase conscription to a mandatory military service to increase your power and save money, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 30
            $ popularity -= 20
            $ national_budget -= 5
        "Decline":
            vc "You have declined to increase conscription to a mandatory military service to increase your power and save money."
            $ popularity += 5
    vc "Do you want to establish a spy agency?"
    menu:
        "Approve":
            vc "You have decided to establish a spy agency, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 10
            $ national_budget -= 50
        "Decline":
            vc "You have declined to establish a spy agency."
            $ popularity += 5
    vc "Do you want to purge corrupt generals to increase the power of the government and decrease corruption?"
    menu:
        "Approve":
            vc "You have decided to purge corrupt generals to increase the power of the government and decrease corruption, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 10
            $ national_budget -= 5
            $ corruption -= 10
            $ award_achievement("corruption_crusader")
        "Decline":
            vc "You have declined to purge corrupt generals to increase the power of the government and decrease corruption."
            $ popularity += 5
            $ corruption += 5
    vc "How would you like to do operation Ricardo(France)?"
    menu:
        "Use your airforce to bomb their cities and infrastructure(this costs 70 billion dollars)":
            vc "You have decided to use your air force to bomb their cities and infrastructure, this will decrease the power of the french government but also decrease the popularity of the government."
            $ warwinchance += 15
            $ popularity -= 10
            $ national_budget -= 70
        "Use your ground forces to invade their territory and capture their capital":
            vc "Choose a strategy for your ground forces to invade their territory and capture their capital"
            $ national_budget += 20
            menu:
                "Use a blitzkrieg strategy to quickly overwhelm their defenses and capture their capital":
                    vc "You have decided to use a blitzkrieg strategy to quickly overwhelm their defenses and capture their capital, this will increase the popularity of the government but also decrease the power of the government."
                    $ warwinchance += 20
                    $ popularity += 5
                    $ power -= 10
                    $ National_budget -= 20
                "Use a siege strategy to slowly wear down their defenses and capture their capital":
                    vc "You have decided to use a siege strategy to slowly wear down their defenses and capture their capital, this will decrease the popularity of the government but also increase the power of the government."
                    $ warwinchance += 15
                    $ popularity -= 5
                    $ power += 10
                    $ National_budget -= 25    
                "Use a guerrilla strategy to harass their forces and capture their capital":
                    vc "You have decided to use a guerrilla strategy to harass their forces and capture their capital, this will decrease the popularity of the government but also increase the power of the government."
                    $ warwinchance += 10
                    $ popularity -= 10
                    $ power += 15
                    $ National_budget -= 30
    
    $ roll = renpy.random.randint(1, 100)
    if roll <= warwinchance:
        vc "You have won the war against France, this will increase the popularity of the government and give you access to their resources."
        $ popularity += 20
        $ national_budget += 100
        $ inhabitants += 500000
        $ welfare += 5
    else:
        vc "You have lost the war against France, so your reign is over and you got assassinated by the french, you have lost the game."
        $ popularity -= 20
        $ national_budget -= 100
        $ inhabitants -= 500000
        $ welfare -= 5
        $ ach_secret_death_assassination = True
        jump end
    vc "What will you do with France?"
    menu:
        "Annex france":
            vc "You have decided to annex France, this will increase the popularity of the government but will also decrease the national budget."
            $ popularity += 10
            $ national_budget -= 50
            $ inhabitants += 5000000
            $ taxes += 25
        "Make it a puppet state":
            vc "You have decided to make France a puppet state, this will decrease the popularity of the government but will also increase the national budget."    
            $ popularity -= 10
            $ national_budget += 50
            $ taxes += 20
        "take the south of france as annexed territory and make the north a puppet state":
            vc "You have decided to take the south of France as annexed territory and make the north a puppet state, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 20
            $ national_budget -= 25
            $ inhabitants += 2500000
            $ taxes += 15
    vc "Do you want to introduce a new flag to promote nationalism and increase the power of the government?"
    menu:
        "Approve":
            vc "You have decided to introduce a new flag to promote nationalism and increase the power of the government, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 5
            $ national_budget -= 1
        "Decline":
            vc "You have declined to introduce a new flag to promote nationalism and increase the power of the government."
            $ popularity += 5
    vc "Do you want to take Andorra as a puppet state to increase the power of the government and save money?"
    menu:
        "Approve":
            vc "You have decided to take Andorra as a puppet state to increase the power of the government and save money, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 5
            $ national_budget += 10
            $ taxes += 5
        "Decline":
            vc "You have declined to take Andorra as a puppet state to increase the power of the government and save money."
            $ popularity += 5
    vc "Do you want to take Gibraltar as a puppet state to increase the power of the government and save money?"
    menu:
        "Approve":
            vc "You have decided to take Gibraltar as a puppet state to increase the power of the government and save money, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 5
            $ national_budget += 10
            $ taxes += 5
        "Decline":
            vc "You have declined to take Gibraltar as a puppet state to increase the power of the government and save money."
            $ popularity += 5
    vc "Are you satisfied with your conquest?"
    menu:
        "Yes":
            vc "You are satisfied with your conquest and you decide to focus on internal affairs"
            jump milrsat
        "No":
            vc "You are not satisfied with your conquest and you decide to continue expanding your territory"
    vc "Do you want to take the strait of Gibraltar to increase the power of the government and put pressure on the mediterranean?"
    menu:
        "Approve":
            vc "You have decided to take the strait of Gibraltar to increase the power of the government and put pressure on the mediterranean, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 10
            $ national_budget -= 50
        "Decline":
            vc "You have declined to take the strait of Gibraltar to increase the power of the government and put pressure on the mediterranean."
            $ popularity += 5
            vc "Sir, it looks like you have done everything you want i suggest you focus on internal affairs now"
            menu:
                "listen to the advisor and focus on internal affairs":
                    vc "You have decided to listen to the advisor and focus on internal affairs."
                    jump milrsat
                "ignore the advisor and continue expanding your territory":
                    vc "Then we will take the strait of Gibraltar to increase the power of the government and put pressure on the mediterranean"
                    $ power += 20
                    $ popularity -= 10
                    $ national_budget -= 50
    vc "What do you want to do now?"
    menu:
        "take morocco as a puppet state to increase the power of the government and gain money":
            vc "You have decided to take Morocco as a puppet state to increase the power of the government and gain money, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 10
            $ national_budget += 50
            $ taxes += 10
        "demand the subjugation of morocco to increase the power of the government and gain money":
            vc "You have decided to demand the subjugation of Morocco to increase the power of the government and gain money, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 10
            $ national_budget += 50
            $ taxes += 10
        "demand the annexation of morocco to increase the power of the government and gain money":
            vc "You have decided to demand the annexation of Morocco to increase the power of the government and gain money, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 30
            $ popularity -= 20
            $ national_budget += 100
            $ taxes += 20
    vc "Do you want to try and seize Monaco to increase the power of the government and gain money?"
    menu:
        "Approve":
            vc "You have decided to try and seize Monaco to increase the power of the government and gain money, this will increase the power of the government but will also decrease the popularity of the government."
            vc "You have successfully seized Monaco, however the rich people living there worked together to assassinate you"
            vc "But you survived the asSASsination attempt"
            vc "Sadly only days later you got hit by a drunk driver and died, you have lost the game."
            $ ach_secret_death_accident = True
            jump end
        "Decline":
            vc "You have declined to try and seize Monaco to increase the power of the government and gain money."
            vc "They thank you by inviting you to a fancy dinner and they try to assassinate you there but you survive the asSASsination attempt and flee the country to avoid another asSASsination attempt."
            vc "After a few years of hiding, you died of old age, you have won the game."
            $ ach_secret_death_natural = True
            jump end

    

label milrsat:
    scene bg mil
    show vcmil
    vc "Do you try to stabilize the country by cracking down on crime and corruption?"
    menu:
        "Approve":
            vc "You have decided to try to stabilize the country by cracking down on crime and corruption, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 15
            $ power -= 10
            $ national_budget -= 5
            $ corruption -= 15
        "Decline": 
            vc "You have declined to try to stabilize the country by cracking down on crime and corruption."
            $ popularity -= 5
            $ corruption += 5
    vc "Do you decrease conscription to increase the popularity of the government and save money?"
    menu:
        "Approve":
            vc "You have decided to decrease conscription to increase the popularity of the government and save money, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 10
            $ power -= 20
            $ national_budget += 5
        "Decline": 
            vc "You have declined to decrease conscription to increase the popularity of the government and save money."
            $ popularity -= 5
    if workcamps == 1:
        vc "Do you want to destroy the workcamps in Portugal to increase the popularity of the government and decrease the power of the government?"
        menu:
            "Approve":
                vc "You have decided to destroy the workcamps in Portugal to increase the popularity of the government and decrease the power of the government, this will increase the popularity of the government but will also decrease the power of the government."
                $ popularity += 20
                $ power -= 20
                $ national_budget += 10
            "Decline":
                vc "You have declined to destroy the workcamps in Portugal to increase the popularity of the government and decrease the power of the government."
                $ popularity -= 5
    if curfews == 1:
        vc "Do you want to lift the curfews in Portugal to increase the popularity of the government and decrease the power of the government?"
        menu:
            "Approve":
                vc "You have decided to lift the curfews in Portugal to increase the popularity of the government and decrease the power of the government, this will increase the popularity of the government but will also decrease the power of the government."
                $ popularity += 20
                $ power -= 20
                $ national_budget += 10
            "Decline":
                vc "You have declined to lift the curfews in Portugal to increase the popularity of the government and decrease the power of the government."
                $ popularity -= 5
    if resource_exploitation == 1:
        vc "Do you want to stop exploiting the resources of Portugal to increase the popularity of the government and decrease the power of the government?"
        menu:
            "Approve":
                vc "You have decided to stop exploiting the resources of Portugal to increase the popularity of the government and decrease the power of the government, this will increase the popularity of the government but will also decrease the power of the government."
                $ popularity += 20
                $ power -= 20
                $ national_budget -= 50
            "Decline":
                vc "You have declined to stop exploiting the resources of Portugal to increase the popularity of the government and decrease the power of the government."
                $ popularity -= 5
    vc "Do you want to re-introduce municipalities to increase the popularity of the government and decrease the power of the government?"
    menu:
        "Approve":
            vc "You have decided to re-introduce municipalities to increase the popularity of the government and decrease the power of the government, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 20
            $ power -= 20
            $ national_budget -= 10
            $ award_achievement("municipal_reformer")
        "Decline":
            vc "You have declined to re-introduce municipalities to increase the popularity of the government and decrease the power of the government."
            $ popularity -= 5
    vc "Do you want to remove weapons from the streets to increase the popularity of the government and decrease the power of the government?"
    menu:
        "Approve":
            vc "You have decided to remove weapons from the streets to increase the popularity of the government and decrease the power of the government, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 20
            $ power -= 20
            $ national_budget -= 10
        "Decline":
            vc "You have declined to remove weapons from the streets to increase the popularity of the government and decrease the power of the government."
            $ popularity -= 5
    vc "Do you want to abolish all forms of corruption to increase the popularity of the government and decrease the power of the government?"
    menu:
        "Approve":
            vc "You have decided to abolish all forms of corruption to increase the popularity of the government and decrease the power of the government, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 20
            $ power -= 20
            $ national_budget -= 30
            $ taxes -= 10
            $ corruption = 0
        "Decline":
            vc "You have declined to abolish all forms of corruption to increase the popularity of the government and decrease the power of the government."
            $ popularity -= 5
            $ corruption += 5
    vc "Do you want to spread your funding out more to increase the popularity of the government"
    menu:
        "Approve":
            vc "You have decided to spread your funding out more to increase the popularity of the government and decrease the power of the government, this will increase the popularity of the government but will also decrease the power of the government."
            $ popularity += 20
            $ power += 15
            $ national_budget -= 50
        "Decline":
            vc "You have declined to spread your funding out more to increase the popularity of the government and decrease the power of the government."
            $ popularity -= 5
    vc "Do you want to build nuclear reactors to have a cleaner energy source and increase the power of the government?"
    menu:
        "Approve":
            vc "You have decided to build nuclear reactors to have a cleaner energy source and increase the power of the government, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 20
            $ popularity -= 1
            $ national_budget -= 140
        "Decline":
            vc "You have declined to build nuclear reactors to have a cleaner energy source and increase the power of the government."
            $ popularity += 5
    vc "Will you re-instate elections to increase the popularity of the government?"
    menu:
        "Approve":
            vc "You have decided to re-instate elections to increase the popularity of the government, this will increase the popularity of the government."
            $ popularity += 20
            $ national_budget -= 10
            $ award_achievement("peacekeeper")
        "Decline":
            vc "You have declined to re-instate elections to increase the popularity of the government."
            $ popularity -= 5
            vc "You stabilized the country and made the people happy, however you kept ruling with an iron fist"
            vc "After a few years of peace, you died of old age, you have won the game."
            $ ach_secret_death_natural = True
            jump end
    scene bg dem
    show vccap
    vc "Will you re-instate the parliament to increase the popularity of the government?"
    menu:
        "Approve":
            vc "You have decided to re-instate the parliament to increase the popularity of the government, this will increase the popularity of the government."
            $ popularity += 20
            $ national_budget -= 10
        "Decline":
            vc "You have declined to re-instate the parliament to increase the popularity of the government."
            $ popularity -= 5
    na "After taking rule of the country during uncertain times you expanded your territory and stabilized the country"
    na "After that you re-instated elections and became a national hero who will be remembered for generations to come"
    na "You died of old age, you have won the game."
    $ ach_secret_death_natural = True
    jump end


label arch:
    scene bg arc
    show vcarc
    $ ideology = "Anarchist"
    vc "You are now an Anarchist, you have given all the power to the people and you have no more power, you can only watch as the country develops without you, good luck."

    n "Get rid of the political parties."
    menu:
        "Approve":
            n "You got rid of political parties."
        "Approve":
            n "You got rid of political parties."
    
    n "Strip the royal family of their power."
    menu:
        "Approve":
            n "You strip the royal family of their power."
        "Approve":
            n "You strip the royal family of their power."
    n "Discontinue the state military."
    menu:
        "Approve":
            n "You discontinue the state military."
        "Approve":
            n "You discontinue the state military."

    n "Remove the state owned emergency responders."
    menu:
        "Approve":
            n "You remove the state owned emergency responders."
        "Approve":
            n "You remove the state owned emergency responders."
    
    n "Disband any and all government bodies."
    menu:
        "Approve":
            n "You disband any and all government bodies."
        "Approve":
            n "You disband any and all government bodies."
    hide vcarc

    n "You achieved total Anarchy, the people are now in control of the country and you have no more power, good luck."
    $ award_achievement("anarchist_vision")

    n "A couple days later, while you are walking home, you get hit by a car and die."
    $ ach_secret_death_accident = True
    $ maybe_award_secret_death()

    na "The end."
    jump end

label soc:
    scene bg dem
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
    scene bg soc
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
    scene bg soc
    show vcsoc
    vc "You have made the people happy,but your economic growth has flatlined."
    jump end

label socgood:
    scene bg soc
    show vcsoc 
    vc "The democrats and the socialist are both happy with your decisions and they have decided to work together to make the country better, this has increased the popularity of the government and the welfare of the country."
    $ popularity += 10
    $ welfare += 10
    vc "You have made the people happy and your economic growth is booming."
    jump end

label mon:
    scene bg mon
    hide vccap
    $ ideology = "Monarchy"
    show vcmon
    vc "Would you like to build a palace for yourself?"
    menu:
        "Approve":
            vc "The people like your palace but a few people lost their lives due to poor working conditions."
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
            vc "Nothing happens because nothing changes"
    
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
    scene bg mon
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
        scene bg mon
        show vcmon
        vc "The people liked your decision to not force religion on them and they have accepted you as their king."
        $ award_achievement("merciful_king")
        $ ach_secret_death_natural = True
        $ maybe_award_secret_death()
        vc "You have become a beloved king and you died surrounded by your family and friends."
        jump end
label fas:
    scene bg fas
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
    scene bg fas
    show vcfas
    n " you have been asSASSASSASsinated by a different power in the government, you have lost the game"
    $ ach_secret_death_assassination = True
    $ maybe_award_secret_death()
    jump end

label fasc2:
    scene bg fas
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
                n "The opposition has been able to fight back and you have been asSASSASSASsinated, you have lost the game"
                $ ach_secret_death_assassination = True
                $ maybe_award_secret_death()
                jump end
            elif roll == 2:
                vc "People have found out about the extermination"
                $ popularity -= 30
                $ power += 15
                jump fasc3
            else: 
                vc "You have asSASSASSASsinated the opposition in their sleep by slicing their throats."
                $ power += 20
                jump fasc3

        
        "Decline":
            vc "You have declined to exterminate the opposition."
            n "Your political opponents didn't like you and they have been able to assassinate you, you have lost the game"
            $ ach_secret_death_assassination = True
            $ maybe_award_secret_death()
            jump end
label fasc3:
    scene bg fas
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
            n "The media has been able to criticize you and you have been asSASSASSASsinated, you have lost the game"
            $ ach_secret_death_assassination = True
            $ maybe_award_secret_death()
            jump end

    label fasc4:
        scene bg fas
        show vcfas

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
        scene bg fas
        show vcfas

        vc "You have decided to let the population work more, this will increase the national budget but will also decrease the popularity of the government."

        $ national_budget += 50000000000

        $ popularity -= 10

        jump fasc_end




    label fasc_infa:
        scene bg fas
        show vcfas
        vc "You have decided to build infrastructure, this will increase the welfare of the country but will also decrease the national budget."

        $ welfare += 10

        $ national_budget -= 50000000000

        jump fasc_end



    label fasc_pop:
        scene bg fas
        show vcfas

        vc "Would you like to force population growth?"

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
        scene bg fas
        show vcfas
        if popularity >= 50:

            $ roll = renpy.random.randint(1, 10)

            if roll <= 4:

                n "You have gained full control of your country and you have been able to win the game"

                jump end

            else:

                n "The population has revolted against you and you have been asSASSASSASsinated, you have lost the game"

                jump end



        else:

            $ roll = renpy.random.randint(1, 10)

            if roll <= 1:

                n "You have gained full control of your country and you have been able to win the game"

                jump end

            else:

                n "The population has revolted against you and you have been asSASSASSASsinated, you have lost the game"

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
    scene bg dem
    vc "Do you want to give money to Israel?"
    menu:
        "Approve":
            vc "You have decided to give money to Israel."
            $ national_budget -= 50
            $ corruption += 20
            jump begin
        "Decline":
            vc "You have been assassinated by the Mossad, you have lost the game."
            $ ach_secret_death_assassination = True
            $ maybe_award_secret_death()
            jump end

label col:
    $ ideology = "Colonialism"
    scene bg col
    show vccol
    vc "Would you like to invest in your navy?"
    menu:
        "Approve":
            vc "You have decided to invest in your navy, this will increase the power of the government but will also increase the popularity of the government."
            $ power += 5
            $ popularity += 5
            $ national_budget -= 50
            $ navy == 1
        "Decline":
            vc "You have declined to invest in your navy."
    
    vc "Would you like start a aliance with Britain to recliam your colonial might"
    menu:
        "Approve":
            vc "You have decided to start a aliance with Britain to reclaim your colonial might."
            $ power += 10
            $ popularity -= 10
            $ national_budget -= 100
        "Decline":
            vc "You have declined to start a aliance with Britain to reclaim your colonial might."

    vc "Would you like to invest in British exports?"
    menu:
        "Approve":
            vc "You have decided to invest in British exports."
            $ national_budget += 100
        "Decline":
            vc "You have declined to invest in British exports."
    
    vc "Would you like to promote colonialism in your country?"
    menu:
        "Approve":
            vc "You have decided to promote colonialism in your country, this will increase the popularity of the government but will also decrease the welfare of the country."
            $ popularity += 10
            $ welfare -= 5
        "Decline":
            vc "You have declined to promote colonialism in your country."

    vc "Focus on colonialism during history class?"
    menu:
        "Approve":
            vc "You have decided to focus on colonialism during history class, this will increase the popularity of the government but will also decrease the education of the country."
            $ popularity += 5
            $ education -= 5
        "Decline":
            vc "You have declined to focus on colonialism during history class."
    
    vc "Would you like to justify your colonial ambitions with the history of the Iberian peninsula?"
    menu:
        "Approve":
            vc "You have decided to justify your colonial ambitions with the history of the Iberian peninsula, this will increase the popularity of the government but will also decrease the education of the country."
            $ popularity += 5
            $ education -= 5
        "Decline":
            vc "You have declined to justify your colonial ambitions with the history of the Iberian peninsula."
        
    vc "Would you like to build more dockyards to increase your naval power?"
    menu:
        "Approve":
            vc "You have decided to build more dockyards to increase your naval power, this will increase the power of the government but will also decrease the national budget."
            $ power += 5
            $ national_budget -= 50
            $ dock = 1
        "Decline":
            vc "You have declined to build more dockyards to increase your naval power."
    
    vc "Would you like to train new generals to increase your military power?"
    menu:
        "Approve":
            vc "You have decided to train new generals to increase your military power, this will increase the power of the government but will also decrease the national budget."
            $ power += 5
            $ national_budget -= 50
            $ generals = 1
        "Decline":
            vc "You have declined to train new generals to increase your military power."
    
    vc "How would you want to reclaim cuba?"
    menu:
        "Diplomacy":
            vc "You have decided to reclaim cuba through diplomacy, this will increase the popularity of the government."
            $ popularity += 5
            $ power -= 5
            $ roll = renpy.random.randint(1, 10) 
            if roll >= 3:
                vc "Your diplomatic efforts have been successful and you have been able to reclaim cuba without any conflict."
                $ popularity += 5
                $ national_budget += 50
                $ inhabitants += 11326616
                $ welfare += 5
                $ award_achievement("diplomatic_victory")
            else:
                vc "Your diplomatic efforts have failed and you have been humiliated on the international stage"
                $ popularity -= 5
                $ power -= 5
                jump col_cuba
        "Military":
            vc "You have decided to reclaim cuba through military"
            jump col_cuba

label col_cuba:
    scene bg col
    show vccol
    vc "You have decided to reclaim cuba through military, in what way would you like to invade them?"
    menu:
        "Naval invasion":
            vc "You have decided to reclaim cuba through a naval invasion, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 1
            if navy == 1 or dock == 1:
                vc "Your naval invasion was successful and you have been able to reclaim cuba without any conflict."
                $ popularity += 5
                $ national_budget += 50
                $ inhabitants += 11326616
                $ welfare += 5
                jump col_sla
                
            else:
                vc "Your naval invasion was unsuccessful and you have been humiliated on the international stage"
                $ popularity -= 5
                $ power -= 5
                jump col_cuba2
        "Ground invasion":
            vc "You have decided to reclaim cuba through a ground invasion, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 1
            if generals == 1:
                vc "Your ground invasion was successful and you have been able to reclaim cuba without any conflict."
                $ popularity += 5
                $ national_budget += 50
                $ inhabitants += 11326616
                $ welfare += 5
                jump col_sla
                
            else:
                vc "Your ground invasion was unsuccessful and you have been humiliated on the international stage"
                $ popularity -= 5
                $ power -= 5
                jump col_cuba2
    label col_cuba2:
        scene bg col
        show vccol
        vc "You first invasion has failed but there is always a second chance, how would you like to invade them?"
        menu:
            "Naval invasion":
                vc "You have decided to reclaim cuba through a naval invasion, this will increase the power of the government but will also decrease the popularity of the government."
                $ power += 10
                $ popularity -= 1
                vc "Your naval invasion was successful, but you had heavy casualties and you have been humiliated on the international stage"
                $ popularity -= 5
                $ power -= 5
                $ national_budget += 10
                $ inhabitants += 9151515
                $ welfare += 2
                jump col_sla
                            
            "Ground invasion":
                vc "You have decided to reclaim cuba through a ground invasion, this will increase the power of the government but will also decrease the popularity of the government."
                $ power += 10
                $ popularity -= 1
                vc "Your ground invasion was successful, but you had heavy casualties and you have been humiliated on the international stage"
                $ popularity -= 5
                $ power -= 5
                $ national_budget += 10
                $ inhabitants += 9151515
                $ welfare += 2
                jump col_sla

    


    label col_sla:
        scene bg col
        show vccol
        vc "You have successfully reclaimed cuba, the people are happy and you have increased your power on the international stage, good job."
        $ award_achievement("reclaim_cuba")
        vc "Would you like to re-introduce slavery?"
        menu:
            "Approve":
                vc "You have decided to re-introduce slavery, this will increase the national budget but will also decrease the popularity of the government."
                $ national_budget += 300
                $ popularity -= 20 
                $ welfare += 5
            "Decline":
                vc "You have declined to re-introduce slavery."

        vc "Would you like to exploit your colonies for resources?"
        menu:
            "Approve":
                vc "You have decided to exploit your colonies for resources, this will increase the national budget but will also decrease the popularity of the government."
                $ national_budget += 200
                $ popularity -= 10
                $ welfare += 5
            "Decline":
                vc "You have declined to exploit your colonies for resources."
        jump col_dec

    label col_dec:
        scene bg col
        show vccol
        vc "Where would you like to re-take your past colonies?"
        menu:
            "Africa:":
                jump col_africa
            "Asia":
                jump col_asia
            "Americas":
                jump col_americas

label col_africa:
    scene bg col
    show vccol
    vc "You have chosen to re-take your colonies in Africa."
    if africa == 0:
        vc "Would you like to reclaim Nambia?"
        menu:
            "Approve":
                vc "You won the war against Nambia and you succesfully reclaimed it."
                $ popularity += 5
                $ national_budget -= 10
                $ inhabitants += 32866272
                $ welfare += 5
    
        vc "Would you like to take over South Africa"
        menu:
            "Approve":
                vc "You invaded South Africa and took al of their land."
                $ popularity += 5
                $ national_budget -= 20
                $ inhabitants += 59308690
                $ welfare += 5
            "Declined":
                vc "You declined to invade South Africa"
        vc "Would you like to invade angola?"
        menu:
            "Approve":
                vc "You invaded Angola and took al of their land."
                $ popularity += 5
                $ national_budget -= 20
                $ inhabitants += 32866272
                $ welfare += 5
            "Declined":
                vc "You declined to invade Angola"
        vc "Would you like to invade botswana?"
        menu:
            "Approve":
                vc "You invaded Botswana and took al of their land."
                $ popularity += 5
                $ national_budget -= 20
                $ inhabitants += 32866272
                $ welfare += 5
            "Declined":
                vc "You declined to invade Botswana"
        vc "Would you like to take back zimbabwe?"
        menu:
            "Approve":
                vc "You reclaimed Zimbabwe."
                $ popularity += 5
                $ national_budget -= 20
                $ inhabitants += 32866272
                $ welfare += 5
            "Declined":
                vc "You declined to reclaim Zimbabwe."
        vc "Would you like to stomp on Lesotho and Eswatini?"
        menu:
            "Approve":
                vc "You stomped on Lesotho and Eswatini."
                $ popularity += 5
                $ national_budget -= 20
                $ inhabitants += 32866272
                $ welfare += 5
            "Declined":
                vc "You declined to stomp on Lesotho and Eswatini."
        vc "Would you like to exploit their resources?"
        menu:
            "Approve":
                vc "You have decided to exploit your colonies for resources, this will increase the national budget but will also decrease the popularity of the government."
                $ national_budget += 200
                $ popularity -= 10
                $ welfare += 5
            "Decline":
                vc "You have declined to exploit your colonies for resources."
        vc "Would you like to take over Mozambique?"
        menu:
            "Approve":
                vc "You have decided to take over Mozambique."
                $ popularity += 5
                $ national_budget -= 20
                $ inhabitants += 32866272
                $ welfare += 5
            "Decline":
                vc "You have declined to take over Mozambique."

        vc "Would you like to take over Zimbabwe?"
        menu:
            "Approve":
                vc "You have decided to take over Zimbabwe."
                $ popularity += 5
                $ national_budget -= 20
                $ inhabitants += 32866272
                $ welfare += 5
            "Decline":
                vc "You have declined to take over Zimbabwe."

        vc "Would you like to build workcamps in your colonies in Africa?"
        menu:
            "Approve":
                vc "You have decided to build workcamps in your colonies in Africa."
                $ national_budget -= 20
                $ welfare += 5
            "Decline":
                vc "You have declined to build workcamps in your colonies in Africa."
        
        vc "Would you like to form the Listunburgian South African colony?"
        menu:
            "Approve":
                vc "You have decided to form the Listunburgian South African colony, this will increase the popularity of the government but will also decrease the national budget."
                $ popularity += 10
                $ national_budget -= 50
                $ inhabitants += 59308690
                $ welfare += 5
                $ africa = 1
            "Decline":
                vc "You have declined to form the Listunburgian South African colony."
                $ africa = 1
                jump africa_win

    if africa == 1:
        label africa_win:
            scene bg col
            show vccol
            vc "You reclaimed your african colonies, would you like reclaim other colonies or did you fullfill your colonial ambitions already?"
            menu:
                "Reclaim other colonies":
                    vc "You have chosen to reclaim other colonies."
                    jump col_dec
                "Fullfilled colonial ambitions":
                    vc "You have fullfilled your colonial ambitions."
                    jump col_end

label col_asia:
    scene bg col
    show vccol
    if asia == 0:
        vc "You have chosen to re-take your colonies in Asia."
        vc "Would you like to reclaim Timor"
        menu:
            "Approve":
                vc "You won the war against the island of Timor and you succesfully reclaimed it."
                $ popularity += 5
                $ national_budget -= 10
                $ inhabitants += 1318442
                $ welfare += 5

            "Decline":
                vc "You have declined to reclaim Timor."
        
        if uk == 1:
            vc "Would you like to reclaim Hong Kong for the Uk and Macau for yourself?"
            menu:
                "Approve":
                    vc "The chinese goverment has accepted your demands and they have ceded Hong Kong to the Uk and Macau to you, this will increase the popularity of the government but will also decrease the national budget."
                    $ popularity += 10
                    $ national_budget -= 100
                    $ inhabitants += 6961000
                    $ welfare += 5
                "Decline":
                    vc "You have declined to reclaim Hong Kong for the Uk and Macau for yourself."
        
        vc "Would you like to reclaim the Philippines?"
        menu:
            "Approve":
                vc "You won the war against the Philippines and you succesfully reclaimed it."
                $ popularity += 5
                $ national_budget -= 10
                $ inhabitants += 11377239
                $ welfare += 5
            "Decline":
                vc "You have declined to reclaim the Philippines."
        
        vc "Would you like to to install puppet goverments in your former colonies in Asia?"
        menu:
            "Approve":
                vc "You have decided to install puppet goverments in your former colonies in Asia, this will increase the national budget."
                $ national_budget += 100
                $ popularity += 10
                $ welfare += 10
            "Decline":
                vc "You have declined to install puppet goverments in your former colonies in Asia."

        vc "Would you like to demand India subjugation for your ally?"
        menu:
            "Approve":
                vc "You have decided to demand Indian subjugation."
                $ roll = renpy.random.randint(1, 100)
                    
                if roll <= 50:
                    vc "The Indian goverment has submitted to yor demands and the UK has given Sri Lanka for your troubles."
                    $ welfare += 5
                    $ population += 145115                        
                    $ national_budget += 10
                    $ asia = 1
                    jump asia_win
                else:
                    vc "After a costly war against, you came out on top and for your contributions during the war, the UK gave you Sri Lanka."
                    $ welfare += 5
                    $ national_budget -= 20
                    $ population -= 141415
                    $ asia = 1
                    jump asia_win
            "Decline":
                vc "You have declined to demand Indian subjugation."
                $ asia = 1
                jump asia_win
                      
    if asia == 1:
        jump asia_win

        label asia_win:
            scene bg col
            show vccol
            vc "You reclaimed your asian colonies, would you like reclaim other colonies or did you fullfill your colonial ambitions already?"
            menu:
                "Reclaim other colonies":
                    vc "You have chosen to reclaim other colonies."
                    jump col_dec
                "Fullfilled colonial ambitions":
                    vc "You have fullfilled your colonial ambitions." 
                    jump col_end

               
label col_americas:
    scene bg col
    show vccol
    if americas == 0:
        vc "You have chosen to re-take your colonies in the Americas."
    
    vc "Would you like to set up a sphere of influence in the Caribbean?"
    menu:
        "Approve":
            vc "You have decided to set up a sphere of influence in the Caribbean, this will increase the national budget but will also decrease the popularity of the government."
            $ national_budget += 100
            $ popularity -= 10
            $ welfare += 5
        "Decline":
            vc "You have declined to set up a sphere of influence in the Caribbean."
    vc "Would you like to split up central America with the Mexicans?"
    menu:
        "Approve":
            vc "You have decided to split up central America with the Mexicans, this will increase the popularity of the government but will also decrease the national budget."
            $ popularity += 10
            $ national_budget -= 50
            $ inhabitants += 5000000
            $ welfare += 5
        "Decline":
            vc "You have declined to split up central America with the Mexicans."
    vc "Would you like to back-stab the Mexicans and take all of central America for yourself?"
    menu:
        "Approve":
            vc "You have decided to back-stab the Mexicans and take all of central America for yourself, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 20
            $ national_budget -= 100
            $ inhabitants += 5000000
            $ welfare += 5
        "Decline":
            vc "You have declined to back-stab the Mexicans and take all of central America for yourself."
    vc "Would you like to invade Norther South America?"
    menu:
        "Approve":
            vc "You have decided to invade Northern South America, this will increase the power of the government but will also decrease the popularity of the government."
            $ power += 10
            $ popularity -= 20
            $ national_budget -= 100
            $ inhabitants += 5000000
            $ welfare += 5
        "Decline":
            vc "You have declined to invade Northern South America."
    
    vc "Would you like to invite the rest of hispanic nations into an aliance?"
    menu:
        "Approve":
            vc "You have decided to invite the rest of hispanic nations into an aliance, this will increase the popularity of the government but will also decrease the national budget."
            $ popularity += 10
            $ national_budget -= 50
            $ inhabitants += 5000000
            $ welfare += 5
            $ alliances = 1
        "Decline":
            vc "You have declined to invite the rest of hispanic nations into an aliance."
    vc "Would you like to invade the Brazilians?"
    menu:
        "Approve":
            if alliances == 1:
                vc "You invaded the Brazilians and with the help of your allies you were able to split the land amongst each other."
                $ popularity += 10
                $ national_budget -= 50
                $ inhabitants += 5000000
                $ welfare += 5
            else:
                vc "You invaded the Brazilians but they were too strong and they were able to repel your invasion, you have been humiliated on the international stage."
                $ popularity -= 10
                $ power -= 10
                vc "After a bit your vice-president has staged a coup and taken over the country, because of your incompetence to beat a colony."
                jump end
        "Decline":
            vc "You have declined to invade the Brazilians."
        
    vc "Would you like to puppet your aliances in the Americas?"
    menu:
        "Approve":
            vc "You have decided to puppet your aliances in the Americas, this will increase the national budget."
            $ national_budget += 100
            $ welfare += 5
        "Decline":
            vc "You have declined to puppet your aliances in the Americas."
    
    vc "Would you like to demand the South of the US, Pueto Rico and the Panama Canal from the US?"
    menu:
        "Approve":
            vc "The Americans folded, because of your great aliance in South America and they have ceded the South of the US, Puerto Rico and the Panama Canal to you, this will increase the popularity of the government but will also decrease the national budget."
            $ popularity += 20
            $ national_budget -= 100
            $ inhabitants += 5000000
            $ welfare += 5
            $ americas = 1
            jump americas_win
        "Decline":
            vc "You have declined to demand the South of the US, Puerto Rico and the Panama Canal from the US."
            $ americas = 1
            jump americas_win


    if americas == 1:
        jump americas_win
        label americas_win:  
            vc "You reclaimed your american colonies, would you like reclaim other colonies or did you fullfill your colonial ambitions already?"
            menu:
                "Reclaim other colonies":
                    vc "You have chosen to reclaim other colonies."
                    jump col_dec
                "Fullfilled colonial ambitions":
                    vc "You have fullfilled your colonial ambitions."
                    jump col_end

label col_end:
    scene bg col
    show vccol
    vc "You have successfully achieved your colonial ambitions, the people are happy and you have increased your power on the international stage, good job."
    vc "After a bit your country to rename itself to the Iberian Company and it becomes a global superpower, you have won the game."
    $ award_achievement("the_iberian_company")
    jump end

label end:
    hide vcimp
    hide vccol
    hide vccap
    hide vccom
    hide vcfas
    hide vcmon
    hide vcmil
    hide vcarc
    hide vcsoc
    hide vctot
    na "Press 'Q' to open the stat screen and see your stats and achievements one final time before the game ends."

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
            $ uk = 0
            $ alliances = 0
            $ africa = 0
            $ asia = 0
            $ americas = 0
            $ militia = 0
            $ military = 0
            $ navy = 0
            $ dock = 0
            $ generals = 0
            $ days = 0
            $ popularity = 60
            jump start
        "No":
            return 
    # This ends the game 


    return
