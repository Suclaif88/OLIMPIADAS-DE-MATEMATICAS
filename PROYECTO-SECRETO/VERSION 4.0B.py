import os #libreria para limpiar la consola
import random #para dar aleatoriedad

import urllib.request #para traer la base de datos de internet

#Un .TSV son valores separados por tabulaciones y saltos de linea
TEXTOBASEDEPREGUNTAS = ''''''
renglones =[]

try:
    conexBD = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQUQRnF7k4i2NaOH7qFnLNi4qMG9F27-5rSLFBGpA1yU5JRzN8O8igK2cif5KjSOK9ujccDxQSnVcVF/pub?output=tsv";
    HTTP_response = urllib.request.urlopen(conexBD)
    for line in HTTP_response:
        renglones.append(line.decode("utf-8").replace("\n","").replace("\r","")) #Decodifica y elimina caracteres especiales para mostrar texto desde la base de datos

except:
    print("No hay conexion a internet, no se pudo cargar la BD :( ")
    exit()

#Variables------------
n_pregunta = 0

Base_de_Preguntas =[]
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

def escogerpregunta(n): #Escoge al azar en el rango de preguntas del banco
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

def mostrarpregunta(): #Muestar las preguntas
    BorrarConsola()

    print()
    print(pregunta)
    print("A)",opciones[0])
    print("B)",opciones[1])
    print("C)",opciones[2])
    print("D)",opciones[3])
    print()

def capturaRespuesta(): #Captura las respuestas del usuario cmparandolas con las diferentes variables

    respuestaUsuario = ""
    opcionesValidas = ["a","b","c","d"]

    while True:
        respuestaUsuario = input("INGRESE SU RESPUESTA > ").lower()
        if not (respuestaUsuario in opcionesValidas): #si la respuesta "not" esta en las validas imprime esto
            print("LA RESPUESTA NO ESTA ENTRE LAS OPCIONES VALIDAS, VUELVE A INTENTARLO")
            continue
        break
    return opcionesValidas.index(respuestaUsuario)

def jugar(): #Compara la respuesta diciendo si es correcta o no
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
    if(n_pregunta == cantidadedepreguntas): #En caso de acabar las preguntas termina el juego
        BorrarConsola()
        print("EL JUEGO A FINALIZADO")
        input("ENTER PARA CONTINUAR")
        break






#SRD ❤ VOB