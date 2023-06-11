from json import loads

import openai

from prompt_cli.config.prompts import SYSTEM_PROMPT_DEVELOPER_PROMPT


class OpenAIGateway:
    def __init__(self, key: str) -> None:
        self.key = key
        openai.api_key = key

    def code_generation(self, instruction: str, user_input: str, model: str):
        # "You are a system that only generates code. Do not describe or contextualize the code.
        # Do not apply any formatting or syntax highlighting. DO NOT wrap the code in a code block!"

        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT_DEVELOPER_PROMPT},
                {
                    "role": "user",
                    "content": f"`instructions:` {instruction} `code:` {user_input}",
                },
            ],
        )

        message = response.choices[0].message.content
        return message

    def ask_question(self, question: str, model: str, sources: bool):
        messages = []
        if sources:
            system_prompt = {
                "role": "system",
                "content": (
                    "Answer the following question and print sources for websites of the information."
                    "The sources should be in the format of a list of links."
                ),
            }
            messages.append(system_prompt)

        messages.append(
            {
                "role": "user",
                "content": f"Q: {question} A:",
            },
        )
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
        )

        message = response.choices[0].message.content

        return message
