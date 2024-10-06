import telebot

bot = telebot.TeleBot("7803559129:AAE7me-e2FLXXTDdbxAyHqwli83JzsRyFWM", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
    response = f"{message.text}\n\nCreated by @kamer_fronend"
    for _ in range(100):  # Xabarni 100 marta yuborish
        bot.reply_to(message, response)

bot.polling(none_stop=True)
