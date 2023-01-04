# import json
# import requests
import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter
# TOKEN = '5899257260:AAGaQBWFnjKt6Sa_oNe8kTCLw3TR1HV8p-U'
bot = telebot.TeleBot(TOKEN)
# bot = telebot.TeleBot('5899257260:AAGaQBWFnjKt6Sa_oNe8kTCLw3TR1HV8p-U')


# @bot.message_handler()
# def echo_test(message: telebot.types.Message):
#     bot.send_message(message.chat.id, 'hello')
#
# bot.polling()

# keys = {
#     'биткоин':'BTC',
#     'эфириум':'ETH',
#     'доллар':'USD',
# }

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionException('Слишком много параметров.')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
    # quote, base, amount = message.text.split(' ')
    # r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    # total_base = json.loads(r.content)[keys[base]]
       text = f'Цена {amount} {quote} в {base} - {total_base}'
       bot.send_message(message.chat.id, text)


bot.polling()



# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')
#
# import telebot
#
# TOKEN = "5899257260:AAGaQBWFnjKt6Sa_oNe8kTCLw3TR1HV8p-U"
#
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler('filters')
# def function_name(message):
#     bot.reply_to(message, "This is a message handler")