import random

class map():
    def __init__(self, name):
        num = random.randbytes(8)
        num = hash(name + str(num))
        open(f'maps/map{num}.json',"w")
        pass
    
    def generateRoom(cardinalDirection):
        pass