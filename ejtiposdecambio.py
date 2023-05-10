#esto es el tipo de cambio a esta fecha 20/02/2023
penusd = 3.85

peneur = 4.11

print("TIPOS DE CAMBIO XD")



print("1 - De soles a dolares?")
print("2 - De soles a euros?")
print("3 - De dolares a soles?")
print("4 - De euros a soles?")

opc = input("SELECIIONE SU DIVISA: ")

if opc =="1" or opc =="2" or opc =="3" or opc =="4":

    if opc == "1":
        divi=float(input("Ingrese sus soles a cambiar porfavor: "))
        divi /=penusd 
        
    if opc =="2":
        divi=float(input("Ingrese sus soles a cambiar porfavor: "))
        divi /=peneur
    if opc =="3":
        divi=float(input("Ingrese sus dolares cambiar porfavor: "))
        divi *=penusd
        
    if opc =="4":
        divi=float(input("Ingrese sus euros a cambiar porfavor: "))
        divi *=peneur

    print("su cambio es : " ,divi)
    
else:
    print("Error: solo es valido esas 4 opciones")
    print ("saliendo del programa...")
    quit()

