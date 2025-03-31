import math 
math.pi

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugarResidencia = input("Ingese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {lugarResidencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = int(input("Ingrese el radio de un circulo: "))
print(f" {radio**2 * math.pi} es su area y {radio*math.pi*2} es su perimetro.")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

seg = int(input("Ingrese una cantidad de segundos: "))
horas = seg / 3600
print(f"{seg} segundos son {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

num = int(input("ingrese un numero: "))
print(num * 1)
print(num * 2)
print(num * 3)
print(num * 4)
print(num * 5)
print(num * 6)
print(num * 7)
print(num * 8)
print(num * 9)
print(num * 10)

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num, num2 = int(input("ingrese un numero: ")), int(input("ingrese un numero: "))
print(num + num2)
print(num - num2)
print(num * num2)
print(num / num2)

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.

altura = int(input("ingrese su altura: "))
peso = int(input("ingrese su peso: "))
imc = peso * (altura)**2
print(imc)

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.

celsius = int(input("ingrese una temperatura en grados celsius: "))
farenheit = celsius*(9/5) + 32
print(farenheit)

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

num, num2, num3 = int(input()), int(input()), int(input())
prom = (num + num2 + num3)/3
print(prom)