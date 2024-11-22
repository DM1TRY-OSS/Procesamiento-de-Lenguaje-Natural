import PyPDF2

def leer_pdf(ruta_pdf):
    texto = ""
    with open(ruta_pdf, "rb") as archivo:
        lector_pdf = PyPDF2.PdfReader(archivo)
        for pagina in range(len(lector_pdf.pages)):
            texto += lector_pdf.pages[pagina].extract_text()
    return texto

def contar_colocaciones(texto, colocaciones):
    frecuencias = {}
    texto = texto.lower()  # Convertir todo el texto a minúsculas para evitar diferencias
    for colocacion in colocaciones:
        colocacion_lower = colocacion.lower()  # Convertir cada colocación a minúsculas
        frecuencias[colocacion] = texto.count(colocacion_lower)
    return frecuencias

ruta_pdf = "C:\\Users\\rico_\\OneDrive\\Escritorio\\tareas UnU\\PDF´S\\acoedeon ordi pelon.pdf"

colocaciones = [
    "protocolo TCP",
    "protocolo BCP",
    "Echo request"
]

texto_pdf = leer_pdf(ruta_pdf)
frecuencias_colocaciones = contar_colocaciones(texto_pdf, colocaciones)

print("Frecuencias de colocaciones:")
for colocacion, frecuencia in frecuencias_colocaciones.items():
    print(f"{colocacion}: {frecuencia}")

colocacion_mas_frecuente = max(frecuencias_colocaciones, key=frecuencias_colocaciones.get)
print(f"\nLa colocación con más frecuencia es: '{colocacion_mas_frecuente}' con {frecuencias_colocaciones[colocacion_mas_frecuente]} apariciones.")