import random
import tkinter as tk

# Definimos la lista de preguntas, cada pregunta es una tupla con la pregunta, las opciones y la respuesta correcta
preguntas = [("¿Cuál es el resultado de 2 + 2?", ["a. 2", "b. 3", "c. 4", "d. 5"], "c"),
             ("¿Cuál es la raíz cuadrada de 16?", ["a. 2", "b. 4", "c. 6", "d. 8"], "b"),
             ("¿Cuál es el resultado de 3 * 5?", ["a. 8", "b. 12", "c. 15", "d. 18"], "c")]

# Mezclamos las preguntas de manera aleatoria
random.shuffle(preguntas)

class Cuestionario:
    def __init__(self, master):
        self.master = master
        self.preguntas = preguntas
        self.puntaje = 0
        self.numero_pregunta = 0
        
        self.lbl_pregunta = tk.Label(self.master, text="")
        self.lbl_pregunta.pack()
        
        self.opciones = []
        for i in range(4):
            opcion = tk.Button(self.master, text="", command=lambda i=i: self.verificar_respuesta(i))
            opcion.pack(fill=tk.X)
            self.opciones.append(opcion)
        
        self.lbl_resultado = tk.Label(self.master, text="")
        self.lbl_resultado.pack()
        
        self.siguiente_pregunta()
    
    def siguiente_pregunta(self):
        if self.numero_pregunta < len(self.preguntas):
            pregunta, opciones, respuesta = self.preguntas[self.numero_pregunta]
            
            self.lbl_pregunta.config(text=pregunta)
            random.shuffle(opciones)
            for i in range(4):
                self.opciones[i].config(text=opciones[i])
            
            self.respuesta_correcta = respuesta
            self.lbl_resultado.config(text="")
            self.numero_pregunta += 1
        else:
            self.mostrar_resultados()
    
    def verificar_respuesta(self, i):
        if self.opciones[i].cget("text") == self.respuesta_correcta:
            self.puntaje += 1
            self.lbl_resultado.config(text="¡Correcto!")
        else:
            self.lbl_resultado.config(text="Incorrecto. La respuesta correcta es la opción " + self.respuesta_correcta)
        self.siguiente_pregunta()
    
    def mostrar_resultados(self):
        resultado = "Tu puntaje final es: " + str(self.puntaje) + " de " + str(len(self.preguntas))
        self.lbl_pregunta.config(text=resultado)
        for opcion in self.opciones:
            opcion.pack_forget()

# Creamos la ventana principal y la instancia del cuestionario
root = tk.Tk()
root.title("Cuestionario de Opción Múltiple")
quiz = Cuestionario(root)

# Ejecutamos el bucle de eventos de la ventana
root.mainloop()