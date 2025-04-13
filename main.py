import os
import telebot
import openai

# Ottieni le chiavi dalle variabili d'ambiente (.env o settings di Render)
openai.api_key = os.getenv("OPENAI_KEY")
bot = telebot.TeleBot(os.getenv("TELEGRAM_KEY"))

CHAT_ID = os.getenv("CHAT_ID")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if str(message.chat.id) == CHAT_ID:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        reply = response['choices'][0]['message']['content']
        bot.send_message(message.chat.id, reply)

bot.polling()
