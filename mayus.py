import string
text=input("Introduce un texto: ")
may=0
for cant in text:
    if cant in string.ascii_uppercase:
        may+=1
        

print("la cantidad total de mayusculas son: ",may)

