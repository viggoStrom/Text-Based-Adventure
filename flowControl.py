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

        print("What do you do?")

        optionsCopy = options.copy()

        for option in optionsCopy:
            if option == None:
                pass
            elif option == "search":
                searchTable = saveManager.read(
                )["rooms"][f'x{player.position[0]}y{player.position[1]}']["loot"]

                if len(searchTable) != 0:
                    replacementString = "search ("
                    for place in searchTable.keys():
                        replacementString += place
                        replacementString += ", "
                        pass
                    replacementString = replacementString[:-2]
                    replacementString += ")"
                    optionsCopy[optionsCopy.index(option)] = replacementString
                else:
                    optionsCopy[optionsCopy.index(option)] = None
                    options[options.index(option)] = None
                    pass
                pass
            elif option == "go":
                allowedDirections = saveManager.read(
                )["rooms"][f'x{player.position[0]}y{player.position[1]}']["allowedDirections"]
                modifiedString = "go ("
                for cardinalDirection in allowedDirections.keys():
                    if allowedDirections[cardinalDirection] == True:
                        modifiedString += cardinalDirection
                        modifiedString += ", "
                        pass
                    pass
                modifiedString = modifiedString[:-2]
                modifiedString += ")"
                optionsCopy[optionsCopy.index(option)] = modifiedString
                pass
            # elif option == "look":
            #     optionsCopy[optionsCopy.index(
            #         option)] = "look (north, south, west, east)"
            #     pass
            elif option == "check":
                optionsCopy[optionsCopy.index(
                    option)] = "check (inventory, stats)"
                pass
            elif option == "menu":
                optionsCopy[optionsCopy.index(
                    option)] = "menu (save, quit, save & quit)"

        for option in optionsCopy:
            if option != None:
                print("<" + option.title() + ">")

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

        def showCheck(playerInput):
            if "inv" in playerInput:
                player.showInventory()
                return flow.choose(player, saveManager, options)
            elif "sta" in playerInput:
                player.showStats()
                return flow.choose(player, saveManager, options)

            print("Check what?")
            print("<Inventory> <Stats> <Back>")
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

                    player.pickUp(items[lootTable[place]], newLine=False)
                    del modifiedMap["rooms"][playerPosition]["loot"][place]
                    saveManager.write(modifiedMap)
                    return

            print("What do you want to search?")
            searchOptions = ""
            for element in lootTable.keys():
                searchOptions += f"<{str(element).title()}> "
            print(searchOptions + "<Back>")

            response = flow.input("I want to search the... ")

            if "bac" in response:
                return flow.choose(player, saveManager, options)

            for place in lootTable.keys():
                if place[:3] in response:
                    modifiedMap = saveManager.read().copy()

                    player.pickUp(items[lootTable[place]])
                    del modifiedMap["rooms"][playerPosition]["loot"][place]
                    saveManager.write(modifiedMap)
                    pass
                pass
            pass

        def findKeyword():
            playerInput = flow.input("I want to... ")

            if "chec" in playerInput:
                showCheck(playerInput)
                return flow.choose(player, saveManager, options)

            elif "sear" in playerInput:
                showSearch(playerInput)
                return flow.choose(player, saveManager, options)

            elif "go" in playerInput:
                player.go(saveManager, playerInput)
                return flow.choose(player, saveManager, options)

            elif "menu" in playerInput:
                return showMenu()

            print("Please rephrase that.")
            findKeyword()

        return findKeyword()
