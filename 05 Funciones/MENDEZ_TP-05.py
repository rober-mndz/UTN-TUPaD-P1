# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

if __name__ == "__main__":
    imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

if __name__ == "__main__":
    user = input("Ingresa tu nombre: ")
    saludar_usuario(user)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
# dir los datos al usuario y llamar a esta función con los valores in-
# gresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}.")
    
if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su residencia: ")
    
    informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
# dio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuel-
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados.

import math 

def calcular_area_circulo(radio):
    area = math.pi * radio**2 
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2*math.pi*radio
    return perimetro

if __name__ == "__main__":
    radio = int(input("Ingrese el radio del circulo: "))
    print(f"El area de su circulo es {calcular_area_circulo(radio)} \n y su perimetro: {calcular_perimetro_circulo(radio)}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos-
# trar el resultado usando esta función.

def segundos_a_horas(seg):
    horas = seg/3600
    return horas

if __name__ == "__main__":
    segundos = int(input("Ingrese la cantidad de segundos: "))
    print(f"{segundos} son {segundos_a_horas(segundos)} horas")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun-
# ción.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero * i)
        
if __name__ == "__main__":
    num = int(input("Ingrese un numero: "))
    tabla_multiplicar(num)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
# sultados de forma clara.

def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    mult = a*b
    div = a/b
    
    resultados = (suma, resta, mult, div)
    return resultados

if __name__ == "__main__":
    num1 = int(input("ingrese num 1:"))
    num2 = int(input("ingrese num 2:"))
    resultados = operaciones_basicas(num1, num2)
    print(f"""{num1} + {num2} = {resultados[0]} 
          \n {num1} - {num2} = {resultados[1]}
          \n {num1} * {num2} = {resultados[2]}
          \n {num1} / {num2} = {resultados[3]}""")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura)**2
    return imc

if __name__ == "__main__":
    peso = int(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura: "))
    print(f"Su IMC es: {calcular_imc(peso, altura)}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

if __name__ == "__main__":
    grados = int(input("Ingresa la temperatra en C°: "))
    print(f"{grados} °C son equivalentes a {celsius_a_farenheit(grados)} °F")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

if __name__ == "__main__":
    num1 = int(input("Ingresa num1: "))
    num2 = int(input("Ingresa num2: "))
    num3 = int(input("Ingresa num3: "))
    print(f"El promedio entre: {num1}, {num2}, {num3} es: {calcular_promedio(num1, num2, num3)}")
    