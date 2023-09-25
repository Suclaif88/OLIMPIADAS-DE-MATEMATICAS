# Definimos la lista de preguntas, cada pregunta es una tupla con la pregunta, las opciones y la respuesta correcta
preguntas = [("¿Cuál es el resultado de 2 + 2?", ["a. 2", "b. 3", "c. 4", "d. 5"], "c"),
             ("¿Cuál es la raíz cuadrada de 16?", ["a. 2", "b. 4", "c. 6", "d. 8"], "b"),
             ("¿Cuál es el resultado de 3 * 5?", ["a. 8", "b. 12", "c. 15", "d. 18"], "c")]

# Creamos una función para hacer preguntas al usuario y verificar si la respuesta es correcta
def hacer_pregunta(pregunta, opciones, respuesta_correcta):
    print(pregunta)
    for opcion in opciones:
        print(opcion)
    respuesta_usuario = input("Introduce la letra de la respuesta correcta: ")
    if respuesta_usuario == respuesta_correcta:
        print("¡Correcto!")
        return True
    else:
        print("Incorrecto. La respuesta correcta es la opción", respuesta_correcta)
        return False

# Iteramos a través de las preguntas y llamamos a la función hacer_pregunta para cada una
puntaje = 0
for pregunta in preguntas:
    if hacer_pregunta(*pregunta):
        puntaje += 1

# Mostramos el puntaje final
print("Tu puntaje final es:", puntaje, "de", len(preguntas))

#SEBAS ROLDAN