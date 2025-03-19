import telebot
from openai import OpenAI
from gtts import gTTS
import os
import tempfile

# Укажите ваш API-ключ OpenAI
client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Замените 'YOUR_BOT_TOKEN' на токен, который вы получили от BotFather
API_TOKEN = '7788717538:AAEWzruCATvnfGNP1JUHe7iHIWMy4IMVuDg'
bot = telebot.TeleBot(API_TOKEN)

# Список сообщений для взаимодействия с нейросетью
messages = []


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global messages
    user_input = message.text

    # Добавляем сообщение пользователя в историю
    messages.append({"role": "user", "content": user_input})

    # Делаем запрос к API ChatCompletion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )

    # Извлекаем ответ ассистента
    assistant_reply = response.choices[0].message.content

    # Добавляем ответ ассистента в историю
    messages.append({"role": "assistant", "content": assistant_reply})

    # Отправляем текстовый ответ пользователю
    bot.reply_to(message, assistant_reply)

    # Генерируем голосовое сообщение
    tts = gTTS(assistant_reply, lang='ru')

    # Создаем временный файл для аудио
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
        audio_file_path = f.name
        tts.save(audio_file_path)

    # Отправляем голосовое сообщение
    with open(audio_file_path, 'rb') as audio:
        bot.send_voice(message.chat.id, audio)

    # Удаляем временный файл после отправки
    os.remove(audio_file_path)


# Запускаем бота
if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
