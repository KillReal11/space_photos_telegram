import telegram
import os
import time
import random
from dotenv import load_dotenv


def main():
    load_dotenv()
    chat_id = os.getenv("TG_CHAT_ID")
    tg_token = os.getenv("TG_BOT_TOKEN")
    posting_freq = int(os.getenv("FREQUENCY"))
    bot = telegram.Bot(token=tg_token)
    while True:
        for root, dirs, files in os.walk('images'):
            random.shuffle(dirs)
            random.shuffle(files)
            for file in files:
                with open(f'{root}/{file}', 'rb') as photo:
                    bot.send_photo(chat_id=chat_id, photo=photo)
                time.sleep(posting_freq)


if __name__ == '__main__':
    main()
