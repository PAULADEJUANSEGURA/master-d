# Saber si un alumno tiene o no diploma de Bachillerato para acceder a Grado Superior de FP:
print("¡Bienvenido! Vamos a determinar si puedes acceder a Grado Superior de FP.")
respuesta = input("¿Tienes el diploma de Bachillerato? Escribe la opción entre estas: (Sí/No):")
if respuesta == "Sí":
    print("¡Enhorabuena! Puedes acceder a Grado Superior de FP.")
elif respuesta == "No":
    print("Lo siento, no puedes acceder a Grado Superior de FP.")   
else:
    print("Opción no válida. Por favor, responde con 'Sí' o 'No'.")