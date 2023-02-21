#esto es el tipo de cambio a esta fecha 20/02/2023
penusd = 3.85

peneur = 4.11

print("ios o android? XD")



print("1 - Android")
print("2 - IOS")


opc = input("SELECIIONE SU PREFERIDO: ")

if opc =="1" or opc =="2":

    if opc == "1":
        print ("ANDROID")
        newopc=input("Tienes dinero? (S/N): ")
        if newopc == "S" or newopc=="s" or newopc == "N" or newopc=="n":
            if newopc == "S" or newopc=="s":
                print("tienes dinero")
                new2opc=input("Te importa la camara del movil? (S/N): ")
                if new2opc == "S" or new2opc=="s":
                    print ("Google pixel supercamera")
                if new2opc == "N" or new2opc=="n":
                    print("android calidad precio")
            elif newopc == "N" or newopc=="n":
                print ("android chino 100 usd")
        
        
        
    if opc =="2":
        print ("IOS")
        newopc=input("Tienes dinero? (S/N): ")
        if newopc == "S" or newopc=="s" or newopc == "N" or newopc=="n":
            if newopc == "S" or newopc=="s":
                print("tienes dinero gaaaa ")
                new2opc=input("Tienes dinero....? (S/N): ")
                if new2opc == "S" or new2opc=="s":
                    print ("iphone ultra proMax")
            elif newopc == "N" or newopc=="n":
                print ("iphone de 2da mano")
            
   
    

