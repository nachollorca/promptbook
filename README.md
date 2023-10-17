# Promptbook UI
Do you find yourself writing the same kind of prompts again and again into ChatGPT?
Work your most used prompts into a comfy graphic user interface with just a few lines of code.

Promptbook allows you to:
 - Have a customizable UI from a simple prompt-building Python function
 - Store your GUI-prompts to reuse them on a click
 - Use fantastic recipe ideas from other contributors
 
## Examples
For a simple example, the recipe in `recipes/correct_text.py`...
```python
def correct_text(
        text: str,
        style: str = None
) -> str:
    prompt = f"""
Your task is to correct and improve the text that is shown delimited by quotation marks below.

"{text}"

Output only the corrected text and perform the following actions:
 1. Identify and correct spelling errors
 2. Identify and correct grammatical issues
 3. If necessary, improve readability and reduce verbosity
"""

    if style is not None:
        prompt = prompt + f" 4. Make sure the text is written in {style} style."

    return prompt
```
...will automatically be shown in the app as...

![Simple example](media/example.png)

Then, **promptbook** offers multiple customization options to embellish your UI. A more complex example (see the code in [`recipes/document_python_code.py`](recipes/document_python_code.py) could look like:

![Complex example](media/example2.png)

## How it works
**Promptbook** is built upon Python function signatures and type hints. Then, Streamlit is used to provide a graphic interface.

In essence, a parser reads the prompt-generating function, identifies the arguments and creates according streamlit input widgets in the application.

Lastly, a Prompt class queries the OpenAI API and computes the answer, together with its token context and resulting cost.

## How to use
**To use the current recipes just get to [Promptbook UI](promptbook.streamlit.app) and start playing!** If you do not have an OpenAI API key to launch the prompts, you can generate them and copy-paste into [ChatGPT](https://chat.openai.com/).

To create your own recipes, head over to [`docs/contribute.md`](docs/contribute.md). To learn best practices on prompt engineering, I recommend [this compendium](https://www.promptingguide.ai/introduction/tips).


