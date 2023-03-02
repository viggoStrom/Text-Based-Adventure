import items

class player:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.stats = {
            "health": 100,
            "speed": 1,
            # "happiness": 100,
            "hunger": 100,
        }
        pass

    def pickUp(self, item):

        pass