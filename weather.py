import requests

API_KEY = "7d4465fb849a5c205ff25d6af11ddd81"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={"7d4465fb849a5c205ff25d6af11ddd81"
}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("\n------ Weather Report ------")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
    print("Humidity:", data["main"]["humidity"], "%")
    print("Wind Speed:", data["wind"]["speed"], "m/s")
else:
    print("Error:", data["message"])

