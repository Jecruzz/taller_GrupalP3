arreglo = None

def crear_arreglo():
    x = int(input("Ingrese la cantidad de numeros del arreglo: "))
    arreglo = [0]*x
    for i in range(x): arreglo[i] = int(input(f"Ingrese el numero {i + 1}: "))
    return arreglo

def arreglo_inverso(arreglo):
    inverso = [0] * len(arreglo)
    for i in range(len(arreglo)):
        inverso[len(arreglo) - 1 - i] = arreglo[i]
    return inverso

def print_arreglo(arreglos):
    resultado = ""
    for num in arreglos:
        resultado += str(num) + " "
    print(resultado)


try:
    arreglo = crear_arreglo()
    print("Arreglo inicial: ")
    print_arreglo(arreglo)

    inverso = arreglo_inverso(arreglo)
    print("Arreglo invertido: ")
    print_arreglo(inverso)
except ValueError:
    print("Se ha producido un error de valor.")


