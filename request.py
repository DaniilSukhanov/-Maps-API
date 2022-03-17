import requests
from PyQt5.QtGui import QPixmap
import const


def get_map_image(ll, spn, map_type, point=None):
    params = {
        'll': ll,
        'spn': spn,
        'l': map_type,
    }
    if point is not None:
        params['pt'] = ','.join(
            map(
                str,
                point
            )
        ) + ',flag'
    response = requests.get(const.PREFIX_STATIC_MAPS, params=params)
    pixmap = QPixmap()
    pixmap.loadFromData(response.content)
    return pixmap

