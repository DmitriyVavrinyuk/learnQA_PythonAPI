from json.decoder import JSONDecodeError
import requests
import json
import urllib3


# 2 задание

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

# first_response = response.history[0]
# second_response = response.history[1]
# third_response = response.history[2]
i = 0
answer = ''

try:
    while answer != "https://playground.learnqa.ru":
        answer = response.history[i]
        print(answer.url)
        i += 1

except:
    print("history over")



# print(first_response.url)
# print(second_response.url)
# print(third_response.url)