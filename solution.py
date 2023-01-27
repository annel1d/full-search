import sys
from io import BytesIO

import requests
from PIL import Image
from getParams import getParameters


longitude, lattitude, dx, dy = getParameters()
map_params = {
    "ll": ",".join([longitude, lattitude]),
    "spn": ",".join([dx, dy]),
    "pt": "{}, pm2dgl".format("{}, {}".format(longitude, lattitude)),
    "l": "sat"
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(response.content)).show()
