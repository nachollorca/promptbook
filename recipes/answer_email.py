def answer_email(
        their_email: str,
        my_answer: str,
        style: str = "formal",
) -> str:
    prompt = f"""
I receive many emails and I do not have time to redact long answers.
Your task is to adapt my quick and badly-composed answer and write instead a proper text to respond to the provided email.

The email (or email chain) to which I am answering is shown here delimited by quotation marks:

"{their_email}"

And my quick answer is:

"{my_answer}"

Use a {style} style.
"""
    return prompt