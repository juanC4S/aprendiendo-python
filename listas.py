init=True
print ("Programa de la lista de compra\n")
lista=[]
while init ==True:
    tecleoalgo= input("que desea comprar? ([Q] para salir): ")
    if tecleoalgo!="q" and tecleoalgo!="Q":
        rpta=input("Seguro que quiere añadir {} ? [S/N]: ".format(tecleoalgo))
        if rpta =="S" or rpta =="s":  
            lista.append(tecleoalgo)
            print(tecleoalgo ,"añadido")
        elif rpta=="n" or rpta =="N":
            init = True
        
    else:
        init=False
    


print("sal ciclo de mrda")


if lista==[]:
    print ("tu lista de compras no contiene nada..")
else:
    print("Su lista de compra es:\n")
    for fucklista in lista:
        print("{} - {}".format(lista.index(fucklista), fucklista))
    