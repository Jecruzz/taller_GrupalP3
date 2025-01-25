#Ejercicio 1: Suma de los elementos de un arreglo Descripción: 
# Crea una función que reciba un arreglo de enteros y retorne la suma de todos sus elementos. 
# Debe tener la función para crear el arreglo e imprimirlo. No se pueden usar funciones propias de listas
def crear_arreglo():
   try: 
    x = int(input("Ingrese la cantidad de números del arreglo: "))
    arreglo = [0] * x  
    suma = 0   
    
    for j in range(x):
        arreglo[j] = int(input(f"Ingrese el número {j + 1}: "))  
        suma += arreglo[j]  
        
    print(f"Arreglo: {arreglo}")  
    print(f"Suma de los números: {suma}") 

    
    return arreglo

       
   except ValueError :
      print()
   except ImportError:
      print("Error al reconocer el arreglo")  
   except Exception as e :
      print("Error al sumar y redondear")  
        




crear_arreglo()























# def crear_arreglo():
#   x = int(input("Ingrese la cantidad de numeros del arreglo :"))
#   arreglo =[0]*x
#   sumas = 0
#   for j in range (x) : arreglo[j] = int(input(f"Ingrese el numero {j + 1}:"))
#   return arreglo
#     print(arreglo)
#      arreglo[i] = nota
#      suma += notas[i]
#     print(suma)    



# def suma_arreglos(arreglo:list):
#  notas = [10.0,8.0,5.0,6.5]
#  suma = 0
#  for i in range (len(notas)) :
#     nota = float(input(f"Ingrese la nota {i+1} :"))
#     print(nota)
#     notas[i] = nota
#     suma += notas[i]
#  print(suma)    

# arreglo1 = int(input("Ingrese el arreglo"))

# suma_arreglos(arreglo1)

















































# Ejercicio 3: Promedio de un arreglo Descripción: 
# Crea una función que reciba un arreglo de números enteros y retorne el promedio de los elementos. 
# Debe tener la función para crear la matriz e imprimirlo. 
# No se pueden usar funciones propias de listas