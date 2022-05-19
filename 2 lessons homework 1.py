from json.decoder import JSONDecodeError
import requests
import json
import urllib3


json_text = '{"messages":' \
            '[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},' \
            '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
json_text_format = json.loads(json_text)
print_text = json_text_format['messages']
# print_text_second = print_text[1]
# print(print_text_second['message'])

i = 0
for i in print_text:
    print(i['message'])







