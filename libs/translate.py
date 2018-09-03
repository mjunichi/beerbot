def mention(message, query):
    from googletrans import Translator
    import re

    translator = Translator()
    if re.search('[あ-んア-ン一-龥]', query):
        translated = translator.translate(query)
    else:
        translated = translator.translate(query, dest='ja')

    message.send('>' + translated.text)
