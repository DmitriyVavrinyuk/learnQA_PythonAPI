import time
from json.decoder import JSONDecodeError
import requests
import json
import urllib3

my_url = "https://playground.learnqa.ru/ajax/api/longtime_job"
# headers = {'Authorization': 'my_Token'}
# cookies = {'session': 'cookies'}


response = requests.get(my_url)
# cookie_value = response.cookies.get('token')
# print(cookie_value)
# print(response.text)

parsed_response_text = response.json()
my_Token = parsed_response_text["token"]
my_Time = parsed_response_text["seconds"]
# print(my_Token)
# print(my_Time)

if my_Token in parsed_response_text["token"]:
    print(f"{my_Token} is correct to this link")
else:
    print("No job linked to this token")

data = {"token": my_Token}

response_post = requests.post(my_url, data)
parsed_response_post = response_post.json()
status_response = parsed_response_post["status"]
print(f"status = '{status_response}', status code = '{response_post.status_code}'. Please wait {my_Time} seconds until the over process \n")

time.sleep(my_Time)
response_post = requests.post(my_url, data)
parsed_response_post = response_post.json()
status_response = parsed_response_post["status"]
result_response = parsed_response_post["result"]
print(f"status = '{status_response}', result = '{result_response}' and status code = '{response_post.status_code}'")