from json.decoder import JSONDecodeError
import requests
import urllib3

# Как пользоваться try и except
response = requests.get("https://playground.learnqa.ru/api/get_text", params={"name": "user"})
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text["answer"])

except JSONDecodeError:
    print("response is not JSON format")


# Как пользоваться urllib3.PoolManager
http = urllib3.PoolManager()
value = "GET"
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
params = {"method": value}

response = http.request(i, url, fields=params)
print(response.data.decode('utf-8'))
print(f"Type request is = {value}, status is = {response.status}, answer = {response.data}, for method = {params}")
