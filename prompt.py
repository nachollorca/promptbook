import openai
import tiktoken


def launch_prompt(input_text: str, api_key: str, model = "gpt-4", temperature = 0) -> str:
    openai.api_key = api_key

    in_cost = get_cost(input_text, model, "input")
    print(f"This prompt costs ca. {round(in_cost,5)} $ to compute")

    messages = [{"role": "user", "content": input_text}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    output_text = response.choices[0].message["content"]

    cost = get_cost(output_text, model, "output")
    print(f"This answer costs ca. {round(cost,5)} $ to compute")

    return output_text


def get_cost(text: str, model: str, mode: str) -> float:
    token_cost = {
        ("gpt-3.5-turbo", "input"): 0.0015 / 1000,
        ("gpt-4", "input"): 0.03 / 1000,
        ("gpt-3.5-turbo", "output"): 0.02 / 1000,
        ("gpt-4", "output"): 0.06 / 1000,
    }

    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(text))
    cost = num_tokens * token_cost[(model, mode)]
    return cost