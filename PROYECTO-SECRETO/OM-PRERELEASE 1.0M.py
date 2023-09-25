import tkinter as tk
import random
from PIL import Image, ImageTk
import pygame
import time

# AUDIO FONDO-------------------------------
def reproducir_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("fondo.mp3")
    pygame.mixer.music.play(-1)

def detener_audio():
    pygame.mixer.music.stop()

# BIEN AUDIO CONTROLES--------------------
def reproducir_bien():
    pygame.mixer.init()
    pygame.mixer.music.load("RECURSOS/bien.mp3")
    pygame.mixer.music.play(-1)
    
def detener_audio_bien():
    pygame.mixer.music.stop()

# MAL AUDIO CONTROLES--------------------
def reproducir_mal():
    pygame.mixer.init()
    pygame.mixer.music.load("RECURSOS/mal.mp3")
    pygame.mixer.music.play(-1)
    
def detener_audio_mal():
    pygame.mixer.music.stop()

# PREGUNTAS---------------------------------
# Define una lista de preguntas y respuestas en el formato adecuado
preguntas = [
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': '¿1?',
        'opciones': ['Madrid', 'París', 'Berlín', 'Londres'],
        'respuesta_correcta': 'París'
    },
    # ... (las demás preguntas)
]

# Variables globales
preguntas_disponibles = []
puntaje_actual = 0
pregunta_actual = None
imagen_pregunta_actual = None
imagen_respuesta_correcta = None
imagen_respuesta_incorrecta = None

