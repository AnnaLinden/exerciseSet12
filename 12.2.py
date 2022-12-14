# Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a
# program that asks the user for the name of a municipality and then prints out the corresponding weather condition
# description text and temperature in Celsius degrees. Take a good look at the API documentation. You must register
# for the service to receive the API key required for making API requests. Furthermore, find out how you can convert
# Kelvin degrees into Celsius.

import requests


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def get_city_name():
    city = input("Enter the name of the city: ")
    return city


def get_temp_in_kelvin(city,key):
    request = "https://api.openweathermap.org/data/2.5/weather?q=" + city + f"&APPID={key}"
    response = requests.get(request).json()
    kelvin = response['main']['temp']
    return kelvin


city = get_city_name()
key = input("Enter your API key: ")
celsius = kelvin_to_celsius(get_temp_in_kelvin(city,key))
print(f"The temperature in {city} is {round(celsius, 1)} degrees Celsius.")
