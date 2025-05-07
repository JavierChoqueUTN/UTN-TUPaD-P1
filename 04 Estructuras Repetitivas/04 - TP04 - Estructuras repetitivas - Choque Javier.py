# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
i = 1
while i <= 100:
    print(i)
    i = i + 1

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
cont = 0
num = int(input("Ingrese un numero:"))
while num > 0:
    num = num // 10
    cont = cont + 1
print(f'El numero ingresado tiene {str(cont)} digitos.')

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese 1er numero: "))
num2 = int(input("Ingrese 2do numero: "))
sum = 0
for i in range (num1+1, num2):
    sum = sum + i
print(f'La suma de los numeros comprendidos entre {str(num1)} y {str(num2)} es {str(sum)}.')

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
num = 1
sum = 0
while num != 0:
    num = int(input("Ingrese un numero (Puede cancelar ingresando 0): "))
    sum = sum + num
print(f"La suma de los numeros ingresados es: {str(sum)}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
num_random = random.randint(0, 9)
num_ingresado = 10
cont = 0

while num_random != num_ingresado:
    num_ingresado = int(input("Ingrese el numero que crea que se generó: "))
    cont = cont + 1
print(f"Usted adivinó el número en {str(cont)} intentos.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for i in range(100,-1,-1):
    if (i % 2) == 0:
        print(f"{str(i)} es par.")

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
num1 = int(input("Ingrese numero: "))
sum = 0
for i in range (0,num1+1):
    sum = sum + i
print(f'La suma de los numeros comprendidos entre 0 y {str(num1)} es {str(sum)}.')

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
num = 0
cont_pares = 0
cont_impares = 0
cont_neg = 0
cont_pos = 0

for i in range(1,101):
    num = int(input("Ingrese numero: "))
    if num < 0:
        cont_neg += 1
    elif num > 0:
        cont_pos += 1
    else:
        continue
    
    if num % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1
print(f"Cantidad de Numeros Pares: {str(cont_pares)}. ")
print(f"Cantidad de Numeros Impares: {str(cont_impares)}. ")
print(f"Cantidad de Numeros Positivos: {str(cont_pos)}. ")
print(f"Cantidad de Numeros Negativos: {str(cont_neg)}. ")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
num = 0
sum = 0
for i in range(1,101):
    num = int(input("Ingrese numero: "))
    sum = sum + num
media = sum / 3
print(f"La media es: {str(media)}. ")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
inv = 0
num = int(input("Ingrese numero:"))
while num > 0:
    digito = num % 10
    inv = inv * 10 + digito
    num //= 10
print(f"Numero invertido: {str(inv)}")