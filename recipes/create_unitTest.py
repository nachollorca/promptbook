# the recipe: build your prompt with required, default and optional inputs
def create_unitTest(
        code: str,  # required ingredient
        scenario: str = "More likely Scenario to test for the code described",  # required ingredient with a default value
        proficiencyLevel: str = "All Levels",  # optional ingredient (use `[]` for lists)
) -> str:
    prompt = f"""
You are an expert QA Engineer, your task is to draft a unit test for the code provided: {code}, which MUST be filled by the user.
""" # This is ugly indenting, but it really helps visualizing the prompts
    # Indenting / new lines do not have impact on GPTs response
    # See docs/prompt_strings_formatting

    if proficiencyLevel is not None:
        prompt = prompt + \
                 f"Adapt the comments for a proficiency level of : {proficiencyLevel}, only in case the user fills it."

    prompt = prompt + \
             f"Here I add a scenario to test{scenario}, which will be More likely Scenario to test for the code described if the user does not fill it."

    return prompt


# optional user interface details
# feel free to use as many as you want
_title = "Automated Unit Tests"  # a descriptive title for your recipe
_author = "AndresBarriga"  # your name or github user
_description = "This allows you to draft Unit test based on your code!"  # what the recipe does / use cases
_ui = {  # additional UI information for each ingredient
    "ingredient_1": {  # must have the same name as the function argument it refers to
        "text": "Provide code you want to draft a Automated Test for",  # some explanatory text written before the input field
        "help": "This is very important to be filled",  # a helper text shown on hover
        "suggestions": "Enter your code...",  # some examples to show in the input placeholder
    },
}