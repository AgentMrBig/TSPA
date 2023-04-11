import pandas as pd

# Read the CSV file
file_path = 'path/to/your/csv_file.csv'
data = pd.read_csv(file_path)

# Parse the date column and set it as index
data['Gmt time'] = pd.to_datetime(data['Gmt time'])
data.set_index('Gmt time', inplace=True)

# Resample the data into different timeframes if needed
data_5min = data.resample('5T').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
data_15min = data.resample('15T').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
data_30min = data.resample('30T').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
