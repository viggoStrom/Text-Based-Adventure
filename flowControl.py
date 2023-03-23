import time
import re
import json
config = json.load(open("config.json"))
items = json.load(open("items.json"))

# For every funtion that prints and such the structure will be:
#
# CONTENT
# newline
# sleep
#
# i.e. trailing newlines and sleep


class flow:
    def __init__(self):
        pass

    def sleep():
        time.sleep(config["masterSleep"])
        pass
   
    def sleepFight():
        time.sleep(config["masterFightSleep"])
        pass

    def newLine():
        print("\n")
        pass

    def newLineSleep():
        flow.newLine()
        flow.sleep()

    def newLineSleepFight():
        flow.newLine()
        time.sleep(config["masterFightSleep"])

    def filter(inputString):
        return re.sub(r"[^a-zA-Z0-9 ]", "", inputString)

    def input(prompt):
        return flow.filter(input(prompt)).lower()

    def pressEnter():
        flow.input("[Press enter to continue]")
        flow.newLineSleep()
        pass

    def choose(player, saveManager, options):
        def doScenario():
            if player.getPos() == "x3y0" and player.equipped["body"] == items["vaultSuit"]:
                print("You are safe now. I recognize your suit, you're one of us, just a bit more hardened perhaps *smirks*.")
                flow.newLineSleep()
                print("This is one of multiple endings.")
                flow.newLineSleep()
                raise SystemExit
            elif player.getPos() == "x1y0":
                print("Welcome to the shops weary traveller! shouts a person over att one of the stores. Do you have any aglets on you perhaps?")
                flow.newLineSleep()

                def yesOrNo():
                    response = flow.input("(Y/N)... ")
                    flow.newLineSleep()
                    
                    if "n" in response:
                        print("Well that's a shame ain't it, kiddo.")
                        flow.newLineSleep()
                        pass
                    elif "y" in response:
                        print("Oh great! I have some quality merchandise like this 9mm gun *now ammo though*.")
                        flow.newLineSleep()
                        if items["aglet"] in player.inventory:
                            print("Before you could give your opinion on the matter the shopkeep hands you the gun and takes all of your caps.")
                            flow.newLineSleep()
                            del player.inventory[player.inventory.index(items["aglet"])]
                            player.pickUp(items["9mmGun"])
                        else:
                            print("Ay kiddo, it seems like you don't have any aglets on you there. I can't trade you someone who doesn't have any money.")
                            flow.newLineSleep()
                            pass
                        pass
                    else:
                        print("Please rephrase that.")
                        flow.newLineSleep()
                        yesOrNo()
                        pass

                yesOrNo()
                map = saveManager.read()
                map["rooms"][player.getPos()]["scenarioRead"] = False
                saveManager.write(map)
            pass        
        doScenario()
        def saveAndQuitGame(save=False, quit=False):
            if save == True:
                # save game here
                flow.sleep()
                print("Saving game...")
                flow.sleep()
                print("Save failed!")
                return
            if quit == True:
                raise SystemExit

        def showCheck(playerInput):
            if "inv" in playerInput:
                player.showInventory()
                return flow.choose(player, saveManager, options)
            elif "sta" in playerInput:
                player.showStats()
                return flow.choose(player, saveManager, options)

            print("Check what?")
            print("<Inventory> <Stats> <Back>")
            flow.newLineSleep()

            response = flow.input("...")
            flow.newLineSleep()

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
            flow.newLineSleep()

            response = flow.input("... ")
            flow.newLineSleep()

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

                    player.pickUp(items[lootTable[place]])
                    del modifiedMap["rooms"][playerPosition]["loot"][place]
                    saveManager.write(modifiedMap)
                    return

            print("What do you want to search?")
            searchOptions = ""
            for element in lootTable.keys():
                searchOptions += f"<{str(element).title()}> "
            print(searchOptions + "<Back>")
            flow.newLineSleep()

            response = flow.input("I want to search the... ")
            flow.newLineSleep()

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
        flow.newLineSleep()

        def findKeyword():
            playerInput = flow.input("I want to... ")
            flow.newLineSleep()

            if "che" in playerInput:
                showCheck(playerInput)
                return flow.choose(player, saveManager, options)

            elif "sea" in playerInput:
                showSearch(playerInput)
                return flow.choose(player, saveManager, options)

            elif "go" in playerInput:
                player.go(saveManager, playerInput)
                return flow.choose(player, saveManager, options)

            elif "men" in playerInput:
                return showMenu()

            print("Please rephrase that.")
            flow.newLineSleep()
            findKeyword()

        return findKeyword()
