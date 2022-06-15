import json
import telebot
import time


credentials_file = open('creds.json')
bot_credentials = json.load(credentials_file)["bot"]


TOKEN = bot_credentials["token"]
bot = telebot.TeleBot(TOKEN)


def send_info_to_bot(info, pdf_file="", design_photo=""):
    for user in bot_credentials["users"]:
        try:
            bot.send_message(int(user), info)
            if pdf_file != "":
                bot.send_message(int(user), pdf_file)
            else:
                pass
            if design_photo !="":
                bot.send_photo(int(user), design_photo)
            else:
                pass
        except Exception:
            print("Something went wrong. Check the message or the files and try to send again.")