# Recommended practices to format your long strings
Python provides various options to format multi-line strings.
All of them have pros and cons, 
and no choice will generally have an impact on the output of a GPT model.
Nevertheless, for the sake of order and user-friendly visualization,
there are indeed better and worse choices. My recommendations are:

Use docstring-style strings (triple quotes):
```python
"""This is a docstring-style string.
Both newlines and tabulations will be shown as you write them
"""
```

Sadly, docstrings count tabs from the leftmost part of the code, 
no matter where you start the docstring.
So, for instance, the string below...
```python
if condition:
    prompt = """
    Some text
    blabla
    """
```
...would be printed as...
```
    Some text
    blabla
```
...instead of...
```
Some text
blabla
```
So I recommend that, no matter where your string starts, you use ¨ugly indenting:¨
 - Start your docstring with triple quotes
 - Jump one line
 - Remove all tabs
 - Write the string
 - Close the triple quotes
```python
def do_something():
    if condition:
        prompt = """
This indenting is ugly.
But it helps visualizing and editing the prompts in the GUI.
"""
    
    return prompt
```
