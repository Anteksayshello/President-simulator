# The script of the game goes in this file.

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
        "war_champion": "War Champion",
        "resource_exploiter": "Resource Exploiter",
        "military_regime": "Military Regime",
        "peacekeeper": "Peacekeeper",
        "open_bakery": "Bakery Owner",
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
            "reclaim_cuba": "Cuban Reclaimer",
            "the_iberian_company": "The Iberian Company",
        },
    }

    for name, value in defaults.items():
        if not hasattr(renpy.store, name):
            setattr(renpy.store, name, value)

screen debug_hotkey():
    key "d" action ShowMenu("debug_menu")

screen debug_menu():
    tag menu

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
                textbutton "Close" action Return()

            vbox:
                xsize 420
                spacing 6

                text "Jump to" size 18 xalign 0.5
                textbutton "Start" action Jump("start")
                textbutton "Democracy " action Jump("begin")
                textbutton "Communism " action Jump("com")
                textbutton "Militarism " action Jump("milr")
                textbutton "Anarchism " action Jump("arch")
                textbutton "Socialism " action Jump("soc")
                textbutton "Monarchy " action Jump("mon")
                textbutton "Fascism " action Jump("fasc1")
                textbutton "Colonialismp" action Jump("col")
                textbutton "Final end screen" action Jump("end")

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
        vc "While fighting the Spanish army, you had a strong military and you were able to defend yourself, but the war was long and costly, you lost a lot of popularity and power but you were able to win."
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
