from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from enum import Enum
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger('beerbot')


@listen_to('beer')
def mention(message):
    message.react('ipa')


class RespondType(Enum):
    beer = 'beer'
    rain = 'rain'
    image = 'img'
    train = 'train'
    translate = 'translate'
    help = 'help'

    def toHelp(self):
        if self == RespondType.beer:
            return self.value + ' kanda|mitsukoshimae'
        elif self == RespondType.train:
            return self.value
        elif self == RespondType.rain:
            return self.value + ' 東京'
        elif self == RespondType.image:
            return self.value + ' hub organic ipa'
        elif self == RespondType.translate:
            return self.value + ' 日本語でおｋ'
        elif self == RespondType.help:
            return self.value


@respond_to(r'.+')
def mention(message):
    from libs import beer
    from libs import rain
    from libs import image
    from libs import train
    from libs import translate
    from libs import ai

    query = ''
    commands = message.body['text'].split(' ')
    logger.debug(commands)
    command = commands[0]
    if len(commands) > 1:
        query = ','.join(commands[1:])

    print(query)

    if command == RespondType.beer.value:
        beer.mention(message, query)
    elif command == RespondType.train.value:
        train.mention(message, query)
    elif command == RespondType.rain.value:
        rain.mention(message, query)
    elif command == RespondType.image.value:
        image.mention(message, query)
    elif command == RespondType.translate.value:
        translate.mention(message, query)
    elif command == RespondType.help.value:
        help = '>>> usage\n'
        for res in RespondType:
            help += res.value + ': [' + res.toHelp() + ']\n'

        message.send(help)
    else:
        ai.mention(message, query)
