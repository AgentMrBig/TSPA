# Trend Prediction App

This app trains a machine learning model on historical time series data to predict the start of a trend and its duration.

## Overview

The app is designed in a modular fashion, with different components handling specific tasks. The main components are:

1. Data input and processing
2. Training and prediction
3. Visualization of results

## Components

### 1. Data input and processing

- **data_processing.py**: Responsible for loading the CSV data, cleaning it, and preparing it for machine learning. The data columns include Gmt time, Open, High, Low, Close, and Volume.

### 2. Training and prediction

- **feature_engineering.py**: Generates features to be used in training the machine learning model. This includes creating moving averages, technical indicators, and other relevant features.

- **model_training.py**: Uses the prepared data and engineered features to train a machine learning model for trend prediction. The model predicts the first candle that starts the trend and the closing price when the trend is expected to end.

### 3. Visualization of results

- **app.py**: A Python web server that uses Flask to run the app. This server integrates the data processing, feature engineering, and model training components.

- **visualization.py**: Responsible for displaying the results of the training, including the model's accuracy and a visualization of the model's performance on the last 25% of the training data.

## Usage

To use the app, simply run `python app.py` and navigate to the specified URL in your browser. The app will display the training results, model accuracy, and a visualization of the model's performance on the last 25% of the training data.
