edad = int(input("digame su edad: "))
tipodcarnet  = input("digame su tipo de carnet (E para estudiante / P pensionista / F familia numerosa / N Nada): ")

if(25>= edad <= 35 and tipodcarnet == "E") or edad < 10 or \
    (edad>=65 and tipodcarnet == "P") or\
    (tipodcarnet == "F"):

    print ("se te aplica el descuento")

else:
    print ("no se te aplica el descuento")