def answer_email(
        their_email: str,
        my_answer: str,
        style: str = "formal",
) -> str:
    prompt = f"""
I receive many emails and I do not have time to redact long answers.
Your task is to adapt my quick and badly-composed answer draft and write instead a proper text to respond to the provided email.

The email (or email chain) to which I am answering is shown here delimited by quotation marks:

"{their_email}"

And my quickly drafted answer is:

"{my_answer}"

Use a {style} style. Be concise and avoid redundancy and verbosity.
"""
    return prompt

_title = "Quick email answers"
_description = "It often takes me more time to style up my messages than actually thinking about the answer. This little prompt allows me to just rush my thoughts into a box and let GPT make it look proper."
_ui ={
    "their_email": {
        "suggestions": """Dear Mr. Smith,

I hope this message finds you well. I trust that you have had a productive and rewarding week thus far. I am writing to discuss the possibility of scheduling a brief phone call with you this Friday at 11:00 AM to delve into a matter of interest.

To that end, I would like to kindly inquire if you have an available time slot on your calendar for a call this Friday at 11:00 AM. I understand that your schedule can be quite hectic, so please know that I greatly appreciate your time and flexibility in accommodating this request.

Best regards,
Max Mustermann
""",
        "help": "The email (or email chain!) you have to answer",
    },
    "my_answer": {
        "help": "My quickly drafted answer for GPT to improve",
        "suggestions": "ok, bro"
    }
}