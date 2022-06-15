from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text", params={"name": "user"})
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text["answer"])

except JSONDecodeError:
    print("response is not JSON format")