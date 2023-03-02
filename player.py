class player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.stats = {
            "health": 100,
            "speed": 1,
            "hunger": 100,
            "equiped": {
                "right": {},
                "left": {},
                "body": {}
            },
        }
        pass

    def pickUp(self, item):
        print("\n")
        print(f'<You picked up {item["name"]}>')
        print("\n")
        self.inventory.append(item)
        pass