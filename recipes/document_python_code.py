def document_python_code(
        code: str,
        context: str = None,
        format: str = "Google"
) -> str:
    prompt = f"""
Your task is to generate a docstring for the Python function/class delimited by triple backticks below.
```python
{code}
```
Use {format} style.
"""

    if context is not None:
        prompt = prompt + f"""
Here you have more code that can help you creating the docstring:
```python
{context}
```
"""

    prompt = prompt + f"Output only the function/class definition and the docstring. Do not output the actual code of the function"

    return prompt


_title = "Document Python Code"
_author = "@nachollorca"
_description = "A senior ordered you to document 1M lines worth of project? Worry not, my friend, for this recipe shall soothe your path."
_ui = {
    "code": {
        "text": "",
        "help": "The function/class you want to document.",
        "suggestions": "def hello_world():\n  caps('Hello World')",
    },
    "context": {
        "text": "",
        "help": "Any code you want GPT-4 to read before generating the docstring.",
        "suggestions": "def caps(string: str) -> str: \n  return string.uppercase()",
    },
    "format": {
        "text": "",
        "help": "The docstring format you want the docstring to have.",
        "suggestions": "NumPy, reST, ...",
    },
}