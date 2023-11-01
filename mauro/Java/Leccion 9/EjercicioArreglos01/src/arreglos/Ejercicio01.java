package arreglos;

import java.util.Scanner;
/*
    Ejercicio 1: Leer 5 números, guardarlos en un arreglo y
    mostrarlos en el mismo orden introducidos.
*/

public class Ejercicio01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float arreglos[] = new float [5];
        
        System.out.println("Guardando los datos en el arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1) + ". Digite un número: ");
            arreglos[i] = entrada.nextFloat();
        }
        
        System.out.println("\nImprimir los elementos del arreglo");
        for(float i:arreglos){
            System.out.println(i + " ");
        }
        System.out.println("\n");
    }
}
