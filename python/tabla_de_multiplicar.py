#Programa que muestra la tabla de multiplicar de un numero dado:
tabla_del_numero = int(input("Ingrese el numero del cual desea conocer su tabla de multiplicar: "))
operador = 0

while(operador <= 10):
    print(tabla_del_numero, "x", operador,"=", tabla_del_numero * operador)
    operador = operador + 1
