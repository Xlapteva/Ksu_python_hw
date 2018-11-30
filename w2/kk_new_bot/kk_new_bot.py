from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

#adding a proxy
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format = "%(asctime)s - %(levelname)s - %(message)s",
                    level = logging.INFO, 
                    filename = "kk_new_bot.log"
                    )


def greet_user(bot, update):
    text = "Вызван старт"
    print(text) #or I could put logging.info(text) here
    update.message.reply_text(text)

#делаем эхобота
def talk_to_me(kk_new_bot, update):
    user_text = "Привет {}, ты написала: {}".format(update.message.chat.first_name, update.message.text) 
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text)
    #print(update.message) #поменяла user_text на update.message 
    update.message.reply_text(user_text)

#this thingy will do the getting 
def main():
    uinteractwithurbotviame = Updater("703624193:AAH9Sgsh98zWVfxk5JCV0YbEz4uO-1Y1Hoo", 
        request_kwargs=PROXY)

    logging.info("Ботик стартанул")


    dp = uinteractwithurbotviame.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    uinteractwithurbotviame.start_polling()
    uinteractwithurbotviame.idle()

main()

#############
#CommandHandler - с его пмощью мы подписываемся на оперделенные события 
#При помощи диспетчера мы подвешиваем события к нашему боту 
#uinteractwithurbotviame - это объект класса Updater, 
#у него есть атрибут диспетчер
#почему импорт логгин мы делаем так именно, а не через запятуйку, как с Updater?
#что у меня с логом за жуть происходит!?
#filters - нужен, чтобы выбирать, с каким типом сообщений мы хотим работать
##########