import time
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

    def pressEnter():
        flow.newLine()
        input("[Press enter to continue]")
        pass

    def choose(player, *options):
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

        def showStats():
            flow.newLine()
            print("Sure, here you go.")
            flow.sleep()
            print(f'- Your name: {player.name}')
            print(f'- Health: {player.health}%')
            print(f'- Radiation exposure: {player.radiation} rads/min')
            print(f'- Armor: {player.armor}%')
            print(f'- Speed: {player.speed}')
            flow.newLine()
            pass

        def showInventory():
            flow.newLine()
            print("Sure, here you go.")
            flow.sleep()
            for item in player.inventory:
                if item["quantity"] > 1:
                    print(" - " + str(item["quantity"]) + "x " + item["name"][1])
                else:
                    print(" - " + item["name"][0])
            pass

        def findKeyword():
            rawInput = input("I want to... ").lower()
            
            if "chec" and "inve" in rawInput:
                showInventory()
                return
            elif "chec" and "stat" in rawInput:
                showStats()
                return
            elif "chec" in rawInput:
                flow.newLine()
                print("Check what?")
                print("<Inventory> <Stats>")
                flow.newLine()
                response = input("...").lower()
                if ("in" or "nv") in response:
                    showInventory()
                    return
                elif ("st" or "at") in response:
                    showStats()
                    return

            print("Please rephrase that.")
            flow.newLine()
            flow.sleep()
            findKeyword()

        findKeyword()
