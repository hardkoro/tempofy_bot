from os import getenv

from dotenv import find_dotenv, load_dotenv
from telegram import ParseMode
from telegram.ext import (CommandHandler, Defaults, Filters, MessageHandler,
                          Updater)

from help import FEATURE_HELP
from song import get_song_data

load_dotenv(find_dotenv())
TOKEN = getenv('TOKEN')
DEBUG_MODE = False

TEST_URI = 'https://open.spotify.com/track/40riOy7x9W7GXjyGp4pjAv?si=ba7f5849faa64fbe'


class TempofyBot():
    def __init__(self):
        if DEBUG_MODE:
            print(get_song_data(TEST_URI))
        else:
            self.updater = Updater(
                TOKEN,
                defaults=Defaults(disable_web_page_preview=True)
            )
            self.dispatcher = self.updater.dispatcher
            self.dispatcher.add_handler(
                CommandHandler('start', self.start)
            )
            self.dispatcher.add_handler(
                CommandHandler('help', self.help)
            )
            self.dispatcher.add_handler(
                MessageHandler(
                    Filters.text & ~Filters.command, self.tempofy_song
                )
            )
            self.updater.start_polling()
            self.updater.idle()

    def start(self, update, context):
        user = update.effective_user
        update.message.reply_markdown_v2(
            fr'Hi, {user.mention_markdown_v2()}\!'
        )

    def help(self, update, context):
        update.message.reply_text(FEATURE_HELP, parse_mode=ParseMode.MARKDOWN)

    def tempofy_song(self, update, context):
        try:
            update.message.reply_text(
                get_song_data(update.message.text),
                parse_mode=ParseMode.MARKDOWN
            )
        except Exception as e:
            update.message.reply_text(
                'Sorry! But I can''t find song with this URI at Spotify'
            )
            update.message.reply_text(
                str(e)
            )


def main():
    TempofyBot()


if __name__ == '__main__':
    main()
