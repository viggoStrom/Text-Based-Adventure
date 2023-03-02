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
        pass

    def pickUp(self, item):
        self.inventory.append(item)
        print(f'[You picked up {item["name"]}]')
        pass

    # def hungerTick(self):
    #     shouldHunger = [True]*3 + [False]*7
    #     if random.choice(shouldHunger):
    #         self.stats["hunger"] -= 5 * config["hungerModifier"]
    #         pass
    #     pass

