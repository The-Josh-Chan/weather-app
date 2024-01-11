import pandas as pd

def process_data(weather_data):
    processed_data = []
    parameters = weather_data["properties"]["parameter"]
    processed_data = pd.DataFrame(parameters)
    return processed_data 