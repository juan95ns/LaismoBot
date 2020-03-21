#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
from telegram.ext import Updater
import logging
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def main():
    load_dotenv()
    updater = Updater(token=os.getenv('TELEGRAM_BOT'), use_context=True)

    dp = updater.dispatcher

    dp.add_handler()

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
