from fightManager import fight
import json
from flowControl import flow
items = json.load(open("items.json"))


class player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 10
        self.maxHealth = 10
        self.damage = 0
        self.armor = 0
        self.speed = 1
        self.radiation = 25
        self.equipped = {
            "rightHand": "",
            "leftHand": "",
            "body": "",
        }
        self.position = [2, 3]
        pass

    def getPos(self):
        return f'x{self.position[0]}y{self.position[1]}'

    def equip(self, item, place):
        self.equipped[place] = items[item]
        for item in self.equipped.values():
            try:
                self.armor += item["armor"]
            except:
                pass
            try:
                self.damage += item["damage"]
            except:
                pass
            try:
                self.speed += item["speed"]
            except:
                pass
        pass

    def pickUp(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            print(f'[You picked up {item["name"][0]}]')
            flow.newLineSleep()
            if item == items["aglet"]:
                print("It appears to be a small, metallic object with a plastic coating at one end. It's an aglet, the currency used in this world. Aglets hold value and can be used to purchase goods and services. Keep them safe, as they may prove useful in your journey through the wasteland.")
                flow.newLineSleep()
                pass
            if item == items["knife"]:
                print(
                    "You feel like you are going to need this in the future so you equip it straight away.")
                self.equip("knife", "rightHand")
                flow.newLineSleep()
            if item == items["vaultSuit"]:
                print("The clothes I am wearing are dirty and somewhat torn.")
                self.equip("vaultSuit", "body")
                flow.newLineSleep()
                pass

        else:
            self.inventory[self.inventory.index(item)]["quantity"] += 1
            print(f'[You picked up another {item["name"][1]}]')
            flow.newLineSleep()
            pass
        pass

    def showStats(self):
        print("Sure, here you go.")
        flow.sleep()
        print(f'- Your name: {self.name}')
        print(f'- Health: {int(self.health/self.maxHealth*100)}%')
        # print(f'- Radiation exposure: {self.radiation} rads/min')
        print(f'- Armor: {self.armor}')
        print(f'- Speed: {self.speed}')
        flow.newLineSleep()
        pass

    def showInventory(self):
        print("Sure, here you go.")
        flow.sleep()
        for item in self.inventory:
            if item["quantity"] > 1:
                print(" - " + str(item["quantity"]) + "x " + item["name"][1])
            elif item in self.equipped.values():
                print(f' - {item["name"][0]} (equipped)')
                pass
            else:
                print(" - " + item["name"][0])
        flow.newLineSleep()

        def findKeyword():
            print("What do you do?")
            print("<Equip> <Unequip> <Use> <Back>")
            flow.newLineSleep()

            response = flow.input("... ")
            flow.newLineSleep()

            if ("eq" or "qu") in response:
                print("Equip what?")
                for item in self.inventory:
                    equipped = ""
                    if item in self.equipped.values():
                        equipped = "(equipped)"
                    print(f' - {item["name"][1]} {equipped}')
                flow.newLineSleep()

                def findKeyword():
                    response = flow.input("... ")

                    for item in self.equipped.values():
                        if type(item) != dict:
                            pass
                        elif response[:3] in item["name"][1]:
                            print(f'{item["name"][1].title()} is already equipped.')
                            flow.newLineSleep()
                            pass

                    print("Please rephrase that.")
                    flow.newLineSleep()
                    findKeyword()
                
                findKeyword()
                pass

            elif ("un" or "ne") in response:
                pass

            elif "use" in response:
                pass

            elif ("bac" or "bak") in response:
                pass
            
            else:
                print("Please rephrase that.")
                flow.newLineSleep()
                findKeyword()
        
        findKeyword()
        pass

    def go(self, saveManager, playerInput):
        def arrivedAt():
            nameOfNewRoom = saveManager.read(
            )["rooms"][self.getPos()]["name"]
            if nameOfNewRoom != "":
                print(f'You arrived at {nameOfNewRoom}.')
            else:
                print("You have arrived.")
                pass
            flow.newLineSleep()

            scenario = saveManager.read()["rooms"][self.getPos()]
            if scenario["scenario"] != "" and scenario["scenarioRead"] == False:
                print(scenario["scenario"])
                flow.newLineSleep()

                map = saveManager.read()
                map["rooms"][self.getPos()]["scenarioRead"] = True
                saveManager.write(map)

            if len(saveManager.read()["rooms"][self.getPos()]["enemies"]) > 0:
                fight(self, saveManager)
                pass
            pass

        allowedDirections = saveManager.read(
        )["rooms"][self.getPos()]["allowedDirections"]

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
