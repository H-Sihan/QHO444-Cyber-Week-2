import requests
import json

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=0b3bdd00fa307fd362a0bce74e85ccf7")
data = response.json()

with open("output_request.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

json_file.close()