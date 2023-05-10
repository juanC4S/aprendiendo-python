#mi ver con fallas xd
listanums=[]
while True:
    n=int(input("dame un nros, presiona cualquier tecla para salir:"))
    listanums.append(n)
    print("{} añadido".format(n))
    if n==-1:
        print("solo acepta nros")
        break
print("el numero maximo es: " ,max(listanums))
print("el numero minimo es: " ,min(listanums))