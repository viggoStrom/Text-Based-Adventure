import random
import datetime
import re
import shutil
import json
import os

class map():
    def __init__(self, player):
        def generateAdress():
            num = random.randbytes(8)
            num = str(abs(hash(player.name + str(num))))

            date = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S-")

            playerName = re.sub(r"[^a-zA-Z]", "", player.name)

            saveDir = 'saves/saves'
            if not os.path.exists(saveDir):
                os.makedirs(saveDir)
            saveAdress = f'{saveDir}/{date}{playerName}{num}.json'

            try:
                open(saveAdress, "x")
                pass
            except:
                generateAdress()

            return saveAdress

        self.saveAdress = generateAdress()

        templateAdress = "saves/template/map.json"
        try:
            shutil.copy(templateAdress, self.saveAdress)
        except:
            print(f"Error: Files missing... ({templateAdress})")
            SystemExit
        pass


    def write(self, newData):
        json.dump(newData, open(self.saveAdress, "w"))
        pass

    def read(self):
        return json.load(open(self.saveAdress))