from datetime import datetime, timedelta

import openmeteo_requests
import pytest
import requests_cache
from retry_requests import retry

from weather import API_process


def test_API_process_number_of_nulls():
    cache_session = requests_cache.CachedSession(".cache", expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    prev_2_date = datetime.today() - timedelta(2)
    prev_2_date = prev_2_date.strftime("%Y-%m-%d")

    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "longitude": -84.3877,
        "latitude": 33.7488,
        "start_date": prev_2_date,
        "end_date": prev_2_date,
        "hourly": "temperature_2m",
        "temperature_unit": "fahrenheit",
        "timezone": "America/New_York",
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    with pytest.raises(Exception) as excinfo:
        test_df, test_df_orig = API_process.API_process(response)
    assert str(excinfo.value) == "Nulls surpass 5 percent level of the data"


def test_API_process_no_na():
    cache_session = requests_cache.CachedSession(".cache", expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    prev_2_date = datetime.today() - timedelta(2)
    prev_2_date = prev_2_date.strftime("%Y-%m-%d")

    prev_30_date = datetime.today() - timedelta(30)
    prev_30_date = prev_30_date.strftime("%Y-%m-%d")

    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "longitude": -84.3877,
        "latitude": 33.7488,
        "start_date": prev_30_date,
        "end_date": prev_2_date,
        "hourly": "temperature_2m",
        "temperature_unit": "fahrenheit",
        "timezone": "America/New_York",
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    test_df, test_df_orig = API_process.API_process(response)

    assert test_df.isnull().sum().sum() == 0


def test_API_process_date_range():
    cache_session = requests_cache.CachedSession(".cache", expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    prev_2_date = datetime.today() - timedelta(2)
    prev_2_date = prev_2_date.strftime("%Y-%m-%d")

    prev_30_date = datetime.today() - timedelta(30)
    prev_30_date = prev_30_date.strftime("%Y-%m-%d")

    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "longitude": -84.3877,
        "latitude": 33.7488,
        "start_date": prev_30_date,
        "end_date": prev_2_date,
        "hourly": "temperature_2m",
        "temperature_unit": "fahrenheit",
        "timezone": "America/New_York",
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    test_df, test_df_orig = API_process.API_process(response)

    assert test_df.isnull().sum().sum() == 0
