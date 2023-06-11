from pathlib import Path

import typer

from prompt_cli.config.config import OPENAI_API_KEY
from prompt_cli.gateway import OpenAIGateway

app = typer.Typer()
gateway = OpenAIGateway(key=OPENAI_API_KEY)

system_prompt = ""


@app.command()
def code_generation(
    instruction: str = typer.Argument(),
    file: typer.FileText = typer.Argument(),
    model: str = typer.Argument("gpt-3.5-turbo", help="Choose a model to use for chat"),
    overwrite: bool = typer.Option(
        False, "--overwrite", help="overwrite the file with the new content"
    ),
):
    """
    Chat with an AI using OpenAI's GPT model.
    """
    file_content = file.read()
    result = gateway.code_generation(instruction, file_content, model)
    print(result)

    if overwrite:
        with Path(file.name).open("w") as file:
            file.write(result)
            file.flush()


@app.command()
def ask_question(
    question: str = typer.Argument(),
    model: str = typer.Argument("gpt-3.5-turbo", help="Choose a model to use for chat"),
    sources: bool = typer.Option(False, "--sources", help="With source prompt."),
):
    """
    Chat with an AI using OpenAI's GPT model.
    """
    result = gateway.ask_question(question=question, model=model, sources=sources)
    print(result)


if __name__ == "__main__":
    app()
