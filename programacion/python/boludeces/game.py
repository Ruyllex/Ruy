'''
juego:
consite en mandar True o False si los colores acertan al nombre
'''
#-----------imports--------------
import random
import os
import time
import matplotlib.pyplot as plt
import tkinter

#----------------------------------------------


lista_intervalo_tiempo = []
lista_intentos = []
lista_colores = ["azul","violeta","amarillo","rojo","verde","celeste","blanco"]
diccionario_numeros_colores = {"azul":34, "amarillo":33,"rojo":31,"verde":32,"violeta":35,"blanco":37,"celeste":36}

values = diccionario_numeros_colores.values()

keys = diccionario_numeros_colores.keys()
diccionario_alreves = dict(zip(values,keys))
os.system('clear')
#-----------------reglas-----------------------
print("Las reglas del juego son:\n  1.Presiona Enter si el color no coincide con la palabra\n  2.Si el color, si coincide con la palabra escribi algo y presiona enter\n  3.Los aciertos suman 1 punto y los desaciertos restan 1 punto\n  4.Solo se pueden tener 3 desaciertos\n  5.Podes perder por tiempo tenes solo 60segundos")
print("  6.Si te cansaste de jugar escribi la palara FIN para salir de la partida")
print("Un ejemplo:")
ejemplo_correcto = print('   Coincide:\033[31m rojo \033[0m (en este caso presiona enter)')
ejemplo_incorrecto = print('   NO Coincide:\033[33m violeta \033[0m (en este caso escribi algo y presiona enter)')

#-----------------constantes-------------------
start = input("Presiona enter para empezar")
respuesta = ""
inicio = time.time()
puntos = 0
fallas = 0
intentos = 0
cant_max_desaciertos = 3
#---------------------------------------------
os.system('clear')
tiempo = inicio - inicio
while respuesta.lower() != "fin" and fallas != cant_max_desaciertos and tiempo <= 60:
    palabra = random.choice(lista_colores)
    color = str(diccionario_numeros_colores[random.choice(lista_colores)])
    pregunta = '\033[' + color + 'm' + palabra + '\033[m  ' + str(puntos)
    print(pregunta)
    inicio_intervalo = time.time()
    respuesta = input("respuesta: ")
    intentos += 1
    fin_intervalo = time.time()
    lista_intervalo_tiempo.append(fin_intervalo - inicio_intervalo)
    os.system('clear')
    if respuesta != '':
        if palabra == diccionario_alreves[int(color)]:
            puntos += 1 
        else:
            puntos -= 1
            fallas += 1
    else:
        if palabra == diccionario_alreves[int(color)]:
            puntos -= 1
            fallas += 1
        else:
            puntos += 1
    tiempo_final = time.time()
    tiempo = tiempo_final - inicio
    
tiempo_por_punto = str(format((60/puntos),".2f"))
Mas_rapido = str(format(min(lista_intervalo_tiempo),".2f"))
Mas_lento = str(format(max(lista_intervalo_tiempo),".2F"))

if fallas == 3:
    print("perdiste por fallas, tus puntos fueron: ",str(puntos))
    print("Tu reacción mas rápida fue de: ",Mas_rapido)
    print("Tu reacción mas lenta fue de: ",Mas_lento)
    
else:
    if puntos <= 60:
        print("Estas bastante lento, tu promedio es mas de un segundo.")
        print("obtuviste",str(puntos),"puntos")
        print("El promedio de tiempo por jugada fue de: ",tiempo_por_punto,"segundos por punto")
        print("Tu reacción mas rapida fue de: ",Mas_rapido,"segundos")
        print("Tu reacción mas lenta fue de: ",Mas_lento,"segundos")
    if puntos > 60 and puntos < 100:
        print("Estas dentro del promedio.")    
        print("otuviste: ",str(puntos),"puntos")
        print("El promedio de tiempo por jugada fue de: ",tiempo_por_punto,"segundos por punto")
        print("Tu reacción mas rapida fue de: ",Mas_rapido,"segundos")
        print("Tu reacción mas lenta fue de: ",Mas_lento,"segundos")
    if puntos > 100:
        print("wow, sos flash")
        print("tardaste",tiempo_por_punto,"segundos por punto")
        print("Obtuviste ",puntos,"puntos")
        print("Tu reacción mas rapida fue de: ",Mas_rapido,"segundos")
        print("Tu reacción mas lenta fue de: ",Mas_lento,"segundos")

pregunta_grafico = input("Deseas ver un grafico de las reacciones?(escribi ver y enter para mostrar grafico)")
for i in range(0,intentos):
    lista_intentos.append(i)
if pregunta_grafico == "ver":
    plt.plot(lista_intentos,lista_intervalo_tiempo)
    plt.xlabel("Intentos")
    plt.ylabel("Tiempo por intento")
    plt.show()









