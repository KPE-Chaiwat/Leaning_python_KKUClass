import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York","1":1234}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y["1"])
print(y)