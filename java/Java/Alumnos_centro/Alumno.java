/*@author Paula de Juan Creando Programa con Clases y Objetos */ 

package alumnos_centro; 
public class Alumno {
    private int id_alumno; 
    private String nombre; 
    private int edad; 
    private String genero; // "Hombre" o "Mujer"
    private boolean generoMasculino; 
    // Constructor de la Clase Alumno 
    public Alumno(int id_alumno, String nombre, int edad, String genero){ 
        this.id_alumno = id_alumno;
        this.nombre = nombre; 
        this.edad = edad; 
        this.genero = genero; 

        //Calcular automáticamente el valor booleano a partir del String genero 
            if (genero.equalsIgnoreCase("Hombre")){ 
                        this.generoMasculino = true;
            } else { this.generoMasculino = false; 
            } 
        }
        
        // Getters 
        public int getId_Alumno(){ 
            return id_alumno;
             } 
        public String getNombre(){ 
            return nombre; 
        }
        public int getEdad(){ 
            return edad; 
        } 
        public String getGenero(){ 
            return genero; 
        }
        public boolean isGeneroMasculino(){ 
            return generoMasculino; 
        }
}