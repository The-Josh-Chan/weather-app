import sqlite3

def check_city(city, db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    connection.close()

def search_city(city):
    connection = sqlite3.connect("weather_data.db")
    cursor = connection.cursor()
    try:
        cursor.execute(f"select * from {city}")
        tuple_list = cursor.fetchall()
        connection.close()
        return tuple_list
    except sqlite3.Error as err: 
        print(err, ": Use create_city_table to pull weather data into database and try again")
        connection.close()
        # Search city expects a return, if not able to search for city, return False
        tuple_list = False
        return tuple_list

def create_location_db(user_location, weather_df):
    connection = sqlite3.connect("weather_data.db")
    cursor = connection.cursor()
    # Create Table
    cursor.execute(f"create table {user_location} (date integer, temperature_2m integer)")
    weather_tuple_list = []
    for date, values in weather_df.iterrows():
        weather_tuple_list += [(date, values["T2M"])]
    cursor.executemany(f"insert into {user_location} values (?,?)", weather_tuple_list)
    connection.commit()
    connection.close()

def update_city(user_location, weather_df):
    connection = sqlite3.connect("weather_data.db")
    cursor = connection.cursor()
    weather_tuple_list = []
    for date, values in weather_df.iterrows():
        weather_tuple_list += [(date, values["T2M"])]
    cursor.executemany(f"insert into {user_location} values (?,?)", weather_tuple_list)
    connection.commit()
    print(f"{user_location} weathter data has been updated, use search_city function to view updated weather data table")
    connection.close()
