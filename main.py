import json
import random
import re

import player
import gameManager
from flowControl import flow

item = json.load(open("items.json"))
config = json.load(open("config.json"))


def intro():
    print("Welcome to")
    flow.sleep()
    print(" ██████╗ ███████╗███████╗ █████╗ ████████╗██╗ ██████╗ ")
    print("██╔════╝ ██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝ ")
    print("██║  ███╗█████╗  ███████╗███████║   ██║   ██║██║  ███╗")
    print("██║   ██║██╔══╝  ╚════██║██╔══██║   ██║   ██║██║   ██║")
    print("╚██████╔╝███████╗███████║██║  ██║   ██║   ██║╚██████╔╝")
    print(" ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ")
    flow.newLineSleep()

    print("In the aftermath of a global nuclear war, the world is a barren wasteland. The few surviving humans eke out a living in the ruins of once-great cities, scavenging for food, water, and supplies among the rubble and debris. The survivors face constant danger from mutated creatures, raiders, and other humans who will do whatever it takes to survive. The few remaining factions are locked in a struggle for power, territory, and resources. Technology has regressed to a crude and makeshift state, with primitive weapons and armor fashioned from scrap metal and scavenged materials. The few remaining functioning machines and gadgets are highly prized and fiercely contested. Radiation levels are still dangerously high in many areas, and survivors must constantly monitor their exposure levels and seek out supplies of RadAway to counteract the effects of radiation poisoning. As a player in this world, you will need to navigate the dangers of the wasteland, making alliances, fighting enemies, and searching for resources and technologies that can help you survive and thrive. You'll need to make tough choices and face difficult moral dilemmas as you navigate the harsh realities of life in a post-apocalyptic world.")
    flow.newLineSleep()
    flow.pressEnter()
    pass


def playerSetup():
    print("Welcome to the post-apocalyptic wasteland. Before we begin, what is your name?")
    flow.newLineSleep()

    name = flow.input("My name is... ").title()
    flow.newLineSleep()

    name = re.sub(r'\s{2,}', " ", name)
    if name == "" or name == " ":
        randomNames = [
            "Sally Smith",
            "Max Matthews",
            "Peter Parker",
            "Lucy Lee",
            "Ben Brown",
            "Molly Martin",
            "Jake Johnson",
            "Fiona Fernandez",
            "Kyle King",
            "Samantha Stevens"
        ]
        name = random.choice(randomNames)
        pass

    survivor = player.player(name)

    print(
        f"Nice to meet you, {survivor.name}! Your journey through the wasteland begins now.")
    flow.newLineSleep()
    return survivor


def vaultSequence():
    flow.pressEnter()

    print("You slowly open your eyes, feeling groggy and disoriented. As your senses slowly come back to you, you hear the familiar sound of Geiger counters going wild in the background. You look down to see a knife in your hand, but you have no idea how you got here, or what happened. You seem to be in a vault of some sort, but everything is hazy and confusing.")
    flow.newLineSleep()

    survivor.pickUp(item["knife"])

    #
    survivor.position = [2, 1]
    from fightManager import fight
    fight(survivor, saveManager)
    #

    flow.choose(survivor, saveManager, ["search", "go", "check", "menu"])
    pass


# intro()
survivor = playerSetup()
saveManager = gameManager.map(survivor)
vaultSequence()

# endings:
#   time capsule
#   deep sleep a la futurama
#   find true love and settle down
#   die
#   suicide
#   die from radiation
#   buy a casino
#   make a deal with the devil
#     become a mutant
#   roaches take over

# ideas:
#   fake difficulty slider
#   aglets as currency
#   stickers you find on fruit as currency
#   burn down a city
#   roach boss
#   ability to consume every object ranging from hp gain to death (suicide)
#   save system via json
