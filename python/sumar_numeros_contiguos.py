# ENUNCIADO: Diseña un algoritmo que calcule la suma de una cantidad de números contiguos determinada, consultando con el usuario desde qué número se debe empezar a realizar la suma y cuántos números se deben sumar.
NUMERO_INICIAL = int(input("Ingrese el numero desde el cual desea empezar a sumar: "))
CANTIDAD_DE_SUMAS = int(input("Ingrese la cantidad de numeros contiguos que desea sumar: ")) 
resultado = 0
for i in range(NUMERO_INICIAL, NUMERO_INICIAL + CANTIDAD_DE_SUMAS):
    if NUMERO_INICIAL > 0:
        print(f"Valor de i: {i}")
        # print(f"Valor de suma antes de sumar: {suma}")
        resultado = resultado + i
        # print(f"Sumando el numero: {i} + {i+1} = {suma+i+1}")
        print(f"-------")
print("La suma total es:", resultado)
