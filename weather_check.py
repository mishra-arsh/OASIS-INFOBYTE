import requests

def get_weather(city_name):
    # This is my API Key of openweathermap
    api_key = "bb7dc3e5c84ae46414a6d534ae9ad165"  
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}"

    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather_description = weather_data["weather"][0]["description"]

        print(f"Please enter the weather in {city_name}:")
        print(f"Temperature in {city_name} is : {temperature} K")
        print(f"Humidity in {city_name} is : {humidity}%")
        print(f"Description: {weather_description}")
    else:
        print("Error fetching weather data. Please check the city name or try again later.")

if __name__ == "__main__":
    city_name = input("Enter a city name: ")
    get_weather(city_name)
