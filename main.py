#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
from pathlib import Path
from telegram.ext import CallbackContext, CommandHandler, CommandHandler, Filters, MessageHandler, Updater
from telegram import Update
from laismo_lib import *
import logging
import os


def messageHandler(update: Update, context: CallbackContext):
    user = update.message.from_user

    if user and allowed_user(user.username) and check_laismo(update.message.text):
        add_stats(user.username)
        update.message.reply_text("¡Cuidado con ese posible laísmo/leísmo madrizleño!")


def statsHandler(update: Update, context: CallbackContext):
    stats_list = show_stats().items()

    msg_stats = "📭 No hay laístas aún"

    if len(stats_list) > 0:
        msg_stats = "\n".join(map(lambda user: "🤡 {}: {}".format(user[0], user[1]), stats_list))
        update.message.reply_text(msg_stats)
    else:
        update.message.reply_text(msg_stats)


def error(update: Update, context: CallbackContext):
    logging.warning("Update {} caused error {}".format(update, context.error))


def main():
    token = os.getenv("LAISMO_TELEGRAM_TOKEN")
    updater = Updater(token=token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("lastats", statsHandler))
    dp.add_handler(MessageHandler(Filters.text, messageHandler))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    env_path = Path(".") / ".env"
    load_dotenv(dotenv_path=env_path)

    main()
