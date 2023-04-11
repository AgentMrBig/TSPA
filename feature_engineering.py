import numpy as np

def create_features(data, window_size=10):
    # Moving averages
    data['MA'] = data['Close'].rolling(window=window_size).mean()

    # Exponential moving averages
    data['EMA'] = data['Close'].ewm(span=window_size).mean()

    # Relative Strength Index (RSI)
    delta = data['Close'].diff()
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)
    avg_gain = gains.rolling(window=window_size).mean()
    avg_loss = losses.rolling(window=window_size).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # MACD (Moving Average Convergence Divergence)
    short_ema = data['Close'].ewm(span=12).mean()
    long_ema = data['Close'].ewm(span=26).mean()
    data['MACD'] = short_ema - long_ema
    data['Signal'] = data['MACD'].ewm(span=9).mean()

    # Drop rows with NaN values
    data.dropna(inplace=True)

    return data

# Create features for each time frame
window_size = 10
data_5min_features = create_features(data_5min, window_size)
data_15min_features = create_features(data_15min, window_size)
data_30min_features = create_features(data_30min, window_size)
