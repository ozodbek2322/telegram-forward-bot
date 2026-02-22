import telebot
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = "8416702430:AAF5lNyiteQ97-rqpK4lU95F-u9AJfKUzO4"
ADMIN_ID = 8348539088

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text','photo','video','document','audio','voice'])
def forward_all(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

# Web server (Render uxlamasligi uchun)
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Bot is alive")

def run_web():
    server = HTTPServer(('0.0.0.0', 10000), Handler)
    server.serve_forever()

threading.Thread(target=run_web).start()

print("Bot ishlayapti...")
bot.infinity_polling()
