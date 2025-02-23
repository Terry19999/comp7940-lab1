# This file is based on version 13.7 of python telegram chatbot
# and version 2.18.0 of urllib3

import telegram
from telegram.ext import Updater, MessageHandler, Filters
import configparser
import logging

def main():
    # Load your token and create an Updater for your Bot
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Define a function to handle messages
    def echo(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    # Define a handler to handle messages
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    # Add the handler to the dispatcher
    dispatcher.add_handler(echo_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()