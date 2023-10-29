def chat_with_gpt(first_message: str) -> str:
    if str(first_message) == "<class 'inspect._empty'>":
        return ""
    else:
        return first_message

_description = "I cannot chat with GPT4 on chat.openai.com with the API key, so this simple recipe allows me to it."
