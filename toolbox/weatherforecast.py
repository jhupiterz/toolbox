import sys
import requests

BASE_URI = "https://www.metaweather.com"

def search_city(query):
    query = query.lower()
    query = query.strip()
    url = f'{BASE_URI}/api/location/search/?query={query}'
    response = requests.get(url).json()
    if len(response) == 1:
        return response[0]
    if len(response) > 1:
        for index, city in enumerate(response):
            print(f"{index+1} - {city['title']}")
        query = int(input("Which city? (enter number):"))
        return response[query-1]
    print("Wrong entry, try again!")
    return None

def weather_forecast(woeid):
    url = f'{BASE_URI}/api/location/{woeid}/'
    response = requests.get(url).json()
    five_day_forecast = []
    for i in range(5):
        day_weather = ({"applicable_date": response["consolidated_weather"][i]["applicable_date"],
                        "weather": response["consolidated_weather"][i]["weather_state_name"],
                        "max_temp": response["consolidated_weather"][i]["max_temp"]})
        five_day_forecast.append(day_weather)
    return five_day_forecast