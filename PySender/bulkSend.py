import requests
import config
import sys
import numpy as np
import time

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print("USAGE: python3 bulkSend.py <message> [<numbersFile>]")
    sys.exit()
elif len(sys.argv) == 2:
    message = sys.argv[1]
    numbersFile = "numbers.npy"
elif len(sys.argv) == 3:
    message = sys.argv[1]
    numbersFile = sys.argv[2]
count = 0
numbers = np.load(numbersFile)
headers = {
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
}
apiPayload = config.apiPayload
numberField = config.numberField
messageField = config.messageField
start = time.time()
for number in numbers:
    payload = f"{config.apiPayload}&{numberField}={number}&{messageField}={message}"
    # print("Request to ", config.base_url + "?" + payload)
    try:
        for attempt in range(config.attemptsPerEachMessage):
            response = requests.request(config.http_method, config.base_url,
                                        data=payload, headers=headers)
            json = response.json()
            if json[config.responseStatusField] == 0:
                count += 1
                break
        else:
            raise Exception("")
    except Exception as e:
        print(f"{config.sendErrorMessage} {number}")

duration = time.time() - start
print(f"{count} {config.bulkSendResultMessage} {len(numbers)} in {duration} sec.")
