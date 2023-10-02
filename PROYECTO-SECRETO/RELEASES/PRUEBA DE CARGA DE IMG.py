import tkinter as tk
from PIL import Image, ImageTk
# Prueba de carga de imágenes
test_window = tk.Tk()
imagen_bien = Image.open('RECURSOS/bien.png')
imagen_mal = Image.open('RECURSOS/mal.png')

label_bien = tk.Label(test_window, image=ImageTk.PhotoImage(imagen_bien))
label_bien.pack()

label_mal = tk.Label(test_window, image=ImageTk.PhotoImage(imagen_mal))
label_mal.pack()

test_window.mainloop()
