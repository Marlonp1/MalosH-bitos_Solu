def calcular_multiplicacion_suma(a, b, c):
    resultado = a * b + c
    return resultado

def principal():
    multiplicando = 2
    multiplicador = 4
    suma = 6
    resultado = calcular_multiplicacion_suma(multiplicando, multiplicador, suma)
    print("El resultado es:", resultado)

if __name__ == "__main__":
    principal()

