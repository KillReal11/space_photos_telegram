# Space Telegram

List if scripts that allows you to automatically download photos from NASA and SpaceX.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
To launch sripts you you need to get such data as NASA API key and telegram API-token. They are stored in `.env` file in the root folder. Also frequency setting stored in `.env`.

You can get them using this links: https://api.nasa.gov/, https://telegram.me/BotFather.

### Usage example

You can see scripts usage by typing `python script_name.py -h` in terminal. Examples are given below.

- `python fetch_spacex_last_launch.py`

<img width="719" height="95" alt="SpaceX_example" src="https://github.com/user-attachments/assets/36a7f078-7fe7-42c6-aabc-cba06e43156e" />

- `python get_apod_images.py` 

<img width="659" height="90" alt="Apod_example" src="https://github.com/user-attachments/assets/4d140417-0282-408d-877f-ad9bec1299ee" />

- `python get_epic_images.py` 

<img width="659" height="86" alt="Epic_example" src="https://github.com/user-attachments/assets/813461ff-39a0-4e8e-b0e4-68194f4b484b" />

- `python post_photo_tg.py` 

<img width="1659" height="52" alt="post_photo_example" src="https://github.com/user-attachments/assets/adfcd49c-03c8-4393-99fe-51731fc35b91" />

- `python space_4_bot.py` 

<img width="1655" height="53" alt="space_4_bot_example" src="https://github.com/user-attachments/assets/71abdc1b-ab34-485c-831d-46eab636a47e" />






### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
