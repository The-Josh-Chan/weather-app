import pandas as pd
from api_handling import weather_api
from data_processor import data_processor
from db_handler import db_handler
import cmd

class WeatherStation(cmd.Cmd):
    def do_create_city_table(self, line):
        user_location = input(" location: ")
        weather_data = weather_api.fetch_weather_data(user_location)
        weather_df = data_processor.process_data(weather_data)
        # weather_df is a pandas dataframe with timestamps as keys and parameters as columns
        # Upload data to database
        db_handler.create_location_db(user_location, weather_df)
        return False

    def do_search_city(self, line):
        user_location = input(" City: ")
        weather_data_tuple = db_handler.search_city(user_location)
        # Take Weather data from sqlite3 database and process to look readable
        if weather_data_tuple == False:
            return False
        else:
            weather_df = data_processor.process_data(weather_data_tuple)
            weather_df.rename(columns={'0':"Date", '1':"Average Temperature [C]"})
            print(weather_df)
            return False

    def do_load_old_weather(self, line):
        user_location = input(" City: ")
        start_date = input(" Start Date (YYYYMMDD): ")
        end_date = input(" End Date (YYYYMMDD): ")
        weather_data = weather_api.fetch_weather_data_date_range(user_location, start_date, end_date)
        weather_df = data_processor.process_data(weather_data)
        db_handler.update_city(user_location, weather_df)

if __name__ == "__main__":
    WeatherStation().cmdloop()