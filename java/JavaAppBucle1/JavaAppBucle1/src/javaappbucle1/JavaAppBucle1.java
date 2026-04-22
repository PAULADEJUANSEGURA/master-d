/*@author Paula de Juan */
package javaappbucle1;
import java.util.Scanner;

public class JavaAppBucle1 {

   public static void main(String[] args) {
        /* Programa que muestra la tabla de multiplicar de un numero dado: */
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce un numero para calcular su tabla de multiplicar: ");
        int numero_para_tabla = sc.nextInt();
        int operador = 0;
        while(operador <=10){
                int resultado = numero_para_tabla * operador;
                System.out.println(numero_para_tabla + "x" + operador + "="+ resultado);
                operador++;       
        }
        sc.close();
   }
}
