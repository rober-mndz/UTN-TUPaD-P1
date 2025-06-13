# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
if __name__ == "__main__":
    num = int(input("Ingrese un numero: "))
    for i in range(1, num + 1):
        print(factorial(i))

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

def fibonacci(pos):
    if pos <= 0:
        return 1
    elif pos == 1:
        return 0
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)

    
if __name__ == "__main__":
    num = int(input("Ingresa la posicion:"))
    print(fibonacci(num))

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛∗𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

def potencia_recursiva(n, m):
    if m <= 0:
        return 1
    else:
        return n * potencia_recursiva(n, m-1)


if __name__ == "__main__":
    print(potencia_recursiva(2, 3))

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto.

import math as m

def dec_a_bin(decimal):
    if decimal == 0:
        return 0
    else:
        res = decimal%2
        return str(dec_a_bin(m.floor(decimal/2))) + str(res)
        
if __name__ == "__main__":
    print(dec_a_bin(78))