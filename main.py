import re
import random

import player
import flowControl
flow = flowControl.flow
import mapGenerator

import json
item = json.load(open("items.json"))
config = json.load(open("config.json"))


def intro():
    def logo():
        print("Welcome to")
        print(" ██████╗ ███████╗███████╗ █████╗ ████████╗██╗ ██████╗ ")
        print("██╔════╝ ██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝ ")
        print("██║  ███╗█████╗  ███████╗███████║   ██║   ██║██║  ███╗")
        print("██║   ██║██╔══╝  ╚════██║██╔══██║   ██║   ██║██║   ██║")
        print("╚██████╔╝███████╗███████║██║  ██║   ██║   ██║╚██████╔╝")
        print(" ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ")
        flow.newLine()
        pass

    def exposition():
        print("In the aftermath of a global nuclear war, the world is a barren wasteland. The few surviving humans eke out a living in the ruins of once-great cities, scavenging for food, water, and supplies among the rubble and debris. The survivors face constant danger from mutated creatures, raiders, and other humans who will do whatever it takes to survive. The few remaining factions are locked in a struggle for power, territory, and resources. Technology has regressed to a crude and makeshift state, with primitive weapons and armor fashioned from scrap metal and scavenged materials. The few remaining functioning machines and gadgets are highly prized and fiercely contested. Radiation levels are still dangerously high in many areas, and survivors must constantly monitor their exposure levels and seek out supplies of RadAway to counteract the effects of radiation poisoning. As a player in this world, you will need to navigate the dangers of the wasteland, making alliances, fighting enemies, and searching for resources and technologies that can help you survive and thrive. You'll need to make tough choices and face difficult moral dilemmas as you navigate the harsh realities of life in a post-apocalyptic world.")
        flow.pressEnter()
        pass

    logo()
    flow.sleep()
    exposition()
    pass


def playerSetup():
    flow.newLine()
    print("Welcome to the post-apocalyptic wasteland. Before we begin, what is your name?")
    flow.newLine()

    name = re.sub(r"[^a-zA-Z ]", "", input("My name is... ")).title()
    if name == "":
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

    flow.sleep()

    flow.newLine()
    print(
        f"Nice to meet you, {survivor.name}! Your journey through the wasteland begins now.")
    return survivor


def vaultSequence():
    flow.pressEnter()
    flow.newLine()

    print("You slowly open your eyes, feeling groggy and disoriented. As your senses slowly come back to you, you hear the familiar sound of Geiger counters going wild in the background. You look down to see a knife in your hand, but you have no idea how you got here, or what happened. You seem to be in a vault of some sort, but everything is hazy and confusing.")
    flow.sleep()
    flow.newLine()

    survivor.pickUp(item["knife"])
    flow.sleep()
    flow.newLine()

    flow.choose(survivor, "search (floor, lockers, bodies)", "go", "look","check")
    pass


# intro()
# survivor = playerSetup()
survivor = player.player("Fiona Fernandez")
# vaultSequence()
map = mapGenerator.map(survivor)

# endings:
# time capsule
# deep sleep a la futurama
# find true love and settle down
# die
# suicide
# die from radiation
# buy a casino
# make a deal with the devil
#   become a mutant
# roaches take over

# ideas:
# fake difficulty slider
# aglets as currency
# stickers you find on fruit as currency
# burn down a city
# roach boss
# ability to consume every object ranging from hp gain to death (suicide)
# save system via json