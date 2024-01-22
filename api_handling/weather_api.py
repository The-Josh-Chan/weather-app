import requests
from geopy.geocoders import Nominatim

def fetch_weather_data(city):
    geolocator = Nominatim(user_agent="weather_app")
    try:
        location = geolocator.geocode(city)
    except:
        print("Geolocator Error")
        print("Input Logitude and Latitude: ")
        long = input(" Longitude: ")
        lat = input(" Latitude: ")
        result = requests.get(f"https://power.larc.nasa.gov/api/temporal/monthly/point?parameters=T2M_MIN,T2M_MAX,T2M&community=SB&longitude={long}&latitude={lat}&format=json&start=2022&end=2022").json()
        return result
    try:
        result = requests.get(f"https://power.larc.nasa.gov/api/temporal/monthly/point?parameters=T2M_MIN,T2M_MAX,T2M&community=SB&longitude={location.longitude}&latitude={location.latitude}&format=json&start=2022&end=2022").json()
    #,T2M_MAX,T2M_MIN,CLOUD_AMT_DAY,PRECSNO,TQV
    except:
        print("API Call error...")
    return result
