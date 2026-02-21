import telebot

TOKEN = "8416702430:AAElerASCZC9nHvrrGFDzFJsDbfxsH7YRoo"
ADMIN_ID = 8348539088

bot = telebot.TeleBot(TOKEN)

# User yozsa
@bot.message_handler(func=lambda message: message.chat.id != ADMIN_ID, content_types=['text','photo','video','document','audio','voice'])
def forward_to_admin(message):
    
    user_info = f"""
Yangi xabar!

ID: {message.chat.id}
Username: @{message.from_user.username}
Name: {message.from_user.first_name}
"""
    
    bot.send_message(ADMIN_ID, user_info)
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    
    bot.send_message(message.chat.id, "Xabaringiz adminga yuborildi.")

# Admin reply qilsa → userga boradi
@bot.message_handler(func=lambda message: message.chat.id == ADMIN_ID)
def reply_to_user(message):
    
    if message.reply_to_message:
        try:
            text = message.reply_to_message.text
            user_id = int(text.split("ID: ")[1].split("\n")[0])
            bot.send_message(user_id, message.text)
        except:
            bot.send_message(ADMIN_ID, "Reply noto‘g‘ri userga qilindi.")

print("Bot ishlayapti...")
bot.infinity_polling()