# Función para abrir la ventana de juego
def abrir_ventana_juego(grado):
    global preguntas_disponibles, pregunta_actual, imagen_pregunta_actual, imagen_respuesta_correcta, imagen_respuesta_incorrecta, puntaje_actual
    # Filtrar preguntas según el grado seleccionado
    preguntas_disponibles = [pregunta for pregunta in preguntas if pregunta['grado'] == grado]

    if not preguntas_disponibles:
        # Si no hay preguntas disponibles para el grado, mostrar un mensaje y salir
        tk.messagebox.showinfo("Olimpiadas de Matemáticas", "No hay preguntas disponibles para este grado.")
        terminar_juego()

    # Inicializar la lista de botones de opciones
    botones_opciones = []

    def mostrar_pregunta():
        nonlocal botones_opciones  # Usar nonlocal para modificar la variable externa
        global pregunta_actual, imagen_pregunta_actual
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
        global puntaje_actual, imagen_respuesta_correcta, imagen_respuesta_incorrecta
        if pregunta_actual['respuesta_correcta'] == respuesta:
            resultado_texto.config(text='¡Respuesta Correcta!', fg='green')
            puntaje_actual += 10
            puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")  # Actualizar puntaje visual
            mostrar_imagen_respuesta(imagen_respuesta_correcta)
        else:
            resultado_texto.config(text='Respuesta Incorrecta', fg='red')
            mostrar_imagen_respuesta(imagen_respuesta_incorrecta)
        siguiente_boton.config(state=tk.NORMAL)
        

    def mostrar_imagen_respuesta(imagen_respuesta):
        resultado_ventana = tk.Toplevel()
        resultado_ventana.attributes('-fullscreen', True)
        resultado_ventana.overrideredirect(True)  # Sin bordes ni barra de título

        # Configurar el fondo de la ventana emergente
        fondo_label_resultado = tk.Label(resultado_ventana, image=imagen_respuesta)
        fondo_label_resultado.pack(expand=True, fill="both")

        # Centrar la ventana emergente
        resultado_ventana.update_idletasks()
        width = resultado_ventana.winfo_width()
        height = resultado_ventana.winfo_height()
        x = (resultado_ventana.winfo_screenwidth() // 2) - (width // 2)
        y = (resultado_ventana.winfo_screenheight() // 2) - (height // 2)
        resultado_ventana.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        # Reproducir el sonido correspondiente
        if imagen_respuesta == imagen_respuesta_correcta:
            reproducir_bien()
        elif imagen_respuesta == imagen_respuesta_incorrecta:
            reproducir_mal()

        # Programar una llamada para detener el sonido y cerrar la ventana después de 1,5 segundos
        resultado_ventana.after(1500, lambda: detener_audio_y_cerrar(resultado_ventana))

    def detener_audio_y_cerrar(ventana_a_cerrar):
        detener_audio_bien()
        detener_audio_mal()
        ventana_a_cerrar.destroy()

    def terminar_juego():
        pregunta_texto.config(text='¡JUEGO TERMINADO!')
        for boton in botones_opciones:
            boton.config(state=tk.DISABLED)
        terminar_boton.config(state=tk.DISABLED)
        
        if puntaje_actual <= 20:
         resultado_texto.config(fg='red')
        else:
            resultado_texto.config(fg='green')

        resultado_texto.config(text=f'Puntaje final: {puntaje_actual}', font=('Arial', 30))
        ventana_juego.after(3000, ventana_juego.destroy)

    def avanzar_pregunta():
        siguiente_boton.config(state=tk.DISABLED)
        resultado_imagen.pack_forget()  # Ocultar la imagen de respuesta
        resultado_texto.config(text='', fg='white')

        mostrar_pregunta()

    # Crear la ventana de juego
    ventana_juego = tk.Toplevel()
    ventana_juego.title(grado)
    ventana_juego.attributes('-fullscreen', True)

    # Configurar el fondo de imagen para la ventana de juego
    imagen_fondo_juego = Image.open('RECURSOS/fondo_juego.png')  # Ruta de la imagen de fondo
    imagen_fondo_juego = ImageTk.PhotoImage(imagen_fondo_juego)

    # Crear una etiqueta para mostrar la imagen de fondo
    fondo_label_juego = tk.Label(ventana_juego, image=imagen_fondo_juego)
    fondo_label_juego.place(x=0, y=0, relwidth=1, relheight=1)
    fondo_label_juego.image = imagen_fondo_juego  # Evita que la imagen se elimine por el recolector de basura
    fondo_label_juego.lower()

    # Etiqueta para mostrar la pregunta o imagen
    pregunta_texto = tk.Label(ventana_juego, text='', font=('Arial', 20))
    pregunta_texto.pack(pady=10)

    # Imagen de la pregunta
    pregunta_imagen = tk.Label(ventana_juego)
    pregunta_imagen.pack()

    # Etiqueta para mostrar el texto debajo de la imagen
    texto_debajo_imagen = tk.Label(ventana_juego, text='', font=('Arial', 12))
    texto_debajo_imagen.pack(pady=5)

    # Frame para las opciones
    opciones_frame = tk.Frame(ventana_juego)
    opciones_frame.pack()

    botones_opciones = []
    for i in range(4):
        boton = tk.Button(opciones_frame, text='', font=('Arial', 12), command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]), borderwidth=7, width=40, bg='salmon', highlightbackground='blue')
        botones_opciones.append(boton)
        boton.grid(row=i // 2, column=i % 2, pady=5, padx=10)  # Diseño de 2 arriba y 2 abajo

    resultado_texto = tk.Label(ventana_juego, text='', font=('Arial', 20))
    resultado_texto.pack(pady=10)

    resultado_imagen = tk.Label(ventana_juego)  # Para mostrar la imagen de respuesta

    siguiente_boton = tk.Button(ventana_juego, text='Siguiente', font=('Arial', 20),  bg='lightblue', width=40, command=avanzar_pregunta)
    siguiente_boton.pack(pady=10)
    siguiente_boton.config(state=tk.DISABLED)

    puntaje_label = tk.Label(ventana_juego, text=f"Puntaje actual: {puntaje_actual}", font=('Arial', 25))
    puntaje_label.pack(pady=10)

    terminar_boton = tk.Button(ventana_juego, text='TERMINAR JUEGO', font=('Arial', 12),  bg='red', width=40, command=terminar_juego)
    terminar_boton.pack(pady=10)

    # Iniciar el juego mostrando la primera pregunta
    mostrar_pregunta()

    # Cargar imágenes de respuesta
    imagen_respuesta_correcta = Image.open('RECURSOS/bien.png')  # Ruta de la imagen de respuesta correcta
    imagen_respuesta_correcta = ImageTk.PhotoImage(imagen_respuesta_correcta)
    imagen_respuesta_incorrecta = Image.open('RECURSOS/mal.png')  # Ruta de la imagen de respuesta incorrecta
    imagen_respuesta_incorrecta = ImageTk.PhotoImage(imagen_respuesta_incorrecta)

def chao():
    oli_titulo.config(text='¡JUEGO TERMINADO!')
    etiqueta_grado.config(text='GRACIAS POR JUGAR :D')
    ventana_inicio.after(1000, ventana_inicio.destroy)

# Ventana de inicio para seleccionar el grado
ventana_inicio = tk.Tk()
ventana_inicio.title('Olimpiadas de matemáticas')
ventana_inicio.attributes('-fullscreen', True)

icono = tk.PhotoImage(file="RECURSOS/icono.png")
# Establecerlo como ícono de la ventana.
ventana_inicio.iconphoto(True, icono)

# Configurar el fondo de imagen para la ventana de inicio
imagen_fondo_inicio = Image.open('RECURSOS/fondo_inicio.png')  # Reemplaza 'fondo_inicio.png' con la ruta de tu imagen de fondo para la ventana de inicio
imagen_fondo_inicio = ImageTk.PhotoImage(imagen_fondo_inicio)
fondo_label_inicio = tk.Label(ventana_inicio, image=imagen_fondo_inicio)
fondo_label_inicio.place(x=0, y=0, relwidth=1, relheight=1)

oli_titulo = tk.Label(ventana_inicio, text='OLIMPIADAS DE MATEMATICAS', bg="white", fg="black", pady=20, font=('bold', 50))
oli_titulo.pack(pady=10)

etiqueta_grado = tk.Label(ventana_inicio, text='Selecciona el grado:', bg="white", fg="black", pady=20, font=('bold', 50))
etiqueta_grado.pack(pady=10)

boton_grado_9 = tk.Button(ventana_inicio, text='Grado 9°', bg="white", fg="black", font=('arial', 25), width=18, height=2, pady=2, command=lambda: abrir_ventana_juego(9))
boton_grado_9.pack(pady=15)

boton_grado_10 = tk.Button(ventana_inicio, text='Grado 10°', bg="white", fg="black", font=('arial', 25), width=18, height=2, command=lambda: abrir_ventana_juego(10))
boton_grado_10.pack(pady=15)

boton_grado_11 = tk.Button(ventana_inicio, text='Grado 11°', bg="white", fg="black", font=('arial', 25), width=18, height=2,  command=lambda: abrir_ventana_juego(11))
boton_grado_11.pack(pady=15)

terminar_boton = tk.Button(ventana_inicio, text='CERRAR JUEGO', font=('Arial', 12),  bg='red', width=40,  command=chao)
terminar_boton.pack(pady=10)

ventana_inicio.mainloop()