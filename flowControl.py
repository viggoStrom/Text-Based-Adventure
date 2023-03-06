import time
import re
import json
config = json.load(open("config.json"))


class flow:
    def __init__(self):
        pass

    def sleep():
        time.sleep(config["masterSleep"])
        pass

    def newLine():
        print("\n")
        pass

    def input(prompt):
        return re.sub(r"[^a-zA-Z0-9 ]", "", input(prompt))

    def pressEnter():
        flow.newLine()
        flow.input("[Press enter to continue]")
        pass

    def choose(player, *options):
        result = None

        print("What do you do?")

        for option in options:
            if option == "go":
                option = "go (north, south, west, east)"
                pass
            elif option == "look":
                option = "look (north, south, west, east)"
                pass
            elif option == "check":
                option = "check (inventory, stats)"
                pass
            elif option == "menu":
                option = "menu (save, quit, save & quit)"

            print("<" + option.title() + ">")
            pass

        flow.sleep()
        flow.newLine()

        def saveNQuitGame(save=False, quit=False):
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
            flow.sleep()
            print("What do you want to do?")
            print("<Save> <Quit> <Save & Quit>")
            flow.newLine()
            response = flow.input("... ")
            if ("qui" and "sav") in response:
                saveNQuitGame(save=True, quit=True)
                pass
            elif "sav" in response:
                saveNQuitGame(save=True)
                pass
            elif "qui" in response:
                saveNQuitGame(quit=True)
                pass
            pass

        def showSearch():
            if options[0].lower() == "search":
                
                pass
            pass

        def showLook():

            pass

        def showGo():

            pass

        def findKeyword():
            rawInput = flow.input("I want to... ")
            flow.newLine()

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
