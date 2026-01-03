# Comentario que explica que lo siguiente es una CONSTANTE
MAYORIA_EDAD = 18  # Constante que define la mayoría de edad

# Comentario que explica que lo siguiente es una VARIABLE
edad_usuario = 0  # Variable que almacena la edad del usuario

print("Introduce tu edad: ")
edad_usuario = int(input())

# INDENTACIÓN de condicionales
if (edad_usuario >= MAYORIA_EDAD):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")