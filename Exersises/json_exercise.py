import json

data = {"name": "Santo", "age": 25}

json_string = json.dumps(data)

print(json_string)

py_list = ['apple','banana','cherry']
json_string = json.dumps(py_list)
json_list = json.loads(json_string)
print(json_list)
print(json_string)