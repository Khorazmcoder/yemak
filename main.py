import telebot
from config import BOT_TOKEN, CHANNEL_ID
from telebot.apihelper import ApiTelegramException

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🎬 Salom! Kinoning kodini yuboring, men sizga kanal postini yuboraman.")

@bot.message_handler(func=lambda message: message.text.isdigit())
def find_movie_by_code(message):
    post_id = int(message.text)
    try:
        bot.forward_message(chat_id=message.chat.id,
                            from_chat_id=CHANNEL_ID,
                            message_id=post_id)
    except ApiTelegramException:
        bot.reply_to(message, "❌ Bu kod bo‘yicha kino topilmadi.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Xatolik: {e}")

@bot.message_handler(func=lambda message: not message.text.isdigit())
def handle_non_digit(message):
    bot.reply_to(message, "📩 Faqat kinoning **raqamli kodini** yuboring.")

bot.infinity_polling()
