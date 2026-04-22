/*@author Paula de Juan  
Creando Programa con Clases y Objetos */

package javaappprogramacionoo;

public class Cliente {
    
          private static int contador = 1; // contador global
    
            int cliente_id;
            String nombre;
            String apellido;
            String telefono;
            int edad;
            String direccion;
            int pedido_id;
            int ticket_medio;
          
                // Constructor parametrizado:
                // Constructor SIN cliente_id
                        public Cliente(String nombre, String apellido, String telefono, int edad, String direccion, int pedido_id, int ticket_medio) {
                                        this.cliente_id = contador++; // autoincremento
                                        this.nombre = nombre;
                                        this.apellido = apellido;
                                        this.telefono = telefono;
                                        this.edad = edad;
                                        this.direccion = direccion;
                                        this.pedido_id = pedido_id;
                                        this.ticket_medio = ticket_medio;
    }

            
            
            void mostrarCliente(){
                System.out.println("Cliente ID = " + cliente_id);
                System.out.println("Nombre y Apellido = " + nombre + " " + apellido);
                System.out.println("Telefono = " + telefono);
                System.out.println("Edad = " + edad);
                System.out.println("Dirección de envío = " + direccion);
                System.out.println("Pedido ID = " + pedido_id);
                System.out.println("Ticket medio del Cliente = " + ticket_medio);                       
                System.out.println("Fin Cliente: ----------------------------");
            }
    
}
