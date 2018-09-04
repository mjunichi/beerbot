# coding: utf-8

from slackbot.bot import Bot

from logging import getLogger, StreamHandler, FileHandler, Formatter, DEBUG
logger = getLogger('beerbot')
format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler = FileHandler(filename='beerbot.log')
fileHandler.setLevel(DEBUG)
fileHandler.setFormatter(format)
logger.addHandler(fileHandler)

handler = StreamHandler()
handler.setLevel(DEBUG)
handler.setFormatter(format)
logger.addHandler(handler)

logger.setLevel(DEBUG)
logger.propagate = False


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
