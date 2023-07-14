import os

from linebot import LineBotApi
from linebot.models import TextSendMessage

class Line:
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
    LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
    LINE_MY_USER_ID = os.getenv('LINE_MY_USER_ID')

    @classmethod
    def send_message(cls, message):
        line_bot_api = LineBotApi(cls.LINE_CHANNEL_ACCESS_TOKEN)
        messages = TextSendMessage(text=message)

        try:
            line_bot_api.push_message(cls.LINE_MY_USER_ID, messages)
            return "OK"
        except Exception as e:
            return e.message
