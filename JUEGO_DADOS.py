#carreras con dados

def maxi(valores):
    mayor=valores[0]
    for i in range(1, len(valores)):
        if valores[i]> mayor:
            mayor=valores[i]

    return mayor


import random

print("BIENVENIDOS A CARRERAS DE DADOS ")

jugadores=[]
player=int(input("Cuantos van a jugar? "))
puntosT=int(input("Ingrese el puntaje ganador: "))
for i in range(player):
    jugadores.append(input("ingrese la inicial de tu nombre: "))

contador=[]
for i in range(player):
    contador.append(0)    
puntajeMax=maxi(contador)

print(puntajeMax)

while puntajeMax<=puntosT:
   
    for i in range(player):
        print("-------------------")
        print("turno de ",jugadores[i])
        resp=input("listo para tirar el dado?: (S/N)")
        RESP=resp.upper()
        if RESP=="S":
            dado=random.randrange(1,6)
            contador[i]+=dado
            print("sumaste ",dado," puntos!!")
            print("TOTAL ",contador[i]," PUNTOS")
        puntajeMax=maxi(contador)
WIN=contador.index(puntajeMax)
print("------------------------------------")
print("FELICITACIONES ",jugadores[WIN], " puntos total: ",contador[WIN])



        




