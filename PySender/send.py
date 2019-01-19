import requests
import config
import sys

if len(sys.argv) != 3:
    print("USAGE: python3 send.py <message> <toNumber>")
    exit
else:
    message = sys.argv[1]
    toNumber = sys.argv[2]

#toNumber = "393332583936"
#message = "Messaggio di test"

payload = f"api_secret={config.api_secret}&api_key={config.api_key}&from={config.fromSender}&to={toNumber}&text={message}"
headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
}
print("Request to ", config.base_url + "?" + payload)

# response = requests.request(config.http_method, config.base_url,
#                            data=payload, headers=headers)

# print(response.text)
