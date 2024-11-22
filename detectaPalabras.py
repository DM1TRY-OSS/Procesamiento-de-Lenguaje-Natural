import speech_recognition as sr
import spacy


def transcribir_audio(audio_path):
    # Convertir el audio a texto
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        return texto
    except sr.UnknownValueError:
        return "No se pudo entender el audio"
    except sr.RequestError:
        return "Error al conectarse al servicio de reconocimiento de voz"


def clasificar_palabras(texto):
    # Cargar el modelo de lenguaje en español
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)

    # Clasificar palabras
    clasificacion = {
        "Verbos": [],
        "Sustantivos": [],
        "Adjetivos": [],
        "Adverbios": []
    }

    for token in doc:
        if token.pos_ == "VERB":
            clasificacion["Verbos"].append(token.text)
        elif token.pos_ == "NOUN":
            clasificacion["Sustantivos"].append(token.text)
        elif token.pos_ == "ADJ":
            clasificacion["Adjetivos"].append(token.text)
        elif token.pos_ == "ADV":
            clasificacion["Adverbios"].append(token.text)

    return clasificacion


# Ruta al archivo de audio
ruta_audio = "C:\\Users\\rico_\\Downloads\\fraseUno.wav"

# Paso 1: Transcribir el audio
texto_transcrito = transcribir_audio(ruta_audio)
print("Texto transcrito:", texto_transcrito)

# Paso 2: Clasificar las palabras
if texto_transcrito not in ["No se pudo entender el audio", "Error al conectarse al servicio de reconocimiento de voz"]:
    resultado_clasificacion = clasificar_palabras(texto_transcrito)
    # Imprimir la clasificación con comillas alrededor de la cadena de palabras y saltos de línea
    for categoria, palabras in resultado_clasificacion.items():
        print(f'\n{categoria}: "{", ".join(palabras)}"')
else:
    print(texto_transcrito)
