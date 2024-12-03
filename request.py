import requests
import time

url = "http://localhost:5000/"

payload = {}
headers = {}

while True:
    response = requests.get(url, headers=headers, data=payload)
    print(response.text)
    time.sleep(0.01) 

