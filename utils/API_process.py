import numpy as np
import pandas as pd


def API_process(w_data):
    # Process hourly data. The order of variables needs to be the same as
    # requested.
    hourly = w_data.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {
        "date": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s"),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left",
        )
    }
    hourly_data["temperature_2m"] = hourly_temperature_2m

    # Check if we have a certain number of nulls - if not, drop them
    hourly_dataframe_stage = pd.DataFrame(data=hourly_data)
    rec_length = len(hourly_dataframe_stage)
    for rec in hourly_dataframe_stage.isna().sum():
        if rec > int(rec_length * 0.05):
            raise Exception("Nulls surpass 5 percent level of the data")
        else:
            pass
    hourly_dataframe_stage = hourly_dataframe_stage.dropna()

    # Code to check for and interpolate outliers
    hourly_numeric = hourly_dataframe_stage.select_dtypes(include=[np.number])
    q1 = hourly_numeric.quantile(0.25, numeric_only=True)
    q3 = hourly_numeric.quantile(0.75, numeric_only=True)
    IQR = q3 - q1

    hourly_numeric[
        (hourly_numeric >= (q3 + 1.5 * IQR)) | (hourly_numeric <= (q1 - 1.5 * IQR)) # pylint: disable=line-too-long
    ] = np.nan
    hourly_numeric.fillna(method="ffill", inplace=True)

    hourly_numeric_dated = pd.concat(
        [hourly_dataframe_stage.iloc[:, 0], hourly_numeric], axis=1
    )

    return hourly_numeric_dated, hourly_dataframe_stage
