import telegram
import os
from dotenv import load_dotenv
from parse_inputs import parse_path


def main():
    load_dotenv()
    chat_id = os.getenv("TG_CHAT_ID")
    tg_token = os.getenv("TG_BOT_TOKEN")
    bot = telegram.Bot(token=tg_token)
    photo = parse_path()
    with open(photo, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)


if __name__ == '__main__':
    main()
