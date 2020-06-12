import json

data = '''[ "Glenn", "Sally", "Jen" ]'''
info = json.loads(data)
print(len(info))
print(type(info))

data = '''
    { 
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    }
'''
info = json.loads(data)
print(len(info))
print(type(info))
