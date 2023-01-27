import requests
import sys


def getParameters():
    address = " ".join(sys.argv[1:])
    apiServer = "http://geocode-maps.yandex.ru/1.x/"
    params = {"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
              "geocode": address,
              "format": "json"}
    response = requests.get(apiServer, params=params)
    jsonResponse = response.json()
    toponym = jsonResponse["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    arr = [list(map(float, toponym["boundedBy"]["Envelope"]["lowerCorner"].split())),
           list(map(float, toponym["boundedBy"]["Envelope"]["upperCorner"].split()))]
    dx, dy = str(arr[1][0] - arr[0][0]), str(arr[1][1] - arr[0][1])
    longitude, lattitude = toponym["Point"]["pos"].split(" ")
    return longitude, lattitude, dx, dy
