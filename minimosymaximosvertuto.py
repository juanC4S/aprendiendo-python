aquiintroduscolosnros = input("Introduzca los números separados por coma: ")
#en esta variable almaceno lo q c introducido
#el split coge los nros q estan separados por comas

#luego lo listp en nros de usuario usando LIST COMPREHESION
#es una forma de shacer una forma de hacer un for mas reducido
numeros_d_usuario = [int(numero) for numero in aquiintroduscolosnros.split(",")]


print(numeros_d_usuario)

numero_peque =numeros_d_usuario[0]
numero_grande=numeros_d_usuario[0]

for numero in numeros_d_usuario[1:]:
    if numero_peque > numero:
        numero_peque = numero
    if numero_grande < numero:
        numero_grande = numero

print ("numero grande: {}, numero pequeño {} ".format(numero_grande, numero_peque))