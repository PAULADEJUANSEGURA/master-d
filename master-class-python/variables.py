#  Variables y constantes
print("**** 1. Variables y constantes ****")

#Variables 
nombre_variable = "Valor de la variable que queremos almacenar (Esto es String)"
edad = 18
precio = 2.50
print("Edad de la mayoria de edad:", edad)

#Cambio de valor de una variable
edad = 19  # Ahora la variable 'edad' tiene un nuevo valor
print("Edad actualizada:", edad)  # Imprime el valor actualizado de la variable
 
#Constantes 
PI = 3.1416  # Convención: las constantes se escriben en mayúsculas 
print(PI)

PI = 3.14  # Aunque es posible cambiar el valor, no es recomendable
print("Valor modificado de PI (no recomendado):", PI)

print("\n **** 2. Tipos de datos básicos ****")

#String
nombre = "Paula"
saludo = 'Hola'

#Números enteros
entero_int = 42
numero_con_coma_flotante = 1.75

altura = 1.65  # Número decimal (float)

#Booleanos
verdadero = True
falso = False   

# None
valor_nulo = None   

#listas
lista_de_numeros = [1, 2, 3, 4, 5]

#Tuplas (inmutables
tupla_de_colores = ("rojo", "verde", "azul")

#Diccionarios (pares clave-valor)
dic_persona = {
    "nombre": "Paula",
    "edad": 38,
    "altura": 1.65
}


#funcion
def sumar (a,b):
    return a + b

#Ccosas que se pueden hacer con TEXTO (String)
print("\n **** 3. Operaciones con cadenas de texto ****")
texto1 = "¡Hola mundo!"
texto2 = 'Bienvenidos a Python'
texto3 = '1985'

print(texto1)
print(texto2)
print(texto3)

#Comillas dentro de comillas    Se pone comilla doble fuera y comilla simple dentro
frase_con_comillas = "Ella dijo: 'Python es genial!'"
print(frase_con_comillas)

#Triple comillas para texto multilínea
texto_multilinea = """Este es un texto
que abaraca varias líneas.
Puedes escribir todo lo que quieras aquí."""
print(texto_multilinea)



#Concatenacion de cadenas de texto
print("Concatenación:", texto1 + " " + texto2)  # Concatenar cadenas

nombre = "Paula"
lenguaje = "Python"
print("Concatenacion con el operador + : " + nombre + " está aprendiendo "+ lenguaje)  # Concatenar con +

print("Concatenacion con la coma , : ", texto1, texto2)  # Concatenar con coma

print("Hola me llamo", nombre, "y estoy estudiando", lenguaje)  # Concatenar con coma

print(f"Hola me llamo {nombre} y estoy estudiando {lenguaje}")  # Concatenar con f-strings

#Repeticion de cadenas de texto
print("Feliz navidad", "jo" * 3)  # Repetir cadena 3 veces

edad = 38
#En los f-strings podemos hacer operaciones dentro de las llaves {}
print(f"{nombre} tiene {edad} años y el próximo año tendrá {edad + 1} años.")


#Indices y slicing (rebanado)
palabra = "Python"
print("Primera letra:", palabra[0])  # Primer carácter
print("Última letra:", palabra[-1])  # Último carácter  
print("Subcadena (0-2):", palabra[0:2])  # Subcadena desde índice 0 hasta 2 (exclusivo)
print("Subcadena (2-5):", palabra[2:5])  # Subcadena desde índice 2 hasta 5 (exclusivo)
print("Subcadena desde el índice 3 hasta el final:", palabra[3:])
print("Subcadena desde el inicio hasta el índice 3 (exclusivo):", palabra[:3])


#Longitud de una cadena de texto
s_largo= "supercalifragilisticoespialidoso"
print(len(s_largo))  # Longitud de la cadena

print(len(palabra))  # Longitud de la cadena "Python"


# Artimeticos
a = 8
b = 3
print("suma:", a + b)          # Suma
print("resta:", a - b)         # Resta
print("multiplicacion:", a * b) # Multiplicación    
print("division:", a / b)      # División
print("division entera:", a // b)  # División entera
print("modulo:", a % b)        # Módulo (residuo)
print("potencia:", a ** b)     # Potencia

print(f"Suma: {a+ b}")        # Suma
print(f"Resta: {a - b}")      # Resta
print(f"Multiplicación: {a * b}")  # Multiplicación
print(f"División: {a / b}")    # División
print(f"División entera: {a // b}") # División entera
print(f"Módulo: {a % b}")      # Módulo (residuo)
print(f"Potencia: {a ** b}")   # Potencia

# Redondeo de números decimales
numero_decimal = 5.6789
print("Número original:", numero_decimal)
numero_redondeado = round(numero_decimal, 2)  # Redondear a 2 decimales
print("Número redondeado a 2 decimales:", numero_redondeado)
numero_redondeado_sin_decimales = round(numero_decimal)  # Redondear al entero más cercano
print("Número redondeado al entero más cercano:", numero_redondeado_sin_decimales)

# Comparación y lógica
print(f"a == b: {a == b}")  # Igualdad
print(f"a != b: {a != b}")  # Desigualdad   
print(f"a > b: {a > b}")    # Mayor que
print(f"a < b: {a < b}")    # Menor que     
print(f"a >= 10 and b <= 3: {a >= 10 and b <= 3}")  # Mayor o igual que y menor o igual que con operador lógico AND
print(f"a >= 10 or b <= 3: {a >= 10 or b <= 3}")    # Mayor o igual que o menor o igual que con operador lógico OR
print(f"not (a > b): {not (a > b)}")  # Negación lógica     

# Conversión de tipos de datos
num_string = "123"
num_entero = int(num_string)  # Convertir cadena a entero
num_flotante = float(num_string)  # Convertir cadena a flotante 

# No se puede concatenar ni sumar un String a un número directament 
print(type(num_string))    # Tipo original: str
print(type(num_entero))    # Tipo convertido: int
print(type(num_flotante))  # Tipo convertido: float

num = 50
num_string_convertido = str(num)  # Convertir entero a cadena
print(type(num_string_convertido))  # Tipo convertido: str  

