import csv
from flask import Flask, request, jsonify
app = Flask(__name__)
from flask_cors import CORS
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly as py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from prophet.plot import add_changepoints_to_plot
from sklearn.metrics import mean_absolute_error

CORS(app)

@app.route('/', methods=['POST', 'GET'])
def main():
    for file in request.files.getlist('file'):
        data = pd.read_csv(file)
        data.isnull().sum()
        data.dropna(inplace=True)
        data.isnull().sum()

        ax = data.set_index('Date').plot(figsize=(12, 8))
        ax.set_ylabel('Income')
        ax.set_xlabel('Date')
        plt.show()

        my_model = Prophet(interval_width=0.95)
        data['Date'] = pd.DatetimeIndex(data['Date'])
        data.dtypes

        data = data.rename(columns={'Date': 'ds',
                        'Total': 'y'})
        my_model.fit(data)
        future_dates = my_model.make_future_dataframe(periods=24, freq='MS')
        future_dates.head()

        forecast = my_model.predict(future_dates)
        forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head()

        my_model.plot(forecast, uncertainty=True)
        my_model.plot_components(forecast)
        fig1 = my_model.plot_components(forecast)
        fig = my_model.plot(forecast)
        a = add_changepoints_to_plot(fig.gca(), my_model, forecast)
        my_model.changepoints

        pro_change= Prophet(changepoint_range=0.9)
        forecast = pro_change.fit(data).predict(future_dates)
        fig= pro_change.plot(forecast)
        a = add_changepoints_to_plot(fig.gca(), pro_change, forecast)
        plt.show()

        pro_change= Prophet(n_changepoints=20, yearly_seasonality=True)
        forecast = pro_change.fit(data).predict(future_dates)
        fig= pro_change.plot(forecast)
        a = add_changepoints_to_plot(fig.gca(), pro_change, forecast)
        plt.show()

        pro_change= Prophet(n_changepoints=20, yearly_seasonality=True)
        forecast = pro_change.fit(data).predict(future_dates)
        fig= pro_change.plot(forecast)
        a = add_changepoints_to_plot(fig.gca(), pro_change, forecast)
        plt.show()

        pro_change= Prophet(n_changepoints=20, yearly_seasonality=True, changepoint_prior_scale=0.001)
        forecast = pro_change.fit(data).predict(future_dates)
        fig= pro_change.plot(forecast)
        a = add_changepoints_to_plot(fig.gca(), pro_change, forecast)
        plt.show()

        forecast.info()
        forecast.drop(["trend_lower", "trend_upper", "additive_terms","additive_terms_lower","additive_terms_upper","yearly","yearly_lower","yearly_upper","multiplicative_terms","multiplicative_terms_lower","multiplicative_terms_upper","yhat"], inplace = True, axis = 1)
        forecast.columns
        forecast.info()
        # forecast.drop(["yhat_lower","yhat_upper"], inplace = True, axis = 1)
        forecast.columns
        forecast = forecast.rename(columns={'ds': 'Date',
                        'trend': 'Total'})

        forecast.head()

        # forecast.drop(["weekly", "weekly_lower", "weekly_upper"], inplace = True, axis = 1)

        train = forecast.drop(forecast.index[-36:])

        # y_true = data['y'].values
        # y_pred = train['tickets sold'].values
        # mae = mean_absolute_error(y_true, y_pred)
        # print('MAE: %.3f' % mae)
        data=forecast.to_csv('forecast.csv')
   
    #print("````", data)
    
    return "hello"


if __name__ == "_main_":
    app.run(debug=True)