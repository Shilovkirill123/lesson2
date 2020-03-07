from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem, datetime
import logging


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater("958204140:AAHA21y19NDgyyzTYNJH4WsqQ9mfvY1X-3c", request_kwargs=PROXY)
    dp = mybot.dispatcher

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

planet = ['Mercury', 'Venus' ,'Mars' ,'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    if user_text in planet:
        x = getattr(ephem, user_text)(datetime.date.today())
        print(x)
        constellation = ephem.constellation(x)
        update.message.reply_text(f'{user_text} находится в созвездии {constellation}')

    elif user_text=='Pluto':
        update.message.reply_text('Плутон уже не планета')
    elif user_text == 'Earth':
        update.message.reply_text('Мы находимся на Земле')        
    else:
        update.message.reply_text('Введите название планеты')


main()