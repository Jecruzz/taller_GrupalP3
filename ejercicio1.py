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
