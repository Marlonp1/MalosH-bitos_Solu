def calcular(factorUno, factorDos):
    productoFactores = factorUno * factorDos
    return productoFactores


def main():
    primerNumero = 10
    segundoNumero = 5
    sumaDeNumeros =  primerNumero +  segundoNumero
    resultado = calcular(primerNumero, sumaDeNumeros)

    print("El resultado es:", resultado)



if __name__ == "__main__":
    main()
