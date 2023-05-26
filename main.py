import Constants as keys
from telegram.ext import *
import Responses as R

print("Mark is getting up...")

def start_command(update, context):
    update.message.reply_test('Type something random')

def help_command(update, context):
    update.message.reply_test('Get help!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.responses(text)

    update.message.reply_test(response)

def error(update, context):
    print(f"Update {update} caused error {context}")

def main():
    updater = Updater(keys.API_KEY, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", ))




