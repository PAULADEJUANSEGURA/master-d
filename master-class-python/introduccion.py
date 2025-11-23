# Comentario de Python
print("Hola, mundo!")  # Imprime un saludo en la 
print("Bienvenidos a la clase de Python.")  # Mensaje de bienvenida 
print("-" * 10)  # Línea separadora

#Variables
nombre = "Paula"
apellido = "de Juan"
edad = 38   
altura = 1.65
print("Nombre:", nombre)
print("Edad:", edad)
print("Nombre:", nombre, "tiene la Edad de", edad, "y tiene la Altura de", altura, "metros")

#En Python podemos concatenar cadenas de texto con el operador +
print("Nombre Completo: " + nombre + " " + apellido)  

#Podemos operar con números
num1 = 10
num2 = 3.5
suma = num1 + num2
print("La suma de", num1, "y", num2, "es:", suma)

#Podemos restar, multiplicar y dividir
resta = num1 - num2
multiplicacion = num1 * num2    
division = num1 / num2
print("Resta:", resta)
print("Multiplicación:", multiplicacion)    
print("División:", division)

#Podemos redondear números decimales
division_redondeada = int(division)
print("División redondeada:", division_redondeada)  
division_redondeada_con_round = round(division, 2)
print("División redondeada con round:", division_redondeada_con_round)

#Entrada de datis del usuario
nombre_usuario = input("Por favor, ingresa tu nombre: ")
print("Hola,", nombre_usuario, "! Bienvenido a la clase de Python.") 