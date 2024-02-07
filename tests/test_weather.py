from weather import weather
import pytest

def test_weather():
    assert weather() == "weather"
