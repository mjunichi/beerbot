def mention(message, query):
    import random
    stores = ['kanda', 'mitsukoshimae']
    store = random.choice(stores)
    for query in stores:
        store = query
        break

    message.send(
        'http://www.craftbeermarket.jp/todaysmenu/dm_' + store + '.jpg?' + str(random.randint(1, 10000)))
