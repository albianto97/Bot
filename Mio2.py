import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
 
from pprint import pprint
import time
import datetime
import json
from urllib2 import urlopen
 
 
TOKEN="666243794:AAFG3Ww-snpsCBJEZikIOBMLahNYyyOl1ig" #da sostituire
 
def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	name = msg["from"]["first_name"]
       	txt = msg['text']
	if txt.startswith('/start'):
            	bot.sendMessage(chat_id, 'ciao {}, sono un bot molto stupido!'.format(name))
	elif txt.startswith('/elenco'):
		keyboard = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text='IP', callback_data='ip'),
                     InlineKeyboardButton(text='Info', callback_data='info')],
                     [InlineKeyboardButton(text='Time', callback_data='time')]
                 ])
	elif txt.startswith('/help'):
            bot.sendMessage(chat_id, 'Ecco i comandi che capisco:\n - /elenco\n - /start\n - /conti')
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
	bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)
	
    	
def on_callback_query(msg):
	query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
	print('Callback Query:', query_id, chat_id, query_data)
	if query_data=='ip':
		my_ip = urlopen('http://ip.42.pl/raw').read()
		bot.sendMessage(chat_id, my_ip)
	elif query_data=='info':
		info=json.dumps(bot.getUpdates(),sort_keys=True, indent=4)
		bot.sendMessage(chat_id, info)
	elif query_data=='time':
		ts = time.time()
		bot.answerCallbackQuery(query_id, text=datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')) #messaggio a comparsa


 
 
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
				  'callback_query': on_callback_query}).run_as_thread() 
print('Listening ...')
 
 
while 1:
	time.sleep(10)
