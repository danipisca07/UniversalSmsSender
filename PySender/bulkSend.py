import requests
import config
import sys
import numpy as np

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print("USAGE: python3 bulkSend.py <message> [<numbersFile>]")
    exit
elif len(sys.argv) == 2:
    message = sys.argv[1]
    numbersFile = "numbers.npy"
elif len(sys.argv) == 3:
    message = sys.argv[1]
    numbersFile = sys.argv[2]

settings = f"api_secret={config.api_secret}&api_key={config.api_key}&from={config.fromSender}"
numbers = np.load(numbersFile)
headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
}
for number in numbers:
    payload = f"{settings}&to={number}&text={message}"
    print("Request to ", config.base_url + "?" + payload)
#   response = requests.request(config.http_method, config.base_url,
#                            data=payload, headers=headers)
#   print(response.text)
