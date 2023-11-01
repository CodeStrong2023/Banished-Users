package Ciclos08;

import java.util.Scanner;

/*
    Ejercicio 8: Pedir un número N, y mostrar todos los números
    del 1 al N.
*/
public class Ejercicio8 {
    public static void main(String[] args) {
        // Pedimos el numero
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número: ");
        int numero = Integer.parseInt(entrada.nextLine());
        
        // Ciclo para mostar los n desde 1
        int i = 1;
        while(i <= numero){
            System.out.println(i);
            i++;
        }
        
    }
}
