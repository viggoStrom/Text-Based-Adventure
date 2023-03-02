
class player:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.stats = {
            "health": 100,
            "speed": 1,
            "hunger": 100,
            "experience": 0,
            # "happiness": 100,
        }
        pass

    def pickUp(self, item):
        print(item)
        pass