import telebot
import os

TOKEN = os.getenv("8416702430:AAElerASCZC9nHvrrGFDzFJsDbfxsH7YROo")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice'])
def forward_all(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

print("Bot ishlayapti...")
bot.infinity_polling()
