import requests
import json

# Создание простого тела запроса
payload = {"name": "User"}
response_get = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
response_post = requests.get("https://playground.learnqa.ru/api/check_type", data={"peram1":"value1"})
response_delete = requests.delete("https://playground.learnqa.ru/api/check_type", data={"peram1":"value1"})
response_put = requests.put("https://playground.learnqa.ru/api/check_type", data={"peram1":"value1"})


print(response_get.text)
print(response_get.status_code)

# Разбор URL Длинный редирект

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
# second_response = response.history[1]
third_response = response

print(first_response.url)
# print(second_response.url)
print(third_response.url)



# Парсинг json
string_as_json_format = '{"answer": "Hellowww, User"}'
obj = json.loads(string_as_json_format)
key = "answer2"

if key in obj:
    print(obj[key])
else:
    print(f"Ключи {key} в JSON нет")