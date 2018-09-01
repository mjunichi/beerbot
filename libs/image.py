def mention(message, query):
    import bs4

    from urllib import request as req
    from urllib import error
    from urllib import parse

    urlKeyword = parse.quote(query)
    url = 'https://www.google.com/search?hl=jp&q=' + \
        urlKeyword + '&btnG=Google+Search&tbs=0&safe=on&tbm=isch'

    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0", }
    request = req.Request(url=url, headers=headers)
    page = req.urlopen(request)

    html = page.read().decode('utf-8')
    html = bs4.BeautifulSoup(html, "html.parser")
    elems = html.select('.rg_meta.notranslate')
    counter = 0
    for ele in elems:
        ele = ele.contents[0].replace('"', '').split(',')
        eledict = dict()
        for e in ele:
            num = e.find(':')
            eledict[e[0:num]] = e[num + 1:]
        imageURL = eledict['ou']

        message.send(imageURL)
        break
