import tkinter as tk
import random
import PIL
from PIL import Image, ImageTk

# Define una lista de preguntas y respuestas en el formato adecuado
preguntas = [
    {
        'tipo': 'texto',
        'pregunta': '¿Cuál es la capital de Francia?',
        'opciones': ['Madrid', 'París', 'Berlín', 'Londres'],
        'respuesta_correcta': 'París'
    },
    {
        'tipo': 'imagen',
        'nombre_imagen': 'PREGUNTA AQUI',  # Título que deseas mostrar
        'imagen': 'pregunta1.png',  # Ruta de la imagen
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '1'
    },
    {
        'tipo': 'texto',
        'pregunta': '¿Cuál es el símbolo del hierro?',
        'opciones': ['Fe', 'He', 'H', 'Ir'],
        'respuesta_correcta': 'Fe'
    },
    # Agrega más preguntas aquí en el mismo formato
]

# Configura la ventana principal
ventana = tk.Tk()
ventana.title('Juego de Preguntas y Respuestas')

# Variables globales
preguntas_disponibles = preguntas.copy()
puntaje_actual = 0
pregunta_actual = None
imagen_pregunta_actual = None  # Variable para mantener la imagen actual
pregunta_tipo = None  # Variable para mantener el tipo de pregunta actual

pregunta_texto = tk.StringVar()
pregunta_label_texto = tk.Label(ventana, textvariable=pregunta_texto, font=('Arial', 14))
pregunta_label_texto.pack(pady=10)

pregunta_label_imagen = tk.Label(ventana)
pregunta_label_imagen.pack(pady=10)

# Etiqueta para mostrar el texto personalizado encima de la imagen
texto_personalizado_label = tk.Label(ventana, text='', font=('Arial', 14), bg='white')
texto_personalizado_label.pack()

def cerrar_imagen_actual():
    global imagen_pregunta_actual
    if imagen_pregunta_actual:
        pregunta_label_imagen.config(image=None, text='')  # Limpiar la imagen actual
        texto_personalizado_label.config(text='')  # Limpiar el texto personalizado
        pregunta_label_imagen.pack_forget()  # Ocultar el widget de la imagen
        texto_personalizado_label.pack_forget()  # Ocultar el widget del texto
        imagen_pregunta_actual = None  # Eliminar la referencia a la imagen

def mostrar_pregunta():
    global pregunta_actual, puntaje_actual, preguntas_disponibles, pregunta_tipo, imagen_pregunta_actual
    resultado_texto.set('')

    if not preguntas_disponibles:
        pregunta_texto.set('No hay más preguntas disponibles.')
        cerrar_imagen_actual()
        siguiente_boton.config(state=tk.DISABLED)
        terminar_juego()
        return
    
    cerrar_imagen_actual()  # Cerrar la imagen actual antes de cargar una nueva

    pregunta_actual = random.choice(preguntas_disponibles)
    pregunta_tipo = pregunta_actual['tipo']
    pregunta_texto.set(pregunta_actual['pregunta'] if pregunta_tipo == 'texto' else '')

    if pregunta_tipo == 'imagen':
        imagen_pregunta = Image.open(pregunta_actual['imagen'])
        imagen_pregunta = imagen_pregunta.resize((400, 300))
        imagen_pregunta_actual = ImageTk.PhotoImage(imagen_pregunta)
        nombre_imagen = pregunta_actual.get('nombre_imagen', '')  # Usar el título personalizado si está definido
        pregunta_label_imagen.config(image=imagen_pregunta_actual)
        pregunta_label_imagen.image = imagen_pregunta_actual
        pregunta_label_imagen.pack()  # Mostrar el widget de la imagen

        # Configurar el texto personalizado encima de la imagen
        texto_personalizado = pregunta_actual.get('nombre_imagen', '')
        texto_personalizado_label.config(text=texto_personalizado)
        texto_personalizado_label.pack()

    for i, opcion in enumerate(pregunta_actual['opciones']):
        botones_opciones[i].config(text=opcion)

    siguiente_boton.config(state=tk.DISABLED)
    puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")

def verificar_respuesta(respuesta):
    global puntaje_actual, preguntas_disponibles
    pregunta_actual_temp = pregunta_actual  # Almacenar la pregunta actual antes de verificar la respuesta
    if pregunta_actual_temp['respuesta_correcta'] == respuesta:
        resultado_texto.set('¡Respuesta Correcta!')
        puntaje_actual += 10
    else:
        resultado_texto.set('Respuesta Incorrecta')
    siguiente_boton.config(state=tk.NORMAL)
    preguntas_disponibles.remove(pregunta_actual_temp)  # Usar la pregunta almacenada para eliminarla

def terminar_juego():
    global puntaje_actual, puntaje_label
    pregunta_texto.set('Juego Terminado')
    for boton in botones_opciones:
        boton.config(state=tk.DISABLED)
    resultado_texto.set(f'Puntaje final: {puntaje_actual}')
    puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")

botones_opciones = []
for i in range(4):
    boton = tk.Button(ventana, text='', font=('Arial', 12), command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]))
    botones_opciones.append(boton)
    boton.pack(pady=5)

resultado_texto = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_texto, font=('Arial', 12))
resultado_label.pack(pady=10)

siguiente_boton = tk.Button(ventana, text='Siguiente', font=('Arial', 12), command=mostrar_pregunta)
siguiente_boton.pack(pady=10)
siguiente_boton.config(state=tk.DISABLED)

puntaje_label = tk.Label(ventana, text=f"Puntaje actual: {puntaje_actual}", font=('Arial', 12))
puntaje_label.pack(pady=10)

# Iniciar el juego
mostrar_pregunta()

ventana.mainloop()