import streamlit
import openai
import tiktoken


def launch_prompt(messages: list, api_key: str, model = "gpt-4", temperature = 0) -> str:
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    output_text = response.choices[0].message["content"]

    return output_text


token_cost = {
        ("gpt-4", "user", "8k"): 0.03 / 1000,
        ("gpt-4", "assistant", "8k"): 0.06 / 1000,

        ("gpt-4", "user", "32k"): 0.06 / 1000,
        ("gpt-4", "assistant", "32k"): 0.12 / 1000,

        ("gpt-3.5-turbo", "user", "4k"): 0.0015 / 1000,
        ("gpt-3.5-turbo", "assistant", "4k"): 0.002 / 1000,

        ("gpt-3.5-turbo", "user", "16k"): 0.003 / 1000,
        ("gpt-3.5-turbo", "assistant", "16k"): 0.004 / 1000,
    }


def get_token_cost(text: str, model: str, mode: str) -> float:

    encoding = tiktoken.encoding_for_model(model)
    tokens = len(encoding.encode(text))

    if model == "gpt-4" and tokens < 8000:
        context = "8k"
    elif model == "gpt-4" and tokens >= 8000:
        context = "32k"
    elif model == "gpt-3.5-turbo" and tokens < 4000:
        context = "4k"
    elif model == "gpt-3.5-turbo" and tokens >= 4000:
        context = "16k"

    cost = tokens * token_cost[(model, mode, context)]

    return {
           "tokens": tokens,
           "context": context,
           "cost": cost
    }


def are_required_filled(args: dict, params: dict) -> bool:
    for k in params.keys():
        if params[k]["required"] and str(args[k]) == "<class 'inspect._empty'>":
            return False

    return True


def reset_chat_callback():
    streamlit.session_state.messages = []

