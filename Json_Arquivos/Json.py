import json

# JSON para python
x = '{"name": "John", "age": 23}'

#  load() em arquivos
y = json.loads(x)

print(y["age"])

# Python para JSON
x = {"name": "John", "age": 23}

#  dump() em arquivos
y = json.dumps(x) 

print(y["age"])