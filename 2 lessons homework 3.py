from json.decoder import JSONDecodeError
import requests
import json
import urllib3

# 3 задание

method = ["get", "post", "delete", "put", "options", "patch", "head", "trace"]
http = urllib3.PoolManager()
# payload = {"name": "User"}

for i in method:
    r = http.request(i, 'https://playground.learnqa.ru/ajax/api/compare_query_type')
    r.status
    # print(r)
    print(f'request method type = {i} status is {r.status} data {r.data} ')
    # print("\n")




# response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"peram":"value"})
# print(response_get.text)
# print(response_get.status_code)
#
# response_post = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"peram":"value"})
# print(response_post.text)
#
# response_delete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"peram1":"value1"})
# print(response_delete.text)
#
# response_put = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"peram1":"value1"})
# print(response_put.text)
#
# response_third = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"peram1":"value1"})
# print(response_third.text)
#
# response_third = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"peram1":"value1"})
# print(response_third.text)

