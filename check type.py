import requests



response = requests.get("https://playground.learnqa.ru/api/check_type", params={"peram1":"value1"})
print(response.text)
print(response.status_code)

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"peram1":"value1"})
print(response.text)

response = requests.delete("https://playground.learnqa.ru/api/check_type", data={"peram1":"value1"})
print(response.text)

response = requests.put("https://playground.learnqa.ru/api/check_type", data={"peram1":"value1"})
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
# second_response = response.history[1]
third_response = response

print(first_response.url)
# print(second_response.url)
print(third_response.url)