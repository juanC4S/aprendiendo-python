def potencia_cuadrada(base):
    if base ==1 :
        return 1
    else:
        return base * base

def potencia_libre(base, exponente):
    if exponente == 0:
        return 1
    elif exponente % 2 == 0:
        basemasexpoacumulado = potencia_libre(base, exponente // 2)
        return basemasexpoacumulado * basemasexpoacumulado
    else:
        return base * potencia_libre(base, exponente - 1)

def main():
    print(potencia_cuadrada(6))
    print(potencia_libre(3,9))

if __name__ == "__main__":
    main()