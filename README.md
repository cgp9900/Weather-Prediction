# Weather-Prediction

The Weather-Prediction project aims to utilize recent hourly temperature data and traditional SARIMA forecasting methods to provide a 7 day forecast of future temperatures for Atlanta, GA. Statistical methods are utilized throughout the project focusing on stationarity and residual diagnostics, and the AICc method is used to judge the quality of similar models. 

The data is gathered via the [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api/). This is a robust, free API that allows for retrieval of multiple variables at the hourly or daily grain. 

Step by Step Project Explanation: 

1. Required Imports
    
     Importing all necessary modules - includes pandas, numpy, several statsmodels, and modules to aid with the API call. 

2. API Call
     
     Using the API_process function to retrieve the weather data from the Open-Meteo API. The amount of historical data gathered is controlled by two dynamic variables which pull hourly points starting from 60 days previous to the current day through 2 days previous the current day.

     The hourly data is visualized to get a first look at the dynamics of the time series. 

3. Statistical Diagnostic Steps

     The project aims to use both an auto Arima and visualization/statistical techniques to choose the best SARIMA model. ACF and PACF plots along with ADF Statistics are used to analyze the stationarity of the data, and seasonal and traditional differencing are introduced. 

     These plots, once stationarity is invoked, are used separately to estimate the AR() and MA() components of the model. 

4. Modeling 

     Each of the possible estimated models are trained and fitted, along with an auto Arima to determine if a better model can be found through more computationally heavy processes (non-stepwise). Surprisingly, one of the models chosen by the graphical estimates performs better than the auto Arima when judging by the AICc. 

5. Residual Analysis

     To determine the robustness of the model, and if there is any remaining information that the model is missing, residuals are analyzed through diagnostic plots. A focus is placed on the correlations of the residuals by using the Ljung-Box test. 

6. Predictions and Forecasting

     The data is split into the tradition train/test pieces and the model evaluated with RMSE and visualized with observed values and confidence intervals. A 7-day forecast is then made on the entire set of data and visualized with corresponding confidence intervals. 

     
## Usage

The bulk of the project is within an .ipynb file to provide insight into statistical results and visualizations. Directory: Weather-Prediction/weather/Weather Analysis.ipynb.

Two custom functions are used in this project which can be found in the Weather-Prediction/utils/ directory.

To get started, first clone the repository. This will download a copy of the repository in your current working directory. 

```python
$ git clone https://github.com/cgp9900/Weather-Prediction.git
```
After this, navigate to the .ipynb file and run the code. In the section for training and fitting the model, it is normal for this code to take ~20-25 minutes to complete. This is due to the hyperparameters selected for the auto Arima, which is meant to search for a large number of possible models for best selection.
