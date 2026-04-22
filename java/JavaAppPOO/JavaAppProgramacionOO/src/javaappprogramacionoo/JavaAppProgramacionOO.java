/*@author Paula de Juan  
Creando Programa con Clases y Objetos */

package javaappprogramacionoo;
import java.util.Scanner;

public class JavaAppProgramacionOO {

   public static void main(String[] args) {
       
                    Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 2; i++) {

            System.out.println("=== Cliente " + (i + 1) + " ===");

            System.out.print("Nombre: ");
            String nombre = sc.nextLine();

            System.out.print("Apellido: ");
            String apellido = sc.nextLine();

            System.out.print("Telefono: ");
            String telefono = sc.nextLine();

            System.out.print("Edad: ");
            int edad = sc.nextInt();
            sc.nextLine();

            System.out.print("Direccion: ");
            String direccion = sc.nextLine();

            System.out.print("Pedido ID: ");
            int pedido_id = sc.nextInt();

            System.out.print("Ticket medio: ");
            int ticket_medio = sc.nextInt();
            sc.nextLine();

            Cliente cliente = new Cliente(nombre, apellido, telefono, edad, direccion, pedido_id, ticket_medio);

            cliente.mostrarCliente();
        }

        sc.close();
    }
}