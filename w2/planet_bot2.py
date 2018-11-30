from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime

#adding a proxy
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format = "%(asctime)s - %(levelname)s - %(message)s",
                    level = logging.INFO, 
                    filename = "kk_new_bot.log"
                    )

#def greet_user(bot, update):
    #text = "Вызван старт"
    #print(text) #or I could put logging.info(text) here
    #update.message.reply_text(text)

planet_list = ["Mercury", "Venus", "Earth", 
"Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def what_planet(planet_bot, update): #параметра обязательно нужно два. Первого принято называть bot
    pechenka = update.message.text
    #print(pechenka)
    pechenka_popolam = pechenka.split()
    pech_pop_planet = pechenka_popolam[1]
    pechenka_popolam_s_datoy = ephem.
    
    print(ephem.constellation(pechenka_popolam_s_datoy))
          
        #else:
        #    print("Мимо") 
   

    # update.message.reply_text(pechenka_popolam[1])
    # return pechenka_popolam
    


    #print(text)
    #update.message.reply_text(text)

#делаем эхобота
#def talk_to_me(kk_new_bot, update):
    #user_text = "Привет {}, ты написала: {}".format(update.message.chat.first_name, update.message.text) 
    #logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text)
    #print(update.message) #поменяла user_text на update.message 
    #update.message.reply_text(user_text)

#this thingy will do the getting 
def main():
    mybot = Updater("703624193:AAH9Sgsh98zWVfxk5JCV0YbEz4uO-1Y1Hoo", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("planet", what_planet)) #в телеграме надо писать команду /planet
    #dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()