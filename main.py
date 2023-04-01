import time
import random
import requests
import threading

THREAD_COUNT = 2
CHANNEL_ID = 1076805766847135864
MESSAGE_ID = 1091773165128142939
BREAD_CRUMBS = [3, 11, 39]

headers = {
    "authorization": ""
}


def main():
    while True:
        data = {
            "version": "1.0",
            "variant": "3",
            "language": "en",
            "breadcrumbs": BREAD_CRUMBS,
            "elements": {},
            "name": "message",
            "channel_id": str(CHANNEL_ID),
            "message_id": str(MESSAGE_ID)
        }
        response = requests.post("https://discord.com/api/v9/reporting/message", headers=headers, json=data)
        response_json = response.json()

        if response.status_code == 429:
            color = f'\033[38;2;{random.randint(0, 255)};{random.randint(0, 255)};{random.randint(0, 255)}m'
            print(f"{color}Rate Limited -> {response_json['retry_after']}s")
            time.sleep(response_json['retry_after'])
        else:
            color = f'\033[38;2;{random.randint(0, 255)};{random.randint(0, 255)};{random.randint(0, 255)}m'
            print(f"{color}Reported -> {response_json['report_id']}")


for num in range(THREAD_COUNT):
    threading.Thread(target=main).start()
    print(f"Started Thread {num + 1}")
