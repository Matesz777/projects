import requests

api_key = "0522397835574c67ba272320252404"
city = "London"
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&lang=pl"

response = requests.get(url)
dane = response.json()

print(f"Pogoda w {dane['location']['name']}:")
print(f"Temperatura: {dane['current']['temp_c']}°C")
print(f"Warunki: {dane['current']['condition']['text']}")
