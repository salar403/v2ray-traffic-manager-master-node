import telebot

from backend.environments import TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode=None)

def send_message(chat_id:int, message:str, parse_mode="MarkdownV2"):
    bot.send_message(chat_id=chat_id,  text=message, parse_mode=parse_mode)
