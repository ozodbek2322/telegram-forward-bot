import telebot

TOKEN = "8416702430:AAEZq2ascx7G7DimsexMpfDwWsMk7DZf974"
ADMIN_ID = 8348539088

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice'])
def forward_all(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

print("Bot ishlayapti...")
bot.infinity_polling()
