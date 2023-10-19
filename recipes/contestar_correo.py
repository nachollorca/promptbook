def contestar_correo(
        correo_al_que_responder: str,
        mi_respuesta: str,
        estilo: str = "formal",
) -> str:
    prompt = f"""
Recibo muchos correos electrónicos y no tengo tiempo para redactar respuestas largas.
Tu tarea consiste en adaptar mi mal redactado borrador de respuesta y escribir en su lugar un texto adecuado para responder al correo electrónico proporcionado.

El correo electrónico (o cadena de correos electrónicos) al que estoy respondiendo se muestra aquí, delimitado por comillas:

"{correo_al_que_responder}"

Y mi contestación rápida es esta:

"{mi_respuesta}"

Usa un estilo {estilo}. Se conciso y evita redundancia y verbosidad.
"""
    return prompt

_title = "Responde emails a toda velocidad"
_description = "Normalmente me lleva más tiempo escribir correctamente el mensaje que pensar en la respuesta en si. Este pequeño prompt me permite simplemente hacer un borrador rápido de mis pensamientos en un cuadro y dejar que GPT haga el resto."
_ui ={
    "correo_al_que_responder": {
        "suggestions": """Estimado Sr. Smith,

Espero que este mensaje le encuentre bien. Confío en que haya tenido una semana productiva y gratificante hasta el momento. Le escribo para tratar la posibilidad de programar una breve llamada telefónica con usted este viernes a las 11:00 AM para profundizar en un asunto de interés.

Para ello, me gustaría saber si tiene un hueco disponible en su agenda para una llamada este viernes a las 11:00 AM. Comprendo que su agenda puede ser bastante ajetreada, por lo que le agradezco enormemente su tiempo y flexibilidad para atender esta petición.

Saludos cordiales,
Max Mustermann
""",
        "help": "El correo (o cadena de correos) al que quieres responder",
    },
    "mi_respuesta": {
        "help": "Mi borrador rápido y mal escrito",
        "suggestions": "ok, bro"
    },
    "estilo": {
        "suggestions": "formal, amigable, humorístico..."
    }
}