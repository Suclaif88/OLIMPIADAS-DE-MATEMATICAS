import os #libreria para limpiar la consola
import random #para dar aleatoriedad

#Un .TSV son valores separados por tabulaciones y saltos de linea
TEXTOBASEDEPREGUNTAS = '''
¿Cual es la capital de Colombia? \tBogota\tCartagena\tCali\tBarranquilla
\n

¿Cual es la capital de Venezuela? \tCaracas\tMaracaibo\tBarquisimetro\tBolivar
\n

¿Cual es el simbolo del hierro? \tFe\tHe\tNa\tK
'''

n_pregunta = 0

Base_de_Preguntas =[]
renglones = TEXTOBASEDEPREGUNTAS.split("\n")
cantidadedepreguntas = len(renglones)

opciones = []
preguntaEscogida = []
pregunta = ""
respuesta = ""


for i in range(cantidadedepreguntas):
    if(renglones[i]==""):
        continue
    Base_de_Preguntas.append(renglones[i].split("\t"))

def BorrarConsola():
    os.system("cls" if os.name == "nt" else "clear")

def escogerpregunta(n):
    global opciones, pregunta, respuesta

    preguntaEscogida = Base_de_Preguntas[n]
    pregunta = preguntaEscogida[0]
    respuesta = preguntaEscogida[1]
    opciones = preguntaEscogida[1:]
    for i in range(4):
        random.shuffle(opciones)
    random.shuffle(opciones)
    print(opciones)
    return preguntaEscogida

def mostrarpregunta():
    BorrarConsola()

    print()
    print(pregunta)
    print("A)",opciones[0])
    print("B)",opciones[1])
    print("C)",opciones[2])
    print("D)",opciones[3])
    print()

def capturaRespuesta():

    respuestaUsuario = ""
    opcionesValidas = ["a","b","c","d"]

    while True:
        respuestaUsuario = input("INGRESE SU RESPUESTA > ").lower()
        if not (respuestaUsuario in opcionesValidas): #si la respuesta "not" esta en las validas imprime esto
            print("LA RESPUESTA NO ESTA ENTRE LAS OPCIONES VALIDAS, VUELVE A INTENTARLO")
            continue
        break
    return opcionesValidas.index(respuestaUsuario)

def jugar():
    global n_pregunta
    escogerpregunta(n_pregunta)
    mostrarpregunta()
    if(opciones[capturaRespuesta()]==respuesta):
        print("SU RESPUESTA ES CORRECTA")
        input("ENTER PARA CONTINUAR")
    else:
        print("SU RESPUESTA NO ES CORRECTA LA RESPUESTA CORRECTA ES: "+ respuesta)
        input("ENTER PARA CONTINUAR")
    
while True:
    try:
      jugar()
    except:
        pass
    n_pregunta += 1
    if(n_pregunta == cantidadedepreguntas):
        BorrarConsola()
        print("EL JUEGO A FINALIZADO")
        input("ENTER PARA CONTINUAR")
        break

#VOB