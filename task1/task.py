import psutil
import requests

LIMIT = 80
API_URL = "https://example.com/alarm"


def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent

    if memory_percent > LIMIT:
        payload = {"memory_percentage": memory_percent}
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            print("Alarm sent successfully")
        else:
            print("Failed to sent alarm. Status code:", response.status_code)
