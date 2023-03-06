# import random
import json
config = json.load(open("config.json"))


class player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.armor = 0
        self.speed = 1
        # self.hunger = 100
        self.radiation = 25
        self.equiped = {                
            "rightHand": {},
            "leftHand": {},
            "body": {},
            }
        self.position = [0,0]
        pass

    def pickUp(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            print(f'[You picked up {item["name"][0]}]')
        else:
            self.inventory[self.inventory.index(item)]["quantity"] += 1
            print(f'[You picked up another {item["name"][1]}]')
        pass

    def loot(self):
        result = None
        result = self.pickUp()
        return result

    # def hungerTick(self):
    #     shouldHunger = [True]*3 + [False]*7
    #     if random.choice(shouldHunger):
    #         self.stats["hunger"] -= 5 * config["hungerModifier"]
    #         pass
    #     pass

