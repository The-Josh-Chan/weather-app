import requests
from geopy.geocoders import Nominatim

def fetch_weather_data(city):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    try:
        result = requests.get(f"https://power.larc.nasa.gov/api/temporal/monthly/point?parameters=T2M_MIN,T2M_MAX,T2M&community=SB&longitude={location.longitude}&latitude={location.latitude}&format=json&start=2022&end=2022").json()
    #,T2M_MAX,T2M_MIN,CLOUD_AMT_DAY,PRECSNO,TQV
    except TimeoutError as err:
        print(err)
    return result
