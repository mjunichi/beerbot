from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from enum import Enum


@listen_to('beer')
def mention(message):
    message.react('ipa')


class RespondType(Enum):
    beer = 'beer'
    rain = '雨'
    image = 'img'
    train = '遅延'

    def toHelp(self):
        if self == RespondType.beer:
            return self.value + ' kanda|mitsukoshimae'
        elif self == RespondType.train:
            return self.value
        elif self == RespondType.rain:
            return self.value
        elif self == RespondType.image:
            return self.value + ' hub organic ipa'


@respond_to(r'.+')
def mention(message):
    from libs import beer
    from libs import rain
    from libs import image
    from libs import train

    query = ''
    commands = message.body['text'].split(' ')
    print(commands)
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
    else:
        help = 'available command is\n'
        for res in RespondType:
            help += res.toHelp() + '\n'

        message.send(help)
