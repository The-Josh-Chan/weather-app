import pandas as pd
from api_handling import weather_api
from db_handler import db_handler
import cmd

class WeatherStation(cmd.Cmd):
    def do_create_city_table(self, line):
        user_location = input(" location: ")
        weather_data = weather_api.fetch_weather_data(user_location)
        weather_df = pd.DataFrame(weather_data)
        # weather_df is a pandas dataframe with timestamps as keys and parameters as columns
        # Upload data to database
        db_handler.create_location_db(user_location, weather_df)
        return False

    def do_search_city(self, line):
        user_location = input(" City: ")
        weather_data_tuple, weather_data_columns = db_handler.search_city(user_location)
        # Take Weather data from sqlite3 database and process to look readable
        if weather_data_tuple == False:
            return False
        else:
            weather_df = pd.DataFrame(weather_data_tuple, columns = weather_data_columns)
            print(weather_df)
            return False

    def do_load_old_weather(self, line):
        user_location = input(" City: ")
        start_date = input(" Start Date (YYYYMMDD): ")
        end_date = input(" End Date (YYYYMMDD): ")
        weather_data = weather_api.fetch_weather_data_date_range(user_location, start_date, end_date)
        weather_df = pd.DataFrame(weather_data)
        db_handler.update_city(user_location, weather_df)

    def do_delete_data(self, line):
        print("Which city do you want to delete data from? ")
        user_location = input()
        weather_data_tuple, weather_data_columns = db_handler.search_city(user_location)
        weather_df = pd.DataFrame(weather_data_tuple, columns = weather_data_columns)
        print(weather_df.head())
        print("What column of data do you want to reference to delete data? ")
        column = input()
        print("What does the data look like in the column? ")
        data = input()
        print(f"Are you sure you want to delete data rows that contain {data} in the {column} column? Y/N")
        confirm = input()
        if confirm.lower() == "y" or confirm.lower() == "yes":
            db_handler.delete_invalid_data(user_location, column, data)
        else:
            print("You did not confirm with YES, data will not be deleted, cheerios! ")
            return False
        
    def do_select_range(self, line):
        print("Which city do you want to select data from?")
        user_location = input()
        weather_data_tuple, weather_data_columns = db_handler.search_city(user_location)
        weather_df = pd.DataFrame(weather_data_tuple, columns = weather_data_columns)
        print(weather_df.head())
        print("What column of data do you want to use as reference? ")
        column = input()
        print("What does the data look like in the column? ")
        data = input()
        tuple_list = db_handler.get_data(user_location, column, data)
        if tuple_list == False:
            print("Error selecting data range")
            return False
        else:
            weather_df = pd.DataFrame(tuple_list)
            print(weather_df)

if __name__ == "__main__":
    WeatherStation().cmdloop()