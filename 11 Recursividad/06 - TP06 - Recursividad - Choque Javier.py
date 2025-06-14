# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

limite = int(input("Ingrese un número para calcular los factoriales desde 1 hasta ese número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    return fibonacci(posicion - 1) + fibonacci(posicion - 2)

limite = int(input("\nHasta que posición querés mostrar la serie de Fibonacci?: "))
print("Serie de Fibonacci:")
for i in range(limite + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
# algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("\nIngresa la base: "))
exponente = int(input("Ingresa el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(numero_recibido):
    if numero_recibido == 0:
        return "0"
    elif numero_recibido == 1:
        return "1"
    return decimal_a_binario(numero_recibido // 2) + str(numero_recibido % 2)

numero_decimal = int(input("\nIngresa un número entero positivo para convertir a binario: "))
print(f"{numero_decimal} en binario es {decimal_a_binario(numero_decimal)}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Prueba
palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
print(f"¿Es palíndromo? {es_palindromo(palabra)}")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
def suma_digitos(num_ingresado):
    if num_ingresado < 10:
        return num_ingresado
    else:
        return num_ingresado % 10 + suma_digitos(num_ingresado // 10)

num_ingresado = int(input("Ingrese un numero entero positivo para sumar sus dígitos:"))
print(suma_digitos(num_ingresado))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(num_bloques):
    if num_bloques == 1:
        return 1
    else:
        return num_bloques + contar_bloques(num_bloques - 1)

num_bloques = int(input("Ingrese un numero de bloques:"))
print(contar_bloques(num_bloques))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            coincidencia = 1
        else:
            coincidencia = 0
        return coincidencia + contar_digito(numero // 10, digito)
    
print(contar_digito(12233421, 2)) 
print(contar_digito(5555, 5))
print(contar_digito(123456, 7))
