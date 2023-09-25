import tkinter as tk
import random
from PIL import Image, ImageTk
import tkinter.messagebox

# Define una lista de preguntas y respuestas en el formato adecuado
preguntas = [
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': '¿Cuál es la capital de Francia?',
        'opciones': ['Madrid', 'París', 'Berlín', 'Londres'],
        'respuesta_correcta': 'París'
    },
    {
        'grado': 10,
        'tipo': 'imagen',
        'nombre_imagen': 'PREGUNTA AQUI',
        'imagen': 'pregunta1.png',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '1'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': '¿Cuál es el símbolo del hierro?',
        'opciones': ['Fe', 'He', 'H', 'Ir'],
        'respuesta_correcta': 'Fe'
    },
    # Agrega más preguntas aquí en el mismo formato
]

# Variables globales
preguntas_disponibles = []
puntaje_actual = 0
pregunta_actual = None
imagen_pregunta_actual = None
pregunta_tipo = None

# Función para abrir la ventana de preguntas
def abrir_ventana_juego(grado):
    global preguntas_disponibles, puntaje_actual, pregunta_actual, imagen_pregunta_actual, pregunta_tipo
    # Filtrar preguntas según el grado seleccionado
    preguntas_disponibles = [pregunta for pregunta in preguntas if pregunta['grado'] == grado]

    if not preguntas_disponibles:
        # Si no hay preguntas disponibles para el grado, mostrar un mensaje y salir
        tk.messagebox.showinfo("Olimpiadas de Matemáticas", "No hay preguntas disponibles para este grado.")
        return

    ventana_juego = tk.Tk()
    ventana_juego.title('Olimpiadas de matemáticas')

    def cerrar_imagen_actual():
        global imagen_pregunta_actual
        if imagen_pregunta_actual:
            pregunta_label_imagen.config(image=None)
            pregunta_label_imagen.image = None
            pregunta_label_imagen.pack_forget()  # Ocultar el widget de la imagen
            texto_personalizado_label.pack_forget()  # Ocultar el widget del texto

    def mostrar_pregunta():
        global pregunta_actual, puntaje_actual, pregunta_tipo, imagen_pregunta_actual
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
        pregunta_texto.set(pregunta_actual['pregunta'])

        if pregunta_tipo == 'imagen':
            imagen_pregunta = Image.open(pregunta_actual['imagen'])
            imagen_pregunta = imagen_pregunta.resize((400, 300))
            imagen_pregunta_actual = ImageTk.PhotoImage(imagen_pregunta)
            pregunta_label_imagen.config(image=imagen_pregunta_actual)
            pregunta_label_imagen.image = imagen_pregunta_actual
            pregunta_label_imagen.pack()  # Mostrar el widget de la imagen

            # Configurar el texto personalizado encima de la imagen
            texto_personalizado = pregunta_actual.get('nombre_imagen', '')
            texto_personalizado_label.config(text=texto_personalizado)
            texto_personalizado_label.pack()
            for boton in botones_opciones:
                boton.config(state=tk.NORMAL)
        elif pregunta_tipo == 'texto':
            for i, opcion in enumerate(pregunta_actual['opciones']):
                botones_opciones[i].config(text=opcion)
                botones_opciones[i].config(state=tk.NORMAL)

        siguiente_boton.config(state=tk.DISABLED)
        puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")

    def verificar_respuesta(respuesta):
        global puntaje_actual
        if pregunta_actual['respuesta_correcta'] == respuesta:
            resultado_texto.set('¡Respuesta Correcta!')
            puntaje_actual += 10
        else:
            resultado_texto.set('Respuesta Incorrecta')
        siguiente_boton.config(state=tk.NORMAL)
        preguntas_disponibles.remove(pregunta_actual)  # Usar la pregunta almacenada para eliminarla

    def terminar_juego():
        global puntaje_actual, puntaje_label
        pregunta_texto.set('Juego Terminado')
        for boton in botones_opciones:
            boton.config(state=tk.DISABLED)
        resultado_texto.set(f'Puntaje final: {puntaje_actual}')
        puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")

    pregunta_texto = tk.StringVar()
    pregunta_label_texto = tk.Label(ventana_juego, textvariable=pregunta_texto, font=('Arial', 14))
    pregunta_label_texto.pack(pady=10)

    pregunta_label_imagen = tk.Label(ventana_juego)
    pregunta_label_imagen.pack(pady=10)

    # Etiqueta para mostrar el texto personalizado encima de la imagen
    texto_personalizado_label = tk.Label(ventana_juego, text='', font=('Arial', 14), bg='white')
    texto_personalizado_label.pack()

    botones_opciones = []
    for i in range(4):
        boton = tk.Button(ventana_juego, text='', font=('Arial', 12), command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]))
        botones_opciones.append(boton)
        boton.pack(pady=5)

    resultado_texto = tk.StringVar()
    resultado_label = tk.Label(ventana_juego, textvariable=resultado_texto, font=('Arial', 12))
    resultado_label.pack(pady=10)

    siguiente_boton = tk.Button(ventana_juego, text='Siguiente', font=('Arial', 12), command=mostrar_pregunta)
    siguiente_boton.pack(pady=10)
    siguiente_boton.config(state=tk.DISABLED)

    puntaje_label = tk.Label(ventana_juego, text=f"Puntaje actual: {puntaje_actual}", font=('Arial', 12))
    puntaje_label.pack(pady=10)

    # Iniciar el juego mostrando la primera pregunta
    mostrar_pregunta()

    ventana_juego.mainloop()

# Ventana de inicio para seleccionar el grado
ventana_inicio = tk.Tk()
ventana_inicio.title('Olimpiadas de matemáticas')
ventana_inicio.config(bg="red")

etiqueta_grado = tk.Label(ventana_inicio, text='Selecciona el grado:', bg="red",fg="white", pady=20, font=('bold', 50))
etiqueta_grado.pack(pady=10)

boton_grado_9 = tk.Button(ventana_inicio, text='Grado 9', bg="black", fg="white", font=('arial', 15), width=18, height=3, pady=3, command=lambda: abrir_ventana_juego(9))
boton_grado_9.pack(pady=5)

boton_grado_10 = tk.Button(ventana_inicio, text='Grado 10', bg="black", fg="white", font=('arial', 15), width=18, height=3, command=lambda: abrir_ventana_juego(10))
boton_grado_10.pack(pady=5)

boton_grado_11 = tk.Button(ventana_inicio, text='Grado 11', bg="black", fg="white", font=('arial', 15), width=18, height=3,  command=lambda: abrir_ventana_juego(11))
boton_grado_11.pack(pady=5)

ventana_inicio.mainloop()
