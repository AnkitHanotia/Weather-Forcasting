import requests

api_key = "5dbec145ab578a99f34f505b4511c571"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name: ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

data = response.json()

if data["cod"] != "404":
    # Extracting relevant data from API response
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    # Converting temperature from Kelvin to Celsius
    temp_celsius = temp - 273.15

    # Printing weather forecast
    print("Weather for", city_name)
    print("Description:", weather)
    print("Temperature:", round(temp_celsius, 1), "°C")
    print("Feels like:", round(feels_like - 273.15, 1), "°C")
    print("Humidity:", humidity, "%")
    print("Wind speed:", wind_speed, "m/s")
else:
    print("City not found.")
