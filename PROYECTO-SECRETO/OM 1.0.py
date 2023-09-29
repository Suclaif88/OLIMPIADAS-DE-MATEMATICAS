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
        'tipo': 'texto',
        'pregunta': 'Sabemos que de 4 corredores de la maratón C llegó después de B y el corredor D llegó en medio de los corredores A y C. ¿Cuál fue el orden correcto en el que llegaron los corredores a la meta?',
        'opciones': ['DCAB', 'BDCA', 'BCDA', 'ADCB'],
        'respuesta_correcta': 'BCDA'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'En un grupo la suma del número de mujeres con el de varones es 40 y su diferencia es 10 por lo tanto el grupo tiene:',
        'opciones': ['20 y 20', '25 y 15', '28 y 12', '30 y 10'],
        'respuesta_correcta': '25 y 15'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'El área de la puerta de un edificio mide 4,32 m^2 y su altura es de 2,40 m ¿Cuánto mide su ancho?',
        'opciones': ['1,80 m', '2,00 m', '1,50 m', '1,90 m'],
        'respuesta_correcta': '1,80 m'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': '¿Cuál es el resultado de √4%?',
        'opciones': ['0.02%', '0,2%', '20%', '2%'],
        'respuesta_correcta': '20%'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Un ladrillo más medio ladrillo vale 90 pesos. ¿Cuánto  costarán 10 ladrillos',
        'opciones': ['900 pesos', '300 pesos', '600 pesos', '450 pesos'],
        'respuesta_correcta': '600 pesos'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': '2 personas pintan una casa en 36 horas, si esta labor la realizan 6 personas ¿en  cuánto tiempo la pintarian?',
        'opciones': ['24 horas', '48 horas', '72 horas', '12 horas'],
        'respuesta_correcta': '12 horas'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'A un evento académico asisten 20 profesores de la I.E. "A"; 25 profesores de la I.E. "B"; y 30 de la I.E. "C". Se elige por sorteo a un delegado. ¿Cuál es la probabilidad de que el profesor elegido sea de la I.E. "A"?',
        'opciones': ['4/15', '4/5', '2/3', '1/5'],
        'respuesta_correcta': '4/15'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': '1, 8, 27, 36, 125, 216, ¿Cuál de estos números no pertenece a la sucesión?',
        'opciones': ['216', '36', '125', '8'],
        'respuesta_correcta': '36'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': '22C, 42F, 62I, ... ¿Cuál sigue en la sucesión?',
        'opciones': ['82L', '82O', '82N', '82M'],
        'respuesta_correcta': '82L'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'AMERICA = 1734651, INDIA = 68961, CANADA = ?, ¿Cómo se escribiria Canadá de acuerdo con las representaciones?',
        'opciones': ['715148', '519581', '518191', '719181'],
        'respuesta_correcta': '518191'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'En una clase un profesor pregunta a sus alumnos si le entendieron una explicación, a lo cual uno de ellos contesta: "Todos no entendimos", por lo tanto el profesor puede deducir que:',
        'opciones': ['Todos entendieron', 'Ninguno entendio', 'Algunos entendieron', 'No todos entendieron'],
        'respuesta_correcta': 'Algunos entendieron'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'Un atleta sale a entrenar a las 9:00 a.m a una velocidad de 10 km/h. Media hora después sale en su persecusión otro atleta a una velocidad de 12 km/h. La hora en la cual el segundo atleta alcanza al primero es ',
        'opciones': ['12:00 m', '11:30 m', '11:00 m', '10:30 m'],
        'respuesta_correcta': '12:00 m'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'En una fabrica se empacan botellas en cajas de dos tipos, en las que un tipo caben exactamente 5 botellas y en las del otro tipo caben exactamente 9 botellas. El mínimo número de cajas que se deben usar para empacar totalmente 100 botellas es:',
        'opciones': ['10', '11', '12', '15'],
        'respuesta_correcta': '12'
    },
    {
        
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Héctor ha gastado el 40% de sus ahorros y le han dado a su hermana el 30% de lo que aún tenia. El porcentaje que conserva Héctor de sus ahorros es:',
        'opciones': ['25%', '30%', '42%', '38%'],
        'respuesta_correcta': '42%'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'En el siguiente conjunto de datos: 18, 18, 19, 17, 23, 20, 21, 18. La mediana es:',
        'opciones': ['17.5', '18', '18.5', '19'],
        'respuesta_correcta': '18.5'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'En un estanque hay 100 pares de peces, nacen dos pares de peces por cada pez en el estanque, 350 de los peces que nacen se llevan a un río. ¿Cuántos peces quedarían en el estanque?',
        'opciones': ['550', '450', '650', '250'],
        'respuesta_correcta': '650'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'En una textilera se tiene un corte de dril de 64 metros: si cada día se venden cuatro metros, entonces el tiempo que tardarán en cortar toda la pieza es:',
        'opciones': ['14 días', '15 días', '16 días', '17 días'],
        'respuesta_correcta': '15 días'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'Una máquina tiene 5 bolas rojas, 4 bolas blancas y 5 bolas amarilas. ¿Cuántas monedas de $100 se deben echar en la máquina para que al menos se hayan sacado 2 bolas de igual color, sabiendo que para sacar dos bolas se necesita 1 moneda?',
        'opciones': ['2', '4', '3', '7'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'Si el peso de una persona es 60 kilogramos más la mitad de su propio peso, entonces la ecuación que relaciona los x kilogramos que pasa la persona es',
        'opciones': ['X/2=30', 'X/2=60', 'X=(30+X)/2', 'X=(60+X)/2'],
        'respuesta_correcta': 'X/2=60'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': '"Todos los celulares son rojos", es lo mismo que afirmar:',
        'opciones': ['Algunos celulares son rojos', 'Algunos celulares son negros', 'No todos los celulares son blancos', 'No hay celulares que no sean rojos'],
        'respuesta_correcta': 'No hay celulares que no sean rojos'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': '"Existe un número primo par" es lo mismo que afirmar:',
        'opciones': ['No todos los primos son impares', 'Algunos primos no son pares', 'Todos los primos son pares', 'Hay primos que no son pares'],
        'respuesta_correcta': 'No todos los primos son impares'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'Un estudiante recibe su primer título sólo si pasa todos sus exámenes y presenta todos sus trabajos. De 300 estudiantes, 250 pasaron todos los exámens y 215 presentaron todos los trabajos. ¿Cuántos estudiantes recibieron su primer título?',
        'opciones': ['Por lo menos 215', 'A lo sumo 185', 'Exactamente 215', 'Por lo menos 165'],
        'respuesta_correcta': 'Por lo menos 165'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Una fabrica que trabaja a un ritmo constante produce 20 automóviles en 4 días. ¿Cúantos automóviles es posible fabricar en tres fabricas similares, que trabajan al mismo ritmo, en 6 días?',
        'opciones': ['60', '80', '90', '120'],
        'respuesta_correcta': '90'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'Cierto día Mauricio afirma: la hermana de mi tío no es mi tía. Si lo afirma Mauricio es cierto, ¿a quién se estará refiriendo?',
        'opciones': ['A su hija', 'A su madre', 'A su esposa', 'A su hermana'],
        'respuesta_correcta': 'A su madre'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'Se sabe que un remedio casero funciona en 25 de cada 60 perosnas. ¿Qué probabilidad hay que funcione si me aplico el remdio?',
        'opciones': ['15%', '45%', '35%', '60%'],
        'respuesta_correcta': '25%'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': '¿Cuántos cortes se deben hacer como mínimo para que un pastel quede dividido en 8 partes iguales?',
        'opciones': ['2', '3', '4', '5'],
        'respuesta_correcta': '4'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'La fabrica de leche "Luna Azul", aumentó el precio de cada litro un 5%, si el costo anterios era de $4000, ¿Cuál es el pprecio actual del litro de leche?',
        'opciones': ['$4200', '$4500', '$4100', '$4400'],
        'respuesta_correcta': '$4200'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'En una tienda se reciben 7 cajas de refresco 3 veces a la semana. Si cada caja contiene 24 refrescos, ¿cuántos refrescos se reciben en un mes?',
        'opciones': ['504', '168', '2016', '2060'],
        'respuesta_correcta': '2016'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Una bici avanza 144 mts en un minuto, a velocidad constante. ¿Qué distancia recorrerá en 1/6 de hora?',
        'opciones': ['144 mts', '1440 mts', '148mts', '1480 mts'],
        'respuesta_correcta': '1440'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'Un tren de pasajeros se compone de doce vagones. Cada vagón tiene seis compartimientos y cada compartimiento tiene seis lugares para viajar sentado; ¿cuántos pasajeros pueden viajar sentados en el tren?',
        'opciones': ['342', '172', '422', '432'],
        'respuesta_correcta': '432'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': '¿Cuál es el menor número de caramelos de 65 centavos de dólar que se pueden comprar con monedas de 1 dólar sin recibir cambio?',
        'opciones': ['20', '18', '15', '10'],
        'respuesta_correcta': '20'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Felipe tiene tres docenas y medias de canicas; al jugar pierde 18 canicas y posteriormente le regalan una docena, ¿cuántas le quedaron?',
        'opciones': ['34', '30', '36', '24'],
        'respuesta_correcta': '36'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'Cinco amigos se encuentran en la calle y se saludan de mano, ¿cuántos apretones de mano hubo en total?',
        'opciones': ['10', '15', '20', '25'],
        'respuesta_correcta': '10'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'Un estudiante realiza las operaciones de un problema en su calculadora y redondeo el resultado a 48,2. El redondeo lo hizo respecto a las céntimas más proximas. ¿Cuál de los siguientes números es el más aproximado al que obtuvo en la calculadora?',
        'opciones': ['48,141', '48,269', '48,189', '48,043'],
        'respuesta_correcta': '48,189'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Si se desea hacer una rifa de una nevera en la que cada boleta tiene un número de tres cifras, ¿cuántas boletas se deben imprimir?',
        'opciones': ['100', '1000', '300', '3000'],
        'respuesta_correcta': '1000'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'Al curso de razonamiento lógico asisten 45 estudiantes donde hay 10 alumnas que tiene cabello rubio, 20 alumnas que tiene el cabello negro, 5 hombres que tiene cabello rubio y 10 hombres tiene el cabello negro La probabilidad de que un alumno sea hombre es:',
        'opciones': ['1/3', '2/3', '3/4', '1/2'],
        'respuesta_correcta': '1/3'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'En la siguiente secuencia: 54, 49, X, 39, 34... El número que se debe remplazar por X es:',
        'opciones': ['47', '44', '45', '42'],
        'respuesta_correcta': '44'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Determine el valor de "X+Y" en la sucesión: 14; 11; 13; 12; 12; 13; 11; 14; X; Y',
        'opciones': ['30', '25', '20', '23'],
        'respuesta_correcta': '25'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'Carlos y Rocio deciden verse a las 8 p.m. Carlos tiene un reloj 15 minutos adelantado y Rocio 15 minutos atrasados . Si Carlos llega a la cita 15 minutos antes según su reloj y Rocio llega 15 minutos retrasada según su reloj. ¿Cuánto tiempo esperó Carlos?',
        'opciones': ['15 min', '30 min', '45 min', '60 min'],
        'respuesta_correcta': '60 min'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'Ely le dice a Lenin: Si el pasado mañana de ayer es jueves, ¿qué día será el anteayer, del ayer del mañana?',
        'opciones': ['Miercoles', 'Martes', 'Lunes', 'Domingo'],
        'respuesta_correcta': 'Lunes'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Se tiene una caja con 5 esferas blancas, 3 azules y 4 verdes. ¿Cuántas esferas, como mínimo, se tendrán que extraer al azar para tener la certeza de haber extraído una esfera blanca?',
        'opciones': ['6', '5', '8', '9'],
        'respuesta_correcta': '8'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'Un policía sabe que, de un grupo de 20 personas reunidas en una fiesta, hay 12 que son culpables de un robo, pero no sabe cuáles son. ¿Cuántas personas deben arrestar como mínimo, para tener la seguridad de llevar a un culpable?',
        'opciones': ['8', '9', '12', '7'],
        'respuesta_correcta': '9'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': '¿Cuántos cuartos son seis mitades?',
        'opciones': ['8 cuartos', '10 cuartos', '12 cuartos', '18 cuartos'],
        'respuesta_correcta': '12 cuartos'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Un hombre se come un lechón en un minuto y medio. ¿Cuántos hombres se necesitan para comer 60 lechones en media hora?',
        'opciones': ['9', '30', '3', '6'],
        'respuesta_correcta': '3'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'Si 5 máquinas hacen 5 artículos en 5 minutos. ¿Cuánto tiempo necesitarán 100 máquinas para hacer 100 artículos?',
        'opciones': ['5 minutos', '20 minutos', '30 minutos', '100 minutos'],
        'respuesta_correcta': '5 minutos'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'En una habitación se encuentran 4 gatos. Cada gato está en un rincón y ve a otros 3 felinos. ¿Cuántos gatos hay en la habitación?',
        'opciones': ['4', '12', '16', '9'],
        'respuesta_correcta': '4'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Si 5 máquinas hacen 5 artículos en 5 minutos. ¿Cuánto tiempo necesitarán 100 máquinas para hacer 100 artículos?',
        'opciones': ['5 minutos', '20 minutos', '30 minutos', '100 minutos'],
        'respuesta_correcta': '5 minutos'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'En una caja hay 5 bolas numeradas del 1 al 5. Se extrae al azar una bola de la caja se restituye y se repite la operación dos veces más. Se registra (de izquierda a derecha) los números de las bolas que van saliendo, según el orden de salida de modo que resulte un número de tres cifras. ¿Cuántos diferentes de tres cifras pueden obtenerse de este modo',
        'opciones': ['60', '125', '85', '100'],
        'respuesta_correcta': '125'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'En una caja hay 6 bolas numeradas del 1 al 6. Se extraen al azar, una tras otra, tres bolas, sin restituir la bola que ha sido extraída, y se registran (de izquierda a derecha) los números de las bolas que van saliendo, según el orden de salida de modo que resulte un número de tres cifras. ¿Cuántos números diferentes de tres cifras pueden obtenerse de este modo?',
        'opciones': ['216', '124', '120', '180'],
        'respuesta_correcta': '120'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Arrojamos un dado y luego de ello arrojamos una moneda, ¿cuál será el número de resultados posibles de este experimento?',
        'opciones': ['7', '12', '72', '8'],
        'respuesta_correcta': '12'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'Un tren recorrió 240 km a una velocidad de 80 km/h. ¿Cuántos tiempo llevó realizar el viaje?',
        'opciones': ['3 horas', '4 horas', '2 horas y 30 minutos', '1 hora y 30 miutos'],
        'respuesta_correcta': '3 horas'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'En una caja había 20 sombreros blancos y 13 sombreros neros. Jorge extrajo al azar de la caja tres sombreros uno tras otro sin restituirlos a la caja, y los tres sombreros extraídos resultaron negros. ¿Cuál es la probabilidad de que el cuarto sombrero extraído al azar sea también negro?',
        'opciones': ['13/33', '10/33', '1/3', '1/33'],
        'respuesta_correcta': '1/3'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Dato: 2^X * 2^Y = 32. PRegunta: X+Y=?',
        'opciones': ['8', '7', '5', '4'],
        'respuesta_correcta': '5'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'Se tiene 4 cajas que contienen tornillos de 10 gramos cada uno y una caja que contiene tornillos de 11 gramos cada uno. ¿Cuántas pesadas como mínimo se necesitan hacer en una balanza de 2 platillos para determinar la caja que contiene los tornillos de mayor peso?',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '3'
    },
    {
        'grado': 9,
        'tipo': 'texto',
        'pregunta': 'Juan subió a un árbol que tenía naranjas y no bajó con naranjas. Si en el árbol no quedaron naranjas, ¿cuántas naranjas tenía inicialmente el árbol?',
        'opciones': ['0', '1', '2', '3'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 10,
        'tipo': 'texto',
        'pregunta': 'Se tiene 24 vasos iguales, de los cuales 8 están llenos de vino, 8 contienen vino hasta la mitad y 8 están vacíos. Cuatro personas deben repartirse dichos vasos, de manera que a cada una debe corresponderle la misma cantidad de vino y el mismo número de vasos. ¿Cuántos vasos vacíos le corresponderá a la persona que le toquen 2 vasos llenos de vino?',
        'opciones': ['1', '2', '3', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 11,
        'tipo': 'texto',
        'pregunta': 'En una familia, cada hermano tiene 4 hermanas y 4 hermanos, y cada hermana tiene 5 hermanos y 3 hermanas. ¿Cuántos hijos son en total?',
        'opciones': ['6', '8', '9', '10'],
        'respuesta_correcta': '9'
    },
    {
        'grado': 11,
        'tipo': 'mixta', 
        'pregunta': 'La negación del enunciado <<ningún A es B>>, representado en un diagrama es:',
        'opciones': ['PROYECTO-SECRETO/RECURSOS/54a.jpg', 'PROYECTO-SECRETO/RECURSOS/54b.jpg', 'PROYECTO-SECRETO/RECURSOS/54c.jpg', 'PROYECTO-SECRETO/RECURSOS/55d.jpg'],
        'respuesta_correcta': 'PROYECTO-SECRETO/RECURSOS/54b.jpg'
    },
    {
        'grado': 10,
        'tipo': 'imagen',
        'pregunta': 'De las figuras 1, 2, 3, 4, 5 y 6, la que representa la vista lateral izquierda de la figura inical es:',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p10.png',
        'texto_debajo_imagen': '',
        'opciones': ['2', '1', '5', '6'],
        'respuesta_correcta': '1'
    },
    {
        'grado': 11,
        'tipo': 'imagen',
        'pregunta': '¿Qué número debe reemplazar el signo de interrogación?',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p9.png',
        'texto_debajo_imagen': '',
        'opciones': ['1', '3', '6', '8'],
        'respuesta_correcta': '1'
    },
    {
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': 'William miro en el espejo para ver la hora que marcaba el reloj, y esto es lo que vio:',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p8.png',
        'texto_debajo_imagen': 'Pero el reloj había sido colgado al revés. ¿Qué hora es en realidad',
        'opciones': ['las 10:00', 'Las 8:00', 'Las 2:00', 'Las 4:00'],
        'respuesta_correcta': 'Las 4:00'
    },
    {
        'grado': 10,
        'tipo': 'imagen',
        'pregunta': 'La cantidad de triángulos de igual tamaño de la figura 1 que tendrían la figura 12, siguiendo con el patrón dado es:',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p7.png',
        'texto_debajo_imagen': '',
        'opciones': ['3', '1', '2', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 11,
        'tipo': 'imagen',
        'pregunta': 'Un trozo de madera ha sido marcado en cuadrados iguales. ¿Cuántos cortes rectos deberán realizarse como mínimo, de modo que todos los cuadrados que contiene las letras estén separados?',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p5.png',
        'texto_debajo_imagen': '',
        'opciones': ['2 como mínimo', '3 como minimo', '4 como mínimo', '5 como mínimo'],
        'respuesta_correcta': '3 como minimo'
    },
    {
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': '¿Cuántas monedas como mínimo se debe mover, para que la figura (I) se convierta en la figura (II)?',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p6.png',
        'texto_debajo_imagen': '',
        'opciones': ['2', '3', '4', '5'],
        'respuesta_correcta': '3'
    },
    {
        'grado': 10,
        'tipo': 'imagen',
        'pregunta': '¿Qué número falta?',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p1.png',
        'texto_debajo_imagen': '',
        'opciones': ['1231', '1332', '1331', '1321'],
        'respuesta_correcta': '1331'
    },
    {
        'grado': 11,
        'tipo': 'imagen',
        'pregunta': 'Halla el área de la figura',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p4.png',
        'texto_debajo_imagen': '',
        'opciones': ['80 m^2', '88 m^2', '92 m^2', '96 m^2'],
        'respuesta_correcta': '88 m^2'
    },
    {
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': 'Se presenta:',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p3.png',
        'texto_debajo_imagen': '',
        'opciones': ['1000', '1210', '200', '4010'],
        'respuesta_correcta': '200'
    },
    {
        'grado': 10,
        'tipo': 'imagen',
        'pregunta': 'En una encuesta aplicada a 40 estudiantes se obtuvo los siguientes resultados',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p2.png',
        'texto_debajo_imagen': '¿Qué porcentaje de alumnos prefieren el área de comunicación?',
        'opciones': ['20%', '30%', '40%', '35%'],
        'respuesta_correcta': '30%'
    },
    {
        'grado': 11,
        'tipo': 'imagen',
        'pregunta': 'El número de cuadrados que hay en la figura es:',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p11.png',
        'texto_debajo_imagen': '',
        'opciones': ['19', '11', '30', '29'],
        'respuesta_correcta': '11'
    },
    {
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': '',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p16.png',
        'texto_debajo_imagen': '',
        'opciones': ['9 kg', '10kg', '11 kg', '12'],
        'respuesta_correcta': '12'
    },
    {
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': 'Un trozo de cartón tiene la forma de la figura mostrada (las regiones m, n, p , q, r son cuadrados) y se dobla a lo largo de las líneas punteadas para formar una caja abierta.',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p12.png',
        'texto_debajo_imagen': 'Si la caja se coloca en una mesa de manera que la parte abierta quede hacía arriba. ¿Qué región constituye la base de la caja?',
        'opciones': ['p', 'q', 'r', 'm'],
        'respuesta_correcta': 'p'
    },
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
        'tipo': 'imagen',
        'pregunta': 'En el gráfico, ¿cuál es la menor cantidad de cerillos que se deben mover para formar exactamente 4 cuadrados iguales?',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p14.png',
        'texto_debajo_imagen': '',
        'opciones': ['3', '1', '2', '4'],
        'respuesta_correcta': '2'
    },
    {
        'grado': 9,
        'tipo': 'imagen',
        'pregunta': '¿Cuántas fichas como mínimo, deben ser cambiadas de posición para que el resultado sea 2?',
        'imagen': 'PROYECTO-SECRETO/RECURSOS/p15.png',
        'texto_debajo_imagen': '',
        'opciones': ['3', '1', '2', '4'],
        'respuesta_correcta': '2'
    },#--74--
    {
      'grado': 4,
      'tipo': 'texto',
      'pregunta': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      'opciones': ['1', '2', '3', '4'],
      'respuesta_correcta': '2'
    },
    {
      'grado': 2,
      'tipo': 'texto',
      'pregunta': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      'opciones': ['1', '2', '3', '4'],
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
     global pregunta_actual, imagen_pregunta_actual
        
     if preguntas_disponibles:
        pregunta_actual = random.choice([pregunta for pregunta in preguntas_disponibles if pregunta['pregunta'] not in preguntas_respondidas])
        preguntas_respondidas.add(pregunta_actual['pregunta'])
        pregunta_texto.config(text=pregunta_actual['pregunta'], wraplength=1000)
        pregunta_imagen.pack_forget()
        texto_debajo_imagen.config(text='')
        for boton in botones_opciones:
            boton.destroy()
        botones_opciones = []
        
        opciones = pregunta_actual['opciones']
        random.shuffle(opciones)
        
        if pregunta_actual['tipo'] == 'imagen':
            imagen = Image.open(pregunta_actual['imagen'])
            imagen = imagen.resize((400, 300))
            imagen_pregunta_actual = ImageTk.PhotoImage(imagen)
            pregunta_imagen.config(image=imagen_pregunta_actual)
            pregunta_imagen.image = imagen_pregunta_actual
            pregunta_imagen.pack()
            texto_debajo_imagen.config(text=pregunta_actual.get('texto_debajo_imagen', ''), wraplength=400)
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
        ventana_juego.after(3000, ventana_juego.destroy)
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
        pregunta_imagen.pack_forget()
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
        cronometro.config(text="01:30")
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
    
    tiempo_inicial = 90
    tiempo_restante = tiempo_inicial
    
    cronometro = tk.Label(ventana_juego, text="01:30", bg="gray85", fg="black", font=('arial', 25), width=14, height=2)
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

    pregunta_texto = tk.Label(ventana_juego, text='', font=('Arial', 20), bg='misty rose')
    pregunta_texto.pack(pady=10)

    pregunta_imagen = tk.Label(ventana_juego)
    pregunta_imagen.pack()

    texto_debajo_imagen = tk.Label(ventana_juego, text='', font=('Arial', 12))
    texto_debajo_imagen.pack(pady=5)

    opciones_frame = tk.Frame(ventana_juego)
    opciones_frame.pack()

    botones_opciones = []
    for i in range(4):
        boton = tk.Button(opciones_frame, text='', font=('Arial', 12), command=lambda i=i: verificar_respuesta(pregunta_actual['opciones'][i]), borderwidth=7, width=40, bg='salmon', highlightbackground='blue')
        botones_opciones.append(boton)
        boton.grid(row=i // 2, column=i % 2, pady=5, padx=10)

    resultado_texto = tk.Label(ventana_juego, text='', font=('Arial', 20))
    resultado_texto.pack(pady=10)

    resultado_imagen = tk.Label(ventana_juego)

    siguiente_boton = tk.Button(ventana_juego, text='Siguiente', font=('Arial', 20),  bg='lightblue', width=40, command=avanzar_pregunta)
    siguiente_boton.pack(pady=10)
    siguiente_boton.config(state=tk.DISABLED)

    puntaje_label = tk.Label(ventana_juego, text=f"Puntaje actual: {puntaje_actual}", font=('Arial', 25))
    puntaje_label.pack(pady=10)

    terminar_boton = tk.Button(ventana_juego, text='TERMINAR JUEGO', font=('Arial', 12), bg='Orchid1', width=40, command=terminar_juego)
    terminar_boton.pack(pady=10)

    imagen_respuesta_correcta = Image.open('PROYECTO-SECRETO/RECURSOS/bien.png')
    imagen_respuesta_correcta = ImageTk.PhotoImage(imagen_respuesta_correcta)
    imagen_respuesta_incorrecta = Image.open('PROYECTO-SECRETO/RECURSOS/mal.png')
    imagen_respuesta_incorrecta = ImageTk.PhotoImage(imagen_respuesta_incorrecta)
    
    mostrar_pregunta()

def chao():
    oli_titulo.config(text='¡JUEGO TERMINADO!')
    etiqueta_grado.config(text='GRACIAS POR JUGAR :D')
    ventana_inicio.after(1000, ventana_inicio.destroy)

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