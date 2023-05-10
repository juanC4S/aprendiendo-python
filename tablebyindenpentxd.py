tabla=int(input("De que nro desa la tabla?: "))
for derecha in range(1, 12+1):
    by=tabla*derecha
    print("{} X {} = {}".format(tabla, derecha, by) )

