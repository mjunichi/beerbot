import requests
import slackbot_settings
from slackbot.bot import listen_to

GEO_API_ENDPOINT = 'https://map.yahooapis.jp/geocode/V1/geoCoder'
STATIC_MAP_API_ENDPOINT = 'https://map.yahooapis.jp/map/V1/static'


def mention(message, query):
    try:
        query = '東京' if query == "" else query
        lon, lat = get_coordinates(query)
        if lon == 0:
            message.send(query + 'が見つかりませんでした。他の地域でお試しください。')
            return
        map_content = get_rain_fall_image(lon, lat)
        with open('rain_fall.png', 'wb') as f:
            f.write(map_content)
        message.channel.upload_file(query, 'rain_fall.png')
    except TypeError as e:
        print(e)


def get_coordinates(query):
    params = {'appid': slackbot_settings.YAHOO_APP_ID,
              'query': query,
              'results': 1,
              'output': 'json'}
    r = requests.get(GEO_API_ENDPOINT, params=params)
    if r.json()['ResultInfo']['Total'] > 0:
        return r.json()['Feature'][0]['Geometry']['Coordinates'].split(',')
    return [0, 0]


def get_rain_fall_image(lon, lat):
    params = {'appid': slackbot_settings.YAHOO_APP_ID,
              'lon': lon,
              'lat': lat,
              'mode': 'map',
              'z': 15,
              'overlay': 'type:rainfall|datelabel:on'}
    r = requests.get(STATIC_MAP_API_ENDPOINT, params=params)
    return r.content
