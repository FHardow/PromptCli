import os

import openai

from prompt_cli.config import OPENAI_API_KEY


def chat_gpt(prompt: str, model: str):
    openai.api_key = OPENAI_API_KEY

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI assistant that gets a cli intput or a code instruction and "
                    "you will try to find the error in the cli input or the code instruction."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    )

    message = response.choices[0].message.content

    return message


class OpenAIGateway:
    def __init__(self, key: str) -> None:
        self.key = key

    def call_chat() -> dict:
        ...
