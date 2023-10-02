#Este es un juego simple de preguntas y respuestas utilizando la biblioteca Tkinter de Python para crear la interfaz gráfica. El juego muestra una pregunta con cuatro opciones de respuesta. El usuario debe seleccionar una opción y se le dará una respuesta de si es correcta o incorrecta. El juego lleva un registro del puntaje actual del usuario y muestra el puntaje final al finalizar el juego

import tkinter as tk
import random

#Definir una pregunta y respuesta
7
pregunta = [
    {
        'pregunta':'¿Cuál es la capital de Francia?',
        'opciones':['Madrid','París','Berlín','Londres'],
        'respuesta_correcta':'París'
    },
    {
        'pregunta': '¿Cuál es el río más largo del mundo?',
        'opciones': ['Nilo', 'Amazonas','Yangtsé', 'Misisipi'],
        'respuesta_correcta': 'Amazonas'
    },
    {
        'pregunta': '¿Cuántos continentes hay en el mundo?',
        'opciones': ['5','6','7','8'],
        'respuesta_correcta': '5'
    },
    {
        'pregunta': '¿Quién fue el primer presidente de Estados Unidos?',
        'opciones': ['Obama','G.Washintong','Bush','Trump'],
        'respuesta_correcta':'G.Washintong'
    },
    {
        'pregunta': '¿En qué país se encuentra la Gran Muralla China?',
        'opciones': ['China','Japón','Corea del Sur','India'],
        'respuesta_correcta': 'China'
    },
    {
        'pregunta':'¿Cuál es el desierto más grande del mundo?',
        'opciones': ['Sahara','Gobi','Kalahari','Arabia'],
        'respuesta_correcta' : 'Sahara'
    },
    {
        'pregunta':'¿Cuál es el libro más vendido de la HIstoria después de la Biblia?',
        'opciones': ['Don Quijote', 'El Principito', 'Cien años de soledad', 'Harry Potter y la Piedra Filosofal'],
        'respuesta_correcta' : 'Don Quijote'
    },
    {
        'pregunta': '¿Cuál es el metal más abundante en la corteza terrestre?',
        'opciones': ['Aluminio', 'Hierro', 'Cobre', 'Plomo'],
        'respuesta_correcta': 'Aluminio'
    } 
]

def mostrar_pregunta():
    #Función para mostrar una nueva pregunta y opciones de respuesta
    global pregunta_actual, puntaje_actual, preguntas_disponibles
    resultado_texto.set('')
    if not preguntas_disponibles:
        #Si no hay más preguntas disponibles, mostrar mensaje y finalizar el juego.
        pregunta_texto.set('No hay más preguntas disponibles.')
        siguiente_boton.config(state=tk.DISABLED)
        terminar_juego()
        return
    pregunta_actual = random.choice(preguntas_disponibles)
    pregunta_texto.set(pregunta_actual['pregunta'])
    for i, opcion in enumerate(pregunta_actual['opciones']):
        botones_opciones[i].config(text=opcion)
    siguiente_boton.config(state=tk.DISABLED)
    puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")

def verificar_respuesta(respuesta):
    #Función para verificar la respuesta seleccionada por el usuario
    global pregunta_actual, puntaje_actual, preguntas_disponibles
    if pregunta_actual['respuesta_correcta'] == respuesta:
        resultado_texto.set('¡Respuesta Correcta!')
        puntaje_actual += 10
    else:
        resultado_texto.set('Respuesta Incorrecta')
    siguiente_boton.config(state=tk.NORMAL)
    #Eliminar la pregunta actual de la lsita de preguntas disponibles
    preguntas_disponibles.remove(pregunta_actual)
    
def terminar_juego():
    #Funcion para finalizar el juego y mostrar el puntaje final
    global puntaje_actual
    pregunta_texto.set('Juego Terminado')
    for boton in botones_opciones:
        boton.config(state=tk.DISABLED)
    resultado_texto.set(f'Puntaje final:{puntaje_actual}')
    
#Configuar la ventana principal
ventana= tk.Tk()
ventana.title('Juego de Preguntas y Respuestas')

#Crear una copia de la lista de preguntas disponibles al inicio del juego
preguntas_disponibles = pregunta.copy()

#Variable para llevar un registro de la pregunta actual
pregunta_actual = None

#Variable para mostrar la pregunta actual
pregunta_texto = tk.StringVar()
pregunta_label = tk.Label(ventana, textvariable=pregunta_texto, font=('Arial',14))
pregunta_label.pack(pady=10)

#Botones para opciones de respuesta
botones_opciones = []
for i in range(4):
    boton = tk.Button(ventana, text='', font=('Arial',12), command=lambda i=i:verificar_respuesta(pregunta_actual['opciones'][i]))
    botones_opciones.append(boton)
    boton.pack(pady=5)
    
#Variable para mostrar si la respuesta fue correcta o incorrecta
resultado_texto = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_texto,font=('Arial',12))
resultado_label.pack(pady=10)

#Botón "Siguiente"
siguiente_boton = tk.Button(ventana, text='Siguiente', font=('Arial',12),command=mostrar_pregunta)
siguiente_boton.pack(pady=10)
siguiente_boton.config(state=tk.DISABLED)

#Puntaje Actual
puntaje_actual = 0
puntaje_label = tk.Label(ventana, text=f"Puntaje actual: {puntaje_actual}",font=('Arial',12))
puntaje_label.pack(pady=10)

#Botón "Terminar Juego"
terminar_boton = tk.Button(ventana, text='Terminar Juego', font=('Arial',12), command=terminar_juego)
terminar_boton.pack(pady=10)

#Iniciar el juego
mostrar_pregunta()

#Iniciar el bucle principal de la aplicación
ventana.mainloop()