from toolbox.weatherforecast import search_city
from toolbox.weatherforecast import weather_forecast

def test_search_city():
    assert len(search_city('Paris')) != 0

def test_five_day_forecast():
    assert len(weather_forecast(615702)) != 0