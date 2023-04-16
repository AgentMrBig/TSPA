import pandas as pd
from datetime import datetime




def process_data(file_path):
    file_path = './training_data/USDJPY_Candlestick_1_Hour_BID_02.01.2022-05.04.2023.csv'
    data = pd.read_csv(file_path)


    # Parse the date column and set it as index
    data['Gmt time'] = pd.to_datetime(data['Gmt time'], format="%d.%m.%Y %H:%M:%S.%f")
    data.set_index('Gmt time', inplace=True)

    # Resample the data into different timeframes if needed
    data_5min = data.resample('5T').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
    data_15min = data.resample('15T').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
    data_30min = data.resample('30T').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})

    # Drop rows with missing values
    data_5min.dropna(inplace=True)
    data_15min.dropna(inplace=True)
    data_30min.dropna(inplace=True)

    return data_5min, data_15min, data_30min
