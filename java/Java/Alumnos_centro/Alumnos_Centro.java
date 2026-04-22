/*@author Paula de Juan ENUNCIADO: Un colegio desea conocer el porcentaje de alumnos de cada sexo que hay en su centro. Creando Programa que calcula el Porcentaje de alumnos de cada sexo que hay en un centro académico. */
 package alumnos_centro; 
 import java.util.ArrayList; 
 import java.util.Scanner; 
 public class Alumnos_Centro { 
    public static void main(String[] args) {
         Scanner scanner = new Scanner(System.in);
         ArrayList<Alumno> listaAlumnos = new ArrayList<>(); 
         int numeroAlumnos; 
         int contadorHombres = 0;
         int contadorMujeres = 0; 
         System.out.println("Introduce el número total de alumnos = "); 
         numeroAlumnos = scanner.nextInt(); scanner.nextLine(); // Limpiar buffer 
         
         
         // Crear alumnos uno por uno mediante bucle for:
        for (int i = 0; i < numeroAlumnos; i++){ 
            System.out.println("Introduce el nombre del alumno = "); 
            String nombre = scanner.nextLine(); 
            System.out.println("Introduce la edad del alumno = "); 
            int edad = scanner.nextInt(); 
            System.out.println("Introduce el genero 'Hombre' / 'Mujer' = "); 
            String genero = scanner.nextLine(); 
        //Crear objeto Alumno 
        Alumno alumno = new Alumno(nombre, edad, genero); 
        listaAlumnos.add(alumno); 
        } 
        
        
        //Mostrar datos 
        for (Alumno alumno1 : listaAlumnos){ 
            System.out.println("Nombre = " + alumno1.getNombre());
            System.out.println("Edad = " + alumno1.getEdad());
            System.out.println("Género = " + alumno1.getGenero());
            System.out.println("¿Es masculino su género? = " + alumno1.isGeneroMasculino()); 
            System.out.println("Fin del alumno número =" + alumno1.getId_Alumno() + "----------*****"); 
            } 
        scanner.close(); 
        }       
    }
    