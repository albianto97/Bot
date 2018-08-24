import telepot

TOKEN = '666243794:AAFG3Ww-snpsCBJEZikIOBMLahNYyyOl1ig'

def conti(*args):
    return sum(args), sum(args)/len(args)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        if txt.startswith('/start'):
            bot.sendMessage(chat_id, 'ciao {}, sono un bot molto stupido!'.format(name))
        elif txt.startswith('/help'):
            bot.sendMessage(chat_id, 'Ecco i comandi che capisco:\n - /start\n - /a\n - /conti')
	elif txt.startswith('/a'):
            bot.sendMessage(chat_id, 'Uffa...')
        elif txt.startswith('/conti'):
            params = txt.split()[1:]
            if len(params) == 0:
                bot.sendMessage(chat_id, 'Uso: /conti <parametri>.. Calcola la somma e la media dei numeri')
            else:
                try:
                    params = [float(param) for param in params]
                    somma, media = conti(*params)
                    bot.sendMessage(chat_id, 'Somma: {}, media {}'.format(somma, media))
                except:
                    bot.sendMessage(chat_id, 'Errore nei parametri, non hai inserito numeri!')
        else:
            bot.sendMessage(chat_id, 'Mi spiace {}, non capisco\nUsa /help per sapere cosa posso fare!'.format(name))

if __name__ == '__main__':
    bot = telepot.Bot(TOKEN)
    bot.message_loop(on_chat_message)

    print('Listening ...')

    import time
    while 1:
        time.sleep(10)
