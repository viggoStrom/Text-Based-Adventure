import time
import re

masterSleep = .6

def pressEnter():
    print("\n")
    input("[Press enter to continue]")
    pass


def intro():
    def logo():
        print("Welcome to")
        print(" ██████╗ ███████╗███████╗ █████╗ ████████╗██╗ ██████╗ ")
        print("██╔════╝ ██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝ ")
        print("██║  ███╗█████╗  ███████╗███████║   ██║   ██║██║  ███╗")
        print("██║   ██║██╔══╝  ╚════██║██╔══██║   ██║   ██║██║   ██║")
        print("╚██████╔╝███████╗███████║██║  ██║   ██║   ██║╚██████╔╝")
        print(" ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ")
        print("\n")
        pass

    def exposition():
        print("In the aftermath of a global nuclear war, the world is a barren wasteland. The few surviving humans eke out a living in the ruins of once-great cities, scavenging for food, water, and supplies among the rubble and debris. The survivors face constant danger from mutated creatures, raiders, and other humans who will do whatever it takes to survive. The few remaining factions are locked in a struggle for power, territory, and resources. Technology has regressed to a crude and makeshift state, with primitive weapons and armor fashioned from scrap metal and scavenged materials. The few remaining functioning machines and gadgets are highly prized and fiercely contested. Radiation levels are still dangerously high in many areas, and survivors must constantly monitor their exposure levels and seek out supplies of RadAway to counteract the effects of radiation poisoning. As a player in this world, you will need to navigate the dangers of the wasteland, making alliances, fighting enemies, and searching for resources and technologies that can help you survive and thrive. You'll need to make tough choices and face difficult moral dilemmas as you navigate the harsh realities of life in a post-apocalyptic world.")
        pressEnter()
        pass

    logo()
    time.sleep(masterSleep)
    exposition()
    pass


def playerSetup():
    class player:
        def __init__(self, name):
            self.name = name
            pass

    print("\n")
    print("Welcome to the post-apocalyptic wasteland. Before we begin, what is your name?")
    print("\n")

    name = re.sub(r"[^a-zA-Z ]", "", input("My name is... ")).title()
    if name == "":
        randomNames = []
        pass
    survivor = player(name)
    time.sleep(masterSleep)

    print("\n")
    print(
        f"Nice to meet you, {survivor.name}! Your journey through the wasteland begins now.")
    pass


intro()
playerSetup()
