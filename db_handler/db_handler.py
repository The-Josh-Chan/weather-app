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
    except sqlite3.Error as err: 
        print(err, ": Use load_data to pull weather data into database and try again")
        connection.close()

def create_location_db(user_location, weather_df):
    connection = sqlite3.connect("weather_data.db")
    cursor = connection.cursor()
    # Create Table
    cursor.execute(f"create table {user_location} (date integer, temperature_min integer, temperature_max integer, temperature_2m integer)")
    weather_tuple_list = []
    for date, values in weather_df.iterrows():
        weather_tuple_list += [(date, values["T2M_MIN"], values["T2M_MAX"], values["T2M"])]
    print(weather_tuple_list)
    cursor.executemany(f"insert into {user_location} values (?,?,?,?)", weather_tuple_list)
    connection.commit()
    connection.close()