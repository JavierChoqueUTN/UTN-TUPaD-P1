# TP 6 - Estructuras de datos complejas (sin objetos)

# 1) Añadir frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios de frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Crear lista de frutas (sin precios)
lista_frutas = list(precios_frutas.keys())
print("Frutas disponibles:", lista_frutas)

# 4) Agenda telefónica
agenda = {}
print("\nIngrese 5 contactos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingrese el nombre de un contacto para consultar su número: ")
if consulta in agenda:
    print(f"Número de {consulta}: {agenda[consulta]}")
else:
    print("Ese contacto no está en la agenda.")

# 5) Palabras únicas y frecuencia
frase = input("\nIngrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia de palabras:", frecuencia)

# 6) Notas y promedio de alumnos
alumnos = {}

for i in range(3):
    nombre = input(f"\nIngrese nombre del alumno {i+1}: ")
    
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese nota {j+1} de {nombre}: "))
        notas.append(nota)
    
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio}")

# 7) Conjuntos de aprobados
aprobados_p1 = {1, 2, 3, 4, 5}
aprobados_p2 = {3, 4, 5, 6, 7}
ambos = aprobados_p1 & aprobados_p2
solo_uno = aprobados_p1 ^ aprobados_p2
al_menos_uno = aprobados_p1 | aprobados_p2

print("\nAprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# 8) Diccionario de stock
stock = {
    'Arroz': 10,
    'Fideos': 5,
    'Aceite': 2
}
producto = input("\nIngrese un producto a consultar: ")
if producto in stock:
    print(f"Stock de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuantas unidades quiere agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no encontrado. Ingrese stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# 9) Agenda de eventos con tuplas
agenda_eventos = {
    ('Lunes', '10:00'): 'Reunión',
    ('Martes', '15:00'): 'Clase',
    ('Viernes', '20:00'): 'Cine'
}
dia = input("\nIngresá un día: ")
hora = input("Ingresá una hora (HH:MM): ")

evento = agenda_eventos.get((dia, hora))
if evento:
    print(f"Actividad programada: {evento}")
else:
    print("No hay actividades en ese día y hora.")

# 10) Invertir diccionario de países y capitales
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'Italia': 'Roma',
    'Japón': 'Tokio'
}
capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("\nDiccionario invertido (capital -> país):", capitales_paises)