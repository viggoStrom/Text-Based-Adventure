import json

map = json.load(open("saves/template/map.json"))

columns = 9
rows = 9

# row = ""
# map = {"rooms": {}}
# for y in range(0, rows):
#     for x in range(0, columns):
#         map["rooms"][f'x{x}y{y}'] = {}
#         map["rooms"][f'x{x}y{y}']["x"] = x
#         map["rooms"][f'x{x}y{y}']["y"] = y

#         row += f'[{x}, {y}] '
#         pass
#     print(row)
#     row = ""

# json.dump(map, open("saves/template/map.json", "w"))