/*@author Paula de Juan */
package javaapp2;
import java.util.Scanner;

public class JavaApp2 {

public static void main(String[] args) {
        final int MAYORIA_EDAD = 18;
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce tu nombre: ");
        String nombre = sc.nextLine();
        System.out.println("Introduce tu edad: ");
        int edad_usuario = sc.nextInt();
        if(edad_usuario >= MAYORIA_EDAD){
                System.out.println("El usuario es mayor de edad");
                System.out.println("Hola " + nombre + ", tienes " + edad_usuario + " años.");
                System.out.println("El usuario es mayor de edad y puede aprender a conducir todos los vehículos.");
        }else if(edad_usuario >= 16){
                System.out.println("El usuario es menor de edad pero podrá conducir ciclomotores de hasta 125cc.");
                System.out.println("Hola " + nombre + ", tienes " + edad_usuario + " años.");
        }else if(edad_usuario >= 15){
                System.out.println("El usuario es menor de edad pero podrá conducir ciclomotores de hasta 50cc.");
                System.out.println("Hola " + nombre + ", tienes " + edad_usuario + " años.");
        }else if(edad_usuario >= 12){            
                System.out.println("El usuario es menor de edad y todavia no puedes conducir ningún vehículo. Ve en bici o patinete jeje");
                System.out.println("Hola " + nombre + ", tienes " + edad_usuario + " años.");
        }else{
                System.out.println("El usuario es menor de edad.");
                System.out.println("Hola " + nombre + ", tienes " + edad_usuario + " años.");
        }
        sc.close();
    }
}
