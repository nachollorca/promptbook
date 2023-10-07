def write_cover_letter(
        job: str,
        cv: str,
        style: str = None,
        vocabulary: str = None,
) -> str:
    prompt = f"""
Your task is to write a cover letter for the job posting delimited by quotation marks below:

"{job}" 

Use the information from my resume delimited by quotation marks below, only when you feel it advantageous.

"{cv}"

Perform the following actions:
 1. Write a paragraph of maximum 6 sentences explaining why I would like to work with them and praising their business.
 2. Write a paragraph of maximum 7 sentences explaining why I am a wonderful fit for the role and how my experience aligns perfectly with the position.
 3. Write a short closing paragraph re-stating my interest and hoping to hear from them soon.

"""
    if style is not None:
        prompt = prompt + f"Use a {style} voice tone."

    if vocabulary is not None:
        prompt = prompt + f"Use {vocabulary} vocabulary."

    return prompt
