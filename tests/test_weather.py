import pytest

from weather import weather


def test_weather():
    assert weather() == "weather"
