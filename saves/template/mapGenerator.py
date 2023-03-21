import json

if input("Sure you wanna regenerate the map template? y/n \n ...") != "y":
    SystemExit
else:
    print("ok")

    columns = 5
    rows = 5

    # populate map with rooms from template
    map = json.load(open("saves/template/map.json", "r"))

    map = {"rooms": {}, "meta": {}}

    map["meta"] = {
        "rows": rows,
        "columns": columns,
        "template": {
            "name": "",
            "scenario": "",
            "scenarioRead": False,
            "loot": [],
            "allowedDirections": {
                "north": True,
                "south": True,
                "west": True,
                "east": True
            },
            "enemies": [],
        }
    }

    for y in range(0, rows):
        for x in range(0, columns):
            map["rooms"][f'x{x}y{y}'] = {}
            map["rooms"][f'x{x}y{y}'] = map["meta"]["template"]
            pass
        pass

    json.dump(map, open("saves/template/map.json", "w"))

    # starting room
    map = json.load(open("saves/template/map.json", "r"))

    map["rooms"]["x2y3"]["name"] = "the vault"
    map["rooms"]["x2y3"]["loot"] = {
        "floor": "geigerCounter",
        "lockers": "flashlight",
        "bodies": "aglet"
    }
    map["rooms"]["x2y3"]["allowedDirections"] = {
        "north": True,
        "south": False,
        "west": False,
        "east": False
    }

    json.dump(map, open("saves/template/map.json", "w"))


    # walls
    map = json.load(open("saves/template/map.json", "r"))

    maxX = map["meta"]["rows"]
    maxY = map["meta"]["columns"]

    for room in map["rooms"].keys():
        x = int(room[1])
        y = int(room[3])
        if x == 0:
            map["rooms"][room]["allowedDirections"]["west"] = False
            pass
        elif x == maxX-1:
            map["rooms"][room]["allowedDirections"]["east"] = False
            pass
        if y == 0:
            map["rooms"][room]["allowedDirections"]["north"] = False
            pass
        elif y == maxY-1:
            map["rooms"][room]["allowedDirections"]["south"] = False
            pass

    json.dump(map, open("saves/template/map.json", "w"))

    map = json.load(open("saves/template/map.json", "r"))

    map["rooms"]["x1y3"]["allowedDirections"]["east"] = False
    map["rooms"]["x3y3"]["allowedDirections"]["west"] = False
    map["rooms"]["x2y4"]["allowedDirections"]["north"] = False

    json.dump(map, open("saves/template/map.json", "w"))