import requests
from PyQt5.QtGui import QPixmap


PREFIX = 'https://static-maps.yandex.ru/1.x/?'
APIKEY = "40d1649f-0493-4b70-98ba-98533de7710b"


def get_map_image(ll, zoom, map_type='map'):
    params = {
        'll': ll,
        'z': zoom,
        'l': map_type,
        'key': APIKEY
    }
    response = requests.get(PREFIX, params=params)
    pixmap = QPixmap()
    pixmap.loadFromData(response.content)
    return pixmap

