import json

#sample python object
data = {"name": "Arisu", "age": 30, "city": "Kampla"}

#serialize the obj to a python string
json_string = json.dumps(data)


# Serialize and write to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
