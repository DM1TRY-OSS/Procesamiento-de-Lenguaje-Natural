import PyPDF2

def leer_pdf(ruta_pdf):
    try:
        texto = ""
        with open(ruta_pdf, "rb") as archivo:
            lector_pdf = PyPDF2.PdfReader(archivo)
            for pagina in range(len(lector_pdf.pages)):
                texto += lector_pdf.pages[pagina].extract_text() or ""
        return texto
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_pdf}'.")
        return ""

def contar_frecuencias_colocaciones(texto, colocaciones):
    """Cuenta cuántas veces aparece cada colocación en el texto."""
    frecuencias = {}
    texto = texto.lower()  # Normalizar el texto a minúsculas

    for colocacion in colocaciones:
        colocacion_lower = colocacion.lower()
        frecuencias[colocacion] = texto.count(colocacion_lower)

    return frecuencias

def calcular_probabilidad_condicional(texto, colocaciones):
    """Calcula la probabilidad condicional de que la segunda palabra de cada colocación
    aparezca después de la primera."""
    probabilidades = {}
    frecuencias_palabras = {}
    texto = texto.lower()

    for colocacion in colocaciones:
        colocacion_lower = colocacion.lower()
        primera_palabra, segunda_palabra = colocacion_lower.split()
        frecuencia_bigrama = texto.count(colocacion_lower)
        frecuencia_primera = texto.count(primera_palabra)
        frecuencia_segunda = texto.count(segunda_palabra)

        # Guardar frecuencias de las palabras individuales
        frecuencias_palabras[primera_palabra] = frecuencia_primera
        frecuencias_palabras[segunda_palabra] = frecuencia_segunda

        # Calcular la probabilidad condicional evitando división por cero
        if frecuencia_primera > 0:
            probabilidad = frecuencia_bigrama / frecuencia_primera
        else:
            probabilidad = 0

        probabilidades[(primera_palabra, segunda_palabra)] = probabilidad

    return probabilidades, frecuencias_palabras

# Definición de ruta y colocaciones
ruta_pdf = "C:\\Users\\rico_\\OneDrive\\Escritorio\\tareas UnU\\PDF´S\\PROYECTO FINAL DATA WAREHOUSE 2.pdf"
colocaciones = [
    "Data Mart",
]

# Leer el contenido del PDF
texto_pdf = leer_pdf(ruta_pdf)
if not texto_pdf:
    print("El archivo PDF no contiene texto o no se pudo leer.")
    exit()

# Contar las frecuencias de las colocaciones
frecuencias_colocaciones = contar_frecuencias_colocaciones(texto_pdf, colocaciones)

print("Frecuencias de colocaciones:")
for colocacion, frecuencia in frecuencias_colocaciones.items():
    print(f"'{colocacion}': {frecuencia} apariciones")

# Encontrar la colocación con mayor frecuencia
colocacion_mas_frecuente = max(frecuencias_colocaciones, key=frecuencias_colocaciones.get)
print(f"\nLa colocación con más frecuencia es: '{colocacion_mas_frecuente}' "
      f"con {frecuencias_colocaciones[colocacion_mas_frecuente]} apariciones.")

# Calcular las probabilidades condicionales y frecuencias individuales
probabilidades_colocaciones, frecuencias_palabras = calcular_probabilidad_condicional(texto_pdf, colocaciones)

print("\nProbabilidades condicionales de colocaciones:")
for (primera_palabra, segunda_palabra), probabilidad in probabilidades_colocaciones.items():
    print(f"Hay una probabilidad del {probabilidad * 100:.2f}% que después de la palabra '{primera_palabra}'  "
          f"aparezca la palabra '{segunda_palabra}'.")

    # Imprimir frecuencias de las palabras individuales
    print(f"La palabra '{primera_palabra}' aparece {frecuencias_palabras[primera_palabra]} veces.")
    print(f"La palabra '{segunda_palabra}' aparece {frecuencias_palabras[segunda_palabra]} veces.")
    print(f"La frecuencia es = '{frecuencia/frecuencias_palabras[segunda_palabra]}'")
