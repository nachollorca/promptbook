import openai
import tiktoken


def launch_prompt(input_text: str, api_key: str, model = "gpt-4", temperature = 0) -> str:
    openai.api_key = api_key

    # in_cost = get_cost(input_text, model, "input")
    # print(f"This prompt costs ca. {round(in_cost,5)} $ to compute")

    messages = [{"role": "user", "content": input_text}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    output_text = response.choices[0].message["content"]

    # cost = get_cost(output_text, model, "output")
    # print(f"This answer costs ca. {round(cost,5)} $ to compute")

    return output_text


token_cost = {
        ("gpt-4", "input", "8k"): 0.03 / 1000,
        ("gpt-4", "output", "8k"): 0.06 / 1000,

        ("gpt-4", "input", "32k"): 0.06 / 1000,
        ("gpt-4", "output", "32k"): 0.12 / 1000,

        ("gpt-3.5-turbo", "input", "4k"): 0.0015 / 1000,
        ("gpt-3.5-turbo", "output", "4k"): 0.002 / 1000,

        ("gpt-3.5-turbo", "input", "16k"): 0.003 / 1000,
        ("gpt-3.5-turbo", "output", "16k"): 0.004 / 1000,
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




