# docomo API
#　user registration

import slackbot_settings
import json
import requests
import random
from _datetime import datetime
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger('beerbot')
settings = {}


def register():
    endpoint = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/registration?APIKEY=REGISTER_KEY'
    url = endpoint.replace(
        'REGISTER_KEY', slackbot_settings.DOCOMO_APP_ID)

    headers = {'Content-type': 'application/json'}
    payload = {
        "botId": "Chatting",
        "appKind": "Smart Phone"
    }
    r = requests.post(url,
                      data=json.dumps(payload), headers=headers)
    appId = r.json()['appId']
    return appId


def mention(message, query):
    username = message.user['name']
    if username not in settings.keys():
        setting = {}
        setting['appId'] = register()
        setting['appRecvTime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        setting['t'] = random.choice(['', 'kansai', 'akachan'])
        settings[username] = setting

    endpoint = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY=REGISTER_KEY'
    url = endpoint.replace(
        'REGISTER_KEY', slackbot_settings.DOCOMO_APP_ID)

    headers = {'Content-type': 'application/json;charset=UTF-8'}
    payload = {
        "language": "ja-JP",
        "botId": "Chatting",
        "appId": settings[username]['appId'],
        "voiceText": message.body['text'],
        "appRecvTime": settings[username]['appRecvTime'],
        "appSendTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "clientData": {
            "option": {
                "nickname": username,
                "mode": 'dialog',  # dialog or srtr
                "t": settings[username]['t']  # kansai or akachan
            }
        }
    }

    print(json.dumps(payload))
    # Transmission
    r = requests.post(url,
                      data=json.dumps(payload), headers=headers)
    data = r.json()

    response = data['systemText']['expression']

    logger.debug('[{user}]: {message}  [beer]: {response}'.format(
        user=username, message=message.body['text'], response=response))
    message.reply(response)
