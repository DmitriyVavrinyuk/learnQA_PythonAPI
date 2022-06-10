from json.decoder import JSONDecodeError
import requests
import json
import urllib3

# 3 задание

http = urllib3.PoolManager()
value = ["GET", "POST", "DELETE", "PUT", "OPTIONS", "PATCH", "HEAD", "TRACE"]
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

for i in value:
    for j in value:
        if j == "GET":
            params = {"method": j}
        else:
            params = {"method": j}
        response = http.request(i, url, fields=params)
        # print(response.data.decode('utf-8'))
        print(f"Type request is = {i}, status is = {response.status}, answer = {response.data.decode('utf-8')}, for method = {params}")
    print("\n")






