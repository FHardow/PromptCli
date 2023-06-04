from pathlib import Path

import typer

from prompt_cli.gateway import chat_gpt

app = typer.Typer()

system_prompt = ""


@app.command()
def chat(
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
    result = chat_gpt(instruction, file_content, model)
    print(result)

    if overwrite:
        with Path(file.name).open("w") as file:
            file.write(result)
            file.flush()


if __name__ == "__main__":
    app()
