import json
import flowControl
flow = flowControl.flow
items = json.load(open("items.json"))


class player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.armor = 0
        self.speed = 1
        self.radiation = 25
        self.equiped = {
            "rightHand": {},
            "leftHand": {},
            "body": {},
        }
        self.position = [4, 4]
        pass

    def pickUp(self, item, newLine=True):
        if newLine == True:
            flow.newLine()
        flow.sleep()
        if item not in self.inventory:
            self.inventory.append(item)
            print(f'[You picked up {item["name"][0]}]')
            if item == items["aglet"]:
                print("PLACEHOLDER (Aglets are currency)")
                pass

        else:
            self.inventory[self.inventory.index(item)]["quantity"] += 1
            print(f'[You picked up another {item["name"][1]}]')
        pass

    def showStats(self):
        print("Sure, here you go.")
        flow.sleep()
        print(f'- Your name: {self.name}')
        print(f'- Health: {self.health}%')
        print(f'- Radiation exposure: {self.radiation} rads/min')
        print(f'- Armor: {self.armor}')
        print(f'- Speed: {self.speed}')
        flow.sleep()
        pass

    def showInventory(self):
        print("Sure, here you go.")
        flow.sleep()
        for item in self.inventory:
            if item["quantity"] > 1:
                print(" - " + str(item["quantity"]
                                  ) + "x " + item["name"][1])
            else:
                print(" - " + item["name"][0])
        pass

    def look(self):
        pass

    def go(self, saveManager, playerInput):
        if "nor" in playerInput:
            self.position[1] -= 1
            flow.choose(self, saveManager, ["search", "go", "check", "menu"])
            pass
        elif "sou" in playerInput:
            self.position[1] += 1
            pass
            flow.choose(self, saveManager, ["search", "go", "check", "menu"])
        elif "wes" in playerInput:
            self.position[0] -= 1
            flow.choose(self, saveManager, ["search", "go", "check", "menu"])
            pass
        elif "eas" in playerInput:
            self.position[0] += 1
            flow.choose(self, saveManager, ["search", "go", "check", "menu"])
            pass
        pass

        allowedDirections = saveManager.read(
        )["rooms"][f'x{self.position[0]}y{self.position[1]}']["allowedDirections"]
        modifiedString = ""
        for cardinalDirection in allowedDirections.keys():
            if allowedDirections[cardinalDirection] == True:
                modifiedString += cardinalDirection
                modifiedString += " "
                pass
            pass
        modifiedString = modifiedString[:-1]

        print("Go where?")
        print(f'<{modifiedString}>')
        flow.newLine()
        response = flow.input("... ")

        if "nor" in response:
            self.position[1] -= 1
            pass
        elif "sou" in response:
            self.position[1] += 1
            pass
        elif "wes" in response:
            self.position[0] -= 1
            pass
        elif "eas" in response:
            self.position[0] += 1
            pass
        pass
        flow.choose(self, saveManager, ["search", "go", "check", "menu"])
