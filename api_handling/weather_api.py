import requests
from geopy.geocoders import Nominatim
from datetime import datetime

def fetch_weather_data(city):
    geolocator = Nominatim(user_agent="weather_app")
    today = datetime.today().strftime("%Y%m%d")

    try:
        location = geolocator.geocode(city)
    except:
        print("Geolocator Error")
        print("Input Logitude and Latitude: ")
        long = input(" Longitude: ")
        lat = input(" Latitude: ")
        try:
            result = requests.get(f"https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=T2M&community=SB&longitude={long}&latitude={lat}&format=json&start={today}&end={today}").json()
            return result["properties"]['parameter']
        except:
            print("API Call error...")
            return False
    try:
        result = requests.get(f"https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=T2M&community=SB&longitude={location.longitude}&latitude={location.latitude}&format=json&start={today}&end={today}").json()
    #,T2M_MAX,T2M_MIN,CLOUD_AMT_DAY,PRECSNO,TQV
        return result["properties"]['parameter']
    except:
        print("API Call error...")
        return False
    

def fetch_weather_data_date_range(city, start_date, end_date):
    geolocator = Nominatim(user_agent="weather_app")
    try:
        location = geolocator.geocode(city)
    except:
        print("Geolocator Error")
        print("Input Logitude and Latitude: ")
        long = input(" Longitude: ")
        lat = input(" Latitude: ")
        try:
            result = requests.get(f"https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=T2M&community=SB&longitude={long}&latitude={lat}&format=json&start={start_date}&end={end_date}").json()
            return result["properties"]['parameter']
        except:
            print("API Call error...")
            return False    
    try:
        result = requests.get(f"https://power.larc.nasa.gov/api/temporal/hourly/point?parameters=T2M&community=SB&longitude={location.longitude}&latitude={location.latitude}&format=json&start={start_date}&end={end_date}").json()
    #,T2M_MAX,T2M_MIN,CLOUD_AMT_DAY,PRECSNO,TQV
        return result["properties"]['parameter']
    except:
        print("API Call error...")
        return False
