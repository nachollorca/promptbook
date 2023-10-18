levels = {
        0: "Use the 80/20 Principle for your explanation: what 20% of concepts would give me 80% of the overall understanding? Please concisely explain the concepts.",
        1: "Explain the topic as if you were teaching it to a fifth-grader. Use simple language and avoid jargon.",
        2: "Summarize the explanation as concisely as you can. Output only one paragraph",
        3: "Assume I have knowledge on the topic. Extend your explanation as much as needed with complex and technical details for a deep understanding of the topic."
    }


def explain_concept(
        concept: str,
        act_as: str = None,
        level: int = 0,
) -> str:
    prompt = "Your task is to "

    if act_as is not None:
        prompt = prompt + f"act as an expert {act_as} and "

    prompt = prompt + f"explain the concept of {concept}."

    prompt = prompt + f"\n {levels[level]}"

    return prompt


_title = "Explain a concept"
_description = """
Prompt GPT to explain you a concept in a determined level of difficulty/length:
 
 0. (default) Use the 80/20 Principle for your explanation: what 20% of concepts would give me 80% of the overall understanding? Please concisely explain the concepts
 1. Explain the topic as if you were teaching it to a fifth-grader. Use simple language and avoid jargon
 2. Summarize the explanation as concisely as you can. Output only one paragraph
 3. Assume I have knowledge on the topic. Extend your explanation as much as needed with complex and technical details for a deep understanding of the topic
"""
_ui = {
    "concept": {
        "suggestions": "Representative democracy, self-attention mechanisms in Transformer architectures...",
        "help": "The concept you want to understand"
    },
    "act_as": {
        "suggestions": "politics professor, machine learning engineer...",
        "help": "Sometimes asking the model to 'act as an expert X' improves the output. This is optional"
    },
    "level": {
        "help": "The level of depth of the explanation depicted above."
    }
}