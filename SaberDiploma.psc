Algoritmo SaberDiploma
	Escribir "Hola Usuario: Para cuirsar un Grado Superior tienes que tener Bachiller."
	Escribir "Introduce por teclado si tienes el Titulo de Bachillerato. Escribe: [S/N]" 
	Leer titulo_bachillerato // El usuario introduce 'S' para Si o 'N' para NO
	Si (titulo_bachillerato == "S") Entonces 
		Escribir "Puedes acceder a un Grado Superior porque tienes Bachiller."
	SiNo
		Escribir "No tienes Bachiller. No puedes acceder a Grado Superior de Formación Profesional."
	Fin Si
FinAlgoritmo