import telebot

# Замените 'YOUR_BOT_TOKEN' на токен, который вы получили от BotFather
API_TOKEN = '8194966429:AAFXsaceFm4SgJJWAjebNeNImM0VrH0w_Kc'
bot = telebot.TeleBot(API_TOKEN)

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def echo_message(message):
    # Отправляем обратно то же сообщение, которое получили
    bot.send_message(message.chat.id, message.text)

# Запускаем бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)