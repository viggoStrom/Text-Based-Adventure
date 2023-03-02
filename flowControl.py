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

    def choose(*options):
        presets = ("go", "look", "check")
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

            print("<" + option.title() + ">")
            pass
        flow.sleep()
        flow.newLine()
        rawInput = input("I want to... ").lower()
        if "check" in rawInput:
            flow.newLine()
            print("check what?")
            print("<Inventory> <Stats>")
            flow.newLine()
            input("...")
            pass
        pass
