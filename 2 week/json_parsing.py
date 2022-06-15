import json

string_as_json_format = '{"answer": "Hellowww, User"}'
obj = json.loads(string_as_json_format)


key = "answer2"

if key in obj:
    print(obj[key])
else:
    print(f"Ключи {key} в JSON нет")