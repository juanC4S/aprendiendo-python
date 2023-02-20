print("¿Cuanto te guta el queso?")

puntuacion = 0
print("PREGUNTA 1: ¿Que haces cuando ves una tabla de quesos?")
print("A - Salgo corriendo")
print("B - Pruebo uno de los quesos o incluso varios xd")
print("C - No puedo evitar devorarlos")



opcion=(input("SU RPTA ES?: "))

if opcion == "A" or opcion =="a":
    puntuacion +=0 
elif opcion =="B" or opcion =="b":
    puntuacion +=15
elif opcion =="C" or opcion =="c":
    puntuacion +=20
elif opcion != "A" or opcion !="a" or opcion !="B" or opcion !="b" or opcion !="C" or opcion !="c":
    print("ERROR : SOLO ES PERMITIDO A, B Y C")
    print("Saliendo del programa")
    quit()


print("PREGUNTA 2: ¿Como te gusta la hamburguesa?")
print("A - Sin queso")
print("B - Con queso")
print("C - Pan y queso")

opcion=(input("SU RPTA ES?: "))
if opcion == "A" or opcion =="a":
    puntuacion +=0 
elif opcion =="B" or opcion =="b":
    puntuacion +=15
elif opcion =="C" or opcion =="c":
    puntuacion +=20
elif opcion != "A" or opcion !="a" or opcion !="B" or opcion !="b" or opcion !="C" or opcion !="c":
    print("ERROR : SOLO ES PERMITIDO A, B Y C")
    print("Saliendo del programa")
    quit()



print("PREGUNTA 3: ¿Eres intolerante a la lactosa?")
print("A - Si")
print("B - A veces")
print("C - No")


opcion=(input("SU RPTA ES?: "))
if opcion == "A" or opcion =="a":
    puntuacion +=0 
elif opcion =="B" or opcion =="b":
    puntuacion +=15
elif opcion =="C" or opcion =="c":
    puntuacion +=20
elif opcion != "A" or opcion !="a" or opcion !="B" or opcion !="b" or opcion !="C" or opcion !="c":
    print("ERROR : SOLO ES PERMITIDO A, B Y C")
    print("Saliendo del programa")
    quit()

if puntuacion >= 25:
    print("su puntaje es: (",puntuacion ,") A ud. le encanta y eres cpp del queso xd")
elif puntuacion >=15:
    print("su puntaje es: (",puntuacion ,") A ud. le gusta el queso xd")
else:
    print("su puntaje es: (",puntuacion ,") A ud. no le gusta el queso")
