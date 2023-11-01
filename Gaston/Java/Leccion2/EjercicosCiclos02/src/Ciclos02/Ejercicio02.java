/*
Ejercicio2: leer un numero e indicar si es positivo o neegativo. el proceso se repetira hasta que se introduzca 
un cero 0  ESTE EJERCICIO ES CON LA CLASE SCANNER
 */
package Ciclos02;

import java.util.Scanner;


public class Ejercicio02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("digite un numero");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero > 0){
                System.out.println("el numero "+numero+"es positivo");
            }
            else{
                System.out.println("el numero "+numero+"es negativo");
            }
            System.out.println("digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("el numero "+numero+"finaliza el programa ");
    }
 
}
