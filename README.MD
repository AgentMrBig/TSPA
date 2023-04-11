<pre>
<h1 align="center">Time Series Prediction App</h1>

<p align="center">
  <em>An app for predicting trends in time series data using machine learning models.</em>
</p>

## Table of Contents

- [Overview](#overview)
- [Components](#components)
  - [data_processing.py](#data_processingpy)
  - [feature_engineering.py](#feature_engineeringpy)
  - [train_evaluate.py](#train_evaluatepy)
  - [visualization.py](#visualizationpy)
  - [app.py](#apppy)
- [Installation](#installation)
- [Usage](#usage)

## Overview

The Time Series Prediction App is designed to be modular, simple to use, and easy to debug. It consists of the following components:

1. Data input and processing
2. Feature engineering and model training
3. Evaluation and visualization

These components are implemented in separate Python files, making the app easy to maintain and extend.

## Components

### `data_processing.py`

This file is responsible for reading and processing the input data in CSV format. It contains functions for loading the data, cleaning it, and preparing it for machine learning. The input data should have the following columns:

- Gmt time
- Open
- High
- Low
- Close
- Volume

### `feature_engineering.py`

This file is responsible for generating features that will be used to train the machine learning models. It contains functions for creating features based on the input data, such as moving averages, relative strength index (RSI), and other relevant indicators.

### `train_evaluate.py`

This file is responsible for training the machine learning models using the processed data and features. It contains functions for training models to predict trends, evaluating their performance, and saving the trained models. The models can be trained to predict trends at different time intervals, such as 5-minute, 15-minute, and 30-minute trends.

### `visualization.py`

This file is responsible for visualizing the results of the trained models. It contains functions for generating plots or charts that show the model's predictions and the actual data. The visualization helps users understand the model's performance and make informed decisions.

### `app.py`

This file contains the Flask server that ties together all the components of the app. The server provides endpoints for processing data, training and evaluating models, and displaying the results. The app uses the `data_processing.py`, `feature_engineering.py`, `train_evaluate.py`, and `visualization.py` files to create a complete web application.

## Installation

1. Install Python 3.7 or later.
2. Clone the repository.
3. Install the required packages using `pip install -r requirements.txt`.

## Usage

1. Run the Flask server using `python app.py`.
2. Open your web browser and navigate to `http://localhost:5000`.
3. Upload your CSV file with time series data.
4. Process the data, train the models, and visualize the results.
</pre>