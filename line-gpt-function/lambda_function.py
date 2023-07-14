import os
import sys
import json
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)
from linebot.exceptions import LineBotApiError, InvalidSignatureError
import logging
import openai
from services.line import Line
from services.time_tree import TimeTree

openai.api_key = os.getenv("OPENAI_API_KEY")
gpt_model = "gpt-4-0613"

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    logger.error("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    logger.error("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


def run_conversation(user_input):
    # STEP1: モデルにユーザー入力と関数の情報を送る
    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": "You are best assistant ever!"},
            {"role": "user", "content": user_input},
        ],
        functions=[
            {
                "name": "post_message_to_line",
                "description": "LINEにメッセージを投稿する",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string"},
                    },
                    "required": ["message"],
                },
            },
            {
                "name": "create_schedule_to_time_tree",
                "description": "TimeTreeにスケジュールを作成する",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                        "start_at": {"type": "string", "format": "date"},
                        "end_at": {"type": "string", "format": "date"},
                    },
                    "required": ["title", "description", "start_at", "end_at"],
                },
            },
        ],
        function_call="auto",
    )
    message = response["choices"][0]["message"]

    # STEP2: モデルが関数を呼び出したいかどうかを確認
    if message.get("function_call"):
        function_name = message["function_call"]["name"]
        arguments = json.loads(message["function_call"]["arguments"])

        if function_name == "post_message_to_line":
            function_response = Line.send_message(arguments.get("message"))
        elif function_name == "create_schedule_to_time_tree":
            function_response = TimeTree.create_schedule(
                arguments.get("title"),
                arguments.get("description"),
                arguments.get("start_at"),
                arguments.get("end_at"),
            )
        else:
            raise NotImplementedError()

        second_response = openai.ChatCompletion.create(
            model=gpt_model,
            messages=[
                {"role": "user", "content": user_input},
                message,
                {
                    "role": "function",
                    "name": function_name,
                    "content": str(function_response),
                },
            ],
        )

        return second_response
    else:
        return response


def lambda_handler(event, context):
    signature = event["headers"]["x-line-signature"]
    body = event["body"]
    ok_json = {"isBase64Encoded": False, "statusCode": 200, "headers": {}, "body": ""}
    error_json = {
        "isBase64Encoded": False,
        "statusCode": 500,
        "headers": {},
        "body": "Error",
    }

    @handler.add(MessageEvent, message=TextMessage)
    def message(line_event):
        user_input = line_event.message.text
        text = run_conversation(user_input)["choices"][0]["message"]["content"]
        line_bot_api.reply_message(line_event.reply_token, TextSendMessage(text=text))

    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        logger.error("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            logger.error("  %s: %s" % (m.property, m.message))
        return error_json
    except InvalidSignatureError:
        return error_json

    return ok_json
