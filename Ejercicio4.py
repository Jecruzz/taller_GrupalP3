def CrearunArreglo():
 try:
    dimension = int(input("Ingresa cuántas posiciones debe tener el arreglo: "))
    arreglo = [0] * dimension
    for i in range(len(arreglo)):
        arreglo[i] = int(input(f"Ingrese el dato {i+1}: "))
    return arreglo
 except ValueError:
     print("Error al convertir")
 except Exception as e :
    print(f"Ha ocurrido un valor inesperado en {e}")

def RepeticionDeNumero(arreglo, numeroBuscar):

    contador = 0
    for numero in arreglo:
        if numero == numeroBuscar:
            contador += 1
    return contador
 

def ImprimirArreglo(arreglo):
    print("El arreglo es: ", arreglo)

while True:
    print("Ingresa 1 para crear un arreglo")
    print("Ingresa 2 para saber cuántas veces se repite un número en el arreglo")
    x = int(input("Ingresa tu opción: "))
    if x == 1:
        if arreglo is None:
            print("No existe arreglo")
        else:
            arreglo = CrearunArreglo()
            ImprimirArreglo(arreglo)
    elif x == 2:
        numeroBuscar = int(input("Ingrese el número a buscar: "))
        contador = RepeticionDeNumero(arreglo, numeroBuscar)
        print(f"El número {numeroBuscar} se repite {contador} veces en el arreglo")
    else:
        print("Opción no válida, por favor intente de nuevo.")
