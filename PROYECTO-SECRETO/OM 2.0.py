import tkinter as tk
import random
from PIL import Image, ImageTk
import pygame

def sonido():
    pygame.mixer.init()

    fondo_musical = pygame.mixer.Sound("PROYECTO-SECRETO/RECURSOS/fondo.mp3")

    canal_fondo = pygame.mixer.Channel(0)

    canal_fondo.set_volume(0.5)

    canal_fondo.play(fondo_musical, loops=-1)

sonido()

def detener_audio():
    pygame.mixer.music.stop()

def reproducir_bien():
    pygame.mixer.init()
    pygame.mixer.music.load("PROYECTO-SECRETO/RECURSOS/bien.mp3")
    pygame.mixer.music.play(-1)

def detener_audio_bien():
    pygame.mixer.music.stop()

def reproducir_mal():
    pygame.mixer.init()
    pygame.mixer.music.load("PROYECTO-SECRETO/RECURSOS/mal.mp3")
    pygame.mixer.music.play(-1)

def detener_audio_mal():
    pygame.mixer.music.stop()
    
preguntas = [
    {
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': 'En el siguiente gráfico, ¿cuántos cerillos se deben mover, como mínimo, para obtener 5 cuadrados de un cerillo por lado?',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p13.png',
        'texto_debajo_imagen': '',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'Sabemos que de 4 corredores de la maratón C llegó después de B y el corredor D llegó en medio de los corredores A y C. ¿Cuál fue el orden correcto en el que llegaron los corredores a la meta?',
        'opciones': ['DCAB', 'BDCA', 'BCDA', 'ADCB'],
        'respuesta_correcta': 'BCDA'
    },
    {
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': '¿Cuántas fichas como mínimo, deben ser cambiadas de posición para que el resultado sea 2?',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p15.png',
        'texto_debajo_imagen': '',
        'opciones': ['3', '1', '2', '4'],
        'respuesta_correcta': '2'
    },
]

preguntas_disponibles = []
puntaje_actual = 0
pregunta_actual = None
imagen_pregunta_actual = None
imagen_respuesta_correcta = None
imagen_respuesta_incorrecta = None
preguntas_respondidas = set()

