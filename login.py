import json
with open("data.json") as json_file:
    newDict=json.load(json_file)

for data in newDict:
    for key,value in data.items():
        print(f"{key} | {value}")
