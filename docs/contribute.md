This step-by-step tutorial explains how you can create your own recipes, test them locally and ultimately upload them to the online-app.

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

For your first recipe your best bet is start from the code in the template [`recipes/do_something.py`](recipes/do_something.py) and edit it to your needs:
```python
# the recipe: build your prompt with required, default and optional inputs
def do_something(
        ingredient_1: str,  # required ingredient
        ingredient_2: str = "spaghetti",  # required ingredient with a default value
        ingredient_3: int = None,  # optional ingredient (use `[]` for lists)
) -> str:
    prompt = f"""
This is the base prompt.  
It uses the mandatory ingredient {ingredient_1}, which MUST be filled by the user.
""" # This is ugly indenting, but it really helps visualizing the prompts
    # Indenting / new lines do not have impact on GPTs response
    # See docs/prompt_strings_formatting

    if ingredient_3 is not None:
        prompt = prompt + \
                 f"Here I add the optional ingredient {ingredient_3}, only in case the user fills it."

    prompt = prompt + \
             f"Here I add {ingredient_2}, which will be spaghetti if the user does not fill it."

    return prompt


# optional user interface details
# feel free to use as many as you want
_title = "Fantastic recipe"  # a descriptive title for your recipe
_author = "Gordon Ramsey"  # your name or github user
_description = "This recipe makes doing something much easier!"  # what the recipe does / use cases
_ui = {  # additional UI information for each ingredient
    "ingredient_1": {  # must have the same name as the function argument it refers to
        "text": "Provide essential ingredient",  # some explanatory text written before the input field
        "help": "This is very important",  # a helper text shown on hover
        "suggestions": "Peanut butter",  # some examples to show in the input placeholder
    },
}
```

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
 3. Make a Pull Request in the [GitHub repo](https://github.com/nachollorca/promptbook), I will take care everything is alright and merge it to the online app :partying_face:.
