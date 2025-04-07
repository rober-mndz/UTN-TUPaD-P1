# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = input("Ingrese un numero entero:")
cont = 0

for c in num:
    cont += 1

print(f"El numero {num} tiene {cont} digitos.")
    
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese otro numero"))
suma = 0

for i in range(num1 + 1, num2):
    suma += i

print(suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

sumados = 0
num = int(input("Ingrese un numero entero:"))

while (num != 0):
    sumados += num
    num = int(input("Ingrese un numero entero:"))
    
print(sumados)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random as rnd

ganador = rnd.randint(0, 9)
numeroUsuario = int(input("Adivine el numero ganador entre el 0 y el 9:"))

while ganador != numeroUsuario:
    numeroUsuario = int(input("Adivine el numero ganador entre el 0 y el 9:"))

print(f"Felicitaciones, el numero ganador era: {ganador}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, 1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero entero:"))
suma = 0

# No incluye el numero ingresado por el usuario, respetando la consigna "comprendidos entre"
for i in range(0, num):
    suma += i
    
print(suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(0, 100):
    num = int(input("Ingrese un numero"))
    if((num % 2) == 0):
        pares += 1
    else:
        impares += 1
    if(num > 0):
        positivos += 1
    else:
        negativos += 1
        
print(f"{pares} numeros pares, {impares} impares, {positivos} positivos y {negativos} negativos.")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

acumulador = 0

for i in range(0, 100):
    num = int(input("Ingrese un numero"))
    acumulador += num

print(acumulador/100)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un numero:"))
invertido = 0

while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10
    
print(invertido)
    