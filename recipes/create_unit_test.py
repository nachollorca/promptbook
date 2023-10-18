def create_unit_test(
        code: str,
        scenario: str = "Most likely Scenario to test for the code described",
        proficiencyLevel: str = "All Levels",
) -> str:
    prompt = f"""
You are an expert QA Engineer, your task is to draft a unit test for the code provided below delimited by triple backticks.

```
{code}
```
"""
    prompt = prompt + f"\n Write the test the following scenario: {scenario}. "

    prompt = prompt + f"\n Adapt the comments for a proficiency level of: {proficiencyLevel}."

    return prompt


_title = "Automated Unit Tests"
_author = "AndresBarriga"
_description = "This allows you to draft Unit test based on your code!"
_ui = {
    "code": {
        "text": "Provide the code you want to draft an Automated Test for",
        "help": "This is very important to be filled",
        "suggestions": "Enter your code...",
    },
}