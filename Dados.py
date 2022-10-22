import random


class LanzarDados:


    def __init__(self):


        self.a =random.randint (1,6)


        self.b = random.randint (1,6)


        self.c = (self.a+self.b)

Player =LanzarDados()



print("Dado 1: ")
print(Player.a)

print("Dado 2: ")
print(Player.b)


print("La suma es: ")
print(Player.c)



lista1=[7,11]


lista2=[2,3,12]


lista3=[4,5,6,8,9,10]

if Player.c == 7 or Player.c == 11:


    print("Gano.")
    
else:
    if Player.c == 12 or Player.c == 2 or Player.c == 3:

        print("Perdio.") 

if Player.c == 4 or Player.c == 5 or Player.c == 6 or Player.c == 8 or Player.c == 9 or Player.c == 10:


    print ("Repita su turno.")