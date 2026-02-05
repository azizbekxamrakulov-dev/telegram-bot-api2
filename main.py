import time
import requests
from config import TOKEN


class Bot:
    def __init__(self, token):   #  init to‘g‘rilandi
        self.BASE_URL = f"https://api.telegram.org/bot{token}"
        self.offset = 0

    def getMe(self) -> dict:
        url = f"{self.BASE_URL}/getMe"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        raise Exception("Xatolik bor !!!")

    def get_updates(self) -> list:
        url = f"{self.BASE_URL}/getUpdates"
        params = {
            "offset": self.offset,
            "limit": 10
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("result", [])
        return []

    def send_message(self, chat_id, text):
        url = f"{self.BASE_URL}/sendMessage"
        requests.get(url, params={"chat_id": chat_id, "text": text})

    def send_photo(self, chat_id, photo):
        url = f"{self.BASE_URL}/sendPhoto"
        requests.get(url, params={"chat_id": chat_id, "photo": photo})

    def send_audio(self, chat_id, audio):
        url = f"{self.BASE_URL}/sendAudio"
        requests.get(url, params={"chat_id": chat_id, "audio": audio})

    def send_voice(self, chat_id, voice):
        url = f"{self.BASE_URL}/sendVoice"
        requests.get(url, params={"chat_id": chat_id, "voice": voice})

    def start_polling(self):
        print("Bot ishga tushdi...")
        while True:
            updates = self.get_updates()

            for update in updates:
                #  offset har doim yangilanadi
                self.offset = update["update_id"] + 1

                message = update.get("message")
                if not message:
                    continue

                chat_id = message["chat"]["id"]

                if "text" in message:
                    self.send_message(chat_id, message["text"])

                if "photo" in message:
                    file_id = message["photo"][-1]["file_id"]
                    self.send_photo(chat_id, file_id)

                if "audio" in message:
                    self.send_audio(chat_id, message["audio"]["file_id"])

                if "voice" in message:
                    self.send_voice(chat_id, message["voice"]["file_id"])

            time.sleep(1)


bot = Bot(TOKEN)
bot.start_polling()
