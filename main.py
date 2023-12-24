from api_handling import weather_api

def load_data():
    user_location = input("Location: ")
    weather_data = weather_api.fetch_weather_data(user_location)
    return weather_data

# avg_temp = weather_data['T2M']
# temp_max = weather_data['T2M_MAX']
# temp_min = weather_data['T2M_MIN']
# cloud_coverage = weather_data['CLOUD_AMT_DAY']
# snow_amount = weather_data['PRECSNO']
# precipitation = weather_data['TQV']