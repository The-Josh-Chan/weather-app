import pandas as pd

def process_data(weather_data):
    processed_data = pd.DataFrame(weather_data, columns=['date', 'Average Temperature'])
    return processed_data 