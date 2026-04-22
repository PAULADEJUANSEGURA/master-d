/*@author Paula de Juan */
package javaapp;
import java.util.Scanner;

public class JavaApp {

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
        }else {
                System.out.println("El usuario es menor de edad");
                System.out.println("Hola " + nombre + ", tienes " + edad_usuario + " años.");
        }
        sc.close();
    }
}
