import random;

print("adivina el nro csmrxd")
ram=int(input("Introduce un nro cualquiera en entre 1-10: "))
ramdi= random.randint(1,10)

if ram==ramdi:
    print ("GANASTE TU NRO : {}".format(ram) +" es igual a :" ,ramdi )
else:
    print ("el nro ganador era: ",ramdi)