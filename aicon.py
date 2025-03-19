from openai import OpenAI

# Укажите ваш API-ключ OpenAI

client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)


def interact_with_chatbot():
    # Изначально список сообщений пуст (или можете добавить system-промпт)
    messages = []

    while True:
        user_input = input("User: ")

        # Если пользователь ввёл "пока" или "exit", завершаем цикл
        if user_input.lower() in ["пока", "exit"]:
            print("Пока!")
            break

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

        # Выводим ответ на экран
        print("Assistant:", assistant_reply)


if __name__ == "__main__":
    interact_with_chatbot()