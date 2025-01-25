def CrearunArreglo():
    dimension=int(input("Ingresa Cuantas pocisiones debe tener el arreglo"))
    arreglo=[0]*dimension
    for i in range (len(arreglo)):
        arreglo[i]=int(input(f"Ingrese los numeros enteros de la lista {i+1}:")) 
    return arreglo

def ObtenerNumerosPares(arreglo):
    arregloPares = []
    for numero in arreglo:
        if numero % 2 == 0:
            arregloPares.append(numero)


    # arregloPares = [""]*len(arreglo)
    # posicion = 0
    # for numero in arreglo:
    #     if numero % 2 == 0:
    #         arregloPares[posicion] = numero
    #         posicion +=1



def ImprimirArregloPar(arreglo):
    
    for i in arreglo:
        if i % 2 == 0:

    
    


while True:
    print("Ingresa 1 para crear un arreglo")
    print("Ingresa 2 para saber cuántas veces se repite un número en el arreglo")