import requests
import os
import math
import pycristoforo
import json
from dotenv import load_dotenv

dotenv_path = ".env"
load_dotenv(dotenv_path)
MAP_API_KEY = os.environ.get("MAP_API_KEY")

# 8.681495,49.41461
# 8.687872,49.420318


def get_instructions(start, end):

    stepToInstruction = {}

    routeResponse = requests.get(
        "https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start={start_str}&end={end_str}".format(api_key=MAP_API_KEY, start_str=start, end_str=end)).json()

    steps = routeResponse['features'][0]['properties']['segments'][0]['steps']

    for step in steps:
        stepToInstruction[step["name"]] = step["instruction"]

    return stepToInstruction

# Latitude of Garching 	48.248872
# Longitude of Garching 	11.653248


def get_distance_in_metres(lat1, lon1, lat2, lon2):
    R = 6371e3  # metres
    φ1 = lat1 * math.pi/180  # φ, λ in radians
    φ2 = lat2 * math.pi/180
    Δφ = (lat2-lat1) * math.pi/180
    Δλ = (lon2-lon1) * math.pi/180

    a = math.sin(Δφ/2) * math.sin(Δφ/2) + math.cos(φ1) * \
        math.cos(φ2) * math.sin(Δλ/2) * math.sin(Δλ/2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # // in metres


def is_within_munich_circle(lat, lon):
    latitude = 48.137154
    longitude = 11.576124
    radius = 14000

    d = get_distance_in_metres(lat, lon, latitude, longitude)

    return d <= radius


def get_random_munich_coordinates():
    latitude = 48.137154
    longitude = 11.576124
    radius = 14000


country = pycristoforo.get_shape("Germany")
points = pycristoforo.geoloc_generation(country, 1000000, "Germany")

with open('./CourseInfo/germany_points.json', 'w') as outfile:
    json.dump(points, outfile)
