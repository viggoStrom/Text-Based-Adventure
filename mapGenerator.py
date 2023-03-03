import player
import random
import datetime
import re

import flowControl
flow = flowControl.flow


class map():
    def __init__(self, survivor):
        def generateAdress():
            num = random.randbytes(8)
            num = str(abs(hash(survivor.name + str(num))))

            date = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S-")

            playerName = re.sub(r"[^a-zA-Z]", "", survivor.name)

            saveAdress = f'saves/{date}{playerName}{num}.json'

            try:
                open(saveAdress, "x")
                # flow.sleep()
                # flow.newLine()
                # print("[Saved successfully]")
                pass
            except:
                generateAdress()
            
            return saveAdress

        saveAdress = generateAdress()

        with open(saveAdress, "w") as save:
            save.write(
                "{\"room\": [{\"coordinates\": [0,0],\"enemies\": [],\"radiationLevel\": 50,\"loot\": []}],\"player\": {}}")
            pass

    def generateRoom(cardinalDirection):
        pass
