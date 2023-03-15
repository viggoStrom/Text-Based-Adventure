import flowControl
flow = flowControl.flow
import json
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

    def go(self, options):
        print("Go where?")
        print(f'<{0}>')
        flow.newLine()
        response = flow.input("... ")
        pass
