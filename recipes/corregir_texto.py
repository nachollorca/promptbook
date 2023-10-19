def corregir_texto(
        texto: str,
        estilo: str = None
) -> str:
    prompt = f"""
Tu tarea consiste en corregir y mejorar el texto que se muestra a continuación delimitado por comillas.

"{texto}"

Devuelve sólo el texto corregido y realiza las siguientes acciones:
 1. Identifica y corrige los errores ortográficos.
 2. Identifica y corrige los problemas gramaticales
 3. Si es necesario, mejora la legibilidad y reduce la verbosidad
"""

    if estilo is not None:
        prompt = prompt + f" 4. Asegúrate de que el texto está escrito en estilo {estilo}."

    return prompt


_title = "Corregir texto"
_description = """No estás seguro de si tu texto contiene errores ortográficos o gramaticales? 
Necesitas revisar si es conciso o si está escrito en un estilo específico?
Simplemente cópialo y pégalo aquí y deja que GPT haga la magia.
"""
_ui = {
    "texto": {
        "suggestions": "Los cangrejos, son animules sorprendentos. Tienen esos caparazones duros, que los protejen de los depredadores. Sus pinzas son muy fuertes, y ellos los utilizan para agarar cosas y luchar contra otros cangrejos. Los cangrejos camina lateralmente, y eso es muy divertido, ¿no? Ellos vive en la océano y algunos en la playita. Cuando ves ellos moverse en la arena, es como un show de baile pequeñito. Comen practicamente cualquier cosa que ellos puede conseguir con sus pinzas, desde plantas hasta otros animalitos.",
    },
    "estilo": {
        "suggestions": "formal, académico..."
    }
}