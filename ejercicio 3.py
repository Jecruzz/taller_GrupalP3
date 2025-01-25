def crear_arreglo():
    
    n = int(input("Ingresa el número de elementos en el arreglo: "))
    arreglo = []
    for i in range(n):
        num = int(input(f"Ingresa el elemento {i + 1}: "))
        arreglo.append(num)
    return arreglo

def imprimir_arreglo(arreglo):
    
    print("El arreglo es:", arreglo)

def promedio_arreglo(arreglo):
    
    suma = 0
    for num in arreglo:
        suma += num
    promedio = suma / len(arreglo)
    return promedio


arreglo = crear_arreglo()

imprimir_arreglo(arreglo)

promedio = promedio_arreglo(arreglo)
print("El promedio de los elementos del arreglo es:", promedio)
