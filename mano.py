# environment
import os
from dotenv import load_dotenv
# bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async
# logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# bot handlers
@run_async
def mano(bot, update):
    request_id = update.message.message_id
    logger.info("[{}] Request from {}.".format(str(request_id), str(update.message.from_user.username)))
    if update.message:
            if ((update.message.text.lower()) == "mano"):
                update.message.reply_text("brown")
            if ((update.message.text.lower()) == "brown"):
                update.message.reply_text("mano")


@run_async
def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Mano ou Brown.")


@run_async
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # set env variables
    load_dotenv()
    BOT_TOKEN = os.getenv("TOKEN")
    PORT = int(os.environ.get('PORT', '8443'))
    
    updater = Updater(token=BOT_TOKEN)
    dispatcher = updater.dispatcher

    # add bot handlers
    dispatcher.add_handler(MessageHandler(Filters.text, mano))
    dispatcher.add_error_handler(error)
    dispatcher.add_handler(CommandHandler('help', help))

    # heroku webook
    updater.start_webhook(listen="0.0.0.0",
                        port=PORT,
                        url_path=BOT_TOKEN)
    updater.bot.set_webhook("https://maninhobrownbot.herokuapp.com/" + BOT_TOKEN)
    logger.info("Bot ready.")
    updater.idle()


if __name__ == '__main__':
    main()
