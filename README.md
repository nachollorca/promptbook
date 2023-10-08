# Promptbook UI

Do you find yourself writing the same kind of prompts again and again into ChatGPT?
Work your most used prompts into a comfy graphic user interface with just a few lines of code.

Promptbook allows you to:
 - Have a customizable UI from a simple prompt-building Python function
 - Store your GUI-prompts to reuse them on a click
 - Use fantastic recipe ideas from the community

## Example 
For a simple example, the recipe in `recipes/correct_text/py`:
```python
# the recipe: build your prompt with required, default and optional inputs
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
Will automatically be shown in the app as:

![alt text](media/example.png)

## How to use
**To use the current recipes just get to [Promptbook UI](promptbook.streamlit.app) and start playing!** If you do not have an OpenAI API key to launch the prompts, you can generate them and copy-paste into [ChatGPT](ChatGPT).

To create your own recipes, follow the guide below.

### Install Promptbook UI
To create your own recipe Follow these steps (assuming you have Python and Conda installed):
 0. Decide on its name. Preferred syntax is `verb_noun`, for example `correct_text`
 1. Fork this GitHub repository
 2. Clone it into your machine and locate the terminal inside: 
```shell
git clone git@github.com:<your_github_username>/promptbook.git
cd promptbook
```
 4. Make a new branch for your recipe: 
```shell
git checkout -b verb_noun
```
 5. Create a new conda environment, activate it and install required packages: 
```shell
conda env create -n promptbook
conda activate promptbook
pip install -f requirements.txt
```


### Create your recipe!
Now you just have to create your script in `recipes/verb_noun.py`, and inside the prompt-generation function with the same name `def verb_noun() -> str:`.

For your first recipe your best bet is start from the code in `template.py`

Now launch the app locally with `python -m streamlit run app.py` and start prototyping! Everytime you save your code, the app reruns automatically to display the changes.

### Contribute
If you are satisfied with your recipe share it to see it in the online [Promptbook UI](promptbook.streamlit.app)!
 1. Commit your recipe script
```shell
git add recipes/verb_noun.py
git commit -m "Upload recipe"
```
 2. Push it to your forked repo 
```shell
git push -u origin verb_noun
```
 3. Make a Pull Request in the [GitHub repo](https://github.com/nachollorca/promptbook), I will take care everything is alright and merge it to the online app :party:.

