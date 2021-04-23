from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
import random
import math
from .data import TOKEN

home_keyboard = [['/dice', '/timer']]
dice_keyboard = [['/6', '/2x6'], ['/20', '/back']]
timer_keyboard = [['/1m'], ['/5m'], ['/3s', '/back']]
home_markup = ReplyKeyboardMarkup(home_keyboard, one_time_keyboard=False)
dice_markup = ReplyKeyboardMarkup(home_keyboard, one_time_keyboard=False)
timer_markup = ReplyKeyboardMarkup(home_keyboard, one_time_keyboard=False)


def start(update, context):
    update.message.reply_text(
        "Привет! Я бот помощник для игр!")
    update.message.reply_text(
        "Засечь время, или бросить кубики?", reply_markup=home_markup)


def help(update, context):
    update.message.reply_text(
        "Засеку ремя и брошу кубики за вас")


def main():
    updater = Updater(TOKEN, use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()