#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
from pathlib import Path
from telegram.ext import Updater, MessageHandler, Filters
from telegram import Update
import logging
import os

logger = logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
parguelas = []


def messageHandler(update: Update, context):
    if update.message.from_user.username in parguelas:
        update.message.reply_text('Eres idiota')


def main():
    token = os.getenv('TELEGRAM_TOKEN')
    updater = Updater(token=token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, messageHandler))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    parguelas = os.getenv('USERS').split(',')

    main()
