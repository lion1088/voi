from pyttsx3 import speak
import requests

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import run_async, run_js

def weth():

    api_key = "780ef4f39aeaf0e2eadcb68bb90f0b11"
    url= "http://api.openweathermap.org/data/2.5/weather?"
    
    city_name = ('Moscow') 
    full_url = url+ "q=" + city_name + "&appid=" + api_key
    req= requests.get(full_url)
    info = req.json()
    if info["cod"] != "404": 
        x = info["main"] 
        current_temperature = x["temp"]
        tnc = round(float(current_temperature - 273.15),2)
        current_pressure = x["pressure"] 
        current_humidiy = x["humidity"] 
        z = info["weather"] 
        weather_description = z[0]["description"]
        s = info["wind"]
        speed = s["speed"]
        print()
        print("Температура: ", 
                   round(float(current_temperature - 273.15),2) , "°C",
                "\nАтмосферное давление : " +
                    str(current_pressure) + "hpa"
                "\nВлажность : " +
                    str(current_humidiy) + "%"
                "\nОписание: " +
                    str(weather_description).capitalize()+
                    "\nСкорость ветра :" + str(speed) + "m/s")
    else: 
        print(" City Not Found ")
         

    put_text("Температура: ", 
                   round(float(current_temperature - 273.15),2) , "°C")


if __name__ == 'main':
    start_server(weth)



