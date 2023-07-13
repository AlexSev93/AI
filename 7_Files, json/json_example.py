import json


person = {
    'name': 'Max',
    'age': 10,
    'phones': ['8911', '73833']
}

in_json = json.dumps(person)
print(in_json)
print(type(in_json))

recov = json.loads(in_json)
print(recov)
print(type(recov))

# файлы также как pickle  только *.json, *.yml и без b чтения