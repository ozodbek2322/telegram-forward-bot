import telebot
import threading
import time
import requests

TOKEN = "8416702430:AAElerASCZC9nHvrrGFDzFJsDbfxsH7YRoo"
ADMIN_ID = 8348539088

bot = telebot.TeleBot(TOKEN)

# Forward
@bot.message_handler(content_types=['text','photo','video','document','audio','voice'])
def forward_all(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

# Anti-sleep funksiyasi
def keep_alive():
    while True:
        try:
            requests.get("https://google.com")
        except:
            pass
        time.sleep(300)

threading.Thread(target=keep_alive).start()

print("Bot ishlayapti...")
bot.infinity_polling()
