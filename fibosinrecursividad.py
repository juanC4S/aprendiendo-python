n = 10  # Número de términos de la serie que deseas calcular
a, b = 0, 1

print(a)  # Imprime el primer término de la serie (0)
print(b)  # Imprime el segundo término de la serie (1)

for _ in range(2, n):
    c = a + b  # Calcula el siguiente término sumando los dos anteriores
    print(c)  # Imprime el siguiente término
    a, b = b, c  # Actualiza los valores de a y b para la siguiente iteración