def abrir_ventana_juego(grado):
    global preguntas_disponibles, pregunta_actual, imagen_pregunta_actual, imagen_respuesta_correcta, imagen_respuesta_incorrecta, puntaje_actual, tiempo_inicial, tiempo_restante
    
    preguntas_disponibles = [pregunta for pregunta in preguntas if pregunta['grado'] == grado]

    puntaje_actual = 0
    botones_opciones = []
    preguntas_respondidas.clear()
    
    def mostrar_pregunta():
     nonlocal botones_opciones
     global pregunta_actual, imagen_pregunta_actual, preguntas_disponibles
        
     if preguntas_disponibles:
        pregunta_actual = random.choice([pregunta for pregunta in preguntas_disponibles if pregunta['pregunta'] not in preguntas_respondidas])
        preguntas_respondidas.add(pregunta_actual['pregunta'])
        pregunta_texto.config(text=pregunta_actual['pregunta'], wraplength=1000)
        
        for boton in botones_opciones:
            boton.config(state=tk.DISABLED)
        
        for boton in botones_opciones:
            boton.destroy()
        botones_opciones = []
        
        opciones = pregunta_actual['opciones']
        random.shuffle(opciones)
                
        opciones_frame.pack()
        opciones = pregunta_actual['opciones']
        num_opciones = len(opciones)
        for i in range(num_opciones):
            opcion = opciones[i]
            if isinstance(opcion, str) and opcion.lower().endswith('.png'):
                imagen_opcion = Image.open(opcion)
                imagen_opcion = imagen_opcion.resize((250, 150))
                imagen_width, imagen_height = imagen_opcion.size
                imagen_opcion = ImageTk.PhotoImage(imagen_opcion)
                boton = tk.Button(opciones_frame, text="", image=imagen_opcion, compound="center", width=imagen_width, height=imagen_height, command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]))
                boton.image = imagen_opcion
            else:
                boton = tk.Button(opciones_frame, text=opcion, font=('Arial', 12), width=30, height=2, command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]))
            boton.grid(row=i // 2, column=i % 2, pady=5, padx=10)
            botones_opciones.append(boton)
            boton.config(bg='OliveDrab1', fg='black', highlightbackground='blue', borderwidth=7, font=('Berlin Sans FB', 15))
            
        if pregunta_actual['tipo'] == 'imagen':
            pregunta_imagen.config(state=tk.NORMAL)
            imagen = Image.open(pregunta_actual['imagen'])
            imagen = imagen.resize((400, 300))
            imagen_pregunta_actual = ImageTk.PhotoImage(imagen)
            pregunta_imagen.config(image=imagen_pregunta_actual)
            texto_debajo_imagen.config(text=pregunta_actual.get('texto_debajo_imagen', ''), wraplength=400)
            pregunta_imagen.pack(pady=20)
            
        elif pregunta_actual['tipo'] == 'texto':
            pregunta_imagen.config(image='')
            texto_debajo_imagen.config(text='')
        siguiente_boton.config(state=tk.DISABLED)
        
    def verificar_respuesta(respuesta):
        global puntaje_actual, imagen_respuesta_correcta, imagen_respuesta_incorrecta
        if pregunta_actual['respuesta_correcta'] == respuesta:
            resultado_texto.config(text='¡Respuesta Correcta!', fg='green')
            puntaje_actual += 10
            puntaje_label.config(text=f"Puntaje actual: {puntaje_actual}")
            mostrar_imagen_respuesta(imagen_respuesta_correcta)
        else:
            resultado_texto.config(text='Respuesta Incorrecta', fg='red')
            mostrar_imagen_respuesta(imagen_respuesta_incorrecta)
        siguiente_boton.config(state=tk.NORMAL)

    def mostrar_imagen_respuesta(imagen_respuesta):
        resultado_ventana = tk.Toplevel()
        resultado_ventana.attributes('-fullscreen', True)
        resultado_ventana.overrideredirect(True)
        fondo_label_resultado = tk.Label(resultado_ventana, image=imagen_respuesta)
        fondo_label_resultado.pack(expand=True, fill="both")
        resultado_ventana.update_idletasks()
        width = resultado_ventana.winfo_width()
        height = resultado_ventana.winfo_height()
        x = (resultado_ventana.winfo_screenwidth() // 2) - (width // 2)
        y = (resultado_ventana.winfo_screenheight() // 2) - (height // 2)
        resultado_ventana.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        if imagen_respuesta == imagen_respuesta_correcta:
            reproducir_bien()
            resultado_ventana.after(2000, lambda: detener_audio_y_cerrar(resultado_ventana))
        elif imagen_respuesta == imagen_respuesta_incorrecta:
            reproducir_mal()
            resultado_ventana.after(3100, lambda: detener_audio_y_cerrar(resultado_ventana))   

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
        puntaje_label.config(text='')
        texto_debajo_imagen.config(text='')
        pregunta_imagen.pack_forget()
        empezar_tiempo.config(state=tk.DISABLED)
        cronometro.config(text="00:00")
        empezar_tiempo.config(bg="orange red")
        ventana_juego.after(500, ventana_juego.destroy)#---------cambiar 2000
 #SRD ❤ VOB
    def avanzar_pregunta():
     global puntaje_actual, imagen_respuesta_correcta, imagen_respuesta_incorrecta, tiempo_restante
     if not preguntas_disponibles:
        for boton in botones_opciones:
                boton.config(state=tk.DISABLED)
        siguiente_boton.config(state=tk.DISABLED)
        resultado_imagen.pack_forget()
        resultado_texto.config(text='', fg='black')
        pregunta_texto.config(text='¡NO QUEDAN MAS PREGUNTAS DISPONIBLES!')
        resultado_texto.config(text=f'Puntaje final: {puntaje_actual}', font=('Arial', 30))
        puntaje_label.config(text='')
        texto_debajo_imagen.config(text='')
        empezar_tiempo.config(state=tk.DISABLED)
        empezar_tiempo.config(bg="orange red")
        cronometro.config(text="00:00")
        if puntaje_actual <= 20:
            resultado_texto.config(fg='red')
        else:
            resultado_texto.config(fg='green')
     elif len(preguntas_respondidas) == len(preguntas_disponibles):
        for boton in botones_opciones:
                boton.config(state=tk.DISABLED)
        siguiente_boton.config(state=tk.DISABLED)
        resultado_imagen.pack_forget()
        resultado_texto.config(text='', fg='black')
        pregunta_texto.config(text='¡NO QUEDAN MAS PREGUNTAS DISPONIBLES!')
        resultado_texto.config(text=f'Puntaje final: {puntaje_actual}', font=('Arial', 30))
        puntaje_label.config(text='')
        texto_debajo_imagen.config(text='')
        pregunta_imagen.pack_forget()
        empezar_tiempo.config(state=tk.DISABLED)
        empezar_tiempo.config(bg="orange red")
        cronometro.config(text="00:00")
        if puntaje_actual <= 20:
            resultado_texto.config(fg='red')
        else:
            resultado_texto.config(fg='green')
     else:
        siguiente_boton.config(state=tk.DISABLED)
        resultado_imagen.pack_forget()
        resultado_texto.config(text='', fg='white')
        cronometro.config(fg="black")
        pregunta_texto.config(fg='black')
        empezar_tiempo.config(state=tk.NORMAL)
        empezar_tiempo.config(bg="lawn green")
        cronometro.config(text="01:00")
        reiniciar_tiempo()
        mostrar_pregunta()
    
    def iniciar_tiempo():
        global tiempo_restante, tiempo_iniciado
        tiempo_iniciado = True
        tiempo_restante = tiempo_inicial
        empezar_tiempo.config(state=tk.DISABLED)
        empezar_tiempo.config(bg="orange red")
        actualizar_cronometro()
        
    def reiniciar_tiempo():
        global tiempo_restante, tiempo_iniciado
        tiempo_restante = tiempo_inicial
        tiempo_iniciado = False
    
    def actualizar_cronometro():
        global tiempo_restante, tiempo_iniciado
        
        minutos = tiempo_restante // 60
        segundos = tiempo_restante % 60

        cronometro.config(text=f"{minutos:02}:{segundos:02}")
    
        if tiempo_restante > 0 and tiempo_iniciado:
         tiempo_restante -= 1
         ventana_juego.after(1000, actualizar_cronometro)
         
        elif tiempo_restante != 0:
         reiniciar_tiempo()
            
        else:
          tiempo_terminado()

    ventana_juego = tk.Toplevel()
    ventana_juego.title(grado)
    ventana_juego.attributes('-fullscreen', True)
    
    tiempo_inicial = 60
    tiempo_restante = tiempo_inicial
    
    cronometro = tk.Label(ventana_juego, text="01:00", bg="gray85", fg="black", font=('arial', 25), width=14, height=2)
    cronometro.pack()
    cronometro.place(relx=0.97, rely=0.32, anchor=tk.SE)
    
    empezar_tiempo = tk.Button(ventana_juego, text='>>>', font=('Arial', 20), bg="lawn green", command=iniciar_tiempo)
    empezar_tiempo.pack(pady=2)
    empezar_tiempo.place(relx=0.90, rely=0.41, anchor=tk.SE)
    
    def tiempo_terminado():
     for boton in botones_opciones:
        boton.config(state=tk.DISABLED)
     siguiente_boton.config(state=tk.NORMAL)
     cronometro.config(fg='red')
     pregunta_texto.config(fg='red')
     pygame.mixer.init()
     pygame.mixer.music.load("PROYECTO-SECRETO/RECURSOS/tiempo_acabado.mp3")
     pygame.mixer.music.play(1)

    imagen_fondo_juego = Image.open('PROYECTO-SECRETO/RECURSOS/fondo_juego.png')
    imagen_fondo_juego = ImageTk.PhotoImage(imagen_fondo_juego)

    fondo_label_juego = tk.Label(ventana_juego, image=imagen_fondo_juego)
    fondo_label_juego.place(x=0, y=0, relwidth=1, relheight=1)
    fondo_label_juego.image = imagen_fondo_juego
    fondo_label_juego.lower()
    
    pregunta_imagen = tk.Label(ventana_juego)
    pregunta_texto = tk.Label(ventana_juego, text='', font=('Arial', 20), bg='misty rose')
    texto_debajo_imagen = tk.Label(ventana_juego, text='', font=('Arial', 20), bg='misty rose')
    resultado_texto = tk.Label(ventana_juego, text='', font=('Arial', 20))
    resultado_imagen = tk.Label(ventana_juego)
    siguiente_boton = tk.Button(ventana_juego, text='Siguiente', font=('Arial', 20),  bg='lightblue', width=40, command=avanzar_pregunta)
    puntaje_label = tk.Label(ventana_juego, text=f"Puntaje actual: {puntaje_actual}", font=('Arial', 25))
    terminar_boton = tk.Button(ventana_juego, text='TERMINAR JUEGO', font=('Arial', 12), bg='Orchid1', width=40, command=terminar_juego)
    opciones_frame = tk.Frame(ventana_juego)
    
    botones_opciones = []
    for i in range(4):
        boton = tk.Button(opciones_frame, text='', font=('Arial', 12), command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]), borderwidth=7, width=40, bg='salmon', highlightbackground='blue')
        botones_opciones.append(boton)
        boton.grid(row=i // 2, column=i % 2, pady=5, padx=10)

    imagen_respuesta_correcta = Image.open('PROYECTO-SECRETO/RECURSOS/bien.png')
    imagen_respuesta_correcta = ImageTk.PhotoImage(imagen_respuesta_correcta)
    imagen_respuesta_incorrecta = Image.open('PROYECTO-SECRETO/RECURSOS/mal.png')
    imagen_respuesta_incorrecta = ImageTk.PhotoImage(imagen_respuesta_incorrecta)
    
    pregunta_texto.pack(padx=10, pady=10)

    pregunta_imagen.pack(padx=10, pady=10)
    
    texto_debajo_imagen.pack(padx=10, pady=10)
    
    opciones_frame.pack(padx=10, pady=10)
    
    resultado_texto.pack(padx=10, pady=10)
    
    puntaje_label.pack(padx=10, pady=10)
    
    siguiente_boton.pack(padx=10, pady=10)
    siguiente_boton.config(state=tk.DISABLED)
    
    terminar_boton.pack(padx=10, pady=10)
    
    if not preguntas_disponibles:
         for boton in botones_opciones:
                boton.config(state=tk.DISABLED)
         siguiente_boton.config(state=tk.DISABLED)
         resultado_imagen.pack_forget()
         resultado_texto.config(text='', fg='black')
         pregunta_texto.config(text='¡NO HAY PREGUNTAS DISPONIBLES PARA ESTE GRADO!')
         resultado_texto.config(text=f'Puntaje final: {puntaje_actual}', font=('Arial', 30))
         puntaje_label.config(text='')
         texto_debajo_imagen.config(text='')
         empezar_tiempo.config(state=tk.DISABLED)
         empezar_tiempo.config(bg="orange red")
         cronometro.config(text="00:00")
    else:
     mostrar_pregunta()

def chao():
    oli_titulo.config(text='¡JUEGO TERMINADO!')
    etiqueta_grado.config(text='GRACIAS POR JUGAR :D')
    ventana_inicio.after(200, ventana_inicio.destroy)#------------cambiar 1000

ventana_inicio = tk.Tk()
ventana_inicio.title('Olimpiadas de matemáticas')
ventana_inicio.attributes('-fullscreen', True)

icono = tk.PhotoImage(file="PROYECTO-SECRETO/RECURSOS/icono.png")
ventana_inicio.iconphoto(True, icono)

imagen_fondo_inicio = Image.open('PROYECTO-SECRETO/RECURSOS/fondo_inicio.png')
imagen_fondo_inicio = ImageTk.PhotoImage(imagen_fondo_inicio)
fondo_label_inicio = tk.Label(ventana_inicio, image=imagen_fondo_inicio)
fondo_label_inicio.place(x=0, y=0, relwidth=1, relheight=1)

oli_titulo = tk.Label(ventana_inicio, text='OLIMPIADAS DE MATEMATICAS 2023', bg="white", fg="black", pady=20, font=('Broadway', 40))
oli_titulo.pack(pady=10)

etiqueta_grado = tk.Label(ventana_inicio, text='Selecciona el grado:', bg="white", fg="black", pady=20, font=('Broadway', 40))
etiqueta_grado.pack(pady=10)

boton_grado_9 = tk.Button(ventana_inicio, text='Grado 9°', bg="lightgoldenrod1", fg="black", font=('Broadway', 25), width=18, height=2, pady=2, command=lambda: abrir_ventana_juego(9))
boton_grado_9.pack(pady=15)

boton_grado_10 = tk.Button(ventana_inicio, text='Grado 10°', bg="lightgoldenrod1", fg="black", font=('Broadway', 25), width=18, height=2, command=lambda: abrir_ventana_juego(10))
boton_grado_10.pack(pady=15)

boton_grado_11 = tk.Button(ventana_inicio, text='Grado 11°', bg="lightgoldenrod1", fg="black", font=('Broadway', 25), width=18, height=2,  command=lambda: abrir_ventana_juego(11))
boton_grado_11.pack(pady=15)

boton_final = tk.Button(ventana_inicio, text="FINAL", bg="lightgoldenrod1", fg="black", font=('Broadway', 20), width=18, height=2, command=lambda: abrir_ventana_juego(4))
boton_final.place(relx=0.8, rely=0.6, anchor=tk.CENTER)

boton_empate = tk.Button(ventana_inicio, text="EMPATE", bg="lightgoldenrod1", fg="black", font=('Broadway', 20), width=18, height=2, command=lambda: abrir_ventana_juego(2))
boton_empate.place(relx=0.2, rely=0.6, anchor=tk.CENTER)

terminar_boton = tk.Button(ventana_inicio, text='CERRAR JUEGO', font=('Broadway', 12),  bg='Orchid1', width=40,  command=chao)
terminar_boton.pack(pady=10)

ventana_inicio.mainloop()