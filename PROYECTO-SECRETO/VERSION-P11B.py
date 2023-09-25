import tkinter as tk
import random
from PIL import Image, ImageTk

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
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': '¿Cuál es la capital de Francia?',
        'imagen': 'pregunta1.png',
        'texto_debajo_imagen': 'holaaaaaaa',
        'opciones': ['3', '1', '2', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 10,
        'tipo': 'imagen',
        'pregunta': '¿Cuál de estas opciones es 1?',
        'imagen': 'pregunta1.png',
        'texto_debajo_imagen': 'holaaaaaaa',
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
]

# Variables globales
preguntas_disponibles = []
puntaje_actual = 0
pregunta_actual = None
imagen_pregunta_actual = None

# Función para abrir la ventana de juego
def abrir_ventana_juego(grado):
    global preguntas_disponibles, puntaje_actual, pregunta_actual, imagen_pregunta_actual
    # Filtrar preguntas según el grado seleccionado
    preguntas_disponibles = [pregunta for pregunta in preguntas if pregunta['grado'] == grado]

    if not preguntas_disponibles:
        # Si no hay preguntas disponibles para el grado, mostrar un mensaje y salir
        tk.messagebox.showinfo("Olimpiadas de Matemáticas", "No hay preguntas disponibles para este grado.")
        return

    def mostrar_pregunta():
        global pregunta_actual, puntaje_actual, imagen_pregunta_actual
        if preguntas_disponibles:
            pregunta_actual = random.choice(preguntas_disponibles)
            pregunta_texto.config(text=pregunta_actual['pregunta'])

            if pregunta_actual['tipo'] == 'imagen':
                imagen = Image.open(pregunta_actual['imagen'])
                imagen = imagen.resize((400, 300))
                imagen_pregunta_actual = ImageTk.PhotoImage(imagen)
                pregunta_imagen.config(image=imagen_pregunta_actual)
                pregunta_imagen.image = imagen_pregunta_actual
                pregunta_imagen.pack()

                # Mostrar el texto debajo de la imagen
                texto_debajo_imagen.config(text=pregunta_actual.get('texto_debajo_imagen', ''))

                # Mostrar las opciones de respuesta para preguntas de imagen
                opciones_frame.pack()
                for i in range(4):
                    botones_opciones[i].config(text=pregunta_actual['opciones'][i])
                    botones_opciones[i].config(state=tk.NORMAL)
            elif pregunta_actual['tipo'] == 'texto':
                pregunta_imagen.pack_forget()  # Ocultar la imagen si es una pregunta de texto
                texto_debajo_imagen.config(text='')  # Ocultar el texto debajo de la imagen
                opciones_frame.pack()  # Mostrar las opciones si es una pregunta de texto
                for i in range(4):
                    botones_opciones[i].config(text=pregunta_actual['opciones'][i])
                    botones_opciones[i].config(state=tk.NORMAL)

    def verificar_respuesta(respuesta):
        global puntaje_actual
        if pregunta_actual['respuesta_correcta'] == respuesta:
            resultado_texto.config(text='¡Respuesta Correcta!')
            puntaje_actual += 10
        else:
            resultado_texto.config(text='Respuesta Incorrecta')
        siguiente_boton.config(state=tk.NORMAL)
        preguntas_disponibles.remove(pregunta_actual)

    def terminar_juego():
        pregunta_texto.config(text='Juego Terminado')
        for boton in botones_opciones:
            boton.config(state=tk.DISABLED)
        resultado_texto.config(text=f'Puntaje final: {puntaje_actual}')

    # Crear la ventana de juego
    ventana_juego = tk.Toplevel()
    ventana_juego.title('Olimpiadas de matemáticas')

    # Etiqueta para mostrar la pregunta o imagen
    pregunta_texto = tk.Label(ventana_juego, text='', font=('Arial', 14))
    pregunta_texto.pack(pady=10)

    # Imagen de la pregunta
    pregunta_imagen = tk.Label(ventana_juego)
    pregunta_imagen.pack()

    # Etiqueta para mostrar el texto debajo de la imagen
    texto_debajo_imagen = tk.Label(ventana_juego, text='', font=('Arial', 12))
    texto_debajo_imagen.pack()

    # Frame para las opciones
    opciones_frame = tk.Frame(ventana_juego)
    opciones_frame.pack()

    botones_opciones = []
    for i in range(4):
        boton = tk.Button(opciones_frame, text='', font=('Arial', 12), command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]))
        botones_opciones.append(boton)
        boton.grid(row=i, column=0, pady=5)

    resultado_texto = tk.Label(ventana_juego, text='', font=('Arial', 12))
    resultado_texto.pack(pady=10)

    siguiente_boton = tk.Button(ventana_juego, text='Siguiente', font=('Arial', 12),  bg='lightblue', width=40, command=mostrar_pregunta)
    siguiente_boton.pack(pady=10)
    siguiente_boton.config(state=tk.DISABLED)

    # Iniciar el juego mostrando la primera pregunta
    mostrar_pregunta()

# Ventana de inicio para seleccionar el grado
ventana_inicio = tk.Tk()
ventana_inicio.title('Olimpiadas de matemáticas')
ventana_inicio.config(bg="red")

etiqueta_grado = tk.Label(ventana_inicio, text='Selecciona el grado:', bg="red",fg="white", pady=20, font=('bold', 50))
etiqueta_grado.pack(pady=10)

boton_grado_9 = tk.Button(ventana_inicio, text='Grado 9°', bg="black", fg="white", font=('arial', 15), width=18, height=3, pady=3, command=lambda: abrir_ventana_juego(9))
boton_grado_9.pack(pady=5)

boton_grado_10 = tk.Button(ventana_inicio, text='Grado 10°', bg="black", fg="white", font=('arial', 15), width=18, height=3, command=lambda: abrir_ventana_juego(10))
boton_grado_10.pack(pady=5)

boton_grado_11 = tk.Button(ventana_inicio, text='Grado 11°', bg="black", fg="white", font=('arial', 15), width=18, height=3,  command=lambda: abrir_ventana_juego(11))
boton_grado_11.pack(pady=5)

ventana_inicio.mainloop()
