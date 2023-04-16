import pandas as pd
import numpy as np

def calculate_moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

def calculate_rsi(data, window):
    delta = data['Close'].diff()
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)
    avg_gain = gains.rolling(window=window).mean()
    avg_loss = losses.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def add_features(data, ma_window=14, rsi_window=14):
    data['MA'] = calculate_moving_average(data, ma_window)
    data['RSI'] = calculate_rsi(data, rsi_window)
    data.dropna(inplace=True)
    return data
