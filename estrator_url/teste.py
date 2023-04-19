# import module
import json

# Data to be written
data = {
    "user": {
        "name": "satyam kumar",
        "age": 21,
        "Place": "Patna",
        "Blood group": "O+"
    }
}

# Serializing json and
# Writing json file
with open("datafile.json", "w") as write:
    json.dump(data, write)


f = open('datafile.json')
data1 = json.load(f)

for i in data['user']['name']:
    print(i)