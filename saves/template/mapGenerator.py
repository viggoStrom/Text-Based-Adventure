import json

if input("Sure you wanna regenerate the map template? y/n \n ...") != "y":
    SystemExit
else:
    print("ok")

    map = json.load(open("saves/template/map.json"))

    columns = 9
    rows = 9

    map = {"rooms": {}}
    for y in range(0, rows):
        for x in range(0, columns):
            map["rooms"][f'x{x}y{y}'] = {}
            room = map["rooms"][f'x{x}y{y}']

            room["name"] = ""
            room["coordinate"] = [x, y]
            room["loot"] = {}
            room["allowedDirections"] = {
                "north": True,
                "south": True,
                "west": True,
                "east": True
            }
            room["look"] = {
                "north": "",
                "south": "",
                "west": "",
                "east": ""
            }
            room["enemies"] = {}
            room["radiation"] = 0

            pass

    map["meta"] = {
        "rows": rows,
        "columns": columns
    }

    startRoom = map["rooms"]["x4y4"]
    startRoom["loot"] = {
        "floor": "geigerCounter",
        "lockers": "flashlight",
        "bodies": [
            "aglet",
            "aglet",
            "aglet"
        ]
    }
    startRoom["allowedDirections"] = {
        "north": True,
        "south": False,
        "west": False,
        "east": False
    }
    startRoom["look"] = {
        "north": "the vault door",
        "south": "a wall",
        "west": "a wall",
        "east": "a wall"
    }

    json.dump(map, open("saves/template/map.json", "w"))
