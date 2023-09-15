# 1. Crear un función
# palabra reservada def seguido del nombre de la función

def miFuncion():
    print("Este es un mensaje")

miFuncion()

# 2. Funciones con parámetros

def miFuncion2(nombre, apellido):
    print(f"Hola {nombre} {apellido}!!")

miFuncion2('Alvin', 'Rosales')

# 3. Retornar valores a traves de la función

def sumar(a,b):
    return a + b

resultado = sumar(4,6)

print(f"El resultado es {resultado}")
print(f"El resultado es {sumar(5,6)}")

# 4. Parámetros (por nombre y por posición)

def areaTriangulo(base, altura):
    return (base * altura) / 2

alturaTriangulo = 10
baseTriangulo = 20

# - por posición

print(areaTriangulo(alturaTriangulo, baseTriangulo))

print(areaTriangulo(altura = alturaTriangulo, base = baseTriangulo))

# 5. Valores por defecto

def multiplicar(a, b = 1):
    return a * b

print(f"La multiplicación es: {multiplicar(2,5)}")
print(f"La multiplicación es: {multiplicar(2)}")

# 6. Argumentos indeterminados por posicion

def multiplicarMuchos(a, *numeros):
    for numero in numeros:
        a *= numero

    return a

print(multiplicarMuchos(2))
print(multiplicarMuchos(2, 3))
print(multiplicarMuchos(2, 3, 4))

# 7. Otra forma de argumentos indeterminados por nombre

def mostrarInformacion(**persona):
    informacion = persona.items()
    for clave, valor in informacion:
        print(f"{clave}: {valor}")

mostrarInformacion(
    Nombre = 'Alvin Rosales'
)

mostrarInformacion(
    Nombre = 'Alvin Ezequiel',
    Apellido = 'Rosales Hernández'
)

# 8. Retonor de multiples valores

def datos():
    nombre = "alvin"
    apellido = "rosales"
    return nombre, apellido, 19, 'Masculino'

misDatos = datos()

print(misDatos[0])