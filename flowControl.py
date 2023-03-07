import time
import re
import json
config = json.load(open("config.json"))
items = json.load(open("items.json"))


class flow:
    def __init__(self):
        pass

    def sleep():
        time.sleep(config["masterSleep"])
        pass

    def newLine():
        print("\n")
        pass

    def filter(inputString):
        return re.sub(r"[^a-zA-Z0-9 ]", "", inputString)

    def input(prompt):
        return flow.filter(input(prompt)).lower()

    def pressEnter():
        flow.newLine()
        flow.input("[Press enter to continue]")
        pass

    def choose(player, *options):
        result = None
        options = list(options)

        flow.newLine()
        flow.sleep()

        print("What do you do?")

        for option in options:
            if option.split()[0] == "search":
                availablePlaces = re.findall(r'(\w+)\[', option)
                availableItems = re.findall(r'\[([^\]]+)\]', option)
                searchTable = {w: i for w, i in zip(availablePlaces, availableItems)}
                
                options[options.index(option)] = re.sub(r'\[[^\]]*\]', '', option)
                pass
            elif option == "go":
                options[options.index(option)] = "go (north, south, west, east)"
                pass
            elif option == "look":
                options[options.index(option)] = "look (north, south, west, east)"
                pass
            elif option == "check":
                options[options.index(option)] = "check (inventory, stats)"
                pass
            elif option == "menu":
                options[options.index(option)] = "menu (save, quit, save & quit)"

        for option in options:
            print("<" + option.title() + ">")

        flow.newLine()
        flow.sleep()

        def saveAndQuitGame(save=False, quit=False):
            if save == True:
                # save game here
                flow.sleep()
                print("Saving game...")
                flow.sleep()
                print("Save failed!")
                return
            if quit == True:
                SystemExit
            return

        def showStats():
            print("Sure, here you go.")
            flow.sleep()
            print(f'- Your name: {player.name}')
            print(f'- Health: {player.health}%')
            print(f'- Radiation exposure: {player.radiation} rads/min')
            print(f'- Armor: {player.armor}')
            print(f'- Speed: {player.speed}')
            flow.newLine()
            pass

        def showInventory():
            print("Sure, here you go.")
            flow.sleep()
            for item in player.inventory:
                if item["quantity"] > 1:
                    print(" - " + str(item["quantity"]
                                      ) + "x " + item["name"][1])
                else:
                    print(" - " + item["name"][0])
            pass

        def showCheck():
            print("Check what?")
            print("<Inventory> <Stats>")
            flow.newLine()
            response = flow.input("...")
            if ("in" or "nv") in response:
                showInventory()
            elif ("st" or "at") in response:
                showStats()
            pass

        def showMenu():
            print("What do you want to do?")
            print("<Save> <Quit> <Save & Quit>")
            flow.newLine()
            response = flow.input("... ")
            if ("qui" and "sav") in response:
                saveAndQuitGame(save=True, quit=True)
                pass
            elif "sav" in response:
                saveAndQuitGame(save=True)
                pass
            elif "qui" in response:
                saveAndQuitGame(quit=True)
                pass
            pass

        def showSearch():
            for option in options:
                if option.split()[0].lower() == "search":
                    searchablePlaces = flow.filter(option).split()[1:]
                    pass

            print("What do you want to search?")
            searchOptions = ""
            for element in searchablePlaces:
                searchOptions += f"<{str(element).title()}> "
            print(searchOptions)
            flow.newLine()

            response = flow.input("I want to search the... ")
            
            for place in searchTable:
                if place[:3] in response:
                    player.pickUp(items[searchTable[place]])
                    # break
            pass

        def showLook():

            pass

        def showGo():

            pass

        def findKeyword():
            rawInput = flow.input("I want to... ")
            flow.newLine()
            flow.sleep()

            if "chec" and "inve" in rawInput:
                showInventory()
                return None
            elif "chec" and "stat" in rawInput:
                showStats()
                return None
            elif "chec" in rawInput:
                showCheck()
                return None
            elif "menu" in rawInput:
                showMenu()
                return None
            elif "sear" in rawInput:
                showSearch()
                return None
            elif "look" in rawInput:
                showLook()
                return None
            elif "go" in rawInput:
                showGo()
                return None

            print("Please rephrase that.")
            flow.newLine()
            flow.sleep()
            findKeyword()

        return findKeyword()
