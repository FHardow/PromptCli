# prompt-cli

[![PyPI - Version](https://img.shields.io/pypi/v/prompt-cli.svg)](https://pypi.org/project/prompt-cli)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/prompt-cli.svg)](https://pypi.org/project/prompt-cli)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install dist/prompt_cli-0.0.1-py3-none-any.whl
```

Make sure that you have your `OPEN_API_KEY` set in your environment variables.

## Usage

![img.png](img.png)


## Generate code
You can generate code through a prompt with the command
```console
prompt generate <prompt> <file> 
```
where `<prompt>` is the name of the prompt and `<file>` is the name of the file to use as a input for you prompt.

```console
prompt generate <prompt> <file> --overwrite
```
will overwrite the file with the generated code by openai.

## Ask a question
You can ask a question through a prompt with the command
```console
prompt ask <question>
```
where `<question>` is the question you want to ask.
It behaves the same as the ChatGPT chat functionality.

## License

`prompt-cli` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
