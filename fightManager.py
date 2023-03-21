from flowControl import flow
import json
items = json.load(open("items.json"))
enemies = json.load(open("enemies.json"))


class fight:
    def __init__(self, player, saveManager):
        self.saveManager = saveManager
        self.enemies = []
        self.intro = False
        for enemy in saveManager.read()["rooms"][player.getPos()]["enemies"]:
            self.enemies.append(enemies[enemy])

        def battleOverview():
            if len(self.enemies) > 1:
                opponent = "a bunch of enemies"
            else:
                opponent = self.enemies[0]

            divider = ""
            for i in range(len(f'= A fight has begun between {player.name} and {opponent} =')):
                divider += "="

            if self.intro == False:
                print(
                    f'= A fight has begun between {player.name} and {opponent} =')
                self.intro = True
            else:
                print(divider)

            flow.newLineSleepFight()

            for enemy in self.enemies:
                print(
                    f'{enemy["name"][1].title()}: ❤ {int(enemy["health"]/enemy["maxHealth"]*100)} %')
            flow.newLineSleepFight()

            print(f'{player.name}: ❤ {int(player.health/player.maxHealth*100)} %')
            flow.newLineSleepFight()

            print(divider)
            flow.newLineSleepFight()

        battleOverview()

        alternatives = [
            "<Attack (",
            "<Run>"
        ]
        for enemy in self.enemies:
            alternatives[0] += enemy["name"][1].title() + ", "
        alternatives[0] = alternatives[0][:-2]
        alternatives[0] += ")>"

        print("What do you do?")
        for alternative in alternatives:
            print(alternative)
        flow.newLineSleepFight()

        def promptAttack(passedthroughInput):
            def findKeyword(response, catch=False):
                for enemy in self.enemies:
                    if enemy["name"][1][:3] in response:
                        attack(enemy)
                        break

                if catch == False:
                    print("Please rephrase that.")
                    flow.newLineSleepFight()

            findKeyword(passedthroughInput, catch=True)

            print("Attack what?")
            options = ""
            for enemy in self.enemies:
                options += "<" + enemy["name"][1].title() + "> "
            print(options)
            flow.newLineSleepFight()

            response = flow.input("... ")
            flow.newLineSleepFight()

            findKeyword(response)

        def attack(enemy):
            if player.speed >= enemy["speed"]:
                print(
                    f'{player.name} was faster than {enemy["name"][1]} and attacked first.')
                self.enemies[self.enemies.index(enemy)]["health"] = self.enemies[self.enemies.index(
                    enemy)]["health"] - player.damage
                if enemy["health"] >= 0:
                    player.health -= enemy["damage"]

            else:
                print(
                    f'{enemy["name"][1].title()} was faster than {player.name} and attacked first.')
                self.enemies[self.enemies.index(enemy)]["health"] = self.enemies[self.enemies.index(
                    enemy)]["health"] - player.damage

                if player.health >= 0:
                    player.health -= enemy["damage"]
            flow.newLineSleepFight()

            battleOverview()

        def findKeyword():
            response = flow.input("... ")
            flow.newLineSleepFight()

            if "att" in response:
                promptAttack(response)
            elif "run" in response:
                for enemy in self.enemies:
                    if player.speed < enemy["speed"]:
                        print(
                            f'You try to run away but {enemy["name"][0]} got a hit in.')
                    else:
                        print(
                            f'{enemy["name"][1].title()} tried hitting you but you got away.')
                    flow.sleepFight()
                pass
                flow.newLineSleepFight()
            else:
                print("Please rephrase that.")
                flow.newLineSleepFight()
                findKeyword()

        findKeyword()
