import requests

print("Hello from Lyuba")

response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)