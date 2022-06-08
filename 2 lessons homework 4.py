import time
from json.decoder import JSONDecodeError
import requests
import json
import urllib3

my_url = "https://playground.learnqa.ru/ajax/api/longtime_job"
# headers = {'Authorization': 'my_Token'}
# cookies = {'session': 'cookies'}


response = requests.get(my_url)
cookie_value = response.cookies.get('token')
# print(cookie_value)
# print(response.text)

parsed_response_text = response.json()
my_Token = parsed_response_text["token"]
my_Time = parsed_response_text["seconds"]

if my_Token in parsed_response_text["token"]:
    print("No job linked to this token")
else:
    print(f"{my_Token} is true")

# print(my_Token)
# print(my_Time)

response_post = requests.post(my_url, cookies={"token": my_Token})
print(response_post.status_code)
print(response_post.text)
#
# if key in obj:
#     print(obj[key])
# else:
#     print(f"Ключи {key} в JSON нет")


time.sleep(my_Time)
response_post = requests.post(my_url, data={"token": my_Token})
print(response_post.status_code)