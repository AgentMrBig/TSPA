from flask import Flask, render_template
from data_processing import process_data
from feature_engineering import add_features
from train_evaluate import train_model

app = Flask(__name__)

@app.route('/')
def index():
    file_path = './training_data/USDJPY_Candlestick_1_Hour_BID_02.01.2022-05.04.2023.csv'
    data_5min, data_15min, data_30min = process_data(file_path)

    # Add features to the data
    data_5min = add_features(data_5min)
    data_15min = add_features(data_15min)
    data_30min = add_features(data_30min)

    # Train and evaluate models
    mae_train_5min, mae_test_5min = train_model(data_5min, 'Close', 'model_5min.pkl')
    mae_train_15min, mae_test_15min = train_model(data_15min, 'Close', 'model_15min')
    mae_train_5min, mae_test_5min = train_model(data_5min, 'Close', 'model_5min.pkl')
    mae_train_15min, mae_test_15min = train_model(data_15min, 'Close', 'model_15min.pkl')
    mae_train_30min, mae_test_30min = train_model(data_30min, 'Close', 'model_30min.pkl')

    return render_template('index.html', mae_train_5min=mae_train_5min, mae_test_5min=mae_test_5min,
                           mae_train_15min=mae_train_15min, mae_test_15min=mae_test_15min,
                           mae_train_30min=mae_train_30min, mae_test_30min=mae_test_30min)

if __name__ == '__main__':
    app.run(debug=True)
