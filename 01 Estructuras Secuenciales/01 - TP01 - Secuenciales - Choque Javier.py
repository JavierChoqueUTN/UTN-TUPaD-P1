# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input("Ingrese su nombre por favor:")
print("Hola " + nombre + "!")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Ingrese nombre:")
apellido = input("Ingrese apellido:")
edad = input("Ingrese edad:")
lugar = input("Ingrese lugar de residencia:")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro
radio = float(input("Ingrese radio:"))
area = 3.14 * radio*radio
perimetro = 2 * 3.14 * radio
print(f"El area es: {area}.")
print(f"El perímetro es: {perimetro}.")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
secs = int(input("ingrese cantidad de segundos:"))
horas = secs / 60 / 60
print(f"{secs} segundos equivale a {horas} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
num = int(input("Ingrese un numero: "))
for i in range(1, 11):
    prod = num * i
    print(f"{num} x {i} = {prod}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print(f"Suma = {num1+num2}")
print(f"Resta = {num1-num2}")
print(f"Multiplicacion = {num1*num2}")
print(f"Division = {num1/num2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en M: "))
print(f"su IMC es: {peso/(altura*altura)}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
temp_celsius = float(input("ingrese temperatura en celsius:"))
temp_farenheit = ((9/5) * temp_celsius)+32
print("Su equivalente en Farenheit es: " + str(temp_farenheit))

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
num1 = float(input("Ingrese primer numero: "))
num2 = float(input("Ingrese segundo numero: "))
num3 = float(input("Ingrese tercer numero: "))
prom = (num1+num2+num3)/3
print(f"El promedio de los numeros ingresado es: {prom}")
