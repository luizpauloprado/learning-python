import json

list = [1, 2, 3, "simple", "list"]
print(json.dumps(list))

obj_example: dict = {"name": "Luiz", "age": 37}
print(json.dumps(obj_example))

json_person: str = (
    '{"name": "Charles", "age": 33, "has_hair": false, "hobbies": ["photography", "running"]}'
)
print(json.loads(json_person))
