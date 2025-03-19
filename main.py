import telebot

# Замените 'YOUR_BOT_TOKEN' на токен, который вы получили от BotFather
API_TOKEN = '7788717538:AAEWzruCATvnfGNP1JUHe7iHIWMy4IMVuDg'
bot = telebot.TeleBot(API_TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я ваш бот. Используйте команду /help, чтобы узнать, что я могу делать.")

# Команда /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Я могу помочь вам с следующими командами:\n"
        "/start - Запустить бота и получить приветствие.\n"
        "/help - Получить список доступных команд."
    )
    bot.reply_to(message, help_text)


@bot.message_handler(commands=['count'])
def count_characters(message):
    # Получаем текст после команды
    text_to_count = message.text[len('/count '):].strip()
    character_count = len(text_to_count)

    if text_to_count:
        bot.reply_to(message, f"Количество символов в вашем сообщении: {character_count}")
    else:
        bot.reply_to(message, "Пожалуйста, введите сообщение для подсчета символов.")

@bot.message_handler(commands=['noblank'])
def remove_blanks(message):
    # Извлекаем текст сообщения после команды
    text = message.text[len('/noblank '):].strip()
    # Убираем все пробелы
    no_blanks = text.replace(' ', '')
    bot.reply_to(message, f"Ваше сообщение без пробелов: {no_blanks}")

# Запускаем бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)

