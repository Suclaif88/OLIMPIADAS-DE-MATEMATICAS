import tkinter

ventana = tkinter.Tk()
ventana.title('Olimpiadas de matematicas')
ventana.config(bg="red")

etiqueta = tkinter.Label (ventana, text="Olimpiadas de Matematicas ",bg="red",fg="white", pady=20, font=('bold', 50))
etiqueta.pack()

boton1 = tkinter.Button(ventana, text="Grado Noveno (9)", bg="black", fg="white", font=('arial', 15), width=18, height=3)
boton1.pack(pady=5)

boton1 = tkinter.Button(ventana, text="Grado Decimo (10)", bg="black", fg="white", font=('arial', 15), width=18, height=3)
boton1.pack(pady=5)

boton1 = tkinter.Button(ventana, text="Grado Once (11)", bg="black", fg="white", font=('arial', 15), width=18, height=3)
boton1.pack(pady=5)



ventana.mainloop()
