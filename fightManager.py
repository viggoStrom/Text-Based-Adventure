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
                opponent = self.enemies[0]["name"][0]

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

        def promptAttack(passedthroughInput):
            for enemy in self.enemies:
                if enemy["name"][1][:3] in passedthroughInput:
                    attack(enemy)
                    return findKeyword()

            print("Attack what?")
            options = ""
            for enemy in self.enemies:
                options += "<" + enemy["name"][1].title() + "> "
            print(options)
            flow.newLineSleepFight()

            response = flow.input("... ")
            flow.newLineSleepFight()

            for enemy in self.enemies:
                if enemy["name"][1][:3] in response:
                    attack(enemy)
                    return findKeyword()
            # else
            print("Please rephrase that.")
            flow.newLineSleepFight()
            promptAttack()

        def attack(enemy):
            if player.speed >= enemy["speed"]:
                print(
                    f'{player.name} was faster than {enemy["name"][1]} and attacked first and dealt {player.damage} dmg while {enemy["name"][1]} dealt {enemy["damage"]} dmg.')
                self.enemies[self.enemies.index(enemy)]["health"] = self.enemies[self.enemies.index(
                    enemy)]["health"] - player.damage
                if enemy["health"] >= 0:
                    player.health -= enemy["damage"]

            else:
                print(
                    f'{enemy["name"][1].title()} was faster than {player.name} and attacked first and dealt {enemy["damage"]} dmg while {player.name} dealt {player.damage} dmg.')
                self.enemies[self.enemies.index(enemy)]["health"] = self.enemies[self.enemies.index(
                    enemy)]["health"] - player.damage

                if player.health >= 0:
                    player.health -= enemy["damage"]
            flow.newLineSleepFight()

            battleOverview()

        def checkDeath():
            if player.health <= 0:
                print("You have died.")
                flow.newLineSleep()
                print("This is one of multiple endings")
                flow.newLineSleep()
                raise SystemExit
                
            for enemy in self.enemies:
                if enemy["health"] <= 0:
                    print(f'You have defeated {enemy["name"][1].title()}.')
                    flow.newLineSleep()
                    player.pickUp(items[enemy["drops"][0]])
                    try:
                        pass
                    except:
                        print(f'{enemy["name"][0].title()} did not drop any loot.')
                        flow.newLineSleep()
                        pass
                    map = saveManager.read()
                    del map["rooms"][player.getPos()]["enemies"][map["rooms"][player.getPos()]["enemies"].index(enemy["name"][1])]
                    saveManager.write(map)
            pass

        def findKeyword():
            checkDeath()
            if len(saveManager.read()["rooms"][player.getPos()]["enemies"]) <= 0:
                return

            print("What do you do?")
            for alternative in alternatives:
                print(alternative)
            flow.newLineSleepFight()

            response = flow.input("... ")
            flow.newLineSleepFight()

            if "att" in response:
                promptAttack(response)
            elif "run" in response:
                for enemy in self.enemies:
                    if player.speed < enemy["speed"]:
                        print(
                            f'You try to run away but {enemy["name"][0]} got a hit in. ({enemy["damage"]} dmg)')
                        player.health -= enemy["damage"]
                    else:
                        print(
                            f'{enemy["name"][1].title()} tried hitting you but you got away.')
                    flow.sleepFight()
                    checkDeath()
                pass
                flow.newLineSleepFight()
            else:
                print("Please rephrase that.")
                flow.newLineSleepFight()
                findKeyword()
            findKeyword

        battleOverview()

        alternatives = [
            "<Attack (",
            "<Run>"
        ]
        for enemy in self.enemies:
            alternatives[0] += enemy["name"][1].title() + ", "
        alternatives[0] = alternatives[0][:-2]
        alternatives[0] += ")>"

        findKeyword()
