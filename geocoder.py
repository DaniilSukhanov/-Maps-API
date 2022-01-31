import requests

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


def geocode(address):
    api_server = 'http://geocode-maps.yandex.ru/1.x/?'
    params = {
        'apikey': API_KEY,
        'geocode': address,
        'format': 'json'
    }
    response = requests.get(api_server, params=params)
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


def get_coordinates(address):
    toponym = geocode(address)
    if not toponym:
        return None, None
    toponym_coords = toponym['Point']['pos']
    toponym_long, toponym_latt = toponym_coords.split()
    return float(toponym_long), float(toponym_long)


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

