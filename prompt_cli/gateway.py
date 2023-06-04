import openai

from prompt_cli.config import OPENAI_API_KEY


def chat_gpt(instruction: str, user_input: str, model: str):
    openai.api_key = OPENAI_API_KEY

    # "You are a system that only generates code. Do not describe or contextualize the code. Do not apply any formatting
    # or syntax highlighting. DO NOT wrap the code in a code block!"

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "I will provide some specific instruction to a code snippet and you will change the code so that"
                    " the instructions are meet."
                    "My instructions are placed in quotes and follow the string `instructions:` and the code is placed"
                    " in quotes and follow the string `code:`. "
                    "You are a system that only generates code. Do not describe or contextualize the code. Do not apply"
                    " any formatting or syntax highlighting. Do not wrap the code in a code block."
                    "From now, your response must be only the code block, no talking, no comments."
                    # f"Do not describe or contextualize the code.Do not apply any formatting or syntax highlighting.Do
                    # not wrap the code in a code block."
                    # f"Only return code! Do not say anything else, only return the changed code. "
                ),
            },
            {
                "role": "user",
                "content": f"`instructions:` {instruction} `code:` {user_input}",
            },
        ],
    )

    message = response.choices[0].message.content

    return message


class OpenAIGateway:
    def __init__(self, key: str) -> None:
        self.key = key

    def call_chat() -> dict:
        ...
