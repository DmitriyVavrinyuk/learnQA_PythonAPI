from json.decoder import JSONDecodeError
import requests
import json
import urllib3


# 2 задание

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
# print(response.text)

first_response = response.history[0]
second_response = response.history[1]
# third_response = response.history[2]
i = 0

try:
    while i < 3:
        print(response.history[i])
        i = i + 1

except JSONDecodeError:
    print("response is not JSON format")



print(first_response.url)
print(second_response.url)
# print(third_response.url)