import typer
from prompt_cli.gateway import chat_gpt

app = typer.Typer()

# Add --model flag to specify which model to use
@app.command()
def chat(prompt: str, model: str = "gpt-3.5-turbo"):
    result = chat_gpt(prompt, model)
    print(result)


if __name__ == "__main__":
    app()
