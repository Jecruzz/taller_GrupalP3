def crear_matriz():
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    matriz = [[0] * columnas for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = int(input(f"Ingrese el número en la posición ({i}, {j}): "))
    return matriz

def encontrar_max_min(matriz):
    max_val = matriz[0][0]
    min_val = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > max_val:
                max_val = matriz[i][j]
            if matriz[i][j] < min_val:
                min_val = matriz[i][j]
    return max_val, min_val

def print_matriz(matriz):
    for fila in matriz:
        fila_str = ""
        for num in fila:
            fila_str += str(num) + " "
        print(fila_str)

try:
    matriz = crear_matriz()
    print("Matriz inicial:")
    print_matriz(matriz)

    max_val, min_val = encontrar_max_min(matriz)
    print(f"El número más grande en la matriz es: {max_val}")
    print(f"El número más pequeño en la matriz es: {min_val}")

except ValueError:
    print("No puede ingresar letras")
