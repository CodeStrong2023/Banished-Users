/*
ejercicio2: leer 5 numeros, guardados en un arreglo
y mostramos en el orden inverso al introducidos.
*/
package arreglos_ejercicio_2;

import java.util.Scanner;

public class Arreglos_Ejercicio_2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros [] = new float [5];
        System.out.println("guardando los elementos del arreglo");
        for(int i=0;i<5;i++){
            System.out.println((i+1)+". digite un numero: ");
            numeros[i]= entrada.nextFloat();
            
        }
        System.out.println("\nImprimimos los elementos del arreglo");
        for(int i=4;i>0;i--){
            System.out.println(" "+numeros[i]); 
        }
        System.out.println("\n");
    }
}