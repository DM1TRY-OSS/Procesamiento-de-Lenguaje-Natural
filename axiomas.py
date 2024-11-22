import spacy

# Cargar el modelo en español de spaCy
nlp = spacy.load("es_core_news_sm")

# Definir reglas de gramática generativa ampliada
grammar = {
    'S': ['NP VP'],
    'NP': ['Det N'],
    'VP': ['V NP', 'V'],
}


# Función para identificar los símbolos no terminales en la frase
def detectar_simbolos_no_terminales(frase):
    simbolos_detectados = {}

    # Procesar la frase con spaCy
    doc = nlp(frase)

    # Inicializar variables para almacenar frases
    np_frase = ""
    vp_frase = ""

    # Identificar determinantes, sustantivos y verbos usando spaCy
    for token in doc:
        if token.pos_ == 'DET':  # Determinantes
            np_frase += token.text + " "
            simbolos_detectados['Det'] = np_frase.strip()
        elif token.pos_ == 'NOUN':  # Sustantivos
            np_frase += token.text + " "
            simbolos_detectados['N'] = np_frase.strip()
        elif token.pos_ == 'VERB':  # Verbos
            vp_frase += token.text + " "
            simbolos_detectados['V'] = vp_frase.strip()

    # Guardar la estructura de la oración
    simbolos_detectados['S'] = f"{simbolos_detectados.get('N', '')} {simbolos_detectados.get('V', '')}".strip()

    # Mostrar los símbolos no terminales detectados con sus frases
    if simbolos_detectados:
        for simbolo, frase in simbolos_detectados.items():
            print(f"{simbolo} = {frase}")
    else:
        print("No se detectaron símbolos no terminales en la frase.")


# Solicitar una frase al usuario
frase = input("Ingresa una frase: ")
detectar_simbolos_no_terminales(frase)