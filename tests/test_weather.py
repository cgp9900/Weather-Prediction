from weather import weather


def test_weather():
    assert weather() == "weather"


def test_weather_uppercase():
    assert weather(True) == "WEATHER"
    