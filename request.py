import requests
from PyQt5.QtGui import QPixmap
import const


def get_map_image(ll, spn, map_type):
    params = {
        'll': ll,
        'spn': spn,
        'l': map_type
    }
    response = requests.get(const.PREFIX, params=params)
    pixmap = QPixmap()
    pixmap.loadFromData(response.content)
    return pixmap

