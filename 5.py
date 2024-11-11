import venv







import telebot



TOKEN = '7744544473:AAHd3StAStdw7SfIxkH_lMZnJbqbVdW1Nek'



bot = telebot.TeleBot(TOKEN)



@bot.message_handler(func=lambda message: True)

def echo_message(message):

    bot.reply_to(message, message.text)



bot.polling(none_stop=True)
