import time
import json
config = json.load(open("config.json"))


class flow:
    def __init__(self):
        pass

    def sleep():
        time.sleep(config["masterSleep"])
        pass

    def pressEnter():
        print("\n")
        input("[Press enter to continue]")
        pass

    def choose(*options):
        print("What do you do?")
        for option in options:
            if option == "go":
                option = "go (north, south, west, east)"
                pass
            elif option == "look":
                option = "look (north, south, west, east)"
                pass
            
            print("<" + option.title() + ">")
            pass
        flow.sleep()
        print("\n")
        rawInput = input("I want to... ")
        pass
