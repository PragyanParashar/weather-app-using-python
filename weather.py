import requests
import json
from datetime import datetime

print("Weather Information")

def Time_Format_For_Localtion(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


def showWeather():
    api_key = "5b99c91ddfc4fd21489abee4d48cd509"
    cityName = input("Enter city name: ")
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q='+cityName+'&appid='+api_key
    Response = requests.get(weather_url)
    Weather_Info = Response.json()



#if api code = 200 ( It means that weather data succesfully)


    if Weather_Info['cod'] ==  200:
        kelvin = 273


        temp = int(Weather_Info['main']['temp'] - kelvin)
        pressure = Weather_Info['main']['pressure']
        humidity = Weather_Info['main']['humidity']
        sunrise = Weather_Info['sys']['sunrise']
        sunset = Weather_Info['sys']['sunset']
        timezone = Weather_Info['timezone']
        cloudy = Weather_Info['clouds']['all']
        description = Weather_Info['weather'][0]['description']

        sunrise_time = Time_Format_For_Localtion(sunrise + timezone)
        sunset_time = Time_Format_For_Localtion(sunset + timezone)

        weather_data = f"\nWeather of: {cityName}\nTemperature  (celsius):  {temp}°\nPressure: {pressure}  hpa\nHumidity :{humidity}% \nSunrise at {sunrise_time} and Sunset at {sunset_time} \nCloud: {cloudy}% \nInfo: {description} "
        print(weather_data)
    else:
        weather_data = f"\n\tWeather for '{cityName}' is not found!\n\tplease Enter Valid City Name"    

showWeather()

input()
