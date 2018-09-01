def mention(message, query):
    import urllib
    import json

    url = 'https://rti-giken.jp/fhc/api/train_tetsudo/delay.json'
    html = urllib.request.urlopen(url)
    jsonfile = json.loads(html.read().decode('utf-8'))

    text = ""
    for json in jsonfile:
        name = json['name']
        company = json['company']
        text += company + "：" + name + "\n"

    message.send(text)
