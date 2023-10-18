def correct_text(
        text: str,
        style: str = None
) -> str:
    prompt = f"""
Your task is to correct and improve the text that is shown delimited by quotation marks below.

"{text}"

Output only the corrected text and perform the following actions:
 1. Identify and correct spelling errors
 2. Identify and correct grammatical issues
 3. If necessary, improve readability and reduce verbosity
"""

    if style is not None:
        prompt = prompt + f" 4. Make sure the text is written in {style} style."

    return prompt


_title = "Correct Text"
_description = """You are unsure if your text contains spelling/grammatical errors? 
Do you need to review it is concise or it is written in an specific style?
Just copy-paste it here and let GPT do the magic.
"""
_ui = {
    "text": {
        "suggestions": "Yo, crabs be these cool creatures, man. Dey got dem hard shells that's like armor, so dey can defend themselves from predators. Dem lil' pinchers ain't no joke - they use 'em to grab stuff and even fight other crabs! Crabs also be walkin' sideways, and that's just plain funny, ain't it? Dey live in da ocean and some of 'em on da beach. When ya see 'em scuttlin' around in da sand, it's like a little dance show. Dey eat pretty much anything dey can get their claws on, from plants to other critters."
    },
    "style": {
        "suggestions": "formal, academic..."
    }
}