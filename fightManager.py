import json
items = json.load(open("items.json"))
enemies = json.load(open("enemies.json"))
from flowControl import flow


class fight:
    def __init__(self, player, saveManager):
        self.player = player
        self.saveManager = saveManager
        self.enemies = []
        for enemy in saveManager.read()["rooms"][self.player.getPos()]["enemies"]:
            self.enemies.append(enemies[enemy])

        if len(self.enemies) > 1:
            opponent = "a bunch of enemies"
        else:
            opponent = self.enemies[0]
        
        print(f'= A fight has begun between {self.player.name} and {opponent} =')
        flow.newLineSleepFight()

        for enemy in self.enemies:
            print(f'{enemy["name"][1].title()}: ❤ 100 %')
        flow.newLineSleepFight()
        
        print(f'{self.player.name}: ❤ {self.player.health} %')
        flow.newLineSleepFight()

        divider = ""
        for i in range(len(f'= A fight has begun between {self.player.name} and {opponent} =')):
            divider += "="
        print(divider)
        flow.newLineSleepFight()
        
        alternatives = [
            "<Attack (",
            "<Run>"
        ]
        for enemy in self.enemies:
            alternatives[0] += enemy["name"][1] + ", "
        alternatives[0] = alternatives[0][:-2]
        alternatives[0] += ")>"

        print("What do you do?")
        for alternative in alternatives:
            print(alternative)
        flow.newLineSleepFight()

        response = flow.input("... ")
        
        pass