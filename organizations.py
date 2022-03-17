import requests
import const


def organization(address):
    params = {
        'apikey': const.API_KEY_SEARCH,
        'text': address,
        'lang': 'ru_RU'
    }
    response = requests.get(
        const.PREFIX_SEARCH_MAPS,
        params=params
    )
    if response:
        json_response = response.json()
    else:
        raise RuntimeError(
            """Ошибка выполнения запроса: {request}
            Http статус: {status} ({reason})""".format(
                request=address,
                status=response.status_code,
                reason=response.reason
            )
        )
    feature = (
        json_response['features'][0]['properties']
    )
    return feature


def address_organization(address):
    toponym = organization(address)
    address = toponym['CompanyMetaData']['address']
    return address
