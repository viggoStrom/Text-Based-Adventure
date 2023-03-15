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

    def choose(player, saveManager, options):
        flow.sleep()
        flow.newLine()

        print("What do you do?")

        optionsCopy = options

        for option in optionsCopy:
            if option == "search":
                searchTable = saveManager.read(
                )["rooms"][f'x{player.position[0]}y{player.position[1]}']["loot"]
                print("here")
                replacementString = "search ("
                for place in searchTable.keys():
                    replacementString += place
                    replacementString += ", "
                    pass
                replacementString = replacementString[:-2]
                replacementString += ")"
                optionsCopy[optionsCopy.index(option)] = replacementString
                pass
            elif option == "go":
                optionsCopy[optionsCopy.index(
                    option)] = "go (north, south, west, east)"
                pass
            elif option == "look":
                optionsCopy[optionsCopy.index(
                    option)] = "look (north, south, west, east)"
                pass
            elif option == "check":
                optionsCopy[optionsCopy.index(
                    option)] = "check (inventory, stats)"
                pass
            elif option == "menu":
                optionsCopy[optionsCopy.index(
                    option)] = "menu (save, quit, save & quit)"

        for option in optionsCopy:
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
                return SystemExit

        def showCheck():
            print("Check what?")
            print("<Inventory> <Stats> <Back>")
            flow.newLine()
            response = flow.input("...")
            if "bac" in response:
                return flow.choose(player, saveManager, options)
            elif ("in" or "nv") in response:
                player.showInventory()
            elif ("st" or "at") in response:
                player.showStats()
            pass

        def showMenu():
            print("What do you want to do?")
            print("<Save> <Quit> <Save & Quit> <Back>")
            flow.newLine()
            response = flow.input("... ")
            if "bac" in response:
                return flow.choose(player, saveManager, options)
            elif ("qui" and "sav") in response:
                saveAndQuitGame(save=True, quit=True)
                pass
            elif "sav" in response:
                saveAndQuitGame(save=True)
                pass
            elif "qui" in response:
                saveAndQuitGame(quit=True)
                pass
            return

        def showSearch(playerInput):
            playerPosition = f'x{player.position[0]}y{player.position[1]}'
            lootTable = saveManager.read(
            )["rooms"][playerPosition]["loot"]

            # check if player already specified a place to search in the player input
            for place in lootTable.keys():
                if place[:3] in playerInput:
                    modifiedMap = saveManager.read().copy()
                    if isinstance(lootTable[place], list):
                        lastItem = len(lootTable.keys())-1

                        player.pickUp(items[lootTable[place][lastItem]],newLine=False)

                        del modifiedMap["rooms"][playerPosition]["loot"][place][lastItem]
                    else:
                        player.pickUp(items[lootTable[place]], newLine=False)
                        del modifiedMap["rooms"][playerPosition]["loot"][place]

                    saveManager.write(modifiedMap)
                    return

            print("What do you want to search?")
            searchOptions = ""
            for element in lootTable.keys():
                searchOptions += f"<{str(element).title()}> "
            print(searchOptions + "<Back>")
            flow.newLine()

            response = flow.input("I want to search the... ")
            flow.sleep()

            if "bac" in response:
                return flow.choose(player, saveManager, options)

            for place in lootTable.keys():
                if place[:3] in response:
                    modifiedMap = saveManager.read().copy()
                    if isinstance(lootTable[place], list):
                        lastItem = len(lootTable)-1

                        player.pickUp(
                            items[lootTable[place][lastItem]],
                            newLine=False)

                        del modifiedMap["rooms"][playerPosition]["loot"][place][lastItem]
                    else:
                        player.pickUp(items[lootTable[place]], newLine=False)
                        del modifiedMap["rooms"][playerPosition]["loot"][place]

                    saveManager.write(modifiedMap)
                    pass
                pass
            pass

        def findKeyword():
            playerInput = flow.input("I want to... ")
            flow.newLine()

            if "chec" and "inve" in playerInput:
                flow.sleep()
                player.showInventory()
                return flow.choose(player, saveManager, options)
            elif "chec" and "stat" in playerInput:
                flow.sleep()
                player.showStats()
                return flow.choose(player, saveManager, options)
            elif "chec" in playerInput:
                flow.sleep()
                showCheck()
                return flow.choose(player, saveManager, options)
            elif "sear" in playerInput:
                showSearch(playerInput)
                return flow.choose(player, saveManager, options)
            elif "go" in playerInput:
                flow.sleep()
                player.go()
                return flow.choose(player, saveManager, options)
            elif "look" in playerInput:
                flow.sleep()
                player.look()
                return flow.choose(player, saveManager, options)
            elif "menu" in playerInput:
                flow.sleep()
                return showMenu()

            print("Please rephrase that.")
            flow.newLine()
            flow.sleep()
            findKeyword()

        return findKeyword()
