import random
import datetime
import re
import shutil

import flowControl
flow = flowControl.flow


class map():
    def __init__(self, player):
        def generateAdress():
            num = random.randbytes(8)
            num = str(abs(hash(player.name + str(num))))

            date = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S-")

            playerName = re.sub(r"[^a-zA-Z]", "", player.name)

            saveAdress = f'saves/saves/{date}{playerName}{num}.json'

            try:
                open(saveAdress, "x")
                pass
            except:
                generateAdress()

            return saveAdress

        self.saveAdress = generateAdress()

        try:
            shutil.copy("saves/template/map.json", self.saveAdress)
        except:
            print("Error: Files missing... (saves/template/map.json)")
            SystemExit
        pass

        # code that writes to json
        # save = json.load(open(self.saveAdress))
        # save["player"]["position"] = player.position
        # json.dump(save, open(self.saveAdress, "w"))
