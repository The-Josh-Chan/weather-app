import requests
from geopy.geocoders import Nominatim
# api_key = open('api_key.txt', 'r').read()

geolocator = Nominatim(user_agent="weather_app")
user_location = input("Location: ")
location = geolocator.geocode(user_location)

frequency = input(": ")

result = requests.get(f"https://power.larc.nasa.gov/api/temporal/monthly/point?parameters=T2M,T2M_MAX,T2M_MIN,CLOUD_AMT_DAY,PRECSNO,TQV&community=SB&longitude={location.longitude}&latitude={location.latitude}&format=json&start=2022&end=2022").json()

parameters = result["properties"]["parameter"]
avg_temp = parameters['T2M']
temp_max = parameters['T2M_MAX']
temp_min = parameters['T2M_MIN']
cloud_coverage = parameters['CLOUD_AMT_DAY']
snow_amount = parameters['PRECSNO']
precipitation = parameters['TQV']

