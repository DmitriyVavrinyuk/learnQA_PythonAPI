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

            params = {"method": j}
            response = http.request(i, url, fields=params)
            # print(response.data.decode('utf-8'))
            print(f"Type request is = {i}, status is = {response.status}, answer = {response.data}, for method = {params}")
    print("\n")

    # response_2 = requests.put(url, data={"method": "POST"})
    # print(response_2.text)


