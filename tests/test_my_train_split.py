import numpy as np
import pandas as pd
import pytest

from utils import my_train_split


def test_my_train_split_sorted_dates_X_train():
    X = pd.date_range("2023-12-01T05:00:00.000Z", "2023-12-10T23:00:00.000Z", freq="h")
    y = np.random.randn(235)
    X_train, X_test, y_train, y_test = my_train_split.my_train_split(X, y)
    assert X_train[::-1][0] == pd.Timestamp("2023-12-09T00", tz="UTC")


def test_my_train_split_sorted_dates_X_train():
    X = pd.date_range("2023-12-01T05:00:00.000Z", "2023-12-10T23:00:00.000Z", freq="h")
    y = np.random.randn(235)
    X_train, X_test, y_train, y_test = my_train_split.my_train_split(X, y)
    assert X_test[::-1][0] == pd.Timestamp("2023-12-10T23", tz="UTC")
