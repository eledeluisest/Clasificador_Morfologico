"""
Pruebas para generar la morfología con expresiones regulares
"""

# Que palabras de las 50 más frecuentes tienen etiqueta general.

informacion_de_etiquetado = []
for palabra, frecuencia in fdf:
    try:
        if resultado[palabra] == 'NCMS':
            informacion_de_etiquetado.append([palabra,frecuencia,resultado[palabra]])
    except:
        print(palabra)