import telebot
bot = telebot.TeleBot("5247481623:AAE3uHZ9HaJFsRZeW8u2CGAOb96A08-j4GU", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.reply_to(message, "Я твой персональный бот, давай знакомиться!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
# bot.reply_to(message, "Privet, bebrik")
    if message.text == "privet":
        bot.reply_to(message, "Я рад тебя видеть, Добро пожаловать!")
    else:
        bot.reply_to(message, 'i dont understand u)')

bot.infinity_polling()

#5247481623:AAE3uHZ9HaJFsRZeW8u2CGAOb96A08-j4GU