def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error al dividir entre cero!!!"
    
print(f"Dividir = {dividir(4, 2)}")
print(f"Dividir = {dividir(4, 0)}")