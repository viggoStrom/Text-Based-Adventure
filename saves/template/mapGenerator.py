import json
import math

if input("Sure you wanna regenerate the map template? y/n \n ...") != "y":
    SystemExit
else:
    print("ok")

    columns = 9
    rows = 9

    map = json.load(open("saves/template/map.json"))

    map = {"rooms": {}, "meta": {}}

    map["meta"] = {
        "rows": rows,
        "columns": columns,
        "template": {
            "name": "",
            "coordinates": [0, 0],
            "loot": [],
            "look": {
                "north": "",
                "south": "",
                "west": "",
                "east": ""
            },
            "allowedDirections": {
                "north": True,
                "south": True,
                "west": True,
                "east": True
            },
            "enemies": [],
            "radiation": 0
        }
    }

    for y in range(0, rows):
        for x in range(0, columns):
            map["rooms"][f'x{x}y{y}'] = {}
            map["rooms"][f'x{x}y{y}'] = map["meta"]["template"]
            pass
        pass
        # room["name"] = ""
        # room["coordinate"] = [x, y]
        # room["loot"] = {}
        # room["allowedDirections"] = {
        #     "north": True,
        #     "south": True,
        #     "west": True,
        #     "east": True
        # }
        # room["look"] = {
        #     "north": "",
        #     "south": "",
        #     "west": "",
        #     "east": ""
        # }
        # room["enemies"] = {}
        # room["radiation"] = 0

    json.dump(map, open("saves/template/map.json", "w"))
    map = json.load(open("saves/template/map.json"))

    map["rooms"]["x4y4"]["loot"] = {
        "floor": "geigerCounter",
        "lockers": "flashlight",
        "bodies": [
            "aglet",
            "aglet",
            "aglet"
        ]
    }
    map["rooms"]["x4y4"]["allowedDirections"] = {
        "north": True,
        "south": False,
        "west": False,
        "east": False
    }
    map["rooms"]["x4y4"]["look"] = {
        "north": "the vault door",
        "south": "a wall",
        "west": "a wall",
        "east": "a wall"
    }

    json.dump(map, open("saves/template/map.json", "w"))