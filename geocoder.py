import requests
import const


# Возвращает объект по адресу.
def geocode(address):
    params = {
        'apikey': const.API_KEY_GEOCODE,
        'geocode': address,
        'format': 'json'
    }
    response = requests.get(const.PREFIX_GEOCODE_MAPS, params=params)
    if response:
        json_response = response.json()
    else:
        raise RuntimeError(
            """Ошибка выполнения запроса: {request}
            Http статус: {status} ({reason})""".format(
                request=params['geocode'],
                status=response.status_code,
                reason=response.reason)
        )
    features = (
        json_response["response"]['GeoObjectCollection']
        ['featureMember']
    )
    return features[0]['GeoObject'] if features else None


# Возвращает координаты по заданному адресу.
def get_coordinates(address):
    toponym = geocode(address)
    if toponym is None:
        return None
    toponym_coords = toponym['Point']['pos']
    toponym_latt, toponym_long = toponym_coords.split()
    return float(toponym_latt), float(toponym_long)


# получение постового индекса.
def get_postcode(address):
    toponym = geocode(address)
    if toponym is None:
        raise KeyError()
    return (
        toponym['metaDataProperty']['GeocoderMetaData']['Address']
        ['postal_code']
    )


def get_ll_span(address):
    long, latt = get_coordinates(address)
    ll = ','.join((str(long), str(latt)))
    toponym = geocode(address)
    envelope = toponym['boundedBy']['Envelope']
    left, bottom = map(float, envelope['lowerCorner'].split())
    right, top = map(float, envelope['upperCorner'].split())
    dx = abs(right - left) / 2
    dy = abs(top - bottom) / 2
    span = f'{dx},{dy}'
    return ll, span
