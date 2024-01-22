import pandas as pd
from api_handling import weather_api
from data_processor import data_processor
from db_handler import db_handler
import cmd

class WeatherStation(cmd.Cmd):
    def do_load_data(self, line):
        user_location = input(" location: ")
        weather_data = weather_api.fetch_weather_data(user_location)
        print("Weather Data:", weather_data)
        weather_df = data_processor.process_data(weather_data)
        print("weather_df:", weather_df)
        # weather_df is a pandas dataframe with timestamps as keys and parameters as columns
        # Upload data to database
        db_handler.create_location_db(user_location, weather_df)
        return False

    def do_search_city(self, line):
        user_location = input(" City: ")
        weather_data = db_handler.search_city(user_location)
        return weather_data
    # Processed data is returned as a pandas DataFrame
    # process_data = data_processor.process_data(weather_data)

    # print(weather_data)
    # avg_temp = weather_data['T2M']
    # temp_max = weather_data['T2M_MAX']
    # temp_min = weather_data['T2M_MIN']
    # cloud_coverage = weather_data['CLOUD_AMT_DAY']
    # snow_amount = weather_data['PRECSNO']
    # precipitation = weather_data['TQV']

if __name__ == "__main__":
    WeatherStation().cmdloop()