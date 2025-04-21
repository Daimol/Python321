import requests

response = requests.get("https://www.google.com")
print(f"Status: {response.status_code}")