import requests 

endpoint = "http://127.0.0.1:8000/car/list/"

getResponse = requests.get(endpoint)

print(getResponse.json())
print(getResponse.status_code)
