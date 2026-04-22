# Definición de la función sumar
def sumarEnteros(*numeros):
    resultado = 0
    for numero in numeros:
        resultado = resultado + numero
    return print("El resultado de la sumaes:", resultado)

# Llamada a la función sumar con diferentes números
sumarEnteros(5, 10, 15)
sumarEnteros(2, 4, 6)
sumarEnteros(1, 3, 5)