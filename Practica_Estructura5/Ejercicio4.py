# Funcion para ingresar n datos a una lista
def ingresar_datos():
    n = int(input("Ingrese la cantidad de datos que desea ingresar: "))
    datos = []
    for i in range(n):
        valor = float(input(f"Ingrese el dato {i + 1}: "))
        datos.append(valor)
    return datos

# Funcion para ordenar una lista de menor a mayor (usando el algoritmo de burbuja)
def ordenar_lista(datos):
    n = len(datos)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos

# Funcion para calcular la sumatoria de los datos de una lista
def calcular_sumatoria(datos):
    sumatoria = 0
    for dato in datos:
        sumatoria += dato
    return sumatoria

# Funcion para calcular la media de los datos
def calcular_media(datos):
    n = len(datos)
    if n == 0:
        return 0
    sumatoria = calcular_sumatoria(datos)
    media = sumatoria / n
    return media

# Funcion para calcular la mediana
def calcular_mediana(datos):
    datos_ordenados = ordenar_lista(datos)
    n = len(datos_ordenados)
    if n % 2 == 0:
        mediana = (datos_ordenados[n // 2 - 1] + datos_ordenados[n // 2]) / 2
    else:
        mediana = datos_ordenados[n // 2]
    return mediana

# Funcion para calcular la moda
def calcular_moda(datos):
    frecuencias = {}
    for dato in datos:
        if dato in frecuencias:
            frecuencias[dato] += 1
        else:
            frecuencias[dato] = 1
    moda = [key for key, value in frecuencias.items() if value == max(frecuencias.values())]
    return moda

# Funcion para calcular la desviacion estandar
def calcular_desviacion_estandar(datos):
    n = len(datos)
    if n <= 1:
        return 0
    media = calcular_media(datos)
    suma_cuadrados = sum((dato - media) ** 2 for dato in datos)
    desviacion_estandar = (suma_cuadrados / (n - 1)) ** 0.5
    return desviacion_estandar

# Uso de las funciones
datos = ingresar_datos()
print("Datos ingresados:", datos)
print("Datos ordenados:", ordenar_lista(datos))
print("Sumatoria de datos:", calcular_sumatoria(datos))
print("Media de datos:", calcular_media(datos))
print("Mediana de datos:", calcular_mediana(datos))
print("Moda de datos:", calcular_moda(datos))
print("Desviación estándar de datos:", calcular_desviacion_estandar(datos))
