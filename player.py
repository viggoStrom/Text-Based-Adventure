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

    def pickUp(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            print(f'[You picked up {item["name"][0]}]')
            if item == items["aglet"]:
                flow.newLineSleep()
                print("It appears to be a small, metallic object with a plastic coating at one end. It's an aglet, the currency used in this world. Aglets hold value and can be used to purchase goods and services. Keep them safe, as they may prove useful in your journey through the wasteland.")
                pass

        else:
            self.inventory[self.inventory.index(item)]["quantity"] += 1
            print(f'[You picked up another {item["name"][1]}]')
            pass
        flow.newLineSleep()
        pass

    def showStats(self):
        print("Sure, here you go.")
        flow.sleep()
        print(f'- Your name: {self.name}')
        print(f'- Health: {self.health}%')
        print(f'- Radiation exposure: {self.radiation} rads/min')
        print(f'- Armor: {self.armor}')
        print(f'- Speed: {self.speed}')
        flow.newLineSleep()
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
        flow.newLineSleep()
        pass

    def look(self):
        pass

    def go(self, saveManager, playerInput):        
        def arrivedAt():
            nameOfNewRoom = saveManager.read(
            )["rooms"][f'x{self.position[0]}y{self.position[1]}']["name"]
            if nameOfNewRoom != "":
                print(f'You arrived at {nameOfNewRoom}.')
            else:
                print("You have arrived.")
                pass
            flow.newLineSleep()

            scenario = saveManager.read()["rooms"][f'x{self.position[0]}y{self.position[1]}']
            if scenario["scenario"] != "" and scenario["scenarioRead"] == False:
                print(scenario["scenario"])
                flow.newLineSleep()
                map = saveManager.read()
                map["rooms"][f'x{self.position[0]}y{self.position[1]}']["scenarioRead"] = True
                saveManager.write(map)
            pass

        allowedDirections = saveManager.read()["rooms"][f'x{self.position[0]}y{self.position[1]}']["allowedDirections"]

        if "nor" in playerInput and allowedDirections["north"]:
            self.position[1] -= 1
            arrivedAt()
            flow.choose(self, saveManager, ["search", "go", "check", "menu"])
            pass

        elif "sou" in playerInput and allowedDirections["south"]:
            self.position[1] += 1
            arrivedAt()
            flow.choose(self, saveManager, ["search", "go", "check", "menu"])
            pass

        elif "wes" in playerInput and allowedDirections["west"]:
            arrivedAt()
            self.position[0] -= 1
            flow.choose(self, saveManager, ["search", "go", "check", "menu"])
            pass

        elif "eas" in playerInput and allowedDirections["east"]:
            self.position[0] += 1
            arrivedAt()
            flow.choose(self, saveManager, ["search", "go", "check", "menu"])
            pass
        pass

        modifiedString = ""
        for cardinalDirection in allowedDirections.keys():
            if allowedDirections[cardinalDirection] == True:
                modifiedString += f'<{cardinalDirection}> '
                pass
            pass
        modifiedString += "<cancel>"

        print("Go where?")
        print(modifiedString.title())
        flow.newLineSleep()

        def findKeyword():
            response = flow.input("... ")
            flow.newLineSleep()

            if "can" in response:
                return flow.choose(self, saveManager, ["search", "go", "check", "menu"])

            elif "nor" in response and allowedDirections["north"]:
                self.position[1] -= 1
                pass

            elif "sou" in response and allowedDirections["south"]:
                self.position[1] += 1
                pass

            elif "wes" in response and allowedDirections["west"]:
                self.position[0] -= 1
                pass

            elif "eas" in response and allowedDirections["east"]:
                self.position[0] += 1
                pass
            else:
                print("Please rephrase that.")
                flow.newLineSleep()
                return findKeyword()
            pass

            arrivedAt()
        
        findKeyword()

        flow.choose(self, saveManager, ["search", "go", "check", "menu"])
