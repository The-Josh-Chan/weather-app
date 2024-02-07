import sqlite3

def insert_into_table(weather_df, cursor, connection, user_location):
    weather_tuple_list = []
    for date, values in weather_df.iterrows():
        weather_tuple_list += [(date, values["T2M"])]
    cursor.executemany(f"insert into {user_location} values (?,?)", weather_tuple_list)
    connection.commit()
    print(f"{user_location} weathter data has been updated, use search_city function to view updated weather data table")

def check_city(city, db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    try:
        cursor.execute(f"select * from {city}")
        connection.close()
        return True
    except: 
        connection.close()
        return False

def search_city(city):
    connection = sqlite3.connect("weather_data.db")
    cursor = connection.cursor()
    try:
        cursor.execute(f"PRAGMA table_info({city})")
        columns_info = cursor.fetchall()
        column_names = []
        for column in columns_info:
            column_names.append(column[1])
        cursor.execute(f"select * from {city}")
        tuple_list = cursor.fetchall()
        connection.close()
        return tuple_list, column_names
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
    if weather_df.empty:
        print("API call returned empty data. Try again.")
        cursor.close()
        return False
    cursor.execute(f"create table {user_location} (date integer, temperature_2m integer)")
    insert_into_table(weather_df, cursor, connection, user_location)
    connection.close()

def update_city(user_location, weather_df):
    connection = sqlite3.connect("weather_data.db")
    cursor = connection.cursor()
    if check_city(user_location, "weather_data.db") == True:
        insert_into_table(weather_df, cursor, connection, user_location)
        connection.close()
    else:
        cursor.execute(f"create table {user_location} (date integer, temperature_2m integer)")
        insert_into_table(weather_df, cursor, connection, user_location)
        print(f"{user_location} table has been created and updated, use search_city function to view updated weather data table")
        connection.close()

def delete_invalid_data(user_location, column, data):
    connection = sqlite3.connect("weather_data.db")
    cursor = connection.cursor()
    if check_city(user_location, "weather_data.db") == True:
        try:
            cursor.execute(f"DELETE from {user_location} WHERE {column} = {data}")
            connection.commit()
            print("Data deleted successfully.")
        except sqlite3.Error as e:
            print("Error deleting data:", e)
        finally:
            cursor.close()

def get_data(user_location, column, data):
    connection = sqlite3.connect("weather_data.db")
    cursor = connection.cursor()
    if check_city(user_location, "weather_data.db") == True:
        try:
            cursor.execute(f"SELECT date, temperature_2m FROM {user_location} WHERE {column} = {data}")
            tuple_list = cursor.fetchall()
            connection.close()
            return tuple_list
        except sqlite3.Error as e:
            print("Error selecting data:", e)
            return False

            

